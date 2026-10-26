# Cael v2

Migrazione incrementale: i vecchi JSON restano disponibili fino alla verifica completa.

## File
- `characters/cael/character.json`: unica fonte per scelte, punteggi iniziali, incantesimi e inventario.
- `rules/catalog.json`: indice dei cataloghi 5etools ancora ospitati nella struttura precedente.
- `rules/homebrew/cael-blessed-quarterstaff.json`: +2d6 radianti contro i non morti.
- `schemas/character.schema.json`: schema JSON del personaggio.
- `engine.py`: valori derivati e progressione 1-20.
- `render.py`: scheda HTML minimale.
- `test_engine.py`: test unitari.
- `.github/workflows/cael-v2.yml`: test in GitHub Actions.

## Comandi
```bash
python3 cael/v2/engine.py --level 4
python3 cael/v2/engine.py --level 8 --scenario planned
python3 cael/v2/render.py --level 4
python3 -m unittest discover -s cael/v2 -p 'test_*.py' -v
```

`confirmed` applica le scelte confermate e le nuove scelte adottate; `planned` applica anche le proposte future. La Costituzione 18 al livello 8 aumenta retroattivamente i PF massimi da 67 a 75.

## Lavoro ancora necessario
Normalizzare ogni record di incantesimi e creature, sostituire la tabella di progressione legacy con regole di classe indipendenti, verificare lo schema in CI, modellare tutte le risorse e gli attacchi, e integrare il renderer con il grimorio illustrato. I test sono versionati ma il loro esito non e' ancora verificato.
