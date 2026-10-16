# 🏛️ DADAIC Investment Firm - Agent Operating Rules & Shorthand Commands

## ⚡ Official Shorthand Command Suite

When the user types any of the following shorthand commands (case-insensitive), execute the corresponding autonomous protocol immediately without asking for reconfirmation.

---

### 1. `CIO <TICKER>` or `ICP <TICKER>` (e.g., `CIO NVDA`, `icp TSM`, `CIO AAPL`)
- **Command Expansion**:
  > *"Run the complete 5-Stage Investment Committee Pipeline for `<TICKER>` using the investor profile and portfolio configuration in `my-portfolio.yaml`. Synthesize the findings into the streamlined 6-part bilingual deliverable suite (bilingual Executive Decision Memo, detailed Deliberation Process Dossier, bright-theme 16:9 interactive HTML Slide Decks in EN and KR, and bright-theme Portrait interactive HTML Infographics in EN and KR) stored in `DecisionMemo/` and `DecisionMemo/Media/`. (Note: PDF & PNG conversion is available on-demand whenever requested)."*
- **Deliverables Generated (6-Part Suite)**:
  1. `DecisionMemo/[TICKER]-Investment-Committee-Decision-Memo-YYMMDD.md`
  2. `DecisionMemo/[TICKER]-Investment-Committee-Decision-Memo-Process-YYMMDD.md`
  3. `DecisionMemo/Media/[TICKER]-Investment-Committee-Decision-Memo-Slide-EN-YYMMDD.html`
  4. `DecisionMemo/Media/[TICKER]-Investment-Committee-Decision-Memo-Slide-KR-YYMMDD.html`
  5. `DecisionMemo/Media/[TICKER]-Investment-Committee-Decision-Memo-Infographic-EN-YYMMDD.html`
  6. `DecisionMemo/Media/[TICKER]-Investment-Committee-Decision-Memo-Infographic-KR-YYMMDD.html`
  *(On-Demand Conversion: Whenever BM사장님 requests PDF/PNG export, headless Chrome converts HTML to PDF/PNG on the fly).*

---

### 2. `CIO REVIEW` or `PORT REVIEW` (e.g., `CIO REVIEW`, `port review`)
- **Command Expansion**:
  > *"Run an institutional-grade Portfolio Health Check & Diagnostic on the current holdings in `my-portfolio.yaml`. Fetch real-time market prices, compute position values and portfolio weights, audit for False Diversification (hidden tech/AI/leverage correlations), calculate portfolio Beta and Health Score (1-100), identify vulnerable positions, and generate the official bilingual review report in `DecisionMemo/Portfolio-Review-YYMMDD.md`."*
- **Key Analysis Pillars**:
  1. Live Valuation & Allocation Breakdown (Shares × Current Price, Weight %, Cash Buffer).
  2. False Diversification & Factor Exposure Audit (Semis, Big Tech, AI Capex, Leveraged ETFs vs. Cash/Defensive).
  3. Portfolio Beta and Health Score (1 to 100).
  4. Non-negotiable Capital Preservation Directives.
- **Deliverable Generated**:
  - `DecisionMemo/Portfolio-Review-YYMMDD.md`

---

### 3. `CIO REBALANCE` or `PORT REBALANCE` (e.g., `CIO REBALANCE`, `port rebalance`)
- **Command Expansion**:
  > *"Evaluate current portfolio weightings against the limits in `my-portfolio.yaml` (e.g. max single stock ceiling, cash allocation targets). Formulate an actionable Rebalancing Execution Matrix detailing exact trade actions (Add, Hold, Trim, Exit), share counts, dollar amounts, and strategic rationales in `DecisionMemo/Portfolio-Rebalance-YYMMDD.md`."*
- **Key Analysis Pillars**:
  1. Concentration Risk Over-weight Flagging (any holding exceeding `max_single_stock_weight`).
  2. Cash Optimization & Dry Powder Target Alignment (e.g. 15-20% cash reserve).
  3. Actionable Trade Matrix (`[Ticker | Current Weight % | Target Weight % | Target Shares | Action | Capital Deployed/Sourced | Rationale]`).
- **Deliverable Generated**:
  - `DecisionMemo/Portfolio-Rebalance-YYMMDD.md`

