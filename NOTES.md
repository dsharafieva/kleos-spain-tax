# Spain country guide — sources, decisions and review record

Everything behind the numbers on `index.html`: where each figure comes from, what was
checked, what was corrected, and what is still open. Kept in the repo so the next person
does not repeat the research.

Sections below, in the order they were produced: the original build notes, the expert
fact-check of 11 August, the legal review of 11 August, and the currency decision.

---

Built from `index.html` (Serbia) as the structural base. CSS block, class names,
`data-node-id` values and section order carried over unchanged.

## Verified against sources

| Figure | Value | Source |
|---|---|---|
| RETA rate | 31.5% (28.30 + 1.30 + 0.90 + 0.10 + 0.90 MEI) | Orden PJC/297/2026, BOE 31 Mar 2026 |
| RETA bases | 14 bracket rows, €653.59 – €1,928.10 | same |
| Quota range | €205.88 – €607.35 / month | base × 31.5% |
| Quotas frozen for 2026 | yes, only MEI rose 0.8% → 0.9% | RD-ley 16/2025 — **but one source disputes this**, reporting rises of 0.11–0.26% across most brackets and up to €64.42/month in the top two. Not stated anywhere in the page copy; resolve before it is |
| Starter rate | €80 headline, €88.64 with MEI | art. 38 ter Ley 20/2007 |
| Director's minimum base | €1,424.40 (was €1,000) | Orden PJC/297/2026 dropped the specific floor, so art. 308.1 LGSS reverts to group 7 of the General Regime |
| Generic expense deduction | 7%, or 3% for a director | art. 308.1.c) LGSS |
| Difficult-to-justify deduction | 5%, capped €2,000 | art. 30.2 IRPF Regulation |
| Personal allowance | €5,550 | LIRPF |
| Corporate tax, micro (<€1m) | 19% first €50,000, then 21% | Ley 7/2024 transitional scale |
| Savings scale | 19 / 21 / 23 / 27 / 30% | Ley 7/2024, top band from 2025 |
| Employer contributions | 30.65% + accident premium | Orden PJC/297/2026 |
| Contribution ceiling | €5,101.20 / month | same |
| Minimum wage | €1,221 × 14 = €17,094 | RD 126/2026, BOE 19 Feb 2026 |
| Misclassification fines | €3,750 – €12,000 per person | LISOS art. 22.2 and 40.1.e |
| Dismissal | 20 days/yr (cap 12mo), 33 if unfair (cap 24mo) | Workers' Statute |

**Calculator validated** against a published worked example: €40,000 invoiced with
€8,000 of documented expenses produces a €1,356.21 base and ~€4,770 of income tax,
against €5,118 and €4,775 as published. Income tax model is within €5.

## Stated assumptions in the calculator

- No documented business expenses. The conservative end; a real case will be lower.
- Income tax on the state scale plus the **default** supplementary regional scale.
  Real top marginal rates run 45% (Madrid) to 54% (Valencia); Navarra and the
  Basque Country do not use the state scale at all.
- Single filer, €5,550 allowance, no regional deductions.
- Company route assumes full distribution and no director's salary. Most one-person
  companies take a salary and distribute the rest, which lands between the two columns.
- Company route overtakes a plain autónomo at roughly **€145,000** of invoice on these
  assumptions. The note flips automatically above that point.

## Decisions taken

- **Two calculator tabs, not three or four.** Spain has three legal forms but only two
  tax outcomes: an ordinary autónomo and a TRADE pay identically. A TRADE tab would show
  duplicate numbers and imply a cost difference that does not exist.
- **TRADE moved to the checklist section** as the first item, because the 75% threshold is
  a function of the buyer's spend rather than the contractor's filings.
- **Checklist scores differently from Serbia.** Spain has no numbered statutory test, so the
  message does not count toward a pass mark. Item 1 is a bright line that creates a legal
  status; items 2–7 are indicia weighed as a whole.
