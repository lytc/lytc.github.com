# Ly Tran — Engineering, in practice

Personal portfolio at **https://lytc.github.io**, published from `lytc/lytc.github.com` (the historical GitHub Pages repository). This is the personal `lytc` account.

The site is static HTML, CSS, and a small amount of JavaScript. There are no package dependencies, tracking scripts, external fonts, or visitor API calls.

## Edit and build

- `content/work.json`: the seven case studies.
- `data/evidence.json`: public product sources, chronology methods, and selected secondary contribution links.
- `tools/build.py`: page templates, homepage content, evidence page, contact details.
- `assets/site.css`: responsive layout and original explanatory diagrams.
- `assets/site.js`: accessible approach tabs.

Run `python3 tools/build.py` from the repository root to regenerate the committed HTML. Then preview with `python3 -m http.server 4173 --bind 127.0.0.1` and open `http://127.0.0.1:4173`.

GitHub Pages serves the root of the `master` branch. `.nojekyll` keeps the static output intact. The original site remains in Git history. Other project Pages remain hosted by their own repositories.

## Content boundaries

Career dates and product claims include source scope and verification dates. Private professional work is described in generalized form. No company source code, private evidence files, internal messages, or operational metrics belong in this repository. Explanatory diagrams are original illustrations, not product screenshots.

The contact email and phone number were supplied by the owner for public display. Recent engineering work is described as AI-assisted; adoption and measured effectiveness are kept separate.
