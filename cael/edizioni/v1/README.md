# Cael Vesper — edizioni per il giocatore

Due nuove edizioni additive della scheda di livello 2. I documenti precedenti e le 14 immagini originali non sono modificati.

| Edizione | PDF | HTML autonomo |
|---|---|---|
| Scheda da tavolo — 2 pagine A4 | [PDF](dist/cael-scheda-tavolo.pdf) | [HTML](dist/cael-scheda-tavolo.html) |
| Grimorio illustrato — 27 pagine A4 | [PDF](dist/cael-grimorio-illustrato.pdf) | [HTML](dist/cael-grimorio-illustrato.html) |

L'HTML contiene le immagini, non richiede servizi esterni ed è adattato al telefono. Il PDF è il riferimento per l'impaginazione A4.

## Contenuti e stato

La scheda concentra statistiche, risorse da annotare e riquadri con tempo, gittata/area, attacco o TS, effetto, durata, componenti, costo e pagina. Il grimorio conserva i dettagli e usa tutte le immagini già archiviate; non inventa un'illustrazione del famiglio.

I riferimenti sono al Player's Handbook 2024 in inglese, ripresi dalla [scheda verificata](../../lev02.md). Non sono pagine dell'edizione italiana. I comandi e le anomalie della fonte rimangono nel [registro tecnico esistente](../../mcp-verifica-2026-10-09.md), non nelle pagine del giocatore.

Guidance resta una proposta; forme, famiglio e lingue non sono selezionati automaticamente. I 19 PF restano subordinati alla conferma dell'incremento fisso. Il Circolo delle Stelle e Guiding Bolt compaiono solo nell'anteprima del livello 3. Le regole di campagna restano separate dal PHB. Le progressioni dubbie non sono adottate come verificate.

## Riprodurre

```sh
python -m pip install -r cael/edizioni/v1/requirements.txt
python cael/edizioni/v1/build.py
```

Occorrono le librerie di sistema di WeasyPrint e i font Lato e DejaVu. Nessun file font è distribuito. Il workflow dedicato prepara queste dipendenze e pubblica i nuovi risultati sulla sola branch di lavoro.

`build.py` legge la scheda originale e le immagini senza modificarle; scrive esclusivamente nella directory di output. Il catalogo breve è condiviso dalle due edizioni. Il controllo del blob originale impedisce rigenerazioni silenziose dopo cambiamenti della scheda: una revisione successiva deve aggiornare consapevolmente il riferimento e i dati sintetici.

La build verifica il numero di pagine (2 e 27), l'assenza di pagine di continuazione inattese, di caratteri sostitutivi e di comandi tecnici nel testo. La v1 è stata inoltre renderizzata e controllata visivamente, con prova dell'HTML a 390 px senza scorrimento orizzontale. La provenienza e gli hash delle immagini sono in `dist/provenienza.json`.
