# Ziegenbalg South Indian Genealogy Dataset — Codebook

## Source

Bartholomaeus Ziegenbalg, *Genealogy of the South-Indian Gods* (1869), translated by G.J. Metzger.

Primary sources:

* OCR text (archive.org)
* PDF (Wikimedia Commons)

---

## Unit of Observation

### Wide form (`south_indian_traditions.csv`)

Each row represents one **couple** (a divine union and its offspring).

### Long form (`south_indian_traditions_long.csv`)

Each row represents one **child**.

Childless couples retain one row with empty:

* `child_name`
* `child_sex`
* `child_order`

This format is tidy-compliant:

* one observation per row
* one variable per column
* one value per cell

---

## Schema

Conforms to the cross-epic genealogy schema:
[https://github.com/soodoku/epic_children/tree/main/data](https://github.com/soodoku/epic_children/tree/main/data)

Namespace prefix: `ziegenbalg_south_indian::`

---

## Variables — Wide Form

| Variable        | Type        | Description                                           |
| --------------- | ----------- | ----------------------------------------------------- |
| `parents`       | string      | Couple identifier (e.g., "Isvara & Parvati")          |
| `husband`       | string      | Male deity (Title Case)                               |
| `wife`          | string      | Female deity (Title Case)                             |
| `husband_id`    | string      | Namespaced ID (`ziegenbalg_south_indian::snake_case`) |
| `wife_id`       | string      | Namespaced ID (`ziegenbalg_south_indian::snake_case`) |
| `n_sons`        | numeric     | Number of sons                                        |
| `sons`          | string      | Comma-separated list of sons                          |
| `n_daughters`   | numeric     | Number of daughters                                   |
| `daughters`     | string      | Comma-separated list of daughters                     |
| `n_unknown_sex` | numeric     | Children with unspecified sex                         |
| `epic`          | string      | Dataset tag: `ziegenbalg_south_indian`                |
| `source`        | string      | Chapter reference (e.g., "Part II Ch.I")              |
| `comments`      | string      | Notes, ambiguities, lineage context                   |
| `row_type`      | categorical | Always `couple`                                       |
| `historicity`   | categorical | Always `mythological`                                 |
| `family_id`     | string      | Family grouping identifier                            |

---

## Variables — Long Form (additional columns)

| Variable      | Type        | Description                           |
| ------------- | ----------- | ------------------------------------- |
| `child_name`  | string      | Name of child                         |
| `child_sex`   | categorical | `male`, `female`, `unknown`, or empty |
| `child_order` | numeric     | Birth order within union (1-indexed)  |

The long form replaces:

* `n_sons`, `sons`
* `n_daughters`, `daughters`
* `n_unknown_sex`

---

## Validation Summary — Wide Form

* **38 rows**, **16 columns**
* All rows are `row_type = couple`
* No duplicate `family_id`
* No mismatches between counts (`n_sons`, `n_daughters`) and listed names

---

## Validation Summary — Long Form

* **53 rows** (42 named children + 11 childless couple rows)
* Fully tidy-compliant
* Includes **childless couples** as empty child rows
* No duplicated parent-child combinations

---

## Descriptive Statistics

* **Total named children**: 42
* **Male**: 36
* **Female**: 6
* **Unknown**: 0

### Sex Ratio

* **6.0 males per female**

- **6,000 males per 1,000 females**

Sex ratio calculated as (males / females) × 1,000; unknown-sex children excluded.
---

## OCR and Extraction Validation

Because the source is a scanned OCR text, the extraction was validated using systematic page sampling.

Approximately every 5th page was reviewed across the text to verify that:

* explicitly stated marriages were captured
* explicitly stated children were captured
* core genealogy from the diagram was preserved
* no OCR artifacts introduced missing or duplicated relationships

No missing genealogical relationships were identified within sampled pages. Non-genealogical descriptive content (e.g., iconography, mythology) was intentionally excluded.

---

## Suggested Replication and Validation Checks

Users are encouraged to independently verify the dataset using reproducible sampling strategies.

### 1. Systematic Page Sampling

Select a fixed interval and review the corresponding pages in the source text. For example:

* every 5th page (used in this dataset)
* every 7th or 10th page (independent replication)

For each sampled page, verify that:

* all explicitly stated marriages are present in the dataset
* all explicitly stated children are captured
* no relationships are omitted or duplicated

Using a different interval ensures validation is not tied to the original sampling pattern.

---

### 2. Offset Sampling

Repeat sampling with a shifted starting point:

* e.g., pages 3, 10, 17, 24...

This reduces alignment with structural patterns in the text.

---

### 3. Reverse Lookup Validation

Select families from the dataset and locate them in the source text.

Verify that:

* relationships exist exactly as recorded
* no additional children or spouses are omitted

---

### 4. Diagram Consistency Check

Cross-check sampled entries against the genealogy diagram (page 1), ensuring:

* major lineage nodes are present
* core parent-child structures are preserved

---

### 5. OCR Sensitivity Check

Inspect sampled pages for:

* broken names
* merged words
* character artifacts

Confirm these did not propagate into the dataset.

---

## Cleaning Notes

1. Names standardized to Title Case; IDs in snake_case
2. No inferred children added — only explicit textual relationships
3. Multiple traditions not harmonized (single-source extraction)
4. Some deities have multiple names; alias merging is partial
5. Childless divine couples retained for structural completeness
6. Unknown-sex children left empty (not imputed)

---

## Data Limitations

* Single 19th-century ethnographic source
* OCR noise possible

---

## Relationship to Other Datasets

Fully compatible with:

* `mahavamsa.csv`
* `epic_children.csv`

Can be appended using:

* `husband_id`
* `wife_id`
* `family_id`

---

## Citation

Ziegenbalg, Bartholomaeus.
*Genealogy of the South-Indian Gods.*
Translated by G.J. Metzger. 1869.
