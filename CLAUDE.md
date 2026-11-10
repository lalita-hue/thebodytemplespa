# Notes for Claude

## Tasks: use GoHighLevel, not Asana
- Lalita no longer uses Asana. When asked about pending tasks, pull them from GoHighLevel (GHL).
- Location: "The Body Temple Spa", location ID `oz27FgTyetnlFEnG2O11`.
- Open tasks: `POST https://services.leadconnectorhq.com/locations/oz27FgTyetnlFEnG2O11/tasks/search`
  with headers `Version: 2021-07-28`, `Content-Type: application/json`, body `{"completed":false,"limit":100}`.
  Auth is injected by the session proxy (send a dummy `Authorization: Bearer dummy`).
- Lalita's GHL user ID: `l9RzLvtlZA2vYqYLhGIM`. Team: Georgina (pages/SEO), Russell (content/editing),
  Sebastián (numbers), Alex (role-play/calls).
- Also check Google Calendar for the day's client appointments.
- Mark a task done: `PUT /locations/oz27FgTyetnlFEnG2O11/tasks/{taskId}` with body `{"completed":true}`
  (tasks linked to a contact: `PUT /contacts/{contactId}/tasks/{taskId}/completed`).

## Priorities (Nov 10, 2026)
- Lalita chose the webinar attendee automation as the top priority (highest leverage), ahead of the YouTube outlines.
  Build sheet: `webinar-attendee-followup-workflow.md`.
- Webinar tags in GHL: `attended` (set by "Webinar Link Clicked -> Attended"), `webinar cycle completed`, `webinar_opt`.
