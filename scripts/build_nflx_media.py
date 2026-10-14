"""NFLX media builder: bilingual 7-slide 16:9 decks (HTML+PDF) and portrait infographics (HTML+PNG).
Bright theme, DADAIC slide typography protocol (H1 42px/800, stat 36px/900, card title 23px, body 18.5px lh 1.7)."""
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "DecisionMemo", "Media")
os.makedirs(MEDIA, exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
D = json.load(open(os.path.join(ROOT, "scripts", "nflx_data.json")))
DATE = "261007"
K = 0  # 0 = EN, 1 = KR


def t(en, kr):
    return en if K == 0 else kr


FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Outfit:wght@600;700;800;900&family=Noto+Sans+KR:wght@400;600;700;800;900&display=swap" rel="stylesheet">'

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter','Noto Sans KR','Malgun Gothic',sans-serif;color:#0f172a;background:#e9eef6}
.o{font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif}
.card{background:#fff;border:1px solid #e2e8f0;border-radius:18px;padding:20px 24px;box-shadow:0 6px 18px rgba(15,23,42,.06);overflow:hidden}
.card h3{font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif;font-size:23px;font-weight:800;margin-bottom:8px;color:#0f172a}
.card p,.card li{font-size:18.5px;line-height:1.7}
.card ul{padding-left:22px}
.chip{display:inline-block;padding:3px 12px;border-radius:999px;font-weight:800;font-size:15.5px;line-height:1.5;white-space:nowrap}
.c-red{background:#fee2e2;color:#b91c1c}.c-green{background:#d1fae5;color:#047857}.c-amber{background:#fef3c7;color:#b45309}.c-blue{background:#dbeafe;color:#1d4ed8}.c-slate{background:#e2e8f0;color:#334155}
.box{border-radius:16px;padding:16px 20px;font-size:18.5px;line-height:1.6}
.box b.h{display:block;font-size:20px;margin-bottom:4px;font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif}
.b-red{background:#fff1f2;border-left:8px solid #E50914}.b-blue{background:#eff6ff;border-left:8px solid #2563eb}
.b-green{background:#ecfdf5;border-left:8px solid #059669}.b-amber{background:#fffbeb;border-left:8px solid #d97706}
.b-violet{background:#f5f3ff;border-left:8px solid #7c3aed}
table{width:100%;border-collapse:collapse}
th,td{font-size:18px;padding:8px 10px;border-bottom:1px solid #e2e8f0;text-align:left;line-height:1.45;vertical-align:top}
th{background:#0f172a;color:#fff;font-weight:700}
tr:nth-child(even) td{background:#f8fafc}
.pos{color:#047857;font-weight:800}.neg{color:#b91c1c;font-weight:800}
.stat .l{font-size:16px;color:#64748b;font-weight:700;letter-spacing:.3px;text-transform:uppercase}
.stat .v{font-family:'Outfit','Noto Sans KR',sans-serif;font-size:36px;font-weight:900;line-height:1.15;margin:4px 0}
.stat .s{font-size:17px;color:#475569;line-height:1.5}
"""

SLIDE_CSS = BASE_CSS + """
@page{size:1920px 1080px;margin:0}
.slide{width:1920px;height:1080px;padding:38px 56px 24px;background:linear-gradient(135deg,#ffffff 0%,#f4f7ff 55%,#fff4f4 100%);position:relative;overflow:hidden;page-break-after:always;break-after:page;display:flex;flex-direction:column;gap:16px}
.slide:last-child{page-break-after:auto}
.hdr{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:4px solid #E50914;padding-bottom:10px}
.hdr h1{font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif;font-size:42px;font-weight:800;letter-spacing:-.4px;line-height:1.15}
.hdr .sub{font-size:20px;color:#475569;margin-top:6px}
.tag{background:#E50914;color:#fff;font-weight:800;font-size:18px;padding:8px 16px;border-radius:10px;white-space:nowrap}
.grid{display:grid;gap:18px;flex:1;min-height:0;align-items:stretch}
.grid>.card{display:flex;flex-direction:column;justify-content:space-between}
.boxes{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.ftr{display:flex;justify-content:space-between;font-size:15px;color:#94a3b8;border-top:1px solid #e2e8f0;padding-top:8px}
"""

INFO_CSS = BASE_CSS + """
body{background:#fff}
.page{width:1200px;min-height:3620px;padding:38px 44px;background:linear-gradient(180deg,#fff 0%,#f5f8ff 50%,#fff6f6 100%);display:flex;flex-direction:column;justify-content:space-between;gap:20px}
.hero{background:linear-gradient(120deg,#E50914 0%,#b20710 60%,#7f1d1d 100%);color:#fff;border-radius:24px;padding:34px 38px}
.hero .k{font-size:18px;font-weight:700;opacity:.9;letter-spacing:1px;text-transform:uppercase}
.hero h1{font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif;font-size:50px;font-weight:900;line-height:1.1;margin:8px 0}
.hero .vd{display:inline-block;background:#fff;color:#b20710;font-weight:900;font-size:24px;padding:10px 18px;border-radius:12px;margin-top:10px}
.hero .cro{display:inline-block;background:rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:18px;padding:8px 14px;border-radius:10px;margin:10px 0 0 8px}
.sec{font-family:'Outfit','Noto Sans KR','Malgun Gothic',sans-serif;font-size:30px;font-weight:900;border-left:10px solid #E50914;padding-left:14px;margin-top:6px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:18px}.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.foot{font-size:15px;color:#64748b;text-align:center;padding-top:8px;border-top:1px solid #e2e8f0}
"""

# ------------------------------------------------------------------ charts

def svg_price(w=820, h=380):
    m = D["monthly_24"]
    ks = list(m.keys()); vs = list(m.values())
    lo, hi = 50, 140
    pl, pr, pt, pb = 56, 20, 22, 42
    X = lambda i: pl + i * (w - pl - pr) / (len(vs) - 1)
    Y = lambda v: pt + (hi - v) * (h - pt - pb) / (hi - lo)
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vs))
    area = f"{X(0):.1f},{Y(lo):.1f} " + pts + f" {X(len(vs)-1):.1f},{Y(lo):.1f}"
    g = ""
    for v in (60, 80, 100, 120, 140):
        g += f'<line x1="{pl}" y1="{Y(v):.1f}" x2="{w-pr}" y2="{Y(v):.1f}" stroke="#e2e8f0"/><text x="{pl-8}" y="{Y(v)+5:.1f}" font-size="14" text-anchor="end" fill="#64748b">${v}</text>'
    for i, k in enumerate(ks):
        if i % 4 == 0 or i == len(ks) - 1:
            g += f'<text x="{X(i):.1f}" y="{h-14}" font-size="14" text-anchor="middle" fill="#64748b">{k[2:7]}</text>'
    g += f'<line x1="{pl}" y1="{Y(83.68):.1f}" x2="{w-pr}" y2="{Y(83.68):.1f}" stroke="#2563eb" stroke-dasharray="6 5" stroke-width="2"/><text x="{pl+8}" y="{Y(83.68)-7:.1f}" font-size="15" font-weight="800" fill="#2563eb">{t("200D $83.68", "200일선 $83.68")}</text>'
    g += f'<line x1="{pl}" y1="{Y(65.08):.1f}" x2="{w-pr}" y2="{Y(65.08):.1f}" stroke="#059669" stroke-dasharray="6 5" stroke-width="2"/><text x="{pl+8}" y="{Y(65.08)+18:.1f}" font-size="15" font-weight="800" fill="#059669">{t("52W low $65.08", "52주 저점 $65.08")}</text>'
    iath = vs.index(max(vs))
    g += f'<circle cx="{X(iath):.1f}" cy="{Y(vs[iath]):.1f}" r="7" fill="#E50914"/><text x="{X(iath):.1f}" y="{Y(vs[iath])-12:.1f}" font-size="15" font-weight="800" text-anchor="middle" fill="#b91c1c">ATH ${vs[iath]:.2f}</text>'
    g += f'<circle cx="{X(len(vs)-1):.1f}" cy="{Y(vs[-1]):.1f}" r="7" fill="#0f172a"/><text x="{X(len(vs)-1)-10:.1f}" y="{Y(vs[-1])-10:.1f}" font-size="15" font-weight="800" text-anchor="end" fill="#0f172a">${vs[-1]:.2f}</text>'
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><linearGradient id="ga" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E50914" stop-opacity=".22"/><stop offset="1" stop-color="#E50914" stop-opacity="0"/></linearGradient></defs>'
            f'{g}<polygon points="{area}" fill="url(#ga)"/><polyline points="{pts}" fill="none" stroke="#E50914" stroke-width="3.5"/></svg>')


def svg_bars(w=820, h=420):
    yrs = ["FY22", "FY23", "FY24", "FY25", "TTM"]
    rev = [31.62, 33.72, 39.00, 45.18, 48.37]
    fcf = [1.04, 6.59, 6.65, 9.09, 7.86]
    pl, pb, pt = 50, 44, 28
    mx = 55
    gw = (w - pl - 20) / len(yrs)
    bw = gw * 0.34
    Y = lambda v: pt + (mx - v) * (h - pt - pb) / mx
    g = ""
    for v in (0, 10, 20, 30, 40, 50):
        g += f'<line x1="{pl}" y1="{Y(v):.1f}" x2="{w-20}" y2="{Y(v):.1f}" stroke="#eef2f7"/><text x="{pl-8}" y="{Y(v)+5:.1f}" font-size="14" text-anchor="end" fill="#64748b">${v}B</text>'
    for i, y in enumerate(yrs):
        x0 = pl + i * gw + gw * 0.14
        g += f'<rect x="{x0:.1f}" y="{Y(rev[i]):.1f}" width="{bw:.1f}" height="{Y(0)-Y(rev[i]):.1f}" rx="6" fill="#E50914"/>'
        g += f'<text x="{x0+bw/2:.1f}" y="{Y(rev[i])-7:.1f}" font-size="15" font-weight="800" text-anchor="middle" fill="#b91c1c">{rev[i]:.1f}</text>'
        x1 = x0 + bw + 6
        g += f'<rect x="{x1:.1f}" y="{Y(fcf[i]):.1f}" width="{bw:.1f}" height="{Y(0)-Y(fcf[i]):.1f}" rx="6" fill="#059669"/>'
        g += f'<text x="{x1+bw/2:.1f}" y="{Y(fcf[i])-7:.1f}" font-size="15" font-weight="800" text-anchor="middle" fill="#047857">{fcf[i]:.2f}</text>'
        g += f'<text x="{x0+bw+3:.1f}" y="{h-16}" font-size="15" font-weight="700" text-anchor="middle" fill="#334155">{y}</text>'
    lg = (f'<rect x="{pl+10}" y="4" width="16" height="16" rx="3" fill="#E50914"/><text x="{pl+32}" y="17" font-size="15" fill="#334155">{t("Revenue ($B)", "매출 ($B)")}</text>'
          f'<rect x="{pl+170}" y="4" width="16" height="16" rx="3" fill="#059669"/><text x="{pl+192}" y="17" font-size="15" fill="#334155">{t("True FCF net of SBC ($B, TTM ex-$2.8B fee)", "진성 FCF·SBC 차감 ($B, TTM은 $2.8B 일회성 제외)")}</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{lg}{g}</svg>'


def hbars(items, maxv, w=560):
    out = ""
    for lab, v, c, txt in items:
        out += (f'<div style="display:flex;align-items:center;gap:12px;margin:8px 0"><div style="width:170px;font-size:17.5px;font-weight:700">{lab}</div>'
                f'<div style="flex:1;background:#f1f5f9;border-radius:8px;height:30px;position:relative"><div style="width:{min(v/maxv,1)*100:.1f}%;background:{c};height:30px;border-radius:8px"></div></div>'
                f'<div style="width:96px;text-align:right;font-weight:900;font-size:19px;font-family:Outfit">{txt}</div></div>')
    return out


def ladder(w=560, h=430):
    # Uniformly spaced rows in price order so closely grouped prices ($75.42/$72.24/$69.70/$65.08) never collide.
    lv = [("$102.70", t("Bull target (26x)", "강세 목표 (26배)"), "#047857", "#ecfdf5"),
          ("$83.68", t("200-DMA · Base target $83.60", "200일선 · 기준 목표 $83.60"), "#1d4ed8", "#eff6ff"),
          ("$75.42", t("50-DMA · Target 1", "50일선 · 1차 목표"), "#2563eb", "#f8fafc"),
          ("$72.24", t("20-DMA resistance", "20일선 저항"), "#475569", "#f8fafc"),
          ("$69.70", t("CURRENT PRICE (10/07)", "현재가 (10/07)"), "#ffffff", "#0f172a"),
          ("$62.5–67", t("Approved buy zone (20–25% MoS)", "승인 매수 밴드 (안전마진 20~25%)"), "#047857", "#d1fae5"),
          ("$65.08", t("52W low · Tranche 2 limit $65.00", "52주 저점 · 2차 지정가 $65.00"), "#059669", "#ecfdf5"),
          ("$60.50", t("Hard stop (added shares)", "추가 매수분 손절선"), "#b91c1c", "#fff1f2"),
          ("$55.20", t("Bear value · core review trigger", "약세 가치 · 핵심 보유 재검토"), "#b91c1c", "#fef2f2")]
    rh = (h - 10) / len(lv)
    g = ""
    for i, (px, lab, fg, bg) in enumerate(lv):
        y = 5 + i * rh
        stroke = "#0f172a" if fg == "#ffffff" else "#e2e8f0"
        g += f'<rect x="4" y="{y:.1f}" width="{w-8}" height="{rh-5:.1f}" rx="9" fill="{bg}" stroke="{stroke}"/>'
        g += f'<text x="18" y="{y+rh/2+4:.1f}" font-size="18" font-weight="900" fill="{fg}" font-family="Outfit">{px}</text>'
        g += f'<text x="148" y="{y+rh/2+4:.1f}" font-size="16.5" font-weight="700" fill="{fg}">{lab}</text>'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{g}</svg>'


# ------------------------------------------------------------------ slide pieces

def hdr(title, sub, tag):
    return f'<div class="hdr"><div><h1>{title}</h1><div class="sub">{sub}</div></div><div class="tag">{tag}</div></div>'


def ftr(n):
    return (f'<div class="ftr"><span>DADAIC Investment Firm · {t("Investment Committee", "투자위원회")} · DADAIC-IC-MEMO-NFLX-{DATE} · {t("Prepared for BM사장님", "BM사장님 전용 보고")}</span>'
            f'<span>{t("All figures USD · Live data 2026-10-07 close", "모든 수치 USD(달러) · 2026-10-07 종가 기준")} · {n} / 7</span></div>')


def stat(l, v, s, color="#0f172a"):
    return f'<div class="card stat"><div class="l">{l}</div><div class="v" style="color:{color}">{v}</div><div class="s">{s}</div></div>'


def box(cls, head, body):
    return f'<div class="box {cls}"><b class="h">{head}</b>{body}</div>'


def slide1():
    s = hdr(t("NFLX · Investment Committee Decision", "NFLX · 투자위원회 최종 의결"),
            t("Netflix, Inc. (NASDAQ) · Tech Platform / Subscription + Ads · Existing holding: 340 shares · Meeting 2026-10-07",
              "넷플릭스 (NASDAQ) · 테크 플랫폼 / 구독+광고 · 기존 보유 340주 · 2026년 10월 7일 의결"), t("5-STAGE PIPELINE", "5단계 파이프라인"))
    verdict = f'''<div class="card" style="background:linear-gradient(140deg,#fff 0%,#fff1f2 100%);border:2px solid #fecaca;display:flex;flex-direction:column;gap:12px">
      <div class="stat"><div class="l">{t("Official Verdict", "최종 의결")}</div></div>
      <div class="o" style="font-size:44px;font-weight:900;color:#b20710;line-height:1.12">{t("HOLD CORE +<br>CONDITIONAL ACCUMULATE", "핵심 보유 +<br>조건부 분할 매수")}</div>
      <div><span class="chip c-amber" style="font-size:18px">{t("CRO: APPROVED · CONDITIONAL CAP · MAX 3.0%", "CRO: 승인 · 조건부 상한 · 최대 3.0%")}</span></div>
      <ul style="margin-top:4px">
        <li>{t("<b>Business intact</b>: revenue +13%, Q2 op. margin 33.4%, FY25 true FCF <b>$9.09B</b>, S&P 'A'.", "<b>사업은 건재</b>: 매출 +13%, 2분기 영업이익률 33.4%, FY25 진성 FCF <b>$9.09B</b>, S&P 'A'.")}</li>
        <li>{t("<b>Not a chase</b>: 16.6% below base fair value is short of the 20–30% margin of safety.", "<b>추격 매수 불가</b>: 기준 공정가치 대비 16.6% 할인으로 20~30% 안전마진에 미달.")}</li>
        <li>{t("<b>Stage 350 shares</b> after the Oct 20 print + at $65 support, funded by trimming 100 NVDA.", "<b>350주 분할 매수</b>: 10월 20일 실적 확인 후 + $65 지지선, NVDA 100주 매도로 조달.")}</li>
      </ul></div>'''
    stats = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">' + "".join([
        stat(t("Price (10/07 close)", "현재가 (10/07 종가)"), "$69.70", t("1Y −41.5% · −48% vs ATH", "1년 −41.5% · 최고가 대비 −48%"), "#b91c1c"),
        stat(t("Conservative IV", "보수적 내재가치"), "$74.78", t("DCF $65.95 ⊕ 22x P/E $83.60", "DCF $65.95 ⊕ P/E 22배 $83.60")),
        stat(t("12M Base Target", "12개월 기준 목표가"), "$83.60", t("+19.9% · Prob-wtd $81.28", "+19.9% · 확률가중 $81.28"), "#047857"),
        stat(t("Accumulate Zone", "분할매수 구간"), "$62.5–67", t("20–25% margin of safety", "20~25% 안전마진"), "#059669"),
        stat(t("Position Plan", "보유 계획"), "340→690", t("1.36% → 2.75% (cap 3.0%)", "1.36% → 2.75% (상한 3.0%)"), "#1d4ed8"),
        stat(t("Binary Catalyst", "결정적 이벤트"), t("Oct 20", "10월 20일"), t("Q3: guide $12.86B · 33.2% OM", "3분기: 가이던스 $12.86B · 33.2%"), "#7c3aed"),
    ]) + "</div>"
    main = f'<div class="grid" style="grid-template-columns:0.92fr 1.08fr">{verdict}{stats}</div>'
    boxes = '<div class="boxes">' + box("b-green", t("✅ Fortress Fundamentals", "✅ 요새급 펀더멘털"), t("ROE 41% (FY25 DuPont) · net debt 0.37x EBITDA · SBC ≈1% of revenue · $27.1B buyback capacity.", "ROE 41%(FY25 듀폰) · 순부채 EBITDA 0.37배 · SBC 매출의 약 1% · 자사주 매입 여력 $27.1B.")) + \
        box("b-red", t("⚠️ Attention-Share War", "⚠️ 시청 점유율 전쟁"), t("Nielsen Jul-26: YouTube <b>14.2%</b> vs Netflix <b>7.8%</b>. WFC → UW ($57), HSBC → Hold ($76). Skydance (Paramount+WBD) closed Oct 6.", "닐슨 7월: 유튜브 <b>14.2%</b> vs 넷플릭스 <b>7.8%</b>. 웰스파고 UW($57), HSBC Hold($76). 스카이댄스(파라마운트+WBD) 10/6 합병 완료.")) + \
        box("b-blue", t("🧭 True Diversifier", "🧭 진정한 분산 자산"), t("2Y beta vs SPY <b>0.70</b>, correlation <b>0.33</b>; zero AI-capex linkage vs. a book that is ~77% AI-factor exposed.", "SPY 대비 2년 베타 <b>0.70</b>, 상관계수 <b>0.33</b>. AI 팩터 노출 약 77%인 포트폴리오에서 AI 설비투자와 무관.")) + "</div>"
    return f'<section class="slide">{s}{main}{boxes}{ftr(1)}</section>'


def slide2():
    s = hdr(t("Multi-Year Empirical Validation", "다개년 실증 데이터 전수 검증"), t("BM사장님 30-Year Mandate · 1Y / 3Y / 5Y / 10Y returns, FCF trajectory, solvency, drawdown resilience", "BM사장님 30년 원칙 · 1/3/5/10년 수익률, FCF 궤적, 재무 건전성, 하락장 방어력"), t("VALUE-TRAP TEST: PASSED", "가치함정 검증: 통과"))
    rows = [
        (t("1-Year Return", "1년 수익률"), '<span class="neg">−41.5%</span> ($119.11 → $69.70)', t("vs SPY +17.4%", "SPY +17.4% 대비"), "c-red", t("Sentiment trough", "심리 바닥")),
        (t("3-Year Return", "3년 수익률"), '<span class="pos">+82.7%</span> (CAGR +22.2%)', t("Ad tier + paid sharing", "광고 요금제+공유 단속"), "c-green", t("Compounding", "복리 성장")),
        (t("5-Year Return", "5년 수익률"), '+10.3% (CAGR +2.0%)', t("2022 crash + 2026 de-rating", "2022 폭락 + 2026 디레이팅"), "c-amber", t("Multiple only", "멀티플 압축")),
        (t("10-Year CAGR", "10년 CAGR"), '<span class="pos">+20.9%</span>', t("No dividend", "무배당"), "c-green", t("Elite", "최상위")),
        (t("True FCF (net SBC)", "진성 FCF"), "$1.04B → $6.59B → $6.65B → <b>$9.09B</b>", "FY22 → FY25", "c-green", t("9x in 3Y", "3년 9배")),
        (t("Balance Sheet", "재무구조"), t("Net debt $5.3B · 17x interest cover", "순부채 $5.3B · 이자보상 17배"), "S&P 'A' Stable", "c-green", t("Fortress", "요새급")),
        (t("Drawdown", "최대 낙폭"), t('2022 MDD <span class="neg">−75.9%</span> · now −48%', '2022년 <span class="neg">−75.9%</span> · 현재 −48%'), t("β 0.70 / ρ 0.33", "β 0.70 / ρ 0.33"), "c-amber", t("Fragile on scares", "공포에 취약")),
    ]
    tb = f'<table><tr><th>{t("Metric", "지표")}</th><th>{t("Audited Fact", "실증 데이터")}</th><th>{t("Context", "맥락")}</th><th>{t("Verdict", "판정")}</th></tr>' + "".join(
        f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td><span class="chip {d}">{e}</span></td></tr>' for a, b, c, d, e in rows) + "</table>"
    left = f'<div class="card"><h3>{t("Empirical Scorecard", "실증 성적표")}</h3>{tb}</div>'
    right = f'<div class="card"><h3>{t("24-Month Price Path — De-rating, Not Decay", "24개월 주가 궤적 — 사업 훼손이 아닌 디레이팅")}</h3>{svg_price()}<p style="font-size:17.5px;color:#475569;margin-top:4px">{t("ATH $133.91 (Jun-25) → $69.70. Forward P/E compressed from ~45x to <b>18.3x</b> while revenue grew +24% since mid-2024.", "최고가 $133.91(2025년 6월) → $69.70. 같은 기간 매출이 증가했음에도 선행 P/E는 약 45배에서 <b>18.3배</b>로 압축.")}</p></div>'
    main = f'<div class="grid" style="grid-template-columns:1.02fr 0.98fr">{left}{right}</div>'
    boxes = '<div class="boxes">' + box("b-green", t("Revenue Compounding", "매출 복리 성장"), t("FY22 $31.6B → FY25 $45.2B → TTM $48.4B; FY26 guide $51.0–51.4B (+13%).", "FY22 $31.6B → FY25 $45.2B → TTM $48.4B, FY26 가이던스 $51.0~51.4B (+13%).")) + \
        box("b-amber", t("Value-Trap Verdict", "가치함정 판정"), t("5Y price CAGR +2.0% came entirely from multiple compression; true FCF +770%. <b>No capital erosion.</b>", "5년 주가 CAGR +2.0%는 전적으로 멀티플 압축 때문이며 진성 FCF는 +770%. <b>자본 잠식 없음.</b>")) + \
        box("b-red", t("Drawdown Caveat", "낙폭 주의"), t("The −75.9% 2022 MDD proves NFLX can halve on growth scares. Sizing must stay satellite-level (≤3%).", "2022년 −75.9% 낙폭은 성장 공포 시 반토막 가능성을 입증. 비중은 위성 수준(≤3%) 유지.")) + "</div>"
    return f'<section class="slide">{s}{main}{boxes}{ftr(2)}</section>'


def slide3():
    s = hdr(t("Forensic Financials & Health Scorecard", "포렌식 재무 및 건전성 성적표"), t("10-K / 10-Q audit · one-time $2.8B WBD termination fee (received Q1'26) stripped from all run-rate metrics", "10-K/10-Q 감사 · 2026년 1분기 수취한 WBD 해지 수수료 $2.8B(일회성)를 모든 지표에서 제거"), t("FORENSIC GRADE: A", "포렌식 등급: A"))
    left = f'<div class="card"><h3>{t("Revenue vs. True FCF (net of SBC)", "매출 vs 진성 FCF (SBC 차감)")}</h3>{svg_bars()}</div>'
    sc = [
        (t("Macro", "매크로"), "c-red", t("Headwind", "역풍"), t("Fed +25bp → 3.75–4.00% (9/16); 10Y ~5.3%", "연준 +25bp → 3.75~4.00%(9/16), 10년물 약 5.3%")),
        (t("Forensic", "포렌식"), "c-green", "A", t("'A' credit · 0.37x net debt/EBITDA", "'A' 등급 · 순부채/EBITDA 0.37배")),
        (t("True FCF", "진성 FCF"), "c-green", "$9.09B", t("FY25 · TTM ex-fee $7.86B", "FY25 · TTM 일회성 제외 $7.86B")),
        (t("Moat", "해자"), "c-amber", t("Stable / Narrowing", "안정 / 축소"), t("Monetization strong, attention share slipping", "수익화 견고, 시청 점유율 하락")),
        (t("Earnings", "실적"), "c-amber", t("In-line, soft guide", "부합·가이던스 약세"), t("Q2 EPS $0.80 vs $0.79 · stock −8%", "2분기 EPS $0.80 vs $0.79 · 주가 −8%")),
        (t("Smart Money", "수급"), "c-red", "42/100", t("Co-CEO sales; FMR −33.6% (13F)", "공동 CEO 매도, FMR −33.6%")),
        (t("Sentiment", "센티먼트"), "c-green", "70/100", t("Pessimism peak → contrarian accumulate", "비관 정점 → 역발상 매집")),
        (t("Regulatory", "규제"), "c-amber", t("Moderate watch", "관찰"), t("Brazil CIDE · EU DSA · autoplay suits", "브라질 CIDE · EU DSA · 자동재생 소송")),
    ]
    tb = "<table>" + "".join(f'<tr><td style="width:150px"><b>{a}</b></td><td style="width:200px"><span class="chip {b}">{c}</span></td><td>{d}</td></tr>' for a, b, c, d in sc) + "</table>"
    right = f'<div class="card"><h3>{t("Fundamental, Flow & Forensic Scorecard", "펀더멘털·수급·포렌식 성적표")}</h3>{tb}</div>'
    main = f'<div class="grid" style="grid-template-columns:1fr 1fr">{left}{right}</div>'
    boxes = '<div class="boxes">' + box("b-blue", t("DuPont ROE (FY25)", "듀폰 ROE (FY25)"), t("24.3% net margin × 0.81x turnover × 2.09x leverage ≈ <b>41%</b>. The 49.5% TTM figure is fee-inflated.", "순이익률 24.3% × 회전율 0.81 × 레버리지 2.09 ≈ <b>41%</b>. TTM 49.5%는 일회성 수수료로 부풀려짐.")) + \
        box("b-green", t("Shareholder Yield", "주주환원"), t("FY25 buybacks $9.1B; diluted shares 4.51B → 4.34B (−3.7%, FY22–25); new $25B authorization (Apr-26).", "FY25 자사주 매입 $9.1B, 희석 주식수 4.51B → 4.34B(−3.7%), 2026년 4월 $25B 추가 승인.")) + \
        box("b-amber", t("Normalization", "이익 정상화"), t("FY26 consensus EPS $3.58 includes ~$0.47 of fee benefit → <b>underlying $3.11</b>. FY27E <b>$3.80</b> → 18.3x.", "FY26 컨센서스 EPS $3.58 중 약 $0.47이 수수료 효과 → <b>실질 $3.11</b>. FY27E <b>$3.80</b> → 18.3배.")) + "</div>"
    return f'<section class="slide">{s}{main}{boxes}{ftr(3)}</section>'


MASTERS = [
    ("Warren Buffett", ("Moat & 20–30% MoS", "해자 & 20~30% 안전마진"), ("HOLD · BUY ≤ $67", "보유 · $67 이하 매수"), "c-amber",
     ("325M+ members, scale content economics, pricing power (Mar-26 hike). But the discount to fair value is only 16.6%, short of the 20–30% MoS.",
      "회원 3억 2,500만+, 콘텐츠 규모의 경제, 가격 결정력(2026년 3월 인상). 단 공정가치 대비 할인 16.6%로 안전마진 미달.")),
    ("Charlie Munger", ("ROIC & Inversion", "ROIC & 역발상"), ("QUALITY · FAIR PRICE", "우량 · 적정가"), "c-green",
     ("Capital-light 30% margins. Invert: free YouTube attention (14.2%) could force a content-spend treadmill; a mega-M&A repeat is the other killer.",
      "자본 경량 30% 마진. 역발상: 유튜브(14.2%)의 시간 잠식이 콘텐츠 비용 쳇바퀴를 유발할 수 있고, 대형 인수 재시도가 또 다른 치명 리스크.")),
    ("Peter Lynch", ("Category & PEG", "6분류 & PEG"), ("STALWART · FAIR", "스톨워트 · 적정"), "c-amber",
     ("Fast Grower maturing into a Stalwart. PEG 0.81 (consensus 22.6%) / 1.15 (conservative 16%). Disclosure retreat makes the story harder to track.",
      "고성장주에서 스톨워트로 성숙 중. PEG 0.81(컨센서스 22.6%) / 1.15(보수적 16%). 공시 축소로 스토리 추적이 어려워짐.")),
    ("Stanley Druckenmiller", ("18M Inflection · ≥3:1", "18개월 변곡점 · 3:1"), ("WATCH · 2.3:1", "관망 · 2.3:1"), "c-red",
     ("Ads ~$3B (2x) and live events are real levers, but bull +47% / bear −21% = 2.3:1, and the Fed is hiking with the 10Y at 5.3%. No aggressive size.",
      "광고 약 $3B(2배)·라이브 이벤트는 실질 레버이나 강세 +47%/약세 −21% = 2.3:1, 금리 인상기·10년물 5.3%. 공격적 비중 불가.")),
    ("William J. O'Neil", ("CAN SLIM", "CAN SLIM"), ("LAGGARD · NO BUY", "후발주자 · 매수 불가"), "c-red",
     ("Fails L (RS −41% vs SPY +17%) and M (rate-hike tape). Q3 EPS +40% is on an easy comparison. Needs to reclaim the $83.68 200-DMA on volume.",
      "L(RS −41% vs SPY +17%)·M(금리 인상 장세) 미충족. 3분기 EPS +40%는 기저효과. $83.68 200일선을 거래량 동반 회복해야 함.")),
    ("Market Technician", ("Chart & ≥1:2 R:R", "차트 & 1:2 손익비"), ("SUPPORT BUY · 1:3.2", "지지선 매수 · 1:3.2"), "c-blue",
     ("Bearish stack 69.70 < 72.24 < 75.42 < 83.68; RSI 41. Entry $65–67, stop $60.50, T1 $75.40, T2 $83.60.",
      "역배열 69.70 < 72.24 < 75.42 < 83.68, RSI 41. 진입 $65~67, 손절 $60.50, 1차 $75.40, 2차 $83.60.")),
]


def slide4():
    s = hdr(t("Master Evaluation Matrix", "거장 평가 매트릭스"), t("5 Great Masters + Chief Market Technician · independent verdicts, then CIO arbitration", "5대 거장 + 수석 기술적 분석가 · 독립 판정 후 CIO 중재"), t("CONSENSUS: HOLD / STAGE", "합의: 보유 / 분할"))
    cards = ""
    for name, lens, vd, chip, txt in MASTERS:
        cards += (f'<div class="card"><div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><h3 style="margin:0">{name}</h3><span class="chip {chip}">{t(*vd)}</span></div>'
                  f'<div style="font-size:16.5px;color:#64748b;font-weight:700;margin:4px 0 6px">{t(*lens)}</div><p>{t(*txt)}</p></div>')
    main = f'<div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr">{cards}</div>'
    rec = box("b-violet", t("⚖️ CIO Conflict Reconciliation", "⚖️ CIO 이견 조율"),
              t("The value camp (Buffett/Munger/Lynch) sees an 'A'-credit, 41%-ROE franchise at its cheapest multiple in a decade. The momentum camp (O'Neil/Technician/Druckenmiller) sees a confirmed downtrend, two fresh downgrades and a hiking Fed. <b>Ruling:</b> the business is not broken, but the debate has shifted to <i>“does Netflix still own attention?”</i> and will not resolve before Oct 20. So the firm neither chases at $69.70 nor sells a quality franchise at a sentiment low. <b>Hold 340 sh; stage 350 sh into confirmation and $65 support; cap 3.0%.</b>",
                "가치 진영(버핏·멍거·린치)은 'A' 등급·ROE 41% 프랜차이즈가 10년래 최저 멀티플에 거래된다고 보고, 모멘텀 진영(오닐·기술적 분석가·드러켄밀러)은 확정 하락 추세·연속 하향·금리 인상을 경계합니다. <b>중재:</b> 사업은 훼손되지 않았으나 논쟁이 <i>“넷플릭스가 여전히 시간을 장악하는가”</i>로 바뀌었고 10월 20일 전에는 해소되지 않습니다. $69.70 추격도, 심리 바닥 매도도 하지 않습니다. <b>340주 보유, 실적 확인과 $65 지지선에서 350주 분할 매수, 상한 3.0%.</b>"))
    return f'<section class="slide">{s}{main}{rec}{ftr(4)}</section>'


def slide5():
    s = hdr(t("Competition, Smart Money & Catalyst Calendar", "경쟁 구도 · 스마트머니 · 카탈리스트 캘린더"), t("Stage 2.5 Fact-Check Gatekeeper: 20 claims dual-sourced live · 1 rejected · 3 caveated", "2.5단계 팩트체크: 20개 주장 실시간 이중 검증 · 1건 기각 · 3건 주석"), t("FACT-CHECKED", "팩트체크 완료"))
    att = hbars([(t("YouTube", "유튜브"), 14.2, "#ef4444", "14.2%"), ("Netflix", 7.8, "#E50914", "7.8%"),
                 (t("Streaming total", "스트리밍 전체"), 49.0, "#2563eb", "49.0%")], 50)
    c1 = (f'<div class="card"><h3>{t("US TV Time Share — Nielsen Gauge, Jul-26", "미국 TV 시청 점유율 — 닐슨, 2026년 7월")}</h3>{att}'
          f'<ul style="margin-top:8px"><li>{t("H1-26 global hours <b>97B+ (+2%)</b>, a record; US hours ~−8.6% (3rd-party est.).", "2026년 상반기 글로벌 <b>970억 시간+(+2%)</b> 사상 최대, 미국은 약 −8.6%(제3자 추정).")}</li>'
          f'<li>{t("<b>Skydance Corp.</b> (Paramount+WBD) closed <b>Oct 6, 2026</b>: >200M DTC subs, HBO Max + Paramount+ to unify.", "<b>스카이댄스</b>(파라마운트+WBD) <b>2026년 10월 6일</b> 합병 완료: DTC 2억+, HBO Max·Paramount+ 통합 예정.")}</li>'
          f'<li>{t("Ads ~<b>$3B</b> in 2026 (~2x); 250M+ ad-tier MAV.", "2026년 광고 약 <b>$3B</b>(약 2배), 광고형 월간 시청자 2.5억+.")}</li></ul></div>')
    c2 = (f'<div class="card"><h3>{t("Smart Money — Score 42/100", "스마트머니 — 42/100점")}</h3>'
          f'<table><tr><th>{t("Form 4 (Aug-26)", "Form 4 (8월)")}</th><th>{t("Sold", "매도")}</th></tr>'
          f'<tr><td>{t("Co-CEO Sarandos", "공동CEO 사란도스")}</td><td class="neg">$9.73M</td></tr><tr><td>{t("Co-CEO Peters", "공동CEO 피터스")}</td><td class="neg">$2.01M</td></tr>'
          f'<tr><td>{t("CFO Neumann", "CFO 노이만")}</td><td class="neg">$0.70M</td></tr><tr><td>{t("Open-market buys", "장내 매수")}</td><td><b>0</b></td></tr></table>'
          f'<table style="margin-top:10px"><tr><th>13F Q2-26</th><th>Δ</th></tr><tr><td>FMR</td><td class="neg">−33.6%</td></tr><tr><td>Capital World</td><td class="neg">−11.9%</td></tr>'
          f'<tr><td>State Street / Geode</td><td class="pos">+4.9% / +6.6%</td></tr><tr><td>{t("Short interest", "공매도 비율")}</td><td>2.3%</td></tr></table></div>')
    cal = [(t("Oct 20", "10/20"), t("Q3 print + Q4 guide (EPS est $0.82)", "3분기 실적 + 4분기 가이던스 (EPS 예상 $0.82)"), "#E50914"),
           (t("Nov 25", "11/25"), t("NFL Thanksgiving Eve: GB vs LAR", "NFL 추수감사절 전야: GB vs LAR"), "#2563eb"),
           (t("Dec 25", "12/25"), t("NFL Christmas Day doubleheader", "NFL 크리스마스 더블헤더"), "#2563eb"),
           (t("Jan-27", "2027.1"), t("Q4 print + FY27 margin target", "4분기 실적 + FY27 마진 목표"), "#7c3aed"),
           (t("H1-27", "2027 상반기"), t("Skydance HBO Max/P+ integration", "스카이댄스 HBO Max·P+ 통합"), "#d97706")]
    tl = "".join(f'<div style="display:flex;gap:14px;align-items:flex-start;margin:9px 0"><div style="min-width:96px;background:{c};color:#fff;font-weight:900;border-radius:10px;padding:6px 10px;text-align:center;font-size:17px">{d}</div><div style="font-size:18px;line-height:1.5">{e}</div></div>' for d, e, c in cal)
    c3 = f'<div class="card"><h3>{t("3–6M Catalyst Calendar · Sentiment 70/100", "3~6개월 카탈리스트 · 센티먼트 70점")}</h3>{tl}<p style="font-size:17px;color:#475569;margin-top:6px">{t("Pessimism markers: WFC UW $57 (9/18), HSBC Hold $76 (9/22), weakest Emmys in a decade, Hastings off the board (6/4).", "비관 지표: 웰스파고 UW $57(9/18), HSBC Hold $76(9/22), 10년래 최약 에미상, 헤이스팅스 이사회 퇴진(6/4).")}</p></div>'
    main = f'<div class="grid" style="grid-template-columns:1.05fr 0.9fr 1.05fr">{c1}{c2}{c3}</div>'
    boxes = '<div class="boxes">' + box("b-red", t("❌ Rejected Claim", "❌ 기각된 주장"), t("“Netflix paid a WBD breakup fee” — FALSE. Netflix <b>received $2.8B</b> (Q1-26 NI $5.28B confirms).", "“넷플릭스가 WBD 위약금을 지불” — 거짓. 넷플릭스가 <b>$2.8B을 수취</b>(1분기 순이익 $5.28B로 확인).")) + \
        box("b-green", t("✅ Verified (3+ sources)", "✅ 검증 완료 (3개+ 소스)"), t("Nielsen 14.2%/7.8% · WFC & HSBC downgrades · Q2 results/guide · Fed hike 9/16 · Skydance close 10/6 · Oct 20 date.", "닐슨 14.2%/7.8% · 웰스파고·HSBC 하향 · 2분기 실적/가이던스 · 9/16 금리 인상 · 10/6 스카이댄스 합병 · 10/20 실적일.")) + \
        box("b-amber", t("⚠️ Caveated (single-source)", "⚠️ 주석 (단일 소스)"), t("US hours −8.6% (estimate) · Mar-26 price points · no active DOJ action post-WBD (treated as Watch).", "미국 시청 −8.6%(추정) · 2026년 3월 요금 세부 · WBD 이후 DOJ 무조치(관찰로 처리).")) + "</div>"
    return f'<section class="slide">{s}{main}{boxes}{ftr(5)}</section>'


def slide6():
    s = hdr(t("Valuation Scenarios & Technical Levels", "시나리오 밸류에이션 & 기술적 레벨"), t("FY27E EPS consensus $3.80 (45 analysts) · Street mean target $92.84 (range $57–$135)", "FY27E EPS 컨센서스 $3.80 (45명) · 월가 평균 목표가 $92.84 (범위 $57~$135)"), t("PROB-WEIGHTED $81.28", "확률가중 $81.28"))
    sc = [(t("BULL · 25%", "강세 · 25%"), "$102.70", "+47.3%", t("26x × $3.95 · ads $3B+ re-accelerate, engagement stabilizes", "26배 × $3.95 · 광고 $3B+ 재가속, 시청 안정화"), "#047857", "#ecfdf5"),
          (t("BASE · 50%", "기준 · 50%"), "$83.60", "+19.9%", t("22x × $3.80 · 13% revenue growth, OM 31.5% → 33%", "22배 × $3.80 · 매출 13% 성장, 마진 31.5%→33%"), "#1d4ed8", "#eff6ff"),
          (t("BEAR · 25%", "약세 · 25%"), "$55.20", "−20.8%", t("16x × $3.45 · attention loss forces a content-spend spike", "16배 × $3.45 · 시청 이탈로 콘텐츠 비용 급증"), "#b91c1c", "#fff1f2")]
    cards = "".join(f'<div class="card" style="background:{bg};border-color:{c}55"><div class="stat"><div class="l" style="color:{c}">{a}</div><div class="v" style="color:{c}">{b}</div></div><div class="o" style="font-size:26px;font-weight:900;color:{c}">{r}</div><p style="margin-top:6px">{d}</p></div>' for a, b, r, d, c, bg in sc)
    left = f'<div style="display:flex;flex-direction:column;gap:18px"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;flex:1">{cards}</div>' + \
        f'<div class="card"><h3>{t("Intrinsic Value Triangulation", "내재가치 삼각 측량")}</h3><table><tr><th>{t("Method", "방법")}</th><th>{t("Key assumptions", "핵심 가정")}</th><th>$/sh</th></tr>' + \
        f'<tr><td><b>{t("Strict DCF", "엄격한 DCF")}</b></td><td>{t("FY27E true FCF $10.8B · 13%→8% · g 3% · CoE 9.5%", "FY27E 진성 FCF $10.8B · 13%→8% · 영구 3% · 자기자본비용 9.5%")}</td><td><b>$65.95</b></td></tr>' + \
        f'<tr><td><b>P/E</b></td><td>{t("22x × FY27E EPS $3.80", "22배 × FY27E EPS $3.80")}</td><td><b>$83.60</b></td></tr>' + \
        f'<tr><td><b>{t("Blend (IV)", "블렌드 (내재가치)")}</b></td><td>{t("50 / 50 — conservative anchor", "50/50 — 보수적 기준")}</td><td class="pos">$74.78</td></tr></table></div></div>'
    right = f'<div class="card"><h3>{t("Technical Level Ladder", "기술적 레벨 사다리")}</h3>{ladder()}<p style="font-size:17px;color:#475569">{t("RSI(14) 41.0 · MACD −2.39 < signal −2.12 · reward/risk from $66 ≈ <b>1 : 3.2</b>", "RSI(14) 41.0 · MACD −2.39 < 시그널 −2.12 · $66 기준 손익비 ≈ <b>1 : 3.2</b>")}</p></div>'
    main = f'<div class="grid" style="grid-template-columns:1.25fr 0.75fr">{left}{right}</div>'
    boxes = '<div class="boxes">' + box("b-blue", t("Lynch PEG", "린치 PEG"), t("18.3x ÷ 22.6% consensus = <b>0.81</b>; ÷ 16% conservative = <b>1.15</b> → “fair, not a bargain.”", "18.3배 ÷ 컨센서스 22.6% = <b>0.81</b>, ÷ 보수적 16% = <b>1.15</b> → “적정가, 바겐세일 아님.”")) + \
        box("b-red", t("Druckenmiller Asymmetry", "드러켄밀러 비대칭"), t("+47.3% / −20.8% = <b>2.3 : 1</b> — below the 3:1 bar for aggressive sizing.", "+47.3% / −20.8% = <b>2.3 : 1</b> — 공격적 비중 기준(3:1)에 미달.")) + \
        box("b-green", t("Buffett Margin of Safety", "버핏 안전마진"), t("Today: 16.6% below $83.60. <b>$67.00 = 20% · $62.50 = 25%</b> → the approved accumulation band.", "현재 $83.60 대비 16.6% 할인. <b>$67.00 = 20% · $62.50 = 25%</b> → 승인된 분할매수 밴드.")) + "</div>"
    return f'<section class="slide">{s}{main}{boxes}{ftr(6)}</section>'


def slide7():
    s = hdr(t("Portfolio Fit, CRO Ruling & Execution", "포트폴리오 적합성 · CRO 판정 · 집행 계획"), t("Live book $1,745,865 · 23 holdings · cash 5.7% · portfolio beta 1.56 (ceiling 1.20)", "실시간 총자산 $1,745,865 · 23종목 · 현금 5.7% · 포트폴리오 베타 1.56 (상한 1.20)"), t("CRO CAP 3.0%", "CRO 상한 3.0%"))
    steps = [("1", t("<b>HOLD core 340 sh</b> — no selling at a sentiment trough.", "<b>핵심 340주 보유</b> — 심리 바닥 매도 금지.")),
             ("2", t("<b>Tranche 1: 150 sh (~$10.5K)</b> after Oct 20 <i>only if</i> FY26 guide ≥ $51.0B, 31.5% OM reaffirmed, ads ~2x.", "<b>1차: 150주(약 $10.5K)</b> 10월 20일 이후, FY26 가이던스 ≥ $51.0B·마진 31.5% 재확인·광고 2배 <i>충족 시에만</i>.")),
             ("3", t("<b>Tranche 2: 200 sh @ $65.00 limit (~$13.0K)</b> — 52W-low double-bottom test.", "<b>2차: $65.00 지정가 200주(약 $13.0K)</b> — 52주 저점 쌍바닥 테스트.")),
             ("4", t("<b>Funding: trim 100 NVDA (~$23.7K)</b>; NVDA 20.40% → 19.04%; cash untouched.", "<b>재원: NVDA 100주 매도(약 $23.7K)</b>; NVDA 20.40% → 19.04%, 현금 유지.")),
             ("5", t("<b>Stops:</b> $60.50 on added shares; core reviewed below a $55.20 weekly close.", "<b>손절:</b> 추가분 $60.50, 핵심분은 주봉 $55.20 하회 시 재검토."))]
    st = "".join(f'<div style="display:flex;gap:12px;margin:8px 0"><div style="min-width:38px;height:38px;border-radius:50%;background:#E50914;color:#fff;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:19px">{n}</div><div style="font-size:18px;line-height:1.55">{x}</div></div>' for n, x in steps)
    c1 = f'<div class="card"><h3>{t("Execution Blueprint", "실전 집행 계획")}</h3>{st}</div>'
    c2 = (f'<div class="card"><h3>{t("3-Shock Stress Test (Portfolio MDD)", "3대 충격 스트레스 테스트 (포트폴리오 MDD)")}</h3>'
          f'<table><tr><th>{t("Scenario", "시나리오")}</th><th>NFLX</th><th>{t("Now", "현재")}</th><th>{t("Proposed", "제안")}</th></tr>'
          f'<tr><td>{t("S1 AI-capex digestion", "S1 AI 설비투자 소화")}</td><td>−12%</td><td class="neg">−33.8%</td><td class="neg">−33.3%</td></tr>'
          f'<tr><td>{t("S2 Geopolitical / energy", "S2 지정학·에너지")}</td><td>−15%</td><td class="neg">−26.3%</td><td class="neg">−26.1%</td></tr>'
          f'<tr><td>{t("S3 Higher-for-longer", "S3 고금리 장기화")}</td><td>−25%</td><td class="neg">−24.9%</td><td class="neg">−24.8%</td></tr>'
          f'<tr><td><b>{t("Portfolio beta", "포트폴리오 베타")}</b></td><td>0.70*</td><td>1.56</td><td>1.55</td></tr></table>'
          f'<p style="font-size:15.5px;color:#64748b;margin-top:6px">{t("*2Y realized beta vs SPY; the stress model conservatively uses the 5Y beta of 1.61.", "*SPY 대비 2년 실현 베타. 스트레스 모델은 보수적으로 5년 베타 1.61 적용.")}</p>'
          f'<div class="box b-amber" style="margin-top:8px"><b class="h">{t("CRO Ruling", "CRO 판정")}</b>{t("APPROVED · CONDITIONAL CAP 3.0%. Pre-existing breaches: beta 1.56 > 1.20; cash 5.7% < 15%. Standing order: de-lever KORU/TQQQ/SOXL.", "승인 · 조건부 상한 3.0%. 기존 위반: 베타 1.56 > 1.20, 현금 5.7% < 15%. 상시 지침: KORU/TQQQ/SOXL 디레버리징.")}</div></div>')
    fx = hbars([(t("Semis", "반도체"), 40.8, "#7c3aed", "40.8%"), (t("Big Tech", "빅테크"), 31.1, "#2563eb", "31.1%"), (t("Index ETFs", "지수 ETF"), 14.7, "#64748b", "14.7%"),
                (t("AI infra", "AI 인프라"), 3.3, "#d97706", "3.3%"), (t("Leveraged ETF", "레버리지 ETF"), 2.3, "#b91c1c", "2.3%"), ("NFLX", 1.36, "#E50914", "1.4→2.8%"), (t("Cash", "현금"), 5.7, "#059669", "5.7%")], 45)
    c3 = f'<div class="card"><h3>{t("Factor Exposure — False Diversification", "팩터 노출 — 가짜 분산")}</h3>{fx}<p style="font-size:17.5px;margin-top:8px">{t("~77% of the book rides a single AI-capex factor. NFLX (ρ 0.33) is one of the few true diversifiers, which justifies a larger satellite.", "포트폴리오의 약 77%가 단일 AI 설비투자 팩터에 연동. NFLX(ρ 0.33)는 몇 안 되는 진정한 분산 자산이므로 위성 비중 확대가 정당화됩니다.")}</p></div>'
    main = f'<div class="grid" style="grid-template-columns:1.05fr 1fr 0.95fr">{c1}{c2}{c3}</div>'
    exitb = box("b-red", t("🛑 Non-Negotiable Exit Trigger (100% liquidation)", "🛑 타협 불가 엑시트 트리거 (100% 전량 매도)"),
                t("Revenue growth <b>below 8% YoY for two consecutive quarters AND a full-year operating-margin target cut below 29%</b>, which proves pricing power and ads can no longer offset attention loss to YouTube/Skydance. <b>OR</b> a debt-funded acquisition above <b>$30B</b> (a WBD-bid repeat) pushing net leverage above <b>2.5x EBITDA</b>.",
                  "매출 성장률이 <b>2개 분기 연속 8% 미만이고 동시에 연간 영업이익률 목표가 29% 미만으로 하향</b>되는 경우. 이는 가격 결정력과 광고가 유튜브·스카이댄스로의 시청 이탈을 더 이상 상쇄하지 못한다는 증거입니다. <b>또는</b> 순부채를 <b>EBITDA 2.5배</b> 이상으로 높이는 <b>$30B</b> 초과 차입 인수(WBD 시도 재현)를 발표하는 경우."))
    return f'<section class="slide">{s}{main}{exitb}{ftr(7)}</section>'


def deck():
    lang = "en" if K == 0 else "ko"
    title = t("NFLX Investment Committee Decision Deck", "NFLX 투자위원회 의결 슬라이드")
    return (f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>{title} {DATE}</title>{FONTS}<style>{SLIDE_CSS}</style></head><body>'
            + slide1() + slide2() + slide3() + slide4() + slide5() + slide6() + slide7() + "</body></html>")


# ------------------------------------------------------------------ infographic

def infographic():
    lang = "en" if K == 0 else "ko"
    hero = (f'<div class="hero"><div class="k">DADAIC Investment Committee · {t("Decision", "의결")} 2026-10-07 · {t("Prepared for BM사장님", "BM사장님 전용 보고")}</div>'
            f'<h1>NFLX · Netflix, Inc.</h1><div style="font-size:21px;opacity:.95">{t("Tech Platform · Subscription + Ads · Existing holding 340 shares (1.36%)", "테크 플랫폼 · 구독+광고 · 기존 보유 340주 (1.36%)")}</div>'
            f'<div class="vd">{t("HOLD CORE + CONDITIONAL ACCUMULATE", "핵심 보유 + 조건부 분할 매수")}</div><span class="cro">{t("CRO: CONDITIONAL CAP · MAX 3.0%", "CRO: 조건부 상한 · 최대 3.0%")}</span></div>')
    tiles = '<div class="g3">' + "".join([
        stat(t("Price", "현재가"), "$69.70", t("1Y −41.5% · −48% vs ATH", "1년 −41.5% · 고점 대비 −48%"), "#b91c1c"),
        stat(t("Conservative IV", "보수적 내재가치"), "$74.78", t("DCF $65.95 ⊕ P/E $83.60", "DCF $65.95 ⊕ P/E $83.60")),
        stat(t("12M Base Target", "12개월 기준 목표"), "$83.60", t("+19.9% · prob-wtd $81.28", "+19.9% · 확률가중 $81.28"), "#047857"),
        stat(t("Accumulate Zone", "분할매수 구간"), "$62.5–67", t("20–25% margin of safety", "20~25% 안전마진"), "#059669"),
        stat(t("Position", "보유 계획"), "340→690", t("1.36% → 2.75% · cap 3.0%", "1.36% → 2.75% · 상한 3.0%"), "#1d4ed8"),
        stat(t("Catalyst", "이벤트"), t("Oct 20", "10월 20일"), t("Q3 print · guide $12.86B", "3분기 실적 · 가이던스 $12.86B"), "#7c3aed")]) + "</div>"
    emp = [(t("1Y return", "1년 수익률"), '<span class="neg">−41.5%</span>', t("vs SPY +17.4%", "SPY +17.4%")), (t("3Y CAGR", "3년 CAGR"), '<span class="pos">+22.2%</span>', "+82.7%"),
           (t("5Y CAGR", "5년 CAGR"), "+2.0%", t("multiple compression", "멀티플 압축")), (t("10Y CAGR", "10년 CAGR"), '<span class="pos">+20.9%</span>', t("elite", "최상위")),
           (t("Revenue", "매출"), "$31.6B → $48.4B", "FY22 → TTM"), (t("True FCF", "진성 FCF"), "$1.04B → $9.09B", "FY22 → FY25"),
           (t("Net debt / EBITDA", "순부채/EBITDA"), "0.37x", "S&P 'A'"), (t("2022 MDD", "2022 최대낙폭"), '<span class="neg">−75.9%</span>', t("satellite sizing", "위성 비중"))]
    et = "<table>" + "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in emp) + "</table>"
    sec1 = f'<div class="sec">{t("1 · Multi-Year Empirical Validation — PASSED", "1 · 다개년 실증 검증 — 통과")}</div><div class="g2"><div class="card">{et}</div><div class="card"><h3>{t("24-Month Price Path", "24개월 주가 궤적")}</h3>{svg_price(520, 300)}</div></div>'
    sec2 = f'<div class="sec">{t("2 · Revenue vs. True FCF", "2 · 매출 vs 진성 FCF")}</div><div class="card">{svg_bars(1100, 320)}</div>'
    ms = "".join(f'<div class="card" style="padding:16px 20px"><div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0;font-size:22px">{n}</h3><span class="chip {c}">{t(*v)}</span></div><p style="font-size:17px;line-height:1.6;margin-top:6px">{t(*x)}</p></div>' for n, l, v, c, x in MASTERS)
    sec3 = f'<div class="sec">{t("3 · Masters Matrix", "3 · 거장 평가 매트릭스")}</div><div class="g2">{ms}</div>'
    scn = (f'<div class="g3">'
           f'<div class="card" style="background:#ecfdf5"><div class="stat"><div class="l" style="color:#047857">{t("Bull 25%", "강세 25%")}</div><div class="v" style="color:#047857">$102.70</div><div class="s">+47.3% · 26x × $3.95</div></div></div>'
           f'<div class="card" style="background:#eff6ff"><div class="stat"><div class="l" style="color:#1d4ed8">{t("Base 50%", "기준 50%")}</div><div class="v" style="color:#1d4ed8">$83.60</div><div class="s">+19.9% · 22x × $3.80</div></div></div>'
           f'<div class="card" style="background:#fff1f2"><div class="stat"><div class="l" style="color:#b91c1c">{t("Bear 25%", "약세 25%")}</div><div class="v" style="color:#b91c1c">$55.20</div><div class="s">−20.8% · 16x × $3.45</div></div></div></div>')
    sec4 = f'<div class="sec">{t("4 · Scenarios & Levels", "4 · 시나리오 & 레벨")}</div>{scn}<div class="g2"><div class="card"><h3>{t("Technical Ladder", "기술적 사다리")}</h3>{ladder(520, 400)}</div>' + \
        f'<div class="card"><h3>{t("Attention Share & Flow", "시청 점유율 & 수급")}</h3>' + hbars([(t("YouTube", "유튜브"), 14.2, "#ef4444", "14.2%"), ("Netflix", 7.8, "#E50914", "7.8%")], 16) + \
        f'<ul style="margin-top:8px"><li>{t("Skydance (Paramount+WBD) closed Oct 6, 2026", "스카이댄스(파라마운트+WBD) 2026.10.6 합병 완료")}</li><li>{t("WFC UW $57 · HSBC Hold $76 (Sep-26)", "웰스파고 UW $57 · HSBC Hold $76 (9월)")}</li><li>{t("Co-CEO sales $9.73M + $2.01M; 0 insider buys", "공동CEO 매도 $9.73M + $2.01M, 내부자 매수 0건")}</li><li>{t("FMR −33.6% (13F Q2)", "FMR −33.6% (13F 2분기)")}</li><li>{t("Ads ~$3B in 2026 (~2x)", "2026년 광고 약 $3B (약 2배)")}</li></ul></div></div>'
    ex = (f'<div class="sec">{t("5 · Execution & CRO", "5 · 집행 & CRO")}</div><div class="g2"><div class="card"><ul>'
          f'<li>{t("<b>Hold</b> core 340 sh", "핵심 340주 <b>보유</b>")}</li><li>{t("<b>T1</b> 150 sh after Oct 20 (3-point test)", "<b>1차</b> 10/20 이후 150주 (3대 조건)")}</li><li>{t("<b>T2</b> 200 sh @ $65.00 limit", "<b>2차</b> $65.00 지정가 200주")}</li>'
          f'<li>{t("<b>Fund</b>: trim 100 NVDA (~$23.7K)", "<b>재원</b>: NVDA 100주 매도 (약 $23.7K)")}</li><li>{t("<b>Stop</b> $60.50 on added shares", "추가분 <b>손절</b> $60.50")}</li></ul></div>'
          f'<div class="card"><table><tr><th>{t("Shock", "충격")}</th><th>{t("Now", "현재")}</th><th>{t("Proposed", "제안")}</th></tr><tr><td>S1 AI capex</td><td class="neg">−33.8%</td><td class="neg">−33.3%</td></tr>'
          f'<tr><td>S2 {t("Geo/energy", "지정학")}</td><td class="neg">−26.3%</td><td class="neg">−26.1%</td></tr><tr><td>S3 {t("Rates", "고금리")}</td><td class="neg">−24.9%</td><td class="neg">−24.8%</td></tr>'
          f'<tr><td><b>Beta</b></td><td>1.56</td><td>1.55</td></tr></table></div></div>')
    exitb = box("b-red", t("🛑 Exit Trigger (100%)", "🛑 엑시트 트리거 (100%)"), t("Revenue growth &lt;8% YoY for 2 straight quarters AND FY operating-margin target cut &lt;29% — OR a debt-funded acquisition above $30B pushing net leverage &gt;2.5x EBITDA.", "매출 성장률 2개 분기 연속 8% 미만 + 연간 영업이익률 목표 29% 미만 하향 — 또는 순부채 EBITDA 2.5배 초과를 유발하는 $30B 초과 차입 인수."))
    foot = f'<div class="foot">DADAIC-IC-MEMO-NFLX-{DATE} · {t("All figures USD · Fact-checked: 20 claims dual-sourced, 1 rejected", "모든 수치 USD(달러) · 팩트체크: 20개 주장 이중 검증, 1건 기각")} · {t("Not investment advice outside the DADAIC mandate", "DADAIC 내부 의사결정 자료")}</div>'
    return (f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>NFLX Infographic {DATE}</title>{FONTS}<style>{INFO_CSS}</style></head><body><div class="page">'
            + hero + tiles + sec1 + sec2 + sec3 + sec4 + ex + exitb + foot + "</div></body></html>")


def run(cmd):
    print(" ".join(cmd[-2:]))
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    global K
    base = os.path.join(MEDIA, "NFLX-Investment-Committee-Decision-Memo")
    for K, code in ((0, "EN"), (1, "KR")):
        sh = f"{base}-Slide-{code}-{DATE}.html"
        ih = f"{base}-Infographic-{code}-{DATE}.html"
        open(sh, "w", encoding="utf-8").write(deck())
        open(ih, "w", encoding="utf-8").write(infographic())
        common = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000"]
        run(common + ["--no-pdf-header-footer", f"--print-to-pdf={base}-Slide-{code}-{DATE}.pdf", "file:///" + sh.replace("\\", "/")])
        run(common + ["--window-size=1200,3620", f"--screenshot={base}-Infographic-{code}-{DATE}.png", "file:///" + ih.replace("\\", "/")])
        # QA preview of the full deck as a tall PNG
        run(common + ["--window-size=1920,7560", f"--screenshot={os.path.join(ROOT, 'scripts', f'_qa_deck_{code}.png')}", "file:///" + sh.replace("\\", "/")])
    print("done")


if __name__ == "__main__":
    main()
