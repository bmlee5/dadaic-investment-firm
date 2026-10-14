# 🏛️ DADAIC INVESTMENT COMMITTEE: DELIBERATION PROCESS DOSSIER — NFLX
> **Document Control Number**: DADAIC-IC-PROC-NFLX-261007  
> **Target Asset**: NFLX | Netflix, Inc. (NASDAQ) | **Meeting Date**: 2026-10-07 | **Principal**: BM사장님  
> **Companion Memo**: [NFLX-Investment-Committee-Decision-Memo-261007.md](./NFLX-Investment-Committee-Decision-Memo-261007.md)  
> **Data Engines**: [`scripts/nflx_data.py`](../scripts/nflx_data.py) (yfinance live pull) · [`scripts/nflx_quant.py`](../scripts/nflx_quant.py) (normalization, DCF, scenarios, portfolio stress)  
> *Bilingual: each stage gives the English record first, followed by the Korean summary (한국어 요약).*

---

## 📋 Pipeline Audit Trail / 파이프라인 진행 기록

| Stage | Unit(s) | Status | Key Output |
| :--- | :--- | :--- | :--- |
| 1 | CIO Classification | ✅ | Branch B — Tech Platform / Consumer Subscription |
| 2 | 8 Fact & Forensic Specialists | ✅ | Live data + 10-K/10-Q figures + 25 web sources |
| **2.5** | **Fact-Checker Gatekeeper** | ✅ | **18 claims verified, 1 claim REJECTED, 2 flagged single-source** |
| 3 | 5 Masters + Technician | ✅ | 2 Hold/Fair, 1 Watch, 1 Laggard, 1 Support-buy, 1 Compounder |
| 4 | PM + CRO | ✅ | Target 2.75%, CRO cap 3.0%, funded by semis trim |
| 5 | CIO Synthesis | ✅ | HOLD CORE + CONDITIONAL ACCUMULATE |

---

## STAGE 1 — Classification & Sector Routing / 분류 및 라우팅

**Classification: Branch B — Tech Platforms & Growth Equities.** Netflix is a capital-light, global subscription + advertising video platform. Analytical focus: engagement/attention share, pricing power, ARM growth, content amortization vs. cash spend (~$20B cash content in 2026), SBC dilution, True FCF, and platform-moat durability versus YouTube and consolidated legacy media (Skydance Corp.).

- **Position status**: **Existing holding** — 340 shares in `my-portfolio.yaml`. The mandate is therefore **Hold / Add / Trim / Exit**, not initiation.
- **Corporate action**: A 10-for-1 split (November 2025) is fully reflected in all per-share figures in this dossier.

> **한국어 요약**: 넷플릭스는 분과 B(테크 플랫폼 성장주)로 분류합니다. 기존 보유 종목(340주)이므로 신규 편입이 아닌 **보유/추가/축소/청산** 판단이 과제입니다. 모든 주당 수치는 2025년 11월 10:1 액면분할을 반영했습니다.

---

## STAGE 2 — Fact Gathering & Forensic Investigation / 팩트 수집 및 포렌식 조사

### 2.1 `macro-analyst` — Global Macro & Liquidity
- **Fed**: The FOMC **hiked 25bp to 3.75–4.00%** on Sept 15–16, 2026 (unanimous 12–0). Minutes released Oct 7 show officials divided, with "many" open to another hike by year-end.
- **Rates**: The 10Y UST trades at **~5.27–5.30%**, a hostile regime for long-duration equity multiples. The CIO raised the DCF cost of equity to **9.5%** accordingly.
- **Transmission to NFLX**: Subscription revenue is non-cyclical (low price point; ad tier from $8.99), but valuation is rate-sensitive. **Net verdict: Headwind** (valuation), **Neutral** (fundamentals).