- **Timeline kept at four items.** See the layout constraint below. VeriFactu moved to FAQ 8.
- **No region selector.** The template has no dropdown component and `.seg` holds two options.
  Assumption stated under the calculator instead. Selector is a v2 request.
- **Starter rate in the timeline, not a tab.** It is a 12-month discount, not a regime; as a
  tab it would invite anchoring a rate against a number that expires.
- **Employment reduced to one FAQ answer**, matching how Serbia and Georgia handle it.

## For the designer

1. **Tab strip needs a real fix.** `.calc__tab` is `width:409px` with
   `justify-content:space-between`, sized for four tabs. Two 409px tabs leave a 426px hole in
   the middle of a 1260px box. Carried as `style="width:620px"` inline on both tabs, marked
   `<!-- STOPGAP -->` in the source. 2 × 620 + 20px gap = 1260px exactly. Replace with a
   proper rule; do not copy the pattern to other pages.
2. **Timeline is capped at four items by absolute positioning.** `.yearlife` is
   `height:1299px; overflow:hidden`, `.yearlife__card` sits at `top:324px` and `.warncard` at
   `top:1040px` — 716px for the card. A fifth item pushes it to ~795px, running under the
   warncard and then clipping. Moving `.warncard` down is a CSS change and was not made.
3. **Layout verified arithmetically, not visually.** Chromium could not be installed (network
   allowlist), so no screenshot was taken. Worth one pass in a browser at 1440px.

## Open before publication

1. ~~**Does Kleos have a Spanish entity?**~~ **RESOLVED — confirmed by Dina, 11 August 2026.**
   FAQ 7 now states that Kleos employs in Spain through its own entity. Note for the record that
   the RemotePeople partner meeting notes of 16 July 2026 list Kleos entities as US / UK / Poland
   only; those notes are wrong or incomplete on Spain. What remains open is not the fact but the
   wording: the sentence about article 43 is a public position on a contested legal question and
   needs Legal sign-off. It says what Kleos does and why some providers decline to employ in
   Spain; it does not conclude that the model is lawful. Do not strengthen it into a compliance
   claim without Legal.
2. **Legal review of FAQ 3 (permanent establishment) and FAQ 7 (EOR).** Both are drafted
   deliberately short of a guarantee. Two page-one competitors argue publicly that EOR is not
   lawful in Spain under art. 43 of the Workers' Statute.
3. **RETA bracket count.** The published table has 14 rows; every source describes 15
   brackets. Needs the BOE text.
4. **Published quotas vs base × 31.5%.** The middle rows of the source table are €0.30–€1.00
   below base × 31.5%, while the top and bottom rows match exactly. The build computes from
   the base and the stated rate rather than copying figures that cannot be reproduced. Worth
   resolving against the BOE.
5. **Accident premium (AT/EP)** for software and professional services — not needed by the
   calculator now that the employee tab is gone, but FAQ 7 says "plus an accident premium"
   without a figure.
6. **Named enforcement cases.** FAQ 5 describes the Uber Eats and Engel & Völkers assessments
   without naming them. Naming is a decision above content.
7. **Beckham Law is absent entirely.** Aleksei flagged it on 14 July as the reason Spain needs
   its own calculator page. Unverified, so not built. If it reaches self-employed people and
   not only employees, it is a genuine third tab and this page should be revisited.

## Compliance flag, repeated from the Serbia build

The Johanna Hill demo transcript has a rep telling a prospect that if their accountant wants
specific invoice wording, "if you want to reduce your taxes using this invoices, it's something
that we can really help you with." The Alessandro Giovinazzo meeting notes summarise top-up
invoices as "useful for tax reduction purposes." Same pattern flagged last time. Nothing of the
kind is on this page. Worth someone senior addressing in sales enablement.

## Audit, 11 August 2026 — expert fact-check of the whole page

Two errors found and fixed, four editorial assumptions corrected, one live source conflict.

