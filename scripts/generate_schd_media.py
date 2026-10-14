#!/usr/bin/env python3
"""
DADAIC Investment Firm - Media Generator for SCHD Investment Committee Deliverables
Generates:
1. SCHD-Investment-Committee-Decision-Memo-Slide-EN-261005.pdf
2. SCHD-Investment-Committee-Decision-Memo-Slide-KR-261005.pdf
3. SCHD-Investment-Committee-Decision-Memo-Infographic-EN-261005.png
4. SCHD-Investment-Committee-Decision-Memo-Infographic-KR-261005.png
"""

import os
import sys
import subprocess
import urllib.parse

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCRATCH_DIR = r"C:\Users\bm021\.gemini\antigravity\brain\54e5acf0-c528-4e68-8e6f-1a8e8b47116b\scratch"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(ROOT, "DecisionMemo", "Media")

os.makedirs(SCRATCH_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

# Common CSS for 16:9 Slides (1920x1080)
SLIDE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

@page {
  size: 1920px 1080px;
  margin: 0;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', 'Noto Sans KR', sans-serif;
  background-color: #f8fafc;
  color: #1e293b;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.slide {
  width: 1920px;
  height: 1080px;
  page-break-after: always;
  page-break-inside: avoid;
  position: relative;
  padding: 50px 70px;
  overflow: hidden;
  background: radial-gradient(circle at 90% 10%, rgba(37, 99, 235, 0.08) 0%, transparent 45%),
              radial-gradient(circle at 10% 90%, rgba(16, 185, 129, 0.06) 0%, transparent 45%),
              #f8fafc;
  display: flex;
  flex-direction: column;
}

.slide-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 24px;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 14px;
}

.slide-title-wrap h2 {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 34px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.slide-title-wrap p {
  font-size: 15px;
  color: #64748b;
  margin-top: 4px;
  font-weight: 500;
}

.firm-tag {
  font-family: 'Outfit', sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: #2563eb;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  background: #eff6ff;
  padding: 6px 16px;
  border-radius: 20px;
  border: 1px solid #bfdbfe;
}

.slide-body {
  flex: 1;
  display: flex;
  gap: 24px;
}

.col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.col-2 {
  flex: 2;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 20px 24px;
  box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04), 0 8px 10px -6px rgba(15, 23, 42, 0.02);
}

.card-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.stat-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.stat-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.stat-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.stat-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 12px 14px;
}

