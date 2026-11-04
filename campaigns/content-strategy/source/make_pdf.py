import html, os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_plan import TOPICS, PLAN, PAIN, PROC, PROOF

HERE = os.path.dirname(os.path.abspath(__file__))
e = html.escape
CHIP = {PAIN: "pain", PROC: "proc", PROOF: "proof"}

CSS = """
@page { size: letter; margin: 0.6in 0.65in 0.7in; }
* { box-sizing:border-box; margin:0; padding:0; }
:root { --apricot:#EFA068; --peach:#F9D2AC; --blush:#FDE8D4; --porcelain:#FEF6EC; --ink:#12100E;
  --terra:#C85A28; --terra-dk:#A8481E; --espresso:#1A1610; --bone:#EDE7DB; --umber:#7A6D5B; --line:rgba(26,22,16,.13);
  --serif:'Cormorant Garamond', Georgia, serif; --sans:'Jost', Arial, sans-serif; }
html { background:#fff; }
body { font-family:var(--sans); color:var(--ink); background:#fff; -webkit-print-color-adjust:exact; print-color-adjust:exact; font-size:10.5px; background:#fff; }
.cover { height:9.6in; display:flex; flex-direction:column; justify-content:center; page-break-after:always; position:relative; }
.cover::before { content:""; position:absolute; width:5.5in; height:5.5in; right:-1.8in; top:-1in; border-radius:50%;
  background:radial-gradient(circle, rgba(239,160,104,.55), rgba(249,210,172,.3) 40%, rgba(254,246,236,0) 70%); }
.eyebrow { font-size:9px; letter-spacing:.3em; text-transform:uppercase; color:var(--terra); font-weight:500; }
.cover h1 { font-family:var(--serif); font-weight:400; font-size:58px; line-height:1; margin:14px 0 12px; position:relative; }
.cover h1 em { color:var(--terra); }
.cover .sub { font-family:var(--serif); font-style:italic; font-size:20px; color:var(--umber); max-width:5.5in; position:relative; }
.facts { margin-top:34px; display:grid; grid-template-columns:1fr 1fr; gap:10px; position:relative; }
.fact { background:var(--porcelain); border:1px solid rgba(200,90,40,.16); border-radius:12px; padding:12px 14px; }
.fact b { display:block; font-size:8px; letter-spacing:.24em; text-transform:uppercase; color:var(--terra); font-weight:500; margin-bottom:4px; }
.fact span { font-size:11px; line-height:1.45; }
.legend { display:flex; gap:8px; margin-top:18px; position:relative; flex-wrap:wrap; }
.chip { display:inline-block; font-size:7.5px; letter-spacing:.18em; text-transform:uppercase; font-weight:500; padding:3px 9px; border-radius:999px; }
.chip.pain { background:var(--espresso); color:var(--apricot); }
.chip.proc { background:var(--terra); color:#fff; }
.chip.proof { background:var(--peach); color:var(--ink); }
h2.topic { font-family:var(--serif); font-weight:400; font-size:38px; line-height:1.05; margin:0 0 4px; page-break-before:always; }
h2.topic em { color:var(--terra); }
h3.part { font-size:9px; letter-spacing:.28em; text-transform:uppercase; color:var(--umber); font-weight:500; margin:16px 0 10px; padding-bottom:6px; border-bottom:1px solid var(--terra); }
.idea { break-inside:avoid; background:var(--porcelain); border:1px solid rgba(200,90,40,.14); border-radius:12px; padding:11px 14px 10px; margin-bottom:8px; display:grid; grid-template-columns:26px 1fr; gap:8px; }
.idea .n { font-family:var(--serif); font-size:22px; color:var(--apricot); line-height:1; }
.idea .hook { font-family:var(--serif); font-size:15.5px; font-weight:600; line-height:1.2; margin:5px 0 4px; }
.idea .angle { font-size:10.4px; line-height:1.5; font-weight:300; }
.idea .meta { display:grid; grid-template-columns:auto 1fr; gap:3px 10px; margin-top:6px; padding-top:6px; border-top:1px solid var(--line); font-size:9.8px; line-height:1.4; }
.idea .meta b { font-size:7.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--terra); font-weight:500; padding-top:1px; }
.plan { width:100%; border-collapse:separate; border-spacing:0; background:var(--porcelain); border:1px solid rgba(200,90,40,.16); border-radius:12px; overflow:hidden; }
.plan th { background:var(--espresso); color:var(--bone); font-size:7.5px; letter-spacing:.22em; text-transform:uppercase; font-weight:500; text-align:left; padding:8px 10px; }
.plan td { padding:8px 10px; border-top:1px solid var(--line); font-size:10px; line-height:1.4; vertical-align:top; }
.plan tr:nth-child(even) td { background:rgba(253,232,212,.4); }
.plan td:first-child { font-weight:500; white-space:nowrap; }
.plan td.hook { font-family:var(--serif); font-size:13px; font-weight:600; }
.tips { margin-top:14px; background:linear-gradient(120deg, var(--peach), var(--apricot)); border-radius:14px; padding:14px 18px; break-inside:avoid; }
.tips h4 { font-family:var(--serif); font-size:19px; font-weight:500; margin-bottom:6px; }
.tips li { font-size:10.5px; line-height:1.55; margin-left:16px; }
"""

