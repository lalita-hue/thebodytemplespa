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
- **Before creating or changing several GHL tasks, show Lalita the plan (titles, owners, due dates) and wait
  for her OK.**
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

## Links & handles

- Kollab community (The Feminine Gut): https://thebodytempleacademy.app.clientclub.net/communities/groups/the-feminine-gut
- Gut Audit page: https://thebodytemplespas.com/gut-audit
- Instagram @iam.lalita.sundari · TikTok @lalita.sundari · Facebook lalita.sundari.atl · YouTube @LalitaSundari

## Services & add-ons

- **Vibration Plate Lymphatic Reset**: add-on, $15, no time added. Offered on all services,
  featured on lymphatic services. Georgina setting it up in GHL (task due Wed Nov 18, 2026).

## Saving information

Lalita wants everything she tells Claude saved. Record standing preferences and
business facts in this file.

## Content

- YouTube/live outlines live in `content/youtube-outlines.md`. Add new outlines there.
- Topics so far: "Is It My Hormones or My Gut?", "Is This Really a Toxic Relationship?",
  "Why Successful Women Attract Relationships That Drain Their Bodies"
  (Nov 2026). Earlier outline: "Detox Him First".
- **Live Audit (Thu Nov 19, 2026, 6pm ET):** "How to Activate Natural GLP-1 & Balance Female Hormones Through
  Your Gut (Live Audit)". Sells the $37 Hormonal Reset. On Google Calendar + GHL task.
- Calendar: Lalita's **personal Google Calendar, lalita@lalitasundari.com**, is the one she uses; put her events there.
  The spa Gmail (lalita@thebodytemplespas.com) is for emails to the team.
- **The Hair Temple Blueprint** (community course; formerly "Insight Program"): hair test (HTMA) +
  supplements + teaching members to read their results. Outline: `content/hair-temple-blueprint.md`.

## Funnels / widgets

- **The Feminine Gut** (by The Body Temple Spa) quiz funnel: `GHL-feminine-gut-audit.html`.
  "Feminine GLP-1 & Hormone Gut Audit", 12 questions in 3 pillars, lead gate posting to a GHL inbound
  webhook, results + $37 tripwire ("The 7-Day Feminine GLP-1 & Nervous System Hormonal Reset", see `offers/7-day-hormonal-reset.md`; bonus 14 days VIP in
  The Feminine Gut, Radiant Self Premium $79/mo, on Kollab). Upsell: Sovereign Self 1-on-1 VIP Coaching.
  Settings at top of the script: GHL_WEBHOOK_URL (set: inbound webhook 920fff6e-f3c3-46aa-9b82-3d48e4424316; if the trigger is deleted and re-added, GHL issues a new URL and the code must be updated), CHECKOUT_URL (set), COACHING_URL (empty = link hidden until the Sovereign Self page exists).
  Look: night-bloom (deep indigo, violet, sunset orange) from Lalita's flower photo; dragonfly from the
  spa logo at the top. Lead form asks first name, last name, email and phone (all required).
  Footer: slogan "The Future Is Yours" + "© <year> The Body Temple Spa. All rights reserved."

## Automations

- Esthetics pre-care automations (facials, waxing, lash & brow, chemical peels): `automations/esthetics.md`.
  Instructions written by Mabry (esthetics; has "Mabry's Personal Calendar" in GHL). Screenshots in `automations/screenshots/`.
- GHL calendars: Body Sculpting services, Personalized Acne Consultation, Mabry's Personal Calendar,
  Lalita Sundari's Personal Calendar, Malynda's Practicioner Calendar, Virtual Assistant's Personal Calendar.
- GHL workflows can't be created via API; they're built in the dashboard.
