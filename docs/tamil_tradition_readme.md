# Ziegenbalg South Indian Genealogy Dataset

## Source

Bartholomaeus Ziegenbalg, *Genealogy of the South-Indian Gods* (1869), translated by G.J. Metzger.

Primary sources:

* OCR text (archive.org)
* PDF (Wikimedia Commons)

---

## Overview

Family relationships from the Tamil Hindu pantheon as documented by Ziegenbalg, the first Protestant missionary in India. Covers the Parabaravastu (Supreme Being), the Mummurttis (Isvara/Siva, Vishnu, Brahma), their consorts and children, the Gramadevatas (tutelar deities), Devas, and selected epic characters from the Ramayana and Mahabharata as retold in this text.

---

## Descriptive Statistics

| Metric               | Value |
|---------------------|-------|
| Families (wide rows) | 38 |
| Sons                 | 36 |
| Daughters            | 6 |
| Unknown sex          | 0 |
| Total children       | 42 |

### Sex Ratio

- Male-to-female ratio: **6.0**

This reflects strong patrilineal bias and potentially selective recording of male lineage in the source text.

---

## Wide vs Long Form

**`south_indian_traditions.csv`** — Wide form (one row per couple). Matches `epic_children.csv`.

**`south_indian_traditions_long.csv`** — Long form (one row per child, tidy-compliant).

---

## Schema

Conforms to the cross-epic genealogy schema:
https://github.com/soodoku/epic_children/tree/main/data

Namespace prefix: `ziegenbalg_south_indian::`

---

## Validation Summary — Wide Form

* **38 rows**, **16 columns**
* All rows are `row_type = couple`
* All rows are `historicity = mythological`
* No duplicate `family_id`
* No mismatches between counts (`n_sons`, `n_daughters`) and listed names

---

## Validation Summary — Long Form

* **53 rows** (42 named children + 11 childless couple rows)
* 36 male, 6 female
* Tidy-compliant: no multi-value cells
* No duplicated parent-child combinations

---

## Cleaning Notes

1. Names standardized to Title Case; IDs in snake_case
2. No inferred children added — only explicit textual relationships
3. Multiple traditions not harmonized (single-source extraction)
4. Some deities have multiple names; alias merging is partial
5. Childless divine couples retained for structural completeness

---

## Data Limitations

* Single 19th-century ethnographic source
* OCR noise possible in source text
* Female underrepresentation likely structural

---

## Relationship to Other Datasets

Fully compatible with:

* `mahavamsa.csv`
* `epic_children.csv`

Can be appended or merged using:

* `husband_id`
* `wife_id`
* `family_id`

---

## Citation

Ziegenbalg, Bartholomaeus.
*Genealogy of the South-Indian Gods.*
Translated by G.J. Metzger. 1869.
