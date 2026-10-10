#!/usr/bin/env python3
"""Additive Cael publication build. Reads the existing dossier/images; writes only dist/."""
from __future__ import annotations
import argparse, base64, hashlib, html, io, json, re
from pathlib import Path
import mistune
from PIL import Image
from weasyprint import HTML
import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'cael/lev02.md'
EXPECTED_BLOB = '29df4cc71b2224a1413105b5142ddf990eaa1a42'
VERSION = 'v1 · 10.10.2026'
MD = mistune.create_markdown(plugins=['table'])
IMAGES = {}
RAW = ''

# One quick-reference catalogue feeds both editions. No pending choice is promoted.
SPELLS = [
 dict(id='starry-wisp', name='Starry Wisp', it='Luce stellare', kind='Trucchetto di classe', page=320, image='02_starry_wisp.png', time='1 A', reach='18 m · creatura o oggetto', roll='+6 contro CA', effect='1d8 radiante', duration='Istantaneo', components='V, S', cost='Nessuno slot', detail='Colpito: luce fioca 3 m; niente benefici di Invisible fino alla fine del tuo prossimo turno.', heading='Starry Wisp'),
 dict(id='produce-flame', name='Produce Flame', it='Fiamma', kind='Trucchetto di classe', page=308, image='03_produce_flame.png', time='1 AB crea · 1 A Magia attacca', reach='Personale; attacco 18 m', roll='+6 contro CA', effect='1d8 fuoco', duration='10 min · no concentrazione', components='V, S', cost='Nessuno slot', detail='Creatura o oggetto. Attaccare non termina la fiamma. Luce intensa 6 m + fioca 6 m.', heading='Produce Flame'),
 dict(id='druidcraft', name='Druidcraft', it='Arte druidica', kind='Magic Initiate · trucchetto', page=266, image='04_druidcraft.png', time='1 A', reach='9 m', roll='Nessun tiro', effect='Piccoli effetti naturali', duration='Istantaneo*', components='V, S', cost='Nessuno slot', detail='Meteo locale 24 h, sbocciare, effetto innocuo (cubo 1,5 m), accendere/spegnere fuoco. *Segnale meteo: 1 round.', heading='Druidcraft'),
 dict(id='shillelagh', name='Shillelagh', it='Bastone potenziato', kind='Magic Initiate · trucchetto', page=316, image='05_shillelagh.png', time='1 AB potenzia · 1 A Attaccare', reach='Personale · arma impugnata', roll='+6 contro CA', effect='1d8+4 forza o contundente', duration='1 min · no concentrazione', components='V, S, M', cost='Nessuno slot', detail='Solo Club/Quarterstaff; non il falcetto. Finisce se lasci l’arma. Bastone-focus idoneo: da formalizzare.', heading='Shillelagh'),
 dict(id='healing-word', name='Healing Word', it='Parola Guaritrice', kind='Preparato · 1° livello', page=284, image='09_healing_word.png', time='1 AB', reach='18 m · una creatura visibile', roll='Nessun tiro', effect='Cura 2d4+4 PF', duration='Istantaneo', components='V', cost='1 slot di 1°', detail='Devi vedere il bersaglio. Non richiede contatto.', heading='Healing Word — Parola Guaritrice'),
 dict(id='cure-wounds', name='Cure Wounds', it='Cura Ferite', kind='Preparato · 1° livello', page=259, image='10_cure_wounds.png', time='1 A', reach='Contatto · una creatura', roll='Nessun tiro', effect='Cura 2d8+4 PF', duration='Istantaneo', components='V, S', cost='1 slot di 1°', detail='Il famiglio può consegnare il contatto: entro 30 m da te, usando la propria reazione.', heading='Cure Wounds — Cura Ferite'),
 dict(id='entangle', name='Entangle', it='Intralciare', kind='Preparato · 1° livello', page=268, image='08_entangle.png', time='1 A', reach='27 m · quadrato 6 m sul terreno', roll='TS FOR CD 14', effect='Trattenuto + terreno difficile', duration='CONC · fino a 1 min', components='V, S', cost='1 slot di 1°', detail='TS iniziale di tutti tranne Cael, alleati inclusi. Fuga: 1 A, prova FOR (Atletica) CD 14. Nuovi ingressi: solo terreno difficile.', heading='Entangle — Intralciare'),
 dict(id='faerie-fire', name='Faerie Fire', it='Fuoco Fatato', kind='Preparato · 1° livello', page=271, image='07_faerie_fire.png', time='1 A', reach='18 m · cubo di 6 m', roll='TS DES CD 14', effect='Vantaggio contro gli influenzati', duration='CONC · fino a 1 min', components='V', cost='1 slot di 1°', detail='Vantaggio se li vedi; luce fioca 3 m, niente benefici di Invisible. Oggetti automatici; creature su TS fallito. Anche alleati.', heading='Faerie Fire — Fuoco Fatato nella scheda'),
 dict(id='thunderwave', name='Thunderwave', it='Onda Tonante', kind='Preparato · 1° livello', page=334, image='11_thunderwave.png', time='1 A', reach='Cubo di 4,5 m che origina da te', roll='TS COS CD 14', effect='2d8 tuono + spinta 3 m', duration='Istantaneo', components='V, S', cost='1 slot di 1°', detail='TS riuscito: metà danni, niente spinta. Anche alleati. Spinge oggetti non fissati interamente nel cubo; boato 90 m.', heading='Thunderwave — Onda Tonante'),
 dict(id='goodberry', name='Goodberry', it='Bacche Benefiche', kind='Sempre preparato · Magic Initiate', page=280, image='12_goodberry.png', time='1 A crea · 1 AB mangia', reach='10 bacche nella tua mano*', roll='Nessun tiro', effect='1 PF + nutrimento / bacca', duration='24 h', components='V, S, M', cost='1 gratis / riposo lungo o 1 slot', detail='Una bacca nutre per un giorno; poi le bacche scompaiono. *Gittata da confermare. Non include imboccare un incosciente.', heading='Goodberry — Bacche Benefiche'),
 dict(id='speak-with-animals', name='Speak with Animals', it='Parlare con gli Animali', kind='Sempre preparato · Druidic', page=318, image='13_speak_with_animals.png', time='1 A · rituale: +10 min', reach='Personale', roll='Nessun tiro', effect='Comprendi e parli con le Bestie', duration='10 min · no concentrazione', components='V, S', cost='1 slot; rituale senza slot', detail='Comunicazione, non controllo. Riguarda il tipo Bestia, non ogni creatura dall’aspetto animale.', heading='Speak with Animals — Parlare con gli Animali'),
 dict(id='guidance', name='Guidance', it='Guida', kind='PROPOSTA · Magician', page=282, image='06_guidance.png', time='1 A', reach='Contatto · creatura consenziente', roll='Nessun tiro', effect='+1d4 alle prove di un’abilità scelta', duration='CONC · fino a 1 min', components='V, S', cost='Nessuno slot', detail='Vale per ogni prova dell’abilità scelta durante la durata, non per attacchi o TS. Scelta non ancora confermata.', heading='Guidance — proposta per Magician', pending=True),
]


