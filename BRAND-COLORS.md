# The Body Temple Spa — Brand Colors

Sampled from the circular logo (dragonfly + wordmark on an apricot gradient).
Contrast ratios below are measured, not estimated.

## For a "primary / secondary brand color" form field

```
#C85A28, #EFA068
```

Terracotta goes first because these fields usually drive buttons and headers.
White on the logo's apricot measures **2.1:1** — far below the 4.5:1 readable
minimum — so an auto-generated button in that color would be hard to read.
Terracotta is the same hue (19° vs 25°), dark enough to carry white text.
If the tool only uses the colors decoratively, the order does not matter.

## From the logo

| Name | Hex | RGB | HSL | Use |
|---|---|---|---|---|
| Apricot Glow | `#EFA068` | 239, 160, 104 | 25° 81% 67% | The logo's core color. Gradients, illustration, large fills. |
| Ember Apricot | `#E58A4C` | 229, 138, 76 | 24° 75% 60% | Deepest point of the gradient. |
| Peach Veil | `#F9D2AC` | 249, 210, 172 | 30° 87% 83% | Soft backgrounds, cards. |
| Blush Cream | `#FDE8D4` | 253, 232, 212 | 29° 91% 91% | Page grounds. |
| Porcelain | `#FEF6EC` | 254, 246, 236 | 33° 90% 96% | The near-white outer edge. |
| Ink | `#12100E` | 18, 16, 14 | 30° 12% 6% | The wordmark. Body text. |

## Working colors

Not in the logo, but necessary: every logo color is a light tint, and none can
carry white text or small type.

| Name | Hex | RGB | Use |
|---|---|---|---|
| Terracotta | `#C85A28` | 200, 90, 40 | Buttons, links, accents |
| Terracotta Deep | `#A8481E` | 168, 72, 30 | Hover and pressed states |
| Espresso | `#1A1610` | 26, 22, 16 | Dark sections |
| Bone | `#EDE7DB` | 237, 231, 219 | Text on dark |
| Stone | `#8A7F6E` | 138, 127, 110 | Muted text on dark |
| Umber | `#7A6D5B` | 122, 109, 91 | Muted text on light |

## Measured contrast

| Pair | Ratio | WCAG |
|---|---|---|
| Ink on Porcelain | 17.7:1 | AAA |
| Ink on Blush Cream | 16.0:1 | AAA |
| Ink on Peach Veil | 13.4:1 | AAA |
| Bone on Espresso | 14.6:1 | AAA |
| Ink on Apricot Glow | 9.0:1 | AAA |
| Apricot Glow on Espresso | 8.5:1 | AAA |
| Umber on Porcelain | 4.7:1 | AA |
| Stone on Espresso | 4.6:1 | AA |
| White on Terracotta | 4.2:1 | AA large text only |
| Terracotta on Porcelain | 4.0:1 | AA large text only |
| White on Apricot Glow | 2.1:1 | fails — never do this |

Practical rules that follow:

- Keep white button text at **16px semibold or larger**. Terracotta clears AA
  for large text, not for small.
- Never put white or light type on Apricot Glow, Peach Veil, Blush Cream or
  Porcelain. Use Ink.
- Terracotta as *text* on a cream ground only works at heading sizes. For body
  copy on light backgrounds use Ink or Umber.

## Note

The terracotta already used across the site's landing pages is the logo's
apricot at the same hue, darkened. The pages and the logo match without anyone
having planned it, so there is nothing to reconcile.
