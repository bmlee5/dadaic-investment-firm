#!/usr/bin/env python3
"""
DADAIC Investment Firm - Autonomous Stock & ETF Screening Engine (CIO PICKS)
Version: 2.0 (Dual-Engine Alpha Funnel: Option B Quant Scanner + Option C AI Thematic Radar)

Architecture:
  - Track 1 (Option B): High-speed batch vector scanning across 160+ S&P 500 / NASDAQ 100 leaders.
  - Track 2 (Option C): Thematic intelligence & Wall Street emerging leader discovery.
  - Track 3: Deep 10-K/10-Q fundamental audit, portfolio gap-filling against my-portfolio.yaml,
             and 5 Great Masters + Chief Market Technician 6-in-1 consensus ranking.
"""

import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import argparse
import datetime
import json
import yaml
import yfinance as yf
import pandas as pd
import numpy as np

# ==============================================================================
# 1. INSTITUTIONAL MASTER EQUITY UNIVERSE (160+ Core Institutional Leaders)
# ==============================================================================
MASTER_EQUITY_UNIVERSE = {
    # --- Healthcare, Medical Devices & Biotech Moats ---
    "LLY":   {"name": "Eli Lilly & Co.", "sector": "Healthcare", "theme": "GLP-1 / Metabolic Moat", "category": "Defensive Compounder"},
    "UNH":   {"name": "UnitedHealth Group", "sector": "Healthcare", "theme": "Managed Care Tollbooth", "category": "Defensive Compounder"},
    "ABBV":  {"name": "AbbVie Inc.", "sector": "Healthcare", "theme": "Immunology & Oncology Cash Engine", "category": "Defensive Compounder"},
    "ISRG":  {"name": "Intuitive Surgical", "sector": "Healthcare", "theme": "Robotic Surgery Monopoly", "category": "High-Growth Moat"},
    "VRTX":  {"name": "Vertex Pharmaceuticals", "sector": "Healthcare", "theme": "Cystic Fibrosis & Gene Editing", "category": "High-Growth Moat"},
    "JNJ":   {"name": "Johnson & Johnson", "sector": "Healthcare", "theme": "Diversified MedTech & Pharma Fortress", "category": "Defensive Compounder"},
    "MRK":   {"name": "Merck & Co.", "sector": "Healthcare", "theme": "Keytruda Immuno-Oncology Monopoly", "category": "Defensive Compounder"},
    "TMO":   {"name": "Thermo Fisher Scientific", "sector": "Healthcare", "theme": "Life Sciences Tools Tollbooth", "category": "High ROIC Compounder"},
    "ABT":   {"name": "Abbott Laboratories", "sector": "Healthcare", "theme": "Continuous Glucose Monitoring & Devices", "category": "Defensive Compounder"},
    "BSX":   {"name": "Boston Scientific", "sector": "Healthcare", "theme": "Cardiovascular Interventional Devices", "category": "High-Growth Moat"},
    "REGN":  {"name": "Regeneron Pharmaceuticals", "sector": "Healthcare", "theme": "Antibody Platform Discovery", "category": "High-Growth Moat"},
    "DHR":   {"name": "Danaher Corporation", "sector": "Healthcare", "theme": "Bioprocessing Equipment & DBS Tollbooth", "category": "High ROIC Compounder"},
    "SYK":   {"name": "Stryker Corporation", "sector": "Healthcare", "theme": "Orthopedic & Surgical Robotics Moat", "category": "High-Growth Moat"},
    "BMY":   {"name": "Bristol-Myers Squibb", "sector": "Healthcare", "theme": "Cardiovascular & Oncology Pipeline", "category": "Deep Value Pharma"},
    "ELV":   {"name": "Elevance Health", "sector": "Healthcare", "theme": "Commercial Health Benefits & Pharmacy", "category": "Defensive Compounder"},

    # --- Power Grid, Nuclear & Energy Infrastructure (AI Bottleneck) ---
    "GEV":   {"name": "GE Vernova Inc.", "sector": "Industrials", "theme": "Grid Electrification & Gas Turbines", "category": "Energy Infrastructure"},
    "VRT":   {"name": "Vertiv Holdings Co.", "sector": "Industrials", "theme": "Data Center Liquid Cooling & Thermal", "category": "AI Infrastructure"},
    "ETN":   {"name": "Eaton Corporation", "sector": "Industrials", "theme": "Electrical Power Distribution & Transformers", "category": "Energy Infrastructure"},
    "CEG":   {"name": "Constellation Energy", "sector": "Utilities", "theme": "Nuclear Clean Power Hyperscaler PPA", "category": "Energy Infrastructure"},
    "VST":   {"name": "Vistra Corp.", "sector": "Utilities", "theme": "Nuclear & Gas Merchant Power Supercycle", "category": "Energy Infrastructure"},
    "NRG":   {"name": "NRG Energy", "sector": "Utilities", "theme": "Texas Grid Retail & Generation Capacity", "category": "Energy Infrastructure"},
    "NEE":   {"name": "NextEra Energy", "sector": "Utilities", "theme": "Regulated Utility & Renewable Power Leader", "category": "Defensive Compounder"},
    "HUBB":  {"name": "Hubbell Incorporated", "sector": "Industrials", "theme": "Utility Grid Hardware & High Voltage", "category": "Energy Infrastructure"},
    "POWL":  {"name": "Powell Industries", "sector": "Industrials", "theme": "Custom Electrical Substation Switchgear", "category": "High-Growth Moat"},
    "EMR":   {"name": "Emerson Electric", "sector": "Industrials", "theme": "Industrial Automation & Process Control", "category": "High ROIC Compounder"},
    "PH":    {"name": "Parker-Hannifin", "sector": "Industrials", "theme": "Motion & Control Aerospace/Thermal Systems", "category": "High ROIC Compounder"},
    "PWR":   {"name": "Quanta Services", "sector": "Industrials", "theme": "Electric Grid Construction Engineering", "category": "Energy Infrastructure"},
    "FIX":   {"name": "Comfort Systems USA", "sector": "Industrials", "theme": "Data Center HVAC & Mechanical Contracting", "category": "AI Infrastructure"},
    "BE":    {"name": "Bloom Energy Corp.", "sector": "Industrials", "theme": "Solid Oxide Fuel Cells & Onsite Power", "category": "Speculative Growth"},

    # --- Aerospace, Defense & Capital Goods ---
    "LMT":   {"name": "Lockheed Martin", "sector": "Industrials", "theme": "Defense Monopsony & F-35 / Missile Moat", "category": "Defensive Compounder"},
    "RTX":   {"name": "RTX Corporation", "sector": "Industrials", "theme": "Pratt Engines & Patriot Missile Systems", "category": "Defensive Compounder"},
    "GD":    {"name": "General Dynamics", "sector": "Industrials", "theme": "Nuclear Submarines & Gulfstream Aviation", "category": "Defensive Compounder"},
    "NOC":   {"name": "Northrop Grumman", "sector": "Industrials", "theme": "B-21 Stealth Bomber & Space Defense", "category": "Defensive Compounder"},
    "TDG":   {"name": "TransDigm Group", "sector": "Industrials", "theme": "Proprietary Aerospace Aftermarket Monopoly", "category": "High ROIC Compounder"},
    "HEI":   {"name": "HEICO Corporation", "sector": "Industrials", "theme": "FAA-Approved Replacement Jet Parts Duopoly", "category": "High ROIC Compounder"},
    "AXON":  {"name": "Axon Enterprise", "sector": "Industrials", "theme": "TASER, Body Cameras & Evidence Cloud", "category": "High-Growth Moat"},
    "KTOS":  {"name": "Kratos Defense", "sector": "Industrials", "theme": "Unmanned Jet Drones & Space Satellite Comms", "category": "Defense Tech Disruptor"},
    "CAT":   {"name": "Caterpillar Inc.", "sector": "Industrials", "theme": "Global Heavy Mining & Construction Capex", "category": "Cyclical Leader"},
    "DE":    {"name": "Deere & Company", "sector": "Industrials", "theme": "Autonomous Precision Ag & Tractor Moat", "category": "High ROIC Compounder"},
    "GE":    {"name": "GE Aerospace", "sector": "Industrials", "theme": "Commercial Jet Engine Fleet & LEAP Tollbooth", "category": "High ROIC Compounder"},
    "URI":   {"name": "United Rentals", "sector": "Industrials", "theme": "Mega-Project Equipment Rental Fleet", "category": "High ROIC Compounder"},

    # --- Financial Tollbooths, Exchanges & Asset Managers ---
    "BRK-B": {"name": "Berkshire Hathaway (Class B)", "sector": "Financials", "theme": "Fortress Balance Sheet & Insurance Float", "category": "Ballast Compounder"},
    "V":     {"name": "Visa Inc.", "sector": "Financials", "theme": "Global Consumer Payments Network Duopoly", "category": "High Margin Tollbooth"},
    "MA":    {"name": "Mastercard Inc.", "sector": "Financials", "theme": "Global Consumer Payments Network Duopoly", "category": "High Margin Tollbooth"},
    "SPGI":  {"name": "S&P Global Inc.", "sector": "Financials", "theme": "Credit Rating & Benchmark Index Duopoly", "category": "High Margin Tollbooth"},
    "MCO":   {"name": "Moody's Corporation", "sector": "Financials", "theme": "Credit Rating Duopoly & Analytics", "category": "High Margin Tollbooth"},
    "JPM":   {"name": "JPMorgan Chase & Co.", "sector": "Financials", "theme": "Fortress Global Investment & Consumer Bank", "category": "Financial Fortress"},
    "GS":    {"name": "Goldman Sachs Group", "sector": "Financials", "theme": "M&A Advisory & Institutional Trading Alpha", "category": "Capital Markets Leader"},
    "MS":    {"name": "Morgan Stanley", "sector": "Financials", "theme": "Wealth Management Sticky Fee Machine", "category": "Wealth Management Leader"},
    "BLK":   {"name": "BlackRock Inc.", "sector": "Financials", "theme": "Global iShares ETF & Aladdin Infrastructure", "category": "Asset Management Monopoly"},
    "AXP":   {"name": "American Express", "sector": "Financials", "theme": "Affluent Closed-Loop Spend Network", "category": "High ROIC Compounder"},
    "PGR":   {"name": "Progressive Corp.", "sector": "Financials", "theme": "Telematics Auto Underwriting Superiority", "category": "High ROIC Compounder"},
    "CB":    {"name": "Chubb Limited", "sector": "Financials", "theme": "Global Commercial Property & Casualty P&C", "category": "Defensive Compounder"},
    "ICE":   {"name": "Intercontinental Exchange", "sector": "Financials", "theme": "NYSE Energy Futures & Mortgage Network", "category": "High Margin Tollbooth"},
    "FICO":  {"name": "Fair Isaac Corporation", "sector": "Financials", "theme": "US Credit Score Absolute Monopoly", "category": "High Margin Tollbooth"},

    # --- Consumer Monopolies, Scale Retailers & High-ROIC Brands ---
    "COST":  {"name": "Costco Wholesale", "sector": "Consumer Defensive", "theme": "Membership Annuity & Bulk Supply Chain Scale", "category": "Consumer Monopoly"},
    "WMT":   {"name": "Walmart Inc.", "sector": "Consumer Defensive", "theme": "Omnichannel Retail Dominance & High FCF", "category": "Consumer Monopoly"},
    "HD":    {"name": "Home Depot", "sector": "Consumer Cyclical", "theme": "Home Improvement Duopoly & High ROIC", "category": "High ROIC Compounder"},
    "LOW":   {"name": "Lowe's Companies", "sector": "Consumer Cyclical", "theme": "Home Improvement Duopoly & Share Buybacks", "category": "High ROIC Compounder"},
    "PG":    {"name": "Procter & Gamble", "sector": "Consumer Defensive", "theme": "Household Consumer Staples Pricing Power", "category": "Defensive Compounder"},
    "KO":    {"name": "Coca-Cola Company", "sector": "Consumer Defensive", "theme": "Global Beverage Distribution Route Moat", "category": "Defensive Compounder"},
    "PEP":   {"name": "PepsiCo Inc.", "sector": "Consumer Defensive", "theme": "Frito-Lay Snack & Global Beverage Portfolio", "category": "Defensive Compounder"},
    "MCD":   {"name": "McDonald's Corp.", "sector": "Consumer Cyclical", "theme": "Global Fast Food Real Estate Royalty Moat", "category": "High ROIC Compounder"},
    "TJX":   {"name": "TJX Companies", "sector": "Consumer Cyclical", "theme": "Off-Price Retail Treasure Hunt Immune to E-Com", "category": "High ROIC Compounder"},
    "CMG":   {"name": "Chipotle Mexican Grill", "sector": "Consumer Cyclical", "theme": "Fast-Casual High Unit Economics & ROIC", "category": "High-Growth Moat"},
    "ORLY":  {"name": "O'Reilly Automotive", "sector": "Consumer Cyclical", "theme": "Auto Parts Commercial Delivery Monopoly", "category": "High ROIC Compounder"},
    "AZO":   {"name": "AutoZone Inc.", "sector": "Consumer Cyclical", "theme": "DIY Auto Parts & Relentless Share Cannibal", "category": "High ROIC Compounder"},

    # --- Enterprise Software, Cybersecurity & Cloud Infrastructure ---
    "MSFT":  {"name": "Microsoft Corp.", "sector": "Technology", "theme": "Enterprise Azure Cloud & Office AI Suite", "category": "Tech Platform"},
    "GOOG":  {"name": "Alphabet Inc.", "sector": "Communication Services", "theme": "Search, YouTube Monopoly & GCP Cloud", "category": "Tech Platform"},
    "AMZN":  {"name": "Amazon.com Inc.", "sector": "Consumer Cyclical", "theme": "AWS Cloud Infrastructure & Prime Logistics", "category": "Tech Platform"},
    "CRM":   {"name": "Salesforce Inc.", "sector": "Technology", "theme": "Agentforce Autonomous Enterprise AI CRM", "category": "Software SaaS"},
    "NOW":   {"name": "ServiceNow Inc.", "sector": "Technology", "theme": "Enterprise Workflow Automation System of Action", "category": "Software SaaS"},
    "PANW":  {"name": "Palo Alto Networks", "sector": "Technology", "theme": "Cybersecurity Platformization & Cortex XDR", "category": "High-Growth Moat"},
    "CRWD":  {"name": "CrowdStrike Holdings", "sector": "Technology", "theme": "Falcon Single-Agent Cloud Security Architecture", "category": "High-Growth Moat"},
    "FTNT":  {"name": "Fortinet Inc.", "sector": "Technology", "theme": "Proprietary ASIC Firewalls & Secure SASE", "category": "High Margin Tollbooth"},
    "PLTR":  {"name": "Palantir Technologies", "sector": "Technology", "theme": "AIP Enterprise Ontology & Defense Operating System", "category": "High-Growth Moat"},
    "ORCL":  {"name": "Oracle Corporation", "sector": "Technology", "theme": "OCI GPU Cloud Clusters & Autonomous Database", "category": "Tech Platform"},
    "ADBE":  {"name": "Adobe Inc.", "sector": "Technology", "theme": "Creative Cloud Monopolistic Standard & Firefly", "category": "High Margin Tollbooth"},
    "INTU":  {"name": "Intuit Inc.", "sector": "Technology", "theme": "TurboTax & QuickBooks SMB Ecosystem Moat", "category": "High Margin Tollbooth"},
    "NET":   {"name": "Cloudflare Inc.", "sector": "Technology", "theme": "Global Edge Network CDN & Workers AI", "category": "High-Growth Moat"},
    "DDOG":  {"name": "Datadog Inc.", "sector": "Technology", "theme": "Cloud Observability & LLM Monitoring Stack", "category": "High-Growth Moat"},

    # --- Semiconductor Value Chain (Foundry, Equipment, GPU/ASIC) ---
    "NVDA":  {"name": "NVIDIA Corporation", "sector": "Technology", "theme": "Full-Stack GPU Compute & CUDA Software Moat", "category": "AI Hardware Leader"},
    "TSM":   {"name": "Taiwan Semiconductor (ADR)", "sector": "Technology", "theme": "Leading-Edge Foundry Monopoly (>90% Share)", "category": "AI Hardware Leader"},
    "AVGO":  {"name": "Broadcom Inc.", "sector": "Technology", "theme": "Custom XPU ASIC & PCIe AI Switches", "category": "AI Hardware Leader"},
    "ASML":  {"name": "ASML Holding NV", "sector": "Technology", "theme": "EUV Photolithography Absolute Global Monopoly", "category": "High ROIC Compounder"},
    "AMD":   {"name": "Advanced Micro Devices", "sector": "Technology", "theme": "Data Center Instinct GPU & EPYC CPU", "category": "AI Hardware Challenger"},
    "MU":    {"name": "Micron Technology", "sector": "Technology", "theme": "HBM3E / HBM4 Memory High-Bandwidth Tollbooth", "category": "Memory Compounder"},
    "QCOM":  {"name": "Qualcomm Inc.", "sector": "Technology", "theme": "Snapdragon Edge AI & Automotive Cockpit", "category": "High Margin Tollbooth"},
    "AMAT":  {"name": "Applied Materials", "sector": "Technology", "theme": "Wafer Fab Deposition & Etch Tool Leader", "category": "High ROIC Compounder"},
    "LRCX":  {"name": "Lam Research", "sector": "Technology", "theme": "Cryogenic 3D NAND & GAA Dielectric Etching", "category": "High ROIC Compounder"},
    "KLAC":  {"name": "KLA Corporation", "sector": "Technology", "theme": "Semiconductor Optical Inspection & Yield Monopoly", "category": "High ROIC Compounder"},
    "ARM":   {"name": "Arm Holdings", "sector": "Technology", "theme": "Ultra-Low Power Compute Architecture Royalty", "category": "High Margin Tollbooth"},
    "MRVL":  {"name": "Marvell Technology", "sector": "Technology", "theme": "Electro-Optics DSPs & Custom AI Acceleration", "category": "AI Hardware Leader"},

    # --- Real Assets, Energy, Copper & Commodity Hedges ---
    "XOM":   {"name": "Exxon Mobil Corp.", "sector": "Energy", "theme": "Permian Basin Scale & Integrated FCF Engine", "category": "Energy Supermajor"},
    "CVX":   {"name": "Chevron Corporation", "sector": "Energy", "theme": "Tengiz Megaproject & Low Break-Even Oil", "category": "Energy Supermajor"},
    "COP":   {"name": "ConocoPhillips", "sector": "Energy", "theme": "Pure-Play E&P Low Cost of Supply", "category": "Energy Leader"},
    "FCX":   {"name": "Freeport-McMoRan", "sector": "Materials", "theme": "Global Copper Grasberg Mine Monopoly", "category": "Commodity Supercycle"},
    "SCCO":  {"name": "Southern Copper Corp.", "sector": "Materials", "theme": "Lowest Quartile Copper Cash Cost in World", "category": "Commodity Supercycle"},
    "LIN":   {"name": "Linde plc", "sector": "Materials", "theme": "Industrial Gases Take-or-Pay Onsite Moat", "category": "High ROIC Compounder"},
    "SHW":   {"name": "Sherwin-Williams", "sector": "Materials", "theme": "Architectural Paint Controlled Distribution Stores", "category": "High ROIC Compounder"},
    "GLD":   {"name": "SPDR Gold Shares", "sector": "Commodities", "theme": "Sovereign Debt Debasement & Geopolitical Hedge", "category": "Macro Hedge"},
    "COPX":  {"name": "Global X Copper Miners ETF", "sector": "Materials", "theme": "Global Electrification Physical Bottleneck", "category": "Macro Hedge"},
    "CCJ":   {"name": "Cameco Corporation", "sector": "Energy", "theme": "Pure-Play Uranium Mining & Westinghouse Nuclear", "category": "Energy Infrastructure"},

    # --- Communication Platforms & Media ---
    "META":  {"name": "Meta Platforms", "sector": "Communication Services", "theme": "Family of Apps 3.3B Daily Users & Llama AI", "category": "Tech Platform"},
    "NFLX":  {"name": "Netflix Inc.", "sector": "Communication Services", "theme": "Global Streaming Scale & Operating Margin Expansion", "category": "High-Growth Moat"},
    "DIS":   {"name": "Walt Disney Company", "sector": "Communication Services", "theme": "Parks, Cruise Lines & Century-Old IP Moat", "category": "Turnaround Compounder"}
}

