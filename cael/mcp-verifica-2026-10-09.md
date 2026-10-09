# Cael Vesper — registro della verifica MCP

**Data:** 2026-10-09. **Ambito:** revisione della scheda attiva di livello 2, [lev02.md](lev02.md). La scheda storica `lev01.md` non viene aggiornata da questa revisione.

## Provenienza e metodo

La configurazione del personaggio, la storia e le regole della campagna provengono da `nomed/dnd/cael/lev02.md`, versione 0.4 del 2026-10-08, blob Git `fff6bb91c3d6fd85d3e30bdf5237976430a94def`.

Le regole aggiunte o ricontrollate provengono esclusivamente dalle risposte del server MCP **Dnd**, richieste con `ruleset: "2024"`. Per gli oggetti nominativi è stata selezionata la fonte `XPHB`; dalle ricerche e dai file misti sono state utilizzate soltanto le voci pertinenti con `source: "XPHB"`. Non sono state utilizzate ricerche web, D&D Beyond o altri repository come fonti di regole.

`XPHB` identifica il *Player’s Handbook 2024*. I numeri di pagina sono quelli del campo `page` delle voci inglesi restituite dal server: non costituiscono una verifica della paginazione dell'edizione italiana o un confronto con scansioni del libro. I nomi inglesi sono le chiavi di ricerca; il testo italiano della scheda è una sintesi operativa, non una traduzione ufficiale.

Il manifest MCP interrogato per il regolamento 2024 riportava `built_at: 2026-10-09T18:45:24.015Z` e `total_files: 378`. Questa data identifica il manifest, non garantisce da sola l'aggiornamento editoriale di ogni voce.

I valori applicati a Cael sono calcoli sui punteggi finali già confermati nella scheda: FOR 10, DES 16, COS 17, INT 10, SAG 18, CAR 10, competenza +2. Le distanze in metri sono adattamenti da tavolo secondo 5 piedi = 1,5 metri; i piedi originali sono conservati. I pesi degli oggetti restano in libbre. I prezzi indicano il valore di catalogo restituito dal server, non acquisti effettuati.

## Copertura delle voci

### Incantesimi

Tutte le righe seguenti sono state recuperate con `Dnd.spell_get`, usando il nome inglese, `source: "XPHB"` e `ruleset: "2024"`.

| Voce | Pagina MCP | Stato per Cael |
|---|---:|---|
| Starry Wisp | 320 | Trucchetto di classe già scelto |
| Produce Flame | 308 | Trucchetto di classe già scelto |
| Druidcraft | 266 | Magic Initiate, già scelto |
| Shillelagh | 316 | Magic Initiate, già scelto |
| Guidance | 282 | Proposta preesistente per il trucchetto di Magician, non confermata automaticamente |
| Healing Word | 284 | Uno dei cinque preparati da druido |
| Entangle | 268 | Uno dei cinque preparati da druido |
| Cure Wounds | 259 | Uno dei cinque preparati da druido |
| Thunderwave | 334 | Uno dei cinque preparati; progressione con slot superiori da verificare |
| Faerie Fire | 271 | Quinto preparato già confermato |
| Goodberry | 280 | Sempre preparato da Magic Initiate; anomalia del campo gittata documentata sotto |
| Speak with Animals | 318 | Sempre preparato da Druidic; rituale |
| Find Familiar | 272 | Lancio tramite Wild Companion; non aggiunto ai cinque preparati ordinari |
| Guiding Bolt | 282 | Solo anteprima del livello 3; progressione con slot superiori da verificare |

### Specie, background, talenti e capacità