SHORT_NOTES = {
 'starry-wisp':'Colpito: luce fioca 3 m e niente Invisible fino alla fine del tuo prossimo turno.',
 'produce-flame':'Creatura o oggetto. Attaccare non termina l’effetto. Luce intensa 6 m + fioca 6 m.',
 'druidcraft':'Meteo, sbocciare, effetti innocui, accendere/spegnere fuochi. *Segnale meteo: 1 round.',
 'shillelagh':'Solo Club/Quarterstaff. Finisce se lasci l’arma. Idoneità del focus da formalizzare.',
 'healing-word':'Devi vedere il bersaglio; non serve contatto.',
 'cure-wounds':'Contatto consegnabile dal famiglio: entro 30 m da te, con la sua reazione.',
 'entangle':'TS iniziale, anche alleati (non Cael). Fuga: 1 A, prova FOR (Atletica) CD 14.',
 'faerie-fire':'Vantaggio se vedi il bersaglio; niente Invisible. Luce fioca 3 m. Anche alleati.',
 'thunderwave':'Successo: metà danni, niente spinta. Anche alleati; spinge oggetti liberi. Boato 90 m.',
 'goodberry':'Una bacca nutre per un giorno. *Gittata da confermare. Non include imboccare incoscienti.',
 'speak-with-animals':'Comunicazione, non controllo. Solo creature di tipo Bestia.',
 'guidance':'Ogni prova dell’abilità scelta; non attacchi o TS. Scelta da confermare.'
}

