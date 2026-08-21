> **Tradução automática não oficial - não aconselhamento jurídico.** O [EULA em inglês](./EULA_EN.md) e a [Política de privacidade em inglês](./PRIVACY_POLICY_EN.md) regem se esta tradução entrar em conflito com eles. Consulte um advogado qualificado em sua jurisdição.

---

# Política de Privacidade — Organizar Arquivos

**Editor:** Guțulov Răzvan Constantin PFA  
**Endereço registado:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Registo comercial:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Número de identificação fiscal:** 53610310  
**Contato:** razvan.gutulov@outlook.com  
**Data de vigência:** 28/05/2026  
**URL público:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_PT.md`

---

## Resumo

Organizar Arquivos processa arquivos **localmente no dispositivo**. O conteúdo dos arquivos **não é carregado nos próprios servidores do editor** para operações normais de organização ou reparo. O aplicativo **grava arquivos locais** no dispositivo (instantâneos da sessão, estado de retomada, logs opcionais) conforme descrito abaixo.

## Dados processados localmente

| Dados | Onde armazenado | Finalidade |
|------|----------------|--------|
| Arquivos e pastas que você seleciona | Somente seu dispositivo | Organizar, desduplicar, reparar, excluir opcionalmente |
| Instantâneo da sessão da IU (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) ou armazenamento privado do aplicativo (Android) | Restaurar espaço de trabalho: caminhos, extensões, opções |
| Organizar currículo + diário de movimentação opcional | Saída `_OrganizeMediaLogs` ou pasta de sessão | Pular movimentos concluídos; metadados de recuperação (caminhos codificados) |
| Opcional executar pulsação JSON | Saída `_OrganizeMediaLogs` | Contadores de progresso para ferramentas externas |
| Estado de teste/licença | Pasta de perfil em Dados de aplicativos locais | Aplicar o direito de teste ou armazenar |
| Estado de verificação de atualização | Pasta de perfil | Acelerar verificações opcionais de manifesto de versão |
| Preparação Android SAF | Pasta de sessão no armazenamento do aplicativo | Copie as árvores `content://` para que o mecanismo possa lê-las |
| Senha SMTP opcional para notificações por e-mail | Armazenada criptografada nas preferências de sessão no dispositivo (AES-GCM com arquivo de chave por perfil). Na atualização, se o campo existir, qualquer senha SMTP antiga salva sem AES-GCM é regravada uma vez em AES-GCM. O arquivo de chave AES-GCM permanece na pasta de perfil do aplicativo e pode ser lido pela conta de usuário do OS conectada; protege leituras casuais do JSON de preferências, não é cofre de hardware. | Somente se você ativar notificações por e-mail e inserir credenciais SMTP |

## O que o editor não recebe por padrão

- Conteúdo do arquivo de execuções de organização/reparo  
- Contatos, localização, microfone ou câmera (não usado)  
- SDKs do Analytics agrupados na árvore de código aberto  

## Uso de rede opcional