| Voce | Strumento MCP | XPHB, pagina |
|---|---|---:|
| Human: Resourceful, Skillful, Versatile | `race_get` | 194 |
| Guide | `background_get` | 181 |
| Alert | `feat_get` | 200 |
| Magic Initiate | `feat_get` | 201 |
| Druid: tratti iniziali e progressione | `class_get` | 78 |
| Spellcasting | `class_get`, `resolvedFeatures` | 79 |
| Druidic | `class_get`, `resolvedFeatures` | 80 |
| Primal Order e Magician | `class_get`, `resolvedFeatures` | 80 |
| Wild Shape | `class_get`, `resolvedFeatures` | 80 |
| Wild Companion | `class_get`, `resolvedFeatures` | 81 |
| Accesso alla sottoclasse al livello 3 | `class_get`, `resolvedFeatures` | 81 |
| Circle of the Stars, Star Map, Starry Form, Archer, Chalice, Dragon | `subclassfeature_search`, classe Druid, sottoclasse Stars, livello 3 | 88 |
| Restrained | `condition_search` | 373 |
| Incapacitated | `condition_search` | 369 |
| Concentration | `omnisearch`, risultato di tipo `condition` | 363 |
| Heroic Inspiration | `omnisearch`, risultato di tipo `variantrule` | 368 |
| Ritual | `omnisearch`, risultato di tipo `variantrule` | 373 |

La ricerca delle capacità delle Stelle restituisce anche record TCE e duplicati senza descrizioni: non sono stati usati per sostituire le voci XPHB complete. Le capacità di livello 3 sono documentate ma non attribuite al Cael attuale.

### Armi, protezioni, strumenti ed equipaggiamento

`Dnd.item_get("Sickle", "XPHB")` non trovava l'arma. Il recupero è stato risolto all'interno dello stesso MCP con:

```json
{"content_type":"items-base","file_name":"items-base.json","ruleset":"2024"}
```

Il file contiene più edizioni: sono state selezionate le voci XPHB, non quelle PHB 2014.

| Voce | Recupero MCP | XPHB, pagina |
|---|---|---:|
| Sickle, Shortbow, Quarterstaff, Club | `fetch_content`: `items-base.json`, sezione `baseitem` | 215 |
| Wooden Staff, focus druidico | Stesso file, `baseitem` | 225 |
| Leather Armor, Shield | Stesso file, `baseitem` | 219 |
| Arrows (20) | Stesso file, `baseitem` | 222 |
| Cartographer’s Tools | Stesso file, `baseitem` | 220 |
| Light, Finesse, Ammunition | Stesso file, `itemProperty` | 213 |
| Two-Handed, Versatile, Range | Stesso file, `itemProperty` o `itemType` | 214 |
| Nick, Vex, Topple, Slow | Stesso file, `itemMastery` | 214 |
| Regola della competenza con gli strumenti | Stesso file, `itemType`, Tool | 220 |
| Explorer’s Pack e contenuto | `item_get` | 225 |
| Herbalism Kit | `item_get` | 221 |
| Torch | `item_get` | 229 |
| Quiver | `item_get` | 228 |
| Tent | `item_get` | 229 |

La presenza di una proprietà di maestria nel record di un'arma non concede a Cael la capacità Weapon Mastery: nessuna capacità del personaggio verificata in questa revisione la attribuisce. Club e Quarterstaff sono riferimenti per Shillelagh, non oggetti acquistati automaticamente.

## Correzioni applicabili alla scheda 0.4

| Voce | Vecchio valore o affermazione | Revisione |
|---|---|---|
| TS Forza | −1 | +0, dato FOR 10 |
| TS Intelligenza | +1 | +2: INT 0 e competenza 2 |
| Natura | +1 / +5 con Magician | +2 / +6 con Magician |
| Arcana con Magician | +3 | +4, senza competenza nell'abilità |
| Indagare | +1 | +2, con competenza da Skillful |
| Falcetto | Attacco +5, danni 1d4+3 | +2 e 1d4 taglienti; Light non è Finesse |
| Arco corto | Arma marziale senza competenza | Arma semplice: +5, 1d6+3 perforanti; richiede due mani per attaccare |
| Speak with Animals | Riferimento a quattro preparati | I preparati ordinari al livello 2 sono cinque |
| Guidance | Proposta dispersa nel testo | Esplicitamente proposta, non confermata dalla revisione |
| Produce Flame | Descrizione abbreviata | Distinti lancio bonus e attacco con azione; l'attacco non termina l'effetto |
| Dotazione da viaggio | Raccomandazione generica di comprare torce e acciarino | Explorer’s Pack contiene già 10 torce, acciarino e 2 flaconi d'olio |
| Concentrazione +7 | Possibile confusione con il druido base | +3 standard; +7 soltanto per la variante di campagna riportata nel repository |