CSS = r'''
@page {size:A4; margin:10mm 11mm 12mm; @bottom-left{content:"CAEL VESPER  /  LIVELLO 2";font:7pt "Lato",sans-serif;color:#586477} @bottom-center{content:"PHB 2024: pagine inglesi · v1 / 10.10.2026";font:7pt "Lato",sans-serif;color:#586477} @bottom-right{content:counter(page);font:9pt "Lato",sans-serif;color:#22364e}}
*{box-sizing:border-box}body{margin:0;color:#172738;background:#fff;font:10pt/1.38 "Lato","DejaVu Sans",sans-serif}h1,h2,h3,p{margin-top:0}h1,h2{font-family:"DejaVu Serif",Georgia,serif}h1{font-size:30pt;line-height:1.1;margin-bottom:3mm;color:#172c44}h2{font-size:17pt;margin:0 0 4mm}h3{font-size:11.5pt;margin:4mm 0 2mm;color:#23435e}p{margin-bottom:2.6mm}strong{font-weight:800}a{color:inherit;text-decoration:none}small,.muted{color:#526172}table{width:100%;border-collapse:collapse;font-size:9.2pt;margin:2mm 0 4mm}th{text-align:left;background:#eaf0f3;font-size:8pt;text-transform:uppercase;letter-spacing:.035em}td,th{padding:1.8mm 2mm;vertical-align:top;border-bottom:.2mm solid #d7dfe4}tr{break-inside:avoid}blockquote{margin:5mm 0;padding:3mm 4mm;border-left:2px solid #b19053;font:italic 13pt/1.55 "DejaVu Serif",serif;color:#304962}code{font:inherit}.page{break-after:page}.page:last-child{break-after:auto}.eyebrow{font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:#927343;font-weight:800;margin-bottom:3mm}.running{display:flex;justify-content:space-between;border-bottom:.35mm solid #b69254;padding-bottom:2.5mm;margin-bottom:5mm;font-size:8pt;color:#506276;letter-spacing:.06em}.sub{font-size:11pt;color:#52667a;margin:2mm 0 5mm}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:5mm}.panel{border:1px solid #d4dde4;border-radius:2mm;padding:3mm;background:#f8fafb;break-inside:avoid}.panel h3{margin:0 0 2mm}.ref{font-size:7.8pt;color:#5b6c7e;margin-top:2mm}.note{background:#f4efe4;border-left:2.5px solid #b08b48;padding:2.5mm 3mm;font-size:9pt;margin:3mm 0}.rule{background:#ecf2f6;padding:3mm 4mm;margin:3mm 0}.footer-note{font-size:8pt;color:#586578;margin-top:3mm;border-top:1px solid #d6dfe6;padding-top:2.5mm}.portrait{width:55mm;height:45mm;object-fit:cover;object-position:50% 35%;border-radius:2mm;background:#07101a}.hero{display:grid;grid-template-columns:1fr 55mm;gap:5mm;margin-bottom:5mm}.hero h1{font-size:31pt}.hero .sub{margin:2mm 0;font-size:10pt}.quote{font:italic 10pt/1.5 "DejaVu Serif",serif;color:#56677c;margin-top:4mm}.metrics{display:grid;grid-template-columns:repeat(6,1fr);gap:2mm;margin-bottom:3mm}.metric{text-align:center;padding:2.5mm 1mm;background:#172c44;color:#fff;border-radius:1.5mm}.metric .label{font-size:7pt;text-transform:uppercase;letter-spacing:.07em;color:#e0d9c5}.metric b{display:block;font-size:22pt;line-height:1.1;margin:.7mm 0}.metric small{font-size:7pt;color:#dbe6ef}.attributes{display:grid;grid-template-columns:repeat(6,1fr);gap:2mm;margin-bottom:4mm}.attribute{text-align:center;border:.3mm solid #c8d2dc;border-radius:1.5mm;padding:2mm 1mm}.attribute span{display:block;font-size:8pt;letter-spacing:.05em}.attribute b{font-size:20pt;line-height:1.1}.attribute small{display:block;font-size:8pt}.attribute .save{margin-top:1mm;color:#17364e}.section-label{text-transform:uppercase;font-size:8.5pt;letter-spacing:.1em;font-weight:800;border-bottom:.3mm solid #b69254;margin:4mm 0 2mm;padding-bottom:1mm}.skill-list{display:grid;grid-template-columns:1fr 1fr;gap:1mm 5mm;font-size:9.5pt}.skill{display:flex;justify-content:space-between;border-bottom:1px dotted #cbd5dc;padding:.5mm 0}.resource{display:flex;justify-content:space-between;gap:2mm;font-size:9pt;margin-bottom:1.5mm}.boxes{white-space:nowrap}.box{display:inline-block;width:3mm;height:3mm;border:.3mm solid #667b8d;margin-left:1mm;vertical-align:middle}.tiny{font-size:8pt;line-height:1.35}.capabilities{display:grid;grid-template-columns:1fr 1fr;gap:2mm 5mm;margin-top:2mm}.capabilities p{font-size:9pt;line-height:1.37;margin:0 0 2mm}.weapon-table{font-size:9pt;margin:0 0 2mm}.weapon-table td,.weapon-table th{padding:1.4mm 2mm}.session{font-size:9pt;border-bottom:1px solid #cad5df;padding:2mm 0;margin-bottom:3mm}.cards{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm 4mm}.spell-card{border:.25mm solid #cbd7df;border-radius:1.8mm;padding:2mm 2.5mm;break-inside:avoid;background:#fff;min-height:32mm}.spell-card.proposal{background:#fbf7ef;border-style:dashed;border-color:#ab884a}.card-head{display:grid;grid-template-columns:1fr 8mm;gap:2mm;align-items:center;margin-bottom:1mm}.card-head img{width:8mm;height:8mm;object-fit:cover;border-radius:1mm;background:#060c14}.card-name{font:800 11.8pt/1.1 "Lato",sans-serif;margin-bottom:1mm}.card-kind{font-size:7.1pt;color:#53697f}.spell-card.proposal .card-kind{color:#91632f;font-weight:800}.card-time{font-weight:800;font-size:9pt;line-height:1.24}.card-reach{font-size:8.4pt;color:#324e65;margin-top:.5mm}.card-main{font-size:9.4pt;line-height:1.24;margin:1mm 0;font-weight:800}.card-detail{font-size:8.2pt;line-height:1.25;margin:.6mm 0 1.2mm}.card-meta{font-size:7.6pt;color:#354d61;border-top:1px solid #dce3e8;padding-top:1mm;line-height:1.25}.compact .running{margin-bottom:2.5mm}.compact .hero{margin-bottom:3mm;grid-template-columns:1fr 48mm}.compact .portrait{width:48mm;height:34mm}.compact .hero .quote{margin-top:2mm;font-size:9pt}.compact .hero h1{font-size:28pt}.compact .hero .sub{font-size:9.2pt}.compact .metric{padding:2mm 1mm}.compact .metric b{font-size:20pt}.compact .attribute{padding:1.5mm 1mm}.compact .attribute b{font-size:18pt}.compact .section-label{margin-top:2mm}.compact .capabilities p{font-size:8.8pt}.compact .note{font-size:8.1pt;margin:2mm 0;padding:2mm 2.5mm}.compact .footer-note{font-size:7.8pt;margin-top:1.5mm;padding-top:1.5mm}.compact h2{font-size:20pt;margin-bottom:2mm}.compact .sub{font-size:9pt;margin-bottom:3mm}.compact .cards{gap:2mm 3mm}.legend{font-size:8pt;background:#eef3f6;padding:2mm 3mm;margin:2.5mm 0}.glossary{font-size:7.9pt;line-height:1.35;margin-top:2.5mm}.cover{padding:7mm 0 0}.cover h1{font-size:42pt;letter-spacing:-.03em}.cover-art{width:100%;height:133mm;object-fit:cover;object-position:center;background:#09101a;border-radius:2mm;margin:4mm 0 7mm}.cover .quote{font-size:13pt;color:#283f58}.cover .cover-bottom{margin-top:9mm;border-top:1px solid #b59054;padding-top:4mm;display:grid;grid-template-columns:1fr 1fr;gap:10mm;font-size:9pt}.chapter-title{margin-bottom:6mm}.chapter-body{font-size:10pt;line-height:1.42}.chapter-body h3{margin-top:4mm}.chapter-body table{font-size:9pt}.chapter-body.dense{font-size:9.3pt;line-height:1.36}.chapter-body.dense table{font-size:8.5pt}.chapter-body.columns{columns:2;column-gap:6mm}.chapter-body.columns h3{break-after:avoid}.chapter-body.columns table{font-size:8pt}.spell-hero{display:grid;grid-template-columns:118mm 1fr;gap:5mm;align-items:start;margin-bottom:6mm}.spell-art{width:118mm;height:94mm;object-fit:contain;background:#05090e;border-radius:2mm}.spell-facts{font-size:9.5pt}.fact{padding:2mm 0;border-bottom:1px solid #d3dce4}.fact small{display:block;text-transform:uppercase;letter-spacing:.07em;font-size:7pt;margin-bottom:.5mm}.fact b{font-size:11pt}.spell-long h1{font-size:29pt;margin-bottom:2mm}.spell-long .sub{margin-bottom:5mm}.spell-long .chapter-body{font-size:11pt;line-height:1.45}.spell-long .chapter-body p{margin-bottom:3mm}.spell-long .result{font-size:16pt;font-weight:800;color:#173b55;margin:2mm 0 4mm}.spell-long .pending{background:#eee4cf;color:#755224;padding:2mm 3mm;font-size:9pt;margin-bottom:3mm}.index-row{display:flex;justify-content:space-between;gap:5mm;border-bottom:1px solid #dce4e9;padding:1.5mm 0;font-size:10pt}.screen-toolbar{display:none}.form-lines p{border-bottom:1px solid #c7d5df;height:8mm;margin:0;font-size:9pt}.no-break{break-inside:avoid}
.compact .hero .quote{display:none}.card-name{margin-bottom:0}.card-kind{line-height:1.05}.card-head{margin-bottom:.7mm}.card-main{margin:.25mm 0}.card-detail{margin:.25mm 0}.card-meta{padding-top:.4mm}.spell-card{padding:1.5mm 2.5mm}.chapter-body.dense td,.chapter-body.dense th{padding:1.2mm 2mm}.chapter-title{margin-bottom:4mm}
@media screen{body{background:#e6ebef}.screen-toolbar{display:flex;position:sticky;top:0;z-index:10;background:#172c44;color:white;gap:18px;padding:12px 20px;font-size:14px}.screen-toolbar a{color:white}.page{width:210mm;min-height:297mm;background:white;margin:20px auto;padding:10mm 11mm 12mm;box-shadow:0 3px 20px #172c4422}.screen-toolbar button{background:transparent;color:white;border:1px solid #c4cedb;padding:3px 10px;border-radius:4px;cursor:pointer}}
@media screen and (max-width:760px){.compact .hero{grid-template-columns:1fr 100px}.compact .portrait{width:100px;height:112px}.compact .hero h1{font-size:28px}.compact .hero .sub{font-size:12px}.compact .note{font-size:13px}.page{width:auto;min-height:0;margin:12px 8px;padding:20px 16px}.hero{grid-template-columns:1fr 100px;gap:12px}.portrait{width:100px;height:115px}.hero h1{font-size:28px}.hero .sub{font-size:12px}.hero .quote{display:none}.metrics,.attributes{grid-template-columns:repeat(3,1fr);gap:8px}.grid2,.capabilities,.cards,.compact .cards{grid-template-columns:1fr;gap:12px}.spell-card{padding:14px}.card-head{grid-template-columns:1fr 54px}.card-head img{width:54px;height:54px}.card-name{font-size:21px}.card-kind{font-size:12px}.card-time,.card-main{font-size:16px}.card-reach,.card-detail{font-size:14px;line-height:1.4}.card-meta{font-size:12px}.spell-hero{grid-template-columns:1fr}.spell-art{width:100%;height:auto;max-height:300px}.spell-facts{display:grid;grid-template-columns:1fr 1fr;gap:8px}.chapter-body.columns{columns:1}.cover-art{height:auto}.cover h1{font-size:39px}.cover .cover-bottom{grid-template-columns:1fr;gap:12px}table{font-size:12px}.compact .tiny,.legend,.glossary{font-size:12px}.running{font-size:10px}.compact .capabilities p{font-size:14px}.skill-list,.resource{font-size:14px}.ref,.footer-note{font-size:11px}.screen-toolbar{font-size:12px;padding:10px}.spell-long .chapter-body,.chapter-body,.chapter-body.dense{font-size:15px;line-height:1.5}}
'''

