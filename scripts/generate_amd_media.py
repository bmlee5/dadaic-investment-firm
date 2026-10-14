#!/usr/bin/env python3
"""
DADAIC Investment Firm - Media Compiler for AMD Investment Committee Deliverables
Compiles:
- Slide Deck EN (HTML & PDF)
- Slide Deck KR (HTML & PDF)
- Strategic Infographic EN (HTML & PNG)
- Strategic Infographic KR (HTML & PNG)
All stored directly in DecisionMemo/Media/
"""
import os
import subprocess

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(ROOT, "DecisionMemo", "Media")

def compile_all():
    print("[*] Compiling AMD Media Deliverables with Headless Chrome...")
    
    # 1. Slide EN PDF
    slide_en_html = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Slide-EN-261006.html")
    slide_en_pdf = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Slide-EN-261006.pdf")
    cmd_s_en = [CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={slide_en_pdf}", slide_en_html]
    print("  -> Rendering Slide EN PDF...")
    subprocess.run(cmd_s_en, check=True)

    # 2. Slide KR PDF
    slide_kr_html = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Slide-KR-261006.html")
    slide_kr_pdf = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Slide-KR-261006.pdf")
    cmd_s_kr = [CHROME_PATH, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={slide_kr_pdf}", slide_kr_html]
    print("  -> Rendering Slide KR PDF...")
    subprocess.run(cmd_s_kr, check=True)

    # 3. Infographic EN PNG
    info_en_html = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Infographic-EN-261006.html")
    info_en_png = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Infographic-EN-261006.png")
    cmd_i_en = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,3400", f"--screenshot={info_en_png}", info_en_html]
    print("  -> Rendering Infographic EN PNG...")
    subprocess.run(cmd_i_en, check=True)

    # 4. Infographic KR PNG
    info_kr_html = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Infographic-KR-261006.html")
    info_kr_png = os.path.join(MEDIA_DIR, "AMD-Investment-Committee-Decision-Memo-Infographic-KR-261006.png")
    cmd_i_kr = [CHROME_PATH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,3400", f"--screenshot={info_kr_png}", info_kr_html]
    print("  -> Rendering Infographic KR PNG...")
    subprocess.run(cmd_i_kr, check=True)

    print("[+] All 8 AMD deliverables compiled successfully!")

if __name__ == "__main__":
    compile_all()