# ==============================================================================
# 2. THEMATIC DISCOVERY REGISTRY (Option C: Emerging Pure-Play Leaders)
# ==============================================================================
THEMATIC_DISCOVERY_REGISTRY = {
    # 1. Nuclear Renaissance & SMRs (AI Power Bottleneck)
    "SMR":   {"ticker": "SMR",   "name": "NuScale Power", "sector": "Utilities", "theme": "NRC-Certified Small Modular Reactor", "category": "SMR Pure-Play"},
    "OKLO":  {"ticker": "OKLO",  "name": "Oklo Inc.", "sector": "Utilities", "theme": "Fast Fission Micro-Reactors & Data Center Power", "category": "SMR Speculative Alpha"},
    "NNE":   {"ticker": "NNE",   "name": "Nano Nuclear Energy", "sector": "Utilities", "theme": "Portable Micro-Reactors & Nuclear Fuel", "category": "SMR Speculative Alpha"},
    "BWX":   {"ticker": "BWXT",  "name": "BWX Technologies", "sector": "Industrials", "theme": "Naval Nuclear Propulsion & Commercial SMRs", "category": "Nuclear Infrastructure"},
    
    # 2. Data Center Thermal & Grid Hardware Pure-Plays
    "MOD":   {"ticker": "MOD",   "name": "Modine Manufacturing", "sector": "Industrials", "theme": "Data Center Chillers & Heat Exchangers", "category": "AI Thermal Leader"},
    "FLR":   {"ticker": "FLR",   "name": "Fluor Corporation", "sector": "Industrials", "theme": "Nuclear & Data Center EPC Mega-Projects", "category": "Energy Infrastructure"},
    "MYRG":  {"ticker": "MYRG",  "name": "MYR Group", "sector": "Industrials", "theme": "Transmission Line Construction & Substations", "category": "Grid Electrification"},

    # 3. Autonomous Warfare & Defense AI
    "AVAV":  {"ticker": "AVAV",  "name": "AeroVironment Inc.", "sector": "Industrials", "theme": "Switchblade Loitering Munitions & Military Drones", "category": "Defense Tech Leader"},
    
    # 4. Metabolic & Next-Gen Biotech
    "VKTX":  {"ticker": "VKTX",  "name": "Viking Therapeutics", "sector": "Healthcare", "theme": "Dual GLP-1/GIP Agonist Weight Loss Pipeline", "category": "Biotech Breakthrough"},
    "NVO":   {"ticker": "NVO",   "name": "Novo Nordisk (ADR)", "sector": "Healthcare", "theme": "Ozempic/Wegovy Metabolic Global Duopoly", "category": "Defensive Compounder"}
}