def esc(s: str) -> str:
    return html.escape(str(s))

def image(name: str, thumb: bool=False) -> str:
    key=name+("_thumb" if thumb else "")
    if key not in IMAGES:
        src=ROOT/'cael/images'/name
        if not src.is_file(): raise FileNotFoundError(src)
        im=Image.open(src).convert('RGB'); im.thumbnail((256,256) if thumb else (1450,1200))
        out=io.BytesIO(); im.save(out,'JPEG',quality=88,optimize=True)
        IMAGES[key]='data:image/jpeg;base64,'+base64.b64encode(out.getvalue()).decode()
    return IMAGES[key]

def section(title: str, level: int=3) -> str:
    match=re.search(r'^'+('#'*level)+' '+re.escape(title)+r'\s*$',RAW,re.M)
    if not match: raise ValueError('Missing source section: '+title)
    rest=RAW[match.end():]
    end=re.search(r'^#{1,'+str(level)+r'} ',rest,re.M)
    return rest[:end.start() if end else len(rest)].strip()

def clean(text: str, remove_tables: bool=False) -> str:
    kept=[]
    for p in re.split(r'\n\s*\n',text):
        if p.startswith(('**Fonte:', '**Fonte delle', '**Provenienza:', '**Campo da verificare:', '**Nota di integrità:', '**Slot superiori da verificare:', '**Fonti della')): continue
        if p.startswith('> **Questa sezione'): continue
        if p.startswith('Per la copertura completa'): continue
        if remove_tables and p.lstrip().startswith('|'): continue
        p=re.sub(r'`[^`]*(?:Dnd\.|items-base|ruleset|source=)[^`]*`','',p)
        p=re.sub(r',?\s*`Dnd[^`]*`','',p)
        p=p.replace('**Slot superiori, dato MCP:**','**Con slot superiori:**')
        p=p.replace("Nel testo 2024 restituito dall'MCP",'Nel testo 2024')
        p=p.replace('Il testo MCP consiglia','Il testo della capacità consiglia')
        p=p.replace("dall'MCP",'dalla fonte della scheda').replace('risposta MCP','testo disponibile').replace('dato MCP','dato documentato')
        p='\n'.join(line for line in p.splitlines() if not line.startswith('| Dati MCP'))
        p=p.replace('recuperata con .','').replace('voce Ritual recuperata con .','voce Ritual.')
        p=p.replace('MCP','documentato').replace('XPHB','PHB 2024')
        p=p.replace('Il record','La voce').replace('il record','la voce').replace('Il server','La fonte').replace('il server','la fonte')
        p=p.replace('nel repository','nella scheda originaria').replace('del repository','della scheda originaria')
        p=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',p)
        p=re.sub(r',\s*;',';',p)
        kept.append(p)
    return '\n\n'.join(kept)

