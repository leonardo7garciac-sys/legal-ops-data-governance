"""Gap-check script for the Legal Ops data processing inventory (RoPA).

Compares docs/ropa.md against the schema snapshots in data/ and against the
RoPA's own completeness rules, and reports where they disagree. This script
reports facts only — presence, absence, and structure — never whether a
finding is a compliance failure. That judgment belongs to the human author.
"""

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ROPA_PATH = REPO_ROOT / "docs" / "ropa.md"
CONTRACT_ANALYTICS_SNAPSHOT_PATH = (
    REPO_ROOT / "data" / "contract_analytics_contracts_snapshot.csv"
)
INTAKE_SNAPSHOT_PATH = REPO_ROOT / "data" / "intake_schema_snapshot.sql"

# Matches an activity heading, e.g. "## 4. Ferramenta de intake jurídico".
ACTIVITY_HEADING_RE = re.compile(r"^## (\d+)\. (.+)$", re.MULTILINE)

# Matches a field bullet, e.g. "- **Prazo de retenção:** texto aqui".
FIELD_LINE_RE = re.compile(r"^- \*\*(.+?):\*\* (.*)$")

# Any line starting with "- **" is expected to be a field bullet. If it
# doesn't match FIELD_LINE_RE, the document's shape has changed in a way
# this parser doesn't understand.
BULLET_START_RE = re.compile(r"^- \*\*")


class RopaStructureError(Exception):
    """Raised when docs/ropa.md no longer matches the expected structure.

    This parser is intentionally strict: it fails loudly instead of
    silently parsing zero activities or zero fields, which would make
    every check below report a false "no gaps found".
    """


@dataclass
class Activity:
    number: int
    title: str
    fields: dict = field(default_factory=dict)


def parse_ropa(text: str) -> list[Activity]:
    headings = list(ACTIVITY_HEADING_RE.finditer(text))
    if not headings:
        raise RopaStructureError(
            "No '## N. Title' activity headings found — the document no "
            "longer looks like a numbered-activity RoPA."
        )

    activities = []
    for i, heading_match in enumerate(headings):
        number = int(heading_match.group(1))
        title = heading_match.group(2).strip()
        block_start = heading_match.end()
        block_end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        block = text[block_start:block_end]

        activity = Activity(number=number, title=title)
        for line in block.splitlines():
            line = line.strip()
            if not line or not BULLET_START_RE.match(line):
                continue
            field_match = FIELD_LINE_RE.match(line)
            if not field_match:
                raise RopaStructureError(
                    f"Activity {number} ({title}): line looks like a field "
                    f"bullet but doesn't match the expected "
                    f"'- **Label:** value' shape: {line!r}"
                )
            label, value = field_match.group(1).strip(), field_match.group(2).strip()
            activity.fields[label] = value

        activities.append(activity)

    return activities


@dataclass
class SchemaField:
    source: str  # snapshot file name, for citing where a field came from
    table: str  # table (SQL) or dataset (CSV) the field belongs to
    column: str


def read_csv_snapshot(path: Path) -> list[SchemaField]:
    """Read column names from a CSV snapshot, skipping '#'-prefixed provenance comments."""
    lines = [
        line for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith("#")
    ]
    header = next(csv.reader(lines))
    return [SchemaField(source=path.name, table="contracts", column=col) for col in header]


# Matches a real column-definition line, e.g. "  counterparty_name text," — deliberately
# requires a recognized column type right after the identifier, so multi-line CHECK/enum
# bodies and comment lines (which don't have that shape) are skipped without needing a
# full SQL parser.
SQL_COLUMN_RE = re.compile(
    r"^\s*([a-z_][a-z0-9_]*)\s+(uuid|text|boolean|timestamptz|date)\b", re.IGNORECASE
)
SQL_ADD_COLUMN_RE = re.compile(
    r"^\s*add column\s+([a-z_][a-z0-9_]*)\s+(uuid|text|boolean|timestamptz|date)\b",
    re.IGNORECASE,
)
SQL_TABLE_RE = re.compile(r"^(?:create table|alter table)\s+(\w+)", re.IGNORECASE)


def read_sql_snapshot(path: Path) -> list[SchemaField]:
    """Read column names from a SQL snapshot of CREATE TABLE / ALTER TABLE statements."""
    fields = []
    current_table = None
    for line in path.read_text(encoding="utf-8").splitlines():
        table_match = SQL_TABLE_RE.match(line.strip())
        if table_match:
            current_table = table_match.group(1)
            continue
        if current_table is None:
            continue
        add_match = SQL_ADD_COLUMN_RE.match(line)
        if add_match:
            fields.append(SchemaField(source=path.name, table=current_table, column=add_match.group(1)))
            continue
        col_match = SQL_COLUMN_RE.match(line)
        if col_match:
            fields.append(SchemaField(source=path.name, table=current_table, column=col_match.group(1)))
    return fields


