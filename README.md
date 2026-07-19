# 📈 EUR FX Tracker

An automated pipeline that pulls the latest **ECB euro reference rates** (via the
key-free [Frankfurter API](https://www.frankfurter.app/)), maintains a running history,
regenerates a trend chart, and refreshes this page. Runs on a schedule — every commit is a
real data update, not a placeholder.

**Stack:** Python · pandas · matplotlib · scheduled automation (Windows Task Scheduler / GitHub Actions).


<!--RATES_START-->
**ECB reference date:** 2026-07-17  ·  **Last refreshed:** 2026-07-19 06:34 UTC  ·  **Observations tracked:** 6

| Pair | Rate |
|------|------|
| EUR/USD | 1.1435 |
| EUR/GBP | 0.8510 |
| EUR/JPY | 185.6500 |
| EUR/CHF | 0.9228 |
| EUR/INR | 110.1020 |

![EUR rates](docs/eur_rates.png)
<!--RATES_END-->
