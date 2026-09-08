---
name: ghl-tracking
description: Add Google Tag Manager and conversion/engagement event tracking to a GoHighLevel page for The Body Temple Spa. Use when asked to add GTM, tracking, conversion events, dataLayer events, or analytics to a landing page or thank-you page, or to make a new funnel page match the tracking already on the facials and waxing pages.
---

# GHL tracking for The Body Temple Spa

Adds the spa's standard GTM container and dataLayer events to a GoHighLevel
page. Every funnel page should emit the same event names so one set of GTM
triggers and Google Ads conversions works across all of them.

## Container

GTM container ID: **GTM-PHFH5H6D** (same on every page).

Two snippets, pasted in GoHighLevel under **Settings → Tracking Code**:

- `ghl-clean-gtm-head.txt` → Head Tracking Code
- `ghl-clean-gtm-body.txt` → Body Tracking Code

These go in once per funnel, not once per page.

### Self-contained alternative

When the page must be a single paste, put a **guarded** copy of the loader at
the top of the page's own block instead, so no funnel-level setup is needed.
`GHL-waxing-thankyou.html` shows it: before injecting, the snippet walks
`document.getElementsByTagName('script')` and returns early if a
`googletagmanager.com/gtm.js` tag carrying the same container id is already
present. Without that guard, a page whose funnel already has the head snippet
loads the container twice and every conversion is counted twice. The plain
snippet in `ghl-clean-gtm-head.txt` has no guard, because in the Head slot
nothing can precede it.

## Page scripts

One script per page type, pasted into the page's **Footer Tracking Code**,
or appended inside the page's own HTML block:

| Page type | Reference file |
|---|---|
| Landing page | `ghl-clean-landing-footer.txt` |
| Thank-you page | `ghl-clean-thankyou-footer.txt` |
| Thank-you, sectioned price list | `ghl-clean-waxing-thankyou-footer.txt` |
| Landing, two modals and no data-cta | `ghl-clean-contouring-landing-footer.txt` |

The `tracking-*.html` files are the same scripts with explanatory comments,
kept for reference. The `ghl-clean-*.txt` files are what you actually paste.

## Adapting a script to a new page

Copy the closest existing script and change exactly these:

1. **`PAGE_SOURCE`** — `lp-<service>-athens`, e.g. `lp-waxing-athens`.
2. **`page_path`** in the conversion push — e.g. `/waxing-thank-you`.
3. **The root selector** — `document.querySelector('.btspa-waxty')`. Every page
   block has its own wrapper class; the script scopes all listeners to it so it
   cannot bind to another block on the same page. Keep the `|| document`
   fallback.

Leave everything else alone. The lead capture, phone normalisation and
attribution merge are identical across pages by design.

## Events

**Landing pages:** `form_submission`, `lead_form_abandon`, `exit_intent`,
`scroll_depth`, `engaged_time`, `section_view`, `faq_open`, `video_play`,
`phone_click`, `email_click`

**Thank-you pages:** `form_submission_confirmation` (fires on load, carries
`conversion: true` — this is the Google Ads conversion), `booking_click`,
`sms_to_book`, `service_view`, `phone_click`

`section_jump` is added on pages with in-page navigation.

## What every script does

- **Lead identity** — reads `first_name`, `email`, `phone` and friends from the
  URL, falls back to `sessionStorage.btw_lead`, normalises the phone to E.164
  (`+1XXXXXXXXXX`), and stores it back so later pages in the funnel have it.
- **Attribution** — captures `utm_*`, `gclid`, `fbclid`, merges them over
  anything already in `sessionStorage.btw_attr`, and attaches them to every
  event. This is what keeps a booking attributable to the ad that caused it.
- **Service-level detail** — `booking_click` and `sms_to_book` read the service
  name, price, duration and calendar URL out of the `.price-item` the button
  sits in, and send `value` and `currency: 'USD'` so revenue reporting works.
- **Everything is wrapped in try/catch.** Tracking must never break a page.

## Traps

- **Buttons that are not bookings.** In-page jump links reuse `.btn-book`. Skip
  any `href` starting with `#` and emit `section_jump` instead, or every scroll
  link is counted as a booking. The waxing script shows the guard.
- **Duplicate service names across sections.** When the same service appears in
  more than one section, key the `service_view` seen-set on
  `section + '|' + name`, not the name alone, or the second one never fires.
- **Wrapper class.** Copying a script without changing the root selector leaves
  it bound to nothing, and it fails silently.
- **Price parsing.** `.price` contains the `.unit` span; strip the unit text
  before parsing the number, or `value` comes out wrong.
- **Not every page fits the three-value swap.** The body contouring page uses
  an `id` wrapper rather than a class, opens two different modals from inline
  `onclick` handlers with no `data-cta` attributes, uses `.open` rather than
  `.is-open`, and has plain `<details>` instead of `.faq__item`. Check the
  page's actual markup before copying a script; where it differs, derive the
  CTA label from the button's section and read the service name out of the
  card it sits in.
- **More than one lead path.** When a page has both a booking calendar and an
  enquiry form, a single `form_submission` cannot tell them apart. Decide from
  which modal is open at the time and send `form_type`, so the assessment
  bookings and the pricing enquiries can be reported separately.

## Checks before handing it over

- `node --check` the script with the `<script>` tags stripped.
- Confirm `PAGE_SOURCE`, `page_path` and the root selector all name the new page.
- Confirm no `href="#..."` button can fire a booking event.
- Confirm the page's own tag balance is unchanged.