# --- Check 1: campos a verificar ------------------------------------------------
#
# This check matches schema column names against snake_case tokens that commonly
# indicate personal data, then checks whether a corresponding Portuguese term
# appears anywhere in the RoPA's "Categorias de dados" fields. It is a blunt,
# explicit pattern match, not an inference: it will both miss real personal-data
# columns whose names don't hit a pattern (false negatives) and flag columns that
# aren't personal data at all, such as a boolean flag whose name happens to share
# a token with a pattern (false positives — e.g. a "contains_personal_data" flag
# describes the record, it isn't personal data itself). For that reason this
# check's findings are reported as fields requiring verification, not as
# confirmed gaps: the script narrows where a human has to look, it does not
# decide whether a field is personal data.
PERSONAL_DATA_FIELD_PATTERNS = [
    {"tokens": {"name"}, "ropa_terms": ["nome"]},
    {"tokens": {"email"}, "ropa_terms": ["e-mail", "email"]},
    {"tokens": {"lawyer"}, "ropa_terms": ["advogado"]},
    {"tokens": {"counterparty"}, "ropa_terms": ["contraparte"]},
    {"tokens": {"cpf"}, "ropa_terms": ["cpf"]},
    {"tokens": {"cnpj"}, "ropa_terms": ["cnpj"]},
    {"tokens": {"phone", "telefone"}, "ropa_terms": ["telefone"]},
    {"tokens": {"address", "endereco", "endereço"}, "ropa_terms": ["endereço"]},
]


@dataclass
class FieldsToVerifyResult:
    matched_columns: int  # how many schema columns hit a pattern at all, covered or not
    findings: list  # the subset of those columns whose term wasn't found in the RoPA


def check_fields_to_verify(
    activities: list[Activity], schema_fields: list[SchemaField]
) -> FieldsToVerifyResult:
    """Check 1: schema columns whose name pattern suggests personal data, and
    whose matching Portuguese term is absent from every activity's "Categorias
    de dados" field anywhere in the RoPA (document-wide, not per-activity —
    attributing a column to the one activity that should disclose it needs
    judgment this script doesn't make)."""
    all_categories_text = " ".join(
        activity.fields.get("Categorias de dados", "") for activity in activities
    ).lower()

    matched_columns = 0
    findings = []
    for schema_field in schema_fields:
        column_tokens = set(schema_field.column.lower().split("_"))
        matched_patterns = [
            pattern for pattern in PERSONAL_DATA_FIELD_PATTERNS if column_tokens & pattern["tokens"]
        ]
        if not matched_patterns:
            continue
        matched_columns += 1
        # Covered if ANY matched pattern's Portuguese term appears anywhere in the
        # RoPA — a column can match more than one pattern (e.g. "counterparty_name"
        # matches both "name" and "counterparty"), and only one needs to be covered.
        covered = any(
            term.lower() in all_categories_text
            for pattern in matched_patterns
            for term in pattern["ropa_terms"]
        )
        if not covered:
            findings.append(
                {
                    "source": schema_field.source,
                    "table": schema_field.table,
                    "column": schema_field.column,
                    "matched_terms": [term for pattern in matched_patterns for term in pattern["ropa_terms"]],
                }
            )
    return FieldsToVerifyResult(matched_columns=matched_columns, findings=findings)


# --- Check 2: retenção sem fundamentação -----------------------------------------

UNDEFINED_MARKER = "[A DEFINIR"

# A cited norm looks like one of these — an article number, a numbered law or
# decree, or the named ANPD resolution. Absence of all of these from a "Prazo de
# retenção" field means no norm is cited, which CLAUDE.md's hard rule forbids.
CITATION_RE = re.compile(
    r"art\.\s*\d+|Lei\s*\d|Decreto\s*\d|Resolução\s*CD/ANPD", re.IGNORECASE
)


def check_retention_without_grounding(activities: list[Activity]) -> list[dict]:
    """Check 2: activities whose "Prazo de retenção" is marked [A DEFINIR], or
    whose stated period cites no identifiable norm."""
    findings = []
    for activity in activities:
        value = activity.fields.get("Prazo de retenção", "")
        if UNDEFINED_MARKER in value:
            reason = "prazo marcado [A DEFINIR]"
        elif not CITATION_RE.search(value):
            reason = "nenhuma norma identificável citada no texto do prazo"
        else:
            continue
        findings.append({"activity": activity, "reason": reason})
    return findings


# --- Check 3: transferência internacional sem mecanismo --------------------------

NOT_APPLICABLE_RE = re.compile(r"^n[ãa]o aplic[áa]vel", re.IGNORECASE)