def rendered(title: str, ref: str='', level: int=3, dense: bool=False) -> str:
    body=clean(section(title,level))
    return '<h3>'+esc(title)+'</h3>'+MD(body)+(f'<p class="ref">PHB 2024 (EN), {esc(ref)}.</p>' if ref else '')

def running(label: str) -> str:
    return '<div class="running"><span>CAEL VESPER / '+esc(label)+'</span><span>D&D 2024 · LIVELLO 2</span></div>'

def boxes(n: int) -> str:
    return '<span class="boxes">'+('<span class="box"></span>'*n)+'</span>'

def character_page() -> str:
    stats=[('CA','16','14 senza scudo'),('PF massimi','19*','attuali _____'),('Iniziativa','+5','DES + Alert'),('Velocità','9 m','30 piedi'),('Perc. passiva','16','Percezione +6'),('Competenza','+2','livello 2')]
    attrs=[('FOR',10,'+0','+0'),('DES',16,'+3','+3'),('COS',17,'+3','+3'),('INT',10,'+0','+2 •'),('SAG',18,'+4','+6 •'),('CAR',10,'+0','+0')]
    skills=[('Percezione •','+6'),('Natura •','+6'),('Furtività •','+5'),('Sopravvivenza •','+6'),('Indagare •','+2'),('Arcana','+4')]
    metrics=''.join(f'<div class="metric"><span class="label">{a}</span><b>{b}</b><small>{c}</small></div>' for a,b,c in stats)
    attributes=''.join(f'<div class="attribute"><span>{a} {b}</span><b>{c}</b><small class="save">TS {d}</small></div>' for a,b,c,d in attrs)
    sl=''.join(f'<div class="skill"><span>{a}</span><b>{b}</b></div>' for a,b in skills)
    return f'''<section class="page compact" id="scheda">{running('SCHEDA DA TAVOLO')}
<div class="hero"><div><div class="eyebrow">Il Cartografo del Cielo Morto</div><h1>Cael Vesper</h1><p class="sub"><b>Druido 2 · Umano · Guida</b><br>Ordine: Magician · Il Dominio Oscuro<br><span class="tiny">Circolo delle Stelle: dal 3°, non ancora attivo.</span></p><div class="quote">«Non serve credere alle stelle.<br>Serve sapere dove puntare.»</div></div><img class="portrait" src="{image('01_cael.png')}" alt="Cael Vesper"></div>
<div class="metrics">{metrics}</div><div class="attributes">{attributes}</div>
<div class="grid2"><div><div class="section-label">Abilità e competenze</div><div class="skill-list">{sl}</div><p class="tiny" style="margin-top:2mm">Cartografia <b>+6 (SAG)</b> · Erboristeria <b>+2 (INT)</b><br>• = competente. Magician già incluso in Natura e Arcana.<br>TS e classe: pp. 78–80; Guida p. 181; Umano p. 194.</p><p class="tiny"><b>Lingue:</b> Comune, Druidico; altre da scegliere.<br><b>Addestramento:</b> armi semplici, armature leggere, scudi.</p></div>
<div><div class="section-label">Risorse · compila alla sessione</div><div class="resource"><b>Slot di 1°</b>{boxes(3)}</div><div class="resource"><b>Forma Selvatica</b>{boxes(2)}</div><div class="resource"><b>Goodberry senza slot</b>{boxes(1)}</div><div class="resource"><b>Ispirazione Eroica</b>{boxes(1)}</div><p class="tiny">Slot e Goodberry: riposo lungo. Forma Selvatica: 1 uso al breve, tutti al lungo (pp. 79–80, 201).<br>Dadi vita <b>2d8</b> · PF temporanei ____ · Esaustione ____<br>*19 PF a incremento fisso: da confermare con il DM.</p></div></div>
<div class="section-label">Capacità in un colpo d’occhio</div><div class="capabilities">
<p><b>Forma Selvatica · 1 AB</b> — 2 usi, dura 1 h; GS ≤ 1/4, niente volo. Mantieni i tuoi PF, ottieni 2 PF temporanei; non lanci incantesimi. 4 forme da scegliere. <span class="muted">p. 80</span></p>
<p><b>Wild Companion · 1 A Magia</b> — spendi 1 slot o 1 uso di Forma Selvatica: famiglio Fatato senza materiali. Scompare al riposo lungo. Forma da scegliere. <span class="muted">p. 81</span></p>
<p><b>Alert</b> — iniziativa +5 già calcolata; dopo il tiro puoi scambiarla con un alleato consenziente. Nessuno dei due deve essere Incapacitated. <span class="muted">p. 200</span></p>
<p><b>Umano</b> — Ispirazione Eroica dopo il riposo lungo: ritira un dado appena tirato, usando il nuovo risultato. <span class="muted">pp. 194, 368</span></p>
</div>
<div class="section-label">Attacchi con le armi</div><table class="weapon-table"><thead><tr><th>Arma / configurazione</th><th>Attacco</th><th>Danno</th><th>Portata / nota</th></tr></thead><tbody>
<tr><td>Bastone con Shillelagh*</td><td><b>+6</b></td><td><b>1d8+4</b></td><td>Mischia; forza o contundente</td></tr><tr><td>Bastone senza incantesimo</td><td>+2</td><td>1d6</td><td>1d8 a due mani; contundente</td></tr><tr><td>Falcetto</td><td>+2</td><td>1d4</td><td>Mischia; tagliente, non Finesse</td></tr><tr><td>Arco corto</td><td>+5</td><td>1d6+3</td><td>24/96 m; due mani, no scudo</td></tr></tbody></table>
<p class="tiny">Armi: pp. 215, 225. Cuoio + scudo: p. 219. Nessuna maestria d’arma attiva. *Formalizzare il bastone-focus come Quarterstaff; non è un nuovo acquisto.</p>
<div class="grid2"><div class="note"><b>Concentrazione standard: +3</b><br>TS COS quando subisci danni: CD max(10, metà danni arrotondata per difetto), massimo 30. Un solo effetto. <span class="muted">p. 363</span></div><div class="note"><b>Variante di campagna: +7</b><br>Due effetti: CD minima 20; fallimento = perdi tutti. Non è il TS COS ordinario. In forma animale ricalcola la COS.</div></div>
</section>'''

