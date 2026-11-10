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
