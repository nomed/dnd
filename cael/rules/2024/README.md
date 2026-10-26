# Cael — dati D&D 2024, fonti e progressione

## Stato

**Non ancora completo per una scheda certificata 1–20.** L'archivio contiene 16 incantesimi/trucchetti, 7 creature, la progressione Druido 1–20, un indice di privilegi, riferimenti per talenti/specie e un oggetto homebrew. Le descrizioni italiane sono sintesi originali; i JSON non sono copie integrali dei libri o del database 5etools.

## Organizzazione attuale

- `spells/source-extract.en.json`: campi strutturati da 5etools via Dnd MCP (XPHB), senza testo integrale.
- `spells/italiano.it.json`: corrispondenti nomi e sintesi italiane.
- `class/`, `subclass/`, `feats/`, `species/`: metadati delle fonti e localizzazione, **non** regole complete.
- `source/5etools/features.index.json`: indice canonico delle capacità del Druido 2024 e del Circolo delle Stelle XPHB; livelli e pagine; sintesi italiane per le capacità stellari.
- `creatures/`: statistiche selezionate e riferimenti delle forme selvatiche e del gufo.
- `weapons/`: bastone e benedizione del Master, **homebrew** distinto dalle regole.
- `character/cael-progression.json`: valori attuali e proiezioni per livelli 1–20, privilegi e scelte ancora aperte.
- `build_catalog.py` e `build_progression.py`: due generatori HTML separati; **non** sostituiscono il grimorio illustrato.
- `validate.py`: test di coerenza dei dati, con segnalazione di elementi incompleti.

## Gerarchia delle fonti

1. **5etools XPHB 2024**: Druido pp. 78–81, Circolo delle Stelle pp. 88–89; incantesimi, specie e talenti con pagina in ogni record.
2. **XMM 2024**: forme animali e gufo, dati selezionati.
3. **Scelte del personaggio**: livello 4, caratteristiche 10/16/17/10/20/10, CA 16, PF 35, Allerta, incremento SAG +2 al livello 4.
4. **Homebrew del Master**: bastone +2d6 contro non morti; tipo di danno da confermare.

La sottoclasse di riferimento è **Circle of the Stars, XPHB 2024**, non Circle of Stars TCE. Star Map e Starry Form si sbloccano al livello 3. Guiding Bolt gratuito e Cosmic Omen hanno utilizzi pari al modificatore di Saggezza, non al bonus di competenza.

## Proiezioni PF

Druido d8, COS 17 (+3), metodo fisso: 11 PF al livello 1, poi +8 per livello. Al livello 4: 35 PF; livello 5: 43; livello 6: 51; livello 7: 59; livello 20: 163. Se cambia il modificatore di Costituzione, ricalcolare anche i PF dei livelli precedenti.

## Decisioni mancanti (non inventare)

- Background e sue competenze, abilità scelte, equipaggiamento completo, velocità, percezione passiva.
- Trucchetto aggiuntivo di Magician; ricostruzione delle caratteristiche ai livelli 1–3.
- Scelta Elemental Fury al livello 7 (Potent Spellcasting **oppure** Primal Strike).
- Talenti e incrementi ai livelli 8, 12, 16 e Epic Boon al 19.
- Proprietà esatte e tipo di danno della benedizione del bastone.
- Validazione completa di attacchi, azioni e tratti delle forme animali e delle formule degli incantesimi.
- Riconciliazione del file storico `cael/edizioni/level3/cael-level3.json`, che contiene valori obsoleti e non deve fungere da fonte canonica.

## Verifica

`python3 cael/rules/2024/validate.py`

`python3 cael/rules/2024/build_progression.py`

`python3 cael/rules/2024/build_catalog.py`

I test e i generatori sono versionati, ma **non risultano eseguiti in CI**. La loro presenza non certifica la completezza dei dati.

## Scheda canonica e generazione per livello

- `character/cael-sheet-model.json`: scheda canonica **attuale** di livello 4, con valori, competenze note, risorse, incantesimi e campi esplicitamente null/unconfirmed quando mancanti.
- `build_sheet.py --level 4`: produce `cael-scheda-liv04.html` dalla scheda canonica, dal catalogo degli incantesimi, dai privilegi e dalle creature.
- `build_sheet.py --level 5` (fino a 20): produce una **proiezione**, non una scheda definitiva. Non assegna nuove preparazioni, talenti o competenze in automatico.
- Le sette creature in `creatures/` includono adesso azioni e tratti strutturati ricavati da XMM 2024. Sono riferimenti meccanici selezionati, non il testo integrale dei blocchi statistici.
- Il nuovo renderer HTML è funzionale come scheda dati; **non incorpora ancora l'illustrazione e il layout del grimorio storico**.

## Qualità e vincoli

I dati e i generatori sono stati verificati mediante lettura e controlli strutturali dei JSON nel repository. Non sono stati eseguiti i generatori Python né la suite di test in un runner/CI in questo intervento. La scheda non va dichiarata completa finché background, abilità, velocità, equipaggiamento, Magician e scelte future non sono verificati.
