# Spain — contractor hiring guide

Country page in the Kleos country-guide cluster. Single self-contained HTML file: embedded
gross-to-net calculator, tax explainer, filing timeline, interactive misclassification
checklist, cases grid, FAQ, CTA.

| | |
|---|---|
| Built from | the Serbia page (`index.html`) as structural base |
| Status | content complete, **not cleared for publication** — see Open items |
| Currency | euros, deliberately (see NOTES.md) |
| Rules as of | 2026 |
| Build | 99,234 bytes, sha256 `bd032d4ec6ae914a…` |

Sources, workings and the full review record are in [NOTES.md](./NOTES.md).

---

## Do not edit

These carry over from the Figma export and the series conventions. Changing them breaks
either the round-trip to Figma or consistency with the other country pages.

- **The entire `<style>` block.** It is byte-identical to the Serbia page and must stay that
  way. Layout problems get solved in Figma, not here.
- **Class names.**
- **`data-node-id` attributes.** These map elements back to Figma via the html.to.design MCP.
  212 of the Serbia page's 216 are preserved; none were invented.
- **Order of the nine `<section>` elements.**
- **Entity style** — `&mdash;` `&ndash;` `&rsquo;` `&euro;` `&nbsp;` `&middot;` `&oacute;`.
  No raw `€` in the markup.

Safe to change: text inside blocks, the number of repeatable elements (cards, FAQ items,
timeline items, checklist rows), and the constants at the top of the script.

## Where the numbers live

All tax constants sit in one block at the top of `<script id="kleos-calc">`, each with a
source comment. To update for a new tax year, edit that block and nothing else:

```js
var RETA_RATE   = 0.315;      // 28.30 + 1.30 + 0.90 + 0.10 + 0.90 MEI
var RETA_TABLE  = [ … ];      // Orden PJC/297/2026
var IRPF_SCALE  = [ … ];      // state + default supplementary regional scale
var SAVINGS_SCALE = [ … ];    // Law 7/2024, top band from 2025
var CIT_SCALE   = [ … ];      // micro-enterprise scale, turnover under EUR 1m
var SOC_MIN_BASE = 1424.40;   // art. 308.1 LGSS, group 7 minimum
```

The calculator is validated against a published worked example: €40,000 invoiced with €8,000
of documented expenses gives a €1,356.21 base and ~€4,770 income tax, against €5,118 and
€4,775 as published. Income tax model is within €5.

Any figure appearing in prose **and** in the script must be changed in both places. The
current pairs are: 31.5%, €607.35, €5,550, 19/21% corporate, €1,424.40, and the €145,000
crossover in the first cases card.

## Known stopgaps

**1. Tab strip width — inline style, needs a real rule.**
`.calc__tab` is `width: 409px` with `justify-content: space-between`, sized for the Serbia
page's four tabs. Spain has two priceable regimes, and two 409px tabs leave a 426px hole in
the middle of a 1260px box. Carried as `style="width:620px"` on both tabs, marked
`<!-- STOPGAP -->` in the source. 2 × 620 + 20px gap = 1260px exactly. **Do not copy this
pattern to other country pages.**

**2. Third breakdown row is hidden, not absent.**
`style="display:none"` on one `.row` and one `.rows__sep`. The autónomo route uses two charge
rows and the company route three; the spare is hidden by the script rather than cloned at
runtime, so it is visible in the source and cannot fail on a missing node.

**3. Timeline is capped at four items by absolute positioning.**
`.yearlife` is `height: 1299px; overflow: hidden`, `.yearlife__card` sits at `top: 324px` and
`.warncard` at `top: 1040px` — 716px for the card. A fifth item pushes it past the warncard
and then clips. VeriFactu was moved out to the FAQ for this reason, and later dropped when
FAQ 8 was removed.

**4. No responsive handling.** Zero `@media` queries, no `<meta name="viewport">`, 73
fixed-pixel width rules. Inherited from the Figma export; present on all three country pages.
A one-line `<meta name="viewport" content="width=1440">` would at least make mobile scaling
predictable.

