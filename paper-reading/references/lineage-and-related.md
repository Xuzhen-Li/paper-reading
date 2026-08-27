# Authors, labs, and related literature

A methods note that never names the lab or the competing tool is a software changelog. A note that only lists files already in `NOTES_DIR` is a local index, not a reading.

## Authors

From the PDF Author contributions and affiliations, write who did what:

- corresponding author and group (institution, not a biography)
- if the corresponding author is already a known name in the field: **one or two sentences on why they are known** (signature method, dataset, current lab), then at most two sentences on **this paper's** split. Do not paste Author contributions as a roster. Background facts must come from the lab homepage, Scholar, or a tool page — not from memory
- equal-contribution split when the paper states it (experiments vs method vs downstream)
- the method family this group already published (previous version numbers)
- a same-issue or same-week companion if the publisher page or PDF points to one

Keep this in 导读 as **one paragraph immediately after the opening 全景段**, and again in 关联. Do not invent lab politics. Do not park the author paragraph between methods paragraphs.

## Related literature

Search `NOTES_DIR` for the tool, the competitor, and the dataset. Then add papers the PDF actually cites as the comparison or the predecessor, even if there is no local note.

| Kind | Where | How |
|------|-------|------|
| Any published article | `## 关联` | `First author et al. *Journal* year. [10.xxxx/xxxx](https://doi.org/10.xxxx/xxxx)。` then one clause on *why*. **DOI is mandatory.** Local notes are private; a markdown link to `NOTES_DIR` is extra, never a substitute for the DOI. |
| Local note also exists | same line, after the DOI | `[slug](slug.md)` |
| Cited predecessor / competitor, no local note | same | DOI only; do not create a stub note |
| Same-group companion | 导读 + 关联 | name the shared data or shared haplotypes; still include DOI |
| Dataset paper (UKB WGS, HRC, gnomAD, …) | 关联 or 数字速查 | only if the claim uses that resource; still include DOI |

Do not dump the whole reference list. Five to twelve links that change how the result is read are enough. Preprints: use the preprint DOI if that is what the PDF cites.

## What not to do

- Do not write “相关工作很多” without names.
- Do not cite a paper the PDF does not use unless the user asked for a landscape.
- Do not merge two papers’ numbers.
- Do not list a paper in 关联 with only a local-note filename and no DOI.
