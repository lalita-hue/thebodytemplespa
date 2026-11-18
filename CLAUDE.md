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
- **7-Day Reset ($37) build prompts** (Canva Meal Map PDF + pre-meal somatic audio script): `content/7-day-reset-prompts.md`.
  Finished Meal Map PDF (2 pages, includes probiotic/fermented foods like kimchi): `content/7-day-reset/7-Day-Feminine-GLP-1-Meal-Map.pdf`
  (source `content/7-day-reset/meal-map.html`; edit the HTML and re-render to change it).
  The PDF follows **Week 1 "Nourish First"** (protein 20-30 g/meal, soluble fiber every meal, water = half body weight in oz)
  from Lalita's book "Natural GLP-1 Production: Food, Sleep, Movement, and Stress Management" (a 4-week plan).
  The 7-Day Reset covers Week 1 only. Keep later-week topics (timing, mindful eating, movement, sleep, stress) out
  unless labeled as a bonus. Current bonuses: kimchi/sauerkraut/kefir (gut boost) and the 60-second pre-meal audio.
  Welcome video outline + script (Part 1 intro/overview of the subject, Part 2 Meal Map walkthrough): `content/7-day-reset/meal-map-video.md`.
  Product mockup (night-bloom flowers, "THE FEMININE GUT" wordmark): `content/7-day-reset/source/product-mockup.webp`.
  Full product name on the mockup: "The 7-Day Feminine GLP-1 & Nervous System Hormonal Reset". Included: 7-Day Meal Map,
  Pre-Meal Audio Rituals, 14 Days of Radiant Self Premium (Wellness Library, Community & Expert Support).
  Being built as a GHL Membership course (new course creator). Upload copy (title, description, pricing, modules,
  Day 1-7 lessons) in `content/7-day-reset/course-upload.md`; thumbnail `content/7-day-reset/course-thumbnail-1280x720.jpg`.
  **The 7-Day Reset is the entry to a full plan, with 2 upgrades at the end:** (1) the full 4-week / full-month plan, for women
  who are NOT sensitive to the foods; (2) the hair test (HTMA, The Hair Temple Blueprint), for women WITH food sensitivities.
  Closing upgrade video script: `content/7-day-reset/upgrade-video.md` (Module 5). Still needed from Lalita: full-month
  program name, price and link; hair test price and link; any discount for Reset buyers.
  Lalita wants the course to feel like much more than expected: Module 4 "Celebrate & Keep Your Results" (rewards: Day 7
  reflection, recipe cards, protein & fiber cheat sheet, eat-out/travel guide, Wins Wall + certificate, optional spa gift)
  comes right before Module 5 "Your Next Step" (upgrades).
  **Breakfast must be within 1 hour of waking** (Lalita's rule; overrides the book's "within 2 hours").

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
