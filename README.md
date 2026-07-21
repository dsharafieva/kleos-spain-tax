# Kleos — Hiring a contractor in Spain (2026)

A self-contained landing page that shows companies and contractors exactly where
a Spanish contractor's money goes: gross invoice → social security → IRPF → net
in pocket. Built in the Kleos brand system, with an EN/ES toggle and an
interactive gross-to-net calculator.

Sister page to the Romania build — same structure, Spain's tax rules.

## Files

| File | What it is |
|------|------------|
| `index.html` | The entire page — styling, EN/ES copy, calculator logic. Opens standalone in any browser or on GitHub Pages, no build step. |
| `app.py` | Thin Streamlit wrapper that renders `index.html` full-width. |
| `README.md` | This file. |

## Run it

**Standalone (simplest):** open `index.html` in a browser.

**Streamlit prototype:**
```bash
pip install streamlit
streamlit run app.py
```

**GitHub Pages:** push the repo, enable Pages on the branch root — `index.html`
serves as-is.

## What the calculator models

Three contractor setups (regime tabs):

1. **Autónomo · year 1** — flat €80/mo social-security cuota (tarifa plana).
2. **Autónomo · established** — the 2026 income-based cuota bands + IRPF.
3. **SL company** — corporate tax on profit, then dividend tax on distributions.

Plus: a **region selector** (standard Spain scale vs Madrid) that changes IRPF,
a **new-company** toggle for the SL (15% corporate rate), and a **bidirectional**
mode — "I know the invoice" ↔ "I want a target net" (solved by binary search).

## Updating the tax rules each year

All parameters live in one place: the `TAX` object near the top of the
`<script>` block in `index.html`. Spanish rules shift almost every year, so treat
this as the annual maintenance point.

- **`retaBands`** — monthly social-security cuota by net-income band. Update when
  the RETA schedule changes (bands were frozen at 2025 levels for 2026).
- **`flatCuotaMonthly`** — first-year tarifa plana (€80).
- **`stateScale`** — IRPF state (escala estatal) brackets.
- **`regionScale`** — regional (autonómica) scales. `general` is the legal default
  (mirrors the state scale → combined 19/24/30/37/45/47); `madrid` is the
  Comunidad de Madrid 2026 scale. Add more communities as `{upTo, rate}` arrays.
- **`corpScale` / `corpNewco`** — SL corporate-tax micropyme scale and the
  new-company flat rate.
- **`savingsScale`** — dividend (base del ahorro) brackets, uniform nationwide.
- **`minimoPersonal`, `gastosDificil`, `retaComputableFactor`** — the €5,550
  personal allowance, the €2,000 flat expense deduction, and the 0.93 factor used
  to place income in a cuota band.

## Honest caveats

- **IRPF is state + region.** Only the standard scale and Madrid are modelled
  precisely. Higher-tax regions (Catalonia, Valencia) run several points above
  Madrid at middle incomes — flagged on the page, easy to add to `regionScale`.
- **The SL model is simplified.** It excludes the mandatory administrator salary,
  the administrator's own social security (~€330+/mo as autónomo societario) and
  accounting fees. Real SL cost is higher — stated in the UI.
- **MEI (~0.9%)** on the social-security base is excluded from the cuota figures.
- Every calculation carries a "verify with a gestor / asesor fiscal" note. This is
  an informational tool, not tax advice.

Rates as of 2026. Sources: AEAT (IRPF), TGSS / RDL 16-2025 (RETA bands),
Comunidad de Madrid autonomous scale, Impuesto sobre Sociedades 2026 micropyme
rates.
