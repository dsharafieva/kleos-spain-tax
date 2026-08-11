# Add Spain country guide

Adds `spain/index.html` to the country-guide cluster, plus the sources and review record.

Built from the Serbia page as structural base. CSS block byte-identical, class names and
`data-node-id` attributes preserved (212 of 216, none invented), section order unchanged.

## What differs from Serbia and Georgia, and why

| | Serbia | Georgia | Spain | Reason |
|---|---|---|---|---|
| Calculator tabs | 4 | 3 | **2** | Spain has three legal forms but only two tax outcomes — an ordinary autónomo and a TRADE pay identically, so a TRADE tab would show duplicate numbers and imply a cost difference that does not exist |
| Misclassification section | 9 statutory criteria | — | **8 signals, no pass mark** | Spain has no numbered statutory test. Item 1 is a bright line that creates a legal status; items 2–8 are indicia weighed as a whole |
| Timeline items | 4 | 4 | **4** | capped by absolute positioning, see README |
| FAQ | 8 | 8 | **7** | the currency/recency answer was cut |
| Currency | USD | GEL | **EUR** | Spanish thresholds are set in euros and several are named legal figures. Full reasoning in NOTES.md |

TRADE is handled as a section rather than a tab because the 75% threshold is a function of the
buyer's spend, not the contractor's filings — the same logic that put Serbia's nine criteria in
their own section.

## Reviewers

**Legal — blocking.** FAQ 7 states that Kleos employs in Spain through its own entity, and that
Spain restricts assigning workers to third parties. Two providers ranking on page one for
"employer of record spain" argue publicly that the model is not lawful there. The wording states
what Kleos does and why others decline; it does not conclude the model is lawful. Please confirm
the wording or supply a qualifier. Do not strengthen it into a compliance claim.

Also worth a look: FAQ 3 paraphrases the permanent-establishment tests without saying they are
treaty-dependent, and the page does not mention that TRADE disputes are heard in the social
courts.

**Design.** Three items: the tab-strip inline stopgap needs a real rule; the page has never been
opened in a browser (geometry was verified arithmetically because Chromium could not be installed
in the build environment); the segmented control does not show which mode is active. Details in
`spain/README.md`.

**Ops / content.** Beckham Law is absent and unverified — if it reaches self-employed people and
not only employees it is a third calculator tab. Four BOE and rate checks are listed in the
README.

## Not in scope of this PR

Three placeholder assets (hero image, CTA background, three cases icons), the meta description,
and the two inherited CTAs pointing at `#`. The latter two affect all three country pages and are
probably better fixed across the cluster in one go.

## Separate from this page

Two sales-call transcripts contain language describing invoice wording for tax reduction. Same
pattern was flagged during the Serbia build. Nothing of the kind appears on this page, but it is
worth addressing in sales enablement.
