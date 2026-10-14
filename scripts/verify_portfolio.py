#!/usr/bin/env python3
"""
DADAIC Investment Firm - Real-Time Portfolio Verification & Weight Diagnostic
Reads my-portfolio.yaml, fetches live market prices via yfinance,
and calculates gross equity valuation and asset weights.
"""

import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import yaml
import yfinance as yf
import pandas as pd

def main():
    yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "my-portfolio.yaml")
    if not os.path.exists(yaml_path):
        print(f"[Error] Portfolio configuration not found at {yaml_path}", file=sys.stderr)
        sys.exit(1)

    with open(yaml_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    holdings = cfg.get("holdings", [])
    if not holdings:
        print("[Warning] No holdings found in my-portfolio.yaml")
        sys.exit(0)

    summary = cfg.get("portfolio_summary", {})
    investor = cfg.get("investor_profile", {})
    investor_name = investor.get("investor_name", "BM사장님")
    max_single_stock = investor.get("max_single_stock_weight", 25.0)

    print(f"================================================================================")
    print(f"🏛️ DADAIC Investment Firm - Live Portfolio Diagnostic ({investor_name})")
    print(f"================================================================================")
    print(f"Fetching real-time market data for {len(holdings)} holdings...")

    tickers = [h["ticker"] for h in holdings]
    ticker_str = " ".join(tickers)
    
    # Batch price lookup
    ticker_objs = yf.Tickers(ticker_str)
    
    records = []
    failed_tickers = []

    for h in holdings:
        t = h["ticker"]
        sh = h.get("shares", 0)
        price = 0.0
        
        try:
            t_obj = ticker_objs.tickers.get(t)
            if t_obj:
                fast = getattr(t_obj, "fast_info", None)
                if fast and getattr(fast, "last_price", None):
                    price = float(fast.last_price)
                else:
                    info = t_obj.info or {}
                    price = float(info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose") or 0.0)
        except Exception as e:
            pass

        if price <= 0.0:
            failed_tickers.append(t)
            price = 0.0

        val = sh * price
        records.append({
            "ticker": t,
            "shares": sh,
            "price": price,
            "value": val
        })

    total_equity_value = sum(r["value"] for r in records)

    # Calculate equity weights
    for r in records:
        r["weight"] = (r["value"] / total_equity_value * 100.0) if total_equity_value > 0 else 0.0

    # Sort descending by value
    records.sort(key=lambda x: x["value"], reverse=True)

    print("\n[Holdings Breakdown (Gross Equities)]")
    print(f"{'Ticker':<7} | {'Shares':>7} | {'Price ($)':>10} | {'Value ($)':>14} | {'Equity %':>9} | {'Alert':<10}")
    print("-" * 75)

    overweight_alerts = []
    for r in records:
        alert = ""
        if r["weight"] > max_single_stock:
            alert = "OVERWEIGHT"
            overweight_alerts.append((r["ticker"], r["weight"]))
        elif r["price"] == 0.0:
            alert = "NO PRICE"

        print(f"{r['ticker']:<7} | {r['shares']:>7} | ${r['price']:>9.2f} | ${r['value']:>13,.2f} | {r['weight']:>8.2f}% | {alert:<10}")

    print("-" * 75)
    print(f"Total Gross Equity Valuation: ${total_equity_value:,.2f} USD ({len(records)} Holdings)")

    # Optional cash / total assets display if present
    declared_total = summary.get("total_portfolio_value_usd")
    declared_cash_pct = summary.get("cash_allocation_percent")
    declared_cash_usd = summary.get("cash_usd")

    if declared_cash_usd is not None and declared_cash_usd != "":
        cash_val = float(declared_cash_usd)
        combined_total = total_equity_value + cash_val
        cash_pct = (cash_val / combined_total * 100) if combined_total > 0 else 0
        print(f"Cash Buffer (Declared USD):   ${cash_val:,.2f} USD ({cash_pct:.2f}%)")
        print(f"Total Portfolio Assets:       ${combined_total:,.2f} USD")
    elif declared_total is not None and declared_total != "":
        dec_tot = float(declared_total)
        implied_cash = dec_tot - total_equity_value
        implied_pct = (implied_cash / dec_tot * 100) if dec_tot > 0 else 0
        print(f"Declared Total Target:        ${dec_tot:,.2f} USD (Implied Cash: ${implied_cash:,.2f} / {implied_pct:.2f}%)")
    else:
        print("(Total portfolio managed on Gross Equity basis; Cash tracked externally by BM사장님)")

    if overweight_alerts:
        print(f"\n⚠️ [CRO Concentration Warning]:")
        for t, w in overweight_alerts:
            print(f"   - {t}: {w:.2f}% exceeds max single stock ceiling ({max_single_stock:.1f}%)")

    if failed_tickers:
        print(f"\n⚠️ [Price Fetch Warning]: Failed to fetch prices for: {', '.join(failed_tickers)}")

if __name__ == "__main__":
    main()
