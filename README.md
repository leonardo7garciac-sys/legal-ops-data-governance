# Legal Ops Data Governance

A processing inventory — the registro das operações de tratamento required by
art. 37, LGPD — and a retention framework for the legal department of Corvina
Software Ltda., a fictional Brazilian B2B SaaS company.
This README borrows "RoPA" — Records of Processing Activities, the GDPR art. 30 term —
as shorthand for the Brazilian instrument. Corvina, its processing operations, and
every dataset referenced in this repository are fictional. No real personal data
appears anywhere in this repository.

## Relationship to the sibling repositories

The RoPA describes the processing behind two sibling projects:

- [legal-ops-contract-analytics](https://github.com/leonardo7garciac-sys/legal-ops-contract-analytics)
- [legal-ops-intake](https://github.com/leonardo7garciac-sys/legal-ops-intake)

`data/` holds versioned snapshots of each sibling repository's data model — a CSV
snapshot of the contract analytics dataset and a SQL snapshot of the intake tool's
schema. Each snapshot file carries its own provenance and staleness header, stating
which repository and path it was copied from. These are point-in-time copies, not live
reads: a schema or data change in a sibling repository does not propagate here
automatically, and each snapshot must be re-copied by hand when its source changes.

## Repository contents

- `docs/ropa.md` — the processing inventory itself, in Portuguese: eight processing
  activities of the legal department, each with purpose, data subjects, data
  categories, legal basis, retention period, and the other fields this project has
  adopted as its own convention. Art. 37, LGPD imposes the duty to keep the record but
  leaves its minimum content open — unlike art. 30, GDPR, which enumerates it; see
  `docs/comparativo-lgpd-gdpr.md`, section 1. Primary document for a legal or
  compliance reader.
- `docs/retencao.md` — a retention period reference, in Portuguese: a table of the
  norms (Código Civil, CPC, CTN, Lei 12.846/2013, etc.) that ground each retention
  period cited in the RoPA, plus a "Lacunas" section listing the periods still without
  a norm.
- `docs/comparativo-lgpd-gdpr.md` — a comparison, in Portuguese, of LGPD and GDPR
  limited to the points where the two regimes diverge in a way that changes what a
  company must actually do (registration duty, legal bases, incident notification,
  international transfer).
- `src/check_gaps.py` — the gap-check script, in English: reads `docs/ropa.md` and the
  `data/` snapshots and reports structural gaps. For anyone maintaining the RoPA.
- `data/contract_analytics_contracts_snapshot.csv`, `data/intake_schema_snapshot.sql`
  — the versioned schema/data snapshots described above, read by `check_gaps.py`.
- `CLAUDE.md` — project conventions (scope, language, citation format, commit style).

## Running the gap check

Requires Python 3.9+ (the script uses builtin generic annotations); tested on 3.13.
From the repository root:

```
py src/check_gaps.py
```

The script takes no arguments and reads exactly three files: `docs/ropa.md`,
`data/contract_analytics_contracts_snapshot.csv`, and `data/intake_schema_snapshot.sql`.
It performs four checks:

1. **Campos a verificar** — cross-references column names in the `data/` schema
   snapshots against the RoPA's "Categorias de dados" text, flagging schema fields with
   no apparent counterpart in the inventory.
2. **Retenção sem fundamentação** — flags any activity whose "Prazo de retenção" is
   marked `[A DEFINIR]` or cites no recognizable norm.
3. **Transferência internacional sem mecanismo** — flags any activity that records an
   international transfer without citing a legitimizing mechanism.
4. **Campos obrigatórios ausentes** — flags any activity missing one of the ten fields
   this project's RoPA convention requires (art. 37, LGPD does not itself enumerate
   these fields — see `docs/comparativo-lgpd-gdpr.md`, section 1).

Exit codes:

- **0** — no gaps found.
- **1** — one or more gaps found across the four checks above.
- **2** — `docs/ropa.md`'s structure could not be parsed (e.g. missing activity
  headings or a malformed field line) — a parsing failure, not a content finding.

## The open [A DEFINIR] flags

`docs/ropa.md` currently contains 15 `[A DEFINIR]` occurrences. `check_gaps.py` finds
gaps through two distinct routes, which together are why the script currently exits 1:

- **Four explicit markers.** The four retention periods marked
  `[A DEFINIR — fundamentação pendente]`: Ferramenta de intake jurídico, Gestão de
  procurações e poderes, Atendimento a requisições de titulares (arts. 18 a 22), and
  Gestão de incidentes de segurança.
- **One missing citation, found independently of any marker.** The Ferramenta de
  intake jurídico activity's "Transferência internacional" field is not marked
  `[A DEFINIR]` at all — it states the Cloudflare Pages hosting (a global CDN outside
  Brazil) as fact. The script flags it anyway, because it checks every non-"não
  aplicável" transfer field for a citation to a legitimizing mechanism under art. 33,
  LGPD, regardless of whether anyone remembered to mark the field as open.

This is the intended state of the repository, not an unfinished build. Each flag marks
a decision that requires a business or legal owner this repository does not have — a
retention policy the sibling project hasn't set, a norm that doesn't obviously apply,
a hosting fact with no stated legal basis for the transfer it represents. The script's
job is to keep those decisions visible rather than let a placeholder pass as a grounded
period or a legitimized transfer. Resolving them is out of scope here.

## Method note

CLAUDE.md sets a hard rule for this project: every retention period must cite the
specific norm that produces it, and every legal basis must cite the specific item —
"art. 7º, V", not bare "art. 7º". A retention period with no cited norm cannot be
audited or defended, since there is nothing to point to when someone asks why data is
kept for that long; the same is true of a legal basis cited at the article level only,
since LGPD's bases are enumerated by item, not by article.

## Known limitations

- **`check_gaps.py` only validates `docs/ropa.md` structurally.** It does not read or
  validate `docs/comparativo-lgpd-gdpr.md` or `docs/retencao.md`, both of which are
  prose. A statute cited with the wrong article or inciso in either of those two files
  passes undetected — every citation in them was checked by hand, not by the script.
- **The script's marker check catches 4 of the 15 `[A DEFINIR]` occurrences in
  `docs/ropa.md`.** The other 11 — open questions about "Informação ao titular",
  "Relatório de impacto", and the encarregado field in the preamble — are tracked only
  in the document text. The script does not check those fields at all.
- **The snapshots in `data/` go stale silently.** Nothing re-copies them automatically
  when the sibling repository's schema changes; the staleness caveat in each header is
  a note to the reader, not an enforced check.
- **The RoPA has no encarregado (DPO) named.** Art. 41, §1º, LGPD requires public
  disclosure of the encarregado's identity and contact details; this inventory has no
  name to record there.
- **The European customer base is a premise introduced only in
  `docs/comparativo-lgpd-gdpr.md`.** It is not stated in `docs/ropa.md`, nor in either
  sibling repository.

## Language note

`docs/ropa.md` and `docs/retencao.md` are written in Portuguese because they reproduce
Brazilian legal terminology that does not translate cleanly. README, code, and commit
messages are in English.
