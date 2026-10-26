# Feminine Gut Program — Waiting List Form + Automation (GoHighLevel)

Everything here is built inside GoHighLevel (GHL). The page file
`GHL-feminine-gut-waitlist.html` is the branded section that holds the form;
the form itself and the automation are created in GHL using the steps below.

## What it does

1. A visitor fills out the **Feminine Gut Waiting List** form.
2. The workflow fires on that form submission.
3. The contact is tagged **`feminine gut waiting list`**.
4. The contact gets this text message from Lalita:

```
Hiii! This is Lalita! So honor you are here! Save my number so we can communicate better. Let me know if you have any questions! Look forward to see you soon. ❤️
```

> Optional polish before you paste it: "So **honored** you are here!" and
> "**Looking** forward to **seeing** you soon." The text above is exactly as
> you wrote it — use whichever you prefer.

---

## Step 1 — Create the form

**Sites → Forms → Builder → + Add Form → Blank form**

- **Form name:** `Feminine Gut Waiting List`
- **Fields** (drag in from the left panel):

| Field | Type | Required |
|---|---|---|
| First Name | Standard → First Name | Yes |
| Last Name | Standard → Last Name | No |
| Phone | Standard → Phone | **Yes** (the text can't send without it) |
| Email | Standard → Email | Yes |
| What would you most like help with? | Custom → Multi-line text | No |
| SMS consent | Standard → **SMS consent / Terms & Conditions** checkbox | **Yes** |

- **Submit button text:** `Join the Waiting List`
- **Button color:** `#C85A28` (Terracotta), text white, 16px+ — see `BRAND-COLORS.md`.
- **Options (gear icon) → On submit:** either show a message
  (`You're on the list! Check your phone — Lalita just texted you. ❤️`)
  or redirect to a thank-you page.

**Consent text** for the SMS checkbox (required by carriers for A2P 10DLC, or
your texts can be blocked):

```
I agree to receive text messages from The Body Temple Spa about the Feminine Gut Program. Msg & data rates may apply. Msg frequency varies. Reply STOP to opt out, HELP for help.
```

Save, then **Integrate → Embed → Inline** and copy the **form ID**
(the string after `/widget/form/` in the code).

## Step 2 — Create the tag

**Settings → Tags → + New Tag** → `feminine gut waiting list`

(Lowercase, exactly as written, so it matches across filters and workflows.)

## Step 3 — Build the workflow

**Automation → Workflows → + Create Workflow → Start from scratch**

Name it: `Feminine Gut Waiting List — Tag + Welcome Text`

### Trigger
- **+ Add New Trigger → Form Submitted**
- Filter: **Form is** `Feminine Gut Waiting List`
- Save trigger

### Action 1 — Add Tag
- **+ → Add Contact Tag** → select `feminine gut waiting list`

### Action 2 — Send SMS
- **+ → Send SMS**
- **Message:** paste the text from the top of this file
  (to personalize: `Hiii {{contact.first_name}}! This is Lalita! ...`)
- Leave "From" as your business number: **(959) 400-9242**

### Settings (gear icon at top of the workflow)
- **Allow re-entry:** Off (so someone who submits twice isn't texted twice)
- **Stop on response:** Off

Click **Save**, then flip the toggle from **Draft** to **Publish**.

## Step 4 — Put the form on the page

1. Open `GHL-feminine-gut-waitlist.html` and replace **every** `FORM_ID_HERE`
   with the form ID from Step 1 (use Find & Replace to catch them all).
2. In GHL, open the funnel/website page → add a **Custom JS/HTML** element →
   paste the whole file in → Save.

(Or skip the custom page and drop the native **Form** element onto any GHL
page, then pick `Feminine Gut Waiting List`.)

## Step 5 — Test it

1. Submit the form with your own phone number.
2. **Contacts** → find yourself → confirm the `feminine gut waiting list` tag.
3. Confirm the text arrived on your phone.
4. **Automation → Workflows → your workflow → Execution Logs** if anything is missing.

## Later: when the program opens

Go to **Contacts → Smart Lists → filter Tag = `feminine gut waiting list`**
to see everyone who's waiting, or use that tag as the trigger for a launch
announcement workflow.
