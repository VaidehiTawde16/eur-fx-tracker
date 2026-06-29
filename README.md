# 📈 EUR FX Tracker

An automated pipeline that pulls the latest **ECB euro reference rates** (via the
key-free [Frankfurter API](https://www.frankfurter.app/)), maintains a running history,
regenerates a trend chart, and refreshes this page. Runs on a schedule — every commit is a
real data update, not a placeholder.

**Stack:** Python · pandas · matplotlib · scheduled automation (Windows Task Scheduler / GitHub Actions).


<!--RATES_START-->
**ECB reference date:** 2026-06-26  ·  **Last refreshed:** 2026-06-29 08:00 UTC  ·  **Observations tracked:** 2

| Pair | Rate |
|------|------|
| EUR/USD | 1.1401 |
| EUR/GBP | 0.8625 |
| EUR/JPY | 184.3000 |
| EUR/CHF | 0.9218 |
| EUR/INR | 107.6305 |

![EUR rates](docs/eur_rates.png)
<!--RATES_END-->