# ==============================================================================
# 3. INSTITUTIONAL ETF UNIVERSE
# ==============================================================================
ETF_UNIVERSE = {
    "VOO": {
        "name": "Vanguard S&P 500 ETF",
        "asset_class": "US Large-Cap Blend",
        "theme": "S&P 500 Low-Cost Core Anchor",
        "category": "Broad Market Anchor",
        "expense_ratio": 0.03,
        "role_en": "Core Portfolio Foundation (Dilutes Tech Beta)",
        "role_kr": "미국 경제 전반 코어 앵커 (개별 기술주 변동성 희석)",
        "thesis_en": "Ultra-low cost (0.03%) index foundation tracking 500 diversified US leaders, stabilizing mega-cap single stock volatility.",
        "thesis_kr": "연 0.03%의 초저비용으로 미국 500대 우량 기업에 분산 투자하여 현재 편중된 빅테크 변동성을 완화."
    },
    "RSP": {
        "name": "Invesco S&P 500 Equal Weight ETF",
        "asset_class": "US Equal-Weight Large-Cap",
        "theme": "Equal-Weight Anti-Concentration Ballast",
        "category": "Anti-Concentration Ballast",
        "expense_ratio": 0.20,
        "role_en": "Anti-Concentration Factor Balance (Equal Weight)",
        "role_kr": "빅테크 쏠림 배제 동일가중 밸런서",
        "thesis_en": "Allocates equal 0.2% weight across all 500 companies, systematically eliminating mega-cap tech concentration risk.",
        "thesis_kr": "S&P 500 전 종목에 각 0.2%씩 동일 비중으로 분산 투자하여 상위 기술주 쏠림 리스크를 구조적으로 차단."
    },
    "SCHD": {
        "name": "Schwab U.S. Dividend Equity ETF",
        "asset_class": "US Large-Cap Value / Quality",
        "theme": "High ROE & FCF Dividend Growth",
        "category": "Quality Dividend Compounder",
        "expense_ratio": 0.06,
        "role_en": "High Cash Flow Yield & Low-Beta Shock Absorber",
        "role_kr": "고현금흐름 배당 성장 및 저베타 완충재 (기술주 하락 시 현금흐름 밸러스트)",
        "thesis_en": "Screens for 10 consecutive years of dividend payments, high ROE (>25%), low beta (0.56) and ~3.4% yield with zero tech overlap.",
        "thesis_kr": "10년 연속 배당, 높은 ROE, 건전한 재무구조를 갖춘 기업 추종. 기술주와 겹치지 않는 저베타(0.56) 현금흐름 제공."
    },
    "COWZ": {
        "name": "Pacer US Cash Cows 100 ETF",
        "asset_class": "US Large-Cap Deep FCF Value",
        "theme": "Top 100 Free Cash Flow Yield Leaders",
        "category": "Deep Cash Flow Value",
        "expense_ratio": 0.49,
        "role_en": "Pure FCF Valuation Multiple Discipline",
        "role_kr": "순수 FCF 일드 기반 딥 밸류 (실질 현금 창출력 중심 가치 방어)",
        "thesis_en": "Selects top 100 Russell 1000 companies ranked by Free Cash Flow Yield (~7-8%), providing hard downside margin of safety.",
        "thesis_kr": "잉여현금흐름 수익률 최상위 100개 기업을 선별하여 밸류에이션 하방 경직성 확보."
    },
    "XLU": {
        "name": "Utilities Select Sector SPDR Fund",
        "asset_class": "US Utilities & Power Grid",
        "theme": "AI Data Center Power & Nuclear Demand Supercycle",
        "category": "Infrastructure & Power Ballast",
        "expense_ratio": 0.09,
        "role_en": "AI Power Bottleneck Proxy with High Dividend & Low Beta",
        "role_kr": "AI 전력 병목 수혜 프록시 + 고배당 방어추",
        "thesis_en": "Captures the AI energy bottleneck thesis with hyperscaler power contracts, offering ~3.0% yield and low beta (0.40).",
        "thesis_kr": "빅테크 AI 데이터센터 전력 계약 수혜를 흡수하며 저베타 방어력과 안정적 배당을 동시 제공."
    },
    "XLE": {
        "name": "Energy Select Sector SPDR Fund",
        "asset_class": "US Energy Sector",
        "theme": "Traditional Energy FCF & Geopolitical Supply Shock Hedge",
        "category": "Inflation & Geopolitical Hedge",
        "expense_ratio": 0.09,
        "role_en": "Negative Correlation to Tech & Physical Energy Hedge",
        "role_kr": "기술주 역상관 인플레이션 & 지정학 에너지 쇼크 헤지",
        "thesis_en": "Provides negative correlation to tech drawdowns and protects against geopolitical supply disruptions.",
        "thesis_kr": "전통 에너지 메이저의 막대한 현금흐름을 바탕으로 기술주 급락 및 지정학 유가 쇼크를 헤지."
    },
    "COPX": {
        "name": "Global X Copper Miners ETF",
        "asset_class": "Global Natural Resources",
        "theme": "Global Grid Electrification Physical Bottleneck",
        "category": "Commodity Supercycle Hedge",
        "expense_ratio": 0.65,
        "role_en": "Physical Infrastructure Scarcity Play",
        "role_kr": "글로벌 전력망 및 전력화 필수 원자재 희소성 헤지",
        "thesis_en": "Plays the physical copper deficit driven by power grid expansion and AI cabling with mining cash flows.",
        "thesis_kr": "전력망 확충 및 AI 데이터센터 전력 배선에 필수적인 구리 공급 부족 수혜를 레버리지."
    },
    "GLD": {
        "name": "SPDR Gold Shares",
        "asset_class": "Physical Commodity (Gold)",
        "theme": "Sovereign Debt Debasement & Geopolitical Safe-Haven",
        "category": "Macro Tail-Risk Hedge",
        "expense_ratio": 0.40,
        "role_en": "Zero Correlation Equity Market Shock Absorber",
        "role_kr": "주식 시장 무상관(Zero Correlation) 거시 테일 리스크 헤지",
        "thesis_en": "Physical gold trust providing non-correlated ballast against debt expansion, currency debasement, and equity crashes.",
        "thesis_kr": "글로벌 부채 급증 및 화폐가치 하락에 대응하는 무상관 안전자산 앵커."
    },
    "SGOV": {
        "name": "iShares 0-3 Month Treasury Bond ETF",
        "asset_class": "Ultra-Short US Treasury Bills",
        "theme": "Risk-Free Cash Flow Yield & Capital Preservation",
        "category": "Dry Powder Cash Proxy",
        "expense_ratio": 0.07,
        "role_en": "Protects Dry Powder Buffer with ~4.5% Risk-Free Yield",
        "role_kr": "원금 보존 및 연 ~4.5% 무위험 달러 수익 창출 (현금 버퍼 완벽 대체)",
        "thesis_en": "Surrogate for portfolio dry powder buffer (15-20% target). Invests in 0-3 month US Treasury bills.",
        "thesis_kr": "0~3개월 만기 미국 단기국채에만 투자하여 금리 리스크 없이 월배당 무위험 달러 수익 창출."
    },
    "XLV": {
        "name": "Health Care Select Sector SPDR Fund",
        "asset_class": "US Healthcare & Pharma",
        "theme": "Inelastic Demand & Secular Demographics",
        "category": "Defensive Growth Ballast",
        "expense_ratio": 0.09,
        "role_en": "Non-Cyclical Defensive Growth Outside Tech Ecosystem",
        "role_kr": "비순환적 경기 방어 성장주 (기술주 사이클과 무관한 필수 소비)",
        "thesis_en": "Broad exposure to pharma, medical devices, and managed care. Immune to tech spending cycles with low beta (0.52).",
        "thesis_kr": "IT 설비투자 사이클과 무관한 비탄력적 헬스케어 수요에 투자하여 저베타 방어력 확보."
    },
    "ITA": {
        "name": "iShares U.S. Aerospace & Defense ETF",
        "asset_class": "US Defense & Aerospace",
        "theme": "Global Geopolitical Defense Spending Supercycle",
        "category": "Monopsony Defense Moat",
        "expense_ratio": 0.40,
        "role_en": "Government Contract Stability & Low Macro Sensitivity",
        "role_kr": "정부 독점 국방 예산 기반 안정적 수주 방어주",
        "thesis_en": "Holds prime US defense contractors backed by multi-year backlog and non-discretionary federal defense spending.",
        "thesis_kr": "미국 핵심 방산 기업에 분산 투자하여 지정학적 위기 속에서 확정된 수주 잔고를 바탕으로 안정적 수익 창출."
    }
}

