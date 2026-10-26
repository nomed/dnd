#!/usr/bin/env python3
"""Renderizza una scheda HTML per un livello, usando dati JSON e fonti locali."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))
def esc(x):
    return html.escape(str(x), quote=True)

def render(level):
    sheet = read("character/cael-sheet-model.json")
    progression = read("character/cael-progression.json")
    spells_en = {x["name"]: x for x in read("spells/source-extract.en.json")["records"]}
    spells_it = {x["name"]: x for x in read("spells/italiano.it.json")["records"]}
    features = read("source/5etools/features.index.json")["features"]
    record = progression["levels"][level - 1]
    current = level == sheet["identity"]["level"]
    hp = record["hp_max"]
    attack = record.get("derived_if_wisdom_remains_20", {}).get("spell_attack_bonus")
    dc = record.get("derived_if_wisdom_remains_20", {}).get("spell_save_dc")
    def card(title, body):
        return f'<section><h2>{esc(title)}</h2>{body}</section>'
    stats = sheet["ability_scores"] if current else None
    attrs = ''.join(f'<div class="stat"><strong>{esc(k)}</strong><span>{v} ({sheet["modifiers"][k]:+d})</span></div>' for k, v in stats.items()) if stats else '<p>Caratteristiche future: proiezione basata sul livello 4, non scelte definitive.</p>'
    items = [f'<li><strong>{esc(f["name"])}</strong> · livello {f["level"]} · {esc(f["source"])} p. {esc(f["page"] or "?")} {esc(f.get("summary_it") or "")}</li>' for f in features if f["level"] <= level and f["name"] not in ("Warden","Primal Strike","Potent Spellcasting")]
    selected = sheet["spellcasting"]["prepared"] + sheet["spellcasting"]["always_prepared"] + sheet["spellcasting"]["class_granted"] + sheet["spellcasting"]["feat_granted"] + sheet["spellcasting"]["cantrips"]
    spells = []
    for name in dict.fromkeys(selected):
        source = spells_en.get(name, {})
        translated = spells_it.get(name, {})
        spells.append(f'<li><strong>{esc(translated.get("name_it", name))}</strong> ({esc(name)}) · {esc(source.get("source","?"))} p. {esc(source.get("page","?"))} · {esc(translated.get("summary_it",""))}</li>')
    if not current:
        spells.insert(0, "<li><em>Lista incantesimi del livello 4: le nuove preparazioni per questo livello non sono state scelte.</em></li>")
    beasts = []
    for name in sheet["wild_shape"]["known_forms"]:
        animal = read("creatures/" + name.lower().replace(" ", "-") + ".json")
        src = animal["source_en"]
        attacks = "; ".join(esc(a["name"] + ": " + a.get("damage", "") + (" +" + a["additional_damage"] if "additional_damage" in a else "")) for a in src.get("mechanics", {}).get("actions", []))
        beasts.append(f'<li><strong>{esc(animal["localization_it"]["name"])}</strong> · CR {esc(src["cr"])} · {esc(src["source"])} p. {esc(src["page"])} · {attacks}</li>')
    warnings = list(sheet["pending"])
    if level < 4: warnings.append("Caratteristiche storiche e scelte ai livelli 1-3 non ricostruite")
    if level >= 7: warnings.append("Elemental Fury: scegliere Potent Spellcasting o Primal Strike")
    if not current: warnings.append("Livello diverso dal 4: scelte, preparazioni, caratteristiche e statistiche non ancora confermate")
    html_body = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cael · livello {level}</title><style>
    body{{font:15px/1.55 system-ui;background:#0f1827;color:#f1eee5;max-width:1060px;margin:auto;padding:24px}}header{{border-bottom:1px solid #8d9bb2;padding-bottom:18px}}h1{{color:#e9d294}}h2{{color:#e9d294}}section{{border:1px solid #45536a;background:#1a273b;padding:18px;border-radius:14px;margin:16px 0}}.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:12px}}.stat{{display:flex;flex-direction:column;border:1px solid #53617a;border-radius:10px;padding:12px}}.stat span{{font-size:20px}}li{{margin:8px 0}}.warning{{color:#f5c89c}}a{{color:#e9d294}}
    </style></head><body><header><h1>Cael Vesper · livello {level}</h1><p>Druido · Circolo delle Stelle · XPHB 2024 · {'Scheda attuale' if current else 'PROIEZIONE NON DEFINITIVA'}</p><p><strong>PF massimi {hp}</strong> · CA {sheet["combat"]["ac"] if current else "da confermare"} · Competenza +{record["proficiency_bonus"]} · Attacco magico {("+" + str(attack)) if attack is not None else "da verificare"} · CD {dc if dc is not None else "da verificare"}</p></header>
    {card("Caratteristiche", '<div class="stats">' + attrs + '</div>')}
    {card("Incantesimi e slot", '<p>Slot: ' + esc(", ".join(k + "°: " + str(v) for k,v in record["spell_slots"].items())) + '</p><p>Incantesimi da Druido preparabili: ' + str(record["druid_prepared_spells"]) + '</p><ul>' + "".join(spells) + '</ul>')}
    {card("Privilegi e fonti", '<ul>' + "".join(items) + '</ul>')}
    {card("Forme selvatiche documentate per il livello 4 (non storicizzate)", '<p>Statistiche e attacchi dalle creature XMM 2024; i PF di Cael restano invariati in Forma Selvatica.</p><ul>' + "".join(beasts) + '</ul>')}
    {card("Dati da confermare", '<ul class="warning">' + "".join('<li>' + esc(w) + '</li>' for w in warnings) + '</ul>')}
    <footer>Fonte dei dati: cael/rules/2024/ · Le sintesi italiane non sono traduzioni ufficiali.</footer></body></html>"""
    output = ROOT / f"cael-scheda-liv{level:02d}.html"
    output.write_text(html_body, encoding="utf-8")
    print(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", type=int, default=4, choices=range(1,21), metavar="1..20")
    args = parser.parse_args()
    render(args.level)
