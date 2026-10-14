"""NFLX quant layer: normalized earnings, DCF, scenarios, portfolio beta & 3-shock stress test."""
import json
import yfinance as yf

d = json.load(open("scripts/nflx_data.json"))
P = d["last_close"]
sh_out = d["info"]["sharesOutstanding"] / 1e9
res = {"price": P}

# --- Normalized earnings / FCF (strip $2.8B WBD termination fee received Q1'26) ---
q_fcf = d["q_cf"]["Free Cash Flow"]; q_sbc = d["q_cf"]["Stock Based Compensation"]
ttm_q = ["2026-06-30", "2026-03-31", "2025-12-31", "2025-09-30"]
ttm_fcf = sum(q_fcf[q] for q in ttm_q) / 1e9
ttm_sbc = sum(q_sbc[q] for q in ttm_q) / 1e9
res["ttm_fcf_reported"] = ttm_fcf
res["ttm_fcf_ex_fee"] = ttm_fcf - 2.8
res["ttm_sbc"] = ttm_sbc
res["ttm_true_fcf_ex_fee"] = ttm_fcf - 2.8 - ttm_sbc
qi = d["q_income"]
res["ttm_rev"] = sum(qi["Total Revenue"][q] for q in ttm_q) / 1e9
res["ttm_opinc"] = sum(qi["Operating Income"][q] for q in ttm_q) / 1e9
res["ttm_opm"] = res["ttm_opinc"] / res["ttm_rev"]
eps26_cons, eps27_cons = 3.5834, 3.80137
fee_eps = 1.23 - 0.76  # Q1 actual vs guide ~ fee contribution
res["eps26_underlying"] = eps26_cons - fee_eps
res["eps27"] = eps27_cons
res["pe_fwd27"] = P / eps27_cons
res["pe_und26"] = P / res["eps26_underlying"]
res["eps_cagr_25_27"] = (eps27_cons / 2.53) ** 0.5 - 1
res["peg_consensus"] = res["pe_fwd27"] / (res["eps_cagr_25_27"] * 100)
res["peg_conservative16"] = res["pe_fwd27"] / 16
ann = d["annual_cf"]
res["true_fcf_hist"] = {y[:4]: (ann["Free Cash Flow"][y] - ann["Stock Based Compensation"][y]) / 1e9 for y in ann["Free Cash Flow"] if ann["Free Cash Flow"][y]}
mcap = P * sh_out
res["mcap_b"] = mcap
res["true_fcf_yield_fy25"] = res["true_fcf_hist"]["2025"] / mcap
res["true_fcf_yield_ttm_ex_fee"] = res["ttm_true_fcf_ex_fee"] / mcap

# --- Conservative DCF (owner earnings) ---
fcf0 = 10.8   # FY2027E normalized true FCF ($B): ~$15.8B NI x ~70% conversion less SBC
g1, g2, gt, r = 0.13, 0.08, 0.03, 0.095   # 10Y UST ~5.3% -> 9.5% cost of equity
pv, f = 0.0, fcf0
for t in range(1, 11):
    if t > 1:
        f *= (1 + (g1 if t <= 5 else g2))
    pv += f / (1 + r) ** t
tv = f * (1 + gt) / (r - gt) / (1 + r) ** 10
net_debt = (14.4 - 9.1)
eq = pv + tv - net_debt
res["dcf"] = {"pv_fcf": pv, "pv_tv": tv, "equity_b": eq, "per_share": eq / (sh_out * 0.97)}  # 3% net buyback shrink by 2027
# P/E cross-check: 22x FY27E haircut EPS 3.80
res["pe_crosscheck"] = 22 * 3.80
res["intrinsic_blend"] = round((res["dcf"]["per_share"] + res["pe_crosscheck"]) / 2, 2)

# --- Scenarios ---
sc = {"Bull": (0.25, 26.0, 3.95), "Base": (0.50, 22.0, 3.80), "Bear": (0.25, 16.0, 3.45)}
res["scen"] = {k: {"p": p, "mult": m, "eps": e, "tp": m * e, "ret": m * e / P - 1} for k, (p, m, e) in sc.items()}
res["pw_target"] = sum(v["p"] * v["tp"] for v in res["scen"].values())
res["pw_ret"] = res["pw_target"] / P - 1