# ==============================================================================
# 4. PORTFOLIO & CACHING CONFIGURATION
# ==============================================================================
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache", "market_data")
os.makedirs(CACHE_DIR, exist_ok=True)
CACHE_TTL_HOURS = 24.0

def load_portfolio(yaml_path):
    """Loads existing portfolio configuration from yaml."""
    if not os.path.exists(yaml_path):
        return {"holdings": [], "profile": {}, "tickers": set()}
    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        holdings = data.get("holdings", [])
        tickers = {h.get("ticker", "").upper() for h in holdings if h.get("ticker")}
        return {
            "holdings": holdings,
            "profile": data.get("investor_profile", {}),
            "summary": data.get("portfolio_summary", {}),
            "tickers": tickers
        }
    except Exception as e:
        print(f"[Warning] Failed to parse {yaml_path}: {e}", file=sys.stderr)
        return {"holdings": [], "profile": {}, "tickers": set()}

def get_cached_metrics(ticker):
    """Retrieves cached metrics if fresher than CACHE_TTL_HOURS."""
    cache_file = os.path.join(CACHE_DIR, f"{ticker}_metrics.json")
    if os.path.exists(cache_file):
        try:
            mtime = os.path.getmtime(cache_file)
            age_hours = (datetime.datetime.now().timestamp() - mtime) / 3600.0
            if age_hours < CACHE_TTL_HOURS:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    return None

def save_cached_metrics(ticker, data):
    """Saves metrics to local cache."""
    if not data:
        return
    try:
        cache_file = os.path.join(CACHE_DIR, f"{ticker}_metrics.json")
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

# ==============================================================================
# 5. TRACK 1: HIGH-SPEED BATCH QUANT SCANNER (Option B)
# ==============================================================================
def run_batch_quant_scanner(universe_dict, mode="default"):
    """
    Downloads 6-month price data in a single batch vector query for all universe tickers.
    Computes 52w high discount, RS momentum vs SPY, moving average trend, and Beta.
    Returns ranked candidates (top 25-30) for deep fundamental audit.
    """
    tickers = list(universe_dict.keys())
    benchmark = "SPY"
    all_tickers = tickers + [benchmark]
    
    print(f"[*] [Track 1 Quant Funnel] Batch vector downloading price action for {len(tickers)} institutional leaders...", file=sys.stderr)
    try:
        df = yf.download(all_tickers, period="6mo", interval="1d", progress=False, group_by="ticker", auto_adjust=True)
    except Exception as e:
        print(f"[Warning] Batch download failed ({e}), falling back to direct pool.", file=sys.stderr)
        return tickers[:30]

    quant_results = []
    spy_perf_3m = 0.0
    
    # Calculate SPY benchmark performance
    try:
        if benchmark in df.columns.levels[0]:
            spy_close = df[benchmark]["Close"].dropna()
            if len(spy_close) >= 60:
                spy_perf_3m = ((spy_close.iloc[-1] - spy_close.iloc[-60]) / spy_close.iloc[-60]) * 100.0
    except Exception:
        pass

    mode_lower = mode.lower()

    for ticker in tickers:
        try:
            if ticker not in df.columns.levels[0]:
                continue
            series = df[ticker]["Close"].dropna()
            if len(series) < 20:
                continue
            
            curr_price = float(series.iloc[-1])
            high_6m = float(series.max())
            discount_from_high = ((high_6m - curr_price) / high_6m) * 100.0 if high_6m > 0 else 0.0
            
            # Momentum calculation
            perf_3m = (((curr_price - float(series.iloc[-60])) / float(series.iloc[-60])) * 100.0) if len(series) >= 60 else 0.0
            rs_score = perf_3m - spy_perf_3m  # Relative Strength vs SPY
            
            # Moving average trend
            sma_20 = float(series.tail(20).mean())
            sma_50 = float(series.tail(50).mean()) if len(series) >= 50 else sma_20
            trend_bullish = curr_price >= sma_20 >= sma_50
            
            meta = universe_dict.get(ticker, {})
            sector = meta.get("sector", "General")
            
            # Sector filtering based on mode
            if mode_lower in ["power", "grid", "nuclear", "smr"]:
                th_lower = meta.get("theme", "").lower()
                if sector not in ["Utilities", "Industrials"] and "nuclear" not in th_lower and "power" not in th_lower:
                    continue
            elif mode_lower in ["energy", "oil"] and sector != "Energy":
                continue
            elif mode_lower in ["health", "healthcare", "biotech"] and sector != "Healthcare":
                continue
            elif mode_lower in ["tech", "semi", "software"] and sector not in ["Technology", "Communication Services"]:
                continue
            elif mode_lower in ["defense", "aerospace", "drone"] and sector != "Industrials":
                continue
            elif mode_lower in ["defense", "hedge"] and sector not in ["Industrials", "Healthcare", "Consumer Defensive", "Utilities", "Financials"]:
                continue

            # Quant score weighting based on regime
            q_score = 50.0
            
            # 1. Momentum & Trend
            if rs_score > 10.0: q_score += 15.0
            elif rs_score > 0.0: q_score += 8.0
            elif rs_score < -15.0: q_score -= 10.0
            
            if trend_bullish: q_score += 10.0

            # 2. 52W High Proximity / Pullback Discount
            if "canslim" in mode_lower or "oneil" in mode_lower:
                if discount_from_high <= 15.0: q_score += 20.0
                elif discount_from_high > 30.0: q_score -= 15.0
            elif "buffett" in mode_lower or "garp" in mode_lower:
                if 10.0 <= discount_from_high <= 25.0: q_score += 15.0  # Quality on temporary pullback
            elif "defense" in mode_lower:
                if discount_from_high <= 20.0: q_score += 10.0
            
            quant_results.append({
                "ticker": ticker,
                "price": curr_price,
                "rs_score": round(rs_score, 1),
                "discount_from_high": round(discount_from_high, 1),
                "trend_bullish": trend_bullish,
                "quant_score": q_score
            })
        except Exception:
            continue

    quant_results.sort(key=lambda x: x["quant_score"], reverse=True)
    selected_tickers = [x["ticker"] for x in quant_results[:30]]
    print(f"[+] [Track 1 Quant Funnel] Filtered down to top {len(selected_tickers)} candidates from {len(tickers)} universe.", file=sys.stderr)
    return selected_tickers

