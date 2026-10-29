# One-page landscape "Build Your Plate" category chart, rebranded from the
# Food Guide - Build Your Plate PDF. Reuses the series styles from build.py.
import os
from build import CSS, DRAGONFLY, OUT, e

CATS = [
    ("Protein", "100g/day", "Chicken, turkey, grass-fed beef, eggs, fish, lentils, beans.", "At least 30g per meal"),
    ("Nutrients", "", "Leafy greens & cruciferous veggies, root veggies.", "A serving of colorful foods with each meal"),
    ("Fiber", "", "Cooked veggies, leafy greens, sweet potatoes.", "1 cup of cooked veggies with each meal"),
    ("Antioxidants", "", "Berries, carrots, leafy greens, dark chocolate (70%+ cacao).", "A serving of colorful foods with each meal"),
    ("Essential Fatty Acids", "", "Avocados, olive oil, flaxseeds, chia seeds, walnuts, almonds, sunflower seeds.", "Incorporate essential fatty acids and probiotics as needed"),
    ("Probiotics", "if tolerated", "Sauerkraut, kimchi, yogurt (with live cultures), kefir, kombucha.", "Incorporate essential fatty acids and probiotics as needed"),
]

EXTRA = r"""
@page { size: 11in 8.5in; margin: 0; }
.page.land { width:11in; height:8.5in; padding:0.5in 0.6in 0.42in; }
.land .hero { padding:18px 0 0; display:flex; align-items:flex-end; justify-content:space-between; gap:24px; }
.land h1 { font-size:46px; }
.land .body { padding-top:18px; }
.cats { display:grid; grid-template-columns:repeat(6, 1fr); gap:12px; flex:1; }
.cat { display:flex; flex-direction:column; border-radius:16px; overflow:hidden; background:rgba(255,255,255,.8); border:1px solid rgba(200,90,40,.16); box-shadow:0 16px 30px -26px rgba(168,72,30,.6); }
.cat__band { padding:16px 14px 14px; height:1.3in; display:flex; flex-direction:column; justify-content:space-between; }
.cat__n { font-family:var(--serif); font-size:30px; line-height:1; opacity:.7; }
.cat__name { font-family:var(--serif); font-size:21px; font-weight:500; line-height:1.05; margin-top:8px; }
.cat__q { font-size:8px; letter-spacing:.2em; text-transform:uppercase; font-weight:500; margin-top:5px; opacity:.85; }
.cat__body { padding:16px 14px 14px; display:flex; flex-direction:column; flex:1; }
.cat__lbl { font-size:8px; letter-spacing:.24em; text-transform:uppercase; color:var(--terra); font-weight:500; margin-bottom:6px; }
.cat__foods { font-size:14px; line-height:1.55; font-weight:400; }
.cat__goal { margin-top:auto; padding-top:12px; height:1.12in; font-variant-numeric:lining-nums; border-top:1px solid var(--line); font-family:var(--serif); font-style:italic; font-size:16.5px; line-height:1.25; }
.c1 .cat__band { background:var(--espresso); color:var(--bone); } .c1 .cat__n { color:var(--apricot); opacity:1; }
.c2 .cat__band { background:var(--terra-dk); color:#fff; }
.c3 .cat__band { background:var(--terra); color:#fff; }
.c4 .cat__band { background:var(--ember); color:var(--ink); }
.c5 .cat__band { background:var(--apricot); color:var(--ink); }
.c6 .cat__band { background:var(--peach); color:var(--ink); }
.land .notes { display:flex; justify-content:space-between; align-items:center; gap:24px; margin-top:16px; padding:14px 20px; border-radius:14px; background:var(--blush); }
.land .notes p { font-size:11px; line-height:1.5; font-weight:300; }
.land .notes .ask { font-family:var(--serif); font-style:italic; font-size:17px; color:var(--terra); white-space:nowrap; }
"""

def main():
    cards = ""
    for i, (name, q, foods, goal) in enumerate(CATS, 1):
        cards += f"""<div class="cat c{i}">
  <div class="cat__band"><div class="cat__n">{i:02d}</div><div><div class="cat__name">{e(name)}</div>{f'<div class="cat__q">{e(q)}</div>' if q else ''}</div></div>
  <div class="cat__body"><div class="cat__lbl">Sample foods</div><div class="cat__foods">{e(foods)}</div><div class="cat__goal">{e(goal)}</div></div>
</div>"""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Feminine Gut Build Your Plate Categories</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS.replace('@page { size: letter; margin: 0; }', '')}{EXTRA}</style></head><body>
<section class="page land">
  <header class="top">
    <div class="brand">{DRAGONFLY}<div><div class="brand__name">The Body Temple Spa</div><div class="brand__sub">The Feminine Gut</div></div></div>
    <div class="series">Guide <b>06</b> · Plate Categories<br>The TEMPLE Method</div>
  </header>
  <div class="hero">
    <div><div class="eyebrow">The Feminine Gut · Food Guide</div><h1>Build Your <em>Plate</em></h1></div>
    <p class="sub">by choosing from the following categories.</p>
  </div>
  <div class="body">
    <div class="cats">{cards}</div>
    <div class="notes"><p>Please keep in mind your bio-individual needs.<br>This is meant to be a guide but may need to be adjusted for your own unique body.</p><span class="ask">Have questions? Reach out for help!</span></div>
  </div>
  <footer class="foot"><span>The Feminine Gut | The TEMPLE Method</span><span class="tag">The future is yours.</span><span>01 / 01</span></footer>
</section></body></html>"""
    with open(os.path.join(OUT, "Feminine_Gut_Build_Your_Plate_Categories.html"), "w") as f:
        f.write(page)
    print("wrote Feminine_Gut_Build_Your_Plate_Categories")

if __name__ == "__main__":
    main()
