#!/usr/bin/env python3
"""
DADAIC Investment Firm - Master Media Generator for AMD
Generates all 8 institutional deliverables:
1. AMD-Investment-Committee-Decision-Memo-Slide-EN-261006.html
2. AMD-Investment-Committee-Decision-Memo-Slide-EN-261006.pdf
3. AMD-Investment-Committee-Decision-Memo-Slide-KR-261006.html
4. AMD-Investment-Committee-Decision-Memo-Slide-KR-261006.pdf
5. AMD-Investment-Committee-Decision-Memo-Infographic-EN-261006.html
6. AMD-Investment-Committee-Decision-Memo-Infographic-EN-261006.png
7. AMD-Investment-Committee-Decision-Memo-Infographic-KR-261006.html
8. AMD-Investment-Committee-Decision-Memo-Infographic-KR-261006.png
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
  padding: 44px 64px;
  overflow: hidden;
  background: radial-gradient(circle at 90% 10%, rgba(239, 68, 68, 0.05) 0%, transparent 45%),
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
  color: #dc2626;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  background: #fef2f2;
  padding: 8px 20px;
  border-radius: 24px;
  border: 1px solid #fecaca;
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
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
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
# INFOGRAPHIC CSS (High-Contrast, Portrait Poster)
# ------------------------------------------------------------------------------
INFOGRAPHIC_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

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
  width: 1120px;
  background: #ffffff;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.hero-header {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
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
  color: #fca5a5;
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid rgba(239, 68, 68, 0.4);
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
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.15);
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
  color: #fbbf24;
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
  padding: 18px 20px;
}

.m-label {
  font-size: 13px;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
}

.m-val {
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  font-weight: 800;
  color: #0f172a;
  margin-top: 4px;
}

.m-sub {
  font-size: 13px;
  font-weight: 600;
  margin-top: 4px;
}

.text-emerald { color: #059669; }
.text-rose { color: #e11d48; }
.text-amber { color: #d97706; }
.text-blue { color: #2563eb; }

table.info-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
}

table.info-table th {
  background: #f8fafc;
  color: #475569;
  text-align: left;
  padding: 14px 16px;
  font-weight: 700;
  border-bottom: 2px solid #e2e8f0;
}

table.info-table td {
  padding: 14px 16px;
  border-bottom: 1px solid #f1f5f9;
  color: #334155;
  vertical-align: top;
  line-height: 1.5;
}

.footer-bar {
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
  padding: 22px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: #64748b;
  font-weight: 500;
}
"""

print("[*] Media generation script initialized.")
