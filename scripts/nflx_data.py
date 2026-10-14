"""NFLX Investment Committee data pull: live price, fundamentals, multi-year returns, technicals, portfolio context."""
import json, math, warnings
import yaml
import numpy as np
import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore")
T = "NFLX"
out = {}

tk = yf.Ticker(T)
info = tk.info or {}
keys = ["currentPrice", "regularMarketPrice", "previousClose", "marketCap", "enterpriseValue", "trailingPE", "forwardPE",
        "trailingEps", "forwardEps", "pegRatio", "trailingPegRatio", "priceToSalesTrailing12Months", "beta",
        "fiftyTwoWeekHigh", "fiftyTwoWeekLow", "fiftyDayAverage", "twoHundredDayAverage", "totalRevenue",
        "revenueGrowth", "earningsGrowth", "earningsQuarterlyGrowth", "grossMargins", "operatingMargins", "profitMargins",
        "returnOnEquity", "returnOnAssets", "totalCash", "totalDebt", "debtToEquity", "freeCashflow", "operatingCashflow",
        "sharesOutstanding", "heldPercentInstitutions", "heldPercentInsiders", "shortPercentOfFloat", "shortRatio",
        "targetMeanPrice", "targetHighPrice", "targetLowPrice", "targetMedianPrice", "numberOfAnalystOpinions",
        "recommendationKey", "ebitda", "enterpriseToEbitda", "currentRatio", "bookValue", "priceToBook"]
out["info"] = {k: info.get(k) for k in keys}

# Price history
h = tk.history(period="max", auto_adjust=True)
h.index = h.index.tz_localize(None)
c = h["Close"]
last = float(c.iloc[-1]); last_date = str(c.index[-1].date())
out["last_close"] = last; out["last_date"] = last_date

def ret(years):
    d = c.index[-1] - pd.DateOffset(years=years)
    s = c[c.index <= d]
    if s.empty: return None
    p0 = float(s.iloc[-1])
    tot = last / p0 - 1
    return {"start": p0, "total": tot, "cagr": (last / p0) ** (1 / years) - 1}
out["returns"] = {f"{y}y": ret(y) for y in (1, 3, 5, 10)}
ytd = c[c.index < pd.Timestamp(c.index[-1].year, 1, 1)]
out["ytd"] = last / float(ytd.iloc[-1]) - 1 if not ytd.empty else None

# drawdowns
def mdd(s):
    peak = s.cummax(); dd = s / peak - 1
    return float(dd.min()), str(dd.idxmin().date())
out["mdd_2022"] = mdd(c["2021-11-01":"2022-12-31"])
out["mdd_5y"] = mdd(c[c.index >= c.index[-1] - pd.DateOffset(years=5)])
out["dd_from_ath"] = last / float(c.max()) - 1; out["ath"] = float(c.max()); out["ath_date"] = str(c.idxmax().date())

# Technicals
sma = lambda n: float(c.rolling(n).mean().iloc[-1])
out["sma20"], out["sma50"], out["sma200"] = sma(20), sma(50), sma(200)
d = c.diff(); up = d.clip(lower=0).ewm(alpha=1/14).mean(); dn = (-d.clip(upper=0)).ewm(alpha=1/14).mean()
out["rsi14"] = float((100 - 100 / (1 + up / dn)).iloc[-1])
ema12 = c.ewm(span=12).mean(); ema26 = c.ewm(span=26).mean(); macd = ema12 - ema26; sig = macd.ewm(span=9).mean()
out["macd"], out["macd_signal"] = float(macd.iloc[-1]), float(sig.iloc[-1])
y1 = h[h.index >= h.index[-1] - pd.DateOffset(years=1)]
out["hi_52w"], out["lo_52w"] = float(y1["High"].max()), float(y1["Low"].min())
out["lo_52w_date"] = str(y1["Low"].idxmin().date()); out["hi_52w_date"] = str(y1["High"].idxmax().date())
out["low_3m"] = float(h["Low"][h.index >= h.index[-1] - pd.DateOffset(months=3)].min())
out["high_3m"] = float(h["High"][h.index >= h.index[-1] - pd.DateOffset(months=3)].max())
out["vol20_vs_vol50"] = float(h["Volume"].iloc[-20:].mean() / h["Volume"].iloc[-50:].mean())
out["last_30_closes"] = [round(float(x), 2) for x in c.iloc[-30:]]
# monthly closes last 24m for charts
m = c.resample("ME").last().iloc[-24:]
out["monthly_24"] = {str(k.date()): round(float(v), 2) for k, v in m.items()}
# RS vs SPY (12m)
spy = yf.Ticker("SPY").history(period="2y", auto_adjust=True)["Close"]; spy.index = spy.index.tz_localize(None)
out["spy_1y"] = float(spy.iloc[-1] / spy[spy.index <= spy.index[-1] - pd.DateOffset(years=1)].iloc[-1] - 1)
# beta 2y weekly
rets = pd.concat([c.pct_change(), spy.pct_change()], axis=1, join="inner").dropna().iloc[-504:]
rets.columns = ["n", "s"]
out["beta_2y_daily"] = float(rets.cov().iloc[0, 1] / rets["s"].var())
out["corr_spy_2y"] = float(rets.corr().iloc[0, 1])

