#!/usr/bin/env python3
"""
DADAIC Investment Firm - Investment Committee Decision Tracker (Scorecard)
Reads DecisionMemo/decision-log.csv, fetches live market prices,
and computes return performance against memo price, entry bands, and 12M targets.
"""

import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import pandas as pd
import yfinance as yf

def main():
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DecisionMemo", "decision-log.csv")
    if not os.path.exists(log_path):
        print(f"[Error] Decision log not found at {log_path}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(log_path)
    if df.empty:
        print("[Warning] Decision log is empty.")
        sys.exit(0)

    print("================================================================================")
    print("🏛️ DADAIC Investment Firm - Historical Decision Performance Tracker")
    print("================================================================================")

    tickers = df["Ticker"].unique().tolist()
    ticker_objs = yf.Tickers(" ".join(tickers))

    current_prices = {}
    for t in tickers:
        p = 0.0
        try:
            t_obj = ticker_objs.tickers.get(t)
            if t_obj:
                fast = getattr(t_obj, "fast_info", None)
                if fast and getattr(fast, "last_price", None):
                    p = float(fast.last_price)
                else:
                    info = t_obj.info or {}
                    p = float(info.get("currentPrice") or info.get("regularMarketPrice") or 0.0)
        except Exception:
            pass
        current_prices[t] = p

    results = []
    for _, row in df.iterrows():
        t = row["Ticker"]
        curr_p = current_prices.get(t, 0.0)
        memo_p = float(row["Price_At_Memo"])
        target_p = float(row["Target_12M_Base"])
        stop_p = float(row["Stop_Loss"])

        ret_since_memo = ((curr_p - memo_p) / memo_p * 100.0) if memo_p > 0 and curr_p > 0 else 0.0
        target_upside = ((target_p - curr_p) / curr_p * 100.0) if curr_p > 0 else 0.0

        # Status check
        status = "IN_PLAY"
        if curr_p <= stop_p and curr_p > 0:
            status = "STOPPED_OUT"
        elif curr_p >= target_p and curr_p > 0:
            status = "TARGET_HIT"

        results.append({
            "Date": row["Date"],
            "Ticker": t,
            "Verdict": row["Verdict"],
            "Memo Price": memo_p,
            "Current Price": curr_p,
            "Return (%)": ret_since_memo,
            "12M Target": target_p,
            "Remain Upside (%)": target_upside,
            "Status": status
        })

    res_df = pd.DataFrame(results)

    print(f"\n{'Date':<10} | {'Ticker':<6} | {'Memo ($)':>9} | {'Live ($)':>9} | {'Return':>8} | {'12M Target':>10} | {'Status':<11}")
    print("-" * 75)
    for _, r in res_df.iterrows():
        ret_str = f"{r['Return (%)']:+.2f}%"
        print(f"{r['Date']:<10} | {r['Ticker']:<6} | ${r['Memo Price']:>8.2f} | ${r['Current Price']:>8.2f} | {ret_str:>8} | ${r['12M Target']:>9.2f} | {r['Status']:<11}")

    print("-" * 75)
    valid_returns = [r["Return (%)"] for r in results if r["Current Price"] > 0]
    if valid_returns:
        avg_ret = sum(valid_returns) / len(valid_returns)
        win_rate = (len([r for r in valid_returns if r > 0]) / len(valid_returns)) * 100.0
        print(f"Average Return Since Recommendation: {avg_ret:+.2f}% | Win Rate: {win_rate:.1f}% ({len(valid_returns)} Decisions)")

if __name__ == "__main__":
    main()
