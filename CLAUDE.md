# Notes for Claude

## Tasks = GoHighLevel (GHL), never Asana

When Lalita asks for "my tasks", "pending tasks", "what's on my plate", etc.,
pull them from **GoHighLevel**, not Asana. Do not use the Asana tools for tasks.

- API host: `services.leadconnectorhq.com` (auth is injected by the session proxy; no key needed)
- Location ID: `oz27FgTyetnlFEnG2O11` (The Body Temple Spa)
- Open tasks:

  ```bash
  curl -sS -X POST -H "Version: 2021-07-28" -H "Content-Type: application/json" \
    "https://services.leadconnectorhq.com/locations/oz27FgTyetnlFEnG2O11/tasks/search" \
    -d '{"completed":false,"limit":100}'
  ```

- Mark a task complete (only when Lalita says it's done):
  `PUT https://services.leadconnectorhq.com/locations/oz27FgTyetnlFEnG2O11/tasks/<taskId>`
  with body `{"completed":true}` (same headers as above).
- Create a task: `POST https://services.leadconnectorhq.com/locations/oz27FgTyetnlFEnG2O11/tasks`
  with `{"title","body","assignedTo":"<userId>","dueDate":"<ISO>","completed":false}`.
- Team user IDs: Georgina Mc Bain `GsYbT3st89lCZ9br97vA`, Ann Loyer `okHTaQE5BnJLGV2nmymL`,
  Mabry Cooper `aWwBfmjczARmKisaDBIQ`, Russel Cabudbud `XZ6Y7sGrTw5BHJ5jtdLd`,
  Sebastián Sáenz `s0rDQ5D7HFkFbYkRyuMT`, Malynda Barakadyn `gszFoEKVK6cxXYTyuWAI`,
  Lalita `l9RzLvtlZA2vYqYLhGIM`, Frank Mike `dcYvkU2P7BDRGUDWXJjM` (Frank handles email/Kit: moving contacts from GHL to Kit).
  Full list with emails: `GET /users/?locationId=oz27FgTyetnlFEnG2O11`.
- Emailing the team: use Gmail drafts (see "Sending emails" below). GHL sending is only a last resort
  when Lalita explicitly asks for it:
  find the person's contact (`GET /contacts/?locationId=...&query=<email>`), then
  `POST /conversations/messages` (header `Version: 2021-04-15`) with
  `{"type":"Email","contactId","subject","html"}`. Georgina's contact ID: `ZiopFUcKiv1FXnBPLugV`.
- Lalita's tasks are the ones assigned to "Lalita Sundari - Owner". Show those first,
  sorted by due date, then team tasks (Georgina, Russell, Sebastian, Alex, Ann) and unassigned ones.

## Sending emails / messages: ALWAYS get approval first

- **Never send an email or text without Lalita's approval.** Always show her the full draft
  (to, subject, body) first and wait for her OK before sending.
- Connected Gmail account: **lalita@thebodytemplespas.com** (Lalita's spa email).
- **Send emails through Gmail, not GHL.** Gmail can now send directly (send_message, reply,
  forward) and create drafts. Either way, show Lalita the full email here first and only send
  after she approves. If Gmail isn't connected, tell her
  to reconnect it at https://claude.ai/customize/connectors and start a new session (don't fall back to GHL).
- **Georgina's work email is `hello@thebodytemplespas.com`** (note the "s" in temple**spas**). Send to that,
  not her Gmail. In GHL it's saved as an additional email on her contact, so pass `"emailTo":"hello@thebodytemplespas.com"`.

## Brand

- **Slogan: "The Future Is Yours."** Use it in footers and brand copy (exactly these words, nothing added).
- The logo's small tagline reads "Self care is self love". It is not the slogan.
- Logo: a dragonfly over "THE BODY TEMPLE SPA" on a peach/orange glow.
- Footers: "© <year> The Body Temple Spa. All rights reserved."

## Saving information

Lalita wants everything she tells Claude saved. Record standing preferences and
business facts in this file.

## Content

- YouTube/live outlines live in `content/youtube-outlines.md`. Add new outlines there.
- Topics so far: "Is It My Hormones or My Gut?", "Is This Really a Toxic Relationship?",
  "Why Successful Women Attract Relationships That Drain Their Bodies"
  (Nov 2026). Earlier outline: "Detox Him First".
- Live/social announcements: `content/live-announcements.md`.
- **Content rule ("What, not How"):** public lives and social posts only cover the what and why
  (awareness, root cause, mindset, why conventional approaches fail). Never give protocols, recipes,
  supplements or how-to routines; those are saved for the paid course and lead magnets.
- **Audience (The Feminine Gut):** women in their 30s-40s in perimenopause/menopause wanting root-cause,
  non-synthetic results. Struggles: stubborn weight, heartburn/bloating, exhaustion, lost glow,
  toxic/draining relationships. Tone: empathetic, authoritative, luxury.
- **The Hair Temple Blueprint** (community course; formerly "Insight Program"): hair test (HTMA) +
  supplements + teaching members to read their results. Outline: `content/hair-temple-blueprint.md`.

## Funnels / widgets

- **The Feminine Gut** (by The Body Temple Spa) quiz funnel: `GHL-feminine-gut-audit.html`.
  "Feminine GLP-1 & Hormone Gut Audit", 12 questions in 3 pillars, lead gate posting to a GHL inbound
  webhook, results + $37 tripwire ("7-Day Feminine GLP-1 & Nervous System Reset"; bonus 14 days VIP in
  The Feminine Gut, Radiant Self Premium $79/mo, on Kollab). Upsell: Sovereign Self 1-on-1 VIP Coaching.
  Settings at top of the script: GHL_WEBHOOK_URL, CHECKOUT_URL, COACHING_URL.
  Look: night-bloom (deep indigo, violet, sunset orange) from Lalita's flower photo; dragonfly from the
  spa logo at the top. Lead form asks first name, email and phone (all required).
  Footer: slogan "The Future Is Yours" + "© <year> The Body Temple Spa. All rights reserved."

## Payroll

- Google Sheet **"Payroll "** (Drive ID `15ueU6Vd5ef6S9x3NW6awN-dRo3dxZ9kmnZIb-vzHe1w`, owner thewomenstemplecoaching@gmail.com).
  One tab per 2-week cycle (e.g. "Cycle OCT 25 - Nov 7 2026"): summary at top, WEEK 1 entries from row 17,
  WEEK 2 entries further down, then an add-ons log (Georgina gets $0.10 per add-on she books).
  Other tabs: Georgina Bonus, Matriz (DONT TOUCH), Data (auto), Dashboard, Payslip (template).
- Commission rates: Lalita 50%, Marty 35%, Adam/Julia/Mabry/Malynda/Russel 33%, Kaitlin 31%, Ann 60%.
- Payslips: export the sheet as .xlsx with the Drive connector, then run
  `python3 -I payroll/make_payslips.py <file.xlsx> "<cycle tab>" <out_dir>` and `node payroll/html_to_pdf.js <out_dir>`.
  Same layout as the sheet's Payslip tab (contact: WhatsApp (321) 364-2679, sebastiansaenz628@gmail.com).
  Don't commit payslips or payroll data to git (client names).

## Automations

- Esthetics pre-care automations (facials, waxing, lash & brow, chemical peels): `automations/esthetics.md`.
  Instructions written by Mabry (esthetics; has "Mabry's Personal Calendar" in GHL). Screenshots in `automations/screenshots/`.
- GHL calendars: Body Sculpting services, Personalized Acne Consultation, Mabry's Personal Calendar,
  Lalita Sundari's Personal Calendar, Malynda's Practicioner Calendar, Virtual Assistant's Personal Calendar.
- GHL workflows can't be created via API; they're built in the dashboard.
