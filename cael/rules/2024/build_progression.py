#!/usr/bin/env python3
"""Genera una scheda di progressione HTML dalla fonte JSON di Cael."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "character/cael-progression.json").read_text(encoding="utf-8"))
escape = lambda value: html.escape(str(value), quote=True)
rows = []
for entry in data["levels"]:
    level = entry["level"]
    feats = entry.get("class_features", []) + entry.get("subclass_features", [])
    feat_text = "; ".join(f'{f["name"]} ({f.get("source", "XPHB")} p. {f.get("page", "?")})' for f in feats) or "—"
    slots = ", ".join(f'{k}°: {v}' for k, v in entry["spell_slots"].items())
    derived = entry.get("derived_if_wisdom_remains_20", {})
    attack = f'+{derived["spell_attack_bonus"]}' if derived else "da verificare"
    dc = derived.get("spell_save_dc", "da verificare")
    hp = entry["hp_max"]
    rows.append(f'<tr id="level-{level}"><td><strong>{level}</strong></td><td>{hp}</td><td>+{entry["proficiency_bonus"]}</td><td>{attack}</td><td>{dc}</td><td>{entry["druid_prepared_spells"]}</td><td>{escape(slots)}</td><td>{escape(feat_text)}</td></tr>')
css = """body{font:15px/1.5 system-ui;margin:auto;padding:24px;max-width:1300px;background:#101827;color:#f1eadd}h1{color:#f6d78c}table{width:100%;border-collapse:collapse}th,td{border-bottom:1px solid #46536b;padding:10px;text-align:left;vertical-align:top}th{position:sticky;top:0;background:#26344b}tr:nth-child(even){background:#1b2739}.note{color:#bccce3}a{color:#f6d78c}"""
document = f'<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cael — Progressione 1–20</title><style>{css}</style></head><body><h1>Cael Vesper · Progressione 1–20</h1><p>Fonte: 5etools / XPHB 2024, Druido p. 78–81 e Circolo delle Stelle p. 88.</p><p class="note">PF: metodo fisso 11 al 1° livello e +8 per livello, assumendo COS 17 invariata. Dal livello 4: valori magici calcolati con SAG 20; i livelli precedenti richiedono le caratteristiche storiche. Scelte future non confermate.</p><div style="overflow:auto"><table><thead><tr><th>Livello</th><th>PF</th><th>Competenza</th><th>Attacco magia</th><th>CD</th><th>Preparati</th><th>Slot</th><th>Privilegi e fonte</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></body></html>'
out = ROOT / "cael-progressione-1-20.html"
out.write_text(document, encoding="utf-8")
print(out)