## Dati incompleti o da verificare: nessuna sostituzione esterna

### Thunderwave: slot superiori

Il campo `entriesHigherLevel` restituisce letteralmente:

> The damage increases by 2d8 for each spell slot level above 1.

Il dato viene registrato, ma la progressione è lasciata da verificare prima di utilizzarla. Non viene sostituita con un numero tratto da altre fonti. Al livello 2 Cael possiede soltanto slot di 1°: il profilo operativo resta 2d8 e non dipende da questo campo.

### Guiding Bolt: slot superiori

Il campo `entriesHigherLevel` restituisce:

> The damage increases by 4d6 for each spell slot level above 1.

Anche questo campo è lasciato da verificare, senza introdurre una progressione alternativa. L'anteprima riporta soltanto i 4d6 del lancio base e il beneficio del successivo attacco. L'incantesimo non è attivo per Cael al livello 2.

### Goodberry: gittata

Il record restituisce `range.distance.type: "touch"`, mentre la descrizione colloca le dieci bacche nella mano dell'incantatore. La scheda conserva entrambe le informazioni distinguendole: non sostituisce silenziosamente `touch` con un'altra gittata e non trasforma il lancio in una guarigione a contatto. La guarigione deriva dal mangiare una bacca.

### Find Familiar: testo incompleto e metadati di classe

Il testo delle forme alternative termina con `or another Beast that has a .`: il requisito è perso nella risposta. Non viene ricostruito a memoria. Le forme nominate nel testo sono riportate, ma la scelta concreta di un famiglio resta aperta.

`class_get` inserisce inoltre Find Familiar nei metadati `additionalSpells.prepared` del livello 2. Il testo risolto di Wild Companion descrive invece una modalità specifica di lancio spendendo uno slot o un uso di Wild Shape. La scheda documenta questa modalità esplicita; non deduce dai soli metadati un nuovo lancio rituale gratuito o un ottavo incantesimo ordinariamente preparato.

### Rinvii persi, strumenti di recupero e regole generali

Alcuni campi testuali perdono i nomi contenuti nei rinvii: esempi in Magician, Magic Initiate, Versatile dell'umano e nelle tabelle della classe. Quando il dato è presente in un altro campo strutturato della stessa risposta viene utilizzato con questa provenienza; altrimenti non viene inventato.

`book_content_get` per XPHB ha restituito `sections: []`. Questo non significa che il manuale non contenga quelle regole: indica che quell'azione non ne ha fornito il testo. Concentrazione, rituali e Ispirazione Eroica sono stati comunque recuperati da altre azioni dello stesso MCP. La ricerca esatta della regola «One Spell with a Spell Slot per Turn» non ha restituito una voce; non è quindi stata aggiunta una pagina non verificata per quel limite.

`item_get("Druidic Focus", "XPHB")` non ha trovato la voce generica. Il Wooden Staff scelto nel repository è però presente in `items-base.json`, con tipo druidico, statistiche d'arma e pagina 225. Non viene convertito in un focus arcano o duplicato nell'inventario.

## Decisioni che questa revisione non prende

Non sono cambiati livello, caratteristiche, background, talento Alert, scelte di Magic Initiate o cinque incantesimi preparati. Non vengono scelte al posto del giocatore le quattro forme di Wild Shape, la forma del famiglio, le lingue ancora aperte o il trucchetto aggiuntivo di Magician. I 19 PF sono mantenuti come calcolo a valore fisso già proposto, soggetto alla conferma del DM.

Le regole del Dominio Oscuro e la storia restano materiale del repository. I due prontuari del master non sono stati consultati: nessuna pagina viene inventata. In particolare, l'idoneità di Produce Flame come «luce viva» contro il Miasma resta una decisione del DM, non un beneficio attribuito dal record dell'incantesimo.
