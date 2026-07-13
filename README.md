# 📈 EUR FX Tracker

An automated pipeline that pulls the latest **ECB euro reference rates** (via the
key-free [Frankfurter API](https://www.frankfurter.app/)), maintains a running history,
regenerates a trend chart, and refreshes this page. Runs on a schedule — every commit is a
real data update, not a placeholder.

**Stack:** Python · pandas · matplotlib · scheduled automation (Windows Task Scheduler / GitHub Actions).


<!--RATES_START-->
**ECB reference date:** 2026-07-10  ·  **Last refreshed:** 2026-07-13 09:12 UTC  ·  **Observations tracked:** 5

| Pair | Rate |
|------|------|
| EUR/USD | 1.1430 |
| EUR/GBP | 0.8516 |
| EUR/JPY | 185.0200 |
| EUR/CHF | 0.9223 |
| EUR/INR | 108.9665 |

![EUR rates](docs/eur_rates.png)
<!--RATES_END-->
