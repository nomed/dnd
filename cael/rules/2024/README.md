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

## Recupero delle scelte originali (27 ottobre 2026)

È stato riesaminato il grimorio illustrato originale di Cael (materiale locale `cael-liv04-grimorio-light-astral.html`). Dati già documentati, non nuove ipotesi: background **Guide** (XPHB p.181); Furtività e Sopravvivenza dal background; strumenti da cartografo; **Magic Initiate (Druid)** dal background; **Alert** dal tratto Versatile dell'Umano; **Indagare** dal tratto Skillful; **Percezione** e **Natura** dal Druido; velocità 9 m; armatura di cuoio e scudo; pacchetto A del background (arco corto, 20 frecce, faretra, cartografia, giaciglio, tenda, abiti e 3 mo). I valori WIS del vecchio grimorio erano +4: con SAG 20 sono Percezione +7, Natura +7, Sopravvivenza +7, Arcana +5 grazie a Magician, Percezione passiva 17. Il vecchio grimorio è prova storica delle scelte, non la fonte dei valori numerici attuali.

**Nuove scelte discrezionali, esplicitamente marcate come tali:** trucchetto extra di Magician = **Mending** (XPHB p.297); Elemental Fury livello 7 = **Potent Spellcasting**; proposta per il livello 8 = ASI COS +1 e DES +1; livello 12 = ASI DES +1 e INT +1; livello 16 = War Caster. Le proposte future **non sono applicate** ai calcoli della progressione base, che rimane un riferimento a caratteristiche invariate. La scelta di Epic Boon al 19 rimane aperta in attesa di verifica dei talenti disponibili. Elfico come lingua aggiuntiva è una scelta discrezionale, non un dato storico.

**Da chiarire con il Master:** tipo di danno del bonus +2d6 del bastone benedetto e proprietà magiche; stato effettivo dell'inventario dopo le sessioni; eventuali lingue ulteriori; scelte future ancora modificabili.

Per una scheda futura realmente corretta, il calcolo dei PF deve ricalcolare retroattivamente il modificatore di Costituzione quando aumenta; il JSON attuale mantiene per i livelli futuri la baseline +8 e segnala le proposte separatamente.
