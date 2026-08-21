> **Traduction automatique non officielle — pas de conseil juridique.** Le [CLUF en anglais](./EULA_EN.md) et la [Politique de confidentialité en anglais](./PRIVACY_POLICY_EN.md) prévalent en cas de conflit avec cette traduction. Consultez un conseil qualifié dans votre juridiction.

---

# Politique de confidentialité — Organize Files

**Éditeur :** Razvan Constantin Gutulov  
**Contact :** razvan.gutulov@outlook.com  
**Date d'effet :** 2026-05-28  
**URL publique :** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_FR.md`

---

## Résumé

Organize Files traite les fichiers **localement sur votre appareil**. Le contenu n'est **pas** envoyé à l'éditeur pour les opérations d'organisation ou de réparation habituelles. L'application **écrit des fichiers locaux** (instantanés de session, état de reprise, journaux optionnels) comme décrit ci-dessous.

## Responsable du traitement et contact

Pour les données personnelles traitées par l'éditeur, le responsable du traitement est **Razvan Constantin Gutulov**. Contact : **razvan.gutulov@outlook.com**.

## Données traitées localement

| Donnée | Où c'est stocké | Finalité |
|--------|-----------------|----------|
| Fichiers et dossiers sélectionnés | Uniquement votre appareil | Organiser, dédupliquer, réparer, supprimer (option) |
| Instantané UI (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (bureau) ou stockage app (Android) | Restaurer l'espace de travail |
| Reprise organize + journal optionnel | Output `_OrganizeMediaLogs` ou dossier session | Ignorer les déplacements déjà faits |
| Heartbeat JSON optionnel | Output `_OrganizeMediaLogs` | Compteurs pour outils externes |
| État essai / licence | Profil Local App Data | Essai ou droit store |
| État vérif. mise à jour | Profil | Limiter les checks manifeste |
| Staging SAF Android | Dossier session | Copier les arbres `content://` pour le moteur |
| Mot de passe SMTP des notifications e-mail (optionnel) | Chiffré au repos dans les préférences de session sur l’appareil (AES-GCM avec fichier de clé par profil). Lors d’une mise à niveau, une migration unique réécrit tout mot de passe SMTP hérité stocké sans AES-GCM vers AES-GCM lorsque ce champ est présent |  Uniquement si vous activez les notifications e-mail et saisissez des identifiants SMTP. Le fichier de clé AES-GCM reste dans le dossier du profil de l'application et est lisible par le compte utilisateur du système d'exploitation connecté. Il protège les lectures occasionnelles des préférences JSON, et non un coffre-fort matériel. |

## Ce que l'éditeur ne reçoit pas par défaut

- Contenu des fichiers lors des runs organize/repair  
- Contacts, localisation, micro ou caméra (non utilisés)  
- SDK analytics dans l'arborescence open source  
- Mots de passe SMTP que vous stockez localement (restent sur l’appareil, sauf envoi via votre serveur SMTP)  

## Usage réseau optionnel

| Activité | Données envoyées | Destinataire |
|----------|------------------|--------------|
| Vérif. mise à jour optionnelle | GET HTTPS vers un manifeste de version. L'hôte (ex. GitHub) reçoit l'IP, le User-Agent `OrganizeFiles-UpdateCheck/1.0` et des métadonnées TLS. Aucun chemin ni contenu de fichier. Désactivation : `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Hôte du JSON |
| Achat store / licence | API facturation plateforme | Microsoft, Google ou Apple |
| Serveur de licence optionnel (configuré par l'opérateur) | Un identifiant d'installation persistant aléatoire (GUID dans `license_installation_id.txt`) est envoyé à un serveur de licence opéré par l'éditeur ou configuré par l'opérateur à `ORGANIZE_FILES_LICENSE_SERVER_URL`. Cet identifiant est un identifiant d'appareil au sens du considérant 30 du RGPD. Base légale : exécution du contrat. Conservation côté éditeur : enregistrements d'entitlement pendant la période active plus jusqu'à 24 mois après expiration/révocation (prévention des abus et litiges) ; documents comptables pouvant être conservés jusqu'à 7 ans lorsque la loi l'exige. Les serveurs opérés par un opérateur suivent le calendrier de conservation documenté de l'opérateur. Inactif sauf si `ORGANIZE_FILES_LICENSE_SERVER_URL` est défini. | Serveur de licence éditeur ou opérateur |
| Traçage OpenTelemetry optionnel (configuré par l'opérateur) | Lorsque `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` est défini, les métadonnées des jobs d'automatisation (IDs de job, IDs de corrélation, balises de type de cible, contexte de trace W3C) sont exportées vers le collecteur OTLP configuré. Aucun chemin ni contenu de fichier. Inactif par défaut ; configuration explicite de l'opérateur requise. | Collecteur OTLP configuré par l'opérateur |
| Notifications par e-mail optionnelles (lorsqu'elles sont activées) | État d'exécution et extraits de journal (pouvant inclure des chemins de fichiers) envoyés via le serveur SMTP configuré par l'opérateur | SMTP / fournisseur de messagerie de l'opérateur |

Les checks comparent **uniquement des métadonnées de version** — pas chemins ni contenus.

## Google Play

Les achats in-app utilisent **Google Play Billing sur l'appareil**. Le client open source valide localement. Les fiches **production** Play devraient ajouter **Play Integrity** et/ou **validation serveur** ; ce traitement est configuré par l'éditeur, pas activé par défaut dans ce dépôt.

## Bases légales (cadre RGPD, pas un avis juridique)

| Traitement | Base typique |
|------------|--------------|
| Organisation/réparation locale sur dossiers déjà sélectionnés | Exécution du contrat / intérêt légitime de l'opérateur |
| Fichiers locaux de session, reprise et heartbeat | Même base — nécessaires pour fournir l'outil |
| Facturation Store et droits | Contrat avec la plateforme store |
| Vérification optionnelle du manifeste de mise à jour | Intérêt légitime (mises à jour de sécurité) ; désactivable via variable d'environnement |
| E-mail de support | Intérêt légitime / démarches précontractuelles à votre demande |
| Serveur de licence / OpenTelemetry optionnels | Exécution du contrat ou intérêt légitime de l'opérateur ; uniquement si configurés explicitement |

## Sous-traitants (si vous utilisez)

- **Microsoft Store / Google Play / Mac App Store** — facturation et droits  
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

- [CLUF (anglais)](./EULA_EN.md)  
- [CLUF (français)](./EULA_FR.md)  
- [Confidentialité (anglais)](./PRIVACY_POLICY_EN.md)  
- [Confidentialité (roumain)](./PRIVACY_POLICY_RO.md)  
- [Confidentialité (allemand)](./PRIVACY_POLICY_DE.md)