**Fixed:**
- Timeline said the post-flat-rate quota was "€3,592 and up". That came from the €1,166.70–1,300
  bracket, but the flat rate can only be extended below the minimum wage, so anyone who cannot
  extend is already in €1,300–1,700 (€3,632). Replaced with €5,435 on a €36,000 invoice, which
  matches the calculator exactly and needs no bracket reasoning.
- FAQ 7 said "The floor is €1,221 over fourteen payments" directly after the €5,101.20 base
  ceiling, which reads as a contribution-base floor. It is the minimum wage; the AT/EP base floor
  is €1,424.40. Reworded to "Minimum wage is €1,221 a month".

**Editorial assumptions corrected:**
- Bottom tile read "19–54%", mixing the supplementary-scale floor with a real regional top. Now
  "45–54%", the actual span of top marginal rates (Madrid to Valencia), both figures verified.
- "Common bracket — €426.54/month" removed. No source publishes the distribution of self-employed
  people across brackets, so "common" was unsupportable; and €426.54 is the published figure while
  the calculator computes base × 31.5% = €427. Now "At €2,500 net — €427/month", verifiable and
  consistent with the calculator.
- The €145,000 crossover is now attributed to the calculator's assumptions rather than stated as a
  fact about Spanish tax.
- The calculator note now names simplified direct estimation as the method assumed.

**Verified clean:** state scale 9.5–24.5% and its thresholds; Valencia 54% (two independent
sources plus arithmetic); the 19/24/30/37/45/47 table as state plus *supplementary* regional scale;
RETA 31.5% and its components; €607.35 ceiling; employer 30.65%; €5,101.20 cap; LISOS bands;
both enforcement cases; the cooperative history and STS 941/2025; article 43; article 11 of Law
20/2007; the TRADE 18-day right; 15% Spanish withholding; reverse charge and non-EU place of
supply; corporate 19/21%; savings scale. Page copy cross-checked against every JS constant.

**Open disagreement:** Madrid's aggregate top marginal. We use 45% (24.5% state + 20.5% regional,
corroborated). One source gives 43.50%. It is the only figure on the page a source contradicts.

## Currency: euros, decided 11 August 2026

The series rule discussed during the Serbia build was a single currency in USD. Spain stays in
euros. Reviewed and decided with Dina; recorded here so it is not reopened.

Where the series actually stands: **Serbia = USD** (26 `$` in copy, thresholds held in RSD and
converted at display via `RSD_PER_USD = 101.5`, NBS rate, disclosed in the footer).
**Georgia = GEL** (24 GEL references, no dollars). **Spain = EUR.** The single-currency rule is
live on one page of three, so Spain in euros is not the outlier Georgia is.

Reasons for euros here, in order of weight:

1. **Some figures are names, not amounts.** The €80 starter rate is called "la tarifa plana de 80
   euros" in the statute, the press and by every Spanish accountant. At $92 it stops being
   recognisable. Same for the €607.35 contribution ceiling, which is a hard statutory cap and is
   not a cap at any dollar figure.
