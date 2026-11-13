# Esthetics Pre-Care Automations

Source: pre-care texts from **Mabry**, sent to Lalita (screenshots in `screenshots/esthetics-precare-1..5.png`).
Goal: every client who books one of these services automatically gets the matching pre-care instructions.

## The 4 automations

| # | Service group | Send full instructions | Reminder |
|---|---|---|---|
| 1 | Facials | Right after booking | 3 days before (start of the 3–5 day no-retinoids window) |
| 2 | Waxing | Right after booking | 2 days before (24–48h no-exfoliation window) |
| 3 | Lash & Brow | Right after booking | 2 days before (48h window) |
| 4 | Chemical Peels | Right after booking | 7 days before (5–7 day window) + 24h before |

Why "right after booking": if someone books 2 days out, a "7 days before" step would never fire.

### How to build each one in GHL (Automation → Workflows)
1. **Trigger:** Appointment Status → *Booked* (filter: the calendar/service for that group, e.g. Mabry's Personal Calendar + service name).
2. **Action:** Send Email with the full instructions below (subject: "Getting ready for your [service] at The Body Temple Spa").
3. **Action:** Send SMS (short version below) with a link to the full instructions or "check your email."
4. **Wait:** until X days before the appointment start time (see table).
5. **If/Else:** appointment still booked/confirmed → send the reminder SMS.
6. Peels only: wait until 24h before → send a final reminder SMS.

Note: GHL's API can't create workflows, so these have to be built in the GHL dashboard.

## Short SMS versions (draft, review before use)

- **Facials:** "Hi {{contact.first_name}}! Getting ready for your facial at The Body Temple Spa: please skip exfoliants, retinoids & at-home peels for 3–5 days before, no waxing/shaving the area 24–48h before, and come with a clean face. Full prep tips are in your email. Questions? Just reply!"
- **Waxing:** "Hi {{contact.first_name}}! For your wax at The Body Temple Spa: let hair grow to 1/4 inch (a grain of rice), no exfoliating 24–48h before, no lotions/oils on the area that day, and no sunburn. Full prep tips are in your email. Questions? Just reply!"
- **Lash & Brow:** "Hi {{contact.first_name}}! For your lash/brow appointment at The Body Temple Spa: come with clean, makeup-free lashes & brows, skip oils and waterproof mascara, and avoid retinoids/exfoliants around the eyes for 48h. Full prep tips are in your email. Questions? Just reply!"
- **Chemical Peels:** "Hi {{contact.first_name}}! Your peel at The Body Temple Spa is coming up: stop retinoids & exfoliants (AHAs, BHAs, scrubs, at-home peels) and waxing/threading the area 5–7 days before, and avoid sun & tanning for a week. Full prep tips are in your email. Questions? Just reply!"

## Full instructions (Mabry's original wording)

### FOR ALL FACIALS
A few things to keep in mind before your appointment:

- Please avoid exfoliating products, retinoids (Retin-A, tretinoin, Differin, etc.), and at-home chemical peels for 3–5 days before your appointment, unless we've discussed otherwise.
- Avoid waxing, shaving, or other aggressive treatments on the area for at least 24–48 hours beforehand.
- Please arrive with a clean face if possible and avoid wearing makeup.
- If you've started any new skincare products, medications, or experienced any changes in your skin, please let me know beforehand.
- Please let me know if you have any recent sun exposure, sunburn, or skin irritation.

### FOR ALL WAXING
A few things to keep in mind before your appointment to help ensure the best results and a comfortable experience:

- Please allow hair to grow to at least ¼ inch (about the length of a grain of rice) so the wax can properly grip the hair.
- Avoid exfoliating the treatment area for 24–48 hours before your appointment.
- Avoid applying lotions, oils, or heavy skincare products to the area on the day of your appointment.
- Avoid excessive sun exposure, tanning, or coming in with sunburned or irritated skin.
- Please avoid shaving between waxing appointments to maintain optimal results.
- Let me know if you're currently using retinoids, acne medications, or exfoliating products, especially if waxing the face.
- Please inform me of any new medications, skin sensitivities, or changes in your skin before your appointment.

### FOR ALL LASH & BROW SERVICES
Here are a few things to keep in mind before your appointment:

- Please arrive with clean skin and lashes/brows free of makeup, mascara, and brow products.
- Avoid applying oils, heavy creams, or serums to the lash and brow area on the day of your appointment.
- Avoid using waterproof mascara or other stubborn eye makeup before your visit.
- Please avoid exfoliating products, retinoids, and harsh skincare treatments around the eye and brow area for 48 hours beforehand.
- Avoid excessive sun exposure or coming in with irritated, sunburned, or compromised skin.
- Please remove contact lenses before lash services if required for your treatment.
- Let me know if you've experienced any recent eye irritation, infections, allergic reactions, or sensitivity to lash and brow products.

### FOR CHEMICAL PEELS
To help prepare your skin and ensure the best treatment experience, please follow these pre-care instructions:

- Discontinue retinoids (Retin-A, tretinoin, Differin, etc.) for 5–7 days before your appointment, unless otherwise instructed.
- Avoid exfoliating products, including AHAs, BHAs, enzymes, scrubs, and at-home peels, for 5–7 days prior.
- Avoid waxing, threading, depilatories, and other aggressive hair removal treatments on the treatment area for at least 5–7 days.
- Avoid excessive sun exposure and tanning for at least one week before your appointment. Please do not come in with a sunburn.
- Keep your skincare routine simple and focus on gentle cleansing and moisturizing.
- Please let me know if you have started any new medications or skincare products, have experienced any recent skin irritation, or have had significant sun exposure.
