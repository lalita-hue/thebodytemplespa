# Acne & Gut Intake — GoHighLevel setup

Internal runbook for the intake questionnaire → report automation.
The Body Temple Spa, Athens GA.

> **Never commit the live webhook URL to this repo.** It is public.
> The webhook lives only in the local copy of the form that is uploaded to GHL.
> `acne-gut-intake-form.html` in this repo ships with an empty `webhookUrl`.

---

## The pieces

| File | Where it lives | What it does |
|---|---|---|
| `acne-gut-intake-form.html` | GHL custom-code page | 40-step questionnaire, scores locally, POSTs to the webhook |
| `client-report.html` | GHL page at `/acne-gut-final-report-page` | 6-page client report, reads scores from the URL token |
| `coach-report.html` | Internal only — **never publish** | Full clinical view, flags, worksheet |
| `email-client.html` | GHL workflow → Send Email | Report link + answer record |
| `email-coach.html` | GHL workflow → Internal Notification | Scores, flags, medications, diagnoses |

## The workflow

Trigger: **Inbound Webhook**

1. **Create/Update Contact** — map first name, last name, email, phone, + 5 custom fields
2. **Add Tag** — `acne-gut-intake`, plus `urgent-review` when flagged
3. **Add Note** — the full `merge.transcript` (~24KB, every answer)
4. **Send Email** — goes to the contact. There is no To field; that is correct.
5. **Internal Notification** — the only action with a **To Custom Email**. This is
   how the coach report reaches staff. The coach email contains medications and
   diagnoses; do not forward it to the client.

**A workflow in Draft does not run.** Publish it.

## Scoring rules

- 376 scored rows: 321 NAQ + 47 scale + 8 safety
- Reverse-scored: `diet__vitamins_and_minerals`, `lifestyle__exercise_per_week`
- Flags only, never scored: `medications`
- A domain needs **80% completion** before it produces a score
- Bands: ≤20 Optimal · 21–47 Early · 48–74 High · 75–100 Critical
- Anything above 20 is worth a conversation

## Phone numbers

GHL drops anything that is not E.164. The form normalises before sending:
10 digits → `+1XXXXXXXXXX`. The on-screen formatter strips a typed leading `1`
so `+1 (706) 555-0142` does not become `(170) 655-5014`.

## Reading Execution logs

| Status | Meaning |
|---|---|
| Executed | Ran and sent |
| Failed | Tried, something broke |
| **Skipped** | Refused to try — usually the address is flagged Invalid |

## "Email is marked as Invalid"

GHL validates every address and permanently refuses to send to one it has
flagged. Causes: the mailbox does not exist, the domain has no mail service
(no MX records), or a previous send hard-bounced.

To test: send a normal email to the address from Gmail. If it bounces, GHL is
right and the address is dead. If it arrives, the validator got a bad answer —
clear the address on the contact, save, retype it, save, which forces a
revalidation.

This is almost always a *test data* problem. Real clients type working addresses.

## Still open

- [ ] Delete the test contacts once the client email is confirmed sending
- [ ] Optional: If/Else branch adding an SMS when `needs_urgent_review = YES`
- [ ] Decide whether clients should see band names at all (the coach guide says no)
- [ ] Decide whether to keep `SHOW_RISK = true` in `client-report.html`
