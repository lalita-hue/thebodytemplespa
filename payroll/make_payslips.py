"""Build one payslip PDF per therapist from a cycle tab of the Payroll Google Sheet.

Usage: python3 -I make_payslips.py <Payroll.xlsx> "<Cycle tab name>" <out_dir>
       node html_to_pdf.js <out_dir>      (turns the HTML payslips into PDFs)
Export the sheet with the Google Drive connector as .xlsx first.
"""
import sys, datetime, html, os
from collections import defaultdict, OrderedDict
import openpyxl

xlsx, tab, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
ws = openpyxl.load_workbook(xlsx, data_only=True)[tab]

rows, week = [], 0
for r in ws.iter_rows(values_only=True):
    a = r[0]
    if isinstance(a, str) and a.startswith("WEEK 1"): week = 1; continue
    if isinstance(a, str) and a.startswith("WEEK 2"): week = 2; continue
    if isinstance(a, str) and a.startswith("ADD-ONS"): week = 0; continue
    if week and r[1] and r[0] != "Client" and isinstance(r[4], datetime.datetime):
        rows.append(dict(week=week, client=r[0], who=r[1], pct=r[2] or 0, day=r[3],
                         date=r[4], svc=(r[5] or "").strip(), cost=r[6] or 0,
                         com=r[7] or 0, tip=r[8] or 0, note=r[10], ok=r[11]))

m = lambda x: f"${x:,.2f}"
by = defaultdict(list)
for x in rows: by[x["who"]].append(x)
issue = datetime.date.today().strftime("%b %d, %Y")
cycle = tab.replace("Cycle ", "")

CSS = """
@page{size:Letter;margin:0.5in}
body{font-family:Georgia,'Times New Roman',serif;color:#2b2420;font-size:11px;margin:0}
.hd{text-align:center;border-bottom:3px solid #e8935b;padding-bottom:10px;margin-bottom:14px}
.hd h1{margin:0;font-size:24px;letter-spacing:4px;color:#3a2a4f}
.hd h2{margin:4px 0;font-size:12px;letter-spacing:3px;color:#e8935b;font-weight:normal}
.hd p{margin:2px 0;font-size:10px;color:#6b5e57}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:4px 24px;margin-bottom:14px}
.meta b{color:#3a2a4f}
.sec{background:#3a2a4f;color:#fff;padding:5px 8px;font-size:11px;letter-spacing:2px;margin:14px 0 6px}
.kpi{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.kpi div{border:1px solid #ecd9cb;background:#fdf6f0;padding:8px;text-align:center}
.kpi span{display:block;font-size:9px;color:#6b5e57;text-transform:uppercase;letter-spacing:1px}
.kpi strong{font-size:16px;color:#3a2a4f}
.kpi .big strong{color:#c2622d}
table{width:100%;border-collapse:collapse}
th{background:#fdf0e6;text-align:left;padding:5px;font-size:10px;border-bottom:1px solid #e8935b}
td{padding:4px 5px;border-bottom:1px solid #f0e6df;vertical-align:top}
td.n,th.n{text-align:right;white-space:nowrap}
tr.tot td{font-weight:bold;border-top:2px solid #3a2a4f;background:#fdf6f0}
.note{margin-top:14px;font-size:9.5px;color:#6b5e57;font-style:italic}
.sig{display:flex;justify-content:space-between;margin-top:28px}
.ft{margin-top:22px;text-align:center;font-size:9.5px;color:#6b5e57;border-top:1px solid #ecd9cb;padding-top:8px}
.ft b{color:#c2622d;letter-spacing:1px}
.pb{page-break-after:always}
"""