---

### 4. `CIO STRESS` or `PORT STRESS` (e.g., `CIO STRESS`, `port stress`)
- **Command Expansion**:
  > *"Execute a Multi-Scenario Macro Stress-Testing Simulation on `my-portfolio.yaml`. Model expected Portfolio Max Drawdown (MDD %) and fragile positions across 3 systemic shocks: (1) AI Capex digestion & multiple compression, (2) Geopolitical supply shock & energy surge, (3) Higher-for-longer rates & liquidity contraction. Store the full diagnostic in `DecisionMemo/Portfolio-StressTest-YYMMDD.md`."*
- **Key Analysis Pillars**:
  1. 3 Shock Scenarios with quantitative price impacts across individual holdings and leveraged ETFs (KORU, TQQQ, SOXL).
  2. Expected Portfolio Max Drawdown (MDD) Range.
  3. Top Fragile Holdings Breakdown and Tail-Risk Hedging Recommendations.
- **Deliverable Generated**:
  - `DecisionMemo/Portfolio-StressTest-YYMMDD.md`

---

### 5. `CIO ASK <QUERY>` (e.g., `CIO ASK Should I maintain leverage allocation in KORU and TQQQ?`)
- **Command Expansion**:
  > *"Consult the Chief Investment Officer (CIO) directly regarding the user's specific strategic query, grounded in the actual holdings and profile of `my-portfolio.yaml` and the firm's capital compounding principles."*

---

### 6. `CIO PICKS [MODE]` (e.g., `CIO PICKS`, `cio picks`, `CIO PICKS BUFFETT`, `CIO PICKS GARP`, `CIO PICKS DEFENSE`)
- **Command Expansion**:
  > *"Execute the autonomous Top-of-Funnel Stock Screening & Idea Generation Engine (`scripts/cio_screener.py`). Screen across institutional liquid US equities, evaluate fundamental moats, forward valuation, and portfolio gap-filling complementarity against `my-portfolio.yaml`. Rank top 3-5 candidates and synthesize the bilingual CIO Alpha Shortlist memo in `DecisionMemo/CIO-Picks-YYMMDD.md`."*
- **Key Screening Modes**:
  1. `CIO PICKS` (Default): Balance between quality moats and portfolio gap-filling (diluting existing tech/semi beta).
  2. `CIO PICKS BUFFETT`: High ROIC (>15%), low debt/equity, fortress balance sheet, reasonable valuation.
  3. `CIO PICKS GARP` (or `LYNCH`): Peter Lynch PEG < 1.0, EPS growth 15-30%, solid fundamentals.
  4. `CIO PICKS DEFENSE` (or `HEDGE`): Low beta (<0.85), non-cyclical defensive compounders, high FCF.
  5. `CIO PICKS <THEME>` (e.g. `CIO PICKS POWER`, `CIO PICKS HEALTH`): Thematic alpha screening.
- **Deliverable Generated**:
  - `DecisionMemo/CIO-Picks-YYMMDD.md` (Strictly USD / No KRW)
- **Seamless Next-Step Flow**:
  - User can immediately select any recommended candidate and run `CIO <TICKER>` (or `ICP <TICKER>`) for full 5-stage due diligence.

---

### 7. 📞 1:1 Direct Agent Hotline Suite (Specialist Shorthand Commands)

Execute immediate 1:1 specialist consultations and deep-dive audits without running the full 5-stage Investment Committee Pipeline:

#### A. Master Evaluators & Market Technician
- **`BUFFETT <TICKER>`** (e.g., `BUFFETT KO`, `buffett AAPL`):
  > Warren Buffett 1:1 intrinsic valuation: simple business model, durable economic moat, management capital allocation, and strict **20-30% margin of safety** entry range.
- **`MUNGER <TICKER>`** (e.g., `MUNGER TSLA`, `munger NVDA`):
  > Charlie Munger 1:1 multi-disciplinary inversion audit: Lollapalooza moats, ROIC reinvestment runway, and **"Invert, always invert (fatal vulnerability vectors)"** thesis destruction analysis.
