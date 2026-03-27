# Mahavamsa Genealogy Dataset

**This dataset augments [soodoku/epic_children](https://github.com/soodoku/epic_children)**  
The Mahavamsa data follows the same schema and can be appended directly to `epic_children.csv`.

Mahavamsa genealogical data extracted from the **Genealogical Trees of the Kings of Lanka**, compiled by John Still (1907) and published in the *Index to the Mahavamsa*. The authoritative text is Wilhelm Geiger's translation of the Mahavamsa from Pali (1912), with the English translation by Mabel Haynes Bode.

---

## Overview

This dataset covers the two genealogy trees appended to the Mahavamsa (chapters 1–37), spanning from the legendary Mahasammata line of kings (6th century BC) through the reign of King Mahasena (277 AD).

---

## Descriptive Statistics

| Metric               | Value |
|---------------------|-------|
| Families (wide rows) | 64 |
| Sons                 | 73 |
| Daughters            | 13 |
| Unknown sex          | 4 |
| Total children       | 90 |

### Sex Ratio

- Male-to-female ratio: **5.62**
- **5,615 males per 1,000 females**

### Interpretation

The dataset shows a **moderate male skew**, consistent with dynastic genealogies where succession and inheritance are male-dominated but female lineage still plays a critical role in alliance-building and legitimacy.

---

## Wide vs Long Form

**`mahavamsa.csv`** — Wide form (one row per couple). Matches `epic_children.csv`.

**`mahavamsa_long.csv`** — Long form (one row per child, tidy-compliant).

---

## Source Material

Original URL: http://www.budsas.org/ebud/mahavamsa/gene.html  

In case the link rots, the relevant screenshots are preserved below.

### Genealogical Tree I (6th century BC – 52 AD)

![Genealogical Tree I](/figs/genealogy_tree_i.png)  
[View Image](/figs/genealogy_tree_i.png)

### Genealogical Tree II (60 AD – 277 AD)

![Genealogical Tree II](./figs/genealogy_tree_ii.png)  
[View Image](/figs/genealogy_tree_ii.png)

### Title Page

![Genealogy Title](/figs/genealogy_title.png)  
[View Image](/figs/genealogy_title.png)

---

## Validation

The dataset was validated through:

- full transcription of both genealogy trees  
- internal consistency checks (counts vs names)  
- duplicate handling (polygamy and repeated names)  
- structural validation of lineage continuity  

No mismatches were found between listed children and recorded counts.

---

## Schema

Conforms to the cross-epic genealogy schema:  
https://github.com/soodoku/epic_children/tree/main/data  

Namespace prefix: `mahavamsa::`

---

## Historicity

- **Legendary** — early mythological lineages  
- **Semi-historical** — partially corroborated rulers  
- **Historical** — supported by inscriptions, chronicles, and archaeology  

---

## Structure of the Book

The dataset is derived from:

- Genealogical Tree I (early lineage and Buddhist connections)  
- Genealogical Tree II (Anuradhapura royal succession)  

---

## Key Relationships

The trees document the intersection of two major lineages:

### 1. Sinhala royal line

King of Kalinga → King of Vanga → The Lion → Sihabahu → Vijaya I → (via Pandu/Susima) Panduvasudeva → Pandukabhaya → Mutasiva → and onward through the Anuradhapura kings.

The Lion is Suppadevi's husband. Suppadevi is the daughter of the King of Wagu (Vanga in the csv) and the queen of Kalinga. When Suppadevi was born the astrologers proclaimed "One day, this princess will marry a lion, for she possesses an unusually strong passion and desire."  

The Lion and Suppadevi's child is the legendary Sinhabahu (Sihabahu in the csv, literally meaning Lion Armed or the one who had arms like Lion) who features on the Sri Lankan Flag.  

![Sri Lankan Flag](/figs/sinhabahu_flag.png)  
[View Image](/figs/sinhabahu_flag.png)

---

### 2. Sakya/Buddhist line

Jayasena (Mahasammata) → Sihahanu → Suddhodana → Siddhartha (the Buddha)

Connected to the Sinhala line through Amitodana (son of Sihahanu, ancestor of Pandu) and Bhaddakacchana (Sakyan princess, wife of Panduvasudeva).

---

## Data Construction Notes

- trees transcribed manually  
- polygamous unions recorded as separate rows  
- unnamed queens recorded as "Queen"  
- usurpers included as `row_type=usurper`  
- no inferred relationships added  

---

## Citation

Still, John. *Genealogical Trees of the Kings of Lanka.* 1907.  

Geiger, Wilhelm, trans. *The Mahavamsa.* 1912.
