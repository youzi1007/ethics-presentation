# Ethics project concept prototypes

Two independent static websites in one GitHub Pages repository.

- [`privacy/`](privacy/): **The Price of Convenience**, Basketfield privacy simulation (V5). Includes a real-photography storefront, simulated cookie controls, customer profiling reveal, dark internal data scientist console, and final receipt.
- [`hiring/`](hiring/): **The Perfect Candidate**, original hiring-scoring concept (unchanged).
- [`index.html`](index.html): simple launcher with one link to each prototype.

## Publish

Upload the repository contents to a GitHub repository, then configure **Settings → Pages → Deploy from a branch → main → /(root)**. The home page will be `https://USERNAME.github.io/REPOSITORY/` and individual links `/privacy/` and `/hiring/`.

The Basketfield demo currently loads real photos from Unsplash, with attribution in [PHOTO_SOURCES.md](PHOTO_SOURCES.md). To avoid third-party image requests before publishing, run `python3 download_photos.py` on your own computer with internet access, then commit the `privacy/assets/` folder along with the updated HTML. This is recommended for an actual privacy-themed presentation.

No AI-generated merchandise images are used. Pricing and storefront branding are fictional. There is no backend and visitor choices remain in the browser tab. External photo requests are disclosed in the site until localized.