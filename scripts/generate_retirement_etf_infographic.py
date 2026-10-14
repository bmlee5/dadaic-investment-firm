#!/usr/bin/env python3
"""
DADAIC Investment Firm - Retirement ETF Master Infographic Generator
Generates:
1. DecisionMemo/Media/Retirement-ETF-Master-Infographic.html
2. DecisionMemo/Media/Retirement-ETF-Master-Infographic.png
3. Copies to Artifact directory for instant viewing
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
  <title>은퇴 대비 핵심 ETF 26선 완전 분석 인포그래픽</title>
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
      background-color: #0b1120;
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
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
      border: 1px solid #e2e8f0;
    }
    
    /* HEADER HERO */
    .hero-header {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f2744 100%);
      color: #ffffff;
      padding: 60px 70px 50px;
      position: relative;
      border-bottom: 4px solid #3b82f6;
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
      background: rgba(59, 130, 246, 0.18);
      border: 1px solid rgba(147, 197, 253, 0.4);
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      color: #93c5fd;
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .doc-meta {
      font-size: 13px;
      color: #94a3b8;
      font-weight: 500;
    }
    .hero-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 46px;
      font-weight: 900;
      letter-spacing: -1px;
      line-height: 1.25;
      margin-bottom: 16px;
      background: linear-gradient(120deg, #ffffff 30%, #93c5fd 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
      font-size: 19px;
      color: #cbd5e1;
      line-height: 1.6;
      max-width: 1100px;
      font-weight: 400;
    }
    
    /* STATS SUMMARY BAR */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      padding: 30px 70px;
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
      font-size: 13px;
      font-weight: 700;
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
      color: #3b82f6;
      font-weight: 600;
      margin-top: 4px;
    }

    /* MAIN CONTAINER */
    .content-container {
      padding: 50px 70px;
      display: flex;
      flex-direction: column;
      gap: 45px;
      background: #ffffff;
    }

    /* SECTION HEADER */
    .section-headline {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 24px;
    }
    .section-icon {
      width: 44px;
      height: 44px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
    }
    .section-title-text h3 {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }
    .section-title-text p {
      font-size: 14px;
      color: #64748b;
      margin-top: 2px;
    }

    /* PYRAMID COMPONENT */
    .pyramid-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 20px;
      padding: 32px 36px;
    }
    .pyramid-tiers {
      display: flex;
      flex-direction: column;
      gap: 12px;
      align-items: center;
      margin-top: 10px;
    }
    .tier-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-radius: 14px;
      padding: 16px 28px;
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);
      transition: transform 0.2s;
    }
    .tier-5 {
      width: 65%;
      background: linear-gradient(90deg, #7c3aed, #9333ea);
    }
    .tier-4 {
      width: 74%;
      background: linear-gradient(90deg, #0284c7, #0ea5e9);
    }
    .tier-3 {
      width: 83%;
      background: linear-gradient(90deg, #059669, #10b981);
    }
    .tier-2 {
      width: 92%;
      background: linear-gradient(90deg, #2563eb, #3b82f6);
    }
    .tier-1 {
      width: 100%;
      background: linear-gradient(90deg, #334155, #475569);
    }
    .tier-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .tier-rank {
      background: rgba(255,255,255,0.22);
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }
    .tier-name {
      font-size: 16px;
      font-weight: 700;
    }
    .tier-etfs {
      font-family: 'Outfit', sans-serif;
      background: rgba(0,0,0,0.2);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }
    .tier-right {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .tier-weight {
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 900;
      background: rgba(255,255,255,0.2);
      padding: 4px 14px;
      border-radius: 10px;
    }
    .tier-role {
      font-size: 13.5px;
      color: #f1f5f9;
      font-weight: 500;
    }

    /* 8 CLUSTERS GRID */
    .clusters-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 26px;
    }
    .cluster-card {
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 20px;
      padding: 26px 28px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.04);
      position: relative;
    }
    .cluster-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 14px;
    }
    .cluster-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .cluster-icon {
      font-size: 26px;
    }
    .cluster-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
    }
    .cluster-desc {
      font-size: 13px;
      color: #64748b;
      margin-top: 2px;
    }
    .badge-category {
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* ETF LIST INSIDE CLUSTER */
    .etf-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .etf-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: background 0.15s;
    }
    .etf-item:hover {
      background: #f1f5f9;
    }
    .etf-item-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .etf-ticker-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .etf-num {
      font-size: 12px;
      font-weight: 800;
      color: #94a3b8;
    }
    .ticker-tag {
      font-family: 'Outfit', sans-serif;
      font-size: 17px;
      font-weight: 900;
      color: #0f172a;
      background: #ffffff;
      padding: 3px 10px;
      border-radius: 8px;
      border: 1.5px solid #cbd5e1;
      letter-spacing: 0.5px;
    }
    .etf-name {
      font-size: 14px;
      font-weight: 700;
      color: #1e293b;
    }
    .etf-exposure-badge {
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 6px;
    }
    .etf-item-bot {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      color: #475569;
      line-height: 1.45;
    }
    .etf-features {
      flex: 1;
    }
    .etf-target {
      font-size: 12px;
      font-weight: 700;
      color: #2563eb;
      background: #eff6ff;
      padding: 2px 8px;
      border-radius: 6px;
      white-space: nowrap;
      margin-left: 12px;
    }

    /* COLOR THEMES FOR CLUSTERS */
    .theme-blue { border-top: 5px solid #2563eb; }
    .theme-blue .badge-category { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
    .theme-blue .etf-exposure-badge { background: #dbeafe; color: #1e40af; }
    
    .theme-green { border-top: 5px solid #059669; }
    .theme-green .badge-category { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
    .theme-green .etf-exposure-badge { background: #d1fae5; color: #065f46; }

    .theme-purple { border-top: 5px solid #7c3aed; }
    .theme-purple .badge-category { background: #f5f3ff; color: #6d28d9; border: 1px solid #ddd6fe; }
    .theme-purple .etf-exposure-badge { background: #ede9fe; color: #5b21b6; }

    .theme-cyan { border-top: 5px solid #0284c7; }
    .theme-cyan .badge-category { background: #f0f9ff; color: #0369a1; border: 1px solid #bae6fd; }
    .theme-cyan .etf-exposure-badge { background: #e0f2fe; color: #075985; }

    .theme-teal { border-top: 5px solid #0d9488; }
    .theme-teal .badge-category { background: #f0fdfa; color: #0f766e; border: 1px solid #99f6e4; }
    .theme-teal .etf-exposure-badge { background: #ccfbf1; color: #115e59; }

    .theme-amber { border-top: 5px solid #d97706; }
    .theme-amber .badge-category { background: #fffbeb; color: #b45309; border: 1px solid #fde68a; }
    .theme-amber .etf-exposure-badge { background: #fef3c7; color: #92400e; }

    .theme-orange { border-top: 5px solid #ea580c; }
    .theme-orange .badge-category { background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; }
    .theme-orange .etf-exposure-badge { background: #ffedd5; color: #9a3412; }

    .theme-rose { border-top: 5px solid #e11d48; }
    .theme-rose .badge-category { background: #fff1f2; color: #be123c; border: 1px solid #fecdd3; }
    .theme-rose .etf-exposure-badge { background: #ffe4e6; color: #9f1239; }

    /* SPECIAL WARNING CALLOUT BOX */
    .warning-box {
      background: #fff5f5;
      border: 1.5px solid #fca5a5;
      border-radius: 16px;
      padding: 22px 26px;
      margin-top: 10px;
    }
    .warning-header {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #b91c1c;
      font-size: 16px;
      font-weight: 800;
      margin-bottom: 8px;
    }
    .warning-content {
      font-size: 13.5px;
      color: #4b5563;
      line-height: 1.6;
    }

    /* LIFECYCLE 3-PHASE MATRIX */
    .lifecycle-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .lifecycle-card {
      background: #f8fafc;
      border: 1.5px solid #e2e8f0;
      border-radius: 20px;
      padding: 28px 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .lifecycle-tag {
      font-family: 'Outfit', sans-serif;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 8px;
      align-self: flex-start;
    }
    .tag-phase1 { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
    .tag-phase2 { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
    .tag-phase3 { background: #fdf4ff; color: #86198f; border: 1px solid #f5d0fe; }

    .lifecycle-title {
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
    }
    .lifecycle-target-user {
      font-size: 13px;
      color: #64748b;
      margin-top: 2px;
    }
    .lifecycle-goal {
      background: #ffffff;
      padding: 12px 14px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      font-size: 13px;
      color: #334155;
      font-weight: 600;
    }
    .portfolio-bars {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }
    .p-bar-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .p-bar-labels {
      display: flex;
      justify-content: space-between;
      font-size: 12.5px;
      font-weight: 700;
      color: #334155;
    }
    .p-bar-track {
      height: 9px;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
    }
    .p-bar-fill {
      height: 100%;
      border-radius: 9999px;
    }

    /* 5 GOLDEN RULES */
    .rules-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
    }
    .rule-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 22px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .rule-num {
      width: 32px;
      height: 32px;
      border-radius: 10px;
      background: #0f172a;
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
      background: #0f172a;
      color: #94a3b8;
      padding: 26px 70px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      border-top: 1px solid #1e293b;
    }
    .footer-left {
      display: flex;
      gap: 18px;
      align-items: center;
    }
    .footer-badge {
      color: #38bdf8;
      font-weight: 700;
    }
  </style>
</head>
<body>

<div class="infographic-wrapper">
  
  <!-- 1. HERO HEADER -->
  <header class="hero-header">
    <div class="hero-tag-row">
      <div class="firm-badge">
        <span>🏛️</span> DADAIC Investment Firm | Master Research
      </div>
      <div class="doc-meta">
        Strict USD Benchmark | Comprehensive Retirement Blueprint
      </div>
    </div>
    <h1 class="hero-title">은퇴 대비 핵심 ETF 26선 완전 분석 인포그래픽</h1>
    <p class="hero-subtitle">
      장기 자본 복리(Growth), 지속 가능한 배당 인컴(Cash Flow), 그리고 시스템 붕괴를 막는 안전판(Preservation)을 완성하는 8대 자산배분 클러스터 및 생애주기별 실전 포트폴리오 로드맵.
    </p>
  </header>

  <!-- 2. KEY STATS AT A GLANCE -->
  <div class="stats-bar">
    <div class="stat-pill">
      <div class="stat-label">분석 대상 ETF</div>
      <div class="stat-value">26종</div>
      <div class="stat-desc">검증된 글로벌 기관급 라인업</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">자산배분 축</div>
      <div class="stat-value">8개 클러스터</div>
      <div class="stat-desc">시장/배당/성장/채권/해외/리츠/소형/옵션</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">생애주기 모델</div>
      <div class="stat-value">3단계 Matrix</div>
      <div class="stat-desc">축적기 ➔ 전환기 ➔ 인컴수령기</div>
    </div>
    <div class="stat-pill">
      <div class="stat-label">운용 통화 원칙</div>
      <div class="stat-value">Strict USD ($)</div>
      <div class="stat-desc">환율 왜곡 배제 · 순수 달러 복리</div>
    </div>
  </div>

  <div class="content-container">

    <!-- 3. RETIREMENT ASSET ALLOCATION PYRAMID -->
    <section>
      <div class="section-headline">
        <div class="section-icon">🏛️</div>
        <div class="section-title-text">
          <h3>은퇴 자산 배분 5층 피라미드 (Asset Allocation Pyramid)</h3>
          <p>어떤 금융 위기가 닥쳐도 계좌가 영구 파산하지 않는 계층별 포트폴리오 적층 구조</p>
        </div>
      </div>

      <div class="pyramid-card">
        <div class="pyramid-tiers">
          <!-- Tier 5 -->
          <div class="tier-row tier-5">
            <div class="tier-left">
              <span class="tier-rank">TIER 5</span>
              <span class="tier-name">성장 가속 & 테크 알파 (Satellite Growth)</span>
              <span class="tier-etfs">QQQM · VUG · VGT · SMH</span>
            </div>
            <div class="tier-right">
              <span class="tier-role">초과 수익 창출 & 기술 메가트렌드</span>
              <span class="tier-weight">5 ~ 15%</span>
            </div>
          </div>

          <!-- Tier 4 -->
          <div class="tier-row tier-4">
            <div class="tier-left">
              <span class="tier-rank">TIER 4</span>
              <span class="tier-name">보완 분산 & 인플레 헤지 (Diversifiers)</span>
              <span class="tier-etfs">VEA · VWO · VXUS · IJR · VB · VNQ · XLRE · GLDM · SLV</span>
            </div>
            <div class="tier-right">
              <span class="tier-role">비미국·실물 자산·소형주 팩터 분산</span>
              <span class="tier-weight">10 ~ 20%</span>
            </div>
          </div>

          <!-- Tier 3 -->
          <div class="tier-row tier-3">
            <div class="tier-left">
              <span class="tier-rank">TIER 3</span>
              <span class="tier-name">우량 배당성장 엔진 (Dividend Compounder)</span>
              <span class="tier-etfs">SCHD · VIG · VYM</span>
            </div>
            <div class="tier-right">
              <span class="tier-role">인플레이션을 능가하는 현금흐름 증액</span>
              <span class="tier-weight">20 ~ 35%</span>
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="tier-row tier-2">
            <div class="tier-left">
              <span class="tier-rank">TIER 2</span>
              <span class="tier-name">미국 & 글로벌 핵심 코어 (Broad Market Core)</span>
              <span class="tier-etfs">VOO · VTI · VT</span>
            </div>
            <div class="tier-right">
              <span class="tier-role">자본주의 장기 우상향 복리의 닻</span>
              <span class="tier-weight">25 ~ 45%</span>
            </div>
          </div>

          <!-- Tier 1 -->
          <div class="tier-row tier-1">
            <div class="tier-left">
              <span class="tier-rank">TIER 1</span>
              <span class="tier-name">안전판 & 비상 유동성 버퍼 (Liquidity & Bonds)</span>
              <span class="tier-etfs">SGOV · IEF · BND · TLT</span>
            </div>
            <div class="tier-right">
              <span class="tier-role">하락장 주식 강제 매도 방지 (1~2년 생활비)</span>
              <span class="tier-weight">10 ~ 25%</span>
            </div>
          </div>
        </div>
        <div style="margin-top: 18px; font-size: 13px; color: #64748b; text-align: center;">
          * 주의: ⚠️ 고배당 커버드콜군(JEPI, JEPQ, DIVO)은 원금 복리를 제한하므로 기본 형성기 피라미드에서 제외되며, 은퇴 직후 인컴 수령기에 한해 5~10% 이내 전술적 편입을 권장합니다.
        </div>
      </div>
    </section>

    <!-- 4. 8 CLUSTERS - ALL 26 ETFS DIRECTORY -->
    <section>
      <div class="section-headline">
        <div class="section-icon">📊</div>
        <div class="section-title-text">
          <h3>8대 자산배분 클러스터 및 26개 ETF 정밀 해부</h3>
          <p>각 ETF의 명확한 역할, 노출 자산, 핵심 강점 및 은퇴 포트폴리오 내 적합성 평가</p>
        </div>
      </div>

      <div class="clusters-grid">

        <!-- CLUSTER 1: U.S. CORE MARKET -->
        <div class="cluster-card theme-blue">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">🇺🇸</span>
              <div>
                <div class="cluster-title">1. 미국 & 글로벌 핵심 코어 (Core Market)</div>
                <div class="cluster-desc">장기 자본 복리의 근간이 되는 최저비용 광범위 시장 지수</div>
              </div>
            </div>
            <span class="badge-category">코어 앵커 (Core)</span>
          </div>
          <div class="etf-list">
            <!-- 1. VOO -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#01</span>
                  <span class="ticker-tag">VOO</span>
                  <span class="etf-name">Vanguard S&P 500 ETF</span>
                </div>
                <span class="etf-exposure-badge">U.S. LARGE CAP</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">미국 대표 500대 우량주 압축. 연 보수 0.03%의 최상급 효율. 워런 버핏 추천 1순위.</div>
                <span class="etf-target">전 생애주기 필수</span>
              </div>
            </div>
            <!-- 2. VTI -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#02</span>
                  <span class="ticker-tag">VTI</span>
                  <span class="etf-name">Vanguard Total Stock Market ETF</span>
                </div>
                <span class="etf-exposure-badge">U.S. TOTAL MARKET</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">대형·중형·소형주 3,700여 개 전체 편입. 미국 경제 전체에 베팅하는 완벽한 시장 중립.</div>
                <span class="etf-target">올라운드 기본형</span>
              </div>
            </div>
            <!-- 3. VT -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#03</span>
                  <span class="ticker-tag">VT</span>
                  <span class="etf-name">Vanguard Total World Stock ETF</span>
                </div>
                <span class="etf-exposure-badge">GLOBAL ALL-CAP</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">미국(60%) + 비미국 선진·신흥국(40%) 전 세계 9,800+ 주식 통합. 궁극의 글로벌 올인원.</div>
                <span class="etf-target">글로벌 무손실 분산</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 2: DIVIDEND GROWTH -->
        <div class="cluster-card theme-green">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">💵</span>
              <div>
                <div class="cluster-title">2. 우량 배당성장 & 가치 인컴 (Dividend Growth)</div>
                <div class="cluster-desc">물가상승을 능가하는 현금흐름과 우량 펀더멘털을 겸비한 복리 머신</div>
              </div>
            </div>
            <span class="badge-category">현금흐름 (Cash Flow)</span>
          </div>
          <div class="etf-list">
            <!-- 4. SCHD -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#04</span>
                  <span class="ticker-tag">SCHD</span>
                  <span class="etf-name">Schwab U.S. Dividend Equity ETF</span>
                </div>
                <span class="etf-exposure-badge">DIVIDEND GROWTH</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">10년 연속 배당+ROE 27%+부채건전성 엄선 100종목. 연 3.2% 배당 + 연 10%+ 배당성장률.</div>
                <span class="etf-target">은퇴 포트폴리오의 심장</span>
              </div>
            </div>
            <!-- 5. VIG -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#05</span>
                  <span class="ticker-tag">VIG</span>
                  <span class="etf-name">Vanguard Dividend Appreciation ETF</span>
                </div>
                <span class="etf-exposure-badge">DIVIDEND FOCUS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">10년 이상 연속 배당 증액 기업 300여 개. 테크·헬스케어 비중이 높아 자본 성장 탄력 우수.</div>
                <span class="etf-target">성장+배당 하이브리드</span>
              </div>
            </div>
            <!-- 6. VYM -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#06</span>
                  <span class="ticker-tag">VYM</span>
                  <span class="etf-name">Vanguard High Dividend Yield ETF</span>
                </div>
                <span class="etf-exposure-badge">HIGH DIVIDEND</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">FTSE 고배당 지수 추종 450+ 종목. 금융·에너지·필수소비재 비중 높은 클래식 가치주 인컴.</div>
                <span class="etf-target">안정적 즉시 인컴</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 3: GROWTH & TECH ALPHA -->
        <div class="cluster-card theme-purple">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">🚀</span>
              <div>
                <div class="cluster-title">3. 성장 가속 & 테크 메가트렌드 (Growth & Tech)</div>
                <div class="cluster-desc">자산 축적기(2040) 총자산 증식을 극대화하는 메가트렌드 엔진</div>
              </div>
            </div>
            <span class="badge-category">성장 엔진 (Growth)</span>
          </div>
          <div class="etf-list">
            <!-- 14. QQQM -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#14</span>
                  <span class="ticker-tag">QQQM</span>
                  <span class="etf-name">Invesco NASDAQ 100 ETF</span>
                </div>
                <span class="etf-exposure-badge">U.S. LARGE CAP TECH</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">나스닥 100 우량 비금융 혁신 기업. QQQ 대비 낮은 보수(0.15%)로 장기 적립에 최적.</div>
                <span class="etf-target">청장년기 적립 필수</span>
              </div>
            </div>
            <!-- 15. VUG -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#15</span>
                  <span class="ticker-tag">VUG</span>
                  <span class="etf-name">Vanguard Growth ETF</span>
                </div>
                <span class="etf-exposure-badge">LARGE CAP GROWTH</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">CRSP 대형 성장주 지수. 테크뿐 아니라 소비재·통신 성장주까지 넓게 포괄 (보수 0.04%).</div>
                <span class="etf-target">광범위 대형 성장주</span>
              </div>
            </div>
            <!-- 16. VGT -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#16</span>
                  <span class="ticker-tag">VGT</span>
                  <span class="etf-name">Vanguard Information Technology ETF</span>
                </div>
                <span class="etf-exposure-badge">PURE TECH</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">소프트웨어, 하드웨어, 반도체 등 순수 IT 섹터 300+ 기업 압축. 가장 순도 높은 기술주 베타.</div>
                <span class="etf-target">테크 집중 초과수익</span>
              </div>
            </div>
            <!-- 26. SMH -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#26</span>
                  <span class="ticker-tag">SMH</span>
                  <span class="etf-name">VanEck Semiconductor ETF</span>
                </div>
                <span class="etf-exposure-badge">SEMICONDUCTORS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">엔비디아, TSMC, ASML 등 글로벌 25대 반도체 독점 지배기업 집중. AI 인프라 최강 수혜.</div>
                <span class="etf-target">슈퍼 메가트렌드 위성</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 4: FIXED INCOME & LIQUIDITY -->
        <div class="cluster-card theme-cyan">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">🛡️</span>
              <div>
                <div class="cluster-title">4. 채권 & 비상 유동성 안전판 (Fixed Income)</div>
                <div class="cluster-desc">하락장에서도 주식을 팔지 않고 버티게 해주는 원금 보존 및 비상금 밸러스트</div>
              </div>
            </div>
            <span class="badge-category">자본 보존 (Preservation)</span>
          </div>
          <div class="etf-list">
            <!-- 7. SGOV -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#07</span>
                  <span class="ticker-tag">SGOV</span>
                  <span class="etf-name">iShares 0-3 Month Treasury Bond ETF</span>
                </div>
                <span class="etf-exposure-badge">CASH / T-BILLS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">0~3개월 미국 초단기 국채. 금리 변동 위험 제로에 수렴. 1~2년 생활비 파킹 및 매수 대기 자금.</div>
                <span class="etf-target">최고의 무위험 파킹통장</span>
              </div>
            </div>
            <!-- 8. IEF -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#08</span>
                  <span class="ticker-tag">IEF</span>
                  <span class="etf-name">iShares 7-10 Year Treasury Bond ETF</span>
                </div>
                <span class="etf-exposure-badge">INTERMEDIATE BONDS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">7~10년 중기 미국 국채. 적절한 듀레이션(약 7년)으로 주식 시장 급락 시 반등 탄력 제공.</div>
                <span class="etf-target">표준 자산배분 채권</span>
              </div>
            </div>
            <!-- 9. BND -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#09</span>
                  <span class="ticker-tag">BND</span>
                  <span class="etf-name">Vanguard Total Bond Market ETF</span>
                </div>
                <span class="etf-exposure-badge">TOTAL BOND MARKET</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">미국 국채(65%) + 우량 회사채(25%) + MBS 종합 채권. 월배당 제공 및 극강의 분산 효과.</div>
                <span class="etf-target">올웨더 종합 채권</span>
              </div>
            </div>
            <!-- 10. TLT -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#10</span>
                  <span class="ticker-tag">TLT</span>
                  <span class="etf-name">iShares 20+ Year Treasury Bond ETF</span>
                </div>
                <span class="etf-exposure-badge">LONG-TERM BONDS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">20년+ 미국 초장기 국채. 경기침체/블랙스완 발생 시 주식 폭락을 방어하는 가장 강력한 헤지 수단.</div>
                <span class="etf-target">위기 방어 전술 헤지</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 5: GLOBAL EX-U.S. -->
        <div class="cluster-card theme-teal">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">🌐</span>
              <div>
                <div class="cluster-title">5. 글로벌 다각화 (Global Ex-U.S. Markets)</div>
                <div class="cluster-desc">미국 단일 국가 밸류에이션 부담 및 달러 약세 국면을 보완하는 인터내셔널 자산</div>
              </div>
            </div>
            <span class="badge-category">글로벌 분산 (Ex-US)</span>
          </div>
          <div class="etf-list">
            <!-- 11. VEA -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#11</span>
                  <span class="ticker-tag">VEA</span>
                  <span class="etf-name">Vanguard FTSE Developed Markets ETF</span>
                </div>
                <span class="etf-exposure-badge">DEVELOPED EX-U.S.</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">유럽, 일본, 영국, 캐나다 등 미국 외 선진국 4,000+ 기업. 안정적인 배당과 저평가 밸류에이션.</div>
                <span class="etf-target">선진국 분산 밸러스트</span>
              </div>
            </div>
            <!-- 12. VWO -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#12</span>
                  <span class="ticker-tag">VWO</span>
                  <span class="etf-name">Vanguard FTSE Emerging Markets ETF</span>
                </div>
                <span class="etf-exposure-badge">EMERGING MARKETS</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">대만, 인도, 중국, 브라질 등 5,000+ 신흥국 기업. 인구 구조와 신흥 경제 성장 수혜.</div>
                <span class="etf-target">신흥국 성장 알파</span>
              </div>
            </div>
            <!-- 13. VXUS -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#13</span>
                  <span class="ticker-tag">VXUS</span>
                  <span class="etf-name">Vanguard Total International Stock ETF</span>
                </div>
                <span class="etf-exposure-badge">TOTAL EX-U.S.</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">미국을 제외한 전 세계 8,500+ 종목(선진국 75% + 신흥국 25%). 비미국 주식 시장 완전 정복.</div>
                <span class="etf-target">인터내셔널 올인원</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 6: REAL ESTATE & COMMODITIES -->
        <div class="cluster-card theme-amber">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">🏢</span>
              <div>
                <div class="cluster-title">6. 부동산 리츠 & 실물 원자재 (Real Assets)</div>
                <div class="cluster-desc">화폐 가치 하락과 스태그플레이션 환경에서 실물 가치를 보전하는 인플레 헤지</div>
              </div>
            </div>
            <span class="badge-category">인플레 헤지 (Real Assets)</span>
          </div>
          <div class="etf-list">
            <!-- 20. VNQ -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#20</span>
                  <span class="ticker-tag">VNQ</span>
                  <span class="etf-name">Vanguard Real Estate ETF</span>
                </div>
                <span class="etf-exposure-badge">REAL ESTATE</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">미국 상업용, 주거용, 데이터센터, 물류센터 리츠 160+ 개사. 임대료 상승 연동형 고배당.</div>
                <span class="etf-target">부동산 간접 실물 소유</span>
              </div>
            </div>
            <!-- 21. XLRE -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#21</span>
                  <span class="ticker-tag">XLRE</span>
                  <span class="etf-name">Real Estate Select Sector SPDR Fund</span>
                </div>
                <span class="etf-exposure-badge">REIT SECTOR</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">S&P 500에 편입된 미국 최정상급 30대 메가 리츠만 압축. 우량 대형 부동산 위주 구성.</div>
                <span class="etf-target">대형 리츠 섹터 집중</span>
              </div>
            </div>
            <!-- 22. GLDM -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#22</span>
                  <span class="ticker-tag">GLDM</span>
                  <span class="etf-name">SPDR Gold MiniShares Trust</span>
                </div>
                <span class="etf-exposure-badge">GOLD</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">금 실물 보관 기반. GLD 대비 1/4 수준의 최저 운용보수(0.10%). 달러 가치 희석 및 지정학 방패.</div>
                <span class="etf-target">불변의 안전자산</span>
              </div>
            </div>
            <!-- 23. SLV -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#23</span>
                  <span class="ticker-tag">SLV</span>
                  <span class="etf-name">iShares Silver Trust</span>
                </div>
                <span class="etf-exposure-badge">SILVER</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">은 실물 보유 ETF. 통화 가치 저장 수단이자 태양광/반도체/AI 전력 인프라 산업재 수요 겸비.</div>
                <span class="etf-target">원자재 성장 탄력</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 7: U.S. SMALL CAP -->
        <div class="cluster-card theme-orange">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">📈</span>
              <div>
                <div class="cluster-title">7. 팩터 보완: 미국 중소형주 (Small-Cap Factor)</div>
                <div class="cluster-desc">대형주 편중을 탈피하고 경기 회복기 강력한 초과 수익률을 창출하는 크기(Size) 팩터</div>
              </div>
            </div>
            <span class="badge-category">팩터 알파 (Small-Cap)</span>
          </div>
          <div class="etf-list">
            <!-- 24. IJR -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#24</span>
                  <span class="ticker-tag">IJR</span>
                  <span class="etf-name">iShares Core S&P Small-Cap ETF</span>
                </div>
                <span class="etf-exposure-badge">U.S. SMALL CAP</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">S&P 600 지수 추종. 4분기 연속 흑자 기업만 편입하여 부실 좀비기업 배제 (IWM 대비 우수).</div>
                <span class="etf-target">실적 검증 우량 소형주</span>
              </div>
            </div>
            <!-- 25. VB -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#25</span>
                  <span class="ticker-tag">VB</span>
                  <span class="etf-name">Vanguard Small-Cap ETF</span>
                </div>
                <span class="etf-exposure-badge">U.S. SMALL CAP</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">CRSP 소형주 지수 추종 1,400+ 종목. 낮은 보수(0.05%)로 미국 중소형주 전반을 완전 커버.</div>
                <span class="etf-target">광범위 중소형 익스포저</span>
              </div>
            </div>
          </div>
        </div>

        <!-- CLUSTER 8: COVERED CALL (SPECIAL WARNING) -->
        <div class="cluster-card theme-rose">
          <div class="cluster-header">
            <div class="cluster-title-wrap">
              <span class="cluster-icon">⚠️</span>
              <div>
                <div class="cluster-title">8. 고배당 커버드콜 & 옵션 인컴 (Covered Call)</div>
                <div class="cluster-desc">높은 분배율을 제공하지만 원금 상승이 제한되는 비대칭 구조의 특수 인컴형</div>
              </div>
            </div>
            <span class="badge-category">주의 요망 (Tactical)</span>
          </div>
          <div class="etf-list">
            <!-- 17. DIVO -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#17</span>
                  <span class="ticker-tag">DIVO</span>
                  <span class="etf-name">Amplify C-PACE / Enhanced Dividend ETF</span>
                </div>
                <span class="etf-exposure-badge">⚠️ COVERED CALL</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">우량 배당성장주 20~25개 선별 + 개별 종목 콜옵션 부분 매도. 원금 상승 참여율이 가장 양호.</div>
                <span class="etf-target">배당성장형 옵션 인컴</span>
              </div>
            </div>
            <!-- 18. JEPI -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#18</span>
                  <span class="ticker-tag">JEPI</span>
                  <span class="etf-name">JPMorgan Equity Premium Income ETF</span>
                </div>
                <span class="etf-exposure-badge">⚠️ COVERED CALL</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">S&P 500 저변동성 주식 + ELN 콜옵션 매도 프리미엄. 연 7~8% 월배당. 횡보장에서 최적.</div>
                <span class="etf-target">은퇴 직후 월 생활비 보조</span>
              </div>
            </div>
            <!-- 19. JEPQ -->
            <div class="etf-item">
              <div class="etf-item-top">
                <div class="etf-ticker-group">
                  <span class="etf-num">#19</span>
                  <span class="ticker-tag">JEPQ</span>
                  <span class="etf-name">JPMorgan Nasdaq Equity Premium Income</span>
                </div>
                <span class="etf-exposure-badge">⚠️ COVERED CALL</span>
              </div>
              <div class="etf-item-bot">
                <div class="etf-features">나스닥 100 대형주 + ELN 옵션 프리미엄. 연 9~11% 고배당 제공하나 기술주 대세상승기 소외.</div>
                <span class="etf-target">초고인컴 현금흐름</span>
              </div>
            </div>
          </div>

          <!-- SPECIAL WARNING BOX -->
          <div class="warning-box">
            <div class="warning-header">
              <span>🚨</span> 커버드콜 상품 투자 시 은퇴자 필수 경고 지침
            </div>
            <div class="warning-content">
              커버드콜은 <strong>'상승 폭은 콜옵션 매도로 잘려나가고(Capped upside), 하락 폭은 고스란히 노출되는(Uncapped downside)'</strong> 비대칭 구조를 갖습니다. 따라서 <strong>원금을 불려야 하는 '축적기' 투자자에게는 절대 비권장</strong>하며, 은퇴 후 즉각적인 월 고정 생활비가 필요한 '수령기'에 한해서만 포트폴리오의 <strong>최대 5~10% 이내</strong>로 엄격히 통제하여 편입해야 합니다.
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 5. 3-STAGE RETIREMENT LIFECYCLE BLUEPRINT -->
    <section>
      <div class="section-headline">
        <div class="section-icon">🎯</div>
        <div class="section-title-text">
          <h3>은퇴 생애주기별 3단계 최적 포트폴리오 모델 (Lifecycle Models)</h3>
          <p>연령과 은퇴 시점에 맞추어 위험 자산과 인컴 자산의 황금 비율을 재조정하는 실전 공식</p>
        </div>
      </div>

      <div class="lifecycle-grid">
        
        <!-- PHASE 1 -->
        <div class="lifecycle-card">
          <span class="lifecycle-tag tag-phase1">PHASE 1 : 자산 축적기</span>
          <div>
            <div class="lifecycle-title">최대 자본 복리 증식형</div>
            <div class="lifecycle-target-user">20대 ~ 40대 중반 (은퇴 15년+ 전)</div>
          </div>
          <div class="lifecycle-goal">
            목표: 주가 변동성을 견디며 장기 복리 성장(Growth) 극대화. 배당 재투자 100%.
          </div>
          <div class="portfolio-bars">
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>미국 코어 (VOO / VTI)</span><span>45%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 45%; background: #2563eb;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>성장 & 테크 (QQQM / SMH)</span><span>25%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 25%; background: #7c3aed;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>배당성장 앵커 (SCHD / VIG)</span><span>15%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 15%; background: #059669;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>글로벌 / 소형주 (VXUS / IJR)</span><span>10%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 10%; background: #0d9488;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>현금 / 비상금 (SGOV)</span><span>5%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 5%; background: #64748b;"></div></div>
            </div>
          </div>
          <div style="font-size: 12.5px; color: #475569; border-top: 1px dashed #cbd5e1; padding-top: 10px;">
            💡 핵심: 커버드콜 완전 배제. 하락장에 흔들리지 않고 매달 적립식 복리 엔진 가동.
          </div>
        </div>

        <!-- PHASE 2 -->
        <div class="lifecycle-card">
          <span class="lifecycle-tag tag-phase2">PHASE 2 : 은퇴 전환기</span>
          <div>
            <div class="lifecycle-title">균형 성장 & 인컴 전환형</div>
            <div class="lifecycle-target-user">40대 후반 ~ 50대 (은퇴 5~10년 전)</div>
          </div>
          <div class="lifecycle-goal">
            목표: 급격한 하락장(MDD) 방어 및 안정적 배당 파이프라인 구축.
          </div>
          <div class="portfolio-bars">
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>배당성장 (SCHD / VIG)</span><span>35%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 35%; background: #059669;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>미국 코어 (VOO)</span><span>25%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 25%; background: #2563eb;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>중기 국채 & 종합채권 (BND / IEF)</span><span>20%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 20%; background: #0284c7;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>빅테크 성장주 (QQQM)</span><span>10%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 10%; background: #7c3aed;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>금 & 단기채 (GLDM / SGOV)</span><span>10%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 10%; background: #d97706;"></div></div>
            </div>
          </div>
          <div style="font-size: 12.5px; color: #475569; border-top: 1px dashed #cbd5e1; padding-top: 10px;">
            💡 핵심: 고변동 테크 비중을 줄이고 SCHD 및 채권 비중을 늘려 시퀀스 오브 리턴 리스크 차단.
          </div>
        </div>

        <!-- PHASE 3 -->
        <div class="lifecycle-card">
          <span class="lifecycle-tag tag-phase3">PHASE 3 : 은퇴 수령기</span>
          <div>
            <div class="lifecycle-title">월현금흐름 & 자본 보존형</div>
            <div class="lifecycle-target-user">60대 이후 (은퇴 후 생활비 수령기)</div>
          </div>
          <div class="lifecycle-goal">
            목표: 주식 원금을 헐값 매도하지 않고 배당금과 이자만으로 은퇴 생활비 100% 충당.
          </div>
          <div class="portfolio-bars">
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>고배당 & 배당성장 (SCHD / VYM)</span><span>35%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 35%; background: #059669;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>초단기채 파킹 (SGOV 1~2년 생활비)</span><span>20%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 20%; background: #0284c7;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>미국 코어 (VOO 인플레 방어)</span><span>15%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 15%; background: #2563eb;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>중장기 국채 (IEF / TLT)</span><span>15%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 15%; background: #475569;"></div></div>
            </div>
            <div class="p-bar-item">
              <div class="p-bar-labels"><span>옵션 인컴 / 리츠 (DIVO / JEPI / VNQ)</span><span>15%</span></div>
              <div class="p-bar-track"><div class="p-bar-fill" style="width: 15%; background: #e11d48;"></div></div>
            </div>
          </div>
          <div style="font-size: 12.5px; color: #475569; border-top: 1px dashed #cbd5e1; padding-top: 10px;">
            💡 핵심: SGOV 2년 치 생활비 버퍼 덕분에 어떤 대폭락장이 와도 주식을 손절할 필요가 없음.
          </div>
        </div>

      </div>
    </section>

    <!-- 6. 5 GOLDEN RULES FOR RETIREMENT INVESTING -->
    <section>
      <div class="section-headline">
        <div class="section-icon">⚖️</div>
        <div class="section-title-text">
          <h3>은퇴 ETF 포트폴리오 성공을 위한 5대 불변 원칙 (Institutional Rules)</h3>
          <p>기관 투자자들이 자산을 수십 년간 안전하게 복리 증식시키는 절대적 원칙</p>
        </div>
      </div>

      <div class="rules-grid">
        <div class="rule-card">
          <div class="rule-num">1</div>
          <div class="rule-title">총보수율 0.1%의 기적</div>
          <div class="rule-text">
            VOO(0.03%), VTI(0.03%) 등 초저보수 상품을 활용하세요. 연 1%의 수수료 차이는 30년 후 자산의 25% 이상을 갉아먹습니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">2</div>
          <div class="rule-title">'가짜 다각화'의 덫 경계</div>
          <div class="rule-text">
            VOO + VTI + QQQM + VGT를 동시에 사면 종목이 많아 보이지만, 실제로는 엔비디아·애플·MS 등 상위 빅테크 중복 몰빵에 불과합니다.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">3</div>
          <div class="rule-title">2년 치 생활비 SGOV 버퍼</div>
          <div class="rule-text">
            은퇴 직후 주식 시장이 -30% 폭락해도 주식을 헐값에 매도하지 않도록, 반드시 1~2년 치 순생활비는 SGOV 등 초단기 국채로 방어하세요.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">4</div>
          <div class="rule-title">고배당률의 착시 탈피</div>
          <div class="rule-text">
            JEPI, JEPQ의 연 8~10% 분배율만 보지 말고, 원금 하락을 감안한 '총수익률(Total Return)'을 반드시 백테스팅하고 비중을 10% 이내로 제한하세요.
          </div>
        </div>
        <div class="rule-card">
          <div class="rule-num">5</div>
          <div class="rule-title">연 1회 기계적 리밸런싱</div>
          <div class="rule-text">
            시장 폭등기에는 많이 오른 테크주를 덜어내고, 폭락기에는 떨어진 주식을 채권 이자로 사들이는 캘린더 리밸런싱을 감정 없이 실행하세요.
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
      <span>은퇴 포트폴리오 자산배분 연구보고서</span>
      <span>|</span>
      <span>Strict USD Accounting Standard</span>
    </div>
    <div>
      Document ID: DADAIC-INFOGRAPHIC-RETIREMENT-26ETF-261005
    </div>
  </footer>

</div>

</body>
</html>
"""

def generate_files():
    html_path = os.path.join(MEDIA_DIR, "Retirement-ETF-Master-Infographic.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[+] Saved HTML: {html_path}")

    # Copy HTML to artifact scratch
    artifact_html = os.path.join(ARTIFACT_DIR, "Retirement-ETF-Master-Infographic.html")
    shutil.copy(html_path, artifact_html)

    # Render PNG with Chrome Headless
    png_path = os.path.join(MEDIA_DIR, "Retirement-ETF-Master-Infographic.png")
    
    # We use a custom window size to ensure the entire graphic is captured crisply
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1500,5600",
        "--force-device-scale-factor=1.5",
        f"--screenshot={png_path}",
        html_path
    ]
    print(f"[*] Rendering PNG via Headless Chrome...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] Rendered PNG successfully: {png_path} ({os.path.getsize(png_path)} bytes)")
        # Copy to artifact folder for Antigravity preview
        artifact_png = os.path.join(ARTIFACT_DIR, "Retirement-ETF-Master-Infographic.png")
        shutil.copy(png_path, artifact_png)
        print(f"[+] Copied to Artifact: {artifact_png}")
    else:
        print(f"[-] Error rendering Chrome: {res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    generate_files()
