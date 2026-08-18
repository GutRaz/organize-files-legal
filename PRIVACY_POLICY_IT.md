> **Traduzione automatica non ufficiale: non consulenza legale.** L'[EULA inglese](./EULA_EN.md) e l'[Informativa sulla privacy inglese](./PRIVACY_POLICY_EN.md) regolano se questa traduzione è in conflitto con essi. Consulta un consulente qualificato nella tua giurisdizione.

---

# Informativa sulla privacy: organizza i file

**Editore:** Razvan Constantin Gutulov  
**Contatto:** razvan.gutulov@outlook.com  
**Data di entrata in vigore:** 28-05-2026  
**URL pubblico:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_IT.md`

---

## Riepilogo

Organizza file elabora i file **localmente sul dispositivo**. I contenuti dei file **non vengono caricati sui server dell'editore** per le normali operazioni di organizzazione o riparazione. L'app **scrive file locali** sul dispositivo (istantanee della sessione, stato di ripresa, registri facoltativi) come descritto di seguito.

## Titolare del trattamento e contatto

Per i dati personali trattati dall'editore, il titolare del trattamento è **Razvan Constantin Gutulov**. Contatto: **razvan.gutulov@outlook.com**.

## Dati elaborati localmente

| Dati | Dove conservato | Scopo |
|------|----------------|---------|
| File e cartelle selezionati | Solo il tuo dispositivo | Organizza, deduplica, ripara, elimina facoltativamente |
| Istantanea della sessione dell'interfaccia utente (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) o archiviazione privata dell'app (Android) | Ripristina l'area di lavoro: percorsi, estensioni, opzioni |
| Organizza curriculum + diario di spostamento opzionale | Output `_OrganizeMediaLogs` o cartella della sessione | Salta le mosse completate; metadati di ripristino (percorsi codificati) |
| Esegui heartbeat JSON facoltativo | Output `_OrganizeMediaLogs` | Contatori di avanzamento per strumenti esterni |
| Stato di prova/licenza | Cartella del profilo in Dati app locali | Applicare la prova o il diritto di archiviazione |
| Stato di controllo aggiornamento | Cartella profilo | Limita i controlli facoltativi del manifest della versione |
| Stadiazione Android SAF | Cartella della sessione nella memoria dell'app | Copia gli alberi `content://` in modo che il motore possa leggerli |
| Password SMTP opzionale per notifiche e-mail | Salvata cifrata nelle preferenze di sessione sul dispositivo (AES-GCM con file chiave per profilo). In fase di aggiornamento, se il campo è presente, qualsiasi password SMTP legacy salvata senza AES-GCM viene riscritta una sola volta in AES-GCM. Il file chiave AES-GCM resta nella cartella profilo dell’app ed è leggibile dall’account OS connesso; protegge letture casuali del JSON delle preferenze, non è un vault hardware. | Solo se abiliti le notifiche e-mail e inserisci credenziali SMTP |

## Ciò che l'editore non riceve per impostazione predefinita

- Contenuti dei file dalle corse di organizzazione/riparazione  
- Contatti, posizione, microfono o fotocamera (non utilizzati)  
- SDK di Analytics raggruppati nell'albero open source  

## Utilizzo della rete opzionale

