# Rule: DADAIC Shorthand Command Aliases

## Triggers & Actions

### 1. `ICP <TICKER>` or `icp <TICKER>`
- **Action**: Run the complete 5-Stage Investment Committee Pipeline for `<TICKER>` using `my-portfolio.yaml`. Generate the full 10-part deliverable suite (2 bilingual markdown dossiers in `DecisionMemo/` and 8 bright-theme visual files [PDF, PNG, HTML] in `DecisionMemo/Media/`).

### 2. `CIO REVIEW` or `PORT REVIEW`
- **Action**: Run institutional portfolio diagnostic on `my-portfolio.yaml`. Calculate live market values, portfolio weights, beta, False Diversification audit, and output `DecisionMemo/Portfolio-Review-YYMMDD.md`.

### 3. `CIO REBALANCE` or `PORT REBALANCE`
- **Action**: Formulate actionable trade matrix comparing current holdings against investor limits in `my-portfolio.yaml`. Output `DecisionMemo/Portfolio-Rebalance-YYMMDD.md`.

### 4. `CIO STRESS` or `PORT STRESS`
- **Action**: Run 3-scenario macro stress test modeling portfolio MDD and vulnerable assets. Output `DecisionMemo/Portfolio-StressTest-YYMMDD.md`.

### 5. `CIO ASK <QUERY>`
- **Action**: Answer the specific strategic question as the CIO directly grounded in `my-portfolio.yaml`.

### 6. `CIO PICKS [MODE]`
- **Action**: Execute `scripts/cio_screener.py` to screen US equities, evaluate moats and portfolio gap-filling complementarity, and output `DecisionMemo/CIO-Picks-YYMMDD.md`. Supported modes: default, `buffett`, `garp`, `defense`, or themes (`power`, `health`, etc.).

---

## Strict Currency Protocol (USD Only / No KRW)
The investor resides in the United States and uses USD base currency (`base_currency: "USD"`). In ALL outputs (English and Korean versions of memos, deliberation process files, slide decks, and infographics), all values, stock prices, target prices, and portfolio figures must remain strictly denominated in **USD ($)**. Do NOT convert to or append Korean Won (KRW / 원).

---

## Strict Principal Title & Honorific Protocol (Always 'BM사장님')
In ALL communications, reports, Decision Memos, process files, and infographics, NEVER refer to the principal as '유저님', '유저', or generic terms. ALWAYS address and designate the principal strictly as **'BM사장님'**.