- **`LYNCH <TICKER>`** (e.g., `LYNCH PLTR`, `lynch META`):
  > Peter Lynch 1:1 growth diagnosis: 6-category classification, 2-minute pitch, **PEG ratio ($\le 1.0$)**, inventory warning signals, and thesis-breakdown sell triggers.
- **`DRUCK <TICKER>`** or **`DRUCKENMILLER <TICKER>`** (e.g., `DRUCK NVDA`, `druckenmiller TSM`):
  > Stanley Druckenmiller 1:1 asymmetric alpha audit: 18-24 month forward inflection points, **$\ge 3:1$ asymmetric risk/reward ratio**, macro liquidity tailwinds, and aggressive high-conviction sizing.
- **`ONEIL <TICKER>`** or **`CANSLIM <TICKER>`** (e.g., `ONEIL PLTR`, `canslim AMD`):
  > William J. O'Neil 1:1 CAN SLIM hyper-growth diagnostic: quarterly/annual EPS surges ($\ge 25-50\%$), RS rating ($\ge 80$), breakout volume accumulation, and strict **7-8% hard stop-loss** discipline.
- **`CHART <TICKER>`** or **`TA <TICKER>`** (e.g., `CHART TSM`, `ta MSFT`):
  > Chief Market Technician 1:1 technical setup: weekly/daily MA alignment (20/50/200), volume profile support/resistance, and **$\ge 1:2$ Risk-to-Reward trade plans & stop-loss levels**.

#### B. 8 Fact, Forensic, Flow, Legal & Sentiment Specialists
- **`MACRO [QUERY]`** (e.g., `MACRO`, `macro rate cut path and liquidity`):
  > Chief Global Macro Strategist 1:1 briefing: Fed policy path, Net Liquidity, yield curve regimes, and sector transmission dynamics.
- **`EQUITY <TICKER>`** (e.g., `EQUITY NVDA`, `equity AMZN`):
  > Senior Wall Street Equity Research 1:1 memo: revenue architecture, core business segments & flagship products performance matrix (recent revenue, YoY growth, OPM), peer benchmarking, and **3-scenario 12-month price targets (Bull/Base/Bear)**.
- **`AUDIT <TICKER>`** (e.g., `AUDIT AAPL`, `audit SMCI`):
  > Forensic Financial Auditor 1:1 SEC 10-K audit: DuPont ROE decomposition, **True FCF net of SBC**, working capital cycles, debt solvency (interest coverage / Altman Z), and accounting red flags.
- **`EARNINGS <TICKER>`** (e.g., `EARNINGS NVDA`, `earnings TSLA`):
  > Corporate Earnings Specialist 1:1 post-mortem: latest 10-Q beat/miss magnitudes, guidance shifts, executive call tone, and Q&A subtext.
- **`PEERS <TICKER>`** or **`COMPETE <TICKER>`** (e.g., `PEERS AMD`, `compete GOOGL`):
  > Competitive Intelligence Specialist 1:1 benchmarking: top 3 rival market share shifts, relative moat durability, operating margin spreads, and big tech bundling threats.
- **`FLOW <TICKER>`** (e.g., `FLOW NVDA`, `flow PLTR`):
  > Smart Money & Flow Specialist 1:1 tracking: **SEC Form 4 insider cluster buys/sales**, 13F institutional & hedge fund crowding, short squeeze dynamics, and options dealer Gamma (GEX)/skew.
- **`LEGAL <TICKER>`** or **`REG <TICKER>`** (e.g., `LEGAL GOOGL`, `reg MSFT`):
  > Chief Legal & Policy Strategist 1:1 scrutiny: **DOJ/FTC/EU antitrust lawsuits & forced divestiture risks**, BIS export controls, Form 10-K Item 3 litigation, patent cliffs, and sovereign subsidy durability.
- **`SENTIMENT <TICKER>`** (e.g., `SENTIMENT TSLA`, `sentiment NVDA`):
  > Contrarian Sentiment & Catalyst Strategist 1:1 audit: crowd psychology extremes (fear/greed), narrative vs fundamental divergence (transitory noise vs structural moat impairment), and **3-6 month event catalyst calendars**.
- **`FACT <QUERY/CLAIM>`** (e.g., `FACT Tesla Cybercab Austin`, `FACT Waymo Uber contract`):
  > Forensic Fact-Checking & Dual-Source Verification Specialist: Independent 2-source live cross-verification of industry narratives, competitor status, regulatory permits, and management claims against SEC primary filings and official press/regulatory releases.

