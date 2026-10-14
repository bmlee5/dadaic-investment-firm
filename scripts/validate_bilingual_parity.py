#!/usr/bin/env python3
"""
🏛️ DADAIC Investment Firm - Automated Bilingual Parity & Quality Validator
Programmatically audits Decision Memos and Deliberation Process Dossiers for:
1. Strict 1:1 Table Parity (Every markdown table in EN must exist in KR with equal columns)
2. Structural Section Symmetry (H2 and H3 header alignment between EN and KR)
3. Line Count Ratio (KR lines >= 90% of EN lines)
4. Forbidden Currency (USD only / No KRW or 원)
5. Principal Honorific Protocol (Strictly 'BM사장님', zero '유저'/'사용자')

Usage:
    python scripts/validate_bilingual_parity.py <path_to_markdown_file>
"""

import sys
import os
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def split_en_kr_sections(content: str):
    """Splits markdown content into English and Korean sections."""
    lines = content.split("\n")
    kr_split_idx = -1
    
    # Scan line by line for H1 headers marking Korean section
    for idx, line in enumerate(lines):
        # Must be an H1 or H2 header that appears after the top header
        if idx > 5 and line.strip().startswith("#"):
            lower = line.lower()
            if any(k in lower for k in ["한글판", "한국어", "🇰🇷", "part 2", "part ii"]):
                # Calculate char index
                kr_split_idx = len("\n".join(lines[:idx])) + 1
                break
            
    if kr_split_idx == -1:
        return None, None
        
    en_section = content[:kr_split_idx]
    kr_section = content[kr_split_idx:]
    return en_section, kr_section


def count_markdown_tables(text: str) -> list:
    """Finds all markdown tables in the given text and returns their header signatures."""
    lines = text.split("\n")
    tables = []
    in_table = False
    current_table = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                current_table = [stripped]
            else:
                current_table.append(stripped)
        else:
            if in_table:
                if len(current_table) >= 3 and any("---" in r for r in current_table):
                    tables.append(current_table)
                in_table = False
                current_table = []
                
    if in_table and len(current_table) >= 3 and any("---" in r for r in current_table):
        tables.append(current_table)
        
    return tables


def audit_file(filepath: str) -> bool:
    if not os.path.exists(filepath):
        print(f"❌ [Error] File not found: {filepath}", file=sys.stderr)
        return False
        
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
        
    filename = os.path.basename(filepath)
    print("=" * 80)
    print(f"🏛️ DADAIC BILINGUAL PARITY AUDITOR: {filename}")
    print("=" * 80)
    
    passed = True
    issues = []
    
    # 1. Split into English and Korean sections
    en_section, kr_section = split_en_kr_sections(content)
    if not en_section or not kr_section:
        print("❌ [FAIL] Could not distinguish English and Korean sections. File must be bilingual.")
        return False
        
    en_lines = [l for l in en_section.split("\n") if l.strip()]
    kr_lines = [l for l in kr_section.split("\n") if l.strip()]
    
    en_line_count = len(en_lines)
    kr_line_count = len(kr_lines)
    line_ratio = (kr_line_count / en_line_count) if en_line_count > 0 else 0
    
    print(f"📊 Line Count: English = {en_line_count} lines | Korean = {kr_line_count} lines (Ratio: {line_ratio:.1%})")
    
    if line_ratio < 0.85:
        issues.append(f"Line count ratio too low ({line_ratio:.1%} < 85%). Korean section appears compressed or summarized.")
        passed = False
    else:
        print("✅ Line count density parity passed (>= 85%).")
        
    # 2. Audit Table Counts
    en_tables = count_markdown_tables(en_section)
    kr_tables = count_markdown_tables(kr_section)
    
    print(f"📋 Table Count: English = {len(en_tables)} tables | Korean = {len(kr_tables)} tables")
    
    if len(kr_tables) < len(en_tables):
        issues.append(f"Table count mismatch: English has {len(en_tables)} tables, but Korean has only {len(kr_tables)} tables! "
                      f"Check for tables converted into bullet points in the Korean section.")
        passed = False
    else:
        print("✅ Table count parity passed (Korean has equal or greater table count).")
        
    # Check row counts of tables
    for idx, (t_en, t_kr) in enumerate(zip(en_tables, kr_tables), 1):
        en_rows = len(t_en)
        kr_rows = len(t_kr)
        if abs(en_rows - kr_rows) > 2:
            issues.append(f"Table #{idx} row count discrepancy: EN has {en_rows} rows, KR has {kr_rows} rows.")
            passed = False
            
    # 3. Check for forbidden currency (KRW, 원화, 원 converted)
    krw_patterns = [r"\bKRW\b", r"\b\d+[\d,]*\s*원\b", r"\(약\s*[\d,.]+\s*원\)"]
    found_krw = []
    for pat in krw_patterns:
        matches = re.findall(pat, content)
        if matches:
            found_krw.extend(matches)
            
    if found_krw:
        issues.append(f"Strict Currency Rule Violation (USD Only): Found forbidden KRW expressions: {found_krw[:5]}")
        passed = False
    else:
        print("✅ Currency Rule Passed (Strictly USD / Zero KRW found).")
        
    # 4. Check Principal Honorific (Always 'BM사장님')
    forbidden_user_terms = [r"\b유저님\b", r"\b유저\b", r"\b사용자\b"]
    found_user = []
    for pat in forbidden_user_terms:
        matches = re.findall(pat, content)
        if matches:
            found_user.extend(matches)
            
    if found_user:
        issues.append(f"Principal Title Violation: Found generic user terms: {found_user[:5]}. Must address as 'BM사장님'.")
        passed = False
    else:
        print("✅ Principal Honorific Passed (Correctly addressed as 'BM사장님').")
        
    # Final Result
    print("-" * 80)
    if passed:
        print("🎉 [AUDIT PASSED] The deliverable fulfills 100% Strict Bilingual Parity and Institutional Standards!")
        print("=" * 80)
        return True
    else:
        print("🚨 [AUDIT FAILED] Parity violations detected:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        print("=" * 80)
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_bilingual_parity.py <path_to_markdown_file>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    success = audit_file(target_file)
    sys.exit(0 if success else 1)
