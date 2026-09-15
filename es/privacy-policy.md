> **Traducción facilitada por comodidad.** El [CLUF en inglés](../en/eula.md) y la [Política de privacidad en inglés](../en/privacy-policy.md) son las versiones de referencia. Cuando la legislación imperativa de consumo de su país dé prioridad a la versión en su propio idioma, prevalecerá esa versión. No es asesoramiento jurídico — consulte a un abogado cualificado en su jurisdicción.

---

# Política de privacidad: Organize Files

**Editor:** Guțulov Răzvan Constantin PFA  
**Domicilio registrado:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Registro mercantil:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Número de identificación fiscal:** 53610310  
**Contacto:** razvan.gutulov@outlook.com  
**Fecha de entrada en vigor:** 2026-05-28  
**URL pública:** `https://github.com/GutRaz/organize-files-legal/blob/main/es/privacy-policy.md`

---

## Resumen

Organize Files procesa archivos **localmente en el dispositivo**. El contenido del archivo **no se carga en los servidores propios del editor** para operaciones normales de organización o reparación. La aplicación **escribe archivos locales** en el dispositivo (instantáneas de sesión, estado de reanudación, registros opcionales) como se describe a continuación.

## Responsable del tratamiento y contacto

Para los datos personales tratados por el editor, el responsable del tratamiento es **Guțulov Răzvan Constantin PFA**. Contacto: **razvan.gutulov@outlook.com**.

## Datos procesados localmente

| Datos | Dónde se almacena | Propósito |
|------|----------------|---------|
| Archivos y carpetas que usted elige | Solo en su dispositivo | Organizar, buscar duplicados, reparar y eliminar cuando se elige |
| Instantánea de la sesión de UI (`last-ui-session.json`) | La carpeta `sessions\<id>\` dentro de la carpeta de perfil de la aplicación: `%LocalAppData%\OrganizeFilesCrossPlatform` en Windows, `~/Library/Application Support/OrganizeFilesCrossPlatform` en macOS, `~/.local/share/OrganizeFilesCrossPlatform` en Linux, o el almacenamiento privado de la aplicación en Android e iOS | Restaurar espacio de trabajo: rutas, extensiones, opciones |
| Estado de reanudación de una organización + registro de movimientos opcional | `_OrganizeMediaLogs` en la carpeta de salida, o la carpeta de sesión | Omitir movimientos ya hechos, datos de recuperación con rutas codificadas |
| Archivo de progreso opcional de una ejecución, JSON | `_OrganizeMediaLogs` en la carpeta de salida | Contadores de progreso para otros programas |
| Estado de la prueba y de la licencia | Carpeta de perfil de la aplicación | Aplicar la prueba o la compra en la tienda |
| Estado de la comprobación de actualizaciones | Carpeta de perfil de la aplicación | Limitar la frecuencia de la comprobación opcional de versión |
| Android: copias de carpetas elegidas con el selector del sistema, SAF | Carpeta de sesión en el almacenamiento de la aplicación | Copia árboles de carpetas `content://` para que el motor pueda leerlos |
| Contraseña SMTP opcional para notificaciones por correo | Se almacena cifrada en las preferencias de sesión del dispositivo (AES-GCM con un archivo de clave por perfil). Al actualizar, si el campo existe, cualquier contraseña SMTP heredada guardada sin AES-GCM se reescribe una sola vez a AES-GCM. El archivo de clave AES-GCM permanece en la carpeta de perfil de la aplicación y puede leerlo la cuenta de usuario del OS con sesión iniciada; protege lecturas casuales del JSON de preferencias, no una bóveda de hardware. | Solo si habilitas notificaciones por correo e introduces credenciales SMTP |

## Lo que el editor no recibe por defecto

- Contenido del archivo de ejecuciones de organización/reparación.  
- Contactos, ubicación, micrófono o cámara (no utilizados)  
- Datos de análisis o publicidad (la aplicación no incluye ningún SDK de ese tipo)  
- Contraseñas SMTP que guarda localmente (permanecen en su dispositivo salvo que envíe correo a través de su servidor SMTP)  

## Uso de red opcional

