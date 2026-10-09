# ✨ Cael Vesper — Il Cartografo del Cielo Morto

> «Non so se le stelle siano ancora lassù. So che qualcuno si è preso parecchio disturbo per impedirci di guardare.»

**Campagna:** Il Dominio Oscuro · **Versione:** 0.5 — 2026-10-09 · **Livello attuale: 2** · **Regolamento: D&D 2024**.

**Fonti della revisione:** server MCP **Dnd** per le regole; scheda preesistente del repository per le scelte del personaggio, i punteggi, la storia e le varianti di campagna. Dettagli, interrogazioni e campi da verificare sono nel [registro della verifica MCP](mcp-verifica-2026-10-09.md). Nessuna fonte web utilizzata per questa revisione.

In questa scheda **PHB 2024 / XPHB** indica il *Player’s Handbook 2024*: le pagine sono quelle dei record inglesi restituiti dall'MCP, non pagine verificate sull'edizione italiana. I nomi inglesi identificano esattamente le voci consultate; le descrizioni italiane sono sintesi operative. Le distanze metriche seguono l'adattamento da tavolo **5 piedi = 1,5 metri**; i valori originali in piedi sono conservati.

**Stati delle informazioni:** le capacità di livello 2 sono attive; Guidance è una proposta ancora da confermare; le capacità delle Stelle sono soltanto un'anteprima del livello 3; le regole del Dominio Oscuro sono materiale di campagna non verificato nei prontuari originali.

## Indice

