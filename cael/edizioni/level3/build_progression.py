#!/usr/bin/env python3
"""Generate a level-aware HTML spell appendix from cael-level3.json.
This is additive; the original illustrated HTML is never overwritten.
"""
import json, html
from pathlib import Path

here=Path(__file__).resolve().parent
c=json.loads((here/"cael-level3.json").read_text(encoding="utf-8"))
def esc(x): return html.escape(str(x))
def scaled(dice,inc,steps,mod=0):
    a,b=map(int,dice.split("d")); n=int(inc.split("d")[0])
    return f"{a+steps*n}d{b}"+(f"+{mod}" if mod else "")
def slot_unlock(slot): return 1 if slot==1 else slot*2-1
rows=[]
for name,data in c["spell_scaling"].items():
    status="Storico · non preparato" if data.get("prepared") is False else ("Concesso da Star Map" if name=="Guiding Bolt" else "Preparato")
    trs=[]
    for slot in range(data["base_slot"],6):
        usable=slot<=max(map(int,c["spell_slots"]))
        val=scaled(data["base_dice"],data["per_higher_slot"],slot-data["base_slot"],data.get("ability_modifier",0))
        trs.append(f'<tr class="{"available" if usable else "future"}"><td>{slot}°</td><td>Liv. {slot_unlock(slot)}</td><td>{val}</td><td>{"Disponibile" if usable else "Futuro"}</td></tr>')
    rows.append(f'<section><h2>{esc(name)} <small>{esc(status)}</small></h2><p>XPHB p. {data["page"]}</p><table><thead><tr><th>Slot</th><th>Livello druido</th><th>Danno / cura</th><th>Stato</th></tr></thead><tbody>{"".join(trs)}</tbody></table></section>')
feats="".join(f'<li>Liv. {f["unlocked_at_character_level"]}: {esc(f["name"])}</li>' for f in c["class_features"])
doc=f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cael · progressione</title><style>
body{{max-width:800px;margin:auto;padding:16px;background:#fffdf8;color:#21374c;font:16px/1.5 system-ui}}section{{margin:20px 0;padding:14px;background:white;border:1px solid #c8d5e0;border-radius:10px}}table{{width:100%;border-collapse:collapse}}th,td{{padding:7px;border-bottom:1px solid #dbe3e9;text-align:left}}.available{{background:#eaf5e9}}.future{{color:#697786}}small{{font-size:12px;color:#526578}}@media(max-width:600px){{body{{padding:10px}}th,td{{padding:5px;font-size:12px}}}}
</style></head><body><h1>Cael · livello {c["level"]}</h1><p>Trucchetti: sempre disponibili, senza slot e senza preparazione. Incantesimi ordinari: sei preparati. Guiding Bolt: sempre preparato da Star Map, quattro lanci gratuiti per riposo lungo (livello base).</p><h2>Capacità per livello</h2><ul>{feats}</ul><h2>Progressione per incantesimo</h2>{"".join(rows)}</body></html>'''
(here/"cael-progression-generated.html").write_text(doc,encoding="utf-8")
print("Created",here/"cael-progression-generated.html")
