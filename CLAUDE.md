# CLAUDE.md

Project conventions for this repository. Follow these before writing any code, data, or docs.

## Purpose

This is a Legal Operations portfolio project — a data processing inventory (RoPA, Registro de
Operações de Tratamento, art. 37 LGPD) for the legal department of Corvina Software Ltda., a
demonstration artifact for job applications, not production code.

## Fictional company

All synthetic data and documentation refer to a single fictional company, the same one used in
the sibling projects `legal-ops-contract-analytics` and `legal-ops-intake`:

- **Corvina Software Ltda.** — B2B SaaS company
- 400 employees
- In-house legal team of 4 lawyers
- Roughly 150 contracts processed per quarter

## Scope of the inventory

The RoPA covers the **legal department only**, not the whole company:

- Contract management
- Litigation
- Compliance
- The intake tool itself (`legal-ops-intake`)
- External counsel relationships

## Language

- **RoPA and the retention reference are written in Portuguese.** They reproduce Brazilian legal
  terminology that does not translate cleanly — a legal basis is cited as "art. 7º, VI, LGPD",
  not as an English paraphrase.
- **README, code, comments, and commit messages are in English.**

## Legal grounding (hard rule)

Every retention period must cite the specific norm that produces it (statute, regulation, or
internal policy with its own justification). A retention period with no legal grounding is not
acceptable in this project — that is the specific failure this artifact exists to avoid.

## Legal basis citations

Legal bases are cited with the specific item, not just the article: "art. 7º, V (execução de
contrato)", never bare "art. 7º".

## No real personal data

No real personal data appears anywhere in this repository. The inventory describes categories of
data (e.g. "dados cadastrais de contraparte") — never actual data.

## Scope boundary

Never write legal conclusions or risk assessments of your own — in code, comments, docs, or
commit messages. The human author writes those.

## Commits

- Follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`, etc.).
- One commit per logical step.
- Reference the relevant GitHub issue in each commit message, e.g. `docs: add RoPA entry for contract lifecycle (#3)`.

## Environment

- Windows with PowerShell.
- Python is invoked as `py`.

## Folder structure

- `docs/` — the inventory (RoPA), retention reference, and comparison docs (Portuguese)
- `src/` — the gap-check script (Python, English)
- `data/` — schema snapshots the gap-check script reads