def spell_card(s: dict) -> str:
    return f'''<article class="spell-card {'proposal' if s.get('pending') else ''}" id="{s['id']}"><div class="card-head"><div><div class="card-name">{s['name']}</div><div class="card-kind">{s['kind']}</div></div><img src="{image(s['image'],True)}" alt="{s['name']}"></div><div class="card-time">{s['time']} <span style="font-weight:400">· {s['reach']}</span></div><div class="card-main">{s['roll']} → {s['effect']}</div><div class="card-detail">{SHORT_NOTES[s['id']]}</div><div class="card-meta">{s['duration']} · {s['components']}<br>{s['cost']} · <b>PHB24 p. {s['page']} (EN)</b></div></article>'''

def spell_page() -> str:
    return '<section class="page compact" id="incantesimi">'+running('INCANTESIMI')+'<h2>Incantesimi</h2><p class="sub"><b>Attacco magico +6 · CD 14 · SAG +4</b> · 3 slot di 1° · 5 preparati ordinari</p><div class="cards">'+''.join(spell_card(s) for s in SPELLS)+'</div><div class="legend"><b>A</b> azione · <b>AB</b> azione bonus · <b>TS</b> tiro salvezza · <b>CONC</b> concentrazione · <b>V/S/M</b> verbale/somatica/materiale.<br><b>Trattenuto:</b> velocità 0; suoi attacchi e TS DES con svantaggio, attacchi contro di lui con vantaggio (p. 373).<br><b>Luce viva contro il Miasma:</b> da chiarire con il DM. Non basta che un effetto emetta luce.</div></section>'

def chapter(title: str, content: str, label: str, dense: bool=False) -> str:
    return '<section class="page">'+running(label)+'<div class="eyebrow">Grimorio illustrato</div><h1 class="chapter-title">'+title+'</h1><div class="chapter-body '+('dense' if dense else '')+'">'+content+'</div></section>'

def expanded_spell(s: dict) -> str:
    text=clean(section(s['heading']),remove_tables=True)
    # Move data-quality diagnostics to the technical record; keep only player-facing caveats.
    text=text.replace('**Stato:** proposta già presente nella scheda, da confermare.','')
    note=''
    if s['id']=='thunderwave': note='Progressione con slot superiori da verificare prima dell’uso. Il profilo attuale è 2d8 con slot di 1°.'
    if s['id']=='goodberry': note='La gittata resta da verificare: la descrizione fa apparire dieci bacche nella mano dell’incantatore. Non è una cura a contatto.'
    if s['id']=='shillelagh':
        text=re.sub(r'La dotazione precedente indica.*', 'La dotazione comprende un bastone-focus. Formalizzarne l’uso come Quarterstaff idoneo con il DM, senza aggiungere un’arma gratuita.',text,flags=re.S)
    cell=lambda key: next((line.split('|')[2].strip().replace('**','') for line in section(s['heading']).splitlines() if line.startswith('| '+key+' |')), '')
    s=dict(s, school=cell('Livello e scuola'), material=cell('Componenti') or s['components'])
    facts=[('Tempo',s['time']),('Gittata / area',s['reach']),('Durata',s['duration']),('Componenti',s['material']),('Costo',s['cost'])]
    return f'''<section class="page spell-long" id="long-{s['id']}">{running('GRIMORIO / '+('PROPOSTA' if s.get('pending') else 'INCANTESIMO'))}<div class="eyebrow">{s['kind']}</div><h1>{s['name']}</h1><div class="sub">{s['school']} · PHB 2024 (EN), p. {s['page']}</div>{'<div class="pending"><b>Proposta, non scelta confermata.</b> Non aggiunta alle capacità attive.</div>' if s.get('pending') else ''}<div class="spell-hero"><img class="spell-art" src="{image(s['image'])}" alt="Cael: {s['name']}"><div class="spell-facts">{''.join('<div class="fact"><small>'+a+'</small><b>'+b+'</b></div>' for a,b in facts)}</div></div><div class="result">{s['roll']} → {s['effect']}</div><div class="chapter-body">{MD(text)}</div>{'<div class="note">'+note+'</div>' if note else ''}<p class="ref">Riferimento: Player’s Handbook 2024, edizione inglese, p. {s['page']}. Sintesi italiana per il tavolo.</p></section>'''

