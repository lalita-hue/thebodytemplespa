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
  Sebastián Sáenz `s0rDQ5D7HFkFbYkRyuMT`, Malynda Barakadyn `gszFoEKVK6cxXYTyuWAI`.
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
- **Send emails through Gmail, not GHL.** The Gmail connector can only create drafts: put the
  email in Lalita's Gmail Drafts, she reviews and hits Send. If Gmail isn't connected, tell her
  to reconnect it at https://claude.ai/customize/connectors and start a new session (don't fall back to GHL).
- **Georgina's work email is `hello@thebodytemplespas.com`** (note the "s" in temple**spas**). Send to that,
  not her Gmail. In GHL it's saved as an additional email on her contact, so pass `"emailTo":"hello@thebodytemplespas.com"`.

## Saving information

Lalita wants everything she tells Claude saved. Record standing preferences and
business facts in this file.

## Content

- YouTube/live outlines live in `content/youtube-outlines.md`. Add new outlines there.
- Topics so far: "Is It My Hormones or My Gut?", "Is This Really a Toxic Relationship?",
  "Why Successful Women Attract Relationships That Drain Their Bodies"
  (Nov 2026). Earlier outline: "Detox Him First".

## Automations

- Esthetics pre-care automations (facials, waxing, lash & brow, chemical peels): `automations/esthetics.md`.
  Instructions written by Mabry (esthetics; has "Mabry's Personal Calendar" in GHL). Screenshots in `automations/screenshots/`.
- GHL calendars: Body Sculpting services, Personalized Acne Consultation, Mabry's Personal Calendar,
  Lalita Sundari's Personal Calendar, Malynda's Practicioner Calendar, Virtual Assistant's Personal Calendar.
- GHL workflows can't be created via API; they're built in the dashboard.
