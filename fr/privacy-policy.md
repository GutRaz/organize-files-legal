> **Traduction fournie par commodité.** Le [CLUF en anglais](../en/eula.md) et la [Politique de confidentialité en anglais](../en/privacy-policy.md) sont les versions de référence. Lorsque le droit impératif de la consommation de votre pays donne la priorité à la version dans votre propre langue, cette version s'applique. Pas un conseil juridique — consultez un avocat qualifié dans votre juridiction.

---

# Politique de confidentialité — Organize Files

**Éditeur :** Guțulov Răzvan Constantin PFA  
**Adresse enregistrée:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Registre du commerce:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Numéro d'identification fiscale:** 53610310  
**Contact :** razvan.gutulov@outlook.com  
**Date d'effet :** 2026-05-28  
**URL publique :** `https://github.com/GutRaz/organize-files-legal/blob/main/fr/privacy-policy.md`

---

## Résumé

Organize Files traite les fichiers **localement sur votre appareil**. Le contenu n'est **pas** envoyé à l'éditeur pour les opérations d'organisation ou de réparation habituelles. L'application **écrit des fichiers locaux** (instantanés de session, état de reprise, journaux optionnels) comme décrit ci-dessous.

## Responsable du traitement et contact

Pour les données personnelles traitées par l'éditeur, le responsable du traitement est **Guțulov Răzvan Constantin PFA**. Contact : **razvan.gutulov@outlook.com**.

## Données traitées localement

| Donnée | Où c'est stocké | Finalité |
|--------|-----------------|----------|
| Fichiers et dossiers que vous choisissez | Uniquement sur votre appareil | Organiser, trouver les doublons, réparer et supprimer si choisi |
| Instantané UI (`last-ui-session.json`) | Le dossier `sessions\<id>\` du dossier de profil de l'application : `%LocalAppData%\OrganizeFilesCrossPlatform` sous Windows, `~/Library/Application Support/OrganizeFilesCrossPlatform` sous macOS, `~/.local/share/OrganizeFilesCrossPlatform` sous Linux, ou le stockage privé de l'application sous Android et iOS | Restaurer l'espace de travail |
| État de reprise d'une organisation + journal de déplacements facultatif | `_OrganizeMediaLogs` dans le dossier de sortie, ou le dossier de session | Ignorer les déplacements déjà faits, données de récupération avec chemins encodés |
| Fichier de progression facultatif d'une exécution, JSON | `_OrganizeMediaLogs` dans le dossier de sortie | Compteurs de progression pour d'autres programmes |
| État de l'essai et de la licence | Dossier de profil de l'application | Appliquer l'essai ou l'achat en boutique |
| État de la vérification des mises à jour | Dossier de profil de l'application | Limiter la fréquence de la vérification de version facultative |
| Android : copies des dossiers choisis avec le sélecteur du système, SAF | Dossier de session dans le stockage de l'application | Copie des arborescences `content://` pour que le moteur puisse les lire |
| Mot de passe SMTP des notifications e-mail (optionnel) | Chiffré au repos dans les préférences de session sur l’appareil (AES-GCM avec fichier de clé par profil). Lors d’une mise à niveau, une migration unique réécrit tout mot de passe SMTP hérité stocké sans AES-GCM vers AES-GCM lorsque ce champ est présent |  Uniquement si vous activez les notifications e-mail et saisissez des identifiants SMTP. Le fichier de clé AES-GCM reste dans le dossier du profil de l'application et est lisible par le compte utilisateur du système d'exploitation connecté. Il protège les lectures occasionnelles des préférences JSON, et non un coffre-fort matériel. |

## Ce que l'éditeur ne reçoit pas par défaut

- Contenu des fichiers lors des runs organize/repair  
- Contacts, localisation, micro ou caméra (non utilisés)  
- Données analytiques ou publicitaires (aucun SDK de ce type n'est inclus dans l'application)  
- Mots de passe SMTP que vous stockez localement (restent sur l’appareil, sauf envoi via votre serveur SMTP)  

## Usage réseau optionnel

