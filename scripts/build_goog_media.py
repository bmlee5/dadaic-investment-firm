#!/usr/bin/env python3
"""
DADAIC Investment Firm - Master Media Generator for GOOG (Alphabet Inc.)
Generates all 8 visual deliverables:
1. GOOG-Investment-Committee-Decision-Memo-Slide-EN-261008.html
2. GOOG-Investment-Committee-Decision-Memo-Slide-EN-261008.pdf
3. GOOG-Investment-Committee-Decision-Memo-Slide-KR-261008.html
4. GOOG-Investment-Committee-Decision-Memo-Slide-KR-261008.pdf
5. GOOG-Investment-Committee-Decision-Memo-Infographic-EN-261008.html
6. GOOG-Investment-Committee-Decision-Memo-Infographic-EN-261008.png
7. GOOG-Investment-Committee-Decision-Memo-Infographic-KR-261008.html
8. GOOG-Investment-Committee-Decision-Memo-Infographic-KR-261008.png
"""

import os
import sys
import subprocess

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(ROOT, "DecisionMemo", "Media")
os.makedirs(MEDIA_DIR, exist_ok=True)

# ------------------------------------------------------------------------------
# HIGH-READABILITY, SPACIOUS SLIDE CSS (1920x1080 Widescreen)
# ------------------------------------------------------------------------------
SLIDE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@500;600;700;800;900&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

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
  padding: 44px 64px;
  overflow: hidden;
  background: radial-gradient(circle at 90% 10%, rgba(37, 99, 235, 0.05) 0%, transparent 45%),
              radial-gradient(circle at 10% 90%, rgba(16, 185, 129, 0.06) 0%, transparent 45%),
              #f8fafc;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.slide-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 20px;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 14px;
}

.slide-title-wrap h2 {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 42px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.slide-title-wrap p {
  font-size: 19px;
  color: #64748b;
  font-weight: 500;
  margin-top: 4px;
}

.slide-badge {
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: #2563eb;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  padding: 8px 18px;
  border-radius: 9999px;
  letter-spacing: 0.5px;
}

.slide-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #e2e8f0;
  padding-top: 14px;
  font-size: 15px;
  color: #94a3b8;
  font-weight: 500;
}

.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 22px;
}

/* CARDS & GRIDS */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.card {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  padding: 24px 28px;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);
}

.card-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.card p, .card li {
  font-size: 18px;
  color: #334155;
  line-height: 1.65;
}

.stat-box {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  padding: 22px 24px;
  text-align: center;
}

.stat-label {
  font-size: 16px;
  color: #64748b;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.stat-val {
  font-family: 'Outfit', sans-serif;
  font-size: 36px;
  font-weight: 900;
  color: #0f172a;
}

.stat-sub {
  font-size: 15px;
  color: #10b981;
  font-weight: 600;
  margin-top: 4px;
}

.table-wrap {
  width: 100%;
  border-collapse: collapse;
  background: #ffffff;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
}

.table-wrap th {
  background: #f1f5f9;
  padding: 14px 18px;
  font-size: 17px;
  font-weight: 700;
  color: #334155;
  text-align: left;
  border-bottom: 2px solid #cbd5e1;
}

.table-wrap td {
  padding: 14px 18px;
  font-size: 17px;
  color: #334155;
  border-bottom: 1px solid #f1f5f9;
}