2. **Converted penalties become uncheckable.** The LISOS bands are €3,750 / €7,500 / €9,600 /
   €12,000. Converted they read $4,326 / $8,651 / $11,074 / $13,842, none of which appears in
   article 40.1.e. This works directly against the page's accuracy positioning — the audit already
   catalogues Multiplier publishing Spanish contribution bases with dollar signs ("$1,519 and
   $5,611") as a competitor error, and converting would put us in the same visual place.
3. **Much of the audience is already in euros.** The RemotePeople partner meeting of 16 July 2026
   records the top EOR requests as Germany, Cyprus, Spain and Netherlands — three of four in the
   eurozone. For those buyers a dollar conversion is strictly worse.

Why Serbia's decision does not transfer: the dinar carries no intuition for an English-reading
buyer, so "8,000,000 RSD" → "$79,000" converts the unintelligible into the useful. Euros run the
other way. Serbia converts to aid comprehension; Spain would convert away from it.

**Suggested revision to the series rule:** show the country's own currency, and disclose any
conversion with a rate and a date. Serbia already does the second half in its footer ("work in
dinars if you are near a threshold"). Under that rule Serbia is an exception made for a reason,
not the standard the other pages must follow.

If the decision is ever reversed, use the Serbia architecture rather than hardcoding dollars:
thresholds stay in euros in the JS, a single `USD_PER_EUR` constant converts at display only, and
the footer carries the rate and date. ECB reference rate was 1.1535 on 7 August 2026 (market
1.1547 on 10 August). Scope of that change: 32 euro figures in visible copy, 14 `money()` calls in
the script, the input label and hint, and the footer disclaimer.

## Legal review, 11 August 2026

A second pass over the same page looking at characterisations, statutory attribution and
advice-boundary rather than at numbers. One genuine legal error, three characterisations tightened,
three gaps left open.

### Fixed — legal error

**The page contradicted itself on withholding.** FAQ 2 and the second cases card said a payer
outside Spain never withholds. Article 76.1.c) of the IRPF Regulation obliges non-residents that
operate in Spain **through a permanent establishment** to withhold; non-residents without a PE
withhold only on employment income and on other withholdable income that is a deductible expense
under article 24.2 TRLIRNR. Since FAQ 3 tells the reader a PE is possible, the two answers were
inconsistent. Both now condition the claim on the absence of a permanent establishment, and FAQ 2
says a PE would change it. The card title changed from "You never withhold anything" to
"You probably don't withhold".

### Fixed — characterisations

- "Regularising before an inspection reduces the penalty" → "can reduce it". The source says
  penalties can be cut, in some cases by up to half. It is not automatic.
- The cooperative answer credited the Labour Inspectorate with dissolving the largest billing
  cooperative. The disqualification was made by the Ministry under article 116 of Law 17/1999, on
  an Inspectorate report. Now "the authorities... disqualified it and wound it up".
- Two checklist messages drew a conclusion about the reader's own facts — "This reads as a genuine
  contractor relationship" and "Still reads as contracting". Both now describe the signals rather
  than classifying the arrangement.

### Open — for Legal, not fixable in copy

1. **FAQ 7, "we employ in Spain through our own entity, so you need neither."** Factually accurate
   as a statement of what the client must set up. The risk is adjacency: the next sentence is about
   article 43, and a reader may infer that using Kleos removes that exposure. It does not follow
   automatically — article 43 turns on who directs the work, so the client's own behaviour matters
   whoever the employer is. Recommend Legal either accepts the wording or adds a qualifier.
2. **FAQ 3 does not say the permanent establishment test is treaty-dependent.** The answer
   paraphrases the dependent-agent and fixed-place tests, which come from the applicable double tax
   treaty, with Spain's domestic rules in the Non-Resident Income Tax Act applying where there is
   no treaty. The answer sends the reader to a Spanish adviser, which covers it practically, but a
   reviewer may want the dependence made explicit.
3. **The page never says where a TRADE dispute is heard.** Chapter III of Law 20/2007 routes TRADE
   claims to the social courts rather than the commercial courts, with termination claims handled
   analogously to article 50 of the Workers' Statute. For a foreign buyer that is a material
   consequence of crossing 75% and it is currently absent. Gap, not an error.

### Checked and sound

Article 43 characterisation; article 11 conditions and the 75% definition; the LISOS bands and
their per-person counting; the four-year contribution recovery; the TRADE written contract and SEPE
registration; the 18 working days of annual interruption; the CJEU reference; the reverse charge
and the non-EU place-of-supply rule; the 15% Spanish professional withholding; the dismissal
figures; the statement that no at-will dismissal exists. Hero and footer both carry an explicit
"not legal advice" line, and the footer states that the Employer of Record position in Spain is
disputed.
