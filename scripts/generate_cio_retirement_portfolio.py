#!/usr/bin/env python3
"""
DADAIC Investment Firm - CIO & Investment Committee Universal Retirement ETF Portfolio Generator
Generates:
1. DecisionMemo/Media/CIO-Universal-Retirement-ETF-Infographic.html
2. DecisionMemo/Media/CIO-Universal-Retirement-ETF-Infographic.png
3. Copies to Artifact directory for Antigravity viewer
"""

import os
import sys
import subprocess
import shutil

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(ROOT, "DecisionMemo", "Media")
ARTIFACT_DIR = r"C:\Users\bm021\.gemini\antigravity\brain\6eb41325-9c08-4bb3-a746-1013336e4aa3"

os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

HTML_CONTENT = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>CIO & 투자위원회 엄선 평생 은퇴 ETF 골든 포트폴리오</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+KR:wght@400;500;600;700;800;900&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', 'Noto Sans KR', sans-serif;
      background-color: #060d17;
      color: #0f172a;
      display: flex;
      justify-content: center;
      padding: 40px 20px;
      -webkit-font-smoothing: antialiased;
    }
    .infographic-wrapper {
      width: 1400px;
      background: #ffffff;
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.45);
      border: 1px solid #1e293b;
    }
    
    /* HERO HEADER */
    .hero-header {
      background: linear-gradient(135deg, #091322 0%, #0f172a 40%, #1e1b4b 100%);
      color: #ffffff;
      padding: 65px 70px 55px;
      position: relative;
      border-bottom: 4px solid #6366f1;
    }
    .hero-tag-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
    }
    .firm-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(99, 102, 241, 0.2);
      border: 1px solid rgba(165, 180, 252, 0.45);
      padding: 8px 20px;
      border-radius: 9999px;
      font-size: 13.5px;
      font-weight: 800;
      color: #c7d2fe;
      letter-spacing: 1.2px;
      text-transform: uppercase;
    }
    .doc-meta {
      font-size: 13.5px;
      color: #94a3b8;
      font-weight: 600;
    }
    .hero-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 46px;
      font-weight: 900;
      letter-spacing: -1.2px;
      line-height: 1.25;
      margin-bottom: 18px;
      background: linear-gradient(120deg, #ffffff 40%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
      font-size: 18.5px;
      color: #cbd5e1;
      line-height: 1.65;
      max-width: 1150px;
      font-weight: 400;
    }

    /* STATS SUMMARY BAR */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      padding: 28px 70px;
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
    }
    .stat-pill {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 20px 24px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }
    .stat-label {
      font-size: 12.5px;
      font-weight: 800;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .stat-value {
      font-family: 'Outfit', sans-serif;
      font-size: 34px;
      font-weight: 900;
      color: #0f172a;
      margin-top: 4px;
    }
    .stat-desc {
      font-size: 13px;
      color: #4f46e5;
      font-weight: 700;
      margin-top: 4px;
    }

    /* CONTENT CONTAINER */
    .content-container {
      padding: 55px 70px;
      display: flex;
      flex-direction: column;
      gap: 50px;
      background: #ffffff;
    }

    /* SECTION HEADLINE */
    .section-headline {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 24px;
    }
    .section-icon {
      width: 46px;
      height: 46px;
      background: #eef2ff;
      border: 1.5px solid #c7d2fe;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
    }
    .section-title-text h3 {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }
    .section-title-text p {
      font-size: 14.5px;
      color: #64748b;
      margin-top: 2px;
    }

    /* PHILOSOPHY STATEMENT CALLOUT */
    .thesis-banner {
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 2px solid #a7f3d0;
      border-radius: 20px;
      padding: 30px 36px;
      display: flex;
      gap: 24px;
      align-items: flex-start;
    }
    .thesis-icon {
      font-size: 40px;
      line-height: 1;
    }
    .thesis-text h4 {
      font-size: 20px;
      font-weight: 800;
      color: #065f46;
      margin-bottom: 8px;
    }
    .thesis-text p {
      font-size: 15px;
      color: #1e3a2f;
      line-height: 1.65;
    }

    /* 7 GOLDEN PILLARS GRID */
    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 14px;
    }
    .pillar-card {
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 18px;
      padding: 22px 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);
      transition: transform 0.2s;
    }
    .pillar-num {
      font-family: 'Outfit', sans-serif;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 1px;
      color: #94a3b8;
    }
    .pillar-ticker {
      font-family: 'Outfit', sans-serif;
      font-size: 24px;
      font-weight: 900;
      color: #0f172a;
      letter-spacing: -0.5px;
    }
    .pillar-badge {
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      align-self: flex-start;
    }
    .pillar-role {
      font-size: 12.5px;
      font-weight: 700;
      color: #1e293b;
      line-height: 1.4;
      min-height: 36px;
    }
    .pillar-fee {
      font-size: 12px;
      font-weight: 800;
      color: #059669;
      background: #ecfdf5;
      padding: 2px 6px;
      border-radius: 4px;
      display: inline-block;
      align-self: flex-start;
    }
    .pillar-desc {
      font-size: 12px;
      color: #475569;
      line-height: 1.5;
      flex: 1;
    }
    .pillar-champion {
      font-size: 11.5px;
      font-weight: 700;
      color: #4f46e5;
      border-top: 1px dashed #e2e8f0;
      padding-top: 8px;
    }

    /* PILLAR THEME COLORS */
    .p-voo { border-top: 5px solid #2563eb; }
    .p-voo .pillar-badge { background: #dbeafe; color: #1e40af; }

    .p-schd { border-top: 5px solid #059669; }
    .p-schd .pillar-badge { background: #d1fae5; color: #065f46; }

    .p-qqqm { border-top: 5px solid #7c3aed; }
    .p-qqqm .pillar-badge { background: #ede9fe; color: #5b21b6; }

    .p-sgov { border-top: 5px solid #0284c7; }
    .p-sgov .pillar-badge { background: #e0f2fe; color: #075985; }

    .p-ief { border-top: 5px solid #475569; }
    .p-ief .pillar-badge { background: #f1f5f9; color: #334155; }

    .p-gldm { border-top: 5px solid #d97706; }
    .p-gldm .pillar-badge { background: #fef3c7; color: #92400e; }

    .p-vnq { border-top: 5px solid #ea580c; }
    .p-vnq .pillar-badge { background: #ffedd5; color: #9a3412; }

    /* TWO MODEL PORTFOLIOS COMPARISON */
    .models-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
    }
    .model-box {
      border: 2px solid #e2e8f0;
      border-radius: 24px;
      padding: 34px 36px;
      background: #f8fafc;
      display: flex;
      flex-direction: column;
      gap: 22px;
      position: relative;
    }
    .model-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 18px;
    }
    .model-tag {
      font-family: 'Outfit', sans-serif;
      font-size: 12px;
      font-weight: 900;
      letter-spacing: 1px;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 8px;
    }
    .tag-growth { background: #eff6ff; color: #1d4ed8; border: 1.5px solid #bfdbfe; }
    .tag-income { background: #ecfdf5; color: #047857; border: 1.5px solid #a7f3d0; }
    
    .model-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 24px;
      font-weight: 800;
      color: #0f172a;
    }
    .model-target {
      font-size: 13.5px;
      color: #64748b;
      margin-top: 3px;
    }
    .model-goal-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 14px 18px;
      font-size: 13.5px;
      color: #334155;
      font-weight: 600;
      line-height: 1.5;
    }

    /* ALLOCATION BREAKDOWN TABLE */
    .alloc-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      background: #ffffff;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid #e2e8f0;
    }
    .alloc-table th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      text-align: left;
      padding: 10px 14px;
      border-bottom: 2px solid #cbd5e1;
      font-size: 12.5px;
    }
    .alloc-table td {
      padding: 10px 14px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }
    .alloc-weight {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 900;
      color: #0f172a;
    }
    .alloc-bar-cell {
      width: 32%;
    }
    .alloc-bar-wrap {
      height: 8px;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
    }
    .alloc-bar-fill {
      height: 100%;
      border-radius: 9999px;
    }

    /* SIMULATION METRICS BOX */
    .sim-strip {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px;
    }
    .sim-item {
      text-align: center;
    }
    .sim-label {
      font-size: 11.5px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
    }
    .sim-val {
      font-family: 'Outfit', sans-serif;
      font-size: 20px;
      font-weight: 900;
      color: #0f172a;
      margin-top: 3px;
    }

    /* ELIMINATION COMPARISON TABLE */
    .elimination-card {
      background: #fff5f5;
      border: 2px solid #fecaca;
      border-radius: 20px;
      padding: 30px 34px;
    }
    .elim-header {
      display: flex;
      align-items: center;
      gap: 12px;
      color: #b91c1c;
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 16px;
    }
    .elim-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      background: #ffffff;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid #fca5a5;
    }
    .elim-table th {
      background: #fee2e2;
      color: #991b1b;
      font-weight: 800;
      text-align: left;
      padding: 12px 16px;
    }
    .elim-table td {
      padding: 12px 16px;
      border-bottom: 1px solid #fee2e2;
      color: #374151;
      line-height: 1.5;
    }

    /* 5 LIFE PRINCIPLES */
    .rules-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
    }
    .rule-card {
      background: #f8fafc;
      border: 1.5px solid #e2e8f0;
      border-radius: 18px;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .rule-num {
      width: 32px;
      height: 32px;
      border-radius: 10px;
      background: #4f46e5;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Outfit', sans-serif;
      font-size: 15px;
      font-weight: 900;
    }
    .rule-title {
      font-size: 15px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.35;
    }
    .rule-text {
      font-size: 12.5px;
      color: #475569;
      line-height: 1.55;
    }

    /* FOOTER */
    .footer-bar {
      background: #091322;
      color: #94a3b8;
      padding: 28px 70px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13.5px;
      border-top: 1px solid #1e293b;
    }
    .footer-left {
      display: flex;
      gap: 18px;
      align-items: center;
    }
    .footer-badge {
      color: #818cf8;
      font-weight: 800;
    }
  </style>
</head>
<body>

<div class="infographic-wrapper">
  
  <!-- HERO HEADER -->
  <header class="hero-header">
    <div class="hero-tag-row">
      <div class="firm-badge">
        <span>🏛️</span> DADAIC Investment Committee Official Portfolio
      </div>
      <div class="doc-meta">
        Strict USD Standard | Institutional All-Weather Architecture
      </div>
    </div>
    <h1 class="hero-title">평생 은퇴 ETF 골든 포트폴리오 (The Golden 7 Blueprint)</h1>
    <p class="hero-subtitle">
      CIO와 투자위원회가 26개 중복 리스트를 원천 해체하여 도출한 <strong>단 7개의 무결점 정예 ETF</strong>.  
      가짜 다각화와 수수료 낭비를 배제하고, 어떤 경제 위기에도 원금을 지키며 복리로 성장하는 보편적(Universal) 은퇴 표준 설계도.
    </p>
  </header>

  <!-- KEY METRICS BAR -->
  <div class="stats-bar">
    <div class="stat-pill">
      <div class="stat-label">선정 ETF 개수</div>
      <div class="stat-value">7종 (The Golden 7)</div>
      <div class="stat-desc">26개 중복 ➔ 7대 무결점 압축</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">가중평균 운용보수</div>
      <div class="stat-value">0.075% / yr</div>
      <div class="stat-desc">30년 복리 수수료 누수 제로</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">상호 비상관 자산</div>
      <div class="stat-value">5대 핵심 팩터</div>
      <div class="stat-desc">주식·배당·초단기채·중기채·금·리츠</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">적용 대상자</div>
      <div class="stat-value">Universal (누구나)</div>
      <div class="stat-desc">20대 사회초년생부터 70대 은퇴자까지</div>
    </div>
  </div>

  <div class="content-container">

    <!-- 1. COMMITTEE THESIS -->
    <section>
      <div class="thesis-banner">
        <div class="thesis-icon">💡</div>
        <div class="thesis-text">
          <h4>CIO & 투자위원회 핵심 철학: "은퇴 포트폴리오에 26개 종목은 독(Poison)이다"</h4>
          <p>
            일반 투자자들은 종목이 많을수록 분산투자가 잘 되었다고 착각하지만, 26개 리스트는 <strong>빅테크 중복 노출(가짜 다각화), 비대칭 위험의 커버드콜 함정, 리밸런싱 피로도</strong>만 가중시킵니다.  
            기관급 은퇴 투자의 본질은 <strong>'서로 다른 경제 국면에서 다르게 반응하는 7개의 무결점 코어 자산'</strong>을 초저비용으로 묶어 영구적으로 보유하는 것입니다.
          </p>
        </div>
      </div>
    </section>

    <!-- 2. THE 7 GOLDEN PILLARS -->
    <section>
      <div class="section-headline">
        <div class="section-icon">👑</div>
        <div class="section-title-text">
          <h3>투자위원회가 엄선한 7대 골든 ETF (The Golden 7)</h3>
          <p>각자 독자적인 임무를 수행하며 상호 보완하는 7개의 복리 빌딩 블록</p>
        </div>
      </div>

      <div class="pillars-grid">

        <!-- 1. VOO -->
        <div class="pillar-card p-voo">
          <div class="pillar-num">PILLAR 01</div>
          <div class="pillar-ticker">VOO</div>
          <span class="pillar-badge">미국 핵심 시장</span>
          <div class="pillar-role">자본주의 500대 기업 장기 복리 닻</div>
          <div class="pillar-fee">연 0.03%</div>
          <div class="pillar-desc">
            미국 경제 패권과 기업 이익 성장의 과실을 가장 순수하고 저렴하게 수취하는 불변의 코어.
          </div>
          <div class="pillar-champion">
            🏛️ 버핏 1순위 추천
          </div>
        </div>

        <!-- 2. SCHD -->
        <div class="pillar-card p-schd">
          <div class="pillar-num">PILLAR 02</div>
          <div class="pillar-ticker">SCHD</div>
          <span class="pillar-badge">우량 배당성장</span>
          <div class="pillar-role">물가를 이기는 현금흐름 복리 머신</div>
          <div class="pillar-fee">연 0.06%</div>
          <div class="pillar-desc">
            10년 연속 배당+ROE 27%+부채 안전망. 연 3.2% 배당과 연 11% 배당성장률의 황금 밸런스.
          </div>
          <div class="pillar-champion">
            💎 멍거 퀄리티 픽
          </div>
        </div>

        <!-- 3. QQQM -->
        <div class="pillar-card p-qqqm">
          <div class="pillar-num">PILLAR 03</div>
          <div class="pillar-ticker">QQQM</div>
          <span class="pillar-badge">테크 혁신 성장</span>
          <div class="pillar-role">AI·디지털 메가트렌드 초과수익</div>
          <div class="pillar-fee">연 0.15%</div>
          <div class="pillar-desc">
            나스닥 100 혁신 기업. QQQ 대비 저렴한 보수로 평생 은퇴 계좌 적립에 최적화된 성장 터빈.
          </div>
          <div class="pillar-champion">
            🚀 린치 혁신 성장주
          </div>
        </div>

        <!-- 4. SGOV -->
        <div class="pillar-card p-sgov">
          <div class="pillar-num">PILLAR 04</div>
          <div class="pillar-ticker">SGOV</div>
          <span class="pillar-badge">초단기 국채</span>
          <div class="pillar-role">무위험 현금 & 강제 손절 방지 방패</div>
          <div class="pillar-fee">연 0.07%</div>
          <div class="pillar-desc">
            0~3개월 미국 초단기 국채. 변동성 0. 대폭락장에도 주식을 팔지 않게 해주는 1~2년 치 생활비 버퍼.
          </div>
          <div class="pillar-champion">
            🛡️ 리스크 매니저 픽
          </div>
        </div>

        <!-- 5. IEF -->
        <div class="pillar-card p-ief">
          <div class="pillar-num">PILLAR 05</div>
          <div class="pillar-ticker">IEF</div>
          <span class="pillar-badge">중기 미국 국채</span>
          <div class="pillar-role">시스템 위기 시 반사적 자본차익 헤지</div>
          <div class="pillar-fee">연 0.15%</div>
          <div class="pillar-desc">
            7~10년 중기 국채. TLT의 치명적 금리 변동성을 피하면서 경기 침체 시 주식 폭락을 방어.
          </div>
          <div class="pillar-champion">
            ⚖️ 매크로 헤지 앵커
          </div>
        </div>

        <!-- 6. GLDM -->
        <div class="pillar-card p-gldm">
          <div class="pillar-num">PILLAR 06</div>
          <div class="pillar-ticker">GLDM</div>
          <span class="pillar-badge">실물 금</span>
          <div class="pillar-role">통화가치 희석 & 지정학적 방파제</div>
          <div class="pillar-fee">연 0.10%</div>
          <div class="pillar-desc">
            실물 금 기반 초저보수 ETF. 달러 약세와 스태그플레이션 국면에서 주식·채권과 무관하게 자산 수호.
          </div>
          <div class="pillar-champion">
            🌍 올웨더 인플레 방패
          </div>
        </div>

        <!-- 7. VNQ -->
        <div class="pillar-card p-vnq">
          <div class="pillar-num">PILLAR 07</div>
          <div class="pillar-ticker">VNQ</div>
          <span class="pillar-badge">부동산 리츠</span>
          <div class="pillar-role">물가상승 전가형 실물 부동산 인컴</div>
          <div class="pillar-fee">연 0.13%</div>
          <div class="pillar-desc">
            미국 물류센터, 데이터센터, 주거용 리츠 160여 개사. 임대료 상승이 배당으로 직결되는 실물 자산.
          </div>
          <div class="pillar-champion">
            🏢 실물 인컴 헤지
          </div>
        </div>

      </div>
    </section>

    <!-- 3. TWO UNIVERSAL LIFECYCLE MODELS -->
    <section>
      <div class="section-headline">
        <div class="section-icon">⚖️</div>
        <div class="section-title-text">
          <h3>누구에게나 추천하는 2대 생애주기 표준 모델 (Universal Twin Models)</h3>
          <p>투자자의 연령과 목표에 따라 7개 ETF의 '비중(Weight)'만 조절하여 평생 운용</p>
        </div>
      </div>

      <div class="models-grid">

        <!-- MODEL 1: WEALTH ACCUMULATOR -->
        <div class="model-box">
          <div class="model-header">
            <div>
              <div class="model-title">Model A : 부의 증식 엔진 (Wealth Accumulator)</div>
              <div class="model-target">20대 ~ 50대 초반 (은퇴 준비기 / 직장인 누구나)</div>
            </div>
            <span class="model-tag tag-growth">성장 극대화형</span>
          </div>

          <div class="model-goal-card">
            🎯 <strong>운용 목표:</strong> 주식 75% 비중으로 복리 자산 성장을 가속하고, 25%의 안전자산으로 단기 변동성을 흡수. 배당금은 100% 재투자.
          </div>

          <table class="alloc-table">
            <thead>
              <tr>
                <th>티커</th>
                <th>자산군</th>
                <th>비중</th>
                <th>할당 바</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>VOO</strong></td>
                <td>미국 S&P 500 코어</td>
                <td class="alloc-weight">30.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 30%; background: #2563eb;"></div></div></td>
              </tr>
              <tr>
                <td><strong>SCHD</strong></td>
                <td>우량 배당성장</td>
                <td class="alloc-weight">25.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 25%; background: #059669;"></div></div></td>
              </tr>
              <tr>
                <td><strong>QQQM</strong></td>
                <td>나스닥 100 테크</td>
                <td class="alloc-weight">20.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 20%; background: #7c3aed;"></div></div></td>
              </tr>
              <tr>
                <td><strong>SGOV</strong></td>
                <td>초단기채 (비상금)</td>
                <td class="alloc-weight">10.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 10%; background: #0284c7;"></div></div></td>
              </tr>
              <tr>
                <td><strong>IEF</strong></td>
                <td>중기 국채</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #475569;"></div></div></td>
              </tr>
              <tr>
                <td><strong>GLDM</strong></td>
                <td>실물 금</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #d97706;"></div></div></td>
              </tr>
              <tr>
                <td><strong>VNQ</strong></td>
                <td>부동산 리츠</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #ea580c;"></div></div></td>
              </tr>
            </tbody>
          </table>

          <div class="sim-strip">
            <div class="sim-item">
              <div class="sim-label">기대 연환산 수익률</div>
              <div class="sim-val" style="color: #2563eb;">연 9.5 ~ 11.5%</div>
            </div>
            <div class="sim-item">
              <div class="sim-label">초기 배당수익률</div>
              <div class="sim-val">연 2.2% + 성장</div>
            </div>
            <div class="sim-item">
              <div class="sim-label">위기 예상 MDD</div>
              <div class="sim-val" style="color: #059669;">-19.5% 이내</div>
            </div>
          </div>
        </div>

        <!-- MODEL 2: PERPETUAL CASH FLOW -->
        <div class="model-box">
          <div class="model-header">
            <div>
              <div class="model-title">Model B : 영구 현금흐름 엔진 (Perpetual Cash Flow)</div>
              <div class="model-target">50대 후반 ~ 70대+ (은퇴 생활자 / 즉시 인컴 수령 누구나)</div>
            </div>
            <span class="model-tag tag-income">원금 보존 & 인컴형</span>
          </div>

          <div class="model-goal-card">
            🎯 <strong>운용 목표:</strong> 주식 원금을 단 1주도 팔지 않고, 연 3.5~4.0% 수준의 순수 배당과 이자만으로 매월 생활비를 영구 조달.
          </div>

          <table class="alloc-table">
            <thead>
              <tr>
                <th>티커</th>
                <th>자산군</th>
                <th>비중</th>
                <th>할당 바</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>SCHD</strong></td>
                <td>우량 배당성장 (코어)</td>
                <td class="alloc-weight">35.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 35%; background: #059669;"></div></div></td>
              </tr>
              <tr>
                <td><strong>SGOV</strong></td>
                <td>초단기채 (2년 생활비)</td>
                <td class="alloc-weight">20.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 20%; background: #0284c7;"></div></div></td>
              </tr>
              <tr>
                <td><strong>VOO</strong></td>
                <td>미국 S&P 500</td>
                <td class="alloc-weight">15.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 15%; background: #2563eb;"></div></div></td>
              </tr>
              <tr>
                <td><strong>IEF</strong></td>
                <td>중기 국채</td>
                <td class="alloc-weight">15.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 15%; background: #475569;"></div></div></td>
              </tr>
              <tr>
                <td><strong>GLDM</strong></td>
                <td>실물 금</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #d97706;"></div></div></td>
              </tr>
              <tr>
                <td><strong>VNQ</strong></td>
                <td>부동산 리츠</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #ea580c;"></div></div></td>
              </tr>
              <tr>
                <td><strong>QQQM</strong></td>
                <td>나스닥 100</td>
                <td class="alloc-weight">5.0%</td>
                <td class="alloc-bar-cell"><div class="alloc-bar-wrap"><div class="alloc-bar-fill" style="width: 5%; background: #7c3aed;"></div></div></td>
              </tr>
            </tbody>
          </table>

          <div class="sim-strip">
            <div class="sim-item">
              <div class="sim-label">연간 순수 현금흐름</div>
              <div class="sim-val" style="color: #059669;">연 3.65% (월지급)</div>
            </div>
            <div class="sim-item">
              <div class="sim-label">2년 치 생활비 버퍼</div>
              <div class="sim-val">SGOV 20% 확보</div>
            </div>
            <div class="sim-item">
              <div class="sim-label">위기 예상 MDD</div>
              <div class="sim-val" style="color: #059669;">-11.2% 이내</div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 4. WHY WE ELIMINATED THE OTHER 19 ETFS -->
    <section>
      <div class="elimination-card">
        <div class="elim-header">
          <span>🚫</span> 투자위원회가 기존 19개 ETF를 과감히 탈락시킨 이유 (Elimination Matrix)
        </div>
        <table class="elim-table">
          <thead>
            <tr>
              <th style="width: 25%;">탈락 그룹 및 티커</th>
              <th style="width: 35%;">포렌식 탈락 사유</th>
              <th style="width: 40%;">위원회 결정 및 대체 해결책</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>커버드콜 군<br>(JEPI, JEPQ, DIVO)</strong></td>
              <td>상방 이익은 캡(Capped)되고 하방 위험은 열려 있어 장기 보유 시 실질 구매력과 원금이 심각하게 훼손됨.</td>
              <td><strong>전원 일치 탈락</strong>. 원금 마모 없는 <strong>SCHD(우량 배당성장) + SGOV(초단기 무위험채)</strong>로 대체.</td>
            </tr>
            <tr>
              <td><strong>중복 테크/반도체<br>(VUG, VGT, SMH)</strong></td>
              <td>엔비디아, 애플, MS 등에 극단적 중복 몰빵을 초래하며, 반도체 단일 섹터 사이클 폭락 위험이 과도함.</td>
              <td><strong>탈락</strong>. 나스닥 100을 가장 저렴한 보수(0.15%)로 추종하는 <strong>QQQM 단 1종목</strong>으로 일원화.</td>
            </tr>
            <tr>
              <td><strong>중복 시장/해외<br>(VTI, VT, VEA, VWO, VXUS)</strong></td>
              <td>VOO와 VTI는 상관계수 0.99로 동일하며, 비미국 주식은 15년간 저성장과 환율 변동성으로 미국 대비 성과 열위.</td>
              <td><strong>탈락</strong>. 글로벌 혁신을 주도하는 <strong>미국 S&P 500(VOO)</strong>에 집중하여 복리 수익률 극대화.</td>
            </tr>
            <tr>
              <td><strong>초장기채 / 중복 리츠<br>(TLT, XLRE, BND)</strong></td>
              <td>TLT는 금리 변동에 따른 듀레이션 리스크가 주식만큼 위험함(-45% 폭락 이력). XLRE는 VNQ의 하위 집합에 불과.</td>
              <td><strong>탈락</strong>. 변동성이 통제된 <strong>중기채(IEF)</strong>와 광범위 리츠 <strong>VNQ</strong>로 위험 대비 보상 비율 최적화.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 5. 5 GOLDEN RULES FOR LIFE -->
    <section>
      <div class="section-headline">
        <div class="section-icon">📜</div>
        <div class="section-title-text">
          <h3>평생 계좌를 지키는 5대 실전 투자 원칙 (Institutional Axioms)</h3>
          <p>종목 선정보다 더 중요한, 평생 흔들리지 않고 자산을 지키는 행동 강령</p>
        </div>
      </div>

      <div class="rules-grid">
        <div class="rule-card">
          <div class="rule-num">1</div>
          <div class="rule-title">종목 단순화의 미학</div>
          <div class="rule-text">
            7개 ETF면 전 세계 자산배분이 완성됩니다. 종목이 15개를 넘어가면 관리가 불가능해지고 수수료만 누수됩니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">2</div>
          <div class="rule-title">SGOV 2년 생활비 철칙</div>
          <div class="rule-text">
            은퇴자는 2년 치 생활비를 무조건 SGOV로 채워두세요. 금융위기가 터져도 주식을 단 1주도 손절하지 않고 버팁니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">3</div>
          <div class="rule-title">가짜 고배당 현혹 금지</div>
          <div class="rule-text">
            연 10% 커버드콜 분배금은 내 원금을 깎아서 주는 착시일 뿐입니다. 배당은 반드시 '기업 이익 성장의 결과물(SCHD)'이어야 합니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">4</div>
          <div class="rule-title">연 1회 생일 리밸런싱</div>
          <div class="rule-text">
            매년 생일이나 연초에 딱 한 번만 비중을 맞추세요. 많이 오른 테크주를 팔아 떨어진 배당주와 채권을 기계적으로 사모읍니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">5</div>
          <div class="rule-title">평생 인출률 4% 규칙</div>
          <div class="rule-text">
            은퇴 후에는 포트폴리오 총액의 연 3.5~4.0%만 인출하십시오. Golden 7 포트폴리오는 100세까지 자산이 마르지 않습니다.
          </div>
        </div>
      </div>
    </section>

  </div>

  <!-- FOOTER -->
  <footer class="footer-bar">
    <div class="footer-left">
      <span class="footer-badge">DADAIC INVESTMENT FIRM</span>
      <span>|</span>
      <span>Chief Investment Officer (CIO) Executive Recommendation</span>
      <span>|</span>
      <span>Strict USD Accounting Standard</span>
    </div>
    <div>
      Document ID: DADAIC-CIO-GOLDEN7-RETIREMENT-261005
    </div>
  </footer>

</div>

</body>
</html>
"""

def generate_files():
    html_path = os.path.join(MEDIA_DIR, "CIO-Universal-Retirement-ETF-Infographic.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[+] Saved HTML: {html_path}")

    # Copy HTML to artifact scratch
    artifact_html = os.path.join(ARTIFACT_DIR, "CIO-Universal-Retirement-ETF-Infographic.html")
    shutil.copy(html_path, artifact_html)

    # Render PNG with Chrome Headless
    png_path = os.path.join(MEDIA_DIR, "CIO-Universal-Retirement-ETF-Infographic.png")
    
    # Render with full height window
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1500,4800",
        "--force-device-scale-factor=1.5",
        f"--screenshot={png_path}",
        html_path
    ]
    print(f"[*] Rendering PNG via Headless Chrome...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] Rendered PNG successfully: {png_path} ({os.path.getsize(png_path)} bytes)")
        # Copy to artifact folder for Antigravity preview
        artifact_png = os.path.join(ARTIFACT_DIR, "CIO-Universal-Retirement-ETF-Infographic.png")
        shutil.copy(png_path, artifact_png)
        print(f"[+] Copied to Artifact: {artifact_png}")
    else:
        print(f"[-] Error rendering Chrome: {res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    generate_files()