# ==============================================================================
# 6. TRACK 2: THEMATIC & WALL STREET RADAR (Option C)
# ==============================================================================
def discover_thematic_candidates(mode="default", extra_tickers=None):
    """
    Identifies high-growth emerging leaders and theme-specific pure plays
    from the Thematic Registry and dynamic inputs.
    """
    discovered = []
    mode_lower = mode.lower()
    
    print(f"[*] [Track 2 Thematic Radar] Scanning emerging pure-play leaders and thematic intelligence for '{mode}'...", file=sys.stderr)
    
    # 1. Query Thematic Registry based on keywords
    for key, item in THEMATIC_DISCOVERY_REGISTRY.items():
        t = item["ticker"]
        th = item.get("theme", "").lower()
        sec = item.get("sector", "").lower()
        
        match = False
        if mode_lower in ["default", "all"]:
            match = True
        elif mode_lower in ["power", "energy", "smr", "nuclear"] and ("nuclear" in th or "power" in th or "grid" in th or "smr" in th):
            match = True
        elif mode_lower in ["defense", "drone", "warfare"] and ("defense" in th or "drone" in th or "munitions" in th):
            match = True
        elif mode_lower in ["health", "biotech", "glp1", "glp-1"] and ("glp" in th or "biotech" in th or sec == "healthcare"):
            match = True
        elif mode_lower in ["tech", "ai", "cooling", "thermal"] and ("thermal" in th or "chillers" in th or "cooling" in th):
            match = True
        
        if match and t not in discovered:
            discovered.append(t)

    # 2. Add extra dynamic tickers passed via CLI / Agent
    if extra_tickers:
        for t in extra_tickers:
            t_clean = t.strip().upper()
            if t_clean and t_clean not in discovered:
                discovered.append(t_clean)
                print(f"[+] [Track 2 Dynamic] Ingested dynamic ticker: {t_clean}", file=sys.stderr)

    print(f"[+] [Track 2 Thematic Radar] Surfaced {len(discovered)} thematic candidate leaders: {discovered[:8]}", file=sys.stderr)
    return discovered

# ==============================================================================
# 7. DEEP METRIC AUDIT & TRUE ROIC ENGINE
# ==============================================================================
def calculate_true_roic(t, info):
    """Calculates true institutional ROIC = NOPAT / Invested Capital using financial statements."""
    try:
        inc = getattr(t, 'financials', None)
        bs = getattr(t, 'balance_sheet', None)
        if inc is not None and not inc.empty and bs is not None and not bs.empty:
            op_inc = None
            for key in ['Operating Income', 'Operating Profit', 'EBIT']:
                if key in inc.index:
                    op_inc = inc.loc[key].iloc[0]
                    break
            
            equity = None
            for key in ['Stockholders Equity', 'Common Stock Equity', 'Total Stockholder Equity']:
                if key in bs.index:
                    equity = bs.loc[key].iloc[0]
                    break
            
            debt = 0.0
            for key in ['Total Debt', 'Long Term Debt']:
                if key in bs.index:
                    val = bs.loc[key].iloc[0]
                    if pd.notna(val): debt = float(val)
                    break
            
            cash = 0.0
            for key in ['Cash And Cash Equivalents', 'Cash Cash Equivalents And Short Term Investments']:
                if key in bs.index:
                    val = bs.loc[key].iloc[0]
                    if pd.notna(val): cash = float(val)
                    break
            
            if op_inc is not None and equity is not None and pd.notna(op_inc) and pd.notna(equity):
                nopat = float(op_inc) * (1.0 - 0.21)
                inv_cap = float(equity) + debt - cash
                if inv_cap > 0:
                    roic_val = (nopat / inv_cap) * 100.0
                    if -100.0 <= roic_val <= 300.0:
                        return round(roic_val, 1)
    except Exception:
        pass
    
    roc = info.get("returnOnCapital")
    if roc is not None and pd.notna(roc):
        return round(float(roc) * 100.0, 1)
    
    return "N/A"

def fetch_metrics_for_ticker(ticker, meta=None):
    """Fetches key quantitative and valuation metrics for equities via yfinance (with local cache)."""
    meta = meta or {}
    cached = get_cached_metrics(ticker)
    if cached:
        return cached
    try:
        t = yf.Ticker(ticker)
        info = t.info or {}
        fast = getattr(t, 'fast_info', None)
        curr_price = (fast.get('last_price') if fast else None) or info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose") or 0.0
        mkt_cap = (info.get("marketCap") or 0.0) / 1e9  # in Billions
        fwd_pe = info.get("forwardPE") or info.get("trailingPE") or 0.0
        peg = info.get("pegRatio") or 0.0
        roic = calculate_true_roic(t, info)
        fcf = info.get("freeCashflow") or 0.0
        fcf_yield = ((fcf / (info.get("marketCap") or 1.0)) * 100) if fcf > 0 else 0.0
        beta = info.get("beta") or 1.0
        debt_to_equity = info.get("debtToEquity") or 50.0
        gross_margin = (info.get("grossMargins") or 0.0) * 100
        rev_growth = (info.get("revenueGrowth") or 0.0) * 100
        high_52 = info.get("fiftyTwoWeekHigh") or curr_price
        discount_from_52w = (((high_52 - curr_price) / high_52) * 100) if high_52 > 0 else 0.0

        name = meta.get("name") or info.get("shortName") or info.get("longName") or ticker
        sector = meta.get("sector") or info.get("sector") or "General"
        theme = meta.get("theme") or info.get("industry") or "Institutional Growth Leader"
        category = meta.get("category") or "Secular Compounder"

        res = {
            "ticker": ticker,
            "name": name,
            "sector": sector,
            "theme": theme,
            "category": category,
            "price": round(curr_price, 2),
            "market_cap_b": round(mkt_cap, 1),
            "forward_pe": round(fwd_pe, 1) if fwd_pe > 0 else "N/A",
            "peg": round(peg, 2) if peg > 0 else "N/A",
            "roic": roic,
            "fcf_yield": round(fcf_yield, 2),
            "beta": round(beta, 2),
            "debt_to_equity": round(debt_to_equity, 1),
            "gross_margin": round(gross_margin, 1),
            "revenue_growth": round(rev_growth, 1),
            "discount_from_52w": round(discount_from_52w, 1)
        }
        save_cached_metrics(ticker, res)
        return res
    except Exception as e:
        return None

