#!/usr/bin/env python3
"""
DADAIC Investment Firm - Master Media Generator for UBER
Generates all 8 institutional deliverables:
1. UBER-Investment-Committee-Decision-Memo-Slide-EN-261007.html
2. UBER-Investment-Committee-Decision-Memo-Slide-EN-261007.pdf
3. UBER-Investment-Committee-Decision-Memo-Slide-KR-261007.html
4. UBER-Investment-Committee-Decision-Memo-Slide-KR-261007.pdf
5. UBER-Investment-Committee-Decision-Memo-Infographic-EN-261007.html
6. UBER-Investment-Committee-Decision-Memo-Infographic-EN-261007.png
7. UBER-Investment-Committee-Decision-Memo-Infographic-KR-261007.html
8. UBER-Investment-Committee-Decision-Memo-Infographic-KR-261007.png
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
  background: radial-gradient(circle at 90% 10%, rgba(16, 185, 129, 0.05) 0%, transparent 45%),
              radial-gradient(circle at 10% 90%, rgba(37, 99, 235, 0.06) 0%, transparent 45%),
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
  font-size: 20px;
  color: #64748b;
  margin-top: 5px;
  font-weight: 500;
}

.firm-tag {
  font-family: 'Outfit', sans-serif;
  font-size: 16px;
  font-weight: 800;
  color: #059669;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  background: #ecfdf5;
  padding: 8px 20px;
  border-radius: 24px;
  border: 1px solid #a7f3d0;
}

.slide-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: space-between;
}

.slide-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #e2e8f0;
  padding-top: 14px;
  margin-top: 16px;
  font-size: 16px;
  color: #64748b;
  font-weight: 600;
}

.card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 24px 30px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
}

.card-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.card p, .card li {
  font-size: 18px;
  line-height: 1.7;
  color: #334155;
}

.stat-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.stat-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.stat-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.stat-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 18px 22px;
}

.stat-label {
  font-size: 15px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-val {
  font-family: 'Outfit', sans-serif;
  font-size: 36px;
  font-weight: 900;
  color: #0f172a;
  margin-top: 4px;
}

.stat-sub {
  font-size: 16px;
  color: #16a34a;
  font-weight: 600;
  margin-top: 4px;
}

.badge-verdict {
  background: #ecfdf5;
  color: #047857;
  border: 1px solid #a7f3d0;
  padding: 8px 22px;
  border-radius: 10px;
  font-weight: 800;
  font-size: 20px;
  display: inline-block;
}

.badge-blue {
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
  padding: 6px 14px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 15px;
}

table.report-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 18px;
}

table.report-table th {
  background: #f1f5f9;
  color: #475569;
  text-align: left;
  padding: 16px 20px;
  font-weight: 800;
  font-size: 19px;
  border-bottom: 2px solid #cbd5e1;
}

table.report-table td {
  padding: 16px 20px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
  vertical-align: middle;
  line-height: 1.5;
}

table.report-table tr:hover {
  background: #f8fafc;
}

.highlight-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px 20px;
}

.highlight-box h5 {
  font-size: 16px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.highlight-box p {
  font-size: 15px;
  line-height: 1.6;
  color: #475569;
}
"""

# ------------------------------------------------------------------------------
# INFOGRAPHIC CSS (High-Contrast, Portrait Poster 1200px Wide)
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
  background: linear-gradient(135deg, #064e3b 0%, #0f172a 100%);
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
  color: #6ee7b7;
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid rgba(16, 185, 129, 0.4);
  padding: 6px 16px;
  border-radius: 20px;
  letter-spacing: 1px;
}

.memo-num {
  font-size: 14px;
  color: #94a3b8;
  font-weight: 500;
}

.hero-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 42px;
  font-weight: 900;
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.hero-sub {
  font-size: 18px;
  color: #cbd5e1;
  margin-top: 10px;
  font-weight: 400;
}

.verdict-banner {
  margin-top: 28px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 14px;
  padding: 20px 24px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 18px;
  align-items: center;
}

.verdict-box h4 {
  font-size: 13px;
  text-transform: uppercase;
  color: #94a3b8;
  letter-spacing: 1px;
}

.verdict-tag {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 22px;
  font-weight: 800;
  color: #34d399;
  margin-top: 4px;
}

.v-item h5 {
  font-size: 13px;
  color: #94a3b8;
  text-transform: uppercase;
}

.v-item p {
  font-family: 'Outfit', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #ffffff;
  margin-top: 4px;
}

.info-body {
  padding: 40px 50px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  background: #f8fafc;
}

.section-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 28px 32px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
}

.sec-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid #f1f5f9;
  padding-bottom: 14px;
  margin-bottom: 20px;
}

.sec-title {
  font-family: 'Outfit', 'Noto Sans KR', sans-serif;
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 10px;
}

.sec-tag {
  font-size: 13px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  background: #f1f5f9;
  color: #475569;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.metric-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px 18px;
}

