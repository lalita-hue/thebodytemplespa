# GoHighLevel pages

Paste-ready code for the GoHighLevel pages. Each file is markup + script only —
**none of them carry their own CSS.** The styling lives on the GHL page itself,
so each file must go into the element that already holds the current version of
that page. Pasting one onto a fresh blank page renders it as plain text.

Two wrappers, and they are not interchangeable:

| Wrapper | Used by |
|---|---|
| `.btspa` | landing pages |
| `.btspa-ty` | thank-you pages |

Check the first line before pasting. `btspa-ty` is a thank-you page.

## Files

| File | Goes on |
|---|---|
| `GHL-acne-landing.html` | `/acne-treatments-ga-landing-page` |
| `GHL-acne-thankyou.html` | `/acne-treatment-ga-thank-you-page` |
| `GHL-coaching-landing.html` | weight / functional longevity coaching landing page |
| `GHL-coaching-thankyou.html` | coaching thank-you page |
| `GHL-services-menu.html` | services menu page |
| `GHL-facials-thankyou-updated.html` | `/thank-you-page-facials-page` |
| `GHL-lymphatic-landing.html` | lymphatic drainage landing page |
| `GHL-pmu-thankyou.html` | permanent makeup thank-you page |

## Shared values

- GTM container: `GTM-PHFH5H6D`
- Phone: +1 (959) 400-9242 · 2350 Prince Ave, Athens, GA 30606
- Reviews: **400+** at 5.0. Visible copy uses `400+`; schema uses plain `400`,
  because a `+` invalidates `AggregateRating` and Google drops the stars.
- Lead form: `https://link.thebodytemplespas.com/widget/form/b3hDBYcxqESa0PF3ntL3`

## Tracking

Every page tags its events with a `source` so the campaigns can be told apart:

| Page | `source` |
|---|---|
| Acne | `lp-acne-athens` |
| Coaching / weight | `lp-weightloss-athens` |
| Facials | `lp-facials-athens` |

Events: `lead_form_open`, `form_submission`, `lead_form_abandon`,
`booking_click`, `sms_to_book`, `service_view`, `scroll_depth`,
`section_view`, `engaged_time`, `video_play`, `exit_intent`, `faq_open`,
`phone_click`, `email_click`.

A text is never reported as a booking. Calendar links fire `booking_click`;
`sms:` links fire `sms_to_book`.

The coaching page's form is served from `link.thebodytemplespas.com`, so its
postMessage origin check accepts that domain as well as `leadconnectorhq.com`.
Without it every submission is silently dropped.

## Testing — how to describe it

- **GI-MAP** is a *microbial* stool test. It measures the bacteria, yeast,
  parasites and pathogens in the gut and how much of each is present, plus
  digestion and gut-inflammation markers. Do not call it a DNA test.
- **Hair Sensitivity & Wellness Screen** is a 1,771-item bioresonance hair
  sample screen covering food and drink, non-food, metals, minerals, vitamins,
  additives, hormones, gut, digestion, sleep, stress and skin. Items are rated
  high / moderate / no reactivity; high is removed for 6–8 weeks, moderate 4–6.
  It is **not** hair tissue mineral analysis.
  The report states it is Complementary and Alternative Medicine, that it does
  not diagnose, and that it is not an allergy test. Pages must not claim
  otherwise, and must not describe it as "lab-based".

Product pages:
- GI-MAP — `/product-details-3747/product/gi-map-gut-microbiome-test`
- Hair screen — `/product-details-3747/product/hair-bioresonance-wellness-report`

## Google Ads constraints

- **Weight:** no pounds, no dress sizes, no timelines, no before-and-after
  photos, nothing implying guaranteed or rapid loss. The page sells
  understanding your metabolism, not losing a number.
- **GLP-1:** offered as part of coaching. No brand names on the page.
  US prescription-drug advertising is restricted and may require
  certification — confirm before running ads against that page.
- Coaching is not medical care. Both the footer and a FAQ say so.
- Avoid open-ended urgency. The $85 is written as a new-client rate, not a
  countdown.

## Known open items

- Alt text on the newest images is generic — nobody has described what they show.
- Acne and coaching share one lead form, so their GHL pipelines are merged.
  Duplicating the form in GHL would split them.
- The coaching booking slug is spelled `funtional-health` (missing a "c").
  Fixing it in GHL breaks any link using it.
- The services menu still prices Lip Liner & Soft Blend at $455, above Lip
  Blush at $350, while its own copy calls it the lightest lip option.
- `GHL-facials-thankyou-updated.html` carries a known defect: seven booking
  buttons open the wrong service's calendar. Corrections are listed in the
  session notes. Do not publish it before fixing them.