### 2.2 `equity-analyst` — Revenue Architecture & Targets
- **Revenue**: FY22 $31.62B → FY23 $33.72B → FY24 $39.00B → FY25 $45.18B → TTM $48.37B. FY26 guide **$51.0–51.4B** (+13%); FY27 consensus $56.9B (+11.2%).
- **Engines**: (1) Price increases (March 2026 US: Ads $8.99 / Standard $19.99 / Premium $26.99); (2) **Advertising ~ $3B in 2026, roughly 2x FY25's ~$1.5B**; ad tier at 250M+ monthly active viewers (May 2026 upfront); ads drive >60% of sign-ups in ad markets; (3) Live events: NFL Thanksgiving Eve + Christmas Day doubleheader, WWE Raw, MLB events, FIFA Women's World Cup 2027/2031.
- **Street**: 45 analysts, mean target **$92.84**, median $90, high $135, low $57 (Wells Fargo). Rating skew: "Buy".
- **3-scenario 12M targets**: Bull $102.70 / Base $83.60 / Bear $55.20 (see Stage 5).

### 2.3 `financial-auditor` — Forensic 10-K / 10-Q Audit

| FY | Revenue | Op. Income | Op. Margin | Net Income | Dil. EPS | OCF | FCF | SBC | **True FCF** | Buybacks |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2022 | $31.62B | $5.63B | 17.8% | $4.49B | $0.995 | $2.03B | $1.62B | $0.58B | **$1.04B** | $0.00B |
| 2023 | $33.72B | $6.95B | 20.6% | $5.41B | $1.203 | $7.27B | $6.93B | $0.34B | **$6.59B** | $6.05B |
| 2024 | $39.00B | $10.42B | 26.7% | $8.71B | $1.983 | $7.36B | $6.92B | $0.27B | **$6.65B** | $6.26B |
| 2025 | $45.18B | $13.33B | 29.5% | $10.98B | $2.530 | $10.15B | $9.46B | $0.37B | **$9.09B** | $9.13B |
| TTM Q2'26 | $48.37B | $14.35B | 29.7% | $13.65B* | $3.18* | $11.97B* | $11.15B* | $0.49B | **$7.86B (ex-fee)** | — |

\* *Includes the **$2.8B WBD termination fee** received in Q1 2026 (booked in "interest and other income"). Normalized TTM FCF = $11.15B − $2.80B = $8.35B; less SBC $0.49B = **$7.86B**.*

- **DuPont ROE (FY25)**: Net margin 24.3% × asset turnover 0.81x × equity multiplier 2.09x ≈ **41%** (yfinance TTM ROE 49.5% is inflated by the fee).
- **Solvency**: Debt $14.46B; cash $9.03B; **net debt $5.4B ≈ 0.37x EBITDA ($14.7B)**; interest coverage 13.3/0.78 ≈ **17x**; current ratio 1.14. S&P **'A' / Stable** (July 2026); July 2026 IG notes refinanced ~$1B of 2026 maturities.
- **Dilution**: Diluted shares fell from 4.513B (FY22) to 4.344B (FY25), a 3.7% reduction. SBC is ~1% of revenue, among the lowest in mega-cap tech.
- **Red flags**: (1) Q1'26 headline EPS ($1.23) and TTM FCF are **non-recurring-inflated** (corrected above); (2) Q3'25 included a **$619M Brazil CIDE tax charge** (EPS −15.8% surprise); (3) cash content spend (~$20B) exceeds amortization in growth years, so the auditor tracks the gap between FCF and net income. FY25 FCF/NI conversion of 86% is acceptable.
- **Forensic Grade: High Quality A.**

### 2.4 `earnings-analyst` — Latest Print Post-Mortem (Q2 2026, reported Jul 16)
- Revenue **$12.56B (+13.4% YoY)**, a slight miss and the slowest growth in over a year. Operating margin **33.4%**. EPS **$0.80 vs $0.79** (+1.45% surprise).
- Guidance: FY26 revenue **narrowed to $51.0–51.4B** (from $50.7–51.7B in April); **31.5% operating margin reiterated**. Q3 guide: revenue **$12.86B (+11.7%)**, margin **33.2%**.
- Disclosure: Engagement reporting was cut to **once per year**, adding opacity on top of the 2025 end of quarterly subscriber counts.
- Reaction: **−8% on Jul 17, 2026**.
- Beat/miss history (EPS surprise): Q1'25 +16.8%, Q2'25 +2.2%, Q3'25 **−15.8%** (Brazil tax), Q4'25 +1.4%, Q1'26 −1.4% vs consensus (vs company guide: $1.23 vs $0.76 thanks to the fee), Q2'26 +1.5%.
- **Grade: In-Line, Soft Guide.** **Next print: Tuesday, Oct 20, 2026, 1:01pm PT** (consensus EPS $0.82, +40% YoY on the easy Brazil-tax comparison).

