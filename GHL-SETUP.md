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
| `consent-agreement.html` | Print to PDF | The agreement on paper, for in-person intake |

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

## Email buttons

Anchor styles get stripped somewhere between the file and the inbox, so both
buttons put their padding and background on the `<td>` and repeat the text
colour three ways (`style`, `<font color>`, and a coloured `<span>`). If you
edit a button, keep that pattern — a plain styled `<a>` renders as a blue
underlined link inside a tight coloured blob.

**Paste the email HTML into GHL's code/source view, not the visual editor.**
The visual editor re-parses the markup through its own builder.

## Signing

The client signs **once**, at the end. Everything else on the signature lines is
filled in for them:

| Field | Behaviour |
|---|---|
| `today_s_date`, `date`, `signature_date` | Today's date, read-only |
| `client_signature` (consent section) | Carried from `full_name`, read-only |
| `signature_name` (final step) | **The only thing the client types** |
| `signature_confirm` | The accuracy checkbox |

Typing the name at the end rewrites the consent line, so the two always agree.

`consent-agreement.html` is the same agreement as a printable one-page sheet
with blank signature lines, for a client signing in person. **Its wording is
character-for-character identical to the online consent step. If either is ever
reworded, reword both in the same commit** — a client signing on paper and a
client signing online must be agreeing to the same thing.
Locked fields use `readonly`, never `disabled` — a disabled input is dropped
from the payload. `restore()` refills them afterwards, or a returning client
meets a locked empty box.

## Still open

- [ ] Repaste the intake form and both emails, then send one confirming test
- [ ] Map **Phone** in the Create/Update Contact action — the number reaches the
      Note but is not landing in the contact's Phone field, so SMS has nothing
      to send to
- [ ] Delete the test contacts
- [ ] Optional: If/Else branch adding an SMS when `needs_urgent_review = YES`
- [ ] Decide whether clients should see band names at all (the coach guide says no)
- [ ] Decide whether to keep `SHOW_RISK = true` in `client-report.html`

## Known quirks, not bugs

- Gmail auto-links the street address in the footer. Expected, harmless.
- "Email is marked as Invalid" on a mailbox that works is a stale GHL flag —
  see the section above. It does not indicate a workflow fault.
