#!/usr/bin/env python3
"""One-time photo localization for the Basketfield GitHub Pages project.
Run from the repository root: python3 download_photos.py
Uses the real photographs credited in PHOTO_SOURCES.md. No third-party packages.
"""
from pathlib import Path
import urllib.request
import re
root=Path(__file__).resolve().parent
htmlpath=root/'privacy'/'index.html'
content=htmlpath.read_text()
outdir=root/'privacy'/'assets'
outdir.mkdir(exist_ok=True)
photos={
    "tote":"photo-1565072893031-7e6b2dacf296",
    "lamp":"photo-1678819483347-3faeb1e426c0",
    "mug":"photo-1512311734173-51a49c854e78",
    "audio":"photo-1697652974624-470e68497990",
    "book":"photo-1743385779392-cab22721fac6",
    "shoe":"photo-1637437757614-6491c8e915b5",
}
for label, photo_id in photos.items():
    url=f"https://images.unsplash.com/{photo_id}?fm=jpg&fit=crop&w=840&q=78"
    target=outdir/f"{label}.jpg"
    if not target.exists():
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=30) as r:
            data=r.read()
        if not data.startswith((b"\xff\xd8",b"RIFF",b"\x89PNG")):
            raise ValueError(f"Unexpected image format for {label}")
        target.write_bytes(data)
    # Also replace custom intro sizes, matching photo ID rather than query string
    content=re.sub(r"https://images\.unsplash\.com/"+re.escape(photo_id)+r"\?[^\"'<> ]+",f"assets/{label}.jpg",content)
htmlpath.write_text(content)
# All photo requests should now be first-party.
content=htmlpath.read_text()
assert 'images.unsplash.com/photo-' not in content, 'Remote product photos remain'
content=content.replace('This preview currently loads real product photography from Unsplash, so your browser makes normal image requests to Unsplash servers; the photo sources are listed below.', 'Real merchandise photographs are stored locally with this page. No outside image server requests are necessary; the photo sources are listed below.')
content=content.replace('Images are loaded from Unsplash in this ready-to-preview version. For a privacy-preserving GitHub Pages release, run the included photo-download script to store the images locally.', 'Photographs are bundled locally. The source photographers are credited below.')
htmlpath.write_text(content)
print('Localized',len(photos),'real product photos into privacy/assets/. Ready to upload to GitHub Pages.')