# Financials
def frame(df):
    if df is None or df.empty: return {}
    df = df.copy(); df.columns = [str(x.date()) for x in df.columns]
    return df
inc, cf, bs = frame(tk.income_stmt), frame(tk.cashflow), frame(tk.balance_sheet)
qinc, qcf = frame(tk.quarterly_income_stmt), frame(tk.quarterly_cashflow)
def rows(df, names):
    r = {}
    for n in names:
        if isinstance(df, pd.DataFrame) and n in df.index:
            r[n] = {k: (None if pd.isna(v) else float(v)) for k, v in df.loc[n].items()}
    return r
out["annual_income"] = rows(inc, ["Total Revenue", "Gross Profit", "Operating Income", "Net Income", "Diluted EPS", "Diluted Average Shares", "Interest Expense"])
out["annual_cf"] = rows(cf, ["Operating Cash Flow", "Free Cash Flow", "Capital Expenditure", "Stock Based Compensation", "Repurchase Of Capital Stock"])
out["annual_bs"] = rows(bs, ["Total Assets", "Total Debt", "Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments", "Stockholders Equity", "Total Liabilities Net Minority Interest", "Current Assets", "Current Liabilities", "Retained Earnings"])
out["q_income"] = rows(qinc, ["Total Revenue", "Operating Income", "Net Income", "Diluted EPS"])
out["q_cf"] = rows(qcf, ["Operating Cash Flow", "Free Cash Flow", "Stock Based Compensation"])
try:
    ed = tk.earnings_dates
    if ed is not None:
        ed = ed.reset_index(); ed.iloc[:, 0] = ed.iloc[:, 0].astype(str)
        out["earnings_dates"] = ed.head(8).to_dict(orient="records")
except Exception as e:
    out["earnings_dates_err"] = str(e)
try:
    out["eps_trend"] = tk.eps_trend.to_dict() if tk.eps_trend is not None else None
    out["growth_est"] = tk.growth_estimates.to_dict() if tk.growth_estimates is not None else None
    out["earnings_est"] = tk.earnings_estimate.to_dict() if tk.earnings_estimate is not None else None
    out["revenue_est"] = tk.revenue_estimate.to_dict() if tk.revenue_estimate is not None else None
except Exception as e:
    out["est_err"] = str(e)
try:
    ih = tk.insider_transactions
    if ih is not None and not ih.empty:
        ih = ih.head(15).copy()
        for col in ih.columns: ih[col] = ih[col].astype(str)
        out["insider_tx"] = ih.to_dict(orient="records")
    ih2 = tk.insider_purchases
    if ih2 is not None: out["insider_purchases"] = ih2.astype(str).to_dict(orient="records")
    ihold = tk.institutional_holders
    if ihold is not None: out["inst_holders"] = ihold.head(10).astype(str).to_dict(orient="records")
except Exception as e:
    out["flow_err"] = str(e)

# Portfolio context
cfg = yaml.safe_load(open("my-portfolio.yaml", encoding="utf-8"))
tickers = [x["ticker"] for x in cfg["holdings"]]
px = {}
for t in tickers:
    try:
        hh = yf.Ticker(t).history(period="5d", auto_adjust=False)
        px[t] = float(hh["Close"].iloc[-1])
    except Exception:
        px[t] = None
total_cfg = cfg["portfolio_summary"]["total_portfolio_value_usd"]
cash_pct = cfg["portfolio_summary"]["cash_allocation_percent"]
pos = {x["ticker"]: x["shares"] * (px[x["ticker"]] or 0) for x in cfg["holdings"]}
eq = sum(pos.values())
cash = total_cfg * cash_pct / 100
tot = eq + cash
out["portfolio"] = {"prices": px, "values": pos, "equity": eq, "cash_cfg": cash, "total_live": tot,
                    "weights": {k: v / tot for k, v in pos.items()}}
json.dump(out, open("scripts/nflx_data.json", "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ["last_close", "last_date", "returns", "ytd", "mdd_2022", "mdd_5y", "dd_from_ath", "ath", "ath_date",
                                       "sma20", "sma50", "sma200", "rsi14", "macd", "macd_signal", "hi_52w", "hi_52w_date", "lo_52w", "lo_52w_date",
                                       "low_3m", "high_3m", "vol20_vs_vol50", "spy_1y", "beta_2y_daily", "corr_spy_2y"]}, indent=1, default=str))
print(json.dumps(out["info"], indent=1, default=str))
