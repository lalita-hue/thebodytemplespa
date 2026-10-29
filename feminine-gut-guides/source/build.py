import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import DOCS

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
os.makedirs(OUT, exist_ok=True)

DRAGONFLY = """<svg class="mark" viewBox="0 0 64 64" aria-hidden="true">
<g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round">
<ellipse cx="18.5" cy="22" rx="15" ry="4.6" transform="rotate(-14 32 24)"/>
<ellipse cx="45.5" cy="22" rx="15" ry="4.6" transform="rotate(14 32 24)"/>
<ellipse cx="20.5" cy="30.5" rx="12" ry="3.8" transform="rotate(16 32 30)"/>
<ellipse cx="43.5" cy="30.5" rx="12" ry="3.8" transform="rotate(-16 32 30)"/>
<path d="M32 22 L32 58"/>
</g>
<circle cx="32" cy="17.5" r="3.2" fill="currentColor"/>
<circle cx="32" cy="24" r="2.2" fill="currentColor"/>
</svg>"""

CSS = r"""
@page { size: letter; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --apricot:#EFA068; --ember:#E58A4C; --peach:#F9D2AC; --blush:#FDE8D4; --porcelain:#FEF6EC;
  --ink:#12100E; --terra:#C85A28; --terra-dk:#A8481E; --espresso:#1A1610; --bone:#EDE7DB;
  --stone:#8A7F6E; --umber:#7A6D5B; --line:rgba(26,22,16,.13);
  --serif:'Cormorant Garamond', Georgia, serif; --sans:'Jost', 'Helvetica Neue', Arial, sans-serif;
}
html, body { background:#d9d2c7; }
body { font-family:var(--sans); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page {
  width:8.5in; height:11in; position:relative; overflow:hidden; background:var(--porcelain);
  page-break-after:always; break-after:page; display:flex; flex-direction:column;
  padding:0.55in 0.7in 0.5in;
}
.page:last-child { page-break-after:auto; break-after:auto; }
/* soft apricot glow, echoing the logo gradient */
.page::before {
  content:""; position:absolute; width:6.2in; height:6.2in; right:-2.4in; top:-2.6in; border-radius:50%;
  background:radial-gradient(circle, rgba(239,160,104,.55) 0%, rgba(249,210,172,.35) 38%, rgba(254,246,236,0) 70%);
}
.page::after {
  content:""; position:absolute; width:4in; height:4in; left:-2in; bottom:-2.2in; border-radius:50%;
  background:radial-gradient(circle, rgba(249,210,172,.5) 0%, rgba(254,246,236,0) 70%);
}
.page > * { position:relative; z-index:1; }

.top { display:flex; align-items:center; justify-content:space-between; padding-bottom:12px; border-bottom:1px solid var(--line); }
.brand { display:flex; align-items:center; gap:10px; }
.mark { width:36px; height:36px; color:var(--terra); }
.brand__name { font-family:var(--sans); font-size:10px; letter-spacing:.32em; text-transform:uppercase; font-weight:500; }
.brand__sub { font-family:var(--serif); font-style:italic; font-size:12px; color:var(--umber); letter-spacing:.02em; }
.series { text-align:right; font-size:8.5px; letter-spacing:.26em; text-transform:uppercase; color:var(--umber); line-height:1.6; }
.series b { color:var(--terra); font-weight:500; }

.hero { padding:24px 0 4px; }
.eyebrow { font-size:9px; letter-spacing:.3em; text-transform:uppercase; color:var(--terra); font-weight:500; display:flex; align-items:center; gap:10px; }
.eyebrow::before { content:""; width:26px; height:1px; background:var(--terra); }
h1 { font-family:var(--serif); font-weight:400; font-size:50px; line-height:1.02; letter-spacing:-.01em; margin-top:12px; }
h1 em { font-style:italic; color:var(--terra); }
.sub { font-family:var(--serif); font-style:italic; font-size:19px; color:var(--umber); margin-top:8px; }

.body { flex:1 0 auto; display:flex; flex-direction:column; gap:13px; padding-top:14px; }
.intro { font-size:13.5px; line-height:1.65; font-weight:300; max-width:6.3in; padding-left:14px; border-left:2px solid var(--apricot); }
p.txt { font-size:12.5px; line-height:1.62; font-weight:300; margin-top:-6px; }
h2 { font-family:var(--serif); font-weight:500; font-size:21px; line-height:1.15; display:flex; align-items:center; gap:10px; margin-top:2px; }
h2::before { content:"✦"; font-size:10px; color:var(--terra); }

.table { border-radius:14px; overflow:hidden; background:rgba(255,255,255,.72); border:1px solid rgba(200,90,40,.16); box-shadow:0 14px 30px -24px rgba(168,72,30,.5); }
.table__head { display:grid; grid-template-columns:2.1in 1fr; background:var(--espresso); color:var(--bone); font-size:8.5px; letter-spacing:.26em; text-transform:uppercase; font-weight:500; }
.table__head div { padding:10px 16px; }
.table__head div:first-child { color:var(--apricot); }
.row { display:grid; grid-template-columns:2.1in 1fr; border-top:1px solid var(--line); }
.row:first-of-type { border-top:none; }
.row:nth-child(odd) { background:rgba(253,232,212,.45); }
.row__k { padding:11px 16px; font-family:var(--serif); font-size:16.5px; font-weight:600; line-height:1.15; display:flex; gap:9px; align-items:baseline; }
.row__k span { font-family:var(--sans); font-size:8px; color:var(--terra); font-weight:500; letter-spacing:.1em; }
.row__v { padding:11px 16px 11px 4px; font-size:11.8px; line-height:1.55; font-weight:300; }

ul.bul { list-style:none; display:flex; flex-direction:column; gap:6px; margin-top:-4px; }
ul.bul li { font-size:12.5px; line-height:1.5; font-weight:300; padding-left:20px; position:relative; }
ul.bul li::before { content:""; position:absolute; left:3px; top:6px; width:6px; height:6px; border-radius:50%; background:var(--apricot); box-shadow:0 0 0 3px rgba(239,160,104,.22); }

ul.chk { list-style:none; display:flex; flex-direction:column; gap:7px; margin-top:-4px; }
ul.chk li { font-size:12.5px; line-height:1.5; font-weight:300; padding-left:26px; position:relative; }
ul.chk li::before { content:""; position:absolute; left:0; top:1px; width:13px; height:13px; border:1.3px solid var(--terra); border-radius:4px; background:#fff; }

.steps { display:flex; flex-direction:column; gap:12px; }
.step { display:grid; grid-template-columns:0.72in 1fr; gap:6px; padding:14px 18px 14px 6px; border-radius:14px; background:rgba(255,255,255,.66); border:1px solid rgba(200,90,40,.14); }
.step__n { font-family:var(--serif); font-size:40px; line-height:.9; color:var(--apricot); text-align:center; font-weight:500; }
.step h3 { font-family:var(--serif); font-size:20px; font-weight:500; margin-bottom:6px; }
.step p, .step li { font-size:12.2px; line-height:1.55; font-weight:300; }
.step ul.bul { margin-top:0; gap:4px; }

.warm { border-radius:16px; padding:18px 22px; background:linear-gradient(120deg, var(--peach) 0%, var(--apricot) 100%); }
.label { font-size:8.5px; letter-spacing:.28em; text-transform:uppercase; font-weight:500; }
.warm .label { color:var(--ink); opacity:.75; }
.warm h3 { font-family:var(--serif); font-size:21px; font-weight:500; margin:4px 0 6px; }
.warm p { font-size:12.5px; line-height:1.6; font-weight:400; }

.dark { border-radius:16px; padding:22px 26px; background:var(--espresso); color:var(--bone); display:grid; grid-template-columns:40px 1fr; gap:14px; align-items:center; }
.dark .mark { width:40px; height:40px; color:var(--apricot); }
.dark .label { color:var(--apricot); }
.dark q { display:block; font-family:var(--serif); font-style:italic; font-size:19px; line-height:1.35; margin-top:6px; quotes:"“" "”"; }

.formula { display:flex; flex-wrap:wrap; align-items:center; gap:8px; margin-top:-4px; }
.formula span.c { font-family:var(--serif); font-size:16px; font-weight:500; padding:5px 14px; border-radius:999px; background:#fff; border:1px solid rgba(200,90,40,.3); }
.formula span.c:first-letter { text-transform:uppercase; }
.formula span.plus { color:var(--terra); font-size:15px; }

.trio { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-top:-4px; }
.trio div { border-radius:12px; background:rgba(255,255,255,.7); border:1px solid rgba(200,90,40,.14); padding:12px 14px; border-top:3px solid var(--apricot); }
.trio h4 { font-family:var(--serif); font-size:16px; font-weight:600; margin-bottom:4px; }
.trio p { font-size:11.3px; line-height:1.5; font-weight:300; }

.chips { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:-4px; }
.chips div { border-radius:12px; padding:10px 14px; background:var(--blush); font-family:var(--serif); font-size:15px; font-weight:500; line-height:1.25; }

.pair { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.pair div { border-radius:14px; background:rgba(255,255,255,.7); border:1px solid rgba(200,90,40,.14); padding:14px 16px; }
.pair h4 { font-family:var(--serif); font-size:18px; font-weight:500; margin-bottom:6px; }
.pair p { font-size:11.6px; line-height:1.55; font-weight:300; }

.note { font-family:var(--serif); font-style:italic; font-size:15.5px; line-height:1.4; color:var(--umber); padding:12px 16px; border-left:2px solid var(--apricot); background:rgba(253,232,212,.5); border-radius:0 10px 10px 0; }

.fill { border-radius:16px; padding:16px 22px 18px; border:1.2px dashed rgba(200,90,40,.55); background:rgba(255,255,255,.6); }
.fill h3 { font-family:var(--serif); font-size:20px; font-weight:500; margin-bottom:6px; }
.fill .ln { display:flex; align-items:flex-end; gap:10px; margin-top:14px; font-size:10px; letter-spacing:.18em; text-transform:uppercase; color:var(--umber); font-weight:500; }
.fill .ln i { flex:1; border-bottom:1px solid rgba(26,22,16,.35); height:1px; }

.shop { column-count:2; column-gap:14px; }
.shop__cat { break-inside:avoid; margin-bottom:12px; border-radius:14px; background:rgba(255,255,255,.72); border:1px solid rgba(200,90,40,.16); padding:12px 16px 10px; }
.shop__cat h4 { font-size:8.5px; letter-spacing:.26em; text-transform:uppercase; color:var(--terra); font-weight:500; padding-bottom:7px; margin-bottom:4px; border-bottom:1px solid var(--line); }
.shop__cat ul { list-style:none; }
.shop__cat li { font-size:11.2px; line-height:1.3; font-weight:400; padding:3.5px 0; }
.shop__cat a { color:var(--ink); text-decoration:none; display:flex; justify-content:space-between; gap:8px; }
.shop__cat a .go { color:var(--terra); font-size:10px; }
.shop__cat li.plain { color:var(--umber); font-weight:300; }

.disclaimer { margin-top:auto; font-size:9px; line-height:1.55; color:var(--umber); font-weight:300; padding-top:10px; border-top:1px solid var(--line); }

.foot { display:flex; align-items:center; justify-content:space-between; padding-top:12px; margin-top:12px; border-top:1px solid var(--terra); font-size:8.5px; letter-spacing:.18em; text-transform:uppercase; color:var(--umber); }
.foot .tag { font-family:var(--serif); font-style:italic; font-size:14px; letter-spacing:0; text-transform:none; color:var(--terra); }
"""