.badge-tag {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 700;
}
.badge-green { background: #dcfce7; color: #166534; }
.badge-blue { background: #dbeafe; color: #1e40af; }
.badge-amber { background: #fef3c7; color: #92400e; }
.badge-red { background: #fee2e2; color: #991b1b; }
"""

# ------------------------------------------------------------------------------
# SLIDE EN HTML GENERATOR
# ------------------------------------------------------------------------------
def generate_slide_en_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GOOG Investment Committee Decision Deck (English)</title>
<style>
{SLIDE_CSS}
</style>
</head>
<body>

<!-- SLIDE 1: COVER & VERDICT -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>DADAIC INVESTMENT COMMITTEE EXECUTIVE MEMO</h2>
      <p>Target Asset: GOOG | Alphabet Inc. (Class C Capital Stock, NASDAQ)</p>
    </div>
    <div class="slide-badge">MEETING DATE: OCTOBER 8, 2026</div>
  </div>

  <div class="slide-content">
    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); color: #ffffff; padding: 36px 44px; border-radius: 20px; display: flex; justify-content: space-between; align-items: center;">
      <div>
        <span style="background: #3b82f6; color: #ffffff; padding: 6px 14px; border-radius: 6px; font-size: 15px; font-weight: 800; letter-spacing: 1px;">OFFICIAL COMMITTEE VERDICT</span>
        <h1 style="font-family: 'Outfit'; font-size: 46px; font-weight: 900; margin: 12px 0 8px 0; color: #ffffff;">APPROVED: QUALITY COMPOUNDER WITH SIZE CAP</h1>
        <p style="font-size: 21px; color: #93c5fd; font-weight: 500;">Core Portfolio Engine • Maintain 600 Shares ($206,916 USD) • Freeze New Capital</p>
      </div>
      <div style="text-align: right; background: rgba(255,255,255,0.1); padding: 20px 32px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 16px; color: #cbd5e1; text-transform: uppercase;">Current Weight</div>
        <div style="font-family: 'Outfit'; font-size: 48px; font-weight: 900; color: #60a5fa;">12.87%</div>
        <div style="font-size: 15px; color: #cbd5e1;">#2 Largest Asset for BM사장님</div>
      </div>
    </div>

    <div class="grid-4">
      <div class="stat-box">
        <div class="stat-label">Current Market Price</div>
        <div class="stat-val">$344.86</div>
        <div class="stat-sub" style="color: #64748b;">Market Cap: $4.18 Trillion</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Conservative Intrinsic Value</div>
        <div class="stat-val">$395.00</div>
        <div class="stat-sub">+14.5% Intrinsic Upside</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">12-Month Base Target</div>
        <div class="stat-val">$420.00</div>
        <div class="stat-sub">+21.8% Expected Return</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Valuation Multiple (P/E)</div>
        <div class="stat-val">17.1x</div>
        <div class="stat-sub">PEG Ratio: 0.88 (< 1.0)</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 1 of 6</span>
  </div>
</div>

<!-- SLIDE 2: MULTI-YEAR EMPIRICAL VALIDATION -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>MULTI-YEAR EMPIRICAL VALIDATION SCORECARD</h2>
      <p>Mandatory Multi-Year Audited Reality Check (BM사장님 30-Year Veteran Protocol)</p>
    </div>
    <div class="slide-badge">AUDITED SEC EDGAR DATA</div>
  </div>

  <div class="slide-content">
    <table class="table-wrap">
      <thead>
        <tr>
          <th>Metric Category</th>
          <th>Multi-Year Audited Fact (USD)</th>
          <th>Benchmark / Sector Context</th>
          <th>Institutional Verdict</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1-Year Total Return</strong></td>
          <td><strong>+21.74%</strong> ($281.27 ➔ $344.86 USD)</td>
          <td>S&P 500: +24.5% / Tech Beta: +31.2%</td>
          <td><span class="badge-tag badge-green">Steady Compounding</span></td>
        </tr>
        <tr>
          <td><strong>3-Year Return & CAGR</strong></td>
          <td><strong>+177.67%</strong> (CAGR: <strong>+40.23%</strong> from $124.20)</td>
          <td>Outperformed 92% of Large-Cap Tech peers</td>
          <td><span class="badge-tag badge-green">Proven Alpha Engine</span></td>
        </tr>
        <tr>
          <td><strong>5-Year Return & CAGR</strong></td>
          <td><strong>+134.63%</strong> (CAGR: <strong>+18.43%</strong> from $146.98)</td>
          <td>Absorbed 2022 Fed rate hikes & DOJ litigation</td>
          <td><span class="badge-tag badge-green">Monetary Cycle Moat</span></td>
        </tr>
        <tr>
          <td><strong>Revenue Scale & Growth</strong></td>
          <td>2023: <strong>$307.4B</strong> ➔ 2025: <strong>$402.8B</strong> ➔ 2026E: <strong>$488.5B</strong></td>
          <td>Q2 2026 Revenue: $119.8B (+24% YoY)</td>
          <td><span class="badge-tag badge-blue">Accelerating Top-Line</span></td>
        </tr>
        <tr>
          <td><strong>Cloud Operating Leverage</strong></td>
          <td>Cloud Rev: <strong>$24.8B</strong> (+82% YoY) | OPM: <strong>35.6%</strong></td>
          <td>Surpassed AWS in incremental enterprise AI growth</td>
          <td><span class="badge-tag badge-blue">Enterprise Infrastructure</span></td>
        </tr>
        <tr>
          <td><strong>Balance Sheet Solvency</strong></td>
          <td>Cash/ST Inv: <strong>$242.47B</strong> vs LT Debt: <strong>$98.17B</strong></td>
          <td>Net Cash Surplus: <strong>+$144.30B USD</strong></td>
          <td><span class="badge-tag badge-green">Fortress Sovereign Health</span></td>
        </tr>
        <tr>
          <td><strong>Capital Allocation Shift</strong></td>
          <td>2026 CapEx: <strong>$195B - $205B</strong> | Q2 FCF: <strong>-$5.86B</strong></td>
          <td>Share buybacks temporarily paused for AI buildout</td>
          <td><span class="badge-tag badge-amber">Infrastructure Sprint</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 2 of 6</span>
  </div>
</div>

<!-- SLIDE 3: MASTER EVALUATORS -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>MASTER EVALUATION MATRIX: THE 5 MASTERS & TECHNICIAN</h2>
      <p>Synthesizing Value, Growth, Momentum, Asymmetry, Technical Setups, and Systematic Inversion</p>
    </div>
    <div class="slide-badge">PHILOSOPHICAL ARBITRATION</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">☕</span> Warren Buffett: Toll Road Moat
          <span class="badge-tag badge-green" style="margin-left: auto;">Fair Value Buy</span>
        </div>
        <p><strong>Core Moat</strong>: Google Search is the quintessential modern toll bridge (89.94% share). YouTube & Cloud create secondary tolls. $144.3B net cash surplus provides rock-solid defense.</p>
        <p style="margin-top: 6px; color: #b45309;"><strong>Red Flag</strong>: Halting buybacks and issuing $84.75B in equity/debt for $200B capex deviates from pure capital return. Current P/E is fair, not a 30% deep discount.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🧠</span> Charlie Munger: Lollapalooza
          <span class="badge-tag badge-blue" style="margin-left: auto;">Inversion Cleared</span>
        </div>
        <p><strong>Lollapalooza Moat</strong>: Android (3B+ users) + Chrome + YouTube + Cloud + Ironwood TPU7x form an impenetrable compounding flywheel where each node reinforces the other.</p>
        <p style="margin-top: 6px; color: #15803d;"><strong>Inversion Cleared</strong>: DOJ breakup was rejected by Judge Mehta in Dec 2025; AI Overviews monetize at parity; Cloud operating margin reached 35.6%.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">📈</span> Peter Lynch: Screaming Bargain
          <span class="badge-tag badge-green" style="margin-left: auto;">PEG 0.88 (&lt; 1.0)</span>
        </div>
        <p><strong>Growth Engine</strong>: Despite $4.18T scale, top-line surged 24% YoY in Q2 2026. Normalized forward P/E is only 19.5x against projected 22% EPS growth.</p>
        <p style="margin-top: 6px; color: #0284c7;"><strong>PEG Assessment</strong>: At <strong>0.88</strong>, Alphabet is the premier growth bargain among Mega-Caps, vastly cheaper than Apple (2.60) or Microsoft (1.45).</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🌊</span> Stanley Druckenmiller: Alpha
          <span class="badge-tag badge-blue" style="margin-left: auto;">3.4 : 1 Asymmetry</span>
        </div>
        <p><strong>18-Month Inflection</strong>: The market mispriced Google as an AI loser. Proprietary Ironwood TPUs deliver the lowest inference cost in tech, capturing enterprise workloads from AWS.</p>
        <p style="margin-top: 6px; color: #b45309;"><strong>Macro Watch</strong>: Persistent 5.28% long-term Treasury yields cap multiple expansion above 25x; sustained AI monetization execution is mandatory.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🎯</span> William J. O'Neil: CAN SLIM
          <span class="badge-tag badge-green" style="margin-left: auto;">Institutional Buy</span>
        </div>
        <p><strong>CAN SLIM Scorecard</strong>: Q2 GAAP net profit surged +294% (+28% adjusted). 3-Yr EPS CAGR +40.2%. Ironwood TPU7x & Waymo rollouts drive new highs with 5,000+ top institutional holders.</p>
        <p style="margin-top: 6px; color: #15803d;"><strong>Base Consolidation</strong>: Healthy -14.7% pullback from $404 ATH; finding strong accumulation above 200-DMA ($339.61). RS score resilient at 74.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">📐</span> Market Technician: Chart R:R
          <span class="badge-tag badge-blue" style="margin-left: auto;">1 : 3.8 Risk / Reward</span>
        </div>
        <p><strong>Trend & Volume Profile</strong>: Price resting on key institutional volume floor ($335-$338 USD) and 200-DMA. 14-day RSI (49.8) in prime neutral accumulation zone.</p>
        <p style="margin-top: 6px; color: #0284c7;"><strong>Trade Execution</strong>: Demand Floor: <strong>$335-$338</strong> | Target 1: <strong>$380</strong> | Target 2: <strong>$420</strong> | Stop Floor: <strong>$318</strong>. Asymmetric 1:3.8 R:R profile.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 3 of 6</span>
  </div>
</div>

<!-- SLIDE 4: ADVERSARIAL CRO BLIND AUDIT -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>ADVERSARIAL CRO BLIND AUDIT: 3 MANDATORY FATAL FLAWS</h2>
      <p>Independent Tail-Risk Guardian & Capital Preservation Directives</p>
    </div>
    <div class="slide-badge" style="color: #dc2626; background: #fef2f2; border-color: #fca5a5;">BINDING CRO DIRECTIVE</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card" style="border-top: 5px solid #dc2626;">
        <div class="card-title" style="color: #dc2626; font-size: 22px;">1. Negative FCF & Capex Drag</div>
        <p><strong>Audited Vulnerability</strong>: CapEx surged to $44.92B in Q2, driving GAAP FCF to -$5.86B and True FCF net of SBC to -$13.82B. Management guided 2026 CapEx to $195B - $205B.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>Downside Impact</strong>: If enterprise AI adoption slows, massive data center depreciation will suppress consolidated ROIC throughout 2027-2028.</p>
      </div>

      <div class="card" style="border-top: 5px solid #ea580c;">
        <div class="card-title" style="color: #ea580c; font-size: 22px;">2. Extreme Factor Overlap</div>
        <p><strong>Portfolio Correlation Audit</strong>: BM사장님 already owns 600 shares ($206,916 USD / 12.87% weight). Together with NVDA (21.50%), AMZN (10.11%), AVGO (7.84%), and AMD (6.95%), Mega-Tech/Semi exposure exceeds 69%.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>CRO Finding</strong>: Purchasing more GOOG today directly intensifies False Diversification and magnifies macro drawdown risk.</p>
      </div>

      <div class="card" style="border-top: 5px solid #d97706;">
        <div class="card-title" style="color: #d97706; font-size: 22px;">3. D.C. Circuit Antitrust Overhang</div>
        <p><strong>Legal Uncertainty</strong>: While Judge Mehta rejected the Chrome/Android breakup, the DOJ's July 2026 appeal seeks a total ban on distribution payments to Apple and mobile OEMs.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>Mitigating Anchor</strong>: A revenue-sharing ban would save Google $20B+ in TAC costs, but causes short-term distribution screen turbulence.</p>
      </div>
    </div>

    <div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 14px; padding: 20px 28px;">
      <div style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">
        🏛️ CRO BINDING SIZING RESTRICTION FOR BM사장님:
      </div>
      <p style="font-size: 18px; color: #334155; line-height: 1.6;">
        "Mechanical Factor Overlap Cap Applied: Current position of 12.87% ($206,916 USD) is ratified as a Tier-1 compounding anchor. However, fresh capital allocation to GOOG is strictly <strong>FROZEN</strong> at current price levels ($344.86). The hard allocation ceiling is set at <strong>15.0% ($240,000 USD)</strong>. New dry powder must be reserved for non-tech defensive assets."
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 4 of 6</span>
  </div>
</div>

<!-- SLIDE 5: VALUATION & TECHNICAL BLUEPRINT -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>VALUATION SCENARIOS & TECHNICAL TRADE BLUEPRINT</h2>
      <p>12-Month Price Targets, Key Moving Averages, and Risk-Reward Setup</p>
    </div>
    <div class="slide-badge">PROBABILITY-WEIGHTED MODEL</div>
  </div>

  <div class="slide-content">
    <div class="grid-2">
      <div>
        <table class="table-wrap">
          <thead>
            <tr>
              <th>Scenario</th>
              <th>Prob.</th>
              <th>Multiple & EPS</th>
              <th>Target ($)</th>
              <th>Return</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #f0fdf4;">
              <td><strong>Bull Case</strong></td>
              <td>25%</td>
              <td>24.0x / FY27E $20.50</td>
              <td><strong>$492.00</strong></td>
              <td><span class="badge-tag badge-green">+42.7%</span></td>
            </tr>
            <tr style="background: #eff6ff;">
              <td><strong>Base Case</strong></td>
              <td>55%</td>
              <td>21.0x / FY27E $20.00</td>
              <td><strong>$420.00</strong></td>
              <td><span class="badge-tag badge-blue">+21.8%</span></td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>Bear Case</strong></td>
              <td>20%</td>
              <td>16.5x / FY27E $18.50</td>
              <td><strong>$305.25</strong></td>
              <td><span class="badge-tag badge-red">-11.5%</span></td>
            </tr>
          </tbody>
        </table>
        <div style="margin-top: 14px; text-align: center; background: #f8fafc; padding: 14px; border-radius: 10px; border: 1px solid #e2e8f0;">
          <span style="font-size: 16px; color: #64748b; font-weight: 600;">EXPECTED PROBABILITY-WEIGHTED TARGET:</span>
          <span style="font-family: 'Outfit'; font-size: 24px; font-weight: 900; color: #2563eb; margin-left: 10px;">$415.05 USD (+20.4%)</span>
        </div>
      </div>

      <div class="card">
        <div class="card-title">Technical Support & Execution Blueprint</div>
        <ul style="padding-left: 20px; display: flex; flex-direction: column; gap: 10px;">
          <li><strong>Moving Average Confluence</strong>: GOOG trades at $344.86, retesting the critical 200-day SMA ($339.61) with 50-day SMA overhead at $345.66.</li>
          <li><strong>Oversold Reset</strong>: 14-day RSI stands at 49.8 (perfect neutral reset after 14.7% pullback from 52-week high of $404.47).</li>
          <li><strong>Approved Add Corridor</strong>: If macro panic drags price into <strong>$315.00 - $330.00 USD</strong>, authorize buying up to 50 shares.</li>
          <li><strong>Hard Stop-Loss Floor</strong>: <strong>$295.00 USD</strong> (structural 5-year trendline breakdown).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 5 of 6</span>
  </div>
</div>

<!-- SLIDE 6: ACTION PLAN FOR BM사장님 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>PORTFOLIO ACTION DIRECTIVES FOR BM사장님</h2>
      <p>Customized Implementation Plan for BM사장님's $1.61M USD Portfolio</p>
    </div>
    <div class="slide-badge" style="background: #ecfdf5; color: #059669; border-color: #a7f3d0;">EXECUTIVE DIRECTIVE</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card" style="border-left: 6px solid #10b981;">
        <div class="card-title">1. Existing Holding Directive</div>
        <div style="font-size: 28px; font-weight: 900; color: #10b981; margin-bottom: 8px;">STRONG HOLD (600 Shs)</div>
        <p>Maintain full 600 shares ($206,916 USD). At 12.87% portfolio weight, Alphabet serves as BM사장님's foundational platform compounder. Do not sell a single share.</p>
      </div>

      <div class="card" style="border-left: 6px solid #3b82f6;">
        <div class="card-title">2. Fresh Cash Management</div>
        <div style="font-size: 28px; font-weight: 900; color: #3b82f6; margin-bottom: 8px;">FREEZE NEW ENTRIES</div>
        <p>Do not allocate new capital into GOOG at current price levels ($344.86). Preserve dry powder for non-tech gap-fillers (e.g., UBER, healthcare, infrastructure).</p>
      </div>

      <div class="card" style="border-left: 6px solid #f59e0b;">
        <div class="card-title">3. Contingency Dip Protocol</div>
        <div style="font-size: 28px; font-weight: 900; color: #d97706; margin-bottom: 8px;">ACCUMULATE &lt; $330</div>
        <p>If geopolitical or regulatory headlines trigger an overshoot below $330.00 USD, authorize adding up to 50 shares to reach the hard CRO cap of 15.0% ($240k).</p>
      </div>
    </div>

    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 14px; padding: 20px 28px;">
      <div style="font-size: 19px; font-weight: 800; color: #991b1b; margin-bottom: 6px;">
        ⚠️ NON-NEGOTIABLE THESIS INVALIDATION TRIGGER (SELL DIRECTIVE):
      </div>
      <p style="font-size: 17px; color: #7f1d1d; line-height: 1.6;">
        Liquidate 50% of the position immediately if: (1) The D.C. Circuit Court of Appeals mandates the forced breakup and divestiture of Chrome and Android; OR (2) Google Cloud revenue growth decelerates below 20% YoY for two consecutive quarters while 2026-2027 CapEx exceeds $200B annually, crushing consolidated operating margins below 25%.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • Global Autonomous Asset Management</span>
    <span>Prepared Exclusively for BM사장님 • Page 6 of 6</span>
  </div>
</div>

</body>
</html>
"""

# ------------------------------------------------------------------------------
# SLIDE KR HTML GENERATOR
# ------------------------------------------------------------------------------
def generate_slide_kr_html():
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>GOOG 투자위원회 공식 의사결정 프레젠테이션 (한글판)</title>
<style>
{SLIDE_CSS}
</style>
</head>
<body>

<!-- SLIDE 1: 표지 및 최종 판정 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>DADAIC 투자위원회 공식 집행 의결서</h2>
      <p>심의 종목: GOOG | 알파벳 (Alphabet Inc. Class C 보통주, 나스닥)</p>
    </div>
    <div class="slide-badge">심의 일자: 2026년 10월 8일</div>
  </div>

  <div class="slide-content">
    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); color: #ffffff; padding: 36px 44px; border-radius: 20px; display: flex; justify-content: space-between; align-items: center;">
      <div>
        <span style="background: #3b82f6; color: #ffffff; padding: 6px 14px; border-radius: 6px; font-size: 15px; font-weight: 800; letter-spacing: 1px;">투자위원회 공식 의결</span>
        <h1 style="font-family: 'Outfit', 'Noto Sans KR'; font-size: 44px; font-weight: 900; margin: 12px 0 8px 0; color: #ffffff;">APPROVED: 최상위 핵심 복리 자산 / 비중 상한 준수</h1>
        <p style="font-size: 21px; color: #93c5fd; font-weight: 500;">포트폴리오 핵심 앵커 • 기보유 600주($206,916 USD) 전량 보유 • 신규 자금 투입 잠정 동결</p>
      </div>
      <div style="text-align: right; background: rgba(255,255,255,0.1); padding: 20px 32px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 16px; color: #cbd5e1; text-transform: uppercase;">현재 편입 비중</div>
        <div style="font-family: 'Outfit'; font-size: 48px; font-weight: 900; color: #60a5fa;">12.87%</div>
        <div style="font-size: 15px; color: #cbd5e1;">BM사장님 계좌 제2위 핵심 주력주</div>
      </div>
    </div>

    <div class="grid-4">
      <div class="stat-box">
        <div class="stat-label">현재 시장 주가</div>
        <div class="stat-val">$344.86</div>
        <div class="stat-sub" style="color: #64748b;">시가총액: $4.18조 달러</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">보수적 본질 내재가치</div>
        <div class="stat-val">$395.00</div>
        <div class="stat-sub">+14.5% 내재가치 상승 여력</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">12개월 기본 목표가</div>
        <div class="stat-val">$420.00</div>
        <div class="stat-sub">+21.8% 기대 수익률</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">밸류에이션 멀티플 (P/E)</div>
        <div class="stat-val">17.1x</div>
        <div class="stat-sub">PEG 비율: 0.88 (< 1.0)</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 1 / 6</span>
  </div>
</div>

<!-- SLIDE 2: 다년간 실증 검증 스코어카드 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>다년간 실증 검증 스코어카드 (BM사장님 30년 투자 원칙)</h2>
      <p>단기 내러티브를 배제하고 공시 감사 데이터와 주가 복리 성과를 엄격 검증</p>
    </div>
    <div class="slide-badge">SEC EDGAR 공시 데이터 검증 완료</div>
  </div>

  <div class="slide-content">
    <table class="table-wrap">
      <thead>
        <tr>
          <th>검증 지표</th>
          <th>다년간 공시 실증 팩트 (USD 기준)</th>
          <th>벤치마크 및 동종 업계 비교</th>
          <th>투자위원회 실증 판정</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1개년 총수익률</strong></td>
          <td><strong>+21.74%</strong> ($281.27 ➔ $344.86 USD)</td>
          <td>S&P 500: +24.5% / 빅테크 평균: +31.2%</td>
          <td><span class="badge-tag badge-green">안정적 저평가 복리 성장</span></td>
        </tr>
        <tr>
          <td><strong>3개년 총수익 및 CAGR</strong></td>
          <td><strong>+177.67%</strong> (연평균 CAGR: <strong>+40.23%</strong> / $124.20)</td>
          <td>대형 테크 상위 8% 초과 성과 기록</td>
          <td><span class="badge-tag badge-green">탁월한 알파 엔진 입증</span></td>
        </tr>
        <tr>
          <td><strong>5개년 총수익 및 CAGR</strong></td>
          <td><strong>+134.63%</strong> (연평균 CAGR: <strong>+18.43%</strong> / $146.98)</td>
          <td>2022년 금리 인상 충격 및 반독점 소송 완벽 극복</td>
          <td><span class="badge-tag badge-green">통화 사이클 관통 해자</span></td>
        </tr>
        <tr>
          <td><strong>매출액 성장 궤적</strong></td>
          <td>2023: <strong>$307.4B</strong> ➔ 2025: <strong>$402.8B</strong> ➔ 2026E: <strong>$488.5B</strong></td>
          <td>2026년 2분기 매출 $1,198억 달러 (+24% YoY)</td>
          <td><span class="badge-tag badge-blue">가속화되는 외형 스케일</span></td>
        </tr>
        <tr>
          <td><strong>클라우드 이익 레버리지</strong></td>
          <td>클라우드 매출: <strong>$24.8B</strong> (+82% YoY) | OPM: <strong>35.6%</strong></td>
          <td>구글 클라우드가 AWS/Azure의 증분 AI 성장 추월</td>
          <td><span class="badge-tag badge-blue">엔터프라이즈 AI 캐시카우</span></td>
        </tr>
        <tr>
          <td><strong>대차대조표 건전성</strong></td>
          <td>현금/단기투자: <strong>$242.47B</strong> vs 장기차입금: <strong>$98.17B</strong></td>
          <td>순 현금 흑자: <strong>+$144.30B USD</strong></td>
          <td><span class="badge-tag badge-green">국가급 초우량 요새형 재무</span></td>
        </tr>
        <tr>
          <td><strong>자본 배분 전환 리스크</strong></td>
          <td>2026년 설비투자: <strong>$195B ~ $205B</strong> | Q2 FCF: <strong>-$5.86B</strong></td>
          <td>자사주 매입 일시 중단 및 AI 데이터센터 총력전</td>
          <td><span class="badge-tag badge-amber">인프라 독점 스프린트</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 2 / 6</span>
  </div>
</div>

<!-- SLIDE 3: 세계 5대 거장 & 마켓 테크니션 투자 관점 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>세계 5대 거장 & 마켓 테크니션 종합 평가</h2>
      <p>가치, 영구 복리, 고성장 PEG, 모멘텀 돌파, 기술적 손익비, 거시 유동성 비대칭의 융합 분석</p>
    </div>
    <div class="slide-badge">철학적 대립 조정 완료</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">☕</span> 워런 버핏: 통행료 다리 해자
          <span class="badge-tag badge-green" style="margin-left: auto;">적정가 매수 / 보유</span>
        </div>
        <p><strong>핵심 해자</strong>: 구글 검색은 글로벌 점유율 89.94%를 장악한 궁극의 디지털 통행료 다리입니다. 유튜브와 클라우드가 강력한 현금 흐름을 창출하며, $1,443억 달러의 순현금이 완충재 역할을 합니다.</p>
        <p style="margin-top: 6px; color: #b45309;"><strong>위험 요인</strong>: AI 설비투자를 위해 자사주 매입을 멈추고 $84.75B 규모의 주식/채권을 발행한 점은 전통적 주주환원에서 이탈. PER 17.1배는 적정가이나 깊은 안전마진은 아님.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🧠</span> 찰리 멍거: 롤라팔루자 독점
          <span class="badge-tag badge-blue" style="margin-left: auto;">역발상 검증 통과</span>
        </div>
        <p><strong>롤라팔루자 효과</strong>: 안드로이드(30억 대) + 크롬 + 유튜브 + 클라우드 + 자체 Ironwood TPU7x 추론 칩이 상호 결합된 난공불락의 네트워크 플라이휠 구축.</p>
        <p style="margin-top: 6px; color: #15803d;"><strong>역발상(Inversion) 검증</strong>: 미 법무부 강제 분할은 2025년 12월 기각되었으며, AI Overviews 도입 후에도 검색 매출은 +17% 성장, 클라우드 영업이익률은 35.6%로 폭발함.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">📈</span> 피터 린치: 강력 추천 고성장
          <span class="badge-tag badge-green" style="margin-left: auto;">PEG 0.88 (&lt; 1.0)</span>
        </div>
        <p><strong>성장 엔진</strong>: $4.18조 달러 시총에도 2분기 매출 24% 급증. 일회성 이익을 제외한 영업 기준 Forward P/E는 19.5배이며 예상 EPS 성장률은 22%에 달함.</p>
        <p style="margin-top: 6px; color: #0284c7;"><strong>PEG 분석</strong>: <strong>0.88</strong>로 빅테크 중 가장 매력적인 성장주 헐값 영역(애플 2.60, 마이크로소프트 1.45 대비 압도적 저평가).</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🌊</span> 스탠리 드러켄밀러: 비대칭 알파
          <span class="badge-tag badge-blue" style="margin-left: auto;">3.4 : 1 비대칭 우위</span>
        </div>
        <p><strong>18개월 변곡점</strong>: 시장은 구글 검색이 무너질 것이라 오판했으나, 자체 Ironwood TPU 수퍼팟을 통한 압도적 토큰당 추론 비용 절감으로 엔터프라이즈 AI 클라우드 점유율을 대거 탈환함.</p>
        <p style="margin-top: 6px; color: #b45309;"><strong>매크로 주의</strong>: 미 국채 장기물 5.28% 고착화 시 25배 이상 멀티플 확장은 제한되므로 철저한 실적 기반 검증 필요.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">🎯</span> 윌리엄 오닐: CAN SLIM
          <span class="badge-tag badge-green" style="margin-left: auto;">기관 매집 재축적</span>
        </div>
        <p><strong>CAN SLIM 지표</strong>: 2분기 순익 +294% GAAP (+28% 조정), 3개년 EPS CAGR +40.2%, Ironwood TPU7x & 웨이모 상용화 추진. 전 세계 5,000개 이상 최상위 기관 투자자가 매집 보유.</p>
        <p style="margin-top: 6px; color: #15803d;"><strong>지지선 확인</strong>: 최고가($404) 대비 -14.7% 건전한 기간 조정 후 200일 이평선($339.61) 강력 지지 안착. 상대강도(RS 74) 양호.</p>
      </div>

      <div class="card">
        <div class="card-title">
          <span style="font-size: 24px;">📐</span> 마켓 테크니션: 차트 셋업
          <span class="badge-tag badge-blue" style="margin-left: auto;">R:R 1 : 3.8 셋업</span>
        </div>
        <p><strong>차트 구조</strong>: $335~$338 USD의 견고한 기관 수급 매물대 지지 및 200일 이평선 안착. 14일 RSI(49.8) 완벽한 중립 반등 구간.</p>
        <p style="margin-top: 6px; color: #0284c7;"><strong>매매 셋업</strong>: 핵심 지지선 <strong>$335~$338</strong> | 1차 저항선 <strong>$380</strong> | 목표가 <strong>$420</strong> | 손절 기준선 <strong>$318</strong>. 손익비 1:3.8의 우수한 비대칭 구조.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 3 / 6</span>
  </div>
</div>

<!-- SLIDE 4: CRO 블라인드 리스크 감사 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>독립 CRO 블라인드 리스크 감사: 의무 3대 결점</h2>
      <p>상승론에 독립된 최고리스크책임자(CRO)의 자본 보존 강제 지침</p>
    </div>
    <div class="slide-badge" style="color: #dc2626; background: #fef2f2; border-color: #fca5a5;">구속력 있는 CRO 지침</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card" style="border-top: 5px solid #dc2626;">
        <div class="card-title" style="color: #dc2626; font-size: 22px;">1. 잉여현금흐름 음수 & CapEx 부담</div>
        <p><strong>공시 감사 결점</strong>: 2분기 설비투자 $449.2억 달러 집행으로 분기 FCF -$58.6억 달러, SBC 차감 True FCF -$138.2억 달러 기록. 연간 $2,000억 달러 투자 집행.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>하방 영향</strong>: AI 소프트웨어 수익화가 지연될 경우 대규모 감가상각비 증가로 2027-2028년 투하자본이익률(ROIC)이 압박받을 수 있음.</p>
      </div>

      <div class="card" style="border-top: 5px solid #ea580c;">
        <div class="card-title" style="color: #ea580c; font-size: 22px;">2. 포트폴리오 내 팩터 중복 심화</div>
        <p><strong>거짓 분산 감사</strong>: BM사장님께서는 이미 구글 600주($206,916 USD / 비중 12.87%)를 보유 중. NVDA(21.50%), AMZN(10.11%), AVGO(7.84%), AMD(6.95%) 등 빅테크/반도체 비중이 69% 초과.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>CRO 판정</strong>: 현재 가격대에서 구글을 추가 매수하는 것은 단일 팩터 쏠림 위험을 치명적으로 증폭시킴.</p>
      </div>

      <div class="card" style="border-top: 5px solid #d97706;">
        <div class="card-title" style="color: #d97706; font-size: 22px;">3. 워싱턴 항소법원 배포계약 소송</div>
        <p><strong>법률 불확실성</strong>: 메타 판사의 강제 분할 기각에도 불구하고, 미 법무부(DOJ)는 2026년 7월 애플 및 통신사 기본 검색 탑재 수수료 전면 금지를 요구하며 항소 제기.</p>
        <p style="margin-top: 10px; font-size: 16px; color: #64748b;"><strong>완충 요소</strong>: 수수료 금지 시 구글은 연간 200억 달러 이상의 트래픽 유입 비용(TAC)을 절감하나 단기 점유율 노이즈 유발 가능.</p>
      </div>
    </div>

    <div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 14px; padding: 20px 28px;">
      <div style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">
        🏛️ BM사장님 맞춤형 CRO 강제 비중 한도 지침:
      </div>
      <p style="font-size: 18px; color: #334155; line-height: 1.6;">
        "기계적 팩터 중복 캡 발동: 현재 보유 비중 12.87%($206,916 USD)는 최상위 핵심 복리 앵커로서 온전히 승인한다. 그러나 현재 주가($344.86 USD)에서 <strong>구글에 대한 신규 자금 투입은 즉각 동결</strong>한다. 구글의 최대 편입 한도는 <strong>15.0%($240,000 USD)</strong>로 절대 제한하며, 신규 유동성은 비(非)빅테크 분산 자산에 배정해야 한다."
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 4 / 6</span>
  </div>
</div>

<!-- SLIDE 5: 목표 주가 및 기술적 매매 셋업 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>3대 시나리오별 목표 주가 및 차트 매매 셋업</h2>
      <p>12개월 목표 주가 산정, 이동평균선 정렬 및 1:2 이상 손익비 전략</p>
    </div>
    <div class="slide-badge">확률 가중 가치평가 모델</div>
  </div>

  <div class="slide-content">
    <div class="grid-2">
      <div>
        <table class="table-wrap">
          <thead>
            <tr>
              <th>시나리오</th>
              <th>확률</th>
              <th>적용 멀티플 및 EPS</th>
              <th>목표가 ($)</th>
              <th>기대수익률</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #f0fdf4;">
              <td><strong>낙관 시나리오</strong></td>
              <td>25%</td>
              <td>24.0x / 2027E $20.50</td>
              <td><strong>$492.00</strong></td>
              <td><span class="badge-tag badge-green">+42.7%</span></td>
            </tr>
            <tr style="background: #eff6ff;">
              <td><strong>기본 시나리오</strong></td>
              <td>55%</td>
              <td>21.0x / 2027E $20.00</td>
              <td><strong>$420.00</strong></td>
              <td><span class="badge-tag badge-blue">+21.8%</span></td>
            </tr>
            <tr style="background: #fef2f2;">
              <td><strong>비관 시나리오</strong></td>
              <td>20%</td>
              <td>16.5x / 2027E $18.50</td>
              <td><strong>$305.25</strong></td>
              <td><span class="badge-tag badge-red">-11.5%</span></td>
            </tr>
          </tbody>
        </table>
        <div style="margin-top: 14px; text-align: center; background: #f8fafc; padding: 14px; border-radius: 10px; border: 1px solid #e2e8f0;">
          <span style="font-size: 16px; color: #64748b; font-weight: 600;">확률 가중 평균 목표 주가:</span>
          <span style="font-family: 'Outfit'; font-size: 24px; font-weight: 900; color: #2563eb; margin-left: 10px;">$415.05 USD (+20.4%)</span>
        </div>
      </div>

      <div class="card">
        <div class="card-title">기술적 지지선 및 실행 로드맵</div>
        <ul style="padding-left: 20px; display: flex; flex-direction: column; gap: 10px;">
          <li><strong>핵심 이동평균선 정렬</strong>: 현재 주가 $344.86은 핵심 장기 지지선인 200일 이평선($339.61)과 50일선($345.66)의 강력한 수급 분기점에 위치함.</li>
          <li><strong>과매도 지표 안정화</strong>: 52주 최고가($404.47) 대비 14.7% 조정을 거친 후 14일 RSI는 49.8로 완벽한 중립 바닥권 형성.</li>
          <li><strong>비상 추가 매수 밴드</strong>: 거시 충격 등으로 주가가 <strong>$315.00 ~ $330.00 USD</strong>까지 일시 급락할 경우에 한해 최대 50주 추가 매수 승인.</li>
          <li><strong>손절 및 추세 이탈 기준선</strong>: <strong>$295.00 USD</strong> (5개년 구조적 상승 추세 붕괴 시 리스크 재점검).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 5 / 6</span>
  </div>
</div>

<!-- SLIDE 6: BM사장님 맞춤형 실행 로드맵 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>BM사장님 맞춤형 포트폴리오 집행 로드맵</h2>
      <p>총 운용 주식 자산 $1,607,952 USD 기반 최적 자본 배분 결론</p>
    </div>
    <div class="slide-badge" style="background: #ecfdf5; color: #059669; border-color: #a7f3d0;">최고운용책임자 집행 명령</div>
  </div>

  <div class="slide-content">
    <div class="grid-3">
      <div class="card" style="border-left: 6px solid #10b981;">
        <div class="card-title">1. 기보유 지분 운용 지침</div>
        <div style="font-size: 28px; font-weight: 900; color: #10b981; margin-bottom: 8px;">전량 강력 보유 (600주)</div>
        <p>보유 중인 600주($206,916 USD)는 단 1주도 매도하지 않습니다. 전체 주식 자산의 12.87% 비중으로 포트폴리오의 최상위 플랫폼 복리 엔진 역할을 지속 수행합니다.</p>
      </div>

      <div class="card" style="border-left: 6px solid #3b82f6;">
        <div class="card-title">2. 신규 자금 집행 방침</div>
        <div style="font-size: 28px; font-weight: 900; color: #3b82f6; margin-bottom: 8px;">신규 매수 잠정 동결</div>
        <p>현재 주가($344.86 USD)에서는 구글에 신규 자금을 추가 투입하지 않습니다. 현금 유동성은 빅테크와 상관관계가 낮은 방어형 알파 자산(UBER 등) 및 현금 버퍼에 배분합니다.</p>
      </div>

      <div class="card" style="border-left: 6px solid #f59e0b;">
        <div class="card-title">3. 위기 시 비상 매수 계획</div>
        <div style="font-size: 28px; font-weight: 900; color: #d97706; margin-bottom: 8px;">$330 이하 분할 매수</div>
        <p>시장 패닉이나 반독점 노이즈로 $330.00 USD 이하로 급락할 경우에만 최대 50주를 추가 매수하여 CRO 한도인 15.0%($240,000 USD)까지 채우는 것을 허용합니다.</p>
      </div>
    </div>

    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 14px; padding: 20px 28px;">
      <div style="font-size: 19px; font-weight: 800; color: #991b1b; margin-bottom: 6px;">
        ⚠️ 타협 없는 투자 전제 훼손 매도 원칙 (Sell Trigger):
      </div>
      <p style="font-size: 17px; color: #7f1d1d; line-height: 1.6;">
        다음 조건 발생 시 기계적으로 보유 지분의 50%를 즉시 매도합니다: (1) D.C. 연방항소법원이 메타 판사의 판결을 파기하고 구글의 크롬 브라우저 및 안드로이드 OS 강제 분할을 최종 명령하거나; (2) 연간 2,000억 달러의 설비투자 집행에도 구글 클라우드 매출 성장률이 2분기 연속 20% 미만으로 급락하여 통합 영업이익률이 25% 이하로 구조적 훼손되는 경우.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <span>DADAIC Investment Firm • 글로벌 자율형 자산배분 시스템</span>
    <span>BM사장님 단독 보고용 • 슬라이드 6 / 6</span>
  </div>
</div>

</body>
</html>
"""

# ------------------------------------------------------------------------------
# INFOGRAPHIC CSS (Portrait Mobile/Tablet/Print Layout)
# ------------------------------------------------------------------------------
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
  color: #1e293b;
  display: flex;
  justify-content: center;
  padding: 40px 20px;
}

.infographic-container {
  width: 1140px;
  background: #ffffff;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.hero-header {
  background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
  color: #ffffff;
  padding: 46px 50px 38px 50px;
  position: relative;
}

.hero-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.firm-badge {
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 800;
  color: #93c5fd;
  background: rgba(59, 130, 246, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.4);
  padding: 6px 16px;
  border-radius: 20px;
  letter-spacing: 1px;
}

.hero-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 40px;
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 12px;
}

.hero-subtitle {
  font-size: 20px;
  color: #cbd5e1;
  font-weight: 500;
}

.hero-verdict-box {
  margin-top: 28px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  padding: 22px 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.verdict-tag {
  background: #3b82f6;
  color: #ffffff;
  padding: 6px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 900;
  letter-spacing: 1px;
  display: inline-block;
  margin-bottom: 6px;
}

.verdict-text {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 26px;
  font-weight: 900;
  color: #ffffff;
}

.content-body {
  padding: 44px 50px;
  display: flex;
  flex-direction: column;
  gap: 36px;
}

.section-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 10px;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.metric-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 20px;
  text-align: center;
}

.metric-label {
  font-size: 14px;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}

.metric-val {
  font-family: 'Outfit', sans-serif;
  font-size: 32px;
  font-weight: 900;
  color: #0f172a;
}

.metric-sub {
  font-size: 14px;
  color: #10b981;
  font-weight: 600;
  margin-top: 4px;
}

.info-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 22px 24px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.info-card-header {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 19px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-card p {
  font-size: 16px;
  color: #334155;
  line-height: 1.6;
}

.footer-bar {
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  padding: 24px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 15px;
  color: #64748b;
  font-weight: 500;
}
"""

# ------------------------------------------------------------------------------
# INFOGRAPHIC EN HTML GENERATOR
# ------------------------------------------------------------------------------
def generate_infographic_en_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GOOG Investment Committee Strategic Infographic (English)</title>
<style>
{INFOGRAPHIC_CSS}
</style>
</head>
<body>

<div class="infographic-container">
  <!-- HERO HEADER -->
  <div class="hero-header">
    <div class="hero-top">
      <div class="firm-badge">DADAIC INVESTMENT FIRM • EXECUTIVE DOSSIER</div>
      <div style="font-size: 15px; color: #94a3b8; font-weight: 500;">OCTOBER 8, 2026</div>
    </div>
    <div class="hero-title">ALPHABET INC. (NASDAQ: GOOG)</div>
    <div class="hero-subtitle">Institutional Due Diligence & Portfolio Allocation Strategy for BM사장님</div>

    <div class="hero-verdict-box">
      <div>
        <span class="verdict-tag">OFFICIAL CIO VERDICT</span>
        <div class="verdict-text">APPROVED: QUALITY COMPOUNDER WITH SIZE CAP</div>
        <div style="font-size: 16px; color: #93c5fd; margin-top: 4px;">Maintain Full 600 Shares ($206,916 USD / 12.87% Weight) • Freeze New Entries</div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 14px; color: #cbd5e1; text-transform: uppercase;">12M Target (Base)</div>
        <div style="font-family: 'Outfit'; font-size: 38px; font-weight: 900; color: #60a5fa;">$420.00</div>
        <div style="font-size: 14px; color: #6ee7b7;">+21.8% Expected Return</div>
      </div>
    </div>
  </div>

  <div class="content-body">
    <!-- SECTION 1: KEY FINANCIAL SNAPSHOT -->
    <div>
      <div class="section-title">📊 Multi-Year Empirical Health Snapshot</div>
      <div class="grid-4">
        <div class="metric-card">
          <div class="metric-label">Current Stock Price</div>
          <div class="metric-val">$344.86</div>
          <div class="metric-sub" style="color: #64748b;">Market Cap: $4.18T</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Q2 2026 Revenue</div>
          <div class="metric-val">$119.8B</div>
          <div class="metric-sub">+24% YoY Growth</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Cloud Revenue & OPM</div>
          <div class="metric-val">$24.8B</div>
          <div class="metric-sub">+82% YoY (OPM: 35.6%)</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Valuation Multiple</div>
          <div class="metric-val">17.1x</div>
          <div class="metric-sub">PEG: 0.88 (< 1.0)</div>
        </div>
      </div>
    </div>

    <!-- SECTION 2: 5 MASTERS & MARKET TECHNICIAN EVALUATION -->
    <div>
      <div class="section-title">🏛️ The 5 Masters & Market Technician Consensus</div>
      <div class="grid-3">
        <div class="info-card">
          <div class="info-card-header">☕ Warren Buffett (Moat & Intrinsic Value)</div>
          <p><strong>Verdict: Fair Value Core Buy</strong>. Google Search (89.94% share) is an inescapable toll bridge. $144.3B net cash surplus provides rock-solid defense. Intrinsic value is $395 USD.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🧠 Charlie Munger (Lollapalooza & Inversion)</div>
          <p><strong>Verdict: Inversion Cleared</strong>. Android (3B+ devices) + Chrome + YouTube + Cloud + Ironwood TPUs form an impenetrable multi-disciplinary flywheel. Breakup risk cleared in Dec 2025.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">📈 Peter Lynch (Fast Grower & PEG)</div>
          <p><strong>Verdict: Screaming Bargain (PEG 0.88)</strong>. Top-line grew 24% YoY; forward P/E is only 19.5x against 22% EPS growth. Classic Lynch bargain threshold (&lt; 1.0).</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🌊 Stanley Druckenmiller (Asymmetric Alpha)</div>
          <p><strong>Verdict: 3.4 : 1 Asymmetric Long</strong>. Ironwood TPU silicon provides the lowest inference cost in tech, driving Google Cloud to decisively seize enterprise share from AWS and Azure.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🎯 William J. O'Neil (CAN SLIM & Breakout)</div>
          <p><strong>Verdict: Institutional Re-accumulation</strong>. Q2 net income surged +294% GAAP (+28% adj). 5,000+ institutions backing. Base consolidation above 200-DMA ($339.61) confirmed.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">📐 Market Technician (Chart Support & R:R)</div>
          <p><strong>Verdict: 1 : 3.8 Asymmetric Setup</strong>. Strong demand floor at $335-$338 USD aligned with 200-DMA. RSI at 49.8. Target $420, stop-loss $318, delivering superior risk-to-reward.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: CRO BLIND AUDIT -->
    <div>
      <div class="section-title" style="color: #dc2626;">🛡️ Adversarial CRO Blind Audit (3 Fatal Flaws)</div>
      <div class="grid-3">
        <div class="info-card" style="border-left: 5px solid #dc2626;">
          <div class="info-card-header" style="color: #dc2626;">1. Capex Surge & Negative FCF</div>
          <p>CapEx surged to $44.92B in Q2, causing negative GAAP FCF of -$5.86B (True FCF net of SBC: -$13.82B). Full-year capex guided to $195B-$205B. ROIC compression risk if AI monetization pauses.</p>
        </div>
        <div class="info-card" style="border-left: 5px solid #ea580c;">
          <div class="info-card-header" style="color: #ea580c;">2. Portfolio Factor Overhang</div>
          <p>BM사장님 already holds 600 shares ($206,916 USD / 12.87%). Broad Tech/Semi factor exposure exceeds 69% of portfolio. Buying more GOOG today creates acute False Diversification.</p>
        </div>
        <div class="info-card" style="border-left: 5px solid #d97706;">
          <div class="info-card-header" style="color: #d97706;">3. D.C. Circuit Court Appeal</div>
          <p>While Judge Mehta rejected the Chrome/Android breakup, the DOJ's July 2026 appeal targets default distribution payments to Apple. Poses near-term query transition noise.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 4: ACTION PLAN FOR BM사장님 -->
    <div>
      <div class="section-title" style="color: #059669;">🎯 Portfolio Execution Plan for BM사장님</div>
      <div class="grid-3">
        <div class="info-card" style="background: #f0fdf4; border-color: #bbf7d0;">
          <div class="info-card-header" style="color: #166534;">1. Existing Holdings</div>
          <div style="font-family: 'Outfit'; font-size: 24px; font-weight: 900; color: #166534; margin-bottom: 6px;">STRONG HOLD (600 Shs)</div>
          <p style="font-size: 15px;">Maintain full 600 shares ($206,916 USD / 12.87% weight). Do not trim. Let the platform compound uninterrupted.</p>
        </div>
        <div class="info-card" style="background: #eff6ff; border-color: #bfdbfe;">
          <div class="info-card-header" style="color: #1e40af;">2. Fresh Capital</div>
          <div style="font-family: 'Outfit'; font-size: 24px; font-weight: 900; color: #1e40af; margin-bottom: 6px;">FREEZE NEW ENTRIES</div>
          <p style="font-size: 15px;">Do not allocate new capital at $344.86 USD. Channel fresh liquidity into non-tech gap-fillers and cash reserves.</p>
        </div>
        <div class="info-card" style="background: #fffbeb; border-color: #fde68a;">
          <div class="info-card-header" style="color: #92400e;">3. Contingency Dip Zone</div>
          <div style="font-family: 'Outfit'; font-size: 24px; font-weight: 900; color: #92400e; margin-bottom: 6px;">ACCUMULATE &lt; $330</div>
          <p style="font-size: 15px;">If macro shocks drag price below $330.00 USD, authorize adding up to 50 shares to reach the hard CRO ceiling of 15.0% ($240k).</p>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER BAR -->
  <div class="footer-bar">
    <div><strong>DADAIC INVESTMENT FIRM</strong> • Autonomous Decision Architecture</div>
    <div>Strictly Confidential • Exclusively for BM사장님 • Currency: Pure USD ($)</div>
  </div>
</div>

</body>
</html>
"""

# ------------------------------------------------------------------------------
# INFOGRAPHIC KR HTML GENERATOR
# ------------------------------------------------------------------------------
def generate_infographic_kr_html():
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>GOOG 투자위원회 핵심 전략 인포그래픽 (한글판)</title>
<style>
{INFOGRAPHIC_CSS}
</style>
</head>
<body>

<div class="infographic-container">
  <!-- HERO HEADER -->
  <div class="hero-header">
    <div class="hero-top">
      <div class="firm-badge">DADAIC INVESTMENT FIRM • 투자위원회 핵심 브리핑</div>
      <div style="font-size: 15px; color: #94a3b8; font-weight: 500;">2026년 10월 8일</div>
    </div>
    <div class="hero-title">알파벳 (Alphabet Inc. | NASDAQ: GOOG)</div>
    <div class="hero-subtitle">BM사장님 맞춤형 정밀 기업 실증 분석 및 자산배분 집행 원장</div>

    <div class="hero-verdict-box">
      <div>
        <span class="verdict-tag">투자위원회 공식 의결</span>
        <div class="verdict-text">APPROVED: 최상위 핵심 복리 자산 / 비중 상한 준수</div>
        <div style="font-size: 16px; color: #93c5fd; margin-top: 4px;">기보유 600주($206,916 USD / 비중 12.87%) 전량 유지 • 신규 자금 투입 잠정 동결</div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 14px; color: #cbd5e1; text-transform: uppercase;">12개월 기본 목표가</div>
        <div style="font-family: 'Outfit'; font-size: 38px; font-weight: 900; color: #60a5fa;">$420.00</div>
        <div style="font-size: 14px; color: #6ee7b7;">+21.8% 기대 수익률</div>
      </div>
    </div>
  </div>

  <div class="content-body">
    <!-- SECTION 1: 핵심 실증 재무 스냅샷 -->
    <div>
      <div class="section-title">📊 다년간 공시 실증 재무 건전성</div>
      <div class="grid-4">
        <div class="metric-card">
          <div class="metric-label">현재 시장 주가</div>
          <div class="metric-val">$344.86</div>
          <div class="metric-sub" style="color: #64748b;">시가총액: $4.18조 달러</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">2026년 Q2 매출액</div>
          <div class="metric-val">$119.8B</div>
          <div class="metric-sub">전년 대비 +24% 성장</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">클라우드 매출 & OPM</div>
          <div class="metric-val">$24.8B</div>
          <div class="metric-sub">+82% YoY (OPM: 35.6%)</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">밸류에이션 멀티플</div>
          <div class="metric-val">17.1x</div>
          <div class="metric-sub">PEG 비율: 0.88 (< 1.0)</div>
        </div>
      </div>
    </div>

    <!-- SECTION 2: 세계 5대 거장 & 마켓 테크니션 종합 평가 -->
    <div>
      <div class="section-title">🏛️ 세계 5대 투자 거장 & 마켓 테크니션 종합 평가</div>
      <div class="grid-3">
        <div class="info-card">
          <div class="info-card-header">☕ 워런 버핏 (경제적 해자와 내재가치)</div>
          <p><strong>판정: 적정가 핵심 매수</strong>. 구글 검색(점유율 89.94%)은 디지털 통행료 다리입니다. $1,443억 달러의 순현금이 강력한 완충재 역할을 합니다. 보수적 내재가치는 $395 USD입니다.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🧠 찰리 멍거 (롤라팔루자 효과 & 역발상)</div>
          <p><strong>판정: 역발상 검증 통과</strong>. 안드로이드(30억 대) + 크롬 + 유튜브 + 클라우드 + 자체 Ironwood TPU7x 칩이 상호 결합된 독점 플라이휠. 강제 분할 리스크는 2025년 12월 기각됨.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">📈 피터 린치 (고성장주와 PEG 지수)</div>
          <p><strong>판정: 강력 추천 고성장주 (PEG 0.88)</strong>. $4.18조 시총에도 매출이 24% 급증했으며 Forward PER은 19.5배에 불과합니다. 린치 기준 1.0 미만의 명백한 저평가 우량주입니다.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🌊 스탠리 드러켄밀러 (비대칭 알파)</div>
          <p><strong>판정: 3.4 : 1 비대칭 우위</strong>. 시장은 구글 검색이 몰락할 것이라 오판했으나, 자체 TPU 칩을 통한 압도적 원가 경쟁력으로 엔터프라이즈 AI 클라우드 점유율을 대거 흡수하고 있습니다.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">🎯 윌리엄 오닐 (CAN SLIM 모멘텀 & 지지선)</div>
          <p><strong>판정: 기관 매집 재축적</strong>. 2분기 순익 +294% GAAP(+28% 조정), 3개년 EPS CAGR +40.2%. 5,000개 이상 기관 매집 및 200일 이평선($339.61) 강력 지지 안착 확인.</p>
        </div>
        <div class="info-card">
          <div class="info-card-header">📐 마켓 테크니션 (차트 지지선 & 손익비)</div>
          <p><strong>판정: R:R 1 : 3.8 셋업</strong>. 핵심 수급 지지선 $335~$338 및 200일선 수요층 확인. 14일 RSI(49.8) 중립 반등권. 목표가 $420, 손절 $318로 최상의 손익비 제공.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: CRO 블라인드 리스크 감사 -->
    <div>
      <div class="section-title" style="color: #dc2626;">🛡️ 독립 CRO 블라인드 리스크 감사 (의무 3대 결점)</div>
      <div class="grid-3">
        <div class="info-card" style="border-left: 5px solid #dc2626;">
          <div class="info-card-header" style="color: #dc2626;">1. 설비투자 폭증과 FCF 음수</div>
          <p>2분기 CapEx가 $449.2억 달러로 급증하며 분기 FCF -$58.6억 달러(SBC 차감 True FCF -$138.2억 달러) 기록. 연간 $2,000억 달러 투자 집행으로 AI 수익화 지연 시 ROIC 압박 위험.</p>
        </div>
        <div class="info-card" style="border-left: 5px solid #ea580c;">
          <div class="info-card-header" style="color: #ea580c;">2. 포트폴리오 팩터 집중 위험</div>
          <p>BM사장님께서는 이미 구글 600주($206,916 USD / 비중 12.87%)를 보유 중이며, 테크/반도체 비중이 69%를 초과합니다. 구글 추가 매수 시 거짓 분산(False Diversification) 심화.</p>
        </div>
        <div class="info-card" style="border-left: 5px solid #d97706;">
          <div class="info-card-header" style="color: #d97706;">3. 워싱턴 항소법원 배포 소송</div>
          <p>메타 판사의 강제 분할 기각에도 불구하고, 미 법무부는 2026년 7월 애플 등에 대한 기본 검색 탑재 수수료 전면 금지를 요구하며 항소. 단기 점유율 변동성 유발 가능.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 4: BM사장님 맞춤형 실행 로드맵 -->
    <div>
      <div class="section-title" style="color: #059669;">🎯 BM사장님 맞춤형 포트폴리오 집행 로드맵</div>
      <div class="grid-3">
        <div class="info-card" style="background: #f0fdf4; border-color: #bbf7d0;">
          <div class="info-card-header" style="color: #166534;">1. 기보유 지분 운용 지침</div>
          <div style="font-family: 'Outfit', 'Noto Sans KR'; font-size: 24px; font-weight: 900; color: #166534; margin-bottom: 6px;">전량 강력 보유 (600주)</div>
          <p style="font-size: 15px;">보유 중인 600주($206,916 USD / 12.87%)는 단 1주도 매도하지 않습니다. 핵심 복리 자산으로 온전히 유지합니다.</p>
        </div>
        <div class="info-card" style="background: #eff6ff; border-color: #bfdbfe;">
          <div class="info-card-header" style="color: #1e40af;">2. 신규 자금 집행 방침</div>
          <div style="font-family: 'Outfit', 'Noto Sans KR'; font-size: 24px; font-weight: 900; color: #1e40af; margin-bottom: 6px;">신규 매수 잠정 동결</div>
          <p style="font-size: 15px;">현재 주가($344.86 USD)에서는 신규 자금을 추가 투입하지 않고 비(非)빅테크 분산 자산 및 현금 버퍼에 배분합니다.</p>
        </div>
        <div class="info-card" style="background: #fffbeb; border-color: #fde68a;">
          <div class="info-card-header" style="color: #92400e;">3. 위기 시 비상 매수 계획</div>
          <div style="font-family: 'Outfit', 'Noto Sans KR'; font-size: 24px; font-weight: 900; color: #92400e; margin-bottom: 6px;">$330 이하 분할 매수</div>
          <p style="font-size: 15px;">시장 패닉 등으로 $330.00 USD 이하로 급락할 경우에만 최대 50주를 추가 매수하여 CRO 한도인 15.0%($240k)까지 채웁니다.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER BAR -->
  <div class="footer-bar">
    <div><strong>DADAIC INVESTMENT FIRM</strong> • 글로벌 자율형 자산배분 시스템</div>
    <div>대외비 • BM사장님 단독 보고용 • 기준 통화: 미국 달러(USD) 전용</div>
  </div>
</div>

</body>
</html>
"""

def compile_media():
    print("[*] Generating HTML Deliverables for GOOG...")
    
    # Paths
    s_en_html = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Slide-EN-261008.html")
    s_en_pdf = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Slide-EN-261008.pdf")
    
    s_kr_html = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Slide-KR-261008.html")
    s_kr_pdf = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Slide-KR-261008.pdf")
    
    i_en_html = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Infographic-EN-261008.html")
    i_en_png = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Infographic-EN-261008.png")
    
    i_kr_html = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Infographic-KR-261008.html")
    i_kr_png = os.path.join(MEDIA_DIR, "GOOG-Investment-Committee-Decision-Memo-Infographic-KR-261008.png")
    
    with open(s_en_html, "w", encoding="utf-8") as f:
        f.write(generate_slide_en_html())
    with open(s_kr_html, "w", encoding="utf-8") as f:
        f.write(generate_slide_kr_html())
    with open(i_en_html, "w", encoding="utf-8") as f:
        f.write(generate_infographic_en_html())
    with open(i_kr_html, "w", encoding="utf-8") as f:
        f.write(generate_infographic_kr_html())
    print("  -> HTML deliverables created successfully.")
    
    print("[*] Compiling PDF & PNG media with Headless Chrome...")
    # 1. Slide EN PDF
    cmd_s_en = [CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={s_en_pdf}", s_en_html]
    print("  -> Rendering Slide EN PDF...")
    subprocess.run(cmd_s_en, check=True)

    # 2. Slide KR PDF
    cmd_s_kr = [CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={s_kr_pdf}", s_kr_html]
    print("  -> Rendering Slide KR PDF...")
    subprocess.run(cmd_s_kr, check=True)

    # 3. Infographic EN PNG
    cmd_i_en = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,2400", f"--screenshot={i_en_png}", i_en_html]
    print("  -> Rendering Infographic EN PNG...")
    subprocess.run(cmd_i_en, check=True)

    # 4. Infographic KR PNG
    cmd_i_kr = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,2400", f"--screenshot={i_kr_png}", i_kr_html]
    print("  -> Rendering Infographic KR PNG...")
    subprocess.run(cmd_i_kr, check=True)

    print("[+] All 8 GOOG visual media deliverables generated successfully!")

if __name__ == "__main__":
    compile_media()