def book() -> str:
    pages=[]
    pages.append(f'''<section class="page cover">{running('GRIMORIO ILLUSTRATO')}<div class="eyebrow">Il Dominio Oscuro</div><h1>Cael Vesper</h1><p class="sub">Il Cartografo del Cielo Morto</p><img class="cover-art" src="{image('01_cael.png')}" alt="Cael Vesper, ritratto"><div class="quote">«Non so se le stelle siano ancora lassù.<br>So che qualcuno si è preso parecchio disturbo<br>per impedirci di guardare.»</div><div class="cover-bottom"><div><b>Umano · Druido 2 · Guida</b><br>Ordine primordiale: Magician<br>Sottoclasse prevista: Circolo delle Stelle, dal 3°.</div><div><b>Edizione illustrata {VERSION}</b><br>Compagna della scheda da tavolo.<br>Le scelte ancora aperte restano tali.</div></div><p class="footer-note">Riferimenti: Player’s Handbook 2024, pagine inglesi riportate nella scheda verificata. Non sono numeri di pagina dell’edizione italiana. Distanze: 5 piedi = 1,5 m. Illustrazioni originali già presenti nella raccolta di Cael.</p></section>''')
    toc='<p>Usa la scheda da tavolo durante il turno; queste pagine conservano dettagli, eccezioni e contesto. I riferimenti al manuale accompagnano ogni capacità.</p>'
    toc+='<div class="grid2"><div class="panel"><h3>In combattimento</h3><p>Attacco magico <b>+6</b> · CD <b>14</b><br>CA <b>16</b> con scudo / <b>14</b> senza<br>PF massimi <b>19*</b> · Iniziativa <b>+5</b></p><p class="tiny">*Incremento fisso, da confermare con il DM.</p></div><div class="panel"><h3>Come leggere</h3><p><b>A</b> azione · <b>AB</b> azione bonus<br><b>TS</b> tiro salvezza · <b>CONC</b> concentrazione<br><b>V, S, M</b> componenti dell’incantesimo.</p></div></div>'
    entries=[('Personaggio e risorse','03'),('Specie, background e talenti','04'),('Magia e capacità di classe','05'),('Forma Selvatica e Wild Companion','06'),('Attacchi, armi e dotazione','07–09'),('Incantesimi illustrati','10–21'),('Find Familiar: il compagno','22'),('Concentrazione e condizioni','23'),('Il Dominio Oscuro e storia','24–25'),('Avanzamento alle Stelle','26–27')]
    toc+=''.join('<div class="index-row"><span>'+a+'</span><b>'+b+'</b></div>' for a,b in entries)
    toc+='<h3>Tre stati, sempre distinti</h3><p><b>Attivo:</b> capacità e incantesimi confermati al livello 2.<br><b>Proposta:</b> Guidance, non ancora scelto.<br><b>Avanzamento:</b> Circolo delle Stelle e Guiding Bolt, non ancora disponibili.</p><div class="note"><b>Da concordare al tavolo:</b> forme animali, famiglio, lingue, bastone-focus e «luce viva». Le varianti del Dominio Oscuro sono separate dalle regole del manuale.</div>'
    pages.append(chapter('Una guida alla consultazione',toc,'INDICE'))
    pages.append(character_page())
    pages.append(chapter('Origini e talenti',rendered('Umano — Human','pp. 194, 368')+rendered('Guida — Guide','p. 181')+rendered('Alert','p. 200')+rendered('Magic Initiate — scelta Druid','p. 201'),'PERSONAGGIO',True))
    pages.append(chapter('La magia di Cael',rendered('Spellcasting — livello 1','pp. 78–79')+rendered('Druidic — livello 1','p. 80')+rendered('Primal Order: Magician — livello 1','p. 80')+'<h3>Lista attuale e accessi speciali</h3>'+clean_render(section('Incantesimi: elenco e risorse',2).split('**Legenda')[0]),'CLASSE',True))
    ws=rendered('Wild Shape — livello 2','p. 80')+rendered('Wild Companion — livello 2','p. 81')
    ws+='<div class="note"><b>Concentrazione in forma animale:</b> ricalcola il tiro con la Costituzione della Bestia e le competenze applicabili. Il +3 della forma umana non si trasferisce automaticamente. L’applicazione della variante COS + SAG va concordata con il DM.</div><h3>Le quattro forme conosciute · da scegliere</h3><div class="form-lines"><p>1. _________________________</p><p>2. _________________________</p><p>3. _________________________</p><p>4. _________________________</p></div>'
    pages.append(chapter('La forma della natura',ws,'CLASSE',True))
    pages.append(chapter('Armi e difese',rendered('Attacchi rapidi di Cael','pp. 215, 225')+rendered('Cuoio e scudo','p. 219')+'<h3>Armi idonee a Shillelagh</h3><p>Riferimenti, non nuovi possedimenti. Entrambe sono armi semplici da mischia; nessuna maestria è attiva per Cael.</p><table><tr><th>Arma</th><th>Base</th><th>Proprietà</th><th>Peso</th><th>Prezzo</th><th>Maestria</th></tr><tr><td>Club</td><td>1d4</td><td>Light</td><td>2 lb</td><td>1 ma</td><td>Slow</td></tr><tr><td>Quarterstaff</td><td>1d6 / 1d8</td><td>Versatile</td><td>4 lb</td><td>2 ma</td><td>Topple</td></tr></table><p>Slow, per chi possiede la maestria: un colpo che infligge danni può ridurre la velocità di 3 m fino al proprio turno successivo; più colpi non aumentano la riduzione oltre 3 m.</p><p class="ref">PHB 2024 (EN), pp. 214–215.</p>'+'<div class="note"><b>Configurazione delle mani:</b> il tiro con l’arco richiede due mani. Formalizza con il DM l’uso del bastone-focus come Quarterstaff e la gestione delle componenti mentre impugni scudo e arma. Non è concessa un’esenzione generale.</div>','DOTAZIONE',True))
    pages.append(chapter('Le tue armi',rendered('Sickle — falcetto','pp. 213–215')+rendered('Shortbow — arco corto','pp. 213–215')+rendered('Wooden Staff — bastone usato come focus druidico','pp. 214, 225'),'DOTAZIONE',True))
    pages.append(chapter('In viaggio',rendered('Strumenti','pp. 220–221')+rendered('Inventario iniziale','pp. 78, 181, 222–229'),'DOTAZIONE',True))
    pages.extend(expanded_spell(s).replace('<div class="eyebrow">','<span id="incantesimi"></span><div class="eyebrow">',1) if s['id']=='starry-wisp' else expanded_spell(s) for s in SPELLS)
    familiar=clean_render(section('Find Familiar — Trova Famiglio, tramite Wild Companion'))
    pages.append(chapter('Find Familiar', '<p class="sub">Trova Famiglio · PHB 2024 (EN), p. 272 · Wild Companion p. 81</p>'+familiar+'<div class="note"><b>Forma non ancora scelta.</b> Questa capacità non seleziona automaticamente un animale. Non è disponibile un’illustrazione dedicata nel materiale esistente.</div>','COMPAGNO',True))
    pages.append(chapter('Concentrazione e condizioni',rendered('Concentration — regola standard','p. 363')+rendered('Incapacitated','p. 369')+rendered('Restrained — Trattenuto','p. 373')+'<h3>Rituali</h3><p>Un incantesimo preparato con il tag Ritual può essere lanciato senza slot impiegando 10 minuti in più del tempo normale, senza aumentarne il livello. Si applica a Speak with Animals. Per Find Familiar è qui documentato l’accesso specifico di Wild Companion, non un rituale gratuito.</p><p class="ref">PHB 2024 (EN), p. 373.</p>','REGOLE'))
    camp=clean_render(section('Regole del Dominio Oscuro: separate dal PHB',2))
    camp+='<div class="note"><b>Concentrazione multipla:</b> con +7 contro CD 20 serve almeno 13 sul d20 (40% di successo). I danni di Sforzo arcano e il momento in cui avvengono vanno chiariti con il DM: nessuna esenzione dai tiri di concentrazione è presunta.</div>'
    pages.append(chapter('Il Dominio Oscuro','<p class="sub">Regole di campagna, non regole del PHB. Fonti: Il Dominio Oscuro – Guida Ambientale; Prontuario Regole e Mutilazioni Dark Fantasy. Originali e pagine non verificati.</p>'+camp,'CAMPAGNA'))
    pages.append(chapter('Il cielo che manca',clean_render(section('Storia e personalità',2))+'<h3>Appunti di sessione</h3><div class="form-lines">'+''.join('<p> </p>' for _ in range(8))+'</div>','STORIA'))
    future='<div class="note"><b>ANTEPRIMA DEL LIVELLO 3.</b> Le capacità di questa pagina non sono attive al livello 2.</div><img style="width:100%;height:61mm;object-fit:contain;background:#05090e;border-radius:2mm" src="'+image('14_forma_stellare.png')+'" alt="Cael in Forma Stellare">'+rendered('Star Map','p. 88')+rendered('Starry Form','p. 88')
    pages.append(chapter('Il Circolo delle Stelle',future,'AVANZAMENTO',True))
    future2='<div class="note"><b>SOLO DAL LIVELLO 3.</b> Nessuna capacità futura è attribuita al personaggio attuale.</div>'+rendered('Guiding Bolt — incantesimo futuro','p. 282')+'<p>Progressione di Guiding Bolt con slot superiori: da verificare prima dell’uso.</p>'+rendered('Progressione prevista','p. 78')+'<h3>Decisioni ancora aperte</h3>'+clean_render(section('Questioni ancora aperte',2))
    pages.append(chapter('Il prossimo passo',future2,'AVANZAMENTO',True))
    return ''.join(pages)