# A legitimizing mechanism for international transfer (LGPD art. 33) looks like
# one of these terms.
TRANSFER_MECHANISM_RE = re.compile(
    r"art\.\s*33|cl[áa]usula|decis[ãa]o de adequa[çc][ãa]o|certifica[çc][ãa]o|selo"
    r"|norma corporativa|consentimento",
    re.IGNORECASE,
)


def check_international_transfer_without_mechanism(activities: list[Activity]) -> list[dict]:
    """Check 3: activities that record an international transfer (i.e. the field
    doesn't start with "não aplicável") without naming a legitimizing mechanism."""
    findings = []
    for activity in activities:
        value = activity.fields.get("Transferência internacional", "")
        if NOT_APPLICABLE_RE.match(value.strip()):
            continue
        if not TRANSFER_MECHANISM_RE.search(value):
            findings.append({"activity": activity})
    return findings


# --- Check 4: campos obrigatórios ausentes ----------------------------------------

REQUIRED_FIELDS = [
    "Finalidade",
    "Categorias de titulares",
    "Categorias de dados",
    "Base legal",
    "Prazo de retenção",
    "Informação ao titular (art. 9º)",
    "Compartilhamentos",
    "Transferência internacional",
    "Medidas de segurança",
    "Nível de risco",
]


def check_missing_required_fields(activities: list[Activity]) -> list[dict]:
    """Check 4: activities missing any of the fields every entry is supposed to carry."""
    findings = []
    for activity in activities:
        for required_field in REQUIRED_FIELDS:
            if required_field not in activity.fields:
                findings.append({"activity": activity, "field": required_field})
    return findings


# --- Report -----------------------------------------------------------------------


def activity_label(activity: Activity) -> str:
    return f"Atividade {activity.number} ({activity.title})"


def print_section(title: str, lines: list[str], empty_message: str, count_label: str) -> None:
    print(f"=== {title} ===")
    if not lines:
        print(empty_message)
    else:
        for line in lines:
            print(f"- {line}")
    print(f"{count_label}: {len(lines)}")
    print()


def build_report(activities: list[Activity], schema_fields: list[SchemaField]) -> int:
    fields_to_verify = check_fields_to_verify(activities, schema_fields)
    retention_findings = check_retention_without_grounding(activities)
    transfer_findings = check_international_transfer_without_mechanism(activities)
    missing_field_findings = check_missing_required_fields(activities)

    print("=== Campos a verificar ===")
    # Reported separately from the finding count below: a matched-columns count of
    # zero means the patterns never fired on these snapshots; a findings count of
    # zero with matched_columns > 0 means they fired and every match was covered.
    # The two read the same in the summary line alone, so both are shown here.
    print(f"Colunas correspondentes a algum padrão: {fields_to_verify.matched_columns}")
    if not fields_to_verify.findings:
        print("Nenhum campo a verificar.")
    else:
        for f in fields_to_verify.findings:
            print(
                f"- {f['source']} ({f['table']}.{f['column']}): não localizado nenhum dos termos "
                f"{f['matched_terms']} em nenhuma 'Categorias de dados' do RoPA"
            )
    print(f"Total de campos a verificar: {len(fields_to_verify.findings)}")
    print()
    print_section(
        "Retenção sem fundamentação",
        [f"{activity_label(f['activity'])}: {f['reason']}" for f in retention_findings],
        "Nenhum gap encontrado.",
        "Total de gaps",
    )
    print_section(
        "Transferência internacional sem mecanismo",
        [
            f"{activity_label(f['activity'])}: transferência internacional registrada sem "
            f"citação de mecanismo legitimador"
            for f in transfer_findings
        ],
        "Nenhum gap encontrado.",
        "Total de gaps",
    )
    print_section(
        "Campos obrigatórios ausentes",
        [f"{activity_label(f['activity'])}: campo '{f['field']}' ausente" for f in missing_field_findings],
        "Nenhum gap encontrado.",
        "Total de gaps",
    )

    total = (
        len(fields_to_verify.findings)
        + len(retention_findings)
        + len(transfer_findings)
        + len(missing_field_findings)
    )
    print(f"=== Resumo ===")
    print(f"Total geral (campos a verificar + gaps): {total}")
    return total


def main() -> int:
    try:
        ropa_text = ROPA_PATH.read_text(encoding="utf-8")
        activities = parse_ropa(ropa_text)
    except RopaStructureError as exc:
        print(f"ERRO: estrutura do RoPA mudou de forma inesperada: {exc}", file=sys.stderr)
        return 2

    schema_fields = read_csv_snapshot(CONTRACT_ANALYTICS_SNAPSHOT_PATH) + read_sql_snapshot(
        INTAKE_SNAPSHOT_PATH
    )

    total = build_report(activities, schema_fields)
    return 1 if total > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
