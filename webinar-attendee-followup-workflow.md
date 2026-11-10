# Webinar Attendees: Follow-Up Workflow (GHL build sheet)

**Goal:** Everyone who attended the Sunday webinar gets the replay and the link to book a
**free personalized plan call**, then reminders until they book.
No-shows get a separate replay sequence (your draft workflow "No Show -> Nurture").

Fill these in before publishing:
- `[REPLAY LINK]` = the replay video
- `[BOOKING LINK]` = the free personalized plan call calendar. No calendar called "plan call" exists
  in GHL yet. Either use Lalita Sundari's Personal Calendar or create a new "Free Personalized Plan Call" calendar.

---

## Workflow settings
- **Name:** Webinar Attended -> Replay + Book Plan Call
- **Trigger:** Contact Tag Added, tag = `attended`. Your existing workflow "Webinar Link Clicked -> Attended"
  already adds this tag.
- **Allow re-entry:** ON, because people can attend more than one Sunday.
- **Goal / exit:** Appointment booked on the plan-call calendar, OR tag `webinar cycle completed` added.
  Leaving the workflow stops all reminders.
- Also exits when a product is purchased. "Product Purchased - Remove From Webinar" already covers this.
- **Send window:** 9am to 8pm, so SMS never goes out at night.

## Steps

| # | Wait | Action | Message |
|---|------|--------|---------|
| 1 | 0, right away | Email + SMS | Replay + booking link (A) |
| 2 | 1 day | Email | What happens on the call (B) |
| 3 | 1 day | SMS | Quick reminder (C) |
| 4 | 2 days | Email | "Is this for me?" (D) |
| 5 | 2 days | Email + SMS | Last call (E) |
| 6 | 0 | Add tag `webinar cycle completed`, remove tag `attended` | |
| 7 | 0 | Internal notification to Lalita/Alex: "Attended, didn't book: {{contact.name}} {{contact.phone}}" | So Alex can call them |

---

## Copy

**A. Email: "Your replay + your next step"**
> Hi {{contact.first_name}},
>
> Thank you for being with me on Sunday. Here is the replay so you can watch it again: [REPLAY LINK]
>
> If something I shared spoke to you, the next step is a **free personalized plan call**. We look at
> what's going on in your body and map out exactly what would help you, step by step.
>
> Book your call here: [BOOKING LINK]
>
> With love,
> Lalita

**A. SMS**
> Hi {{contact.first_name}}, it's Lalita from The Body Temple Spa. Thank you for joining the webinar!
> Replay: [REPLAY LINK]. Ready for your free personalized plan? Book here: [BOOKING LINK]

**B. Email: "What happens on your free plan call"**
> Hi {{contact.first_name}},
>
> A lot of people ask what the call is like, so here it is:
> 1. You tell me what you're dealing with and what you've already tried.
> 2. I tell you what I think is really driving it.
> 3. You leave with a clear plan, whether you work with me or not.
>
> No pressure, just clarity. [BOOKING LINK]
>
> Lalita

**C. SMS**
> {{contact.first_name}}, a few free plan call spots are still open this week. Grab yours: [BOOKING LINK]

**D. Email: "Is this for me?"**
> Hi {{contact.first_name}},
>
> If you're wondering whether this is for you: it is, if you're tired of guessing and want someone to
> look at the whole picture with you. Your body has been asking for attention, and this call is how we start.
>
> [BOOKING LINK]
>
> Lalita

**E. Email: "Last reminder"**
> Hi {{contact.first_name}},
>
> This is my last reminder about your free personalized plan call from Sunday's webinar.
> If now isn't the right time, that's okay. I'll see you at the next one.
>
> If it is the right time: [BOOKING LINK]
>
> Lalita

**E. SMS**
> Last reminder, {{contact.first_name}}: your free plan call from Sunday's webinar. Book here: [BOOKING LINK]

---

## Before you publish
- [ ] Replay link and booking link are filled in everywhere
- [ ] Test with your own contact: add tag `attended`, then check that the email and SMS arrive
- [ ] Book a test appointment and confirm the workflow stops sending
- [ ] Publish "No Show -> Nurture" for the people who didn't attend