def clean_render(text: str) -> str:
    return MD(clean(text))

def document(title: str, content: str) -> str:
    return '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+CSS+'</style></head><body><nav class="screen-toolbar"><b>Cael Vesper</b><a href="#scheda">Scheda</a><a href="#incantesimi">Incantesimi</a><button onclick="window.print()">Stampa</button></nav>'+content+'</body></html>'

def main() -> None:
    global RAW
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=HERE/'dist')
    args=parser.parse_args()
    data=SOURCE.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if blob!=EXPECTED_BLOB: raise SystemExit('Source changed: review the new dossier before updating the pinned edition.')
    RAW=data.decode('utf-8')
    args.out.mkdir(parents=True,exist_ok=True)
    for name,title,content in [('cael-scheda-tavolo','Cael Vesper · Scheda da tavolo',character_page()+spell_page()),('cael-grimorio-illustrato','Cael Vesper · Grimorio illustrato',book())]:
        markup=document(title,content)
        if re.search(r'Dnd\.|MCP|ruleset|entriesHigherLevel',re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+','',markup)): raise AssertionError('Technical diagnostics leaked into player publication')
        path=args.out/(name+'.html');path.write_text(markup,encoding='utf-8')
        pdf=args.out/(name+'.pdf')
        HTML(string=markup,base_url=str(HERE)).write_pdf(str(pdf))
        doc=fitz.open(pdf)
        expected=2 if name=='cael-scheda-tavolo' else 27
        if len(doc)!=expected: raise AssertionError(f'{name}: expected {expected} pages, found {len(doc)}')
        for page in doc:
            text=page.get_text()
            if not text.startswith('CAEL VESPER'): raise AssertionError('Unexpected continuation/overflow page')
            if '\ufffd' in text: raise AssertionError('Unrendered character')
        doc.close()
    (args.out/'catalogo-incantesimi.json').write_text(json.dumps(SPELLS,ensure_ascii=False,indent=2),encoding='utf-8')
    manifest={'edition':VERSION,'source':'cael/lev02.md','source_blob':blob,'build_file':'cael/edizioni/v1/build.py','images':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'cael/images').glob('*.png'))},'notes':['No character choices changed','Guidance is pending','Circle of the Stars is future level 3','Only dist/ is written by this builder']}
    (args.out/'provenienza.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Wrote both editions to',args.out)

if __name__=='__main__':main()
