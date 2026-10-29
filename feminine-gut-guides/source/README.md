# Feminine Gut guide series — source

`content.py` holds the wording, `build.py` turns it into styled HTML, `render.js`
prints each guide to a Letter-size PDF with Chromium/Playwright.

```
python3 build.py && python3 plate.py && node render.js   # outputs html/, pdf/, png/ next to the scripts
```

Edit the wording in `content.py` only; the look lives in the CSS inside `build.py`.
Brand colors match `BRAND-COLORS.md`. Fonts: Cormorant Garamond + Jost (Google Fonts).