### 2.5 `competitor-analyst` — Moat & Share Benchmarking
- **Attention share (Nielsen The Gauge, July 2026)**: **YouTube 14.2% (record)** vs **Netflix 7.8%**, down from Netflix's July 2025 all-time-high share. Streaming as a category hit a record 49.0% of US TV time.
- **Engagement**: H1'26 global hours **97B+ (+2% YoY, record first half)**, but US hours were down ~8.6% YoY by third-party estimates. HSBC: English-language Top-10 hours **−17% YoY** in Jul–Aug 2026. Wells Fargo: average daily viewing per member down ~8% vs H1'23.
- **Consolidation**: **Skydance Corporation (Paramount Skydance + WBD) closed Oct 6, 2026** (~$110B EV incl. debt). It has >200M DTC subscribers, HBO Max and Paramount+ will unify over time, and David Ellison is Chairman & CEO.
- **Relative moat**: Netflix's operating margin (~30–33%) is unmatched among pure-play streamers, and its global scale (190+ countries, >1/3 of viewing is non-English) is unreplicated. **Trajectory: monetization moat stable; attention-share moat narrowing.**

### 2.6 `flow-analyst` — Smart Money & Insider Forensics
- **Form 4 (Aug–Sep 2026)**: Co-CEO Ted Sarandos sold 133,162 sh @ $72.90–73.48 (~$9.73M, Aug 4); Co-CEO Greg Peters sold 27,312 sh @ $73.54 (~$2.01M, Aug 6); CFO Spence Neumann sold 9,248 sh @ $75.79 (~$0.70M, Aug 10); Director Richard Barton made repeated option-exercise-and-sell transactions (Aug 5, Sep 8, Sep 10). **No open-market purchases.** The pattern looks like a routine plan/option program, but there is no conviction buying at 52-week lows.
- **13F (Q2 2026)**: BlackRock 8.38% (+0.7%), Vanguard 6.60% (+0.2%), State Street 4.33% (+4.9%), **FMR 3.26% (−33.6%)**, Invesco 3.25% (+3.0%), Geode 2.65% (+6.6%), Morgan Stanley 2.39% (+0.7%), **T. Rowe 2.25% (−5.5%)**, **Capital World 2.10% (−11.9%)**. Active growth managers are distributing while passive managers accumulate.
- **Short interest**: 2.28% of float, 3.4 days to cover, so there is no squeeze setup. Institutional ownership 84%.
- **Score: 42/100 — Mild Distribution.**

### 2.7 `regulatory-analyst` — Antitrust & Policy
- **WBD bid**: The DOJ review of Netflix's $82.7B WBD bid (reportedly framed under Clayton §7 *and* Sherman §2) lapsed when the deal ended in Feb 2026. The DOJ separately cleared Paramount–WBD (closed Jun 12 review; deal closed Oct 6). **No active DOJ enforcement action against Netflix was identified** (single aggregated source; treated conservatively as a "watch" item).
- **Brazil**: CIDE-Tecnologia 10% remittance tax after the STF ruling (Aug 2025). A $619M charge was booked in Q3'25; the ongoing run-rate is embedded in margins.
- **EU**: DSA compliance obligations; recurring "fair share"/content-quota debates.
- **US litigation**: Class actions alleging addictive autoplay design and minors' data collection (e.g., Ohio).
- **Verdict: Moderate Watch.**

