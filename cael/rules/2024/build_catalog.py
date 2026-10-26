#!/usr/bin/env python3
"""Genera un catalogo HTML bilingue dalle schede JSON di Cael.
Uso: python3 cael/rules/2024/build_catalog.py
Non richiede dipendenze esterne.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
en = json.loads((ROOT / "spells/source-extract.en.json").read_text(encoding="utf-8"))["records"]
it = json.loads((ROOT / "spells/italiano.it.json").read_text(encoding="utf-8"))["records"]
weapons = json.loads((ROOT / "weapons/quarterstaff-blessed.it.json").read_text(encoding="utf-8"))
italian = {r["name"]: r for r in it}
esc = lambda value: html.escape(str(value), quote=True)
cards = []
for spell in en:
    tr = italian.get(spell["name"], {})
    name = esc(spell["name"])
    label = esc(tr.get("name_it", spell["name"]))
    summary = esc(tr.get("summary_it", "Traduzione non disponibile"))
    source = esc(spell.get("source", ""))
    page = esc(spell.get("page", "?"))
    level = esc(spell.get("level", "?"))
    cards.append(f'<article id="{name.lower().replace(" ", "-")}"><h2>{label} <small>{name}</small></h2><p>{summary}</p><p class="meta">Livello {level} · {source} p. {page}</p></article>')
blessing = esc(weapons["blessing"]["effect"])
cards.append(f'<article><h2>Bastone Benedetto delle Stelle</h2><p>{blessing}</p><p class="meta">Homebrew del Master · Con Shillelagh: +7 a colpire, 1d8+5; non morti 1d8+5+2d6</p></article>')
style = "body{font:16px/1.6 system-ui;background:#101724;color:#f0e9da;max-width:980px;margin:auto;padding:2rem}article{border:1px solid #53617b;border-radius:16px;padding:1rem 1.5rem;margin:1rem 0;background:#192538}small,.meta{color:#b9c7dc}small{font-size:.65em}h1{color:#f7d898}"
out = "<!doctype html><html lang='it'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Cael · Catalogo incantesimi</title><style>"+style+"</style><h1>Cael Vesper · Catalogo bilingue</h1><p>Regole 2024 · Sintesi italiane non ufficiali · Dati derivati dai JSON archiviati</p>"+"".join(cards)+"</html>"
target = ROOT / "cael-catalogo-bilingue.html"
target.write_text(out, encoding="utf-8")
print(target)
