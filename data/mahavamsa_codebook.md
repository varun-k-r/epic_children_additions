# Mahavamsa Genealogy Dataset — Codebook

## Source
Genealogical Trees of the Kings of Lanka (Trees I & II), compiled by John Still (1907), published in the *Index to the Mahavamsa*. Authoritative source: Wilhelm Geiger's translation of the Mahavamsa from Pali (1912), English translation by Mabel Haynes Bode.

## Unit of Observation

### Wide form (`mahavamsa_genealogy.csv`)
Each row represents one **couple** (a marriage/union and its offspring), one **individual with children but no recorded spouse**, or one **usurper** entry.

### Long form (`epic_children_long.csv`)
Each row represents one **child**. Childless couples retain one row with empty `child_name`, `child_sex`, and `child_order` fields. This format is tidy-compliant: one observation per row, one variable per column, one value per cell.

## Schema
Conforms to the cross-epic genealogy schema ([soodoku/epic_children](https://github.com/soodoku/epic_children/tree/main/data)). Namespace prefix: `mahavamsa::`.

## Variables — Wide Form

| Variable | Type | Description |
|---|---|---|
| `parents` | string | Couple label (e.g., "Vijaya I and Kuveni") or single parent name |
| `husband` | string | Male partner / patriarch. Title Case. |
| `wife` | string | Female partner. Empty if unknown. Unnamed wives = "Queen". |
| `husband_id` | string | Namespaced ID: `mahavamsa::snake_case_name` |
| `wife_id` | string | Namespaced ID: `mahavamsa::snake_case_name` |
| `n_sons` | numeric | Count of sons |
| `sons` | string | Comma-separated list of sons' names |
| `n_daughters` | numeric | Count of daughters |
| `daughters` | string | Comma-separated list of daughters' names |
| `n_unknown_sex` | numeric | Count of children of unspecified sex |
| `epic` | string | Tradition tag: `mahavamsa` |
| `source` | string | Specific textual citation (e.g., "Mahavamsa Ch.33") |
| `comments` | string | Contextual notes, reign dates, cleaning decisions |
| `row_type` | categorical | `couple` or `usurper` |
| `historicity` | categorical | `legendary`, `semi-historical`, or `historical` |
| `family_id` | string | Reserved for cross-dataset linking |

## Variables — Long Form (additional columns)

| Variable | Type | Description |
|---|---|---|
| `child_name` | string | Name of the child. Empty if unnamed or childless couple. |
| `child_sex` | categorical | `male`, `female`, `unknown`, or empty (childless couple) |
| `child_order` | numeric | Birth order within this union (1-indexed). Empty for childless. |

The long form drops `n_sons`, `sons`, `n_daughters`, `daughters`, and `n_unknown_sex` — these are replaced by the per-child rows.

## Validation Summary — Wide Form
- **64 rows**, **16 columns**
- **57 couple rows**, **7 usurper rows**
- **73 sons**, **13 daughters**, **4 unknown sex** = **90 total children**
- No n_sons/n_daughters mismatches with actual name counts
- Duplicate husband_ids (polygamy): `mahavamsa::kakavanna_tissa` (2 wives), `mahavamsa::vatta_gamani` (2 wives), `mahavamsa::suddhodana` (2 wives)
- Duplicate child names (different historical individuals): Uttiya (×2), Mahanaga (×2), Queen (×2)
- Historicity: 17 legendary, 11 semi-historical, 36 historical

## Validation Summary — Long Form (full combined dataset)
- **2,313 rows** across **33 epics** (473 from epic_children + 64 mahavamsa, expanded to one child per row)
- **112 mahavamsa rows** (73 male, 13 female, 4 unknown, 22 childless couples)
- Tidy-compliant: no multi-value cells

## Cleaning Notes
1. Sumitta classified as male (son) — he marries Princess of Madha in the tree.
2. Sihahanu's 7 sons follow the tree layout; Pamita listed with brothers.
3. Bhaddakacchana recorded as wife of Panduvasudeva (not daughter of Pandu).
4. Dhotodana = Maya recorded as shown in tree (separate Maya from wife of Suddhodana, or same person in different union).
5. Suddhodana has two wife rows: Maya (mother of Siddhartha) and Pajapati (noted in tree as "married Suddhodana").
6. Amitodana given separate row as father of Pandu (shown with connecting line in tree).
7. Jayasena recorded as lineage head (Mahasammata line, King of Kapilavatthu).
8. Two distinct Gothabhaya figures: Ruhuna line (Tree I) vs Lambakanna (Tree II).
9. Tree II `****` breaks indicate non-familial succession.
10. Unnamed queens recorded as "Queen" in wife/daughters fields.
11. Column `epic_source` in earlier versions was split into `epic` (tradition tag) and `source` (textual citation) to match the cross-epic schema.
