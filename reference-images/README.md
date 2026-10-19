# Reference images

**What this is:** photographs we use to model buildings (facades, materials, windows, roofs). Images are NOT committed: most belong to the university or a photographer. Only the log, `IMAGE-LOG.csv`, is public.

**Where they come from**
1. **Northeastern Digital Repository / digital collections** (login required, hundreds of thousands of photos). Search by building name or street name.
2. **Archives and Special Collections, University Photograph collection (A103)**, Series 11 "Physical Plant": one folder per building. These are physical folders, not digitized; the finding aid is in `data/tables/archives_A103_series11_physical_plant.csv`. Ask the University Archivist about scans. Reproduction note on the collection: "Copyright restrictions may apply."
3. Our own photographs of the building.

**How to add one**
1. Save it as `reference-images/<building-code>/<code>_<short-description>_<NN>.jpg`.
2. Add a row to `IMAGE-LOG.csv`: building, file, where it came from (collection and item id or URL), year taken if known, which face of the building it shows, and its rights.
3. If an image cannot be saved, log it anyway with the URL so the next person can find it.