| Atividade | Dados enviados | Destinatário |
|----------|-----------|-----------|
| Verificação de atualização opcional | HTTPS GET para um manifesto de versão. O host (por exemplo GitHub) recebe o endereço IP da solicitação, o agente do usuário `OrganizeFiles-UpdateCheck/1.0` e os metadados TLS. Nenhum caminho de arquivo ou conteúdo de arquivo é enviado. Desative com `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host que atende o manifesto JSON |
| Compra/licença na loja | APIs de faturamento de plataforma | Microsoft, Google ou Apple (por canal) |
| Servidor de licença opcional (configurado pelo operador) | Um ID de instalação persistente aleatório (GUID armazenado em `license_installation_id.txt`) é enviado para um servidor de licença operado pelo editor ou configurado pelo operador em `ORGANIZE_FILES_LICENSE_SERVER_URL`. O ID de instalação é um identificador de dispositivo de acordo com o Considerando 30 do GDPR. Base legal: execução do contrato. Retenção operada pelo editor: registos de entitlement enquanto ativos mais até 24 meses após expiração/revogação para prevenção de abuso e litígios; registos contabilísticos podem ser retidos até 7 anos quando a lei o exigir. Servidores geridos pelo operador seguem o calendário de retenção documentado do operador. Este recurso está inativo a menos que `ORGANIZE_FILES_LICENSE_SERVER_URL` esteja definido. | Servidor de licença de editor ou operador |
| Rastreamento OpenTelemetry opcional (configurado pelo operador) | Quando `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` é definido, os metadados do trabalho de automação (IDs de trabalho, IDs de correlação, tags de tipo de destino, contexto de rastreamento W3C) são exportados para o coletor OTLP configurado. Nenhum caminho de arquivo ou conteúdo de arquivo está incluído. Este recurso está inativo por padrão e requer configuração explícita do operador. | Coletor OTLP configurado pelo operador |
| Notificações por e-mail opcionais (quando ativadas) | Estado da execução e trechos de log (podem incluir caminhos de ficheiros) enviados através do servidor SMTP configurado pelo operador | SMTP / fornecedor de e-mail do operador |
| Webhooks de automação opcionais (configurados pelo operador) | Quando `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` está definido, eventos do ciclo de vida das tarefas com identificadores de correlação e os caminhos dos ficheiros de estado da automação | Ponto final de webhook configurado pelo operador |
| Auxiliares de nova tentativa do Engine NAS | Nenhum além dos caminhos de rede configurados | Anfitrião NAS/SMB |

As verificações de atualização comparam **somente metadados de versão**. O aplicativo de desktop pode executar essa verificação uma vez por dia após a aceitação do EULA, a menos que esteja desativado.

## Bases jurídicas (enquadramento no estilo GDPR, não aconselhamento jurídico)

| Processamento | Base típica |
|------------|----------------|
| Organização/reparo local em pastas já selecionadas | Execução do contrato/interesse legítimo do operador |
| Arquivos de sessão local, currículo e pulsação | Mesmo — necessário para fornecer a ferramenta |
| Faturamento e direitos da loja | Contrato com a loja da plataforma |
| Verificação opcional do manifesto de atualização | Interesse legítimo em atualizações de segurança; pode ser desabilitado via variável de ambiente |
| E-mail de suporte | Interesse legítimo / diligências pré-contratuais a seu pedido |

## Transferências internacionais

As verificações opcionais de atualização podem chegar a servidores fora do Espaço Económico Europeu (por exemplo, GitHub nos Estados Unidos). O faturamento da loja é feito de acordo com os termos de cada plataforma.

## Autoridade supervisora e reclamações

Se a lei aplicável conceder direitos ao titular dos dados ou uma reclamação a uma autoridade supervisora, entre em contato primeiro com o editor em **razvan.gutulov@outlook.com**. Os residentes da UE/EEE também podem apresentar uma reclamação junto da autoridade local de proteção de dados (para a Roménia: ANSPDCP, https://www.dataprotection.ro).

## Processadores de terceiros (quando esses recursos são usados)

- **Microsoft Store/Google Play/Mac App Store** — cobrança e direitos. O Google Play usa faturamento no dispositivo; as listagens de produção devem adicionar Play Integrity e/ou verificação do servidor de acordo com a política do Google.
- **GitHub (ou host do manifesto)** — versão opcional JSON sobre HTTPS (pode incluir IP do cliente nos logs do servidor)
- **Cliente de e-mail** — ao entrar em contato com o suporte via link mailto

## Responsabilidades do operador (enquadramento estilo GDPR)

Dados pessoais podem existir **dentro** dos seus arquivos. Se você processar esses dados, você (ou sua organização) poderá ser um **controlador de dados** e deverá escolher uma base legal, minimizar a retenção e responder às solicitações do titular dos dados.

## Retenção

Os arquivos locais permanecem até que você os exclua, limpe os dados do aplicativo, desinstale o aplicativo ou substitua as pastas de saída. O editor não opera um cronograma de retenção central para dados somente locais.

##Seus direitos

Para dados que o editor possui (por exemplo, correspondência por e-mail de suporte), entre em contato com **razvan.gutulov@outlook.com**. Para dados armazenados apenas no seu dispositivo, você pode excluir a maioria dos dados do aplicativo por meio de **Limpar dados do aplicativo**, desinstalar ou excluir manualmente o arquivo. **Limpar dados do aplicativo** remove sessões, registros e rascunhos de automação, mas pode reter âncoras de avaliação de licença, marcadores de instalação paga e um identificador de instalação anônimo usado para verificações de licença opcionais. Consulte o texto de confirmação no aplicativo antes de continuar.

Para dados detidos pelo editor:

- E-mail de suporte e correspondência: até 24 meses após o último contato significativo, salvo se uma disputa ou obrigação legal exigir retenção maior.
- Registos de compras diretas, reembolsos, impostos e contabilidade: até 7 anos quando a lei fiscal ou contabilística o exigir.
- Registos de entitlement num servidor de licenças operado pelo editor: enquanto ativos mais até 24 meses após expiração ou revogação.
- Registos de acesso/segurança num servidor operado pelo editor: até 90 dias, salvo necessidade maior para investigação de segurança, prevenção de fraude ou reclamações legais.


## Crianças

Ferramenta geral de produtividade não direcionada a crianças menores de 13 anos (ou à idade exigida em sua jurisdição).

## Mudanças

Mudanças materiais devem aparecer nas listagens da loja e na documentação do aplicativo antes do lançamento.


---

Quando esta tradução estiver incompleta, prevalece a Política de Privacidade em inglês.

## Controlador e contato

Para dados pessoais processados pelo editor, o controlador é **Guțulov Răzvan Constantin PFA**. Contato: **razvan.gutulov@outlook.com**.

## Retenção (registros do editor)

Para dados mantidos pelo editor:

- E-mail de suporte e correspondência: até 24 meses após o último contato significativo, salvo se uma disputa ou obrigação legal exigir retenção maior.
- Registros de compra direta, reembolso, fiscais e contábeis: até 7 anos quando exigido por lei fiscal ou contábil.
- Registros de direito em servidor de licença operado pelo editor: enquanto o direito estiver ativo, mais até 24 meses após expiração ou revogação.
- Logs de acesso e segurança em servidor operado pelo editor: até 90 dias, salvo necessidade maior para investigação de segurança, prevenção de fraude ou reivindicações legais.

## Seus direitos (tempo de resposta)

O editor procura responder a solicitações de titulares de dados em até **30 dias** após uma solicitação verificada (a verificação de identidade pode ser solicitada quando razoavelmente necessária).
