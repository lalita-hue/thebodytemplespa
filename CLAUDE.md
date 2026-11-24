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

## Automations

- Esthetics pre-care automations (facials, waxing, lash & brow, chemical peels): `automations/esthetics.md`.
  Instructions written by Mabry (esthetics; has "Mabry's Personal Calendar" in GHL). Screenshots in `automations/screenshots/`.
- GHL calendars: Body Sculpting services, Personalized Acne Consultation, Mabry's Personal Calendar,
  Lalita Sundari's Personal Calendar, Malynda's Practicioner Calendar, Virtual Assistant's Personal Calendar.
- GHL workflows can't be created via API; they're built in the dashboard.

## Facial booking links (correct as of Nov 2026)

Used on the facials thank-you page `GHL-facials-thankyou.html`. Base: `https://link.thebodytemplespas.com/booking/oz27FgTyetnlFEnG2O11/sv/<id>`
(use the `link.thebodytemplespas.com` domain, not the old `api.leadconnectorhq.com` links).

| Service | Price | ID |
|---|---|---|
| The Reveal Custom Facial | $100 / 60 min | `696aa31fb05c4c3fcadea2ba` |
| 90 Min Reveal Custom Facial | $145 / 90 min | `6ac2d988cdf1578919223575` |
| Luminous Facial Lift (Lymphatic & TMJ) | $145 / 60 min | `698a9263ed5dc0f5c3b274e8` |
| 45 Min Lymphatic Facial (was "30 Min", $85) | $105 / 45 min | `68e2636150b0a6bfa01f2626` |
| Royalty Dermaplaning Facial | $145 / 60 min | `69f3b1f13ebf6d6921ee501d` |
| Ultra Sonic Skin Scrubber Facial | $120 / 60 min | `69f3b1b7fac7294f8e196b2b` |
| Microchanneling | $225 / 45 min | `69f51db1feb24d3d8444944e` |
| Define Jaw Line Sculpt (badge: Most Popular) | $199 | `6a30584d7b028c161b530b7f` |
| Chemical Peel Consultation | $0 (complimentary) | `6b0483aa129d1d14404f5b2c` |
| Acne Treatment | $155 | `6a78cc9f1bbd34854e1bc06f` |

Text-to-book number on that page: +1 959-400-9242.

## Payroll / visits spreadsheets (Sebastián builds them)

- Sebastián Sáenz keeps the therapist visits + pay slip spreadsheets. His email in GHL: Sebastiansaenz628@gmail.com.
- Process: Georgina enters all the visit info; then the review goes **therapist by therapist**, matching each one against GHL.
- The visits sheet already has a therapist filter at the top.
- Sheet name: **"Payroll + Lead Tracker"**. Updates Lalita asked for (Nov 2026):
  - **Payslip tab** has two parts per therapist: (1) a **detailed breakdown** for internal review
    (every appointment with the client's name and the appointment date), and (2) the **summary payslip**
    that gets sent to the therapist, as done so far.
  - **Lead Tracker tab:** add the total amount paid per appointment, and make it easy to compare, per
    appointment: amount paid, service cost, tip and revenue.
  - Emailed these updates to Sebastián on 2026-11-24 (subject "Updates for the Payroll + Lead Tracker sheet").
  - Also mentioned earlier: missing visits / wrong amounts to fix; mark couples visits to cross-check with the partner.
- Marty's pay was reviewed and is good to go (Nov 2026).

## Services menu (Services & Gift Guide)

- Lalita's full services menu for GHL is saved in `GHL-services-menu.html` (cover page with search, specials,
  category index, all service pages, closing page). Its main stylesheet lives separately in GHL and isn't in the repo.