- [Riepilogo del personaggio](#riepilogo-del-personaggio)
- [Specie, background e talenti](#specie-background-e-talenti)
- [Capacità di classe attuali](#capacità-di-classe-attuali)
- [Incantesimi: elenco e risorse](#incantesimi-elenco-e-risorse)
- [Trucchetti: dettagli](#trucchetti-dettagli)
- [Incantesimi di primo livello: dettagli](#incantesimi-di-primo-livello-dettagli)
- [Armi, difese ed equipaggiamento](#armi-difese-ed-equipaggiamento)
- [Concentrazione e condizioni rilevanti](#concentrazione-e-condizioni-rilevanti)
- [Anteprima del livello 3: Circolo delle Stelle](#anteprima-del-livello-3-circolo-delle-stelle)
- [Regole del Dominio Oscuro: separate dal PHB](#regole-del-dominio-oscuro-separate-dal-phb)
- [Storia e personalità](#storia-e-personalità)
- [Questioni ancora aperte](#questioni-ancora-aperte)

## Riepilogo del personaggio

| Voce | Valore | Provenienza |
|---|---|---|
| Nome | Cael Vesper | Scheda del giocatore |
| Specie | Umano — Human | XPHB p. 194 |
| Classe e livello | Druido — Druid, livello 2 | XPHB p. 78; livello confermato nel repository |
| Primal Order | Magician | XPHB p. 80; scelta già presente |
| Sottoclasse prevista | Circle of the Stars, **dal livello 3** | XPHB pp. 81, 88; non ancora attiva |
| Background | Guida — Guide | XPHB p. 181 |
| Allineamento narrativo | Neutrale Buono, pragmatico e poco devoto | Storia del personaggio |
| Tipo, taglia, velocità | Umanoide; Media; 9 m / 30 ft | Human, XPHB p. 194; taglia già scelta |
| Bonus di competenza | +2 | Livello 2 della scheda |
| Classe Armatura | **16 con cuoio e scudo; 14 senza scudo** | Leather Armor e Shield, XPHB p. 219; DES +3 |
| Punti ferita massimi | **19**, con avanzamento a valore fisso | Calcolo già proposto, da confermare col DM |
| Iniziativa | **+5** | DES +3 e Alert +2, XPHB p. 200 |
| Percezione passiva | **16** | Valore della scheda, Percezione +6 |
| Attacco con incantesimi | **+6** | SAG +4 e competenza +2 |
| CD degli incantesimi | **14** | 8 + SAG 4 + competenza 2 |

### Caratteristiche e tiri salvezza

I punteggi sono **finali**, comunicati dal giocatore: non si aggiungono nuovamente i bonus del background. Totale dei punteggi: **81**.

| Caratteristica | Punteggio | Modificatore | Competenza nel TS | Totale TS |
|---|---:|---:|---|---:|
| Forza | 10 | +0 | No | **+0** |
| Destrezza | 16 | +3 | No | **+3** |
| Costituzione | 17 | +3 | No | **+3** |
| Intelligenza | 10 | +0 | Sì, druido | **+2** |
| Saggezza | 18 | +4 | Sì, druido | **+6** |
| Carisma | 10 | +0 | No | **+0** |

**Fonte delle competenze nei TS:** Druid, XPHB p. 78, `Dnd.class_get`. I totali sono ricalcolati sui punteggi del personaggio. Il **+7 alla concentrazione** non è il TS ordinario di Costituzione: è la variante di campagna descritta più avanti.

### Abilità e strumenti scelti

| Voce | Calcolo | Totale | Origine |
|---|---|---:|---|
| Percezione | SAG 4 + competenza 2 | **+6** | Abilità del druido, XPHB p. 78 |
| Natura | INT 0 + competenza 2 + Magician 4 | **+6** | Druido p. 78 e Magician p. 80 |
| Arcana | INT 0 + Magician 4 | **+4** | Magician p. 80; **nessuna competenza** scelta in Arcana |
| Furtività | DES 3 + competenza 2 | **+5** | Guide, XPHB p. 181 |
| Sopravvivenza | SAG 4 + competenza 2 | **+6** | Guide, XPHB p. 181 |
| Indagare | INT 0 + competenza 2 | **+2** | Skillful dell'umano, XPHB p. 194 |
| Strumenti da cartografo | SAG 4 + competenza 2 | **+6** per l'uso basato su SAG | Guide p. 181; oggetto p. 220 |
| Kit da erborista | INT 0 + competenza 2 | **+2** per l'uso basato su INT | Druido p. 78; oggetto p. 221 |

Magician aumenta le prove di **Intelligenza (Arcana o Natura)**: non aggiunge automaticamente Saggezza a ogni prova con il kit da erborista. Senza Magician, Natura sarebbe +2. Le due abilità selezionate dalla classe restano **Percezione e Natura**.

**Lingue:** Comune come già indicato nella scheda, **Druidico** dalla classe; le ulteriori lingue restano da scegliere/confermare con il DM. Questa revisione non assegna nuove lingue.

### Punti ferita e risorse

Il dado vita del druido è **d8** — XPHB p. 78. Al livello 2 la riserva del personaggio è **2d8**.

**PF a valore fisso:** livello 1 `8 + 3 = 11`; incremento al livello 2 `5 + 3 = 8`; totale **19**. Se il master richiede il tiro, il totale da determinare è `11 + 1d8 + 3`. Non è stato inventato un risultato del dado. Con il medesimo criterio fisso, il livello 3 porterebbe a 27 PF, ma il personaggio è ancora di livello 2.

| Risorsa | Massimo attuale | Recupero documentato |
|---|---:|---|
| Slot di 1° livello | **3** | Tutti al riposo lungo — Spellcasting, p. 79 |
| Wild Shape | **2 usi** | Uno al riposo breve, tutti al lungo — p. 80 |
| Goodberry senza slot | **1 lancio** | Riposo lungo — Magic Initiate, p. 201 |
| Ispirazione Eroica | Da annotare | Resourceful la concede al termine del riposo lungo — p. 194 |

Questa tabella indica le disponibilità massime: non presume che le risorse attualmente spese durante la sessione siano state recuperate. I riposi della campagna possono avere requisiti più restrittivi.

## Specie, background e talenti

### Umano — Human

**Fonte:** XPHB p. 194, `Dnd.race_get("Human")`.

**Resourceful.** Ottieni Ispirazione Eroica quando termini un riposo lungo.

**Skillful.** Ottieni competenza in un'abilità a scelta. Per Cael la scelta già presente è **Indagare**, ora ricalcolata a +2.

**Versatile.** Ottieni un talento Origine. La scelta del personaggio è **Alert**. È aggiuntivo rispetto al talento del background: non sostituisce Magic Initiate.

**Ispirazione Eroica — Heroic Inspiration, XPHB p. 368, `Dnd.omnisearch`.** Puoi spenderla per ritirare **un qualsiasi dado immediatamente dopo averlo tirato**; devi usare il nuovo risultato. Quando ne ricevi una mentre la possiedi già, la nuova è persa a meno che tu la dia a un personaggio giocante che ne è privo. Non si tratta soltanto di vantaggio su un tiro per colpire.

### Guida — Guide

**Fonte:** XPHB p. 181, `Dnd.background_get("Guide")`.

Conferisce competenza in **Furtività**, **Sopravvivenza** e **strumenti da cartografo**, oltre al talento **Magic Initiate (Druid)**. Le caratteristiche ammesse per gli incrementi sono Destrezza, Costituzione e Saggezza, distribuendo +2/+1 oppure +1 a tutte e tre: nella presente scheda i punteggi finali includono già quanto deciso dal giocatore.

La dotazione scelta è il pacchetto A: **arco corto, 20 frecce, faretra, strumenti da cartografo, giaciglio, tenda, abiti da viaggiatore e 3 mo**. Non è stato scelto il pacchetto alternativo in denaro.

### Alert

**Categoria:** talento Origine. **Fonte:** XPHB p. 200, `Dnd.feat_get("Alert")`. **Origine per Cael:** Versatile dell'umano.

**Initiative Proficiency.** Aggiungi il bonus di competenza al tiro di iniziativa: per Cael `1d20 + 3 + 2 = 1d20 + 5`.

**Initiative Swap.** Subito dopo aver tirato l'iniziativa puoi scambiare il tuo risultato con quello di **un alleato consenziente nello stesso combattimento**. Lo scambio non è possibile se tu o l'alleato avete la condizione Incapacitated.

Alert **non aumenta la CA** e questa versione non va sostituita con i benefici di un'altra edizione.

### Magic Initiate — scelta Druid

**Categoria:** talento Origine. **Fonte:** XPHB p. 201, `Dnd.feat_get("Magic Initiate")`. **Origine per Cael:** background Guide, p. 181.

Impari due trucchetti e scegli un incantesimo di 1° livello dalla stessa lista ammessa dal talento. La caratteristica magica può essere Intelligenza, Saggezza o Carisma; **Cael ha scelto Saggezza**.

| Scelta di Cael | Beneficio |
|---|---|
| Druidcraft | Trucchetto aggiuntivo rispetto a quelli di classe |
| Shillelagh | Trucchetto aggiuntivo; utilizza SAG per i benefici descritti nell'incantesimo |
| Goodberry | Sempre preparato; un lancio senza slot per riposo lungo; ulteriori lanci con slot |

Quando ottieni un nuovo livello puoi sostituire **uno** degli incantesimi scelti per questo talento con un altro dello stesso livello e della stessa lista. Il talento è ripetibile soltanto scegliendo ogni volta una lista differente. Nessuna scelta viene sostituita automaticamente da questa revisione.

## Capacità di classe attuali

### Spellcasting — livello 1

**Fonte:** XPHB p. 79, capacità risolta in `Dnd.class_get("Druid")`; progressione nella medesima risposta, voce Druid p. 78.

La caratteristica magica è **Saggezza**. Cael ha attacco magico **+6**, CD **14**, **due trucchetti di classe**, **cinque incantesimi preparati di livello 1+** e **tre slot di 1° livello**. I trucchetti aggiuntivi di Magician e Magic Initiate sono distinti dai due di classe.

Recuperi gli slot spesi al termine di un riposo lungo e puoi cambiare la lista dei preparati dopo quel riposo, scegliendo incantesimi da druido di livelli per cui possiedi slot. Gli incantesimi che una capacità di classe rende sempre preparati non occupano posti nella lista ordinaria. Quando guadagni un livello da druido puoi sostituire un tuo trucchetto da druido con un altro della lista. Puoi usare un **focus druidico** per gli incantesimi da druido.

### Druidic — livello 1

**Fonte:** XPHB p. 80, `Dnd.class_get`, capacità Druidic.

Conosci la lingua segreta **Druidico** e hai **Speak with Animals sempre preparato**. Puoi lasciare messaggi nascosti in Druidico: chi conosce la lingua ne nota automaticamente la presenza; gli altri possono individuarli con una prova di **Intelligenza (Indagare) CD 15**, ma non decifrarli senza magia.

### Primal Order: Magician — livello 1

**Fonte:** XPHB p. 80, `Dnd.class_get`, capacità Primal Order e Magician.

La scelta già adottata è **Magician**, non l'alternativa Warden. Ottieni **un trucchetto aggiuntivo da druido** e un bonus alle prove di Intelligenza basate su **Arcana o Natura**, pari al modificatore di Saggezza, minimo +1. Per Cael il bonus è +4.

**Trucchetto aggiuntivo ancora da formalizzare:** la versione precedente consigliava **Guidance**. La descrizione è inclusa sotto, ma non viene trasformata in una scelta confermata al posto del giocatore.

### Wild Shape — livello 2

**Fonte:** XPHB p. 80, `Dnd.class_get`, capacità Wild Shape.

Con **un'azione bonus** spendi un uso per assumere una delle forme di Bestia che conosci. Al livello 2 hai **due usi**, **quattro forme conosciute**, **GS massimo 1/4**, e non puoi scegliere una forma con velocità di volo. Recuperi un uso con un riposo breve e tutti con un riposo lungo. Dopo un riposo lungo puoi sostituire una forma conosciuta con un'altra idonea.

La forma dura fino a **un'ora** al livello 2. Puoi lasciarla con un'azione bonus; termina anche quando usi nuovamente Wild Shape, diventi Incapacitated o muori.

Mantieni personalità, ricordi e capacità di parlare. Conservi inoltre tipo di creatura, **i tuoi PF e dadi vita**, Intelligenza, Saggezza, Carisma, capacità di classe, lingue e talenti. Le altre statistiche seguono il blocco della Bestia. Mantieni le competenze nelle abilità e nei TS, usando il tuo bonus di competenza, e acquisisci quelle della creatura; se un modificatore del blocco della Bestia è superiore al tuo per un'abilità o TS, usi quello superiore.

Quando assumi la forma guadagni **2 PF temporanei**: **non sostituisci i tuoi PF con quelli della Bestia**. Non puoi lanciare incantesimi in questa forma, ma la trasformazione non interrompe la concentrazione o gli effetti di un incantesimo già lanciato.

L'equipaggiamento può cadere a terra, fondersi con la forma o essere indossato se la nuova anatomia lo permette, a giudizio del DM. Non cambia automaticamente dimensioni; gli oggetti fusi non hanno effetto mentre rimangono fusi.

**Forme conosciute:** quattro scelte da annotare. Il testo MCP consiglia Rat, Riding Horse, Spider e Wolf, ma non risultano scelte dal giocatore nella scheda: **non vengono assegnate automaticamente**.

### Wild Companion — livello 2

**Fonte:** XPHB p. 81, `Dnd.class_get`, capacità Wild Companion; incantesimo Find Familiar p. 272.

Con **un'azione Magia** puoi spendere **uno slot oppure un uso di Wild Shape** per lanciare **Find Familiar senza componenti materiali**. Il famiglio evocato in questo modo è **Fatato — Fey** e scompare quando termini un riposo lungo.

Il consumo di Wild Shape è condiviso con la trasformazione: non esiste una riserva aggiuntiva di due evocazioni. Questa modalità non richiede l'ora di lancio né l'incenso del normale incantesimo. Il suo costo non viene eliminato semplicemente aspettando dieci minuti. I dettagli del famiglio sono nella voce dell'incantesimo.

## Incantesimi: elenco e risorse

**Valori attuali:** SAG +4; attacco +6; CD 14; **3 slot di 1° livello**, nessuno di livello superiore.

| Provenienza | Incantesimi | Stato |
|---|---|---|
| Due trucchetti di classe | Starry Wisp, Produce Flame | Scelti |
| Due trucchetti da Magic Initiate | Druidcraft, Shillelagh | Scelti |
| Un trucchetto da Magician | Guidance | **Proposta da confermare** |
| Cinque preparati da druido | Healing Word, Entangle, Cure Wounds, Thunderwave, Faerie Fire | Scelti; Faerie Fire è il quinto confermato |
| Magic Initiate | Goodberry | Sempre preparato; non occupa uno dei cinque posti |
| Druidic | Speak with Animals | Sempre preparato; non occupa uno dei cinque posti |
| Wild Companion | Find Familiar | Lancio tramite capacità, documentato separatamente |

**Legenda delle componenti:** V = verbale; S = somatica; M = materiale. Le voci riportano quelle richieste dall'incantesimo; non viene attribuita a Cael un'esenzione generale dalle componenti.

**Rituali — XPHB p. 373, voce Ritual recuperata con `Dnd.omnisearch`.** Se hai preparato un incantesimo con il tag Ritual, puoi lanciarlo come rituale: occorrono **10 minuti in più** rispetto al tempo normale, senza consumare uno slot e senza poter aumentare il livello del lancio. Questo si applica a Speak with Animals. Non si deduce dai soli metadati di classe un ulteriore accesso rituale gratuito a Find Familiar: per Cael è documentata la modalità specifica di Wild Companion.

## Trucchetti: dettagli

### Starry Wisp

**Fonte:** XPHB p. 320, `Dnd.spell_get("Starry Wisp", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | Trucchetto; Invocazione — Evocation |
| Provenienza per Cael | Trucchetto di classe |
| Lancio | 1 azione |
| Gittata | 18 m / 60 ft |
| Componenti | V, S |
| Durata | Istantanea, con effetto secondario fino alla fine del tuo prossimo turno |
| Concentrazione / rituale | No / no |
| Bersaglio | Una creatura o un oggetto |
| Risoluzione di Cael | Attacco con incantesimo a distanza **1d20 +6** contro CA |
| Danno | **1d8 radiante**, senza aggiungere SAG |

Scagli una piccola luce. Se colpisci, oltre ai danni, il bersaglio emette **luce fioca entro 3 m / 10 ft** e non può beneficiare della condizione Invisible fino alla fine del tuo prossimo turno. È un effetto sul bersaglio colpito, non una lanterna costantemente portata dal gruppo. Il testo consente di bersagliare una creatura o un oggetto: non garantisce un colpo automatico contro un bersaglio invisibile.

**Progressione:** 2d8 al livello 5, 3d8 all'11, 4d8 al 17. Nessuno slot consumato.

### Produce Flame

**Fonte:** XPHB p. 308, `Dnd.spell_get("Produce Flame", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | Trucchetto; Evocazione — Conjuration |
| Provenienza per Cael | Trucchetto di classe |
| Lancio | **1 azione bonus** per creare la fiamma |
| Gittata del lancio | Personale |
| Gittata dell'attacco | 18 m / 60 ft |
| Componenti | V, S |
| Durata | 10 minuti |
| Concentrazione / rituale | No / no |
| Attacco | **1 azione Magia**, contro una creatura o un oggetto |
| Risoluzione di Cael | **1d20 +6** contro CA; **1d8 fuoco** se colpisce |

Una fiamma appare nella tua mano. Mentre rimane nella mano, **non produce calore e non incendia nulla**. Illumina intensamente entro **6 m / 20 ft** e fiocamente per altri **6 m / 20 ft**.

Per tutta la durata puoi spendere un'azione Magia per scagliare fuoco. **Nel testo 2024 restituito dall'MCP attaccare non termina l'incantesimo.** Puoi quindi creare la fiamma con l'azione bonus e attaccare con l'azione nello stesso turno; nei turni successivi basta l'azione per attaccare ancora. Rilanciare Produce Flame termina l'istanza precedente.

**Progressione:** 2d8 al livello 5, 3d8 all'11, 4d8 al 17. Non aggiungi SAG ai danni al livello attuale. Non richiede slot o concentrazione. L'idoneità come «luce viva» contro il Miasma **non è stabilita da questo incantesimo**: è una questione della campagna.

### Druidcraft

**Fonte:** XPHB p. 266, `Dnd.spell_get("Druidcraft", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | Trucchetto; Trasmutazione |
| Provenienza per Cael | Magic Initiate, lista Druid |
| Lancio / gittata | 1 azione; 9 m / 30 ft |
| Componenti | V, S |
| Durata | Istantanea; il segnale meteorologico persiste per un round |
| Concentrazione / rituale | No / no |
| Attacco, TS, danni | Nessuno previsto |

Scegli uno degli effetti descritti: un piccolo segnale sensoriale innocuo che prevede il tempo **locale nelle prossime 24 ore**; far sbocciare un fiore, aprire un baccello o germogliare una gemma; un effetto sensoriale innocuo entro un **cubo di 1,5 m / 5 ft**; oppure **accendere o spegnere una candela, una torcia o un fuoco da campo**.

Non trasforma questi effetti in attacchi o danni. Nessun potenziamento con il livello riportato. È questo trucchetto a menzionare esplicitamente l'accensione di una torcia, a differenza della fiamma tenuta in mano di Produce Flame.

### Shillelagh

**Fonte:** XPHB p. 316, `Dnd.spell_get("Shillelagh", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | Trucchetto; Trasmutazione |
| Provenienza per Cael | Magic Initiate, lista Druid; caratteristica scelta SAG |
| Lancio / gittata | 1 azione bonus; personale |
| Componenti | V, S, M: vischio |
| Durata | 1 minuto |
| Concentrazione / rituale | No / no |
| Oggetto richiesto | **Club o Quarterstaff che stai impugnando** |
| Attacco potenziato di Cael | **1d20 +6**; danni **1d8 +4** |

Per gli attacchi in mischia con l'arma idonea puoi usare la caratteristica magica al posto di Forza sia per colpire sia per i danni. Il dado dell'arma diventa d8; quando infliggi danni scegli **forza — Force** oppure il normale tipo dell'arma, contundente per Club/Quarterstaff.

**Il lancio non comprende un attacco gratuito:** l'azione bonus potenzia l'arma, l'attacco usa la normale azione Attaccare. L'effetto termina prima della scadenza se lo rilanci o lasci andare l'arma. Non si applica al falcetto; **Club non significa Mace**.

**Progressione del dado:** d10 al livello 5, d12 all'11, 2d6 al 17. Il modificatore della caratteristica utilizzata rimane distinto dal dado.

La dotazione precedente indica un bastone come focus. Il record MCP Wooden Staff ne documenta anche le statistiche d'arma; l'uso come **Quarterstaff idoneo a Shillelagh** va esplicitato nella dotazione con il DM, senza aggiungere automaticamente un'altra arma acquistata.

### Guidance — proposta per Magician

**Fonte:** XPHB p. 282, `Dnd.spell_get("Guidance", source="XPHB", ruleset="2024")`. **Stato:** proposta già presente nella scheda, da confermare.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | Trucchetto; Divinazione |
| Lancio / gittata | 1 azione; contatto |
| Componenti | V, S |
| Durata | **Concentrazione fino a 1 minuto** |
| Rituale | No |
| Bersaglio | Una creatura consenziente |
| Beneficio | **+1d4 alle prove che utilizzano un'abilità scelta** |

Tocchi la creatura e scegli un'abilità, per esempio Furtività. Finché dura l'effetto aggiunge 1d4 a **ogni** prova che utilizza quell'abilità; il testo 2024 non limita il beneficio a una sola prova. Non concede bonus ai tiri per colpire o ai tiri salvezza.

Richiedendo concentrazione, secondo la regola standard interrompe Entangle o Faerie Fire se inizi a lanciarlo mentre mantieni uno di essi. Nessuno slot consumato. La futura Star Map può fornire lo stesso trucchetto, ma non è attiva al livello 2.

## Incantesimi di primo livello: dettagli

### Healing Word — Parola Guaritrice

**Fonte:** XPHB p. 284, `Dnd.spell_get("Healing Word", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Abiurazione |
| Provenienza | Uno dei cinque preparati da druido |
| Lancio / gittata | **1 azione bonus**; 18 m / 60 ft |
| Componenti | **V soltanto** |
| Durata | Istantanea |
| Concentrazione / rituale | No / no |
| Bersaglio | Una creatura scelta **che puoi vedere** |
| Effetto per Cael | Recupera **2d4 +4 PF** |
| Costo | Uno slot |

Non richiede tiro per colpire o TS. La differenza operativa rispetto a Cure Wounds è la cura a distanza con azione bonus, mantenendo il requisito di vedere il bersaglio.

**Slot superiori, dato MCP:** +2d4 di guarigione per ogni livello dello slot oltre il primo. Al livello 2 Cael usa soltanto il profilo base.

### Entangle — Intralciare

**Fonte:** XPHB p. 268, `Dnd.spell_get("Entangle", source="XPHB", ruleset="2024")`. **Condizione collegata:** Restrained, XPHB p. 373, `Dnd.condition_search`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Evocazione — Conjuration |
| Provenienza | Uno dei cinque preparati da druido |
| Lancio / gittata | 1 azione; 27 m / 90 ft |
| Area | **Quadrato di 6 m / 20 ft di lato**, sul terreno |
| Componenti | V, S |
| Durata | **Concentrazione fino a 1 minuto** |
| Rituale | No |
| Tiro iniziale | **TS Forza CD 14** |
| Danni / costo | Nessun danno; uno slot |

Le piante rendono il terreno nell'area **difficile** per la durata; scompaiono al termine dell'incantesimo. Ogni creatura presente nell'area al momento del lancio, **eccetto Cael**, deve superare il TS oppure essere **Trattenuta — Restrained** fino al termine dell'effetto. Gli alleati non hanno un'esenzione generale.

Una creatura trattenuta può spendere **un'azione** per una prova di **Forza (Atletica) CD 14**: se riesce si libera. Questa è una prova di abilità, **non un nuovo TS**. Il testo non applica nuovamente il vincolo a chi entra nell'area dopo il lancio; resta il terreno difficile.

**Trattenuto non significa paralizzato:** velocità 0 e non aumentabile; attacchi contro la creatura con vantaggio; suoi attacchi con svantaggio; suoi TS di Destrezza con svantaggio. Può ancora attaccare rispettando tali effetti. Nessuna progressione con slot superiori riportata nella voce.

### Cure Wounds — Cura Ferite

**Fonte:** XPHB p. 259, `Dnd.spell_get("Cure Wounds", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Abiurazione |
| Provenienza | Uno dei cinque preparati da druido |
| Lancio / gittata | 1 azione; **contatto** |
| Componenti | V, S |
| Durata | Istantanea |
| Concentrazione / rituale | No / no |
| Effetto per Cael | Una creatura toccata recupera **2d8 +4 PF** |
| Costo | Uno slot |

Nessun tiro per colpire o TS. Cura più di Healing Word con il profilo base, ma richiede l'azione e il contatto. Un famiglio può consegnare il contatto alle condizioni descritte in Find Familiar.

**Slot superiori, dato MCP:** +2d8 di guarigione per ogni livello dello slot oltre il primo. Al livello 2 Cael non dispone di questi slot.

### Thunderwave — Onda Tonante

**Fonte:** XPHB p. 334, `Dnd.spell_get("Thunderwave", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Invocazione — Evocation |
| Provenienza | Uno dei cinque preparati da druido |
| Lancio | 1 azione |
| Area | **Cubo di 4,5 m / 15 ft di lato che origina da te** |
| Componenti | V, S |
| Durata | Istantanea |
| Concentrazione / rituale | No / no |
| Tiro | **TS Costituzione CD 14** |
| Costo | Uno slot |

Ogni creatura nell'area effettua il TS. **Fallimento:** 2d8 danni da tuono e spinta di **3 m / 10 ft** lontano da Cael. **Successo:** metà danni, senza spinta. Gli oggetti non assicurati e interamente nel cubo vengono spinti di 3 metri. Il boato è udibile entro **90 m / 300 ft**.

Non è un'esplosione piazzabile a distanza: il cubo origina dall'incantatore. Il testo non esclude automaticamente gli alleati nell'area.

**Campo da verificare:** l'MCP restituisce un aumento di **2d8 per livello dello slot oltre il primo**. Questa progressione non è adottata automaticamente come dato risolto e non viene sostituita con valori esterni: è registrata nel documento di verifica. Il profilo attualmente utilizzabile da Cael rimane **2d8 con slot di 1° livello**.

### Faerie Fire — Fuoco Fatato nella scheda

**Fonte:** XPHB p. 271, `Dnd.spell_get("Faerie Fire", source="XPHB", ruleset="2024")`.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Invocazione — Evocation |
| Provenienza | Quinto preparato da druido, già confermato |
| Lancio / gittata | 1 azione; 18 m / 60 ft |
| Area | **Cubo di 6 m / 20 ft di lato** |
| Componenti | **V soltanto** |
| Durata | **Concentrazione fino a 1 minuto** |
| Rituale | No |
| Tiro delle creature | **TS Destrezza CD 14** |
| Danni / costo | Nessun danno; uno slot |

Gli oggetti nel cubo vengono contornati di luce blu, verde o viola, a scelta; le creature sono contornate se falliscono il TS. Gli oggetti e le creature influenzati emettono **luce fioca entro 3 m / 10 ft** e non possono beneficiare della condizione Invisible.

Gli attacchi contro un bersaglio influenzato hanno **vantaggio se l'attaccante può vederlo**. Non infligge danni, non immobilizza e può coinvolgere anche alleati. Nessun potenziamento con slot superiori riportato nella voce.

### Goodberry — Bacche Benefiche

**Fonte:** XPHB p. 280, `Dnd.spell_get("Goodberry", source="XPHB", ruleset="2024")`; accesso da Magic Initiate, p. 201.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Evocazione — Conjuration |
| Provenienza | Magic Initiate, lista Druid; sempre preparato |
| Lancio | 1 azione |
| Gittata restituita nel campo MCP | **Contatto — touch; campo da verificare** |
| Componenti | V, S, M: un rametto di vischio |
| Durata | **24 ore** |
| Concentrazione / rituale | No / no |
| Costo per Cael | Un lancio senza slot per riposo lungo; oppure uno slot |

La **descrizione** dice che compaiono **dieci bacche nella tua mano**. Una creatura usa **un'azione bonus** per mangiarne una: recupera **1 PF** e riceve nutrimento sufficiente per un giorno. Le bacche non consumate **scompaiono** quando termina l'incantesimo.

Il lancio non è una cura a contatto: la guarigione avviene mangiando una bacca. La voce non descrive una procedura per imboccare automaticamente una creatura incosciente; non la si aggiunge come regola certa.

**Nota di integrità:** il campo gittata `touch` e la collocazione delle bacche nella mano del lanciatore sono riportati distintamente, senza correggere il server con altre fonti. Nessuna progressione con slot superiori è indicata. Non aggiungi SAG al singolo punto ferita della bacca.

### Speak with Animals — Parlare con gli Animali

**Fonte:** XPHB p. 318, `Dnd.spell_get("Speak with Animals", source="XPHB", ruleset="2024")`; Druidic p. 80; Ritual p. 373.

| Campo | Dettaglio |
|---|---|
| Livello e scuola | 1°; Divinazione |
| Provenienza | Sempre preparato da Druidic, fuori dai cinque posti |
| Lancio / gittata | 1 azione; personale |
| Componenti | V, S |
| Durata | 10 minuti |
| Concentrazione | No |
| Rituale | **Sì: 10 minuti aggiuntivi di lancio, senza slot** |
| Lancio ordinario | Consuma uno slot |

Comprendi e comunichi verbalmente con creature di tipo **Bestia — Beast**, potendo usare con esse le opzioni di abilità dell'azione Influence. Le informazioni dipendono da ciò che la Bestia ha percepito: il testo menziona luoghi vicini, mostri e percezioni dell'ultimo giorno, con interessi generalmente legati a sopravvivenza e compagnia.

Comunicazione non significa controllo o amicizia automatica. L'effetto riguarda le Bestie, non ogni creatura che abbia un aspetto animale. Nessun potenziamento con slot superiori riportato.

### Find Familiar — Trova Famiglio, tramite Wild Companion

**Fonte:** XPHB p. 272, `Dnd.spell_get("Find Familiar", source="XPHB", ruleset="2024")`; modalità di Cael: **Wild Companion, p. 81**.

| Campo | Incantesimo ordinario | Modalità documentata per Cael |
|---|---|---|
| Livello e scuola | 1°; Evocazione — Conjuration | Invariati |
| Tempo di lancio | 1 ora; il record ha il tag Ritual | **1 azione Magia** |
| Gittata iniziale | 3 m / 10 ft | Invariata |
| Componenti | V, S; incenso acceso da almeno 10 mo, consumato | **V, S; nessuna componente materiale** |
| Durata indicata | Istantanea; il famiglio permane secondo le regole della voce | **Scompare al termine del riposo lungo** |
| Concentrazione | No | No |
| Tipo del famiglio | Celestiale, Fatato o Immondo | **Fatato — Fey** |
| Costo | Normale accesso all'incantesimo | **Uno slot oppure un uso di Wild Shape** |

Il famiglio compare in uno spazio libero entro gittata, agisce autonomamente ma obbedisce ai tuoi comandi. Il testo nomina **Bat, Cat, Frog, Hawk, Lizard, Octopus, Owl, Rat, Raven, Spider e Weasel**. Il requisito per forme ulteriori è incompleto nella risposta MCP e non viene ricostruito a memoria. **La forma del famiglio di Cael non è ancora scelta.**

**Combattimento.** È un alleato del gruppo, tira la propria iniziativa e agisce nel proprio turno. **Non può attaccare**, ma può compiere altre azioni normalmente.

**Legame.** Entro **30 m / 100 ft** comunichi telepaticamente con lui. Con un'azione bonus puoi vedere e sentire attraverso i suoi sensi fino all'inizio del tuo prossimo turno, beneficiando dei suoi sensi speciali.

**Incantesimi a contatto.** Quando lanci un incantesimo a contatto, il famiglio può consegnare quel contatto se è entro 30 metri da te, usando **la propria reazione nel momento del lancio**. Per esempio può consegnare Cure Wounds; il tuo lancio continua a consumare la tua azione e lo slot previsto.

**Scomparsa.** A 0 PF scompare e serve un nuovo lancio per farlo ricomparire. Con un'azione Magia puoi congedarlo temporaneamente in una dimensione tascabile o definitivamente; se è temporaneamente congedato, un'azione Magia lo fa riapparire in uno spazio libero entro **9 m / 30 ft**. Quando scompare a 0 PF o nella dimensione tascabile lascia sul posto gli oggetti indossati o trasportati.

Puoi avere **un solo famiglio**. Rilanciare l'incantesimo mentre ne hai uno ne cambia la forma idonea, non crea un secondo aiutante. Nessun potenziamento con slot superiori è riportato. I metadati di classe e il testo di Wild Companion sono distinti nel registro: non si attribuisce un ulteriore lancio rituale gratuito non esplicitato dalla capacità.

## Armi, difese ed equipaggiamento

Le armi e protezioni seguenti sono state recuperate da **`Dnd.fetch_content`, `items-base/items-base.json`, voci XPHB**. I prezzi sono di catalogo, non spese da detrarre nuovamente dalle 12 mo iniziali.

### Attacchi rapidi di Cael

| Attacco | Tiro | Danni | Requisito o limite |
|---|---|---|---|
| Starry Wisp | **1d20 +6** | **1d8 radianti** | 1 azione, 18 m / 60 ft |
| Produce Flame | **1d20 +6** | **1d8 fuoco** | Fiamma creata con azione bonus; 1 azione Magia per attaccare, 18 m |
| Sickle — falcetto | **1d20 +2** | **1d4 taglienti** | Arma da mischia; usa FOR, non DES |
| Wooden Staff — bastone, senza Shillelagh | **1d20 +2** | **1d6 contundenti**, oppure **1d8 a due mani** | Statistiche d'arma del focus; usa FOR |
| Shortbow — arco corto | **1d20 +5** | **1d6+3 perforanti** | Due mani; frecce; gittata 24/96 m |
| Club/Quarterstaff con Shillelagh | **1d20 +6** | **1d8+4 contundenti o forza** | Solo arma idonea; non è un acquisto automatico |

I bonus fisici sono ricalcolati su FOR +0, DES +3 e competenza +2. Il falcetto non acquista Finesse perché è Light; il druido è competente nell'arco corto perché l'arma è **semplice**.

### Sickle — falcetto

**Fonte:** XPHB p. 215; proprietà Light p. 213; maestria Nick p. 214.

Arma **semplice da mischia**, **1d4 taglienti**, proprietà **Light**, peso **2 lb**, valore **1 mo**. Fa parte della dotazione del druido. Non ha Finesse: Cael usa Forza, per **+2 a colpire e 1d4 danni**.

**Light:** dopo aver attaccato con un'arma Light durante l'azione Attaccare del tuo turno, puoi effettuare un attacco aggiuntivo come azione bonus, più tardi nello stesso turno, con **un'altra arma Light**. Non aggiungi il modificatore di caratteristica ai danni dell'attacco extra, salvo sia negativo. Non basta possedere un solo falcetto per ottenere un secondo attacco con lo stesso.

Il record riporta la maestria **Nick**, ma **Cael non possiede Weapon Mastery**: l'effetto non è attivo. Nick, per chi lo può usare, sposta l'attacco extra di Light nell'azione Attaccare anziché nell'azione bonus, una volta per turno.

### Shortbow — arco corto

**Fonte:** XPHB p. 215; Ammunition p. 213; Two-Handed e Range p. 214; Vex p. 214.

Arma **semplice a distanza**, **1d6 perforanti**, gittata **80/320 ft — 24/96 m**, proprietà **Ammunition e Two-Handed**, peso **2 lb**, valore **25 mo**. Proviene dal pacchetto Guide. Cael usa Destrezza: **+5 a colpire, 1d6+3 danni**.

Occorrono **due mani quando attacchi** e una freccia per ogni attacco. Oltre 24 metri e fino a 96 metri hai svantaggio; oltre la gittata lunga non puoi attaccare. Non trattare questa configurazione come un tiro effettuato continuando a impugnare anche lo scudo.

Dopo lo scontro puoi spendere un minuto per recuperare metà delle munizioni usate, arrotondando per difetto. La maestria **Vex non è attiva per Cael**: per un utilizzatore abilitato, dopo un colpo che infligge danni dà vantaggio al successivo attacco contro quel bersaglio prima della fine del proprio prossimo turno.

### Wooden Staff — bastone usato come focus druidico

**Fonte:** XPHB p. 225, voce Wooden Staff in `items-base.json`; Versatile e Topple p. 214.

È la forma di focus già indicata dalla scheda. Il record lo identifica come **Druidic Focus** e riporta statistiche d'arma semplice: **1d6 contundenti a una mano**, **1d8 a due mani**, proprietà **Versatile**, peso **4 lb**, valore **5 mo**. Senza Shillelagh, Cael ha **+2 a colpire**, con il dado indicato e modificatore di Forza +0.

Versatile permette l'uso a una o due mani con il relativo danno. Il record include **Topple**, ma Cael non ha la capacità per usare questa maestria. Per un utilizzatore abilitato, un colpo può imporre un TS Costituzione con CD `8 + modificatore usato nell'attacco + competenza`; un fallimento rende Prone il bersaglio.

Non aggiungere un secondo bastone gratuito. Il requisito di Shillelagh è specificamente Club/Quarterstaff: va formalizzato che il focus della dotazione viene usato come Quarterstaff, non dedotto da un generico oggetto chiamato «bastone».

### Armi idonee a Shillelagh: riferimenti, non nuovi possedimenti

**Fonte:** XPHB p. 215, `items-base.json`.

| Arma | Tipo | Danno base | Proprietà | Peso | Prezzo | Maestria stampata, non attiva per Cael |
|---|---|---|---|---:|---:|---|
| Club — randello | Semplice da mischia | 1d4 contundenti | Light | 2 lb | 1 ma | Slow |
| Quarterstaff — bastone | Semplice da mischia | 1d6 contundenti; 1d8 a due mani | Versatile | 4 lb | 2 ma | Topple |

**Slow — XPHB p. 214:** per chi può usare la maestria, un colpo che infligge danni può ridurre la velocità del bersaglio di **3 m / 10 ft** fino all'inizio del proprio prossimo turno; più colpi con questa proprietà non aumentano la riduzione oltre 3 metri. Nessuno di questi benefici di maestria viene aggiunto al personaggio.

### Cuoio e scudo

**Fonte degli oggetti:** Leather Armor e Shield, XPHB p. 219. **Addestramento:** Druid, XPHB p. 78.

| Oggetto | Valore difensivo della scheda | Peso | Prezzo |
|---|---|---:|---:|
| Leather Armor — cuoio | **11 + DES 3 = CA 14** | 10 lb | 10 mo |
| Shield — scudo | **+2 alla CA**, totale 16 nella configurazione con scudo | 6 lb | 10 mo |

Il druido ha addestramento nelle armature leggere e negli scudi. Non è stata aggiunta una corazza di scaglie o equipaggiamento appartenente ad altri personaggi. Il bonus dello scudo va distinto dalla CA senza scudo, e Alert non entra in nessuno di questi calcoli.

### Strumenti

**Cartographer’s Tools — XPHB p. 220.** Peso 6 lb; prezzo 15 mo. L'uso indicato dal record è **Saggezza**, con competenza per Cael: **+6**. Puoi disegnare una mappa di una piccola area con **CD 15**; Map è l'oggetto elencato nella voce Craft. Non viene inventato un successo automatico.

**Herbalism Kit — XPHB p. 221, `Dnd.item_get`.** Peso 3 lb; prezzo 5 mo. L'uso indicato è **Intelligenza**, con competenza per Cael: **+2**. Identificare una pianta ha **CD 10**. La voce Craft elenca **Antitoxin, Candle, Healer’s Kit e Potion of Healing**; questo elenco non rende la creazione istantanea o gratuita e non fornisce, da solo, tempi e costi completi di lavorazione.

**Competenza negli strumenti — XPHB p. 220**, voce Tool in `items-base.json`: aggiungi competenza alla prova che usa lo strumento; se sei competente anche in un'abilità applicabile a quella prova, hai **vantaggio**, non un secondo bonus di competenza da sommare.

### Inventario iniziale

**Druido, pacchetto A — XPHB p. 78:** cuoio, scudo, falcetto, focus druidico, Explorer’s Pack, kit da erborista e **9 mo**. La forma di focus già indicata nel repository è il bastone.

**Guide, pacchetto A — XPHB p. 181:** arco corto, 20 frecce, faretra, strumenti da cartografo, giaciglio, tenda, abiti da viaggiatore e **3 mo**.

**Totale iniziale: 12 mo**, prima di eventuali acquisti e modifiche del DM. I prezzi elencati sopra non si sottraggono automaticamente: quegli oggetti fanno parte dei pacchetti già scelti.

**Explorer’s Pack — XPHB p. 225, `Dnd.item_get`:** zaino, giaciglio, **2 flaconi d'olio**, razioni per **10 giorni**, corda, **acciarino**, **10 torce** e otre. Il record riporta peso complessivo 55 lb e valore 10 mo. Non è necessario comprare nuovamente acciarino e torce per completare questo pacchetto.

Se si mantengono integralmente entrambi i pacchetti, il giaciglio di Guide si aggiunge a quello dello zaino: risultano **due giacigli**. La revisione non li vende o elimina automaticamente; il conteggio va convalidato nell'inventario effettivo.

| Voce di supporto | Dettaglio MCP | Riferimento |
|---|---|---|
| Arrows (20) | 20 frecce, peso 1 lb, valore 1 mo; munizioni per l'arco | XPHB p. 222, `items-base.json` |
| Quiver | Contiene fino a 20 frecce; 1 lb; 1 mo | XPHB p. 228, `item_get` |
| Tent | Ospita fino a due creature Piccole o Medie; 20 lb; 2 mo | XPHB p. 229, `item_get` |
| Torch | Brucia un'ora; luce intensa 6 m e fioca per altri 6 m; 1 lb; 1 mr | XPHB p. 229, `item_get` |

Il testo della torcia consente anche di usarla come arma semplice da mischia con l'azione Attaccare e riporta **1 danno da fuoco su un colpo**. Questa voce non viene trasformata in un'arma con danni da Shillelagh.

Per giacigli, abiti e altri componenti dello zaino non sono stati inventati effetti speciali, prezzi o pagine individuali: la loro presenza è documentata dalle voci Guide ed Explorer’s Pack.

**Oggetti narrativi preesistenti:** registro delle rotte, pergamena annerita con il disegno delle stelle, bussola guasta. Non conferiscono benefici meccanici gratuiti e la pergamena non è già una Star Map attiva al livello 2. Nessuna lanterna aggiunta come acquisto implicito.

## Concentrazione e condizioni rilevanti

### Concentration — regola standard

**Fonte:** XPHB p. 363, `Dnd.omnisearch("Concentration")`, risultato XPHB di tipo condition.

Puoi terminare la concentrazione in qualsiasi momento senza azione. La perdi **quando inizi a lanciare un altro incantesimo che la richiede** o attivi un altro effetto a concentrazione. Subendo danni, devi superare un **TS Costituzione**: la CD è **10 o metà dei danni subiti arrotondata per difetto, scegliendo il valore maggiore, fino a un massimo di 30**. Incapacitated o morte terminano la concentrazione.

Per Cael il TS ordinario è **1d20 +3**. Il **+7** e la concentrazione su più effetti sono esclusivamente la variante di campagna riportata sotto.

Fra le voci di questa scheda, **Guidance, Entangle e Faerie Fire richiedono concentrazione**. Produce Flame e Shillelagh no. Secondo il regolamento standard i tre effetti a concentrazione sono alternativi; non si può ignorare il limite perché Guidance è un trucchetto.

### Incapacitated

**Fonte:** XPHB p. 369, `Dnd.condition_search("Incapacitated")`.

Non puoi compiere **azioni, azioni bonus o reazioni**, non puoi parlare e perdi concentrazione. Se tiri l'iniziativa in questo stato hai svantaggio. Le capacità Wild Shape e, in futuro, Starry Form specificano inoltre di terminare con questa condizione; Alert non permette lo scambio di iniziativa quando uno dei due partecipanti è Incapacitated.

### Restrained — Trattenuto

**Fonte:** XPHB p. 373, `Dnd.condition_search("Restrained")`.

Velocità 0 e non aumentabile; attacchi contro la creatura con vantaggio; suoi attacchi e TS di Destrezza con svantaggio. Non equivale a perdere automaticamente azione e capacità di attaccare. Per liberarsi da **Entangle** si usa la procedura di quell'incantesimo, non una procedura di fuga inventata per ogni effetto che trattiene.

## Anteprima del livello 3: Circolo delle Stelle

> **Questa sezione non attribuisce capacità al Cael di livello 2.** È mantenuta come progetto di avanzamento già presente nel repository. Si usa la versione **XPHB 2024**, non una combinazione con TCE.

**Fonte:** `Dnd.subclassfeature_search`, classe Druid, sottoclasse Stars, livello 3; voci complete con `source`, `classSource` e `subclassSource` XPHB. **Circle of the Stars e capacità seguenti: XPHB p. 88.** L'accesso alle sottoclassi è indicato a p. 81 nella classe.

### Star Map

Crei una carta stellare come oggetto Minuscolo, utilizzabile come focus per gli incantesimi da druido. **Mentre la impugni**, hai accesso a **Guidance e Guiding Bolt** e puoi lanciare Guiding Bolt senza slot un numero di volte pari al modificatore di Saggezza, minimo una: con i punteggi attuali **quattro volte per riposo lungo**.

Se perdi la mappa, una cerimonia di un'ora crea una sostituta e distrugge la precedente; può svolgersi durante un riposo breve o lungo. Il testo consente diverse forme dell'oggetto: non occorre assegnare subito un nuovo oggetto magico alla dotazione del livello 2.

### Guiding Bolt — incantesimo futuro

**Fonte:** XPHB p. 282, `Dnd.spell_get("Guiding Bolt", source="XPHB", ruleset="2024")`.

Incantesimo di **1° livello, Invocazione — Evocation**; **un'azione**, gittata **36 m / 120 ft**, componenti **V, S**, durata indicata **un round**, nessuna concentrazione e nessun tag rituale. Bersaglia una creatura con un attacco con incantesimo a distanza: con i punteggi attuali **+6 a colpire e 4d6 radianti**.

Se colpisce, il **successivo tiro per colpire** effettuato contro il bersaglio prima della fine del tuo prossimo turno ha vantaggio. Non concede vantaggio a tutti gli attacchi per tutta la durata. Il normale lancio usa uno slot; Star Map concede i lanci senza slot sopra descritti, mentre la impugni.

**Slot superiori da verificare:** il server restituisce **+4d6 per ogni livello dello slot oltre il primo**. Il campo è conservato nel registro, non corretto con altre fonti né assunto automaticamente come progressione risolta.

### Starry Form

Con **un'azione bonus** spendi un uso di Wild Shape per assumere una forma stellare invece di trasformarti in Bestia. Conservi le statistiche; emetti luce intensa entro **3 m / 10 ft**, più luce fioca per altri 3 metri. Dura **10 minuti**; termina se la congedi, senza azione, se diventi Incapacitated o se la attivi di nuovo. La voce non richiede concentrazione.

Scegli una delle tre costellazioni quando attivi la forma:

| Forma | Effetto documentato a p. 88 |
|---|---|
| **Archer — Arciere** | Quando attivi la forma, e con un'azione bonus nei turni successivi, puoi effettuare un attacco con incantesimo a distanza contro una creatura entro **18 m / 60 ft**: **+6**, **1d8+4 radianti** con gli attuali punteggi. |
| **Chalice — Calice** | Quando lanci un incantesimo **usando uno slot** che ripristina PF a una creatura, tu o un'altra creatura entro **9 m / 30 ft** può recuperare **1d8+4 PF**. Non si elimina il requisito dello slot e non basta consumare una bacca per attivarlo. |
| **Dragon — Drago** | Per prove di **Intelligenza o Saggezza**, e per **TS Costituzione per mantenere concentrazione**, puoi trattare un risultato del d20 di 9 o meno come 10. Non si applica a tutti i TS e non rende automaticamente superata una CD 20. |

L'attacco dell'Arciere nei turni successivi e Healing Word richiedono entrambi l'azione bonus: non vanno sommati come se il personaggio ne avesse due. Il colpo durante l'attivazione dell'Arciere è invece esplicitamente incluso dalla capacità.

### Progressione prevista

Il record Druid riporta per il livello 3 **sei preparati ordinari**, **quattro slot di 1° e due di 2°**. Non vengono selezionati adesso gli incantesimi futuri. L'eventuale doppione di Guidance andrà gestito al passaggio di livello secondo le possibilità di sostituzione, senza concedere un trucchetto aggiuntivo oltre a quelli previsti.

## Regole del Dominio Oscuro: separate dal PHB

**Provenienza:** trascrizione già presente nella scheda 0.4 del repository. Fonti nominate dal documento: *Il Dominio Oscuro – Guida Ambientale* e *Prontuario Regole e Mutilazioni Dark Fantasy*. **I prontuari originali non sono stati consultati in questa revisione e le loro pagine non sono disponibili.** Le regole seguenti non sono presentate come capacità XPHB verificate dall'MCP.

| Regola della campagna | Quanto riportato nella scheda precedente |
|---|---|
| Cappa d'inchiostro | Di giorno luce fioca; luna e stelle non visibili |
| Miasma notturno | Attraversare la nebbia senza «luce viva»: ogni ora **TS COS CD 13**; fallimento: **1d6 necrotici**, un livello di Esaustione e allucinazioni |
| Risveglio dei morti | Cadaveri da cremare entro **1d12 ore**, tempo determinato segretamente dal master |
| Critici brutali | Un critico naturale a segno o la riduzione a 0 PF da danni diretti attiva un tiro **d100 di mutilazione** |
| Riposi | Breve: un'ora con riparo e razioni. Lungo: otto ore in luogo realmente sicuro; otto ore nelle terre selvagge concedono soltanto un riposo breve |
| Sforzo arcano | Possibili più incantesimi con slot nello stesso turno; dal secondo, **1d6 × livello dell'incantesimo aggiuntivo**, danni non resistibili |
| Concentrazione multipla | Più effetti ammessi; con due effetti, **CD minima 20** quando subisci danni; un fallimento interrompe tutti; bonus speciale **COS + SAG = +7** con i punteggi attuali |

**Luce viva:** Produce Flame illumina ma il suo testo dice che la fiamma in mano non produce calore. L'equivalenza fra quella luce e la protezione dal Miasma **va stabilita dal DM**. Non si assegna una protezione dalla campagna soltanto perché un effetto emette luce. Lo stesso vale per le future manifestazioni stellari.

**Economia delle azioni:** la trascrizione di Sforzo arcano non concede espressamente azioni o azioni bonus aggiuntive. Non usarla per attribuirle automaticamente. Per il limite standard degli incantesimi con slot nello stesso turno non è stata recuperata una voce precisa attraverso la ricerca effettuata: non viene inventata una pagina di riferimento.

## Storia e personalità

Cael era il misuratore delle distanze tra i bracieri: contava passi, annotava sentieri che il Miasma cancellava, verificava che le carovane avessero legna sufficiente. La sua insegnante gli lasciò una carta stellare disegnata prima che il cielo diventasse nero.

Una notte guidò dodici persone attraverso un valico apparentemente sicuro; ne tornarono quattro. Non parla delle otto scomparse, ma disegna ogni notte la loro ultima posizione sulla carta. Non sa se la mappa sia una reliquia autentica, un falso o una trappola.

Per lui le stelle non sono divinità. Sono **coordinate**. Dimostrare che esistono significa dimostrare che il confine si può attraversare.

**Personalità:** curioso, metodico, ironia nera; pretende sempre un piano di fuga, diffida delle autorità ma non abbandona un compagno.

**Difetto:** a volte è disposto a rischiare troppo pur di verificare un indizio sul cielo.

**Segreto da usare col DM:** una delle otto persone scomparse aveva annotato una costellazione **impossibile** sul retro della mappa. Il suo nome è stato cancellato.

**Frase tipica:** «Non serve credere alle stelle. Serve sapere dove puntare.»

## Questioni ancora aperte

| Punto | Stato dopo la revisione |
|---|---|
| Livello, punteggi e cinque preparati | Conservati: livello 2, 10/16/17/10/18/10, Faerie Fire quinto preparato |
| Punti ferita | **19 con valore fisso**, criterio da confermare col DM; nessun tiro inventato |
| Trucchetto di Magician | Guidance resta proposto; serve una scelta esplicita |
| Wild Shape | Annotare le quattro forme effettivamente conosciute |
| Famiglio | Scegliere la forma; non ricostruire il requisito troncato per ulteriori Bestie |
| Bastone/focus | Formalizzare l'uso come Quarterstaff per Shillelagh; nessuna arma duplicata automaticamente |
| Inventario | Verificare i due giacigli derivanti dai pacchetti e le risorse effettivamente consumate in sessione |
| Lingue ulteriori | Ancora da definire con il DM |
| Dati MCP | Gittata di Goodberry e progressioni di Thunderwave/Guiding Bolt documentate come da verificare |
| Regole di campagna | Pagine dei prontuari non disponibili; «luce viva» e altri adattamenti da confermare con il master |

Per la copertura completa delle fonti, i campi restituiti e le correzioni rispetto alla versione precedente: **[registro della verifica MCP](mcp-verifica-2026-10-09.md)**. La scheda di livello 1 resta un documento storico separato.