| Activité | Données envoyées | Destinataire |
|----------|------------------|--------------|
| Vérif. mise à jour optionnelle | GET HTTPS vers un manifeste de version. L'hôte (ex. GitHub) reçoit l'IP, le User-Agent `OrganizeFiles-UpdateCheck/1.0` et des métadonnées TLS. Aucun chemin ni contenu de fichier. Désactivation : `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Hôte du JSON |
| Achat store / licence | API facturation plateforme | Microsoft, Google ou Apple |
| Serveur de licence optionnel (configuré par l'opérateur) | Un identifiant d'installation persistant aléatoire (GUID dans `license_installation_id.txt`) est envoyé à un serveur de licence opéré par l'éditeur ou configuré par l'opérateur à `ORGANIZE_FILES_LICENSE_SERVER_URL`. Cet identifiant est un identifiant d'appareil au sens du considérant 30 du RGPD. Base légale : exécution du contrat. Conservation côté éditeur : enregistrements d'entitlement pendant la période active plus jusqu'à 24 mois après expiration/révocation (prévention des abus et litiges) ; documents comptables pouvant être conservés jusqu'à 7 ans lorsque la loi l'exige. Les serveurs opérés par un opérateur suivent le calendrier de conservation documenté de l'opérateur. Inactif sauf si `ORGANIZE_FILES_LICENSE_SERVER_URL` est défini. | Serveur de licence éditeur ou opérateur |
| Traçage OpenTelemetry optionnel (configuré par l'opérateur) | Lorsque `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` est défini, les métadonnées des jobs d'automatisation (IDs de job, IDs de corrélation, balises de type de cible, contexte de trace W3C) sont exportées vers le collecteur OTLP configuré. Aucun chemin ni contenu de fichier. Inactif par défaut ; configuration explicite de l'opérateur requise. | Collecteur OTLP configuré par l'opérateur |
| Notifications par e-mail optionnelles (lorsqu'elles sont activées) | État d'exécution et extraits de journal (pouvant inclure des chemins de fichiers) envoyés via le serveur SMTP configuré par l'opérateur | SMTP / fournisseur de messagerie de l'opérateur |
| Webhooks d'automatisation facultatifs (configurés par l'opérateur) | Lorsque `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` est défini, des événements du cycle de vie des tâches avec des identifiants de corrélation et les chemins des fichiers d'état de l'automatisation | Point de terminaison webhook configuré par l'opérateur |
| Vérification d'identité facultative pour l'approbation d'exécution (configurée par l'opérateur) | Si `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` est défini, un GET HTTPS récupère les clés de signature et les met en cache une heure ; aucun jeton ne quitte l'appareil. Si `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` est défini, le jeton porteur de l'opérateur lui-même est envoyé à ce point de terminaison pour validation (RFC 7662), avec des identifiants client HTTP Basic le cas échéant. Inactif tant qu'aucune de ces URL n'est définie. | Fournisseur d'identité configuré par l'opérateur |
| Assistants de nouvelle tentative NAS du moteur | Rien en dehors des chemins réseau configurés | Hôte NAS / SMB |

Les checks comparent **uniquement des métadonnées de version** — pas chemins ni contenus.

## Bases légales (cadre RGPD, pas un avis juridique)

| Traitement | Base typique |
|------------|--------------|
| Organisation/réparation locale sur dossiers déjà sélectionnés | Exécution du contrat / intérêt légitime de l'opérateur |
| Fichiers locaux de session, de reprise et de progression | Même base, nécessaires pour fournir l'outil |
| Facturation Store et droits | Contrat avec la plateforme store |
| Vérification optionnelle du manifeste de mise à jour | Intérêt légitime (mises à jour de sécurité) ; désactivable via variable d'environnement |
| E-mail de support | Intérêt légitime / démarches précontractuelles à votre demande |
| Serveur de licence / OpenTelemetry optionnels | Exécution du contrat ou intérêt légitime de l'opérateur ; uniquement si configurés explicitement |

## Transferts internationaux

Les vérifications de mise à jour optionnelles peuvent atteindre des serveurs situés hors de l'Espace économique européen (par exemple GitHub aux États-Unis). La facturation Store relève des conditions de chaque plateforme.

## Autorité de contrôle et réclamations

Si le droit applicable ouvre des droits pour les personnes concernées ou une réclamation auprès d'une autorité de contrôle, contactez d'abord l'éditeur à **razvan.gutulov@outlook.com**. Les résidents de l'UE ou de l'EEE peuvent également déposer une réclamation auprès de leur autorité locale de protection des données (pour la Roumanie : ANSPDCP, https://www.dataprotection.ro).

## Sous-traitants (si vous utilisez)

- **Microsoft Store / Google Play / Mac App Store** — facturation et droits. Google Play valide les achats sur l'appareil.  
- **GitHub (ou hôte manifeste)** — JSON version HTTPS optionnel  
- **Client e-mail** — contact via lien mailto  

## Vos responsabilités (cadre RGPD)

Des données personnelles peuvent exister **dans vos fichiers**. Si vous les traitez, vous (ou votre organisation) pouvez être **responsable du traitement** et devez choisir une base légale, minimiser la conservation et répondre aux demandes.

## Conservation

Les fichiers locaux restent jusqu'à suppression, effacement des données app, désinstallation ou écrasement des dossiers de sortie. L'éditeur n'exploite pas de calendrier central pour les données purement locales.

Pour les données détenues par l'éditeur :

- E-mail de support et correspondance : jusqu'à 24 mois après le dernier contact utile, sauf litige ou obligation légale exigeant une conservation plus longue.
- Achats directs, remboursements, fiscalité et comptabilité : jusqu'à 7 ans lorsque la loi fiscale ou comptable l'exige.
- Enregistrements d'entitlement d'un serveur de licence opéré par l'éditeur : pendant la période active plus jusqu'à 24 mois après expiration ou révocation.
- Journaux d'accès/sécurité d'un serveur opéré par l'éditeur : jusqu'à 90 jours, sauf besoin plus long pour enquête de sécurité, prévention de la fraude ou réclamations juridiques.

## Vos droits

Pour les données détenues par l'éditeur (ex. e-mail support) : **razvan.gutulov@outlook.com**. Le cas échéant, vous pouvez demander l'accès, la rectification, l'effacement, la limitation, l'opposition, la portabilité ou le retrait du consentement. L'éditeur vise à répondre aux demandes des personnes concernées dans un délai de **30 jours** après une demande vérifiée (une vérification d'identité peut être demandée si cela est raisonnablement nécessaire). Pour les données uniquement locales : **Effacer les données**, désinstallation ou suppression manuelle. **Effacer les données** supprime sessions, journaux et brouillons d'automatisation, mais peut conserver l'état local d'entitlement et un identifiant d'installation utilisé pour les contrôles de licence optionnels — voir le texte de confirmation in-app avant de continuer.

## Enfants

Outil de productivité général, non destiné aux enfants de moins de 13 ans (ou l'âge requis localement).

## Modifications

Les changements importants doivent apparaître dans les fiches store et la documentation in-app avant release.

## Documents connexes

- [CLUF (anglais)](../en/eula.md)  
- [CLUF (français)](./eula.md)  
- [Confidentialité (anglais)](../en/privacy-policy.md)  
- [Confidentialité (roumain)](../ro/privacy-policy.md)  
- [Confidentialité (allemand)](../de/privacy-policy.md)