e = html.escape

def render_block(b):
    t = b[0]
    if t == "intro":
        return f'<p class="intro">{e(b[1])}</p>'
    if t == "p":
        return f'<p class="txt">{e(b[1])}</p>'
    if t == "h":
        return f'<h2>{e(b[1])}</h2>'
    if t == "bullets":
        return '<ul class="bul">' + "".join(f"<li>{e(x)}</li>" for x in b[1]) + "</ul>"
    if t == "checks":
        return '<ul class="chk">' + "".join(f"<li>{e(x)}</li>" for x in b[1]) + "</ul>"
    if t == "table":
        (h1, h2), rows = b[1], b[2]
        out = f'<div class="table"><div class="table__head"><div>{e(h1)}</div><div>{e(h2)}</div></div><div>'
        for i, (k, v) in enumerate(rows, 1):
            out += f'<div class="row"><div class="row__k"><span>{i:02d}</span>{e(k)}</div><div class="row__v">{e(v)}</div></div>'
        return out + "</div></div>"
    if t == "steps":
        out = '<div class="steps">'
        for n, title, inner in b[1]:
            out += f'<div class="step"><div class="step__n">{n}</div><div><h3>{e(title)}</h3>{render_block(inner).replace(" class=\"txt\"", "")}</div></div>'
        return out + "</div>"
    if t == "warm":
        return f'<div class="warm"><div class="label">The TEMPLE Method</div><h3>{e(b[1])}</h3><p>{e(b[2])}</p></div>'
    if t == "dark":
        return f'<div class="dark">{DRAGONFLY}<div><div class="label">{e(b[1])}</div><q>{e(b[2])}</q></div></div>'
    if t == "formula":
        parts = [f'<span class="c">{e(x)}</span>' for x in b[1]]
        return '<div class="formula">' + '<span class="plus">+</span>'.join(parts) + "</div>"
    if t == "trio":
        return '<div class="trio">' + "".join(f"<div><h4>{e(h)}</h4><p>{e(p)}</p></div>" for h, p in b[1]) + "</div>"
    if t == "chips":
        return '<div class="chips">' + "".join(f"<div>{e(x)}</div>" for x in b[1]) + "</div>"
    if t == "pair":
        return '<div class="pair">' + "".join(f"<div><h4>{e(h)}</h4><p>{e(p)}</p></div>" for h, p in b[1]) + "</div>"
    if t == "note":
        return f'<p class="note">{e(b[1])}</p>'
    if t == "fill":
        lines = "".join(f'<div class="ln">{e(x)}<i></i></div>' for x in b[2])
        return f'<div class="fill"><h3>{e(b[1])}</h3>{lines}</div>'
    if t == "disclaimer":
        return f'<p class="disclaimer">{e(b[1])}</p>'
    if t == "shop":
        out = '<div class="shop">'
        for cat, items in b[1]:
            lis = "".join(
                f'<li><a href="{e(url)}" target="_blank" rel="noopener">{e(name)}<span class="go">↗</span></a></li>' if url
                else f'<li class="plain">{e(name)}</li>'
                for name, url in items)
            out += f'<div class="shop__cat"><h4>{e(cat)}</h4><ul>{lis}</ul></div>'
        return out + "</div>"
    raise ValueError(t)

for doc in DOCS:
    total = len(doc["pages"])
    pages = []
    for i, pg in enumerate(doc["pages"], 1):
        blocks = "".join(render_block(b) for b in pg["blocks"])
        pages.append(f"""
<section class="page">
  <header class="top">
    <div class="brand">{DRAGONFLY}<div><div class="brand__name">The Body Temple Spa</div><div class="brand__sub">The Feminine Gut</div></div></div>
    <div class="series">Guide <b>{doc['num']}</b> · {e(doc['series'])}<br>The TEMPLE Method</div>
  </header>
  <div class="hero">
    <div class="eyebrow">The Feminine Gut · {e(doc['series'])}</div>
    <h1>{pg['title']}</h1>
    <p class="sub">{e(pg['sub'])}</p>
  </div>
  <div class="body">{blocks}</div>
  <footer class="foot"><span>The Feminine Gut | The TEMPLE Method</span><span class="tag">The future is yours.</span><span>{i:02d} / {total:02d}</span></footer>
</section>""")
    title = doc["slug"].replace("_", " ")
    page_html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""
    with open(os.path.join(OUT, doc["slug"] + ".html"), "w") as f:
        f.write(page_html)
    print("wrote", doc["slug"])