| Attività | Dati inviati | Destinatario |
|----------|-----------|-----------|
| Controllo aggiornamento opzionale | HTTPS GET a un manifest della versione. L'host (ad esempio GitHub) riceve l'indirizzo IP della richiesta, l'agente utente "OrganizeFiles-UpdateCheck/1.0" e i metadati TLS. Non vengono inviati percorsi di file o contenuti di file. Disabilita con "ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1". | Host che serve il manifest JSON |
| Acquisto/licenza in negozio | API di fatturazione della piattaforma | Microsoft, Google o Apple (per canale) |
| Server licenze opzionale (configurato dall'operatore) | Un ID di installazione persistente casuale (GUID memorizzato in `license_installation_id.txt`) viene inviato a un server di licenza gestito dall'editore o configurato dall'operatore in "ORGANIZE_FILES_LICENSE_SERVER_URL". L'ID di installazione è un identificatore del dispositivo ai sensi del considerando 30 del GDPR. Base giuridica: esecuzione del contratto. Conservazione gestita dall'editore: registri di entitlement mentre attivi più fino a 24 mesi dopo scadenza/revoca per prevenzione abusi e gestione controversie; i registri contabili possono essere conservati fino a 7 anni ove richiesto dalla legge. I server gestiti dall'operatore seguono il calendario di conservazione documentato dall'operatore. Questa funzione è inattiva a meno che non sia impostato `ORGANIZE_FILES_LICENSE_SERVER_URL`. | Server di licenza editore o operatore |
| Tracciamento OpenTelemetry opzionale (configurato dall'operatore) | Quando è impostato "ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT", i metadati del lavoro di automazione (ID lavoro, ID di correlazione, tag del tipo di destinazione, contesto di traccia W3C) vengono esportati nel raccoglitore OTLP configurato. Non sono inclusi percorsi o contenuti di file. Questa funzionalità è inattiva per impostazione predefinita e richiede una configurazione esplicita da parte dell'operatore. | Raccoglitore OTLP configurato dall'operatore |
| Notifiche e-mail opzionali (se abilitate) | Stato dell'esecuzione ed estratti di log (possono includere percorsi di file) inviati tramite il server SMTP configurato dall'operatore | SMTP / provider di posta dell'operatore |
| Assistenti tentativi NAS motore | Nessuno oltre i percorsi di rete configurati | Host NAS/PMI |

I controlli degli aggiornamenti confrontano **solo i metadati della versione**. L'app desktop può eseguire questo controllo una volta al giorno dopo l'accettazione dell'EULA, a meno che non sia disabilitato.

## Basi giuridiche (inquadramento in stile GDPR, non consulenza legale)

| Elaborazione | Base tipica |
|------------|----------------|
| Organizza/ripara locale su cartelle già selezionate | Esecuzione del contratto/interesse legittimo dell'operatore |
| File di sessione locale, curriculum e heartbeat | Idem: necessario per fornire lo strumento |
| Fatturazione e diritto del negozio | Contratto con il negozio della piattaforma |
| Controllo facoltativo del manifesto di aggiornamento | Interesse legittimo negli aggiornamenti di sicurezza; può essere disabilitato tramite la variabile d'ambiente |
| E-mail di supporto | Legittimo interesse/fasi precontrattuali su vostra richiesta |

## Trasferimenti internazionali

I controlli facoltativi degli aggiornamenti potrebbero raggiungere server al di fuori dello Spazio Economico Europeo (ad esempio GitHub negli Stati Uniti). La fatturazione del negozio viene gestita in base ai termini di ciascuna piattaforma.

## Autorità di controllo e reclami

Se la legge applicabile garantisce i diritti dell'interessato o un reclamo a un'autorità di controllo, contattare prima l'editore all'indirizzo **razvan.gutulov@outlook.com**. I residenti nell'UE/SEE possono anche presentare un reclamo all'autorità locale per la protezione dei dati (per la Romania: ANSPDCP, https://www.dataprotection.ro).

## Processori di terze parti (quando vengono utilizzate queste funzionalità)

- **Microsoft Store/Google Play/Mac App Store**: fatturazione e diritti. Google Play utilizza la fatturazione sul dispositivo; gli elenchi di produzione dovrebbero aggiungere l'integrità di Play e/o la verifica lato server in base alle norme di Google.
- **GitHub (o l'host manifest)**: versione opzionale JSON su HTTPS (può includere l'IP del client nei log del server)
- **Client di posta elettronica**: quando si contatta l'assistenza tramite il collegamento mailto

## Responsabilità dell'operatore (inquadramento in stile GDPR)

I dati personali potrebbero esistere **all'interno** dei tuoi file. Se tratti tali dati, tu (o la tua organizzazione) potreste essere un **responsabile del trattamento dei dati** e dovete scegliere una base legale, ridurre al minimo la conservazione e rispondere alle richieste dell'interessato.

## Conservazione

I file locali rimangono finché non li elimini, cancelli i dati dell'app, disinstalli l'app o sovrascrivi le cartelle di output. L'editore non gestisce un programma di conservazione centrale per i dati solo locali.

Per i dati detenuti dall'editore:

- E-mail di supporto e corrispondenza: fino a 24 mesi dall'ultimo contatto rilevante, salvo controversia o obbligo di legge che richieda più tempo.
- Acquisti diretti, rimborsi, fisco e contabilità: fino a 7 anni ove richiesto dalla legge fiscale o contabile.
- Registri di entitlement di un server di licenze gestito dall'editore: mentre sono attivi più fino a 24 mesi dopo scadenza o revoca.
- Registri di accesso/sicurezza di un server gestito dall'editore: fino a 90 giorni, salvo necessità maggiore per indagini di sicurezza, frodi o rivendicazioni.

## I tuoi diritti

Per i dati conservati dall'editore (ad esempio corrispondenza e-mail di supporto), contattare **razvan.gutulov@outlook.com**. Ove applicabile, puoi richiedere accesso, rettifica, cancellazione, limitazione, opposizione, portabilità o revoca del consenso. L'editore mira a rispondere alle richieste verificate entro **30 giorni** (può essere richiesta la verifica dell'identità se ragionevolmente necessario). Per i dati archiviati solo sul tuo dispositivo, puoi eliminare la maggior parte dei dati delle app tramite **Cancella dati app**, disinstallazione o eliminazione manuale dei file. **Cancella dati app** rimuove sessioni, registri e bozze di automazione, ma potrebbe conservare ancoraggi di prova della licenza, indicatori di installazione a pagamento e un identificatore di installazione anonimo utilizzato per controlli di licenza opzionali: consulta il testo di conferma in-app prima di procedere.

## Bambini

Strumento di produttività generale non rivolto ai bambini di età inferiore a 13 anni (o all'età richiesta nella tua giurisdizione).

## Modifiche

Le modifiche sostanziali dovrebbero essere visualizzate nelle schede dello Store e nella documentazione in-app prima del rilascio.

## Documenti correlati

- [EULA (inglese)](./EULA_EN.md)  
- [Informativa sulla privacy (rumeno)](./PRIVACY_POLICY_RO.md)  
- [Informativa sulla privacy (tedesco)](./PRIVACY_POLICY_DE.md)  
- [Informativa sulla privacy (francese)](./PRIVACY_POLICY_FR.md)
