# 📁 DADAIC Investment Firm - Local Data Cache (`cache/`)
> **Institutional Local Data Cache Architecture**  
> *Bilingual Edition: [English](#-english-version) | [한국어](#-한국어-버전)*

---

# 🇺🇸 English Version

## 📌 Purpose & Operational Principles
This directory serves as an institutional-grade local data cache designed to locally store raw US SEC filings, quantitative time-series data, and macroeconomic indicators. Its primary goals are to **maximize repeat analysis speed** and **prevent external API rate limit throttling**.

---

## 🗂️ Subdirectory Structure

- `cache/sec_filings/`: Parsed JSON items and raw financial statements from US SEC EDGAR Form 10-K and 10-Q filings (Default TTL: 90 days).
- `cache/market_data/`: Ticker-specific daily/weekly OHLCV time-series, volume profiles, and quantitative/technical metrics (Default TTL: 24 hours / 72 hours over weekends).
- `cache/macro/`: Federal Reserve Net Liquidity, Treasury yield curve spreads, and Reverse Repo (RRP) series (Default TTL: 24 hours).

---

## ⏱️ Data Freshness & TTL (Time-To-Live) Policy

1. **Real-Time Market Prices vs. Cached Data**:
   - For trade order sizing and rebalancing executions (`CIO REBALANCE`), the latest live prices are always fetched with top priority.
   - For historical analysis, multi-year backtesting, 3Y/5Y CAGR calculations, and portfolio Beta modeling, local cached time-series are actively utilized.
2. **SEC Periodic Filings (10-K, 10-Q)**:
   - Immediately following quarterly earnings releases, the latest 10-Q is refreshed on demand. Established historical 10-K/10-Q filings are retained permanently to eliminate redundant remote queries.
3. **Integrity Principle (Zero-Friction Fallback)**:
   - If a cached file is detected to be corrupted or fails schema validation, it is immediately re-downloaded from the primary source and overwritten without interrupting execution.

---

<br><br>

---

# 🇰🇷 한국어 버전

## 📌 목적 및 운영 원칙
본 디렉터리는 미국 SEC 공시 원문, 퀀트 주가 시계열, 거시경제 지표 데이터를 로컬에 임시 저장하여 **반복 분석 속도 극대화** 및 **외부 API Rate Limit 방지**를 위해 운용되는 기관급 로컬 데이터 캐시입니다.

---

## 🗂️ 서브 디렉터리 구조

- `cache/sec_filings/`: 미국 SEC EDGAR 10-K, 10-Q 파싱 JSON 및 재무제표 원문 (기본 TTL: 90일)
- `cache/market_data/`: 티커별 일봉/주봉 시계열, 거래량 프로파일, 기술적 지표 캐시 (기본 TTL: 24시간 / 주말 72시간)
- `cache/macro/`: 연준 유동성(Net Liquidity), 국채 금리 시계열, 역레포(RRP) 데이터 (기본 TTL: 24시간)

---

## ⏱️ 데이터 신선도 및 TTL (Time-To-Live) 정책

1. **실시간 가격 데이터 vs 캐시**:
   - 정밀 주문 및 리밸런싱(`CIO REBALANCE`) 실행 시점의 최종 주가는 항상 실시간(Live) 데이터를 최우선 조회합니다.
   - 백테스팅, 3개년/5개년 장기 CAGR, 변동성(Beta) 연산 등 과거 시계열 분석 시에는 로컬 캐시를 적극 활용합니다.
2. **SEC 정기 보고서 (10-K, 10-Q)**:
   - 분기 실적 발표 직후에는 최신 10-Q를 즉시 갱신하며, 이미 확정된 과거 연도 10-K 데이터는 불필요한 재다운로드를 피하기 위해 영구 보존합니다.
3. **무결성 원칙**:
   - 캐시 파일 손상 또는 포맷 불일치 감지 시 즉시 원격 원천 소스에서 재다운로드하여 덮어씁니다(Zero-Friction Fallback).