## Assets still needed

| Slot | Placeholder in markup |
|---|---|
| Hero image, 665×636 | `[ Screenshot 2026-04-01 at 10.42.22 — 665×636 ]` |
| CTA card background, 1708×1146 rotated | `PLACEHOLDER · background art` |
| Three cases-grid icons | `ic1`, `ic4`, `ic5` |

## Open items

**Blocking publication**

- [ ] **Legal sign-off on the article 43 sentence in FAQ 7.** The page states that Kleos
      employs in Spain through its own entity (confirmed by Dina, 11 Aug 2026) and that Spain
      restricts assigning workers to third parties. Two providers ranking on page one for
      "employer of record spain" argue publicly that the model is not lawful there. The
      wording says what Kleos does and why others decline; it does not conclude that the
      model is lawful. **Do not strengthen it into a compliance claim without Legal.**
      Source carries an `OPEN:` comment at that FAQ item.

**Should close first**

- [ ] Browser pass at 1440px. All geometry was verified arithmetically — Chromium could not
      be installed in the build environment. The warncard overlap in particular was fixed by
      trimming copy, not confirmed visually.
- [ ] Tab strip: replace the inline stopgap.
- [ ] BOE check: the published RETA table has 14 rows, every source describes 15 brackets.
- [ ] BOE check: published quotas in the middle rows sit €0.30–1.00 below base × 31.5%, while
      the top and bottom rows match exactly. The script computes from base × rate.
- [ ] Madrid's aggregate top marginal. Page uses 45% (24.5% state + 20.5% regional, which is
      arithmetically consistent and corroborated). One source gives 43.50%.
- [ ] Accident premium (AT/EP) for software and professional services. FAQ 7 says "plus an
      accident premium" with no figure because none was found.
- [ ] 2026 contribution freeze. One source reports rises of 0.11–0.26% across most brackets
      and up to €64.42/month in the top two, against the freeze under RD-ley 16/2025. Not
      asserted anywhere in the page copy — resolve before it is.

**Product and marketing decisions, not defects**

- [ ] Beckham Law is absent entirely. Flagged internally on 14 July as the reason Spain needs
      its own calculator page. Unverified, so not built. If the regime reaches self-employed
      people and not only employees, it is a genuine third calculator tab and this page should
      be revisited.
- [ ] Title and H1 currently target "hiring in Spain", which pulls job-seeker intent, plus
      "the 75% line", which is a term we coined and has no search volume. The two valuable
      clusters — Employer of Record (~830/mo, KD 3–10, CPC up to $267) and "permanent
      establishment spain" (1,300/mo, KD 6) — are addressed only in FAQ answers. Decide
      whether the page stays contractor-led or is rebalanced.
- [ ] No meta description. None of the three country pages has one.
- [ ] Two CTAs point at `#`: `ctacard__btn` and `footer__cta`. Inherited (Serbia has five,
      Georgia four); the primary buttons here are wired to `#calculator` and `#demo`.
- [ ] The segmented control does not show which mode is active. `.seg__btn` is the white pill
      and is hardcoded to the left option, so switching to "I want a target net" updates the
      field label and the hint but not the control. Fixable with an inline background toggle,
      or properly in Figma.
- [ ] No social proof anywhere — no client logos, no testimonials, no Kleos figures.
- [ ] The checklist loads with item 1 pre-ticked, following the Serbia pattern. It
      demonstrates interactivity but means the page opens by asserting the reader is over 75%.

## Verifying a change

Checks run against every build:

- `<style>` block byte-identical to the Serbia page
- nine `<section>` open/close pairs, all tags balanced inside `<body>`
- no invented `data-node-id`
- no raw `€` outside `<script>`
- element counts: 2 calculator tabs, 4 timeline items, 8 checklist rows, 3 cases cards,
  7 FAQ items, 3 tax panels, 3 stat tiles
- script parses, and both regime models return sane values across €0–€1,000,000
- every figure in prose cross-checked against the corresponding script constant
