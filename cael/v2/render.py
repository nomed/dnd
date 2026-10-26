#!/usr/bin/env python3
"""Render derived Cael data as an HTML sheet."""
import argparse
import html
from pathlib import Path
from engine import ROOT, read, derive

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", type=int, default=4)
    p.add_argument("--scenario", choices=["confirmed", "planned"], default="confirmed")
    p.add_argument("--output")
    args = p.parse_args()
    data = derive(read(ROOT / "characters/cael/character.json"), args.level, args.scenario)
    esc = lambda value: html.escape(str(value))
    rows = []
    for name in ("hpMax", "proficiencyBonus", "spellAttackBonus", "spellSaveDC", "initiative", "passivePerception"):
        rows.append("<tr><th>" + esc(name) + "</th><td>" + esc(data[name]) + "</td></tr>")
    for name, value in data["abilityScores"].items():
        rows.append("<tr><th>" + esc(name) + "</th><td>" + esc(value) + "</td></tr>")
    notes = "".join("<li>" + esc(x) + "</li>" for x in data["warnings"] + data["unresolvedDecisions"])
    page = ("<!doctype html><html lang='it'><meta charset='utf-8'><title>Cael " + str(args.level) +
            "</title><style>body{font:16px system-ui;background:#101a2c;color:#eee;max-width:760px;margin:auto;padding:28px}th,td{padding:8px;border-bottom:1px solid #667}h1{color:#e8d08c}</style>" +
            "<h1>Cael Vesper - livello " + str(args.level) + "</h1><p>Scenario: " + esc(args.scenario) +
            "</p><table>" + "".join(rows) + "</table><h2>Da confermare</h2><ul>" + notes +
            "</ul><p>Fonte: modello canonico v2, Druid XPHB 2024.</p></html>")
    target = Path(args.output) if args.output else ROOT / ("cael-level-" + str(args.level) + ".html")
    target.write_text(page, encoding="utf-8")
    print(target)

if __name__ == "__main__":
    main()