### 2.8 `sentiment-analyst` — Contrarian Sentiment & Catalysts
- **Pessimism markers**: Wells Fargo → Underweight, PT $80 → **$57** (Sep 18); HSBC Buy → Hold, PT $96 → **$76** (Sep 22); weakest Emmy haul in a decade; Co-CEO Sarandos publicly acknowledged growth is "not as fast as desired"; stock −14% in September; Reed Hastings left the board on Jun 4, 2026 (Jay Hoag became Chair).
- **Narrative vs reality**: The narrative says "Netflix is losing the attention war." The reality is +13% revenue, record H1 global hours, expanding margins, and ~$3B ads. The divergence is meaningful but **not yet a structural moat impairment**.
- **Catalyst calendar (3–6M)**: **Oct 20** Q3 print & Q4 guide · Nov 25 NFL Thanksgiving Eve (GB vs LAR) · **Dec 25 NFL Christmas doubleheader** · Jan 2027 Q4 print + **FY27 guidance & margin target** · Skydance HBO Max/Paramount+ integration announcements.
- **Score: 70/100 — Favorable Accumulation** (pessimism high, but no capitulation volume yet: 20D/50D volume ratio 1.10).

> **한국어 요약 (2단계)**: 매크로는 금리 역풍(기준금리 3.75~4.00%, 10년물 5.3%)이나 구독 매출 자체는 비경기적입니다. FY25 진성 FCF $9.09B, 순부채 $5.4B(EBITDA 0.37배), S&P 'A' 등급으로 재무는 우량 A입니다. Q1'26 이익과 TTM FCF에는 **WBD 해지 수수료 $2.8B(수취)**가 포함되어 제거했습니다. 2분기 실적은 부합 수준이었으나 가이던스가 약해 주가가 -8% 하락했습니다. 경쟁 측면에서 유튜브 시청 점유율 14.2% vs 넷플릭스 7.8%이며, 스카이댄스(파라마운트+WBD)가 10월 6일 합병을 완료했습니다. 수급은 공동 CEO들의 매도와 액티브 펀드(FMR -33.6%)의 이탈로 42점, 센티먼트는 연속 하향과 에미상 부진으로 비관 정점에 근접해 70점입니다.

---

## STAGE 2.5 — Fact-Check Gatekeeper Ledger / 독립 팩트체크 게이트키퍼 기록

*Protocol: every qualitative claim requires ≥2 independent live sources (searched 2026-10-07). Claims that fail are removed or corrected before Stage 3.*

