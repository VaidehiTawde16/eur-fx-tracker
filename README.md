# 📈 EUR FX Tracker

An automated pipeline that pulls the latest **ECB euro reference rates** (via the
key-free [Frankfurter API](https://www.frankfurter.app/)), maintains a running history,
regenerates a trend chart, and refreshes this page. Runs on a schedule — every commit is a
real data update, not a placeholder.

**Stack:** Python · pandas · matplotlib · scheduled automation (Windows Task Scheduler / GitHub Actions).


<!--RATES_START-->
**ECB reference date:** 2026-07-06  ·  **Last refreshed:** 2026-07-07 09:11 UTC  ·  **Observations tracked:** 4

| Pair | Rate |
|------|------|
| EUR/USD | 1.1415 |
| EUR/GBP | 0.8554 |
| EUR/JPY | 185.3100 |
| EUR/CHF | 0.9201 |
| EUR/INR | 108.9035 |

![EUR rates](docs/eur_rates.png)
<!--RATES_END-->
