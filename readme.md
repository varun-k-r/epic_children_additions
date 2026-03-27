# Cross-Epic Genealogy Dataset

This repository extends https://github.com/soodoku/epic_children by adding additional genealogy datasets in a common schema.

> **Note:** This data may contain extraction errors, miscoded relationships, or inconsistencies with the source texts. A second round of verification against the primary sources is planned. Use with appropriate caution.

---

## Datasets

- `epic_children.csv` — original cross-epic genealogy (32 traditions)
- `mahavamsa.csv` — Sinhala royal genealogy
- `south_indian_traditions.csv` — Tamil Hindu (Ziegenbalg) genealogy
- `epic_prayer_for_children.csv` — prayers for children across traditions

Each dataset is derived from a single primary source and preserved without cross-source harmonization.

---

## Wide vs Long Form

Each dataset is provided in two formats:

- **Wide form** (`*.csv`)
  - one row per couple
  - schema-compatible with `epic_children.csv`
  - can be appended directly

- **Long form** (`*_long.csv`)
  - one row per child
  - tidy-compliant
  - can be appended to `epic_children_long.csv`

---

## epic_children_long

`epic_children_long.csv` is the fully appended dataset combining:

- original `epic_children` (32 traditions)
- Mahavamsa
- South Indian Traditions (Ziegenbalg)

2,366 rows across 34 traditions. Each row represents one child. No further merging is required.

---

## Schema

All datasets follow the `epic_children` schema:
https://github.com/soodoku/epic_children/tree/main/data

Namespace prefixes ensure uniqueness:
- `mahavamsa::`
- `ziegenbalg_south_indian::`

---

## Structure

```
readme.md

/data
  epic_children.csv
  mahavamsa.csv
  south_indian_traditions.csv
  epic_prayer_for_children.csv

/data_long
  epic_children_long.csv
  mahavamsa_long.csv
  south_indian_traditions_long.csv

/docs
  mahavamsa_readme.md
  mahavamsa_codebook.md
  tamil_tradition_readme.md
  tamil_traditions_codebook.md
```

---

## Notes

- No inferred relationships are added
- Missing values are left empty

---

## Sources

- Mahavamsa — Still (1907), Geiger (1912)
- South Indian — Ziegenbalg (1869)
