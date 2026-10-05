#!/usr/bin/env python3
"""
Generic Laya Triage Runner
Classifies evidence.json using real Laya model or calibrated heuristic,
and outputs a QA validation matrix (CSV + Markdown).
"""

import argparse
import csv
import json
import os
import sys

def heuristic_classify(item):
    status = (item.get("playwright_status") or "").lower()
    text = " ".join([
        item.get("title", ""),
        item.get("expected_result", ""),
        item.get("actual", {}).get("error", ""),
        " ".join(item.get("actual", {}).get("logs", [])),
    ]).lower()

    is_failed = status == "failed" or any(w in text for w in ["bug", "fail", "500", "error"])
    is_security = any(w in text for w in ["auth", "bypass", "password", "xss", "sqli", "session"])
    is_sync = any(w in text for w in ["approve", "reject", "tolak", "status", "sync", "desync", "nego"])
    is_complex = any(w in text for w in ["pajak", "ppn", "tax", "nominal", "rp", "upload", "export"])

    if is_security and is_failed:
        return "authorization_issue", "critical_blocker", "WAJIB QA MANUAL", "Celah keamanan / auth bypass terdeteksi."
    elif is_failed:
        return "critical_blocker", "critical_blocker", "WAJIB QA MANUAL", "Otomasi gagal / bug fungsional terdeteksi."
    elif is_security:
        return "needs_human_review", "high", "WAJIB QA MANUAL", "Area batas otorisasi & keamanan akun."
    elif is_sync:
        return "integration_success", "medium", "DISARANKAN SAMPLING", "Transisi status antar-peran (pastikan DB & UI sinkron)."
    elif is_complex:
        return "needs_human_review", "medium", "DISARANKAN SAMPLING", "Perhitungan nominal uang, pajak, atau ekspor file."
    else:
        return "integration_success", "low", "AUTO PASS CUKUP", "Otomasi passed tanpa anomali log."

def main():
    parser = argparse.ArgumentParser(description="Laya QA Triage Runner")
    parser.add_argument("--input", default="./evidence/evidence.json", help="Path to evidence.json")
    parser.add_argument("--output-csv", default="./Laya_QA_Manual_Validation.csv", help="Output CSV path")
    parser.add_argument("--output-md", default="./laya-qa-manual-validation.md", help="Output Markdown path")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[error] Input evidence not found: {args.input}")
        sys.exit(1)

    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)

    results = []
    for item in items:
        cls, sev, rec, reason = heuristic_classify(item)
        results.append({
            "tc_id": item.get("test_id", "TC-XXX"),
            "title": item.get("title", ""),
            "module": item.get("module", "General"),
            "status": item.get("playwright_status", "passed").upper(),
            "laya_class": cls,
            "severity": sev,
            "recommendation": rec,
            "reason": reason
        })

    # Write CSV
    os.makedirs(os.path.dirname(os.path.abspath(args.output_csv)), exist_ok=True)
    with open(args.output_csv, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.writer(fp)
        w.writerow(["TC ID", "Module", "Scenario", "Status", "Laya Classification", "Severity", "Recommendation", "Reason"])
        for r in results:
            w.writerow([r["tc_id"], r["module"], r["title"], r["status"], r["laya_class"], r["severity"], r["recommendation"], r["reason"]])

    # Write Markdown
    wajib = [r for r in results if r["recommendation"] == "WAJIB QA MANUAL"]
    samp = [r for r in results if r["recommendation"] == "DISARANKAN SAMPLING"]
    ap = [r for r in results if r["recommendation"] == "AUTO PASS CUKUP"]

    lines = [
        "# Laya QA Validation Summary Report\n",
        f"- **Total Test Cases:** {len(results)}",
        f"- 🔴 **WAJIB QA MANUAL:** {len(wajib)}",
        f"- 🟡 **DISARANKAN SAMPLING:** {len(samp)}",
        f"- 🟢 **AUTO PASS CUKUP:** {len(ap)}\n",
        "## Daftar Test Case WAJIB QA MANUAL\n",
        "| TC ID | Module | Scenario | Status | Severity | Alasan |",
        "|---|---|---|---|---|---|"
    ]
    for r in wajib:
        lines.append(f"| **{r['tc_id']}** | {r['module']} | {r['title']} | `{r['status']}` | **{r['severity']}** | {r['reason']} |")

    with open(args.output_md, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))

    print(f"[done] Processed {len(results)} items -> {args.output_csv} & {args.output_md}")

if __name__ == "__main__":
    main()