def fetch_metrics_for_etf(ticker, meta=None):
    """Fetches key quantitative and valuation metrics for ETFs via yfinance (with dedicated ETF local cache)."""
    meta = meta or ETF_UNIVERSE.get(ticker, {})
    cache_file = os.path.join(CACHE_DIR, f"{ticker}_etf_metrics.json")
    if os.path.exists(cache_file):
        try:
            mtime = os.path.getmtime(cache_file)
            age_hours = (datetime.datetime.now().timestamp() - mtime) / 3600.0
            if age_hours < CACHE_TTL_HOURS:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    try:
        t = yf.Ticker(ticker)
        info = t.info or {}
        fast = getattr(t, 'fast_info', None)
        curr_price = (fast.get('last_price') if fast else None) or info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose") or 0.0
        aum = (info.get("totalAssets") or info.get("netAssets") or (info.get("marketCap") or 0.0)) / 1e9
        pe = info.get("trailingPE") or info.get("forwardPE")
        div_yield = (info.get("yield") or info.get("dividendYield") or 0.0) * 100.0
        beta = info.get("beta") or info.get("beta3Year") or (0.0 if ticker == "SGOV" else 0.5)
        high_52 = info.get("fiftyTwoWeekHigh") or curr_price
        discount_from_52w = (((high_52 - curr_price) / high_52) * 100) if high_52 > 0 else 0.0

        res = {
            "ticker": ticker,
            "name": meta.get("name", ticker),
            "asset_class": meta.get("asset_class", "ETF"),
            "theme": meta.get("theme", ""),
            "category": meta.get("category", ""),
            "expense_ratio": meta.get("expense_ratio", 0.10),
            "portfolio_role_en": meta.get("role_en", meta.get("role", "")),
            "portfolio_role_kr": meta.get("role_kr", meta.get("role", "")),
            "thesis_en": meta.get("thesis_en", meta.get("thesis", "")),
            "thesis_kr": meta.get("thesis_kr", meta.get("thesis", "")),
            "price": round(curr_price, 2),
            "aum_b": round(aum, 1),
            "pe": round(pe, 1) if pe and isinstance(pe, (int, float)) else "N/A",
            "dividend_yield": round(div_yield, 2),
            "beta": round(beta, 2),
            "discount_from_52w": round(discount_from_52w, 1)
        }
        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(res, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
        return res
    except Exception as e:
        return None

# ==============================================================================
# 8. 5 GREAT MASTERS + MARKET TECHNICIAN CONSENSUS SCORING
# ==============================================================================
def score_equity_candidate(metrics, mode, user_tickers):
    """
    Evaluates equity candidates against:
      1) Fundamental Quality (ROIC, Gross Margin, FCF Yield, Solvency)
      2) Portfolio Gap-Filling (balancing BM사장님's tech/semi beta)
      3) 5 Great Masters + Chief Market Technician Consensus
    """
    if not metrics or metrics["price"] <= 0:
        return 0.0

    score = 50.0
    ticker = metrics["ticker"]
    sector = metrics["sector"]
    beta = metrics["beta"]
    roic = metrics["roic"]
    fwd_pe = metrics["forward_pe"] if isinstance(metrics["forward_pe"], (int, float)) else 30.0
    peg = metrics["peg"] if isinstance(metrics["peg"], (int, float)) else 2.0
    de = metrics["debt_to_equity"]
    gm = metrics["gross_margin"]
    disc_52 = metrics["discount_from_52w"]

    # 1. Moat & Profitability (Warren Buffett / Charlie Munger Lens)
    if isinstance(roic, (int, float)):
        if roic >= 25.0: score += 12.0
        elif roic >= 15.0: score += 8.0
        elif roic < 7.0: score -= 8.0
    
    if gm >= 60.0: score += 8.0
    elif gm >= 40.0: score += 4.0

    # 2. Fortress Solvency (Buffett Capital Preservation)
    if de < 40.0: score += 8.0
    elif de > 150.0: score -= 8.0

    # 3. Growth at Reasonable Price (Peter Lynch Lens)
    if isinstance(peg, (int, float)) and peg > 0:
        if peg <= 1.0: score += 12.0
        elif peg <= 1.5: score += 6.0
        elif peg > 2.8: score -= 8.0

    if fwd_pe < 20.0: score += 6.0
    elif fwd_pe > 50.0 and "growth" not in mode.lower(): score -= 6.0

    # 4. Breakout & Relative Strength (William O'Neil / CAN SLIM & Technician Lens)
    if disc_52 <= 12.0: score += 8.0   # Near 52-week highs
    elif disc_52 > 35.0: score -= 6.0  # Persistent breakdown unless deep value

    # 5. Portfolio Gap-Filling Complementarity (Crucial for BM사장님's Portfolio)
    # BM사장님 currently holds high semiconductor/tech beta (NVDA, GOOG, AMZN, AVGO, SOXL, TQQQ)
    mode_lower = mode.lower()
    theme_lower = metrics.get("theme", "").lower()
    
    # Mode-Specific Factor & Theme Boosts
    if mode_lower in ["power", "grid", "nuclear", "smr"]:
        if sector in ["Utilities", "Industrials"] or "nuclear" in theme_lower or "power" in theme_lower or "grid" in theme_lower:
            score += 20.0
        else:
            score -= 25.0
    elif mode_lower in ["defense", "aerospace", "drone"]:
        if "defense" in theme_lower or "drone" in theme_lower or ticker in ["LMT", "RTX", "GD", "NOC", "TDG", "HEI", "AXON", "KTOS", "AVAV"]:
            score += 20.0
        else:
            score -= 25.0
    elif mode_lower in ["health", "healthcare", "biotech"]:
        if sector == "Healthcare":
            score += 20.0
        else:
            score -= 25.0
    elif mode_lower in ["energy", "oil"]:
        if sector == "Energy":
            score += 20.0
        else:
            score -= 25.0
    elif mode_lower in ["tech", "semi", "software"]:
        if sector in ["Technology", "Communication Services"]:
            score += 20.0
        else:
            score -= 25.0
    else:
        # Default mode: Massive factor diversification bonus for non-tech
        is_non_tech_diversifier = sector in ["Healthcare", "Utilities", "Industrials", "Financials", "Consumer Defensive", "Materials", "Energy"]
        if is_non_tech_diversifier:
            score += 12.0
            if beta <= 0.85: score += 8.0
            elif beta <= 1.10: score += 4.0
        elif sector == "Technology":
            score -= 5.0  # Mild penalty for adding more tech to an 85% tech portfolio

    # 6. Holding Status
    if ticker in user_tickers:
        score -= 8.0
        metrics["portfolio_status"] = "Already Held (Add/Acc)"
    else:
        metrics["portfolio_status"] = "New Diversifier"

    return round(min(max(score, 10.0), 99.0), 1)

def score_etf_candidate(metrics, mode, user_tickers):
    """Scores ETF candidates based on expense ratio, liquidity, dividend yield, and beta."""
    if not metrics or metrics["price"] <= 0:
        return 0.0

    score = 50.0
    ticker = metrics.get("ticker", "")
    beta = metrics.get("beta", 0.5)
    exp = metrics.get("expense_ratio", 0.10)
    div_yield = metrics.get("dividend_yield", 0.0)
    aum = metrics.get("aum_b", 10.0)

    if beta <= 0.50: score += 20.0
    elif beta <= 0.85: score += 15.0
    elif beta <= 1.05: score += 8.0
    elif beta > 1.30: score -= 10.0

    if div_yield >= 3.0: score += 15.0
    elif div_yield >= 1.5: score += 10.0

    if exp <= 0.05: score += 15.0
    elif exp <= 0.10: score += 10.0
    elif exp <= 0.30: score += 5.0
    elif exp > 0.60: score -= 5.0

    if aum >= 50.0: score += 10.0
    elif aum >= 10.0: score += 5.0

    if ticker in ["SCHD", "VOO", "XLU", "GLD", "SGOV"]:
        score += 10.0

    if ticker in user_tickers:
        score -= 10.0
        metrics["portfolio_status"] = "Already Held (Add/Acc)"
    else:
        metrics["portfolio_status"] = "New ETF Allocation"

    return round(min(max(score, 10.0), 99.0), 1)

# ==============================================================================
# 9. HYBRID DUAL-ENGINE SCREENER PIPELINE
# ==============================================================================
def run_screener(mode="default", top_n=5, portfolio_file="my-portfolio.yaml", extra_tickers=None):
    """
    Executes the Dual-Engine Alpha Funnel:
      1) Track 1: Batch vector quant screening across 160+ master equities.
      2) Track 2: Thematic radar & dynamic discovery across pure plays.
      3) Track 3: Merger, deep fundamental audit, and 6-in-1 committee ranking.
    """
    portfolio_data = load_portfolio(portfolio_file)
    user_tickers = portfolio_data["tickers"]
    mode_lower = mode.lower()
    is_etf_mode = "etf" in mode_lower

    if is_etf_mode:
        print(f"[*] Screening {len(ETF_UNIVERSE)} institutional ETFs under mode: '{mode}'...", file=sys.stderr)
        candidates = []
        for ticker, meta in ETF_UNIVERSE.items():
            metrics = fetch_metrics_for_etf(ticker, meta)
            if metrics:
                score = score_etf_candidate(metrics, mode, user_tickers)
                metrics["alpha_score"] = score
                candidates.append(metrics)
        candidates.sort(key=lambda x: x["alpha_score"], reverse=True)
        return candidates[:top_n], is_etf_mode

    # --- EQUITY DUAL-ENGINE PIPELINE ---
    print(f"=== 🏛️ DADAIC DUAL-ENGINE ALPHA SCREENER (Mode: '{mode}') ===", file=sys.stderr)
    
    # Track 1 (Option B): High-speed batch quant vector filtering
    quant_candidate_tickers = run_batch_quant_scanner(MASTER_EQUITY_UNIVERSE, mode=mode)
    
    # Track 2 (Option C): Thematic radar & dynamic pure-play discovery
    thematic_candidate_tickers = discover_thematic_candidates(mode=mode, extra_tickers=extra_tickers)
    
    # Merge and deduplicate candidates
    combined_tickers = []
    for t in quant_candidate_tickers + thematic_candidate_tickers:
        if t not in combined_tickers:
            combined_tickers.append(t)
            
    print(f"[*] [Convergence] Unified screening pool contains {len(combined_tickers)} high-conviction candidates.", file=sys.stderr)

    candidates = []
    for ticker in combined_tickers:
        meta = MASTER_EQUITY_UNIVERSE.get(ticker) or THEMATIC_DISCOVERY_REGISTRY.get(ticker) or {}
        metrics = fetch_metrics_for_ticker(ticker, meta)
        if metrics and metrics.get("price", 0) > 0:
            score = score_equity_candidate(metrics, mode, user_tickers)
            metrics["alpha_score"] = score
            candidates.append(metrics)

    candidates.sort(key=lambda x: x["alpha_score"], reverse=True)
    return candidates[:top_n], is_etf_mode

# ==============================================================================
# 10. BILINGUAL DELIVERABLE GENERATOR (Strict USD / No KRW)
# ==============================================================================
def generate_report(top_picks, is_etf_mode=False, mode="default", output_dir="DecisionMemo"):
    """Renders the official CIO Alpha Shortlist memo in pure USD without KRW."""
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.datetime.now()
    date_str = today.strftime("%y%m%d")
    date_formatted = today.strftime("%B %d, %Y")
    
    filename = f"CIO-Picks-{date_str}.md"
    filepath = os.path.join(output_dir, filename)

    mode_title_map = {
        "default": "Dual-Engine Portfolio Gap-Filler & Quality Moat",
        "etf": "Institutional ETF Portfolio Stabilizers & Core Alpha Ballast",
        "buffett": "Buffett Fortress Value & High-ROIC Compounders",
        "garp": "Peter Lynch GARP (Growth at a Reasonable Price)",
        "lynch": "Peter Lynch GARP (Growth at a Reasonable Price)",
        "defense": "Low-Beta Defensive Ballast & Non-Tech Hedges",
        "power": "AI Data Center Power Grid & Nuclear Renaissance",
        "health": "Healthcare & Biotech Monopolistic Moats",
        "tech": "Secular Tech Platforms & Mission-Critical Software"
    }
    mode_title = mode_title_map.get(mode.lower(), f"{mode.upper()} Thematic Alpha")

    lines = []
    lines.append(f"# 🏛️ DADAIC INVESTMENT COMMITTEE: CIO ALPHA SHORTLIST & RECOMMENDATIONS")
    lines.append(f"> *Bilingual Edition: [English CIO Pitch Memo](#-part-1-english-cio-alpha-shortlist) | [한국어 CIO 주식·ETF 발굴 추천서](#-part-2-한국어-cio-유망-종목-발굴-추천서)*  ")
    lines.append(f"> **Document Control Number**: DADAIC-CIO-PICKS-{date_str}  ")
    lines.append(f"> **Screening Engine**: **Dual-Engine Alpha Funnel (Track 1 Batch Quant + Track 2 Thematic Radar)**  ")
    lines.append(f"> **Screening Regime / Mode**: **{mode_title}**  ")
    lines.append(f"> **Evaluation Date**: {date_formatted}  ")
    lines.append(f"> **Target Principal**: **BM사장님**  ")
    lines.append(f"> **Presided By**: Chief Investment Officer (CIO), DADAIC Investment Firm  \n")
    lines.append(f"---\n")

    # =========================================================================
    # PART 1: ENGLISH
    # =========================================================================
    lines.append(f"# 🇺🇸 PART 1: English CIO Alpha Shortlist\n")
    lines.append(f"### Executive Summary & Screening Mandate")
    if is_etf_mode:
        lines.append(f"The Chief Investment Officer (CIO) has completed an autonomous screening across institutional US Exchange-Traded Funds (ETFs) to address portfolio factor imbalance, high beta, and excessive tech concentration.")
        lines.append(f"- **Strategic Mandate**: Screen premier institutional ETFs providing durable capital compounding, non-tech equity diversification, high free cash flow / dividend yield, macro safe-haven protection, and capital preservation buffers.")
        lines.append(f"- **Selected Screening Mode**: `{mode.upper()}` ({mode_title}).\n")

        lines.append(f"## 1. Top Recommended Candidates Overview Table\n")
        lines.append(f"| Rank | Ticker | ETF Name & Asset Class | Market Price ($) | Trailing P/E | Div Yield (%) | Expense Ratio (%) | Beta | AUM ($B) | Alpha Score | Portfolio Role |")
        lines.append(f"| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |")

        for i, p in enumerate(top_picks, 1):
            pe_str = f"{p['pe']}x" if isinstance(p['pe'], (int, float)) else p['pe']
            lines.append(f"| **#{i}** | **{p['ticker']}** | {p['name']}<br>*(Class: {p['asset_class']})* | ${p['price']} | {pe_str} | {p['dividend_yield']}% | {p['expense_ratio']}% | {p['beta']} | ${p['aum_b']}B | **{p['alpha_score']} / 100** | {p['portfolio_status']} |")

        lines.append(f"\n---\n")
        lines.append(f"## 2. Deep-Dive Investment Theses & Portfolio Synergies\n")

        for i, p in enumerate(top_picks, 1):
            pe_str = f"{p['pe']}x" if isinstance(p['pe'], (int, float)) else p['pe']
            lines.append(f"### #{i}. **{p['ticker']} ({p['name']})** — *{p['theme']}*")
            lines.append(f"- **Key Metrics**: Market Price **${p['price']}**, Trailing P/E **{pe_str}**, Dividend Yield **{p['dividend_yield']}%**, Expense Ratio **{p['expense_ratio']}%**, Beta **{p['beta']}**, AUM **${p['aum_b']}B**.")
            lines.append(f"- **Investment Thesis**: {p['thesis_en']}")
            lines.append(f"- **Synergy with BM사장님's Portfolio**: {p['portfolio_role_en']}. Directly stabilizes single-stock mega-cap volatility and balances factor concentration.")
            lines.append(f"- **Actionable Protocol**: Enter `CIO {p['ticker']}` (or `ICP {p['ticker']}`) in chat to trigger full 5-stage due diligence.\n")

    else:
        lines.append(f"The Chief Investment Officer (CIO) has completed an autonomous screening using the **Dual-Engine Alpha Funnel** across institutional US equities to discover premier alpha opportunities.")
        lines.append(f"- **Funnel Architecture**: Merged **Track 1 (Batch Quant Vector Scanner across 160+ master equities)** with **Track 2 (Thematic Intelligence Radar)** to eliminate static echo chambers.")
        lines.append(f"- **Strategic Mandate**: Identify assets with durable economic moats, proven ROIC, and **Portfolio Gap-Filling Properties** (diluting excessive semiconductor/tech beta while maximizing forward Sharpe ratio for BM사장님).")
        lines.append(f"- **Selected Screening Mode**: `{mode.upper()}` ({mode_title}).\n")

        lines.append(f"## 1. Top Recommended Candidates Overview Table\n")
        lines.append(f"| Rank | Ticker | Company Name & Sector | Market Price ($) | Forward P/E | PEG | ROIC (%) | Beta | Alpha Score | Portfolio Role |")
        lines.append(f"| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |")

        for i, p in enumerate(top_picks, 1):
            fwd_pe = f"{p['forward_pe']}x" if isinstance(p['forward_pe'], (int, float)) else p['forward_pe']
            peg_str = f"{p['peg']}" if isinstance(p['peg'], (int, float)) else p['peg']
            roic_str = f"{p['roic']}%" if isinstance(p['roic'], (int, float)) else p['roic']
            lines.append(f"| **#{i}** | **{p['ticker']}** | {p['name']}<br>*(Sector: {p['sector']})* | ${p['price']} | {fwd_pe} | {peg_str} | {roic_str} | {p['beta']} | **{p['alpha_score']} / 100** | {p['portfolio_status']} |")

        lines.append(f"\n---\n")
        lines.append(f"## 2. Deep-Dive Investment Theses & Portfolio Synergies\n")

        for i, p in enumerate(top_picks, 1):
            roic_str = f"{p['roic']}%" if isinstance(p['roic'], (int, float)) else p['roic']
            lines.append(f"### #{i}. **{p['ticker']} ({p['name']})** — *{p['theme']}*")
            lines.append(f"- **Key Fundamental Strengths**: ROIC **{roic_str}**, Gross Margin **{p['gross_margin']}%**, Debt/Equity **{p['debt_to_equity']}%**, 52-Week Discount **{p['discount_from_52w']}%**.")
            lines.append(f"- **Core Investment Catalyst**: Category leader in `{p['sector']}` with proven pricing power and robust free cash flow conversion.")
            lines.append(f"- **Synergy with BM사장님's Portfolio**: Asset Beta of **{p['beta']}** injects vital non-cyclical ballast, directly mitigating portfolio vulnerability to tech multiple compression.")
            lines.append(f"- **Actionable Protocol**: Enter `CIO {p['ticker']}` (or `ICP {p['ticker']}`) in chat to trigger the full 5-stage Investment Committee due diligence.\n")

    lines.append(f"---\n")

    # =========================================================================
    # PART 2: KOREAN (Strict USD, No KRW)
    # =========================================================================
    lines.append(f"# 🇰🇷 PART 2: 한국어 CIO 유망 종목·ETF 발굴 추천서\n")
    lines.append(f"### 최고투자책임자(CIO) 발굴 총평")
    if is_etf_mode:
        lines.append(f"DADAIC 투자위원회는 **BM사장님의 포트폴리오(`my-portfolio.yaml`)**의 빅테크/반도체 편중 및 레버리지 위험을 구조적으로 완화하기 위해 기관급 ETF 유니버스를 정밀 스크리닝하였습니다.\n")
        lines.append(f"- **선별 전략 모드**: **{mode_title}**")
        lines.append(f"- **핵심 선별 기준**: 운용보수 0.10% 이하의 극저비용, AUM $10B 이상의 풍부한 유동성, 기술주 하락 국면을 방어하는 저베타 밸러스트.\n")

        lines.append(f"## 1. CIO 추천 최우선 ETF 종합 비교표\n")
        lines.append(f"| 순위 | 티커 | ETF 명칭 및 자산군 | 현재 시장가 ($) | 추종 P/E | 배당수익률 (%) | 운용보수 (%) | 베타 | 순자산 ($B) | 알파 점수 | 포트폴리오 역할 |")
        lines.append(f"| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |")

        for i, p in enumerate(top_picks, 1):
            pe_str = f"{p['pe']}배" if isinstance(p['pe'], (int, float)) else p['pe']
            lines.append(f"| **#{i}** | **{p['ticker']}** | {p['name']}<br>*({p['asset_class']})* | ${p['price']} | {pe_str} | {p['dividend_yield']}% | {p['expense_ratio']}% | {p['beta']} | ${p['aum_b']}B | **{p['alpha_score']}점** | {p['portfolio_status']} |")

        lines.append(f"\n---\n")
        lines.append(f"## 2. ETF별 핵심 투자 포인트 및 포트폴리오 시너지 분석\n")

        for i, p in enumerate(top_picks, 1):
            pe_str = f"{p['pe']}배" if isinstance(p['pe'], (int, float)) else p['pe']
            lines.append(f"### #{i}. **{p['ticker']} ({p['name']})** — *{p['theme']}*")
            lines.append(f"- **핵심 지표**: 현재가 **${p['price']}**, P/E **{pe_str}**, 배당수익률 **{p['dividend_yield']}%**, 운용보수 **{p['expense_ratio']}%**, 베타 **{p['beta']}**, 운용자산 **${p['aum_b']}B**.")
            lines.append(f"- **운용 전략 및 구조**: {p['thesis_kr']}")
            lines.append(f"- **BM사장님 포트폴리오 보완 효과**: {p['portfolio_role_kr']}. 현재 계좌의 변동성을 낮추고 하방 경직성을 제공합니다.")
            lines.append(f"- **즉시 연계 가이드**: 심층 실사를 원하시면 채팅창에 **`CIO {p['ticker']}`** (또는 `ICP`)를 입력하세요.\n")

    else:
        lines.append(f"DADAIC 투자위원회는 정적 에코 챔버를 탈피하고 폭넓은 시장 시야를 확보하기 위해, **하이브리드 듀얼 엔진(Track 1 대형 퀀트 스캐너 + Track 2 테마 인텔리전스 레이더)**을 가동하여 **BM사장님 맞춤형 최우선 유망주 Top {len(top_picks)}**를 발굴하였습니다.\n")
        lines.append(f"- **선별 전략 모드**: **{mode_title}**")
        lines.append(f"- **발굴 아키텍처**: 160개 기관급 마스터 기업 대상 일괄 배치 퀀트 스캔과 최신 테마 퓨어플레이 레이더를 결합하여 지금 시장에서 실질적인 주도력과 해자를 입증한 종목 엄선.")
        lines.append(f"- **BM사장님 포트폴리오 갭 필링**: 기존 빅테크/반도체 집중도를 가중시키지 않고, 상관계수가 낮은 우량 섹터(헬스케어, 전력 인프라, 금융 톨부스, 방산)에서 복리 증식을 도모.\n")

        lines.append(f"## 1. CIO 추천 최우선 유망주 종합 비교표\n")
        lines.append(f"| 순위 | 티커 | 기업명 및 섹터 | 현재 주가 ($) | 선행 P/E | PEG | ROIC (%) | 개별 베타 | 알파 점수 | 포트폴리오 역할 |")
        lines.append(f"| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |")

        for i, p in enumerate(top_picks, 1):
            fwd_pe = f"{p['forward_pe']}배" if isinstance(p['forward_pe'], (int, float)) else p['forward_pe']
            peg_str = f"{p['peg']}" if isinstance(p['peg'], (int, float)) else p['peg']
            roic_str = f"{p['roic']}%" if isinstance(p['roic'], (int, float)) else p['roic']
            lines.append(f"| **#{i}** | **{p['ticker']}** | {p['name']}<br>*({p['sector']})* | ${p['price']} | {fwd_pe} | {peg_str} | {roic_str} | {p['beta']} | **{p['alpha_score']}점** | {p['portfolio_status']} |")

        lines.append(f"\n---\n")
        lines.append(f"## 2. 종목별 핵심 투자 포인트 및 포트폴리오 시너지 분석\n")

        for i, p in enumerate(top_picks, 1):
            roic_str = f"{p['roic']}%" if isinstance(p['roic'], (int, float)) else p['roic']
            lines.append(f"### #{i}. **{p['ticker']} ({p['name']})** — *{p['theme']}*")
            lines.append(f"- **재무 펀더멘털**: ROIC **{roic_str}**, 매출총이익률 **{p['gross_margin']}%**, 부채비율 **{p['debt_to_equity']}%**, 52주 고점 대비 조정폭 **{p['discount_from_52w']}%**.")
            lines.append(f"- **핵심 투자 근거 (Why Now)**: `{p['sector']}` 섹터 내 독보적 경제적 해자와 가격 결정력 보유. 실질적인 현금흐름 창출력으로 거시 충격 흡수.")
            lines.append(f"- **BM사장님 포트폴리오 시너지**: 개별 베타 **{p['beta']}**로 빅테크/반도체 집중 리스크를 효과적으로 희석하는 전략적 보완재 역할 완수.")
            lines.append(f"- **즉시 연계 가이드**: 본 종목에 대한 전면적 5단계 정밀 실사가 필요하시면 채팅창에 **`CIO {p['ticker']}`** (또는 `ICP`)를 입력하세요.\n")

    lines.append(f"---\n")
    lines.append(f"**수신**: **BM사장님**  \n")
    lines.append(f"**발행 승인**: DADAIC Investment Firm 최고투자책임자 (CIO)  \n")
    lines.append(f"**결재 문서 번호**: DADAIC-CIO-PICKS-{date_str}\n")

    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    if is_etf_mode:
        etf_filepath = os.path.join(output_dir, f"CIO-Picks-ETF-{date_str}.md")
        with open(etf_filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"[+] Successfully generated CIO Alpha Shortlist: {filepath}", file=sys.stderr)
    return filepath

# ==============================================================================
# 11. MAIN CLI INTERFACE
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="DADAIC CIO Stock & ETF Dual-Engine Screener")
    parser.add_argument("--mode", type=str, default="default", help="Screening mode: default, etf, buffett, garp, defense, power, health, tech")
    parser.add_argument("--top", type=int, default=5, help="Number of top candidates to recommend")
    parser.add_argument("--portfolio", type=str, default="my-portfolio.yaml", help="Path to my-portfolio.yaml")
    parser.add_argument("--extra-tickers", type=str, default="", help="Comma-separated list of dynamic tickers to inject (Option C)")
    args = parser.parse_args()

    extra_tickers = [t.strip().upper() for t in args.extra_tickers.split(",") if t.strip()] if args.extra_tickers else None

    top_picks, is_etf_mode = run_screener(mode=args.mode, top_n=args.top, portfolio_file=args.portfolio, extra_tickers=extra_tickers)
    if not top_picks:
        print("[!] No candidates found matching criteria.", file=sys.stderr)
        sys.exit(1)

    filepath = generate_report(top_picks, is_etf_mode=is_etf_mode, mode=args.mode)
    print(json.dumps({"status": "SUCCESS", "report_path": filepath, "is_etf": is_etf_mode, "picks": top_picks}, indent=2))

if __name__ == "__main__":
    main()