# --- Portfolio beta & stress ---
port = d["portfolio"]
w = port["weights"]; tot = port["total_live"]
betas = {}
for t in w:
    try:
        b = yf.Ticker(t).info.get("beta")
    except Exception:
        b = None
    betas[t] = b
lev_b = {"KORU": 3 * 1.2, "TQQQ": 3 * 1.2, "SOXL": 3 * 1.8, "SPY": 1.0, "QQQ": 1.15, "EWY": 1.1}
for k, v in lev_b.items():
    if betas.get(k) is None or k in ("KORU", "TQQQ", "SOXL"):
        betas[k] = v
for k in betas:
    if betas[k] is None:
        betas[k] = 1.5
res["betas"] = betas
res["port_beta"] = sum(w[t] * betas[t] for t in w)

cat = {"semi": ["NVDA", "AVGO", "AMD", "TSM", "MU", "SKHY"], "bigtech": ["GOOG", "AMZN", "MSFT", "META"],
       "lev": ["KORU", "TQQQ", "SOXL"], "index": ["SPY", "QQQ", "EWY"], "ai_infra": ["PLTR", "BE", "GEV", "IREN", "CRWV"],
       "defensive": ["LLY"], "nflx": ["NFLX"]}
res["cat_w"] = {k: sum(w[t] for t in v) for k, v in cat.items()}
res["cash_w"] = port["cash_cfg"] / tot
# shocks per holding (price change)
shocks = {
    "S1 AI Capex Digestion": {"semi": -0.45, "bigtech": -0.28, "KORU": -0.65, "TQQQ": -0.62, "SOXL": -0.85, "SPY": -0.20, "QQQ": -0.27, "EWY": -0.30, "ai_infra": -0.50, "defensive": -0.05, "nflx": -0.12},
    "S2 Geopolitical/Energy": {"semi": -0.35, "bigtech": -0.20, "KORU": -0.70, "TQQQ": -0.50, "SOXL": -0.75, "SPY": -0.17, "QQQ": -0.21, "EWY": -0.35, "ai_infra": -0.35, "defensive": -0.08, "nflx": -0.15},
    "S3 Higher-for-Longer": {"semi": -0.30, "bigtech": -0.22, "KORU": -0.55, "TQQQ": -0.55, "SOXL": -0.65, "SPY": -0.16, "QQQ": -0.21, "EWY": -0.22, "ai_infra": -0.45, "defensive": -0.10, "nflx": -0.25},
}
def shock_of(t, s):
    if t in s: return s[t]
    for k, v in cat.items():
        if t in v and k in s: return s[k]
    return -0.25
def stress(weights):
    return {n: sum(weights[t] * shock_of(t, s) for t in weights) for n, s in shocks.items()}
res["stress_now"] = stress(w)
# proposed: NFLX 340 -> 690 shares, funded by trimming 100 NVDA
pr = port["prices"]; vals = dict(port["values"])
vals["NFLX"] = 690 * pr["NFLX"]; vals["NVDA"] = (1500 - 100) * pr["NVDA"]
cash_new = port["cash_cfg"] + 100 * pr["NVDA"] - 350 * pr["NFLX"]
tot_new = sum(vals.values()) + cash_new
w2 = {k: v / tot_new for k, v in vals.items()}
res["stress_proposed"] = stress(w2)
res["port_beta_proposed"] = sum(w2[t] * betas[t] for t in w2)
res["nflx_w_proposed"] = w2["NFLX"]; res["nvda_w_proposed"] = w2["NVDA"]
res["semi_w_proposed"] = sum(w2[t] for t in cat["semi"]) 
res["cash_new"] = cash_new; res["tot_new"] = tot_new
res["trade"] = {"nflx_add_sh": 350, "nflx_add_usd": 350 * pr["NFLX"], "nvda_trim_sh": 100, "nvda_trim_usd": 100 * pr["NVDA"]}
json.dump(res, open("scripts/nflx_quant.json", "w"), indent=1)
print(json.dumps(res, indent=1))
