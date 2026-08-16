#!/usr/bin/env python3
"""Validate the structural coverage of an AI collaboration journal Markdown file."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "why": r"為什麼.*(?:日誌|開始)|真正.*(?:困境|動機)",
    "main_line": r"主線",
    "roles": r"角色",
    "boundaries": r"安全|界線|隱私|匿名",
    "corrections": r"偏航|修正|校正",
    "decisions": r"決策",
    "learning": r"關鍵字|學習",
    "outputs": r"產出|文件.*狀態|成果.*狀態",
    "open_questions": r"待確認|未解|待驗證",
    "next_action": r"下一步|先做什麼",
}

RESEARCH_PATTERN = r"論文|研究"
STATUS_PATTERN = r"已確認|AI 建議|模擬假設|待驗證|未採用"
FIRST_PERSON_PATTERN = r"我原本|我後來|我認為|我發現|我的修正|我把"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_journal.py <journal.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    coverage = {
        name: bool(re.search(pattern, text, flags=re.IGNORECASE))
        for name, pattern in REQUIRED_PATTERNS.items()
    }
    missing = [name for name, present in coverage.items() if not present]
    report = {
        "file": str(path),
        "characters": len(text),
        "headings": len(re.findall(r"^#{1,6}\s+", text, flags=re.MULTILINE)),
        "coverage": coverage,
        "has_research_section": bool(re.search(RESEARCH_PATTERN, text)),
        "has_evidence_status": bool(re.search(STATUS_PATTERN, text)),
        "has_first_person_evolution": bool(re.search(FIRST_PERSON_PATTERN, text)),
        "missing_required": missing,
        "valid": not missing
        and bool(re.search(STATUS_PATTERN, text))
        and bool(re.search(FIRST_PERSON_PATTERN, text)),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