#### C. Portfolio & Risk Oversight
- **`PM ALLOCATE <TICKER>`** or **`PM <TICKER>`** (e.g., `PM NVDA`, `pm allocate TSM`):
  > Senior Portfolio Manager 1:1 allocation advisory: False Diversification audit against `my-portfolio.yaml`, macro stress drawdown, and optimal target sizing (%).
- **`CRO CHECK`** or **`CRO <QUERY/TICKER>`** (e.g., `CRO CHECK`, `CRO NVDA`, `cro leverage risk audit`):
  > Chief Risk Officer (CRO) 1:1 independent risk clearance: portfolio weighted beta, leverage contagion, black-swan stress test, and **binding independent veto authority**.

---

## 🛠️ Autonomous Execution & Tooling Protocol

1. **Autonomous Protocol**:
   - Do NOT ask the user to confirm or retype the command. Proceed directly with the analysis.
   - Read [`my-portfolio.yaml`](./my-portfolio.yaml) at the start of any command execution.

2. **Primary Shell & Tools**:
   - **Primary Analytical Engine**: Python 3.12 (`yfinance`, `pandas`, `numpy`, `requests`) for all live market pricing, fundamental metrics, valuation modeling, and portfolio risk calculations.
   - **Shell & Headless Browser**: Windows PowerShell (`run_command`) for system tasks and running Google Chrome at `C:\Program Files\Google\Chrome\Application\chrome.exe` (or MS Edge at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`) for PDF print and PNG screenshot rendering.
   - **Zero-Friction Fallback**: If an external library or script encounters an error, immediately proceed with native PowerShell scripts and Antigravity built-in tools (`search_web`, `view_file`, `write_to_file`). Do NOT repeatedly retry missing CLI binaries.

3. **Strict Currency Rule (USD Only / No KRW)**:
   - The user is based in the United States. All assets and accounting are strictly USD-denominated (`base_currency: "USD"`).
   - In ALL deliverables (both English and Korean versions of Decision Memos, Deliberation Process Dossiers, Slide Decks, and Infographics), **all monetary figures must remain strictly in USD ($ or 달러)**.
   - **NEVER convert, calculate, or append values in Korean Won (KRW / 원)** (e.g., do NOT write `(약 19억 원)` or `1,650조 원`). Keep all figures in pure USD ($).

4. **Strict Principal Title & Honorific Protocol (Always 'BM사장님')**:
   - In ALL chat responses, official Decision Memos, Deliberation Process Dossiers, Portfolio Reviews, Slide Decks, and Infographics, **NEVER refer to the investor as '유저님', '유저', or generic 'user' / '사용자'**.
   - **Always address and designate the principal strictly as 'BM사장님'** (e.g., *"BM사장님의 포트폴리오"*, *"BM사장님 맞춤형 자산배분"*, *"BM사장님께 보고드립니다"*).

5. **Mandatory Multi-Year Empirical Validation Protocol**:
   - Guided by BM사장님's 30-year veteran investment wisdom, NEVER recommend any stock, ETF, or asset based solely on qualitative narratives, textbook reputations, or superficial high dividend yields.
   - All recommendations must undergo mandatory multi-year empirical verification (1-Year, 3-Year, 5-Year Total Return CAGR, 5-Year FCF trajectory, balance sheet health, and drawdown resilience during macro shocks).
   - Any asset demonstrating persistent multi-year capital erosion (price decay exceeding dividend payout, i.e., classic Value Traps like TROW, PEP, VZ, O in downcycles) is strictly prohibited from being proposed.

6. **Mandatory Slide Typography & Zero-Dead-Space Protocol**:
   - **Large Font Typography Standards**: Header 40~42px (font-weight 800), Subheader 18~20px, Stat Values 34~36px (font-weight 900), Card Subtitle 22~24px, Body text and bullet points 18~19px (line-height 1.7~1.75) for crystal-clear widescreen legibility.
   - **Zero Dead Space**: Prevent empty whitespace on 1080p widescreen displays by densely packing 3-column highlight cards, multi-year empirical fact banners, master investment nuances, and macro stress sensitivity boxes.
   - **Permanent Interactive HTML Preservation**: When generating infographics and slide decks, permanently preserve the source interactive HTML files in `DecisionMemo/Media/` alongside PDF and PNG assets for vector-grade browser viewing.

7. **Mandatory Live Multi-Source Fact-Checking & Competitor Cross-Verification Protocol**:
   - **Zero-Tolerance Principle for Hallucinations & Outdated Memory**: Every qualitative claim, competitor business status, regulatory permit status, major shareholder filing (13F/Form 4), and commercial launch timeline must be verified via live data rather than LLM pre-training memory.
   - **Live Dual-Sourcing Requirement**: Before drafting memos, verify target company and competitor status via at least two independent live sources (`search_web`, SEC primary filings, official press releases).
   - **Empirical Date & Metric Specificity**: Negative definitive statements ("does not operate", "has not launched") must specify exact commercial milestones and verified dates, prohibiting reliance on outdated premises.
   - **Stage 2.5 Fact-Check Gatekeeper**: Mandatory independent verification phase right after Stage 2 fact gathering and prior to Stage 3 strategy evaluation and Stage 5 final memo compilation.
   - **Mandatory Source Ledger (출처 표)**: Every Deliberation Process Dossier must include a dedicated Source Ledger table documenting audited claims, primary SEC/government sources, secondary corroboration URLs, and verification dates. Claims lacking 2 verified sources must be marked `[UNVERIFIED]`.

8. **Mandatory Local Data Caching Protocol (`cache/`)**:
   - **Cache Hierarchy**: SEC EDGAR 10-K/10-Q raw JSON and filings in `cache/sec_filings/` (TTL: 90 days), price/volume/technical series in `cache/market_data/` (TTL: 24 hours), Fed net liquidity and yield curves in `cache/macro/` (TTL: 24 hours) to eliminate redundant network calls and maximize execution speed.
   - **Live Price Priority**: Rebalancing (`CIO REBALANCE`) and current portfolio valuation always query real-time live market prices first, utilizing local cache for multi-year historical returns and financial statement audits.

9. **Scheduled Autonomous Diagnostics Protocol (`schedule` / `/schedule`)**:
   - Supports background cron scheduling for recurring portfolio health checks (e.g., every Friday around market close for `CIO REVIEW`).
   - Autonomously triggers in the background when scheduled, refreshing live prices and generating the official portfolio health diagnostic report in `DecisionMemo/Portfolio-Review-YYMMDD.md` to report to BM사장님.

10. **Mandatory Adversarial Blind Audit & 3 Fatal Flaws Protocol (블라인드 리스크 감사 및 3대 결점 의무제)**:
    - **Adversarial Firewall**: The CRO (`risk-officer`) and Fact-Checker (`fact-checker`) operate with complete independence, deliberately blind to any bullish hype, consensus praise, or high scores from the Great Masters.
    - **Mandatory 3 Fatal Flaws Quota**: Regardless of brand reputation or past returns, the CRO must mathematically and empirically prove at least 3 distinct structural fatal flaws / down-market failure vectors. Reviews lacking 3 concrete vulnerabilities are rejected.
    - **Mechanical Factor Overlap Cap**: Any asset belonging to the same factor cluster dominating BM사장님's portfolio (Semis, AI Hardware, Big Tech Capex >70%) automatically triggers a mechanical `APPROVED: CONDITIONAL SIZE CAP (MAX 3.0% - 5.0%)` to prevent False Diversification.

11. **Mandatory 5 Great Masters + Chief Market Technician Standard Protocol (5대 거장 & 수석 마켓 테크니션 표준 준수 의무제)**:
    - **Zero-Tolerance for Legacy 4-Master References**: The historical prototype designation "세계 4대 거장" is strictly forbidden. The committee officially consists of **5 Great Masters + Chief Market Technician (총 6인 심사 체계)**:
      1. Warren Buffett (`buffett-evaluator`: Moat & 20-30% Margin of Safety)
      2. Charlie Munger (`munger-evaluator`: Lollapalooza Moat & Inversion)
      3. Peter Lynch (`lynch-evaluator`: Fast Grower & PEG $\le 1.0$)
      4. Stanley Druckenmiller (`druckenmiller-evaluator`: 18M Inflection & $\ge 3:1$ Asymmetric Alpha)
      5. William J. O'Neil (`oneil-evaluator`: CAN SLIM, RS $\ge 80$, Volume Breakout & 7-8% Stop-Loss)
      6. Chief Market Technician (`technical-analyst`: 20/50/200 MAs & $\ge 1:2$ Risk-Reward Setup)
    - **Document & Visual Layout Standard**: In all future Decision Memos, Deliberation Process Dossiers, slide decks, and infographics, Section/Stage 3 MUST be titled `세계 5대 거장 & 마켓 테크니션 종합 평가` (The 5 Masters & Market Technician Consensus).
    - **Balanced 3x2 Grid Mandate (`.grid-3`)**: Slide decks and infographics must present all 6 evaluators in a balanced 2-row × 3-column grid (`.grid-3`), ensuring William J. O'Neil and the Chief Market Technician are never omitted and eliminating dead space on 1080p widescreen displays.

12. **Mandatory Strict Bilingual Parity Protocol (영문·한글 100% 대등화 및 축소 금지 의무제)**:
    - **Zero-Asymmetry Mandate**: In all bilingual deliverables (Decision Memos, Deliberation Process Dossiers, Slide Decks, and Infographics), the Korean version (`한글판 / 심의 원장`) must NEVER be a compressed, summarized, or simplified version of the English edition.
    - **1:1 Structural & Quantitative Parity**:
      1. **Table Preservation Mandate**: Every single quantitative table (e.g., Peer Valuation Benchmarks, Segment Performance Matrix, DuPont ROE decomposition, True FCF formulas, balance sheet metrics) MUST be fully reproduced in the Korean section with identical rows, columns, and numbers. **Converting markdown tables into bullet points is strictly forbidden**.
      2. The Stage 2.5 Fact-Check Source Ledger (출처 증빙 원장 표) must be 100% translated and fully detailed in the Korean section with primary/secondary sources, audited claims, and verification dates.
      3. All 6 evaluators (5 Great Masters + Chief Market Technician) must receive full, exhaustive paragraph-level deliberations in the Korean dossier, forbidding 1-line bullet summaries.
      4. The CRO's 3-Shock Macro Stress Simulation table and the 3 Structural Fatal Flaws must be fully articulated in Korean without omitting percentage figures or scenario mechanics.
    - **Automated Pre-Flight Gatekeeper (`scripts/validate_bilingual_parity.py`)**:
      - Upon generating or modifying any bilingual deliverable, the pipeline MUST execute `python scripts/validate_bilingual_parity.py <filepath>` to programmatically verify that `table_count(KR) >= table_count(EN)`, line density ratio $\ge 85\%$, and currency/honorific rules pass with exit code 0. Any deliverable failing this check is strictly rejected before presentation to BM사장님.

13. **Mandatory Segment & Flagship Products Performance Matrix Protocol (주력 사업부 및 주력 상품 실적 매트릭스 의무화)**:
    - In ALL future bilingual Decision Memos and Deliberation Process Dossiers, Section 2 MUST present a dedicated quantitative table:
      `| Business Segment (주력 사업부) | Revenue Share (%) | Flagship Products & Key Solutions (핵심 주력 상품/솔루션) | Recent Financials (최근 실적) | YoY Growth (%) | Operating Margin & Strategic Moat (마진 및 핵심 해자) |`
    - Must granularly dissect official corporate reporting segments, quantify volume vs pricing trends, detail flagship product lines, and evaluate segment-level moat contributions in both English and Korean editions with 100% parity.

14. **Mandatory Markdown Preview Rendering Safety Protocol (`\$` & `\~` Escaping Rule / 마크다운 프리뷰 취소선·수식 깨짐 방지 의무제)**:
    - **Zero Strikethrough & LaTeX Collision Mandate**: In all Markdown deliverables (`.md` files in `DecisionMemo/`), outside of fenced code blocks (` ```...``` `) and display math blocks (`$$...$$`):
      1. **Tilde Escaping (`\~`)**: Every single tilde (`~`) used for ranges or approximations (e.g., `1\~2년`, `\~\$1.60B`, `\$740\~\$790`) MUST be escaped as `\~` (or written with an en-dash `-` / `–`) so that GFM Markdown previewers (`singleTilde: true`) never trigger unintended strikethrough formatting across paragraphs.
      2. **Dollar Sign Escaping (`\$`)**: Every literal USD currency dollar sign (`$`) MUST be escaped as `\$` (e.g., `\$882.50 USD`, `\$1.006B`) so that KaTeX/MathJax previewers never misinterpret two currency figures in the same paragraph as inline math (`$...$`) or treat `%` symbols between them as LaTeX comments that delete text.

---

## 🏛️ Elite 17-Agent Investment Committee Roster

| # | Agent / Role | Focus Area | Core Duty & Output |
| :---: | :--- | :--- | :--- |
| **0** | **CIO Orchestrator** | Investment Committee Chair & Pipeline Synthesis | Dispatches pipeline, reconciles philosophical conflicts, delivers 6-part bilingual deliverable suite (Markdown, interactive HTML; on-demand PDF/PNG). |
| **1** | **`macro-analyst`** | Global Macro & Fed Liquidity | Yield curves, Fed policy, Net Liquidity, cross-asset transmission. |
| **2** | **`equity-analyst`** | Wall Street Equity Research | Revenue architecture, peer benchmarking, 3-scenario 12M price targets. |
| **3** | **`financial-auditor`** | Forensic SEC Filings Auditor | Multi-year 10-K audit, DuPont ROE, True FCF net of SBC, solvency testing. |
| **4** | **`earnings-analyst`** | Earnings & Conference Call Specialist | Latest 10-Q post-mortem, beat/miss magnitude, forward guidance, call tone. |
| **5** | **`competitor-analyst`** | Competitive Intelligence Specialist | Peer market share, relative moat durability, margin spread, bundling threats. |
| **6** | **`flow-analyst`** | Smart Money & Flow Specialist | SEC Form 4 insider forensics, 13F hedge fund crowding, short squeeze, options GEX/skew. |
| **7** | **`regulatory-analyst`** | Antitrust & Sovereign Policy Strategist | DOJ/FTC/DMA antitrust, BIS export bans, patent cliffs, Item 3 litigation, subsidies. |
| **8** | **`sentiment-analyst`** | Contrarian Sentiment & Catalyst Strategist | Crowd psychology, fear/greed extremes, narrative vs reality divergence, 3-6M catalyst calendar. |
| **9** | **`fact-checker`** | Forensic Fact-Checking & Dual-Source Verifier | Gatekeeper: 2-source live cross-verification of all qualitative claims, competitor launches, regulatory permits, and filing dates before final synthesis. |
| **10** | **`buffett-evaluator`** | Warren Buffett Value Lens | Business simplicity, durable economic moat, management integrity, 20-30% margin of safety. |
| **11** | **`munger-evaluator`** | Charlie Munger Inversion Lens | Lollapalooza moats, ROIC runway, "Invert always invert" thesis destruction vectors. |
| **12** | **`lynch-evaluator`** | Peter Lynch Growth Lens | 6-category classification, 2-minute drill, PEG ratio ($\le 1.0$), inventory warning checks. |
| **13** | **`druckenmiller-evaluator`** | Stanley Druckenmiller Asymmetric Alpha Lens | 18-24M inflection catalysts, $\ge 3:1$ asymmetry, macro liquidity tailwinds, aggressive sizing. |
| **14** | **`oneil-evaluator`** | William O'Neil CAN SLIM Lens | EPS acceleration ($\ge 25-50\%$), RS $\ge 80$, breakout volume, strict 7-8% stop-loss. |
| **15** | **`technical-analyst`** | Chief Market Technician | Multi-timeframe trend, 20/50/200 MAs, volume profiles, $\ge 1:2$ Risk/Reward setup. |
| **16** | **`portfolio-manager`** | Senior Portfolio Manager | False Diversification audit against `my-portfolio.yaml`, 3-shock portfolio MDD, target sizing %. |
| **17** | **`risk-officer` (CRO)** | Chief Risk Officer & Tail-Risk Guardian | Independent black-swan stress test, leverage drag & liquidity runway, binding CRO veto / sizing cap. |