def card(i, idea):
    pillar, hook, angle, fmt, cta = idea
    return f"""<div class="idea"><div class="n">{i:02d}</div><div>
<span class="chip {CHIP[pillar]}">{e(pillar)}</span>
<div class="hook">{e(hook)}</div><div class="angle">{e(angle)}</div>
<div class="meta"><b>Format</b><span>{e(fmt)}</span><b>CTA</b><span>{e(cta)}</span></div></div></div>"""

body = f"""<section class="cover">
<div class="eyebrow">The Body Temple Spa · The Feminine Gut</div>
<h1>Your Content <em>Strategy</em></h1>
<p class="sub">60 conversion-focused content ideas across your three pillars, plus a 2-week plan to put them to work.</p>
<div class="facts">
<div class="fact"><b>Ideal client</b><span>High-achieving women whose relationship stress is showing up in their bodies: weight gain, digestive, gut, and hormonal problems.</span></div>
<div class="fact"><b>Desired result</b><span>A healthy relationship, confidence in her body and mind beyond her achievements, and her health reclaimed.</span></div>
<div class="fact"><b>Offer</b><span>The Feminine Gut (waitlist), supported by the hair test, spa services, and your guides.</span></div>
<div class="fact"><b>Your topics</b><span>1. Relationships &amp; self-worth · 2. Beauty, health &amp; wellness · 3. Gut health</span></div>
</div>
<div class="legend"><span class="chip pain">Pain / Problem</span><span class="chip proc">Process / Authority</span><span class="chip proof">Proof / Promotion</span></div>
</section>"""

titles = {"Relationships & Self-Worth": "Relationships <em>&amp; Self-Worth</em>",
          "Beauty, Health & Wellness": "Beauty, Health <em>&amp; Wellness</em>",
          "Gut Health": "Gut <em>Health</em>"}
for t, topic in enumerate(TOPICS, 1):
    body += f'<div class="eyebrow" style="page-break-before:always">Topic {t:02d}</div><h2 class="topic" style="page-break-before:avoid">{titles[topic["name"]]}</h2>'
    body += '<h3 class="part">Short-form · reels, TikToks, carousels, short captions</h3>'
    body += "".join(card(i, x) for i, x in enumerate(topic["short"], 1))
    body += '<h3 class="part">Long-form · lives, podcasts, YouTube, webinars, emails</h3>'
    body += "".join(card(i, x) for i, x in enumerate(topic["long"], 1))

rows = "".join(f'<tr><td>{e(d)}</td><td>{e(src)}</td><td class="hook">{e(h)}</td><td>{e(n)}</td></tr>' for d, src, h, n in PLAN)
body += f"""<div class="eyebrow" style="page-break-before:always">Part 6</div>
<h2 class="topic" style="page-break-before:avoid">Your 2-Week <em>Plan</em></h2>
<h3 class="part">One post a day · short-form to attract, long-form to build trust, proof to convert</h3>
<table class="plan"><tr><th>Day</th><th>From</th><th>Post</th><th>Why here</th></tr>{rows}</table>
<div class="tips"><h4>Make it convert</h4><ul>
<li><b>Set up the comment keywords</b> (GUT, TEMPLE, HAIR, PLATE, STORY, GLOW, RITUAL) as automatic DM replies, so every comment gets your link instantly.</li>
<li><b>Turn each long-form piece into an email</b> to your list the same day, ending with the waitlist link.</li>
<li><b>Proof needs permission:</b> only use real client words, photos, and results that clients have agreed to share.</li>
<li><b>Keep claims gentle:</b> say “can help” and “may,” and point people to their doctor for medical concerns.</li>
<li><b>During Black Friday week (Nov 23–30),</b> swap the gut posts for the hair test offer, and use the hair test reel (Gut short #5) to open it.</li>
</ul></div>"""

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Content Strategy</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{body}</body></html>"""
out = os.path.join(HERE, "content-strategy.html")
open(out, "w").write(page)
print("wrote", out)
