# Reference images

**What this is:** photographs we use to model buildings (facades, materials, windows, roofs). Images are NOT committed: some belong to the university or a photographer, and our own are kept private for now. Only the log, `IMAGE-LOG.csv`, is public.

**Where they come from**
1. **Our own photos.** The best source for any building that exists today. How to take them: `docs/CAPTURE-GUIDE.md`. Anyone can borrow the GoPro and photograph the building we are working on.
2. **Northeastern Digital Repository Service (DRS), collection `neu:6012`.** The digitized part of the Northeastern University photograph collection (A103): https://repository.library.northeastern.edu/collections/neu:6012. Searching it by building name gives small, usable result sets. Titles such as "Exterior of Ell Hall" and "Floor plans for the first floor of Richards Hall" are the ones we want; many hits are people at events. `data/tables/drs_photo_index.csv` is a metadata-only index of hits for every Boston-campus building (made by `scripts/index_drs.py`), with a `kind` column guessing view / drawing / other. The guess is by title and is rough.
3. **University Archives, A103 Series 11 "Physical Plant".** Paper folders, one per building, not scanned. Finding aid: `data/tables/archives_A103_series11_physical_plant.csv`. Collection note: "Copyright restrictions may apply." Ask the University Archivist about scans.

**How to add one**
1. Save it as `reference-images/<building-code>/<code>_<short-description>_<NN>.jpg`.
2. Add a row to `IMAGE-LOG.csv`: building, file, where it came from (collection and item id or URL), year taken if known, which face it shows, and its rights.
3. For DRS images, check the item's own page for its rights statement first. If an image can't be saved, log its URL anyway.