| Actividad | Datos enviados | Destinatario |
|----------|-----------|-----------|
| Comprobación de actualización opcional | HTTPS GET a un manifiesto de versión. El host (por ejemplo, GitHub) recibe la dirección IP de la solicitud, el agente de usuario `OrganizeFiles-UpdateCheck/1.0` y los metadatos TLS. No se envían rutas de archivos ni contenidos de archivos. Deshabilite con `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host que sirve el manifiesto JSON |
| Compra/licencia de tienda | API de facturación de plataforma | Microsoft, Google o Apple (por canal) |
| Servidor de licencias opcional (configurado por el operador) | Se envía un ID de instalación persistente aleatorio (GUID almacenado en `license_installation_id.txt`) a un servidor de licencias operado por el editor o configurado por el operador en `ORGANIZE_FILES_LICENSE_SERVER_URL`. El ID de instalación es un identificador de dispositivo según el considerando 30 del RGPD. Base jurídica: ejecución del contrato. Retención del editor: registros de entitlement mientras estén activos más hasta 24 meses tras caducidad/revocación (prevención de abusos y disputas); registros contables hasta 7 años cuando lo exija la ley. Los servidores del operador siguen el calendario documentado del operador. Esta función está inactiva a menos que se establezca `ORGANIZE_FILES_LICENSE_SERVER_URL`. | Servidor de licencias de editor u operador |
| Seguimiento opcional de OpenTelemetry (configurado por el operador) | Cuando se configura `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT`, los metadatos del trabajo de automatización (ID de trabajo, ID de correlación, etiquetas de tipo de destino, contexto de seguimiento W3C) se exportan al recopilador OTLP configurado. No se incluyen rutas de archivos ni contenidos de archivos. Esta función está inactiva de forma predeterminada y requiere una configuración explícita del operador. | Recopilador OTLP configurado por el operador |
| Notificaciones por correo opcionales (cuando están habilitadas) | Estado de ejecución y extractos del registro (pueden incluir rutas de archivo) enviados a través del servidor SMTP configurado por el operador | SMTP / proveedor de correo del operador |
| Webhooks de automatización opcionales (configurados por el operador) | Cuando `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` está definido, eventos del ciclo de vida de los trabajos con identificadores de correlación y las rutas de los archivos de estado de la automatización | Punto de conexión webhook configurado por el operador |
| Comprobación opcional de identidad para aprobar la ejecución (configurada por el operador) | Con `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` definido, un GET HTTPS obtiene las claves de firma y las guarda en caché una hora; ningún token sale del dispositivo. Con `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` definido, se envía por POST el propio token de portador del operador a ese extremo para validarlo (RFC 7662), con credenciales de cliente HTTP Basic si están configuradas. Inactivo salvo que se defina una de esas URL. | Proveedor de identidad configurado por el operador |

Las comprobaciones de actualización comparan **solo metadatos de la versión**. La aplicación de escritorio puede ejecutar esta verificación una vez al día después de la aceptación del EULA, a menos que esté deshabilitada.

## Bases legales (encuadre estilo GDPR, no asesoramiento legal)

| Procesamiento | Base típica |
|------------|----------------|
| Organización/reparación local en carpetas ya seleccionadas | Ejecución del contrato/interés legítimo del operador |
| Archivos locales de sesión, reanudación y progreso | Igual, necesarios para prestar la herramienta |
| Facturación y derechos de tienda | Contrato con la tienda de plataforma |
| Comprobación de manifiesto de actualización opcional | Interés legítimo en actualizaciones de seguridad; se puede desactivar mediante una variable de entorno |
| Correo electrónico de soporte | Interés legítimo / actuaciones precontractuales a petición suya |

## Transferencias internacionales

Las comprobaciones de actualizaciones opcionales pueden llegar a servidores fuera del Espacio Económico Europeo (por ejemplo, GitHub en los Estados Unidos). La facturación de la tienda se maneja según los términos de cada plataforma.

## Autoridad de control y quejas

Si la ley aplicable otorga derechos a los interesados o presenta una queja ante una autoridad supervisora, comuníquese primero con el editor en **razvan.gutulov@outlook.com**. Los residentes de la UE/EEE también pueden presentar una queja ante su autoridad local de protección de datos (para Rumania: ANSPDCP, https://www.dataprotection.ro).

## Procesadores de terceros (cuando se utilizan estas funciones)

- **Microsoft Store / Google Play / Mac App Store**: facturación y derechos. Google Play valida las compras en el dispositivo.
- **GitHub (o el host de manifiesto)**: versión opcional JSON sobre HTTPS (puede incluir la IP del cliente en los registros del servidor)
- **Cliente de correo electrónico**: al comunicarse con el soporte a través del enlace mailto

## Responsabilidades del operador (encuadre estilo GDPR)

Es posible que existan datos personales **dentro** de sus archivos. Si procesa dichos datos, usted (o su organización) puede ser un **controlador de datos** y debe elegir una base legal, minimizar la retención y responder a las solicitudes de los interesados.

## Retención

Los archivos locales permanecen hasta que los elimina, borra los datos de la aplicación, desinstala la aplicación o sobrescribe las carpetas de salida. El editor no opera un programa de retención central para datos exclusivamente locales.

Para los datos que conserva el editor:

- Correo de soporte y correspondencia: hasta 24 meses tras el último contacto relevante, salvo disputa u obligación legal que exija más tiempo.
- Compras directas, reembolsos, impuestos y contabilidad: hasta 7 años cuando lo exija la ley fiscal o contable.
- Registros de entitlement de un servidor de licencias operado por el editor: mientras estén activos más hasta 24 meses tras caducidad o revocación.
- Registros de acceso/seguridad de un servidor operado por el editor: hasta 90 días, salvo necesidad mayor por investigación de seguridad, fraude o reclamaciones.

## Tus derechos

Para obtener los datos que posee el editor (por ejemplo, correspondencia por correo electrónico de soporte), comuníquese con **razvan.gutulov@outlook.com**. Cuando proceda, puede solicitar acceso, rectificación, supresión, limitación, oposición, portabilidad o retirada del consentimiento. El editor procura responder a las solicitudes verificadas en un plazo de **30 días** (puede pedirse verificación de identidad si es razonablemente necesario). Para los datos almacenados solo en su dispositivo, puede eliminar la mayoría de los datos de la aplicación mediante **Borrar datos de la aplicación**, desinstalación o eliminación manual de archivos. **Borrar datos de la aplicación** elimina sesiones, registros y borradores de automatización, pero puede conservar anclajes de prueba de licencia, marcadores de instalación paga y un identificador de instalación utilizado para verificaciones de licencia opcionales; consulte el texto de confirmación en la aplicación antes de continuar.

## niños

Herramienta de productividad general no dirigida a niños menores de 13 años (o la edad requerida en su jurisdicción).

## Cambios

Los cambios materiales deben aparecer en los listados de tiendas y en la documentación de la aplicación antes del lanzamiento.

## Documentos relacionados

- [CLUF (inglés)](../en/eula.md)  
- [Política de privacidad (rumano)](../ro/privacy-policy.md)  
- [Política de privacidad (alemán)](../de/privacy-policy.md)  
- [Política de privacidad (francés)](../fr/privacy-policy.md)