def slip(name, xs):
    com = sum(x["com"] for x in xs); tip = sum(x["tip"] for x in xs)
    pct = xs[0]["pct"]
    dayt = defaultdict(float)
    for x in xs: dayt[x["day"]] += x["com"] + x["tip"]
    peak = max(dayt, key=dayt.get)
    svc = OrderedDict()
    for x in sorted(xs, key=lambda x: x["svc"].lower()):
        s = svc.setdefault(x["svc"], [0, 0, 0, 0]); s[0] += 1; s[1] += x["cost"]; s[2] += x["com"]; s[3] += x["tip"]
    svc_rows = "".join(f"<tr><td>{html.escape(k)}</td><td class=n>{q}</td><td class=n>{m(b)}</td><td class=n>{m(c)}</td><td class=n>{m(t) if t else '-'}</td><td class=n>{m((c+t)/q)}</td></tr>" for k,(q,b,c,t) in svc.items())
    det = "".join(f"<tr><td style=white-space:nowrap>{x["date"]:%a %b %d}</td><td>{html.escape(str(x['client']))}</td><td>{html.escape(x['svc'])}</td><td class=n>{m(x['cost'])}</td><td class=n>{m(x['com'])}</td><td class=n>{m(x['tip']) if x['tip'] else '-'}</td></tr>" for x in sorted(xs, key=lambda x: x['date']))
    wk = []
    for w, lbl in ((1, "Week 1"), (2, "Week 2")):
        ys = [x for x in xs if x["week"] == w]
        c = sum(y["com"] for y in ys); t = sum(y["tip"] for y in ys)
        wk.append(f"<tr><td>{lbl}</td><td class=n>{len(ys)}</td><td class=n>{m(c)}</td><td class=n>{m(t)}</td><td class=n>{m(c+t)}</td></tr>")
    billed = sum(x["cost"] for x in xs)
    return f"""
<div class=hd><h1>THE BODY TEMPLE SPA</h1><h2>OFFICIAL PAYROLL STATEMENT</h2>
<p>WhatsApp: (321) 364-2679 &nbsp;|&nbsp; Email: sebastiansaenz628@gmail.com</p></div>
<div class=meta><div><b>Therapist / Staff Member:</b> {html.escape(name)}</div><div><b>Pay Cycle:</b> {html.escape(cycle)}</div>
<div><b>Base Commission Rate:</b> {pct*100:.0f}%</div><div><b>Issue Date:</b> {issue}</div></div>
<div class=sec>KEY FINANCIAL &amp; ACTIVITY SUMMARY</div>
<div class=kpi><div class=big><span>Total Net Payout</span><strong>{m(com+tip)}</strong></div>
<div><span>Total Commissions</span><strong>{m(com)}</strong></div><div><span>Total Tips</span><strong>{m(tip)}</strong></div>
<div><span>Services Completed</span><strong>{len(xs)}</strong></div><div><span>Peak Day</span><strong>{peak}</strong></div></div>
<div class=sec>BREAKDOWN BY SERVICE</div>
<table><tr><th>Service Description</th><th class=n>Qty</th><th class=n>Total Billed</th><th class=n>Commission</th><th class=n>Tips</th><th class=n>Avg / Session</th></tr>{svc_rows}
<tr class=tot><td>Total</td><td class=n>{len(xs)}</td><td class=n>{m(billed)}</td><td class=n>{m(com)}</td><td class=n>{m(tip)}</td><td class=n>{m((com+tip)/len(xs))}</td></tr></table>
<div class=sec>WEEKLY SUMMARY &amp; NET PAYABLE</div>
<table><tr><th>Period</th><th class=n>Services</th><th class=n>Commissions</th><th class=n>Tips</th><th class=n>Subtotal</th></tr>{''.join(wk)}
<tr class=tot><td>TOTAL NET PAYABLE</td><td class=n>{len(xs)}</td><td class=n>{m(com)}</td><td class=n>{m(tip)}</td><td class=n>{m(com+tip)}</td></tr></table>
<div class=sec>SERVICE DETAIL</div>
<table><tr><th>Date</th><th>Client</th><th>Service</th><th class=n>Billed</th><th class=n>Commission</th><th class=n>Tip</th></tr>{det}</table>
<p class=note>Official Note: This pay statement summarizes all earned commissions and tips for the selected pay cycle. For any questions or adjustments, please contact Administration via WhatsApp at (321) 364-2679 or email at sebastiansaenz628@gmail.com.</p>
<div class=sig><div>Approved by: The Body Temple Spa Management</div><div>Staff Signature: ___________________________</div></div>
<div class=ft><b>The Future Is Yours.</b><br>&copy; {datetime.date.today().year} The Body Temple Spa. All rights reserved.</div>
""", com + tip

docs, summary = [], []
page = lambda b: f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{b}</body></html>"
for name, xs in sorted(by.items(), key=lambda kv: -sum(x["com"]+x["tip"] for x in kv[1])):
    body, tot = slip(name, xs); summary.append((name, tot)); docs.append(body)
    open(os.path.join(out, f"Payslip - {name} - {cycle}.html"), "w").write(page(body))
open(os.path.join(out, f"All Payslips - {cycle}.html"), "w").write(page("<div class=pb></div>".join(docs)))
for n, t in summary: print(f"{n:10s} {m(t)}")
print("TOTAL", m(sum(t for _, t in summary)))