.m-label {
  font-size: 12px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.m-val {
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  font-weight: 900;
  color: #0f172a;
  margin-top: 4px;
}

.m-desc {
  font-size: 13px;
  color: #059669;
  font-weight: 600;
  margin-top: 4px;
}

.table-custom {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
}

.table-custom th {
  background: #f8fafc;
  padding: 12px 14px;
  text-align: left;
  font-weight: 700;
  color: #475569;
  border-bottom: 2px solid #e2e8f0;
}

.table-custom td {
  padding: 12px 14px;
  border-bottom: 1px solid #f1f5f9;
  color: #334155;
  line-height: 1.5;
}

.callout-box {
  background: #f0fdf4;
  border-left: 4px solid #10b981;
  padding: 16px 20px;
  border-radius: 0 12px 12px 0;
  margin-top: 14px;
}

.callout-box p {
  font-size: 15px;
  color: #065f46;
  line-height: 1.6;
  font-weight: 500;
}

.warn-box {
  background: #fef2f2;
  border-left: 4px solid #ef4444;
  padding: 16px 20px;
  border-radius: 0 12px 12px 0;
  margin-top: 14px;
}

.warn-box p {
  font-size: 15px;
  color: #991b1b;
  line-height: 1.6;
  font-weight: 500;
}

.info-footer {
  padding: 24px 50px;
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: #64748b;
  font-weight: 600;
}
"""

def generate_slide_en_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>UBER Investment Committee Decision Deck (English)</title>
<style>{SLIDE_CSS}</style>
</head>
<body>

<!-- SLIDE 1: Executive Verdict -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>UBER: Executive Investment Committee Verdict</h2>
      <p>Institutional Due Diligence & Decision Directive | October 7, 2026</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <span class="badge-verdict">OFFICIAL VERDICT: STRONG BUY / ASYMMETRIC ALPHA ENTRY</span>
          <span class="badge-blue" style="margin-left: 12px;">CONTRARIAN VALUE ACCUMULATION</span>
        </div>
        <div style="font-size: 18px; color: #64748b; font-weight: 700;">Principal Investor: <strong>BM사장님</strong></div>
      </div>
      <p style="font-size: 20px; line-height: 1.7; color: #1e293b;">
        Uber Technologies, Inc. (UBER) has corrected <strong>-31.8% from its 52-week peak ($100.35 to $68.45 USD)</strong> due to market overreaction regarding autonomous robotaxis. The Investment Committee concludes that this represents an exceptional disconnect between bearish headlines and soaring cash generation ($8.18B True FCF, PEG 0.69, Net Debt/EBITDA 0.64x). Autonomous vehicle adoption will serve as Uber's greatest historical margin expander rather than a terminal threat.
      </p>
    </div>

    <div class="stat-grid-4">
      <div class="stat-box">
        <div class="stat-label">Current Market Price</div>
        <div class="stat-val">$68.45</div>
        <div class="stat-sub">52W Low: $65.41 Support</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Conservative Intrinsic Value</div>
        <div class="stat-val">$88.00</div>
        <div class="stat-sub">+22.2% Margin of Safety</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">12M Target Price (Base)</div>
        <div class="stat-val">$98.00</div>
        <div class="stat-sub">+43.2% Expected Return</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Recommended Allocation</div>
        <div class="stat-val">3.5% - 4.5%</div>
        <div class="stat-sub">~$60,000 USD (~892 Shares)</div>
      </div>
    </div>

    <div class="stat-grid-3">
      <div class="highlight-box">
        <h5>🏛️ Capital Allocation Turnaround</h5>
        <p>Pruned non-core vanity units, generated $10.12B GAAP FCF, and executing a $7B share buyback program under Dara Khosrowshahi.</p>
      </div>
      <div class="highlight-box">
        <h5>🚗 Autonomous Fleet Aggregator</h5>
        <p>162M active users provide the indispensable liquidity layer for Waymo, Cruise, and Avride robotaxi fleets needing >75% utilization.</p>
      </div>
      <div class="highlight-box">
        <h5>🧩 Portfolio Gap-Filling</h5>
        <p>Beta of 1.26 with zero semiconductor capex correlation, providing vital factor diversification to BM사장님's 45.7% semi-heavy portfolio.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Document: DADAIC-IC-SLIDE-UBER-261007-EN</div>
    <div>Slide 1 of 5 | Executive Verdict</div>
  </div>
</div>

<!-- SLIDE 2: Multi-Year Empirical Validation -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Multi-Year Empirical Validation Scorecard</h2>
      <p>BM사장님 30-Year Veteran Investment Mandate | Mandatory Multi-Year Audit</p>
    </div>
    <div class="firm-tag">EMPIRICAL PROOF</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <table class="report-table">
        <thead>
          <tr>
            <th>Metric Category</th>
            <th>Multi-Year Audited Fact</th>
            <th>Peer / Benchmark Context</th>
            <th>Committee Institutional Verdict</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1-Year Return</strong></td>
            <td><strong style="color: #dc2626;">-30.99%</strong> ($100.35 ➔ $68.45)</td>
            <td>S&P 500: +24.5% / Tech: +35%</td>
            <td><span class="badge-blue">Oversold Sentiment Disconnect</span></td>
          </tr>
          <tr>
            <td><strong>3-Year Return & CAGR</strong></td>
            <td><strong style="color: #16a34a;">+51.23%</strong> (CAGR: <strong>+14.78%</strong>)</td>
            <td>Post-pandemic operational inflection</td>
            <td><span class="badge-blue">Proven Long-Term Alpha</span></td>
          </tr>
          <tr>
            <td><strong>5-Year Return & CAGR</strong></td>
            <td><strong style="color: #16a34a;">+44.61%</strong> (CAGR: <strong>+7.66%</strong>)</td>
            <td>Overcame 2022 high-rate bear market</td>
            <td><span class="badge-blue">Durable Moat Surpassed Cycles</span></td>
          </tr>
          <tr>
            <td><strong>Revenue Trajectory</strong></td>
            <td>'22: $31.88B ➔ '24: $43.98B ➔ <strong>TTM: $55.23B</strong></td>
            <td>Q2 '26 Gross Bookings $58B+ (+22% YoY)</td>
            <td><span class="badge-blue">Organic Scale Expansion</span></td>
          </tr>
          <tr>
            <td><strong>True FCF (Net of SBC)</strong></td>
            <td>'22: -$1.40B ➔ '24: +$5.10B ➔ <strong>TTM: +$8.18B</strong></td>
            <td>GAAP FCF $10.12B - SBC $1.94B</td>
            <td><span class="badge-blue">True Cash Flow Machine Validated</span></td>
          </tr>
          <tr>
            <td><strong>Balance Sheet Solvency</strong></td>
            <td>Cash: $7.63B vs Debt: $12.08B (Net Debt: $4.45B)</td>
            <td>Net Debt / EBITDA: <strong>0.64x</strong></td>
            <td><span class="badge-blue">Investment Grade Solvency</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="stat-grid-3">
      <div class="stat-box">
        <div class="stat-label">TTM GAAP Free Cash Flow</div>
        <div class="stat-val">$10.12B</div>
        <div class="stat-sub">First time in corporate history</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Stock-Based Comp Ratio</div>
        <div class="stat-val">3.5%</div>
        <div class="stat-sub">SBC / Revenue down from 8.2% in 2021</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Return on Equity (ROE)</div>
        <div class="stat-val">37.2%</div>
        <div class="stat-sub">Top decile platform profitability</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Document: DADAIC-IC-SLIDE-UBER-261007-EN</div>
    <div>Slide 2 of 5 | Empirical Validation</div>
  </div>
</div>

<!-- SLIDE 3: Master Evaluation Matrix -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>The Masters' Consensus & Philosophical Matrix</h2>
      <p>Multi-Disciplinary Value, Growth & Market Technician Synthesis</p>
    </div>
    <div class="firm-tag">PHILOSOPHICAL ALIGNMENT</div>
  </div>

  <div class="slide-body">
    <div class="stat-grid-2">
      <div class="card">
        <div class="card-title">🛡️ Warren Buffett: Toll Bridge Moat</div>
        <p><strong>Verdict: Strong Buy (22.2% Margin of Safety)</strong></p>
        <p style="margin-top: 8px;">Uber operates an essential toll bridge on worldwide urban transport without owning vehicles or funding capital depreciation. CEO Dara Khosrowshahi eliminated cash-burning experiments, generating $10B+ FCF with disciplined $7B buybacks.</p>
      </div>

      <div class="card">
        <div class="card-title">🔄 Charlie Munger: Inversion & Network Flywheel</div>
        <p><strong>Verdict: Exceptional Network Moat / Inversion Solved</strong></p>
        <p style="margin-top: 8px;"><em>Invert: What kills Uber?</em> An autonomous fleet bypassing Uber completely. <em>Refutation:</em> AV fleets need >75% utilization to survive massive hardware capex. Uber's 162M active users are indispensable to robotaxi operators.</p>
      </div>

      <div class="card">
        <div class="card-title">📈 Peter Lynch: PEG 0.69 Screaming Bargain</div>
        <p><strong>Verdict: Fast Grower / Conviction Buy</strong></p>
        <p style="margin-top: 8px;">Forward P/E is 15.5x against 22.5% expected EPS growth. Lynch PEG ratio of <strong>0.69</strong> is a generational buying signal for a dominant market leader possessing zero physical inventory drag.</p>
      </div>

      <div class="card">
        <div class="card-title">⚡ Stanley Druckenmiller: 4.2 : 1 Asymmetric Alpha</div>
        <p><strong>Verdict: High-Conviction Asymmetric Long</strong></p>
        <p style="margin-top: 8px;">The market misinterprets robotaxis as a terminal risk. Over the next 18-24 months, removing driver payouts (~70% of bookings) will expand operating margins from 13% toward 25%+, generating immense operational leverage.</p>
      </div>
    </div>

    <div class="card" style="padding: 18px 26px; background: #f0fdf4; border: 1px solid #bbf7d0;">
      <h4 style="font-size: 19px; color: #166534; font-weight: 800; margin-bottom: 6px;">CIO Final Conflict Arbitration</h4>
      <p style="font-size: 17px; color: #14532d; line-height: 1.6;">
        Technical resistance at the 200 SMA ($74.63) is decisively overridden by foundational valuation fundamentals. Trading at 15.5x forward earnings and ~17x True FCF with 22% bookings growth represents an irrationally priced margin of safety.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>Document: DADAIC-IC-SLIDE-UBER-261007-EN</div>
    <div>Slide 3 of 5 | Master Consensus</div>
  </div>
</div>

<!-- SLIDE 4: Scenario Valuation & AV Reality -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Scenario-Based Valuation & The AV Economics</h2>
      <p>12-Month Target Price Projections & Autonomous Fleet Realities</p>
    </div>
    <div class="firm-tag">VALUATION ARCHITECTURE</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <div class="card-title">🎯 12-Month Institutional Price Targets</div>
      <table class="report-table">
        <thead>
          <tr>
            <th>Scenario</th>
            <th>Probability</th>
            <th>Valuation Multiple Applied</th>
            <th>Target Price ($ USD)</th>
            <th>Implied Return</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bull Case (AV Fleet Scale & High Ads Growth)</strong></td>
            <td>25%</td>
            <td>22.0x Forward P/E (FY27E EPS $5.70)</td>
            <td><strong>$125.40</strong></td>
            <td><strong style="color: #16a34a;">+83.2%</strong></td>
          </tr>
          <tr>
            <td><strong>Base Case (Sustained 20% Bookings & 15% Margin)</strong></td>
            <td>55%</td>
            <td>18.5x Forward P/E (FY27E EPS $5.30)</td>
            <td><strong>$98.05</strong></td>
            <td><strong style="color: #16a34a;">+43.2%</strong></td>
          </tr>
          <tr>
            <td><strong>Bear Case (AV Integration Delays & Macro Slump)</strong></td>
            <td>20%</td>
            <td>13.5x Forward P/E (FY27E EPS $4.60)</td>
            <td><strong>$62.10</strong></td>
            <td><strong style="color: #dc2626;">-9.3%</strong></td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top: 14px; font-size: 18px; font-weight: 700; color: #0f172a;">
        Probability-Weighted 12-Month Expected Target: <span style="color: #16a34a; font-size: 22px;">$97.70 USD</span> (+42.7% expected return from current price).
      </div>
    </div>

    <div class="stat-grid-3">
      <div class="highlight-box">
        <h5>🤖 Waymo & Cruise Integration</h5>
        <p>Already live in Phoenix, Austin, and Atlanta. AV OEMs recognize that consumer acquisition cost (CAC) on a standalone app destroys unit economics.</p>
      </div>
      <div class="highlight-box">
        <h5>🚗 Tesla Cybercab Context</h5>
        <p>Tesla has zero commercial driverless licenses in operation. Full commercial deployment is years away; Uber remains the default real-world demand hub.</p>
      </div>
      <div class="highlight-box">
        <h5>📢 High-Margin Advertising Engine</h5>
        <p>$1.2B+ advertising run-rate flowing directly to the bottom line at 80%+ gross margin, expanding consolidated corporate EBITDA margins.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>Document: DADAIC-IC-SLIDE-UBER-261007-EN</div>
    <div>Slide 4 of 5 | Valuation Scenarios</div>
  </div>
</div>

<!-- SLIDE 5: Portfolio Allocation & Execution -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>Tactical Execution & Thesis Invalidation Clause</h2>
      <p>BM사장님 Portfolio Blueprint (`my-portfolio.yaml`) & Risk Management</p>
    </div>
    <div class="firm-tag">EXECUTION DIRECTIVES</div>
  </div>

  <div class="slide-body">
    <div class="stat-grid-2">
      <div class="card">
        <div class="card-title">🧩 Portfolio Diagnostic & Gap-Filling</div>
        <p><strong>Total Portfolio Assets: $1,800,000.00 USD (Equities: $1,486,521.84 / 82.6% | Cash: $313,478.16 / 17.4%)</strong></p>
        <p style="margin-top: 8px;"><strong>The Semi Factor Overhang:</strong> NVDA (22.8%), AVGO (8.4%), AMD (7.4%), TSM (3.6%), MU (2.8%) represent <strong>45.68% pure semiconductor exposure</strong> ($714.6k USD).</p>
        <p style="margin-top: 8px;"><strong>UBER Role:</strong> Low beta (1.26), non-correlated real economy cash flow, diluting semiconductor cyclicality while adding asymmetric growth.</p>
      </div>

      <div class="card">
        <div class="card-title">⚡ Phased 2-Tranche Trade Matrix</div>
        <ul style="margin-left: 20px; margin-top: 8px;">
          <li><strong>Tranche 1 (Immediate Market Order):</strong> Deploy <strong>$30,000 USD</strong> at <strong>$68.45 USD</strong> (~438 shares) using dry powder cash.</li>
          <li><strong>Tranche 2 (Pullback Limit Order):</strong> Place resting limit order for <strong>$30,000 USD</strong> at <strong>$66.00 USD</strong> (~454 shares).</li>
          <li><strong>Total Target Size:</strong> <strong>892 Shares</strong> (~$60,000 USD | <strong>3.83% of Portfolio</strong>).</li>
          <li><strong>Hard Stop-Loss / Disaster Floor:</strong> <strong>$62.50 USD</strong> (-8.7%).</li>
        </ul>
      </div>
    </div>

    <div class="card" style="background: #fef2f2; border: 1px solid #fecaca;">
      <h4 style="font-size: 20px; color: #991b1b; font-weight: 800; margin-bottom: 6px;">⚠️ The Non-Negotiable Thesis Invalidation Clause (100% Exit Trigger)</h4>
      <p style="font-size: 17px; color: #7f1d1d; line-height: 1.6;">
        "This position will be liquidated immediately in full (100% exit) if Waymo, Cruise, and major AV OEMs completely terminate dispatch agreements with Uber and launch price-undercutting proprietary networks that cause Uber's Mobility Gross Bookings to decline YoY for two consecutive quarters; OR if regulatory mandates classify gig drivers as W-2 employees globally without pricing pass-through ability, structurally crushing operating margins below 5%."
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>Document: DADAIC-IC-SLIDE-UBER-261007-EN</div>
    <div>Slide 5 of 5 | Portfolio Allocation</div>
  </div>
</div>

</body>
</html>
"""

def generate_slide_kr_html():
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>UBER 투자위원회 공식 의사결정 프레젠테이션 (한글판)</title>
<style>{SLIDE_CSS}</style>
</head>
<body>

<!-- 슬라이드 1: 최종 집행 판정 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>UBER: 투자위원회 최종 의사결정 집행 판정</h2>
      <p>기관급 정밀 실사 및 포트폴리오 편입 지침 | 2026년 10월 7일</p>
    </div>
    <div class="firm-tag">DADAIC INVESTMENT FIRM</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
          <span class="badge-verdict">공식 판정: 강력 매수 및 역발상 알파 편입 (STRONG BUY)</span>
          <span class="badge-blue" style="margin-left: 12px;">저평가 과매도 분할 매집</span>
        </div>
        <div style="font-size: 18px; color: #64748b; font-weight: 700;">핵심 의뢰자: <strong>BM사장님</strong></div>
      </div>
      <p style="font-size: 20px; line-height: 1.7; color: #1e293b;">
        우버 테크놀로지스(UBER)는 로보택시 출현에 대한 시장의 과도한 공포로 <strong>52주 최고가 대비 -31.8% 급락($100.35 ➔ $68.45 달러)</strong>했습니다. 본 투자위원회는 이러한 주가 하락이 사상 최대의 현금 창출력($8.18B 달러 진성 FCF, PEG 0.69, 순부채/EBITDA 0.64배)과 완전히 괴리된 극단적 저평가 기회라고 판단합니다. 자율주행 기술 확산은 우버의 마진을 폭발시킬 역사적 촉매제입니다.
      </p>
    </div>

    <div class="stat-grid-4">
      <div class="stat-box">
        <div class="stat-label">현재 시장 주가</div>
        <div class="stat-val">$68.45</div>
        <div class="stat-sub">52주 저점 지지선: $65.41</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">보수적 본질 가치</div>
        <div class="stat-val">$88.00</div>
        <div class="stat-sub">+22.2% 안전마진 확보</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">12개월 기본 목표 주가</div>
        <div class="stat-val">$98.00</div>
        <div class="stat-sub">+43.2% 기대 수익률</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">권고 목표 편입 비중</div>
        <div class="stat-val">3.5% - 4.5%</div>
        <div class="stat-sub">약 $60,000 달러 (약 892주)</div>
      </div>
    </div>

    <div class="stat-grid-3">
      <div class="highlight-box">
        <h5>🏛️ 자본 배치 턴어라운드 완성</h5>
        <p>적자 사업을 과감히 정리하고 연간 $10.12B 달러의 FCF를 창출하며 $7B 달러 자사주 매입 프로그램을 집행 중입니다.</p>
      </div>
      <div class="highlight-box">
        <h5>🚗 자율주행 차량 수요 독점자</h5>
        <p>1억 6,200만 명의 활성 이용자 풀을 통해 웨이모, 크루즈 등 로보택시 제조사들이 필수적으로 거쳐야 할 배차 플랫폼입니다.</p>
      </div>
      <div class="highlight-box">
        <h5>🧩 포트폴리오 반도체 편중 해소</h5>
        <p>베타 1.26 및 반도체 사이클과 상관계수 제로인 자산으로, BM사장님의 45.7% 반도체 편중 포트폴리오를 완벽히 보완합니다.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>문서 번호: DADAIC-IC-SLIDE-UBER-261007-KR</div>
    <div>슬라이드 1 / 5 | 최종 집행 판정</div>
  </div>
</div>

<!-- 슬라이드 2: 다개년 실증 데이터 검증 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>다개년 실증 데이터 전수 검증 성적표</h2>
      <p>BM사장님 30년 베테랑 투자 원칙 | 재무제표 공시 수치 기반 검증</p>
    </div>
    <div class="firm-tag">실증 팩트 검증</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <table class="report-table">
        <thead>
          <tr>
            <th>검증 핵심 지표</th>
            <th>다개년 감사 실증 데이터</th>
            <th>동종 업계 및 시장 벤치마크</th>
            <th>위원회 공식 검증 판정</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>최근 1년 총수익률</strong></td>
            <td><strong style="color: #dc2626;">-30.99%</strong> ($100.35 ➔ $68.45)</td>
            <td>S&P 500: +24.5% / 나스닥: +35%</td>
            <td><span class="badge-blue">공포에 의한 과매도 저평가</span></td>
          </tr>
          <tr>
            <td><strong>최근 3년 수익률 및 CAGR</strong></td>
            <td><strong style="color: #16a34a;">+51.23%</strong> (CAGR: <strong>+14.78%</strong>)</td>
            <td>팬데믹 이후 구조적 흑자 안착</td>
            <td><span class="badge-blue">검증된 장기 복리 성장</span></td>
          </tr>
          <tr>
            <td><strong>최근 5년 수익률 및 CAGR</strong></td>
            <td><strong style="color: #16a34a;">+44.61%</strong> (CAGR: <strong>+7.66%</strong>)</td>
            <td>2022년 고금리 약세장 완벽 극복</td>
            <td><span class="badge-blue">사이클을 관통하는 경제적 해자</span></td>
          </tr>
          <tr>
            <td><strong>매출액 성장 궤적</strong></td>
            <td>2022: $31.88B ➔ 2024: $43.98B ➔ <strong>TTM: $55.23B</strong></td>
            <td>2026 Q2 총예약액 $58B 돌파 (+22% YoY)</td>
            <td><span class="badge-blue">글로벌 1위 네트워크 규모 확장</span></td>
          </tr>
          <tr>
            <td><strong>진성 FCF (SBC 차감 후)</strong></td>
            <td>2022: -$1.40B ➔ 2024: +$5.10B ➔ <strong>TTM: +$8.18B</strong></td>
            <td>GAAP FCF $10.12B - 주식보상 $1.94B</td>
            <td><span class="badge-blue">경이로운 현금 창출력 입증</span></td>
          </tr>
          <tr>
            <td><strong>대차대조표 건전성</strong></td>
            <td>현금: $7.63B vs 부채: $12.08B (순부채: $4.45B)</td>
            <td>순부채 / EBITDA: <strong>0.64배</strong></td>
            <td><span class="badge-blue">투자적격 등급의 우량 재무구조</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="stat-grid-3">
      <div class="stat-box">
        <div class="stat-label">TTM GAAP 잉여현금흐름</div>
        <div class="stat-val">$10.12B</div>
        <div class="stat-sub">창사 이래 최초 $10B 돌파</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">주식보상비용(SBC) 비율</div>
        <div class="stat-val">3.5%</div>
        <div class="stat-sub">2021년 8.2%에서 대폭 축소</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">자기자본이익률 (ROE)</div>
        <div class="stat-val">37.2%</div>
        <div class="stat-sub">업계 최상위 플랫폼 수익성</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>문서 번호: DADAIC-IC-SLIDE-UBER-261007-KR</div>
    <div>슬라이드 2 / 5 | 실증 성적표</div>
  </div>
</div>

<!-- 슬라이드 3: 5대 투자 거장 & 수석 시장 기술적 분석가 종합 검증 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>5대 투자 거장 & 수석 시장 기술적 분석가 종합 검증</h2>
      <p>가치, 성장, 비대칭 알파, 차트 기술적 분석의 종합 검증</p>
    </div>
    <div class="firm-tag">철학적 종합 검증</div>
  </div>

  <div class="slide-body">
    <div class="stat-grid-2">
      <div class="card">
        <div class="card-title">🛡️ 워런 버핏: 디지털 통행세(Toll Bridge) 해자</div>
        <p><strong>판정: 강력 매수 (22.2% 안전마진 확보)</strong></p>
        <p style="margin-top: 8px;">차량을 소유하거나 감가상각비를 부담하지 않고 전 세계 이동 및 배달 거래에서 25%의 수수료를 징수합니다. 다라 CEO의 엄격한 자본 배치로 $10B 현금 창출 및 $7B 자사주 매입을 가동 중입니다.</p>
      </div>

      <div class="card">
        <div class="card-title">🔄 찰리 멍거: 역발상 반증(Inversion) 극복</div>
        <p><strong>판정: 최상위 네트워크 해자 / 반증 돌파</strong></p>
        <p style="margin-top: 8px;"><em>역발상: 우버를 무너뜨리는 것은 무엇인가?</em> 완성차의 독자 로보택시 앱 출시. <em>반증 해소:</em> 로보택시는 가동률(70% 이상) 유지가 생명이며, 1억 6천만 결제 고객을 가진 우버와 제휴하는 것이 필수적입니다.</p>
      </div>

      <div class="card">
        <div class="card-title">📈 피터 린치: PEG 0.69의 바겐세일</div>
        <p><strong>판정: 고성장주 / 확신 매수</strong></p>
        <p style="margin-top: 8px;">선행 P/E 15.5배 대비 주당순이익(EPS) 성장률 전망 22.5%로 PEG는 <strong>0.69</strong>입니다. 재고 부담 없는 독점적 플랫폼 기업이 PEG 0.7 미만으로 떨어진 것은 역사적 매수 타점입니다.</p>
      </div>

      <div class="card">
        <div class="card-title">⚡ 스탠리 드러켄밀러: 4.2 : 1 비대칭 롱 포지션</div>
        <p><strong>판정: 고확신 비대칭 알파 매수</strong></p>
        <p style="margin-top: 8px;">시장은 로보택시를 악재로 오판하고 있습니다. 운전기사 정산금(~70%)이 제거되면 우버의 영업이익률은 13%에서 25% 이상으로 대폭 도약하는 거대한 운영 레버리지가 발생합니다.</p>
      </div>
    </div>

    <div class="card" style="padding: 18px 26px; background: #f0fdf4; border: 1px solid #bbf7d0;">
      <h4 style="font-size: 19px; color: #166534; font-weight: 800; margin-bottom: 6px;">CIO 최종 철학적 충돌 조정 평결</h4>
      <p style="font-size: 17px; color: #14532d; line-height: 1.6;">
        200일선($74.63) 아래에 위치한 단기 역배열 우려는 압도적인 펀더멘털과 저평가 지표에 의해 완벽히 상쇄됩니다. 선행 P/E 15.5배, 연간 $8.2B 진성 FCF를 창출하는 기업에 대한 과매도 패닉은 역발상 가치 매집의 최고의 기회입니다.
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>문서 번호: DADAIC-IC-SLIDE-UBER-261007-KR</div>
    <div>슬라이드 3 / 5 | 거장 평가 매트릭스</div>
  </div>
</div>

<!-- 슬라이드 4: 시나리오 밸류에이션 및 자율주행 경제학 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>시나리오별 밸류에이션 및 자율주행 경제학</h2>
      <p>12개월 목표 주가 시뮬레이션 및 로보택시 수혜 구조</p>
    </div>
    <div class="firm-tag">가치 평가 프레임워크</div>
  </div>

  <div class="slide-body">
    <div class="card">
      <div class="card-title">🎯 12개월 기관급 목표 주가 시뮬레이션</div>
      <table class="report-table">
        <thead>
          <tr>
            <th>시나리오</th>
            <th>발생 확률</th>
            <th>적용 밸류에이션 배수</th>
            <th>목표 주가 ($ 달러)</th>
            <th>기대 수익률</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>낙관 시나리오 (자율주행 제휴 확대 및 광고 급증)</strong></td>
            <td>25%</td>
            <td>선행 P/E 22.0배 (FY27E EPS $5.70)</td>
            <td><strong>$125.40 달러</strong></td>
            <td><strong style="color: #16a34a;">+83.2%</strong></td>
          </tr>
          <tr>
            <td><strong>기본 시나리오 (총예약액 20% 성장 및 마진 확장)</strong></td>
            <td>55%</td>
            <td>선행 P/E 18.5배 (FY27E EPS $5.30)</td>
            <td><strong>$98.05 달러</strong></td>
            <td><strong style="color: #16a34a;">+43.2%</strong></td>
          </tr>
          <tr>
            <td><strong>비관 시나리오 (자율주행 지연 및 거시 소비 위축)</strong></td>
            <td>20%</td>
            <td>선행 P/E 13.5배 (FY27E EPS $4.60)</td>
            <td><strong>$62.10 달러</strong></td>
            <td><strong style="color: #dc2626;">-9.3%</strong></td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top: 14px; font-size: 18px; font-weight: 700; color: #0f172a;">
        확률 가중 기대 12개월 목표 주가: <span style="color: #16a34a; font-size: 22px;">$97.70 달러</span> (현재가 대비 기대 수익률: +42.7%).
      </div>
    </div>

    <div class="stat-grid-3">
      <div class="highlight-box">
        <h5>🤖 웨이모 및 크루즈의 현실</h5>
        <p>피닉스, 오스틴, 애틀랜타에서 우버를 통해 배차 중입니다. 완성차 진영도 자체 앱의 고객 유치 비용(CAC)을 감당하기 어렵습니다.</p>
      </div>
      <div class="highlight-box">
        <h5>🚗 테슬라 사이버캡의 본질</h5>
        <p>상용 무인 허가가 전무하며 양산 배치까지 수년이 소요됩니다. 우버는 실물 온디맨드 수요를 독점하는 최종 관문입니다.</p>
      </div>
      <div class="highlight-box">
        <h5>📢 초고마진 디지털 광고 사업</h5>
        <p>연간 $1.2B 달러 규모로 급성장한 광고 매출은 마진율 80% 이상으로 전사 영업이익률을 지속적으로 끌어올립니다.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div>문서 번호: DADAIC-IC-SLIDE-UBER-261007-KR</div>
    <div>슬라이드 4 / 5 | 시나리오 평가</div>
  </div>
</div>

<!-- 슬라이드 5: 포트폴리오 자산배분 및 청산 원칙 -->
<div class="slide">
  <div class="slide-header">
    <div class="slide-title-wrap">
      <h2>실전 매수 집행 및 투자 철회(Exit) 원칙</h2>
      <p>BM사장님 맞춤형 자산배분 (`my-portfolio.yaml`) 및 위험 통제</p>
    </div>
    <div class="firm-tag">실전 매매 집행 지침</div>
  </div>

  <div class="slide-body">
    <div class="stat-grid-2">
      <div class="card">
        <div class="card-title">🧩 포트폴리오 진단 및 공백 보완</div>
        <p><strong>총 운용 자산: $1,800,000.00 달러 (보유 주식: $1,486,521.84 / 82.6% | 현금 비축: $313,478.16 / 17.4%)</strong></p>
        <p style="margin-top: 8px;"><strong>반도체 집중 위험:</strong> NVDA(22.8%), AVGO(8.4%), AMD(7.4%), TSM(3.6%), MU(2.8%) 등 <strong>순수 반도체 비중이 45.68% ($714,642 달러)</strong>에 달함.</p>
        <p style="margin-top: 8px;"><strong>UBER의 보완 역할:</strong> 베타 1.26의 실물 소비 플랫폼으로 반도체 Capex 충격 시 강력한 포트폴리오 완충재 역할을 수행합니다.</p>
      </div>

      <div class="card">
        <div class="card-title">⚡ 2단계 분할 매수 실행안</div>
        <ul style="margin-left: 20px; margin-top: 8px;">
          <li><strong>1차 즉시 시장가 매수:</strong> 현금 유동성을 활용해 <strong>$68.45 달러</strong>에서 <strong>$30,000 달러</strong> (약 438주) 집행.</li>
          <li><strong>2차 눌림목 지정가 매수:</strong> 52주 저점 지지선인 <strong>$66.00 달러</strong>에 <strong>$30,000 달러</strong> (약 454주) 예약 대기.</li>
          <li><strong>최종 목표 보유량:</strong> <strong>892주</strong> (약 $60,000 달러 | <strong>포트폴리오 비중 약 3.83%</strong>).</li>
          <li><strong>철통 손절선:</strong> <strong>$62.50 달러</strong> (-8.7% 하향 이탈 시 전량 손절).</li>
        </ul>
      </div>
    </div>

    <div class="card" style="background: #fef2f2; border: 1px solid #fecaca;">
      <h4 style="font-size: 20px; color: #991b1b; font-weight: 800; margin-bottom: 6px;">⚠️ 타협 없는 투자 철회 및 전량 매도 원칙 (100% Exit Trigger)</h4>
      <p style="font-size: 17px; color: #7f1d1d; line-height: 1.6;">
        "웨이모, 크루즈 및 주요 완성차 OEM들이 우버와의 제휴를 전면 파기하고 독자 배차 앱을 출시하여 우버의 모빌리티 총예약액이 2개 분기 연속 전년 대비 역성장(Negative YoY)을 기록하거나, 미국과 유럽 전역에서 기그 노동자의 정규직 전환이 의무화되어 영업이익률이 구조적으로 5% 미만으로 붕괴될 경우 보유 수량 전량을 즉시 매도(100% 청산)합니다."
      </p>
    </div>
  </div>

  <div class="slide-footer">
    <div>문서 번호: DADAIC-IC-SLIDE-UBER-261007-KR</div>
    <div>슬라이드 5 / 5 | 실전 집행 지침</div>
  </div>
</div>

</body>
</html>
"""

def generate_infographic_en_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>UBER Investment Committee Strategic Infographic (English)</title>
<style>{INFOGRAPHIC_CSS}</style>
</head>
<body>

<div class="infographic-container">
  <!-- HERO HEADER -->
  <div class="hero-header">
    <div class="hero-top">
      <div class="firm-badge">DADAIC INVESTMENT FIRM • STRATEGIC RESEARCH</div>
      <div class="memo-num">CONTROL NO: DADAIC-IC-INFO-UBER-261007-EN</div>
    </div>
    <h1 class="hero-title">UBER TECHNOLOGIES (NYSE: UBER)</h1>
    <p class="hero-sub">The Indispensable Toll Bridge of Global Mobility & Autonomous Fleet Orchestration</p>
    
    <div class="verdict-banner">
      <div class="verdict-box">
        <h4>Executive Verdict</h4>
        <div class="verdict-tag">STRONG BUY / ASYMMETRIC ALPHA</div>
      </div>
      <div class="v-item">
        <h5>Current Price</h5>
        <p>$68.45 USD</p>
      </div>
      <div class="v-item">
        <h5>Intrinsic Value</h5>
        <p>$88.00 USD</p>
      </div>
      <div class="v-item">
        <h5>12M Target (Base)</h5>
        <p>$98.00 USD</p>
      </div>
    </div>
  </div>

  <!-- INFOGRAPHIC BODY -->
  <div class="info-body">
    <!-- SECTION 1: EMPIRICAL SCORECARD -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">📊 Multi-Year Empirical Validation Scorecard</div>
        <div class="sec-tag">BM사장님 30-Year Mandate</div>
      </div>
      
      <div class="grid-4">
        <div class="metric-card">
          <div class="m-label">1-Year Total Return</div>
          <div class="m-val" style="color: #dc2626;">-30.99%</div>
          <div class="m-desc">Pullback from $100.35 High</div>
        </div>
        <div class="metric-card">
          <div class="m-label">3-Year Return & CAGR</div>
          <div class="m-val" style="color: #059669;">+51.2%</div>
          <div class="m-desc">CAGR: +14.78% from $45.68</div>
        </div>
        <div class="metric-card">
          <div class="m-label">TTM True FCF (Net of SBC)</div>
          <div class="m-val">$8.18B</div>
          <div class="m-desc">GAAP FCF $10.12B - SBC $1.94B</div>
        </div>
        <div class="metric-card">
          <div class="m-label">Peter Lynch PEG Ratio</div>
          <div class="m-val" style="color: #2563eb;">0.69</div>
          <div class="m-desc">P/E 15.5x / Growth 22.5%</div>
        </div>
      </div>

      <div class="callout-box">
        <p><strong>Audited Inflection:</strong> Operating Income swung from -$1.83B (2022) to +$5.57B (2025) and $6.69B TTM. Gross Bookings reached $58B+ in Q2 2026 (+22% YoY), demonstrating bulletproof secular demand.</p>
      </div>
    </div>

    <!-- SECTION 2: THE 5 MASTERS & CHIEF TECHNICIAN -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">🏛️ The 5 Masters & Chief Technician Evaluation</div>
        <div class="sec-tag">Unanimous Consensus</div>
      </div>

      <div class="grid-2">
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">🛡️ Warren Buffett (Value Lens)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>Verdict: Strong Buy (22.2% Margin of Safety).</strong> Toll bridge on urban movement with zero vehicle capital expenditure. Disciplined capital allocation: $7B buyback program funded by genuine operating cash.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">🔄 Charlie Munger (Inversion Lens)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>Verdict: Top-Tier Network Flywheel.</strong> Inversion solved: AV makers cannot survive low fleet utilization. Uber's 162M active users are indispensable for amortizing expensive robotaxi sensors.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">📈 Peter Lynch (Growth Lens)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>Verdict: Conviction Buy (PEG 0.69).</strong> Forward P/E of 15.5x is lower than the S&P 500 average, despite bookings growing +22% YoY. Rare mispricing of a dominant consumer duopolist.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">⚡ Stanley Druckenmiller (Macro Lens)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>Verdict: 4.2 : 1 Asymmetric Long.</strong> Driver payouts represent ~70% of bookings. The transition to autonomous vehicles will expand operating margins from 13% toward 25%+.
          </p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: PEER BENCHMARKING -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">⚔️ Head-to-Head Peer Benchmarking</div>
        <div class="sec-tag">Valuation & Margins</div>
      </div>

      <table class="table-custom">
        <thead>
          <tr>
            <th>Company</th>
            <th>Market Cap</th>
            <th>Forward P/E</th>
            <th>EV / EBITDA</th>
            <th>Operating Margin</th>
            <th>ROE (%)</th>
            <th>Beta</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: #f0fdf4; font-weight: 700;">
            <td>Uber (UBER)</td>
            <td>$139.8B</td>
            <td>15.5x</td>
            <td>20.3x</td>
            <td>13.3%</td>
            <td>37.2%</td>
            <td>1.26</td>
          </tr>
          <tr>
            <td>DoorDash (DASH)</td>
            <td>$82.9B</td>
            <td>23.2x</td>
            <td>57.0x</td>
            <td>3.9%</td>
            <td>8.9%</td>
            <td>1.89</td>
          </tr>
          <tr>
            <td>Lyft (LYFT)</td>
            <td>$5.9B</td>
            <td>7.2x</td>
            <td>117.3x</td>
            <td>2.6%</td>
            <td>152.6%</td>
            <td>1.96</td>
          </tr>
          <tr>
            <td>Alphabet (GOOG)</td>
            <td>$4,248B</td>
            <td>22.9x</td>
            <td>23.7x</td>
            <td>34.0%</td>
            <td>48.7%</td>
            <td>1.21</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- SECTION 4: PORTFOLIO ALLOCATION & INITIATION -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">🎯 Portfolio Allocation Blueprint (`my-portfolio.yaml`)</div>
        <div class="sec-tag">Factor Gap-Filling</div>
      </div>

      <div class="grid-3">
        <div class="metric-card">
          <div class="m-label">Tranche 1 (Market Order)</div>
          <div class="m-val">$30,000</div>
          <div class="m-desc">~438 Shares @ $68.45 USD</div>
        </div>
        <div class="metric-card">
          <div class="m-label">Tranche 2 (Pullback Limit)</div>
          <div class="m-val">$30,000</div>
          <div class="m-desc">~454 Shares @ $66.00 USD</div>
        </div>
        <div class="metric-card">
          <div class="m-label">Hard Stop-Loss Floor</div>
          <div class="m-val" style="color: #dc2626;">$62.50</div>
          <div class="m-desc">-8.7% Risk Management Floor</div>
        </div>
      </div>

      <div class="warn-box">
        <p><strong>Thesis Invalidation Exit Directive:</strong> 100% position liquidation triggered if Waymo/Cruise terminate partnerships and Uber Mobility bookings turn negative YoY for two consecutive quarters, or if global gig worker reclassification reduces operating margins below 5%.</p>
      </div>
    </div>
  </div>

  <!-- INFOGRAPHIC FOOTER -->
  <div class="info-footer">
    <div>Prepared for: BM사장님 | DADAIC Investment Firm</div>
    <div>Strict Currency: Pure USD ($) | No KRW Converted</div>
  </div>
</div>

</body>
</html>
"""

def generate_infographic_kr_html():
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>UBER 투자위원회 핵심 전략 인포그래픽 (한글판)</title>
<style>{INFOGRAPHIC_CSS}</style>
</head>
<body>

<div class="infographic-container">
  <!-- HERO HEADER -->
  <div class="hero-header">
    <div class="hero-top">
      <div class="firm-badge">DADAIC INVESTMENT FIRM • 기관 리서치 본부</div>
      <div class="memo-num">문서 번호: DADAIC-IC-INFO-UBER-261007-KR</div>
    </div>
    <h1 class="hero-title">우버 테크놀로지스 (NYSE: UBER)</h1>
    <p class="hero-sub">전 세계 도시 교통을 독점하는 디지털 통행세 징수소 및 자율주행 배차 오케스트레이터</p>
    
    <div class="verdict-banner">
      <div class="verdict-box">
        <h4>투자위원회 최종 판정</h4>
        <div class="verdict-tag">강력 매수 / 역발상 알파 편입</div>
      </div>
      <div class="v-item">
        <h5>현재 시장가</h5>
        <p>$68.45 달러</p>
      </div>
      <div class="v-item">
        <h5>보수적 본질가치</h5>
        <p>$88.00 달러</p>
      </div>
      <div class="v-item">
        <h5>12개월 목표가</h5>
        <p>$98.00 달러</p>
      </div>
    </div>
  </div>

  <!-- INFOGRAPHIC BODY -->
  <div class="info-body">
    <!-- SECTION 1: EMPIRICAL SCORECARD -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">📊 다개년 실증 데이터 전수 검증 성적표</div>
        <div class="sec-tag">BM사장님 30년 투자 원칙</div>
      </div>
      
      <div class="grid-4">
        <div class="metric-card">
          <div class="m-label">최근 1년 총수익률</div>
          <div class="m-val" style="color: #dc2626;">-30.99%</div>
          <div class="m-desc">52주 고점($100.35) 대비 과매도</div>
        </div>
        <div class="metric-card">
          <div class="m-label">최근 3년 수익률 및 CAGR</div>
          <div class="m-val" style="color: #059669;">+51.2%</div>
          <div class="m-desc">CAGR: +14.78% ($45.68에서 성장)</div>
        </div>
        <div class="metric-card">
          <div class="m-label">TTM 진성 FCF (SBC 차감 후)</div>
          <div class="m-val">$8.18B</div>
          <div class="m-desc">GAAP FCF $10.12B - SBC $1.94B</div>
        </div>
        <div class="metric-card">
          <div class="m-label">피터 린치 PEG 비율</div>
          <div class="m-val" style="color: #2563eb;">0.69</div>
          <div class="m-desc">P/E 15.5배 / EPS 성장률 22.5%</div>
        </div>
      </div>

      <div class="callout-box">
        <p><strong>실증 턴어라운드 확인:</strong> 영업이익이 2022년 -$1.83B 달러 적자에서 2025년 +$5.57B 달러, 최근 4분기 합산 $6.69B 달러로 폭발적 개선. 2026 Q2 총예약액은 $58B 달러 돌파(+22% YoY)로 흔들림 없는 독점적 수요 증명.</p>
      </div>
    </div>

    <!-- SECTION 2: THE 5 MASTERS & CHIEF TECHNICIAN -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">🏛️ 5대 투자 거장 & 수석 시장 기술적 분석가 심층 평가</div>
        <div class="sec-tag">만장일치 매수 추천</div>
      </div>

      <div class="grid-2">
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">🛡️ 워런 버핏 (가치 투자 관점)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>판정: 강력 매수 (22.2% 안전마진 확보).</strong> 차량 자산 소유 없이 25%의 통행세를 거두는 독점 비즈니스. $7B 규모 자사주 매입으로 주주 환원 가속화.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">🔄 찰리 멍거 (역발상 반증 관점)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>판정: 최상위 양면 네트워크 해자.</strong> 반증 극복: 로보택시 회사는 높은 가동률(70%+)이 없으면 고정비로 파산함. 1억 6천만 결제 고객 풀을 가진 우버와의 제휴는 필수불가결함.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">📈 피터 린치 (성장주 관점)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>판정: 확신 매수 (PEG 0.69).</strong> 예약액이 22% 성장하는데 선행 P/E는 15.5배에 불과함. 재고 없는 독점 플랫폼 기업이 PEG 0.7 미만인 것은 일생일대의 바겐세일.
          </p>
        </div>
        <div class="metric-card">
          <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 6px;">⚡ 스탠리 드러켄밀러 (매크로 비대칭성)</div>
          <p style="font-size: 14px; color: #334155; line-height: 1.6;">
            <strong>판정: 4.2 : 1 비대칭 롱 포지션.</strong> 운전기사 정산금(~70%)이 제거되면 영업이익률이 13%에서 25% 이상으로 도약함. 로보택시 확산은 최대의 마진 확장 촉매제임.
          </p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: PEER BENCHMARKING -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">⚔️ 동종 플랫폼 및 빅테크 밸류에이션 비교</div>
        <div class="sec-tag">수익성 & 멀티플</div>
      </div>

      <table class="table-custom">
        <thead>
          <tr>
            <th>기업명</th>
            <th>시가총액</th>
            <th>선행 P/E</th>
            <th>EV / EBITDA</th>
            <th>영업이익률</th>
            <th>ROE (%)</th>
            <th>베타</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: #f0fdf4; font-weight: 700;">
            <td>우버 (UBER)</td>
            <td>$1,398억 달러</td>
            <td>15.5배</td>
            <td>20.3배</td>
            <td>13.3%</td>
            <td>37.2%</td>
            <td>1.26</td>
          </tr>
          <tr>
            <td>도어대시 (DASH)</td>
            <td>$829억 달러</td>
            <td>23.2배</td>
            <td>57.0배</td>
            <td>3.9%</td>
            <td>8.9%</td>
            <td>1.89</td>
          </tr>
          <tr>
            <td>리프트 (LYFT)</td>
            <td>$59억 달러</td>
            <td>7.2배</td>
            <td>117.3배</td>
            <td>2.6%</td>
            <td>152.6%</td>
            <td>1.96</td>
          </tr>
          <tr>
            <td>알파벳 (GOOG)</td>
            <td>$42,483억 달러</td>
            <td>22.9배</td>
            <td>23.7배</td>
            <td>34.0%</td>
            <td>48.7%</td>
            <td>1.21</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- SECTION 4: PORTFOLIO ALLOCATION & INITIATION -->
    <div class="section-card">
      <div class="sec-head">
        <div class="sec-title">🎯 포트폴리오 자산배분 실행안 (`my-portfolio.yaml`)</div>
        <div class="sec-tag">반도체 편중 해소</div>
      </div>

      <div class="grid-3">
        <div class="metric-card">
          <div class="m-label">1차 즉시 매수 (시장가)</div>
          <div class="m-val">$30,000 달러</div>
          <div class="m-desc">약 438주 @ $68.45 달러</div>
        </div>
        <div class="metric-card">
          <div class="m-label">2차 눌림목 매수 (지정가)</div>
          <div class="m-val">$30,000 달러</div>
          <div class="m-desc">약 454주 @ $66.00 달러</div>
        </div>
        <div class="metric-card">
          <div class="m-label">철통 손절선 (Disaster Floor)</div>
          <div class="m-val" style="color: #dc2626;">$62.50 달러</div>
          <div class="m-desc">-8.7% 하향 이탈 시 전량 손절</div>
        </div>
      </div>

      <div class="warn-box">
        <p><strong>전량 청산 및 투자 철회 원칙:</strong> 웨이모/크루즈가 우버 제휴를 파기하여 모빌리티 예약액이 2분기 연속 전년 대비 역성장하거나, 기그 노동자 전원 정규직화로 영업이익률이 5% 미만으로 추락할 경우 100% 전량 매도합니다.</p>
      </div>
    </div>
  </div>

  <!-- INFOGRAPHIC FOOTER -->
  <div class="info-footer">
    <div>맞춤형 리포트 수신: BM사장님 | DADAIC Investment Firm</div>
    <div>통화 기준: 전액 순수 미국 달러 ($) 표기 | 원화 환산 일체 배제</div>
  </div>
</div>

</body>
</html>
"""

def compile_media():
    print("[*] Generating HTML Deliverables for UBER...")
    
    # Paths
    s_en_html = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Slide-EN-261007.html")
    s_en_pdf = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Slide-EN-261007.pdf")
    
    s_kr_html = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Slide-KR-261007.html")
    s_kr_pdf = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Slide-KR-261007.pdf")
    
    i_en_html = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Infographic-EN-261007.html")
    i_en_png = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Infographic-EN-261007.png")
    
    i_kr_html = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Infographic-KR-261007.html")
    i_kr_png = os.path.join(MEDIA_DIR, "UBER-Investment-Committee-Decision-Memo-Infographic-KR-261007.png")
    
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
    cmd_i_en = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,3400", f"--screenshot={i_en_png}", i_en_html]
    print("  -> Rendering Infographic EN PNG...")
    subprocess.run(cmd_i_en, check=True)

    # 4. Infographic KR PNG
    cmd_i_kr = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,3400", f"--screenshot={i_kr_png}", i_kr_html]
    print("  -> Rendering Infographic KR PNG...")
    subprocess.run(cmd_i_kr, check=True)

    print("[+] All 8 UBER media deliverables generated successfully!")

if __name__ == "__main__":
    compile_media()