.stat-label {
  font-size: 12px;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-val {
  font-family: 'Outfit', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  margin-top: 3px;
}

.stat-sub {
  font-size: 12px;
  color: #10b981;
  font-weight: 600;
  margin-top: 2px;
}

.badge-verdict {
  display: inline-block;
  padding: 6px 14px;
  background: #ecfdf5;
  color: #059669;
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.5px;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13.5px;
}

th {
  background: #f1f5f9;
  color: #334155;
  font-weight: 700;
  text-align: left;
  padding: 9px 12px;
  border-bottom: 2px solid #cbd5e1;
}

td {
  padding: 8.5px 12px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}

tr:nth-child(even) td {
  background: #f8fafc;
}

.bullet-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.bullet-list li {
  font-size: 13.5px;
  line-height: 1.5;
  color: #334155;
  position: relative;
  padding-left: 18px;
}

.bullet-list li::before {
  content: "•";
  position: absolute;
  left: 2px;
  color: #2563eb;
  font-weight: bold;
}

.slide-footer {
  margin-top: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: #94a3b8;
  border-top: 1px solid #e2e8f0;
  padding-top: 10px;
}
"""

def generate_slide_deck_en():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SCHD - Investment Committee Slide Deck (EN)</title>
<style>{SLIDE_CSS}</style>
</head>
<body>

<!-- SLIDE 1 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>SCHD: Executive Investment Verdict & Key Metrics</h2>
      <p>Schwab U.S. Dividend Equity ETF | NYSE Arca | DADAIC-IC-MEMO-SCHD-261005</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card" style="border-left: 5px solid #10b981;">
        <div class="card-title"><span>🏛️</span> Official Committee Verdict</div>
        <div style="margin-bottom: 12px;">
          <span class="badge-verdict">APPROVED: HIGH CONVICTION (STRATEGIC CORE BALLAST)</span>
        </div>
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
          Authorized high-conviction initiation of <strong>SCHD at 7.0% portfolio sizing (~$103,600 USD)</strong>. Serves as the premier institutional ballast, delivering pure non-tech factor diversification, low Beta (0.56), and an self-funding ~3.24% dividend cash flow stream.
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>🎯</span> Valuation & Price Targets (12-Month)</div>
        <div class="stat-grid-2">
          <div class="stat-box">
            <div class="stat-label">Current Market Price</div>
            <div class="stat-val">$32.72</div>
            <div class="stat-sub" style="color: #64748b;">NYSE Arca Close</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">12M Base Target Price</div>
            <div class="stat-val" style="color: #2563eb;">$37.00</div>
            <div class="stat-sub">+16.3% Total Return</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Conservative NAV Value</div>
            <div class="stat-val">$36.50</div>
            <div class="stat-sub">+11.6% Intrinsic Gap</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Approved Buy Range</div>
            <div class="stat-val" style="font-size: 20px; color: #059669;">$31.50 - $33.20</div>
            <div class="stat-sub">Prime Accumulation</div>
          </div>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>📊</span> Institutional ETF Fundamentals</div>
        <div class="stat-grid-4">
          <div class="stat-box">
            <div class="stat-label">Assets Under Mgmt</div>
            <div class="stat-val" style="font-size: 21px;">$107.9B</div>
            <div class="stat-sub">Massive Liquidity</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Expense Ratio</div>
            <div class="stat-val" style="font-size: 21px; color: #059669;">0.06%</div>
            <div class="stat-sub">Ultra-Low Cost</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Dividend Yield</div>
            <div class="stat-val" style="font-size: 21px; color: #2563eb;">3.24%</div>
            <div class="stat-sub">Quarterly USD Payout</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Asset Beta</div>
            <div class="stat-val" style="font-size: 21px; color: #059669;">0.56</div>
            <div class="stat-sub">Low Volatility</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-title"><span>🛡️</span> Strategic Role in Current Portfolio</div>
        <ul class="bullet-list">
          <li><strong>Zero Overlap with Mega-Cap Tech</strong>: Holds 0% of NVDA, GOOG, AMZN, MSFT, META, AMD, and TSM. Pure unadulterated factor complement.</li>
          <li><strong>Portfolio Beta Neutralizer</strong>: Drops overall account Beta from 1.54 down to 1.36, establishing high downside durability.</li>
          <li><strong>Dividend Cash Generation</strong>: Generates ~$3,350+ USD in annual cash dividends, creating steady dry powder without selling shares.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 1 of 7 | Executive Summary</span>
  </div>
</div>

<!-- SLIDE 2 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Strategic Investment Thesis & 4 Core Catalysts</h2>
      <p>Underlying Index Architecture & Secular Compounding Engine</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>⚙️</span> 1. Rules-Based Moat Selection</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          Tracks the <strong>Dow Jones U.S. Dividend 100 Index</strong>. Systematically weeds out fragile yield traps by requiring 10 consecutive years of dividend payments, high Return on Equity (>27% weighted), and high Cash Flow-to-Total Debt (>58%).
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>📈</span> 2. Unbroken 11.2% Dividend CAGR</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          Over the past 10 years, SCHD has grown its dividend payout at an annualized rate of <strong>+11.2% CAGR</strong>. Payout increased from ~$0.38 (split-adjusted) in 2014 to ~$1.11 in 2025, offering rapid yield-on-cost expansion.
        </p>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🌊</span> 3. Macro Capital Rotation Tailwind</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          With over $6.3 Trillion parked in U.S. Money Market Funds, Fed rate reductions toward 3.5%-4.0% will spark massive institutional rotation into high-quality dividend growth equities as cash yields compress.
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>🛡️</span> 4. Valuation Margin of Safety</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          SCHD constituents trade at a forward P/E of <strong>18.1x</strong>, representing a <strong>28% discount</strong> against the S&P 500 (25.1x) and a 45% discount against the Nasdaq 100 (33.0x). Massive buffer against equity multiple squeeze.
        </p>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 2 of 7 | Core Thesis</span>
  </div>
</div>

<!-- SLIDE 3 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>The 4 Great Masters' Evaluation Matrix</h2>
      <p>Institutional Synthesis of Divergent Philosophical Frameworks</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col-2">
      <div class="card">
        <table>
          <thead>
            <tr>
              <th style="width: 18%;">Master Lens</th>
              <th style="width: 18%;">Verdict / Rating</th>
              <th style="width: 32%;">Key Conviction & Evidence</th>
              <th style="width: 32%;">Core Red Flag & Inversion Risk</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Warren Buffett</strong><br><span style="font-size: 12px; color: #64748b;">Economic Moats</span></td>
              <td><span class="badge-verdict">Strong Buy</span></td>
              <td>Algorithmic Berkshire clone. 100 companies with 10-year dividend histories, high ROE (>27%), low debt, and wide moats (LMT, CVX, HD, TXN).</td>
              <td>Underperforms during speculative tech momentum bubbles; lacks AI hyperscaler growth kickers.</td>
            </tr>
            <tr>
              <td><strong>Charlie Munger</strong><br><span style="font-size: 12px; color: #64748b;">ROIC & Inversion</span></td>
              <td><span class="badge-verdict">Elite Compounder</span></td>
              <td>Index mathematically filters out unprofitable debt-laden value traps. 20%+ ROIC and conservative payout ratios (<50%).</td>
              <td>Financials exposure (~17.5%) must be monitored, but top holdings are diversified asset managers (BlackRock), not regional banks.</td>
            </tr>
            <tr>
              <td><strong>Peter Lynch</strong><br><span style="font-size: 12px; color: #64748b;">Stalwarts / PEG</span></td>
              <td><span class="badge-verdict">Ideal Stalwart Buy</span></td>
              <td>Yield of 3.24% plus 11.2% dividend CAGR delivers ~14.4% total return. Trades at PEG of ~1.2x normalized earnings.</td>
              <td>Dividend growth may slow to 5-7% during severe industrial recessions.</td>
            </tr>
            <tr>
              <td><strong>Market Technician</strong><br><span style="font-size: 12px; color: #64748b;">Chart & Support</span></td>
              <td><span class="badge-verdict">Dip-Buy Setup</span></td>
              <td>Trading at $32.72, holding above rising 200 SMA ($31.27) and strong horizontal support shelf ($31.80-$32.50).</td>
              <td>20 EMA ($33.28) and 50 SMA ($33.82) are overhead; breakout above $33.85 unleashes rally to $37.00.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="card" style="background: #f8fafc;">
        <div style="font-size: 14px; color: #334155; line-height: 1.5;">
          <strong>CIO Conflict Reconciliation</strong>: While aggressive growth investors might favor high-beta tech, the CIO enforces the rule: <em>never risk survivability for incremental beta</em>. Adding SCHD optimizes the portfolio's Sharpe ratio and protects against AI Capex digestion.
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 3 of 7 | Master Matrix</span>
  </div>
</div>

<!-- SLIDE 4 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Forensic Constituent Audit & Portfolio Quality</h2>
      <p>Underlying Fundamentals, Solvency Metrics & Top 10 Holdings</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🔍</span> Top 10 Holdings in SCHD</div>
        <table>
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Company Name</th>
              <th>Fund Weight</th>
              <th>P/E</th>
              <th>Div Yield</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>TXN</strong></td><td>Texas Instruments</td><td>4.2%</td><td>24.2x</td><td>2.8%</td></tr>
            <tr><td><strong>LMT</strong></td><td>Lockheed Martin</td><td>4.1%</td><td>15.5x</td><td>2.6%</td></tr>
            <tr><td><strong>ABBV</strong></td><td>AbbVie Inc.</td><td>4.1%</td><td>16.3x</td><td>3.2%</td></tr>
            <tr><td><strong>HD</strong></td><td>Home Depot</td><td>3.9%</td><td>24.1x</td><td>2.4%</td></tr>
            <tr><td><strong>CSCO</strong></td><td>Cisco Systems</td><td>3.8%</td><td>15.2x</td><td>2.9%</td></tr>
            <tr><td><strong>CVX</strong></td><td>Chevron Corp.</td><td>3.8%</td><td>12.8x</td><td>4.3%</td></tr>
            <tr><td><strong>AMGN</strong></td><td>Amgen Inc.</td><td>3.7%</td><td>14.9x</td><td>2.9%</td></tr>
            <tr><td><strong>BLK</strong></td><td>BlackRock Inc.</td><td>3.6%</td><td>21.0x</td><td>2.1%</td></tr>
            <tr><td><strong>PFE</strong></td><td>Pfizer Inc.</td><td>3.5%</td><td>10.5x</td><td>5.9%</td></tr>
            <tr><td><strong>AVGO</strong></td><td>Broadcom Inc.</td><td>3.4%</td><td>28.5x</td><td>1.3%</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🛡️</span> Forensic Balance Sheet Audit</div>
        <div class="stat-grid-2">
          <div class="stat-box">
            <div class="stat-label">Net Debt / EBITDA</div>
            <div class="stat-val" style="color: #059669;">1.72x</div>
            <div class="stat-sub">vs S&P 500 at 2.45x</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Free Cash Flow Yield</div>
            <div class="stat-val" style="color: #2563eb;">6.8%</div>
            <div class="stat-sub">vs S&P 500 at 3.9%</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Weighted ROE</div>
            <div class="stat-val" style="color: #059669;">27.8%</div>
            <div class="stat-sub">High Capital Efficiency</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Average Payout Ratio</div>
            <div class="stat-val">47.5%</div>
            <div class="stat-sub">Strong Safety Buffer</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-title"><span>🍰</span> Sector Allocations</div>
        <div style="font-size: 13.5px; color: #475569; line-height: 1.6;">
          Financials <strong>17.5%</strong> | Industrials <strong>16.8%</strong> | Healthcare <strong>15.6%</strong> | Consumer Staples <strong>12.2%</strong> | Energy <strong>11.4%</strong> | Information Tech <strong>10.8%</strong> | Consumer Discretionary <strong>8.6%</strong> | Others <strong>7.1%</strong>.
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 4 of 7 | Forensic Health</span>
  </div>
</div>

<!-- SLIDE 5 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Scenario-Based Valuation & 12-Month Targets</h2>
      <p>Institutional Modeling Across Bull, Base, and Bear Regimes</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col-2">
      <div class="card">
        <table>
          <thead>
            <tr>
              <th>Scenario</th>
              <th>Probability</th>
              <th>Valuation Driver</th>
              <th>12M Target</th>
              <th>Expected Total Return</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #f0fdf4;">
              <td><strong>Bull Case</strong></td>
              <td><strong>30%</strong></td>
              <td>Multiple expansion to 20.0x P/E + 12% Dividend Growth. Rotational wave into dividend value compounders.</td>
              <td><strong style="color: #059669; font-size: 18px;">$40.50</strong></td>
              <td><strong style="color: #059669;">+27.0%</strong> (incl. dividends)</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td><strong>Base Case</strong></td>
              <td><strong>55%</strong></td>
              <td>Earnings growth 7-8%, stable 18.5x P/E multiple + 8% Dividend Growth. Steady compounding.</td>
              <td><strong style="color: #2563eb; font-size: 18px;">$37.00</strong></td>
              <td><strong style="color: #2563eb;">+16.3%</strong> (incl. dividends)</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>Bear Case</strong></td>
              <td><strong>15%</strong></td>
              <td>Macro recession drag, P/E multiple compresses to 16.0x. Dividends fully maintained.</td>
              <td><strong style="color: #dc2626; font-size: 18px;">$30.00</strong></td>
              <td><strong style="color: #dc2626;">-5.1%</strong> (incl. dividends)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="card">
        <div class="card-title"><span>🎯</span> Probability-Weighted Target: <strong>$36.85 (+15.8% Total Return)</strong></div>
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
          Asymmetrical return-to-risk profile: The downside is capped by the attractive ~3.5%-4.0% yield support floor near $30.00, while the upside to $37.00 - $40.50 offers solid double-digit capital appreciation in addition to reliable quarterly distributions.
        </p>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 5 of 7 | Valuation Scenarios</span>
  </div>
</div>

<!-- SLIDE 6 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Tactical Execution & Portfolio Rebalancing Blueprint</h2>
      <p>Capital Sourcing from Leveraged ETFs & Concentration De-risking</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🔄</span> Rebalancing Execution Matrix</div>
        <table>
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Current</th>
              <th>Target</th>
              <th>Action</th>
              <th>Capital Flow</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #ecfdf5;">
              <td><strong>SCHD</strong></td>
              <td>0.0%</td>
              <td><strong>7.0%</strong></td>
              <td><strong>Initiate Buy</strong></td>
              <td><strong>+$103,600</strong></td>
            </tr>
            <tr>
              <td><strong>NVDA</strong></td>
              <td>24.2%</td>
              <td>20.5%</td>
              <td>Trim ~230 sh</td>
              <td>-$54,900</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>KORU</strong></td>
              <td>1.0%</td>
              <td>0.0%</td>
              <td>Full Exit (1,170 sh)</td>
              <td>-$15,100</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>TQQQ</strong></td>
              <td>0.9%</td>
              <td>0.0%</td>
              <td>Full Exit (165 sh)</td>
              <td>-$13,100</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>SOXL</strong></td>
              <td>0.1%</td>
              <td>0.0%</td>
              <td>Full Exit (17 sh)</td>
              <td>-$900</td>
            </tr>
            <tr>
              <td><strong>Cash</strong></td>
              <td>1.0%</td>
              <td>2.5%</td>
              <td>Deploy Buffer</td>
              <td>-$19,600</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🎯</span> Execution Tranches & Order Staging</div>
        <ul class="bullet-list">
          <li><strong>Tranche 1 (Immediate Entry)</strong>: Deploy <strong>4.0% ($59,200 / ~1,809 shares)</strong> at current market level ($32.72) to establish core position.</li>
          <li><strong>Tranche 2 (Limit Pullback)</strong>: Deploy <strong>3.0% ($44,400 / ~1,356 shares)</strong> via limit order at <strong>$32.00 - $32.25</strong> near 200 SMA support.</li>
          <li><strong>Blended Target Entry</strong>: <strong>$32.52</strong>.</li>
          <li><strong>Structural Stop-Loss</strong>: <strong>$29.80</strong> (Violation of $30 structural multi-year floor; max risk -8.4%).</li>
          <li><strong>Risk-to-Reward Ratio</strong>: <strong>1 : 2.82</strong> ($32.52 -> $37.00 vs $29.80).</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 6 of 7 | Rebalancing Matrix</span>
  </div>
</div>

<!-- SLIDE 7 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Macro Stress-Testing & Non-Negotiable Invalidation Trigger</h2>
      <p>Portfolio Survivability Shocks & Absolute Exit Directives</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>⚡</span> 3-Scenario Macro Stress Test</div>
        <table>
          <thead>
            <tr>
              <th>Shock Scenario</th>
              <th>Pre-Trade MDD</th>
              <th>Post-Trade MDD</th>
              <th>SCHD Protection</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>AI Capex Deceleration (-30% Tech Shock)</strong></td>
              <td style="color: #dc2626;">-38.4%</td>
              <td style="color: #059669;"><strong>-29.8%</strong></td>
              <td><strong>+8.6% Buffer</strong> (SCHD down <8%)</td>
            </tr>
            <tr>
              <td><strong>Higher-for-Longer Rates & Squeeze</strong></td>
              <td style="color: #dc2626;">-28.5%</td>
              <td style="color: #059669;"><strong>-21.2%</strong></td>
              <td><strong>+7.3% Buffer</strong> (Value rotation)</td>
            </tr>
            <tr>
              <td><strong>Geopolitical Shock & Energy Surge</strong></td>
              <td style="color: #dc2626;">-31.2%</td>
              <td style="color: #059669;"><strong>-24.5%</strong></td>
              <td><strong>+6.7% Buffer</strong> (11.4% Energy/Defense)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card" style="border: 2px solid #ef4444; background: #fff5f5;">
        <div class="card-title" style="color: #dc2626;"><span>⚠️</span> Non-Negotiable 100% Invalidation Trigger</div>
        <p style="font-size: 14px; color: #7f1d1d; line-height: 1.6; font-weight: 500;">
          Regardless of market sentiment or dividend yield, this position will be <strong>liquidated immediately in full (100% exit)</strong> if:
        </p>
        <blockquote style="margin-top: 10px; padding: 10px 14px; background: #fee2e2; border-left: 4px solid #ef4444; font-size: 13.5px; color: #991b1b; font-style: italic;">
          "The Dow Jones U.S. Dividend 100 Index fundamentally alters its methodology to abandon the 10-year consecutive dividend payment requirement or removes the ROE and cash flow quality screening criteria, OR the aggregate ETF annual dividend payout experiences two consecutive years of negative distribution growth."
        </blockquote>
      </div>
      <div class="card" style="background: #f8fafc;">
        <div style="font-size: 13px; color: #64748b; line-height: 1.5;">
          <strong>Published By</strong>: Chief Investment Officer (CIO), DADAIC Investment Firm<br>
          <strong>Document ID</strong>: DADAIC-IC-MEMO-SCHD-261005 | Strictly USD Denominated
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC Investment Committee Presentation</span>
    <span>Slide 7 of 7 | Stress Tests & Directives</span>
  </div>
</div>

</body>
</html>
"""
    filepath = os.path.join(SCRATCH_DIR, "slide_deck_light_en.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

def generate_slide_deck_kr():
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>SCHD - 투자위원회 공식 슬라이드 덱 (KR)</title>
<style>{SLIDE_CSS}</style>
</head>
<body>

<!-- SLIDE 1 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>SCHD: 투자위원회 최종 의결 및 핵심 지표 대시보드</h2>
      <p>슈왑 미국 배당 다우존스 ETF | NYSE Arca | DADAIC-IC-MEMO-SCHD-261005</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card" style="border-left: 5px solid #10b981;">
        <div class="card-title"><span>🏛️</span> 투자위원회 공식 의결 결과</div>
        <div style="margin-bottom: 12px;">
          <span class="badge-verdict">승인: 강력 매수 (APPROVED: HIGH CONVICTION / 코어 밸러스트)</span>
        </div>
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
          전체 포트폴리오의 <strong>7.0% (약 $103,600 달러 / 약 3,165주)</strong> 신규 편입 승인. AI 반도체 및 빅테크 쏠림(85% 이상)을 구조적으로 정화하고, 계좌 베타(1.54)를 낮추며 연간 약 $3,350 달러 이상의 무위험 현금 배당을 창출하는 핵심 안정추 역할.
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>🎯</span> 시나리오별 목표주가 및 매수가 밴드</div>
        <div class="stat-grid-2">
          <div class="stat-box">
            <div class="stat-label">현재 시장 주가</div>
            <div class="stat-val">$32.72</div>
            <div class="stat-sub" style="color: #64748b;">NYSE Arca 종가</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">12개월 기본 목표주가</div>
            <div class="stat-val" style="color: #2563eb;">$37.00</div>
            <div class="stat-sub">+16.3% 총 기대수익률</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">보수적 추정 내재가치</div>
            <div class="stat-val">$36.50</div>
            <div class="stat-sub">+11.6% 밸류에이션 갭</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">안전마진 매수 밴드</div>
            <div class="stat-val" style="font-size: 20px; color: #059669;">$31.50 ~ $33.20</div>
            <div class="stat-sub">최적 분할 매수 구간</div>
          </div>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>📊</span> 기관급 ETF 펀더멘털 핵심 지표</div>
        <div class="stat-grid-4">
          <div class="stat-box">
            <div class="stat-label">운용 자산 규모 (AUM)</div>
            <div class="stat-val" style="font-size: 21px;">$107.9B</div>
            <div class="stat-sub">압도적 유동성</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">연간 운용 보수</div>
            <div class="stat-val" style="font-size: 21px; color: #059669;">0.06%</div>
            <div class="stat-sub">초저비용 수수료</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">현재 배당 수익률</div>
            <div class="stat-val" style="font-size: 21px; color: #2563eb;">3.24%</div>
            <div class="stat-sub">분기별 USD 배당</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">개별 자산 베타</div>
            <div class="stat-val" style="font-size: 21px; color: #059669;">0.56</div>
            <div class="stat-sub">저변동성 방어력</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-title"><span>🛡️</span> 고객님 포트폴리오 맞춤 전략적 역할</div>
        <ul class="bullet-list">
          <li><strong>빅테크 종목 중복도 0%</strong>: NVDA, GOOG, AMZN, MSFT, META, AMD, TSM 미보유로 완벽한 독자적 팩터 다변화 달성.</li>
          <li><strong>초고베타 완화</strong>: 포트폴리오 전체 베타를 1.54에서 1.36으로 낮추어 하락장 최대 낙폭(MDD) 방어벽 구축.</li>
          <li><strong>현금흐름 자가 발전</strong>: 연간 약 $3,350 달러 이상의 배당금이 입금되어 주식 매도 없이 저점 매수 실탄 확보.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 1 / 7 | 의결 요약 대시보드</span>
  </div>
</div>

<!-- SLIDE 2 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>핵심 투자 논거 및 4대 투자 촉매</h2>
      <p>기초 지수 선별 알고리즘 및 장기 복리 성장 엔진</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>⚙️</span> 1. 룰베이스 경제적 해자 선별 시스템</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          <strong>다우존스 미국 배당 100 지수</strong> 추종. 10년 연속 배당 지급 기업 중 자기자본이익률(ROE > 27%), 부채 대비 현금흐름 비율(>58%)이 뛰어난 100개 우량 기업만을 기계적으로 엄선하여 부실 고배당 함정을 시스템적으로 차단.
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>📈</span> 2. 지난 10년간 연평균 배당성장률 11.2%</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          지난 10년간 주당 배당금이 연평균 <strong>+11.2% 복리 성장(CAGR)</strong>. 2014년 주당 약 $0.38 달러(분할 조정 기준)에서 2025년 약 $1.11 달러로 급성장하여 투자원금 대비 배당수익률(Yield on Cost)이 빠르게 극대화됨.
        </p>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🌊</span> 3. 머니마켓펀드(MMF) $6.3조 달러 이동 수혜</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          미국 머니마켓펀드에 대기 중인 약 $6.3조 달러의 막대한 현금이 연준의 기준금리 인하 국면에서 재투자 수익률 하락을 피해 기관 선호도 1위 배당성장 ETF인 SCHD로 대규모 유입되는 섹터 로테이션 수혜.
        </p>
      </div>
      <div class="card">
        <div class="card-title"><span>🛡️</span> 4. 28% 저평가된 밸류에이션 안전마진</div>
        <p style="font-size: 13.5px; color: #475569; line-height: 1.55;">
          SCHD 편입 기업들의 가중 선행 P/E는 <strong>18.1배</strong>로 S&P 500(25.1배) 대비 <strong>28% 할인</strong>되어 있으며 나스닥 100(33.0배) 대비 45% 저평가됨. 거시 긴축 및 기술주 멀티플 축소 시 단단한 하방 경직성 확보.
        </p>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 2 / 7 | 핵심 투자 논거</span>
  </div>
</div>

<!-- SLIDE 3 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>거장 심사역 & 마켓 테크니션 종합 평가 매트릭스</h2>
      <p>전설적 투자 철학의 교차 검증 및 CIO 최종 중재안</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col-2">
      <div class="card">
        <table>
          <thead>
            <tr>
              <th style="width: 18%;">거장 관점</th>
              <th style="width: 18%;">판정 / 등급</th>
              <th style="width: 32%;">핵심 확신 요인</th>
              <th style="width: 32%;">경고 신호 및 역발상 점검</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>워런 버핏</strong><br><span style="font-size: 12px; color: #64748b;">경제적 해자 & 안전마진</span></td>
              <td><span class="badge-verdict">적극 매수</span></td>
              <td>버크셔 포트폴리오의 알고리즘 복제판. 록히드마틴, 셰브론, 홈디포, 텍사스인스트루먼트 등 해자 기업 100개 보유.</td>
              <td>빅테크가 없으므로 유동성 투기 랠리 국면에서는 단기 상대 수익률이 뒤처질 수 있음.</td>
            </tr>
            <tr>
              <td><strong>찰리 멍거</strong><br><span style="font-size: 12px; color: #64748b;">ROIC 복리 & 역발상</span></td>
              <td><span class="badge-verdict">엘리트 복리머신</span></td>
              <td>지수 룰이 부실 기업을 기계적으로 제거. 가중 ROE 27% 상회 및 47%의 안전한 배당성향.</td>
              <td>금융주 비중(~17.5%)을 점검해야 하나, 블랙록 등 대형 자산운용사 중심이므로 부실 위험 제한적.</td>
            </tr>
            <tr>
              <td><strong>피터 린치</strong><br><span style="font-size: 12px; color: #64748b;">대형우량주 & 배당 킥</span></td>
              <td><span class="badge-verdict">대형우량주 매수</span></td>
              <td>배당 3.24%와 배당성장 11.2%의 결합으로 연 14.4% 총 기대수익 창출. 정규화 PEG 1.2배 수준.</td>
              <td>극심한 제조업 침체 시 배당성장률이 일시적으로 5~7%대로 둔화될 수 있음.</td>
            </tr>
            <tr>
              <td><strong>마켓 테크니션</strong><br><span style="font-size: 12px; color: #64748b;">차트 지지선 & 손익비</span></td>
              <td><span class="badge-verdict">눌림목 진입 타점</span></td>
              <td>현재가 $32.72는 상승 중인 200일선($31.27) 바로 위 강력한 매물대 지지 구간($31.80~$32.50).</td>
              <td>20일선($33.28)과 50일선($33.82) 돌파 시 12개월 목표가 $37.00을 향한 추세 랠리 전개.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="card" style="background: #f8fafc;">
        <div style="font-size: 14px; color: #334155; line-height: 1.5;">
          <strong>CIO 이견 조율 및 판정</strong>: 적극투자형 투자자라 하더라도 계좌의 생존과 샤프 비율을 희생하면서까지 기술주에 올인해서는 안 됩니다. SCHD는 포트폴리오의 하방 경직성을 확보하고 자본 복리를 지속 가능하게 만드는 필수 앵커입니다.
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 3 / 7 | 거장 평가 매트릭스</span>
  </div>
</div>

<!-- SLIDE 4 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>포렌식 건전성 감사 및 상위 10대 보유 종목</h2>
      <p>편입 기업 부채 건전성, 잉여현금흐름 창출력 및 섹터 배분</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🔍</span> SCHD 상위 10대 편입 종목 현황</div>
        <table>
          <thead>
            <tr>
              <th>티커</th>
              <th>기업 사명</th>
              <th>편입 비중</th>
              <th>선행 P/E</th>
              <th>배당수익률</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>TXN</strong></td><td>텍사스 인스트루먼트</td><td>4.2%</td><td>24.2배</td><td>2.8%</td></tr>
            <tr><td><strong>LMT</strong></td><td>록히드 마틴</td><td>4.1%</td><td>15.5배</td><td>2.6%</td></tr>
            <tr><td><strong>ABBV</strong></td><td>애브비</td><td>4.1%</td><td>16.3배</td><td>3.2%</td></tr>
            <tr><td><strong>HD</strong></td><td>홈디포</td><td>3.9%</td><td>24.1배</td><td>2.4%</td></tr>
            <tr><td><strong>CSCO</strong></td><td>시스코 시스템즈</td><td>3.8%</td><td>15.2배</td><td>2.9%</td></tr>
            <tr><td><strong>CVX</strong></td><td>셰브론</td><td>3.8%</td><td>12.8배</td><td>4.3%</td></tr>
            <tr><td><strong>AMGN</strong></td><td>암젠</td><td>3.7%</td><td>14.9배</td><td>2.9%</td></tr>
            <tr><td><strong>BLK</strong></td><td>블랙록</td><td>3.6%</td><td>21.0배</td><td>2.1%</td></tr>
            <tr><td><strong>PFE</strong></td><td>화이자</td><td>3.5%</td><td>10.5배</td><td>5.9%</td></tr>
            <tr><td><strong>AVGO</strong></td><td>브로드컴</td><td>3.4%</td><td>28.5배</td><td>1.3%</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🛡️</span> 포렌식 재무 건전성 분해</div>
        <div class="stat-grid-2">
          <div class="stat-box">
            <div class="stat-label">순부채 / EBITDA</div>
            <div class="stat-val" style="color: #059669;">1.72배</div>
            <div class="stat-sub">S&P 500(2.45배) 대비 우량</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">잉여현금흐름(FCF) 일드</div>
            <div class="stat-val" style="color: #2563eb;">6.8%</div>
            <div class="stat-sub">S&P 500(3.9%) 상회</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">가중평균 ROE</div>
            <div class="stat-val" style="color: #059669;">27.8%</div>
            <div class="stat-sub">최상위 자본 효율성</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">평균 배당성향</div>
            <div class="stat-val">47.5%</div>
            <div class="stat-sub">불황기 배당 방어력</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-title"><span>🍰</span> 섹터 분산 현황</div>
        <div style="font-size: 13.5px; color: #475569; line-height: 1.6;">
          금융 <strong>17.5%</strong> | 산업재 <strong>16.8%</strong> | 헬스케어 <strong>15.6%</strong> | 필수소비재 <strong>12.2%</strong> | 에너지 <strong>11.4%</strong> | IT <strong>10.8%</strong> | 경기소비재 <strong>8.6%</strong> | 기타 <strong>7.1%</strong>.
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 4 / 7 | 포렌식 건전성 감사</span>
  </div>
</div>

<!-- SLIDE 5 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>시나리오별 밸류에이션 및 12개월 목표주가</h2>
      <p>강세, 기준, 약세 3대 시나리오 정량 모델링</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col-2">
      <div class="card">
        <table>
          <thead>
            <tr>
              <th>시나리오</th>
              <th>발생 확률</th>
              <th>밸류에이션 동인</th>
              <th>12개월 목표주가</th>
              <th>총 기대수익률</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #f0fdf4;">
              <td><strong>Bull Case (강세)</strong></td>
              <td><strong>30%</strong></td>
              <td>가치주 로테이션 랠리, P/E 20.0배 확장 + 배당 성장 12%.</td>
              <td><strong style="color: #059669; font-size: 18px;">$40.50</strong></td>
              <td><strong style="color: #059669;">+27.0%</strong> (배당 포함)</td>
            </tr>
            <tr style="background: #eff6ff;">
              <td><strong>Base Case (기준)</strong></td>
              <td><strong>55%</strong></td>
              <td>이익 성장 7~8%, 안정적 18.5배 P/E + 배당 성장 8%. 꾸준한 복리 증식.</td>
              <td><strong style="color: #2563eb; font-size: 18px;">$37.00</strong></td>
              <td><strong style="color: #2563eb;">+16.3%</strong> (배당 포함)</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>Bear Case (약세)</strong></td>
              <td><strong>15%</strong></td>
              <td>경기 침체 우려, P/E 16.0배로 수축. 기존 배당 수준 방어.</td>
              <td><strong style="color: #dc2626; font-size: 18px;">$30.00</strong></td>
              <td><strong style="color: #dc2626;">-5.1%</strong> (배당 포함)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="card">
        <div class="card-title"><span>🎯</span> 확률 가중 기대 목표주가: <strong>$36.85 (총 기대수익률 +15.8%)</strong></div>
        <p style="font-size: 14px; color: #475569; line-height: 1.6;">
          비대칭적 손익비: $30.00 부근의 3.5%~4.0% 배당수익률 하방 지지선이 강력하게 작용하는 반면, $37.00 ~ $40.50 수준의 상방 잠재력과 분기별 달러 현금 배당이 결합되어 탁월한 리스크 대비 수익성을 제공합니다.
        </p>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 5 / 7 | 시나리오 밸류에이션</span>
  </div>
</div>

<!-- SLIDE 6 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>실전 리밸런싱 실행안 및 자본 조달 계획</h2>
      <p>3배 레버리지 정리 및 NVDA 차익 실현을 통한 최적 포트폴리오 재편</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🔄</span> 포트폴리오 리밸런싱 실행 매트릭스</div>
        <table>
          <thead>
            <tr>
              <th>티커</th>
              <th>현재 비중</th>
              <th>목표 비중</th>
              <th>실행 조치</th>
              <th>자금 흐름</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #ecfdf5;">
              <td><strong>SCHD</strong></td>
              <td>0.0%</td>
              <td><strong>7.0%</strong></td>
              <td><strong>신규 분할 매수</strong></td>
              <td><strong>+$103,600</strong></td>
            </tr>
            <tr>
              <td><strong>NVDA</strong></td>
              <td>24.2%</td>
              <td>20.5%</td>
              <td>일부 익절 (~230주)</td>
              <td>-$54,900</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>KORU</strong></td>
              <td>1.0%</td>
              <td>0.0%</td>
              <td>전량 매도 (1,170주)</td>
              <td>-$15,100</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>TQQQ</strong></td>
              <td>0.9%</td>
              <td>0.0%</td>
              <td>전량 매도 (165주)</td>
              <td>-$13,100</td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>SOXL</strong></td>
              <td>0.1%</td>
              <td>0.0%</td>
              <td>전량 매도 (17주)</td>
              <td>-$900</td>
            </tr>
            <tr>
              <td><strong>현금</strong></td>
              <td>1.0%</td>
              <td>2.5%</td>
              <td>버퍼 가용 투입</td>
              <td>-$19,600</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-title"><span>🎯</span> 주문 집행 단계 및 리스크 관리</div>
        <ul class="bullet-list">
          <li><strong>1차 진입 (즉시 매수)</strong>: 배정 자금의 <strong>4.0% ($59,200 달러 / 약 1,809주)</strong>를 현재가($32.72) 부근에서 집행하여 코어 비중 확보.</li>
          <li><strong>2차 진입 (눌림목 지정가)</strong>: 배정 자금의 <strong>3.0% ($44,400 달러 / 약 1,356주)</strong>를 <strong>$32.00 ~ $32.25</strong> 구간(200일선 지지대)에 대기 매수.</li>
          <li><strong>혼합 목표 평단가</strong>: <strong>$32.52</strong>.</li>
          <li><strong>구조적 손절 기준가</strong>: <strong>$29.80</strong> ($30 심리적 지지선 및 장기 추세선 이탈 시 손절, 최대 리스크 -8.4%).</li>
          <li><strong>손익비 (Risk/Reward)</strong>: <strong>1 : 2.82</strong> (목표가 $37.00 대 손절가 $29.80).</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 6 / 7 | 리밸런싱 실행안</span>
  </div>
</div>

<!-- SLIDE 7 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>거시 스트레스 테스트 및 타협 불가능한 엑시트 트리거</h2>
      <p>포트폴리오 생존성 시뮬레이션 및 100% 전량 매도 지침</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>
  <div class="slide-body">
    <div class="col">
      <div class="card">
        <div class="card-title"><span>⚡</span> 3대 거시 충격 스트레스 테스트</div>
        <table>
          <thead>
            <tr>
              <th>충격 시나리오</th>
              <th>편입 전 MDD</th>
              <th>편입 후 MDD</th>
              <th>SCHD 방어 효과</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>AI Capex 투자 둔화 (-30% 기술주 쇼크)</strong></td>
              <td style="color: #dc2626;">-38.4%</td>
              <td style="color: #059669;"><strong>-29.8%</strong></td>
              <td><strong>+8.6% MDD 방어</strong> (SCHD 하락폭 <8%)</td>
            </tr>
            <tr>
              <td><strong>금리 고공행진 & 유동성 수축</strong></td>
              <td style="color: #dc2626;">-28.5%</td>
              <td style="color: #059669;"><strong>-21.2%</strong></td>
              <td><strong>+7.3% MDD 방어</strong> (가치주 로테이션)</td>
            </tr>
            <tr>
              <td><strong>지정학적 공급망 충격 & 유가 급등</strong></td>
              <td style="color: #dc2626;">-31.2%</td>
              <td style="color: #059669;"><strong>-24.5%</strong></td>
              <td><strong>+6.7% MDD 방어</strong> (에너지/방산 11.4%)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="col">
      <div class="card" style="border: 2px solid #ef4444; background: #fff5f5;">
        <div class="card-title" style="color: #dc2626;"><span>⚠️</span> 타협 불가능한 100% 전량 매도 트리거</div>
        <p style="font-size: 14px; color: #7f1d1d; line-height: 1.6; font-weight: 500;">
          주가의 단기 등락이나 뉴스에 관계없이 다음 사건이 발생할 경우 <strong>보유 지분을 즉시 전량 매도(100% Exit)</strong>합니다:
        </p>
        <blockquote style="margin-top: 10px; padding: 10px 14px; background: #fee2e2; border-left: 4px solid #ef4444; font-size: 13.5px; color: #991b1b; font-style: italic;">
          "다우존스 미국 배당 100 지수(Dow Jones U.S. Dividend 100 Index)가 운용 원칙을 변경하여 '10년 연속 배당 지급' 요건을 완화하거나 '자기자본이익률(ROE) 및 현금흐름 건전성' 스크리닝 기준을 삭제하는 경우, 혹은 ETF의 연간 주당 배당금(Annual Payout)이 2년 연속 역성장하는 경우."
        </blockquote>
      </div>
      <div class="card" style="background: #f8fafc;">
        <div style="font-size: 13px; color: #64748b; line-height: 1.5;">
          <strong>발행 승인</strong>: DADAIC Investment Firm 최고투자책임자 (CIO)<br>
          <strong>문서 번호</strong>: DADAIC-IC-MEMO-SCHD-261005 | 전액 달러(USD) 표기 엄격 준수
        </div>
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <span>DADAIC 투자위원회 공식 프리젠테이션</span>
    <span>슬라이드 7 / 7 | 스트레스 테스트 및 엑시트 지침</span>
  </div>
</div>

</body>
</html>
"""
    filepath = os.path.join(SCRATCH_DIR, "slide_deck_light_kr.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

# Common CSS for Infographics (1200px width, ~3000px height)
INFOGRAPHIC_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@500;600;700;800;900&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', 'Noto Sans KR', sans-serif;
  background-color: #f1f5f9;
  color: #0f172a;
  width: 1200px;
  padding: 40px;
  margin: 0 auto;
}

.infographic-container {
  background: #ffffff;
  border-radius: 24px;
  box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.12);
  border: 1px solid #e2e8f0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding: 48px;
}

.header {
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 28px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.header h1 {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 38px;
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.header p {
  font-size: 16px;
  color: #64748b;
  margin-top: 6px;
  font-weight: 500;
}

.badge-firm {
  background: #eff6ff;
  color: #2563eb;
  padding: 8px 20px;
  border-radius: 30px;
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 1.5px;
  border: 1px solid #bfdbfe;
}

.section-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.stat-row-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.stat-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 20px 22px;
}

.stat-card-label {
  font-size: 13px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-card-val {
  font-family: 'Outfit', sans-serif;
  font-size: 32px;
  font-weight: 900;
  color: #0f172a;
  margin-top: 6px;
}

.stat-card-sub {
  font-size: 13px;
  color: #10b981;
  font-weight: 600;
  margin-top: 4px;
}

.content-box {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 24px 28px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14.5px;
}

th {
  background: #f1f5f9;
  color: #334155;
  font-weight: 700;
  text-align: left;
  padding: 12px 16px;
  border-bottom: 2px solid #cbd5e1;
}

td {
  padding: 12px 16px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}

tr:nth-child(even) td {
  background: #f8fafc;
}

.footer {
  border-top: 2px solid #e2e8f0;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: #64748b;
}
"""

def generate_infographic_en():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SCHD - Strategic Infographic (EN)</title>
<style>{INFOGRAPHIC_CSS}</style>
</head>
<body>

<div class="infographic-container">
  <div class="header">
    <div>
      <h1>🏛️ SCHD: STRATEGIC DECISION INFOGRAPHIC</h1>
      <p>Schwab U.S. Dividend Equity ETF | Institutional Due Diligence Dossier | DADAIC-IC-MEMO-SCHD-261005</p>
    </div>
    <div class="badge-firm">DADAIC INVESTMENT FIRM</div>
  </div>

  <!-- KEY STATS -->
  <div>
    <div class="section-title"><span>📊</span> 1. High-Conviction Core Ballast Dashboard</div>
    <div class="stat-row-4">
      <div class="stat-card" style="border-left: 5px solid #10b981;">
        <div class="stat-card-label">Official Verdict</div>
        <div class="stat-card-val" style="font-size: 22px; color: #059669;">APPROVED</div>
        <div class="stat-card-sub">Core Ballast (7.0% Sizing)</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">Market Price</div>
        <div class="stat-card-val">$32.72</div>
        <div class="stat-card-sub" style="color: #64748b;">P/E: 18.1x (28% Disc)</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">12M Base Target</div>
        <div class="stat-card-val" style="color: #2563eb;">$37.00</div>
        <div class="stat-card-sub">+16.3% Total Return</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">Dividend Yield</div>
        <div class="stat-card-val" style="color: #059669;">3.24%</div>
        <div class="stat-card-sub">11.2% 10Y Dividend CAGR</div>
      </div>
    </div>
  </div>

  <!-- 4 MASTERS CONSENSUS -->
  <div class="content-box">
    <div class="section-title"><span>🧠</span> 2. The 4 Great Masters' Philosophical Consensus</div>
    <table>
      <thead>
        <tr>
          <th>Master Lens</th>
          <th>Rating</th>
          <th>Key Conviction</th>
          <th>Inversion & Red Flag</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Warren Buffett</strong></td>
          <td><span style="color: #059669; font-weight: 700;">Strong Buy</span></td>
          <td>Algorithmic Berkshire clone. 100 wide-moat compounders (LMT, CVX, HD, TXN) with 10-year dividend histories and high ROE (>27%).</td>
          <td>Underperforms during speculative tech mania; holds zero mega-cap tech.</td>
        </tr>
        <tr>
          <td><strong>Charlie Munger</strong></td>
          <td><span style="color: #059669; font-weight: 700;">Elite Compounder</span></td>
          <td>Strict mathematical filters eliminate debt-laden value traps. Weighted ROE > 27% and conservative payout ratio (<50%).</td>
          <td>Financials exposure (~17.5%) requires scrutiny, but holdings are stable custodians (BlackRock).</td>
        </tr>
        <tr>
          <td><strong>Peter Lynch</strong></td>
          <td><span style="color: #059669; font-weight: 700;">Ideal Stalwart Buy</span></td>
          <td>3.24% yield + 11.2% dividend CAGR yields an implied ~14.4% total return. Trades at PEG of ~1.2x.</td>
          <td>Dividend growth could moderate to 5-7% during a prolonged industrial slowdown.</td>
        </tr>
        <tr>
          <td><strong>Market Technician</strong></td>
          <td><span style="color: #059669; font-weight: 700;">Dip-Buy Setup</span></td>
          <td>Consolidating at $32.72 above 200 SMA ($31.27); strong horizontal volume support ($31.80-$32.50).</td>
          <td>Stop-loss set at $29.80; offers superior 1:2.82 risk-to-reward ratio into $37.00 target.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- FORENSIC FUNDAMENTALS -->
  <div class="content-box">
    <div class="section-title"><span>🔍</span> 3. Forensic Portfolio Audit & Top Holdings</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <div>
        <h4 style="font-size: 16px; margin-bottom: 12px; color: #334155;">Top 6 Core Holdings in SCHD</h4>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 14px;">
          <li>• <strong>TXN (Texas Instruments)</strong>: 4.2% Weight | P/E 24.2x | Div Yield 2.8%</li>
          <li>• <strong>LMT (Lockheed Martin)</strong>: 4.1% Weight | P/E 15.5x | Div Yield 2.6%</li>
          <li>• <strong>ABBV (AbbVie Inc.)</strong>: 4.1% Weight | P/E 16.3x | Div Yield 3.2%</li>
          <li>• <strong>HD (Home Depot)</strong>: 3.9% Weight | P/E 24.1x | Div Yield 2.4%</li>
          <li>• <strong>CSCO (Cisco Systems)</strong>: 3.8% Weight | P/E 15.2x | Div Yield 2.9%</li>
          <li>• <strong>CVX (Chevron Corp.)</strong>: 3.8% Weight | P/E 12.8x | Div Yield 4.3%</li>
        </ul>
      </div>
      <div>
        <h4 style="font-size: 16px; margin-bottom: 12px; color: #334155;">Underlying Balance Sheet Fortress</h4>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 14px;">
          <li>• <strong>Net Debt / EBITDA</strong>: <strong>1.72x</strong> (vs S&P 500 at 2.45x)</li>
          <li>• <strong>Free Cash Flow Yield</strong>: <strong>6.8%</strong> (vs S&P 500 at 3.9%)</li>
          <li>• <strong>Cash Flow to Total Debt</strong>: <strong>58.4%</strong> (High solvency)</li>
          <li>• <strong>Average Dividend Payout Ratio</strong>: <strong>47.5%</strong> (Conservative safety buffer)</li>
          <li>• <strong>Sector Distribution</strong>: Financials 17.5%, Industrials 16.8%, Healthcare 15.6%, Tech 10.8%</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- REBALANCING MATRIX -->
  <div class="content-box">
    <div class="section-title"><span>🔄</span> 4. Tactical Portfolio Rebalancing Blueprint</div>
    <table>
      <thead>
        <tr>
          <th>Holding</th>
          <th>Pre-Weight</th>
          <th>Target Weight</th>
          <th>Execution Action</th>
          <th>Capital Flow ($)</th>
          <th>Strategic Rationale</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: #ecfdf5;">
          <td><strong>SCHD</strong></td>
          <td>0.0%</td>
          <td><strong>7.0%</strong></td>
          <td><strong>Initiate Buy (~3,165 sh)</strong></td>
          <td><strong>+$103,600</strong></td>
          <td>Core quality dividend anchor (Beta 0.56)</td>
        </tr>
        <tr>
          <td><strong>NVDA</strong></td>
          <td>24.2%</td>
          <td>20.5%</td>
          <td>Trim ~230 sh</td>
          <td>-$54,900</td>
          <td>De-risks single stock limit (<25% cap)</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>KORU</strong></td>
          <td>1.0%</td>
          <td>0.0%</td>
          <td>Full Exit (1,170 sh)</td>
          <td>-$15,100</td>
          <td>Eliminates 3x leveraged volatility drag</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>TQQQ</strong></td>
          <td>0.9%</td>
          <td>0.0%</td>
          <td>Full Exit (165 sh)</td>
          <td>-$13,100</td>
          <td>Eliminates redundant 3x tech leverage</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>SOXL</strong></td>
          <td>0.1%</td>
          <td>0.0%</td>
          <td>Full Exit (17 sh)</td>
          <td>-$900</td>
          <td>Eliminates redundant 3x semiconductor leverage</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- STRESS TEST & EXIT TRIGGER -->
  <div class="content-box" style="border: 2px solid #ef4444; background: #fff5f5;">
    <div class="section-title" style="color: #dc2626;"><span>⚠️</span> 5. Macro Stress Tests & The 100% Invalidation Trigger</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 14px;">
      <div>
        <strong style="color: #991b1b;">Portfolio Drawdown Mitigation:</strong>
        <p style="margin-top: 6px; color: #475569;">
          • AI Capex Shock (-30% Tech): Max Drawdown improves from <strong>-38.4% to -29.8%</strong> (+8.6% protection buffer).<br>
          • Rates Squeeze: Drawdown improves from <strong>-28.5% to -21.2%</strong>.<br>
          • Portfolio Beta drops from <strong>1.54 to 1.36</strong>.
        </p>
      </div>
      <div>
        <strong style="color: #991b1b;">Absolute 100% Exit Directives:</strong>
        <p style="margin-top: 6px; color: #475569;">
          Liquidate immediately in full if the Dow Jones U.S. Dividend 100 Index eliminates its 10-year consecutive dividend rule or removes ROE/cash flow filters, OR if the ETF's annual payout experiences two consecutive years of negative distribution growth.
        </p>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>DADAIC Investment Firm | Investment Committee Executive Deliverable</span>
    <span>Document ID: DADAIC-IC-MEMO-SCHD-261005 | Strictly USD ($) Denominated</span>
  </div>
</div>

</body>
</html>
"""
    filepath = os.path.join(SCRATCH_DIR, "infographic_light_en.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

def generate_infographic_kr():
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>SCHD - 전략적 인포그래픽 (KR)</title>
<style>{INFOGRAPHIC_CSS}</style>
</head>
<body>

<div class="infographic-container">
  <div class="header">
    <div>
      <h1>🏛️ SCHD: 투자위원회 전략적 최종 의결 인포그래픽</h1>
      <p>슈왑 미국 배당 다우존스 ETF | 기관급 정밀 실사 및 포트폴리오 리밸런싱 | DADAIC-IC-MEMO-SCHD-261005</p>
    </div>
    <div class="badge-firm">DADAIC INVESTMENT FIRM</div>
  </div>

  <!-- KEY STATS -->
  <div>
    <div class="section-title"><span>📊</span> 1. 고확신 코어 밸러스트 핵심 대시보드</div>
    <div class="stat-row-4">
      <div class="stat-card" style="border-left: 5px solid #10b981;">
        <div class="stat-card-label">최종 의결 결과</div>
        <div class="stat-card-val" style="font-size: 22px; color: #059669;">승인: 강력 매수</div>
        <div class="stat-card-sub">코어 밸러스트 (7.0% 편입)</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">현재 시장 주가</div>
        <div class="stat-card-val">$32.72</div>
        <div class="stat-card-sub" style="color: #64748b;">P/E 18.1배 (28% 할인)</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">12개월 기본 목표가</div>
        <div class="stat-card-val" style="color: #2563eb;">$37.00</div>
        <div class="stat-card-sub">+16.3% 총 기대수익률</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">현재 배당 수익률</div>
        <div class="stat-card-val" style="color: #059669;">3.24%</div>
        <div class="stat-card-sub">10년 배당성장 11.2% CAGR</div>
      </div>
    </div>
  </div>

  <!-- MASTERS CONSENSUS -->
  <div class="content-box">
    <div class="section-title"><span>🧠</span> 2. 거장 심사역 & 마켓 테크니션 종합 평가 및 합의</div>
    <table>
      <thead>
        <tr>
          <th>심사역 관점</th>
          <th>판정 / 등급</th>
          <th>핵심 확신 요인</th>
          <th>경고 신호 및 역발상 점검</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>워런 버핏</strong></td>
          <td><span style="color: #059669; font-weight: 700;">적극 매수</span></td>
          <td>버크셔의 알고리즘 복제판. 텍사스인스트루먼트, 록히드마틴, 애브비, 셰브론 등 해자 기업 100개 보유.</td>
          <td>광적인 기술주 투기 장세에서는 단기 상대 수익률이 뒤처질 수 있음.</td>
        </tr>
        <tr>
          <td><strong>찰리 멍거</strong></td>
          <td><span style="color: #059669; font-weight: 700;">엘리트 복리머신</span></td>
          <td>기계적 룰이 부실 고배당 함정을 배제. 가중평균 ROE 27% 상회 및 47%의 건전한 배당성향.</td>
          <td>금융주 비중(~17.5%)을 점검해야 하나, 블랙록 등 대형 금융사 중심이므로 부실 위험 제한적.</td>
        </tr>
        <tr>
          <td><strong>피터 린치</strong></td>
          <td><span style="color: #059669; font-weight: 700;">대형우량주 매수</span></td>
          <td>배당 3.24% + 배당성장 11.2%로 연 14.4% 총 기대수익 창출. 정규화 PEG 1.2배 수준.</td>
          <td>장기적인 제조업 침체 국면에서는 배당성장률이 5~7%대로 일시 둔화 가능.</td>
        </tr>
        <tr>
          <td><strong>마켓 테크니션</strong></td>
          <td><span style="color: #059669; font-weight: 700;">눌림목 매수 타점</span></td>
          <td>현재가 $32.72는 상승 중인 200일선($31.27) 바로 위 강력한 매물대 지지 구간($31.80~$32.50).</td>
          <td>손절가 $29.80 기준 목표가 $37.00 대비 1:2.82의 우수한 손익비 제공.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- FORENSIC FUNDAMENTALS -->
  <div class="content-box">
    <div class="section-title"><span>🔍</span> 3. 포렌식 재무 건전성 감사 및 상위 6대 종목</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <div>
        <h4 style="font-size: 16px; margin-bottom: 12px; color: #334155;">SCHD 상위 6대 핵심 편입 종목</h4>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 14px;">
          <li>• <strong>TXN (텍사스 인스트루먼트)</strong>: 4.2% 비중 | P/E 24.2배 | 배당률 2.8%</li>
          <li>• <strong>LMT (록히드 마틴)</strong>: 4.1% 비중 | P/E 15.5배 | 배당률 2.6%</li>
          <li>• <strong>ABBV (애브비)</strong>: 4.1% 비중 | P/E 16.3배 | 배당률 3.2%</li>
          <li>• <strong>HD (홈디포)</strong>: 3.9% 비중 | P/E 24.1배 | 배당률 2.4%</li>
          <li>• <strong>CSCO (시스코 시스템즈)</strong>: 3.8% 비중 | P/E 15.2배 | 배당률 2.9%</li>
          <li>• <strong>CVX (셰브론)</strong>: 3.8% 비중 | P/E 12.8배 | 배당률 4.3%</li>
        </ul>
      </div>
      <div>
        <h4 style="font-size: 16px; margin-bottom: 12px; color: #334155;">재무 건전성 및 잉여현금흐름 지표</h4>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 14px;">
          <li>• <strong>순부채 / EBITDA</strong>: <strong>1.72배</strong> (S&P 500의 2.45배 대비 우량)</li>
          <li>• <strong>잉여현금흐름(FCF) 수익률</strong>: <strong>6.8%</strong> (S&P 500의 3.9% 대비 우수)</li>
          <li>• <strong>부채 대비 현금흐름 비율</strong>: <strong>58.4%</strong> (탁월한 지급 능력)</li>
          <li>• <strong>평균 배당성향</strong>: <strong>47.5%</strong> (불황기 배당 삭감 방어벽)</li>
          <li>• <strong>섹터 배분</strong>: 금융 17.5%, 산업재 16.8%, 헬스케어 15.6%, IT 10.8%</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- REBALANCING MATRIX -->
  <div class="content-box">
    <div class="section-title"><span>🔄</span> 4. 실전 포트폴리오 리밸런싱 실행 매트릭스</div>
    <table>
      <thead>
        <tr>
          <th>보유 종목</th>
          <th>현재 비중</th>
          <th>목표 비중</th>
          <th>권장 실행 조치</th>
          <th>자금 흐름 ($)</th>
          <th>전략적 사유</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: #ecfdf5;">
          <td><strong>SCHD</strong></td>
          <td>0.0%</td>
          <td><strong>7.0%</strong></td>
          <td><strong>신규 분할 매수 (~3,165주)</strong></td>
          <td><strong>+$103,600</strong></td>
          <td>코어 퀄리티 배당 밸러스트 (베타 0.56)</td>
        </tr>
        <tr>
          <td><strong>NVDA</strong></td>
          <td>24.2%</td>
          <td>20.5%</td>
          <td>일부 차익 실현 (~230주)</td>
          <td>-$54,900</td>
          <td>단일 종목 한도(25%) 대비 리스크 완화</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>KORU</strong></td>
          <td>1.0%</td>
          <td>0.0%</td>
          <td>전량 매도 (1,170주)</td>
          <td>-$15,100</td>
          <td>3배 레버리지 국가 ETF 변동성 잠식 차단</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>TQQQ</strong></td>
          <td>0.9%</td>
          <td>0.0%</td>
          <td>전량 매도 (165주)</td>
          <td>-$13,100</td>
          <td>중복된 3배 기술주 레버리지 리스크 제거</td>
        </tr>
        <tr style="background: #fef2f2;">
          <td><strong>SOXL</strong></td>
          <td>0.1%</td>
          <td>0.0%</td>
          <td>전량 매도 (17주)</td>
          <td>-$900</td>
          <td>중복된 3배 반도체 레버리지 리스크 제거</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- STRESS TEST & EXIT TRIGGER -->
  <div class="content-box" style="border: 2px solid #ef4444; background: #fff5f5;">
    <div class="section-title" style="color: #dc2626;"><span>⚠️</span> 5. 거시 스트레스 테스트 및 100% 전량 매도 지침</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 14px;">
      <div>
        <strong style="color: #991b1b;">포트폴리오 최대 낙폭(MDD) 방어 효과:</strong>
        <p style="margin-top: 6px; color: #475569;">
          • AI Capex 둔화 (-30% 기술주 충격): 포트폴리오 MDD가 <strong>-38.4%에서 -29.8%로 개선</strong> (+8.6% 방어 효과).<br>
          • 금리 고공행진 충격: MDD <strong>-28.5%에서 -21.2%로 완화</strong>.<br>
          • 포트폴리오 베타 <strong>1.54에서 1.36으로 하향 안정화</strong>.
        </p>
      </div>
      <div>
        <strong style="color: #991b1b;">타협 불가능한 100% 전량 매도 트리거:</strong>
        <p style="margin-top: 6px; color: #475569;">
          다우존스 미국 배당 100 지수가 '10년 연속 배당' 또는 'ROE/현금흐름' 선별 기준을 삭제하거나, ETF의 연간 주당 배당금이 2년 연속 역성장할 경우 어떠한 예외 없이 보유 지분을 100% 즉시 전량 매도합니다.
        </p>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>DADAIC Investment Firm | 투자위원회 공식 최고 의결서</span>
    <span>문서 번호: DADAIC-IC-MEMO-SCHD-261005 | 전액 달러(USD) 표기 엄격 준수</span>
  </div>
</div>

</body>
</html>
"""
    filepath = os.path.join(SCRATCH_DIR, "infographic_light_kr.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

def render_media():
    print("[*] Generating HTML files...")
    slide_en = generate_slide_deck_en()
    slide_kr = generate_slide_deck_kr()
    info_en = generate_infographic_en()
    info_kr = generate_infographic_kr()

    print("[*] Compiling Media with Headless Chrome...")
    
    # 1. Slide Deck EN PDF
    pdf_en = os.path.join(MEDIA_DIR, "SCHD-Investment-Committee-Decision-Memo-Slide-EN-261005.pdf")
    cmd_slide_en = [
        CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_en}", slide_en
    ]
    print("  -> Rendering Slide EN PDF...")
    subprocess.run(cmd_slide_en, check=True)

    # 2. Slide Deck KR PDF
    pdf_kr = os.path.join(MEDIA_DIR, "SCHD-Investment-Committee-Decision-Memo-Slide-KR-261005.pdf")
    cmd_slide_kr = [
        CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_kr}", slide_kr
    ]
    print("  -> Rendering Slide KR PDF...")
    subprocess.run(cmd_slide_kr, check=True)

    # 3. Infographic EN PNG
    png_en = os.path.join(MEDIA_DIR, "SCHD-Investment-Committee-Decision-Memo-Infographic-EN-261005.png")
    cmd_info_en = [
        CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--window-size=1200,3100", f"--screenshot={png_en}", info_en
    ]
    print("  -> Rendering Infographic EN PNG...")
    subprocess.run(cmd_info_en, check=True)

    # 4. Infographic KR PNG
    png_kr = os.path.join(MEDIA_DIR, "SCHD-Investment-Committee-Decision-Memo-Infographic-KR-261005.png")
    cmd_info_kr = [
        CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--window-size=1200,3100", f"--screenshot={png_kr}", info_kr
    ]
    print("  -> Rendering Infographic KR PNG...")
    subprocess.run(cmd_info_kr, check=True)

    print("[+] All 4 media files rendered successfully!")

if __name__ == "__main__":
    render_media()
