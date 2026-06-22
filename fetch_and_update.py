# -*- coding: utf-8 -*-
"""
EUR FX Tracker — pull the latest ECB euro reference rates (Frankfurter API, no key),
append them to a running history, regenerate a trend chart, and refresh the README.
Every run does REAL work on REAL, changing data — so each commit is a genuine update.
"""
import json
import os
import urllib.request
from datetime import datetime, timezone

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
HIST = os.path.join(ROOT, "data", "rates_history.csv")
CHART = os.path.join(ROOT, "docs", "eur_rates.png")
README = os.path.join(ROOT, "README.md")
SYMBOLS = ["USD", "GBP", "JPY", "CHF", "INR"]
QUERY = "/v1/latest?base=EUR&symbols=" + ",".join(SYMBOLS)
HOSTS = ["https://api.frankfurter.dev", "https://api.frankfurter.app"]
UA = {"User-Agent": "eur-fx-tracker/1.0 (+github.com/VaidehiTawde16)"}


def fetch():
    last_err = None
    for host in HOSTS:
        for path in (QUERY, QUERY.replace("/v1", "")):   # new + legacy path
            try:
                req = urllib.request.Request(host + path, headers=UA)
                with urllib.request.urlopen(req, timeout=30) as r:
                    return json.loads(r.read().decode())
            except Exception as e:
                last_err = e
    raise RuntimeError(f"All FX endpoints failed: {last_err}")


def update_history(payload):
    row = {"date": payload["date"], **{s: payload["rates"].get(s) for s in SYMBOLS}}
    if os.path.exists(HIST):
        df = pd.read_csv(HIST)
    else:
        df = pd.DataFrame(columns=["date", *SYMBOLS])
    df = df[df["date"] != row["date"]]                 # idempotent: replace same date
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df = df.sort_values("date").tail(400).reset_index(drop=True)
    df.to_csv(HIST, index=False)
    return df


def make_chart(df):
    plot = df.tail(90).copy()
    plot["date"] = pd.to_datetime(plot["date"])
    fig, ax = plt.subplots(figsize=(9, 4.2))
    for s, c in zip(["USD", "GBP", "CHF"], ["#F2C811", "#29C5E8", "#D6409F"]):
        if s in plot:
            ax.plot(plot["date"], plot[s], label=f"EUR/{s}", lw=2, color=c)
    ax.set(title="ECB Euro reference rates — last 90 observations", xlabel="Date", ylabel="Rate")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(CHART, dpi=110); plt.close(fig)


def update_readme(df, payload):
    latest = df.iloc[-1]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    table = "| Pair | Rate |\n|------|------|\n" + "\n".join(
        f"| EUR/{s} | {latest[s]:.4f} |" for s in SYMBOLS if pd.notna(latest[s]))
    block = (f"<!--RATES_START-->\n"
             f"**ECB reference date:** {payload['date']}  ·  **Last refreshed:** {stamp}  ·  "
             f"**Observations tracked:** {len(df)}\n\n{table}\n\n"
             f"![EUR rates](docs/eur_rates.png)\n"
             f"<!--RATES_END-->")
    if os.path.exists(README):
        text = open(README, encoding="utf-8").read()
        import re
        text = re.sub(r"<!--RATES_START-->.*?<!--RATES_END-->", block, text, flags=re.DOTALL)
    else:
        text = HEADER + "\n\n" + block + "\n"
    open(README, "w", encoding="utf-8").write(text)


HEADER = """# 📈 EUR FX Tracker

An automated pipeline that pulls the latest **ECB euro reference rates** (via the
key-free [Frankfurter API](https://www.frankfurter.app/)), maintains a running history,
regenerates a trend chart, and refreshes this page. Runs on a schedule — every commit is a
real data update, not a placeholder.

**Stack:** Python · pandas · matplotlib · scheduled automation (Windows Task Scheduler / GitHub Actions).
"""


def main():
    payload = fetch()
    df = update_history(payload)
    make_chart(df)
    update_readme(df, payload)
    print(f"Updated: {payload['date']} | {len(df)} rows | EUR/USD={payload['rates']['USD']}")


if __name__ == "__main__":
    main()