| # | Claim | Sources (independent) | Status |
| :---: | :--- | :--- | :---: |
| 1 | Netflix–WBD merger agreement (Dec 2025, ~$82.7B EV) terminated Feb 2026 after the WBD board deemed Paramount's all-cash bid superior | Netflix IR; Britannica; Financier Worldwide | ✅ |
| 2 | **Netflix RECEIVED a $2.8B termination fee** (paid by Paramount on WBD's behalf) | Investing.com; Moneywise; Netflix Q1'26 shareholder letter; **yfinance 10-Q: Q1'26 NI $5.28B / OCF $5.29B** | ✅ |
| 2-R | ~~"Netflix opted to pay a breakup fee"~~ (one aggregator summary) | Contradicted by #2 and by the filed financials | ❌ **REJECTED** |
| 3 | Paramount Skydance–WBD closed **Oct 6, 2026**; renamed **Skydance Corporation**; >200M DTC subs | skydance.com; CBS News; PBS; Forbes | ✅ |
| 4 | Nielsen Gauge July 2026: **YouTube 14.2% (record), Netflix 7.8%**, streaming 49.0% | nielsen.com; TheWrap; MediaPlayNews | ✅ |
| 5 | Wells Fargo → **Underweight**, PT $80 → $57 (**Sep 18, 2026**) | Quartz; Investing.com; Barchart | ✅ |
| 6 | HSBC Buy → **Hold**, PT $96 → $76 (**Sep 22, 2026**) | StreetInsider; TradingView; MarketBeat | ✅ |
| 7 | Q2'26: revenue $12.56B (+13%), OM 33.4%, EPS $0.80 vs $0.79; FY26 guide $51.0–51.4B, OM 31.5% | Netflix IR (q4cdn); TradingView; yfinance | ✅ |
| 8 | Stock −8% on Jul 17, 2026 after Q2 | Motley Fool; Zacks | ✅ |
| 9 | Q3'26 report **Oct 20, 2026**; guide rev $12.86B, OM 33.2%; consensus EPS $0.82 | Netflix IR; InsiderFinance; yfinance | ✅ |
| 10 | Q1'26: rev $12.25B (+16%), EPS $1.23 vs guide $0.76 (fee-driven); Hastings to leave board | Netflix IR; Anadolu Agency; TheDesk | ✅ |
| 11 | Reed Hastings left the board **Jun 4, 2026**; Jay Hoag became Chair | MediaPlayNews; LA Times; Fox Business | ✅ |
| 12 | $25B additional buyback (Apr 2026); ~$27.1B remaining; $4.7B repurchased H1'26 | Shacknews; TradingView; TipRanks | ✅ |
| 13 | S&P 'A' / Stable (Jul 2026); Jul 2026 IG notes issued | S&P Global; GuruFocus; Briefs | ✅ |
| 14 | FOMC +25bp to 3.75–4.00% (Sep 16, 2026); 10Y ~5.27–5.30% | federalreserve.gov; Trading Economics; Morningstar | ✅ |
| 15 | Brazil CIDE $619M charge (Q3'25) | Netflix Q3'25 letter (via aggregator); yfinance Q3'25 EPS −15.8% surprise | ✅ |
| 16 | H1'26 engagement 97B+ hrs (+2% YoY); US hours ~−8.6% (third-party estimate) | Netflix Engagement Report; analyst estimates | ⚠️ US figure = estimate |
| 17 | 2026 ads ~ $3B (~2x 2025); 250M+ ad-tier MAV (May 2026) | Netflix upfront; industry press | ✅ |
| 18 | March 2026 US price increase (Ads $8.99 / Std $19.99 / Prem $26.99) | Industry press (single aggregated summary) | ⚠️ Single-source — used qualitatively |
| 19 | Insider sales: Sarandos, Peters, Neumann, Barton (Aug–Sep 2026) | SEC Form 4 (via yfinance); — | ✅ Primary filing |
| 20 | No active DOJ enforcement vs Netflix after the WBD bid ended | One aggregated summary | ⚠️ Treated as "Moderate Watch" |

**Gatekeeper ruling**: Cleared for Stage 3, with one fabricated/erroneous narrative rejected (#2-R) and three items carried with explicit caveats.

> **한국어 요약 (2.5단계)**: 20개 주장을 2개 이상의 독립 소스로 실시간 교차 검증했습니다. 한 검색 요약의 **"넷플릭스가 위약금을 지불했다"는 서술은 오류로 판명되어 기각**했습니다. 실제로는 넷플릭스가 $2.8B을 **수취**했으며 10-Q 순이익($5.28B)으로 확인됩니다. 미국 시청시간 -8.6%(제3자 추정), 요금 인상 세부가격, DOJ 무조치 3건은 단일 소스이므로 주석을 붙여 보수적으로 반영했습니다.

---

## STAGE 3 — Masters' Strategy Evaluation / 거장 평가

### 3.1 Warren Buffett — Value & Margin of Safety → **HOLD; BUY BELOW $67**
- *Simple business?* Yes: monthly subscription plus ads for entertainment.
- *Durable moat?* Scale economics (content cost per member), a global brand, data-driven recommendations, and demonstrated pricing power through repeated price increases with no reported churn spike. Moat **intact but contested** for attention.
- *Management & capital allocation?* Generally disciplined: $9.1B of FY25 buybacks at an average price far above today's (hindsight cost). **The $82.7B WBD bid was a warning sign of "empire" impulses**, but walking away and collecting $2.8B was rational.
- *Margin of safety*: Base fair value $83.60 vs price $69.70 = **16.6%**, which falls short of 20–30%. **Buy zone: ≤ $67 (20%) / ideal $62.50 (25%).**

### 3.2 Charlie Munger — Inversion → **QUALITY COMPOUNDER, FAIR PRICE**
- Lollapalooza factors: global scale × network of local productions × ad + price levers × capital-light distribution.
- **Invert — how could NFLX fail?** (1) Attention migrates to free UGC (YouTube) and AI-generated video, and Netflix overspends to defend share (a content treadmill). (2) A consolidated Skydance (HBO + Paramount libraries) withholds licensed content and bundles aggressively. (3) Management repeats a mega-acquisition. (4) A pivot to sports rights turns Netflix into a rights-inflation victim.
- Mitigants: event-only sports strategy (no full-season packages); 'A' balance sheet; buybacks.
- **Watch metric**: US engagement and content cash-spend/revenue ratio (≤ 40%).

### 3.3 Peter Lynch — Category & PEG → **STALWART IN TRANSITION — FAIR**
- Category: **Fast Grower → Stalwart** (revenue +11–13%, EPS +20%+ from margin expansion and buybacks).
- 2-minute drill: "The world's largest paid streaming platform. It raises prices, adds an ad tier that doubles every year, and buys back stock. The stock fell 48% because people fear YouTube is stealing viewing time."
- PEG: **0.81** (consensus FY25–27 EPS CAGR 22.6%) / **1.15** (conservative 16%). Lynch rates this "fair, not a screaming bargain."
- Inventory warning: N/A (content assets). Lynch's equivalent concern is the **disclosure retreat** (no subs, annual engagement), which hides deterioration.

### 3.4 Stanley Druckenmiller — Asymmetry → **WATCH (2.3:1)**
- Bull +47.3% / Bear −20.8% → **2.3:1**, which fails the ≥3:1 bar.
- 18-month inflection candidates: ads scaling to ~$5B+ in 2027; live events lifting ad CPMs; FY27 margin target of ≥33%.
- Macro: a Fed in hiking mode with the 10Y at 5.3% is the wrong liquidity regime for aggressive sizing in long-duration growth. **No concentrated bet; staged entry only.**

### 3.5 William J. O'Neil — CAN SLIM → **LAGGARD — NO BREAKOUT BUY**
| Pillar | Reading | Pass? |
| :--- | :--- | :---: |
| C (current qtr EPS) | Q3 consensus +40% YoY (low base from the Brazil tax hit) | ⚠️ |
| A (annual EPS) | FY23–25 EPS +21% / +65% / +28% | ✅ |
| N (new product/high) | Ads/live events new; price 48% below high | ❌ |
| S (supply/demand) | Buybacks shrink float; volume 20D/50D 1.10 on declines | ⚠️ |
| L (leader) | 1Y −41.5% vs SPY +17.4% → RS very weak | ❌ |
| I (institutions) | 84% held; active managers trimming | ⚠️ |
| M (market) | Fed hiking; 10Y 5.3% | ❌ |

### 3.6 Chief Market Technician → **DOWNTREND; SUPPORT-ONLY BUY (R:R 1:3.2)**
- MA stack (bearish): $69.70 < 20D $72.24 < 50D $75.42 < 200D $83.68.
- Momentum: RSI(14) 41.0; MACD −2.39 vs signal −2.12 (bearish cross intact).
- Structure: 52W range $65.08 (2026-07-17) – $124.86 (2025-10-21); 3-month range $65.08–$83.60. A potential double bottom forms if $65 holds through earnings.
- Trade plan: entry $65–67 → stop $60.50 (risk ~$5.50) → T1 $75.40 (50D) → T2 $83.60 (200D / base fair value) → **reward/risk ≈ 3.2**.

> **한국어 요약 (3단계)**: 버핏은 안전마진 16.6%로 기준(20~30%)에 미달해 **보유, $67 이하 매수** 판정입니다. 멍거는 **우량 복리 기계이나 가격은 적정**하다고 보며, 역발상 관점에서 유튜브의 시간 잠식에 따른 콘텐츠 비용 쳇바퀴와 대형 인수 재시도를 치명 리스크로 지목했습니다. 린치는 **스톨워트 전환기**로 PEG 0.81~1.15의 적정가 판정입니다. 드러켄밀러는 비대칭 **2.3:1로 3:1에 미달**하고 금리 인상기여서 관망입니다. 오닐은 RS와 M 조건 미충족으로 **후발주자**입니다. 기술적 분석가는 역배열 하락 추세이므로 **$65~67 지지선 매수만 허용**하며 손익비는 1:3.2입니다.

---

## STAGE 4 — Portfolio Allocation & Risk Sizing / 포트폴리오 배분 및 리스크

### 4.1 `portfolio-manager` — Live Book (2026-10-07 close)

| Ticker | Price | Value | Weight |
| :--- | ---: | ---: | ---: |
| NVDA | $237.47 | $356,205 | 20.40% |
| GOOG | $347.37 | $208,422 | 11.94% |
| AMZN | $259.92 | $166,349 | 9.53% |
| SPY | $777.22 | $159,330 | 9.13% |
| AVGO | $376.51 | $131,779 | 7.55% |
| AMD | $645.86 | $116,255 | 6.66% |
| MSFT | $529.76 | $95,357 | 5.46% |
| META | $721.31 | $72,131 | 4.13% |
| QQQ | $757.73 | $68,196 | 3.91% |
| TSM | $472.20 | $56,664 | 3.25% |
| MU | $1,088.00 | $43,520 | 2.49% |
| EWY | $183.69 | $29,390 | 1.68% |
| PLTR | $194.12 | $29,118 | 1.67% |
| **NFLX** | **$69.70** | **$23,698** | **1.36%** |
| KORU | $20.05 | $23,458 | 1.34% |
| TQQQ | $83.62 | $13,797 | 0.79% |
| BE | $291.29 | $13,108 | 0.75% |
| LLY | $1,188.72 | $13,076 | 0.75% |
| GEV | $997.09 | $10,968 | 0.63% |
| SKHY | $178.25 | $7,843 | 0.45% |
| SOXL | $158.91 | $2,701 | 0.15% |
| IREN | $38.69 | $2,554 | 0.15% |
| CRWV | $88.45 | $1,946 | 0.11% |
| Cash | — | $100,000 | 5.73% |
| **Total** | | **$1,745,865** | **100%** |

- **False diversification**: Semis 40.8% + Big Tech 31.1% + AI infra (PLTR/BE/GEV/IREN/CRWV) 3.3% + leveraged ETFs 2.3% → **~77% of the book shares a single AI-capex factor**. Index ETFs (SPY/QQQ, 13.0%) add more of the same mega-cap exposure.
- **NFLX complementarity**: 2Y daily beta vs SPY **0.70**, correlation **0.33**, and no AI-capex revenue linkage. This makes NFLX a genuine diversifier, which supports raising it from 1.36% toward ~2.75%.
- **Sizing logic**: Quality A + fair valuation + negative momentum → **mid-size satellite (2.5–3.0%)**, not core (>5%).

### 4.2 3-Shock Stress Test (holding-level shocks; NFLX shock in parentheses)

| Scenario | NFLX Shock | Portfolio MDD (Current) | Portfolio MDD (Proposed) |
| :--- | :---: | :---: | :---: |
| S1 AI Capex Digestion & Multiple Compression | −12% | **−33.8%** | **−33.3%** |
| S2 Geopolitical Supply Shock & Energy Surge | −15% | **−26.3%** | **−26.1%** |
| S3 Higher-for-Longer Rates & Liquidity Contraction | −25% | **−24.9%** | **−24.8%** |

*Proposed = NFLX 340 → 690 shares (+$24,395), NVDA 1,500 → 1,400 shares (−$23,747). Cash is unchanged at ~$99.4K.*

### 4.3 `risk-officer` (CRO) — Binding Ruling
- **Portfolio beta 1.56 vs ceiling 1.20 → BREACH** (pre-existing, not caused by NFLX).
- **Cash 5.7% vs 15–20% dry-powder target → BREACH** (pre-existing).
- **S1 MDD −33.8% exceeds BM사장님's stated 20–30% tolerance.**
- NFLX itself: 2022 MDD −75.9% shows severe idiosyncratic drawdown risk on growth scares → hence the cap.
- **RULING: `APPROVED: CONDITIONAL CAP — MAX 3.0%`**, conditions: (1) fund only via semis trim (NVDA), never cash; (2) Tranche 1 only after the Oct 20 print passes the 3-point test; (3) $60.50 hard stop on added shares; (4) **separate standing directive** to cut leveraged ETFs (KORU/TQQQ/SOXL = 2.3%) and rebuild cash toward 15%.

> **한국어 요약 (4단계)**: 실시간 총자산은 $1,745,865 달러이며 NFLX 비중은 1.36%입니다. 반도체·빅테크·AI 인프라·레버리지 ETF를 합치면 **약 77%가 단일 AI 설비투자 팩터**에 노출되어 있습니다. NFLX는 SPY 대비 2년 베타 0.70, 상관계수 0.33으로 진정한 분산 자산입니다. 스트레스 테스트에서 제안안 적용 시 S1 낙폭이 -33.8%에서 -33.3%로 개선됩니다. CRO는 기존 포트폴리오의 베타 1.56(상한 1.20)과 현금 5.7%(목표 15~20%)를 위반으로 지적하고, NFLX는 **최대 3.0% 조건부 승인**(NVDA 매도 자금만 사용, 실적 확인 후 집행, 추가분 $60.50 손절)했습니다.

---

## STAGE 5 — CIO Synthesis & Valuation Math / CIO 종합 및 밸류에이션

### 5.1 Normalized Earnings
- FY26 consensus EPS $3.58 includes ~$0.47 of fee benefit, so **underlying FY26 EPS ≈ $3.11** (P/E 22.4x).
- FY27E EPS **$3.80** (45 analysts; range $3.48–$4.09) → **forward P/E 18.3x**.

### 5.2 Intrinsic Value
| Method | Assumptions | Value/Share |
| :--- | :--- | ---: |
| Strict DCF | FY27E true FCF $10.8B; growth 13% (Y2–5) → 8% (Y6–10); terminal 3%; CoE 9.5%; net debt $5.3B; 3% share shrink | **$65.95** |
| P/E cross-check | 22x × FY27E EPS $3.80 | **$83.60** |
| **Blend (Conservative IV)** | 50/50 | **$74.78** |

### 5.3 Scenarios
| Scenario | Prob. | EPS (FY27E) | Multiple | Target | Return |
| :--- | :---: | ---: | ---: | ---: | ---: |
| Bull | 25% | $3.95 | 26x | $102.70 | +47.3% |
| Base | 50% | $3.80 | 22x | $83.60 | +19.9% |
| Bear | 25% | $3.45 | 16x | $55.20 | −20.8% |
| **Prob-weighted** | | | | **$81.28** | **+16.6%** |

### 5.4 Final Committee Vote
| Member | Vote |
| :--- | :--- |
| Buffett | Hold / add ≤ $67 |
| Munger | Hold (quality compounder) |
| Lynch | Hold (fair) |
| Druckenmiller | Watch (no aggressive size) |
| O'Neil | No new buy until > 200-DMA |
| Technician | Buy only at $65–67 support |
| PM | Raise to 2.75%, fund from NVDA |
| CRO | Approved, cap 3.0% |
| **CIO** | **HOLD CORE + CONDITIONAL ACCUMULATE** |

> **한국어 요약 (5단계)**: 일회성 수수료를 제거한 FY26 실질 EPS는 약 $3.11, FY27E EPS는 $3.80(선행 P/E 18.3배)입니다. 엄격한 DCF $65.95와 P/E 22배 $83.60을 블렌드한 보수적 내재가치는 **$74.78 달러**입니다. 확률가중 목표가는 **$81.28 달러(+16.6%)**입니다. 위원회는 최종적으로 **핵심 보유 + 조건부 분할 매수**로 의결했습니다. 10월 20일 실적이 3대 조건(매출 가이던스 $51.0B 이상, 영업이익률 31.5% 재확인, 광고 2배 성장)을 통과하면 150주를 매수하고, $65.00 지정가로 200주를 매수하며, NVDA 100주 매도로 자금을 조달합니다.

---
**Prepared for**: BM사장님 | **Approved**: DADAIC CIO | **Document**: DADAIC-IC-PROC-NFLX-261007
