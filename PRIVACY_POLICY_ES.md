> **Traducción automática no oficial: no asesoramiento legal.** El [CLUF en inglés](./EULA_EN.md) y la [Política de privacidad en inglés](./PRIVACY_POLICY_EN.md) rigen si esta traducción entra en conflicto con ellos. Consulte a un abogado calificado en su jurisdicción.

---

# Política de privacidad: organizar archivos

**Editor:** Razvan Constantin Gutulov  
**Contacto:** razvan.gutulov@outlook.com  
**Fecha de entrada en vigor:** 2026-05-28  
**URL pública:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_ES.md`

---

## Resumen

Organizar archivos procesa archivos **localmente en el dispositivo**. El contenido del archivo **no se carga en los servidores propios del editor** para operaciones normales de organización o reparación. La aplicación **escribe archivos locales** en el dispositivo (instantáneas de sesión, estado de reanudación, registros opcionales) como se describe a continuación.

## Responsable del tratamiento y contacto

Para los datos personales tratados por el editor, el responsable del tratamiento es **Razvan Constantin Gutulov**. Contacto: **razvan.gutulov@outlook.com**.

## Datos procesados localmente

| Datos | Dónde se almacena | Propósito |
|------|----------------|---------|
| Archivos y carpetas que seleccione | Sólo tu dispositivo | Organizar, deduplicar, reparar, eliminar opcionalmente |
| Instantánea de la sesión de UI (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (escritorio) o almacenamiento privado de aplicaciones (Android) | Restaurar espacio de trabajo: rutas, extensiones, opciones |
| Organizar currículum + diario de movimiento opcional | Salida `_OrganizeMediaLogs` o carpeta de sesión | Saltar movimientos completados; metadatos de recuperación (rutas codificadas) |
| Ejecutar JSON de latido opcional | Salida `_OrganizeMediaLogs` | Contadores de progreso para herramientas externas |
| Estado de prueba/licencia | Carpeta de perfil en Datos de aplicación local | Hacer cumplir el derecho de prueba o almacenamiento |
| Estado de verificación de actualización | Carpeta de perfil | Acelerar las comprobaciones del manifiesto de versión opcional |
| Puesta en escena de Android SAF | Carpeta de sesión en el almacenamiento de aplicaciones | Copie los árboles `content://` para que el motor pueda leerlos |
| Contraseña SMTP opcional para notificaciones por correo | Se almacena cifrada en las preferencias de sesión del dispositivo (AES-GCM con un archivo de clave por perfil). Al actualizar, si el campo existe, cualquier contraseña SMTP heredada guardada sin AES-GCM se reescribe una sola vez a AES-GCM. El archivo de clave AES-GCM permanece en la carpeta de perfil de la aplicación y puede leerlo la cuenta de usuario del OS con sesión iniciada; protege lecturas casuales del JSON de preferencias, no una bóveda de hardware. | Solo si habilitas notificaciones por correo e introduces credenciales SMTP |

## Lo que el editor no recibe por defecto

- Contenido del archivo de ejecuciones de organización/reparación.  
- Contactos, ubicación, micrófono o cámara (no utilizados)  
- SDK de análisis incluidos en el árbol de código abierto  

## Uso de red opcional

| Actividad | Datos enviados | Destinatario |
|----------|-----------|-----------|
| Comprobación de actualización opcional | HTTPS GET a un manifiesto de versión. El host (por ejemplo, GitHub) recibe la dirección IP de la solicitud, el agente de usuario `OrganizeFiles-UpdateCheck/1.0` y los metadatos TLS. No se envían rutas de archivos ni contenidos de archivos. Deshabilite con `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host que sirve el manifiesto JSON |
| Compra/licencia de tienda | API de facturación de plataforma | Microsoft, Google o Apple (por canal) |
| Servidor de licencias opcional (configurado por el operador) | Se envía un ID de instalación persistente aleatorio (GUID almacenado en `license_installation_id.txt`) a un servidor de licencias operado por el editor o configurado por el operador en `ORGANIZE_FILES_LICENSE_SERVER_URL`. El ID de instalación es un identificador de dispositivo según el considerando 30 del RGPD. Base jurídica: ejecución del contrato. Retención del editor: registros de entitlement mientras estén activos más hasta 24 meses tras caducidad/revocación (prevención de abusos y disputas); registros contables hasta 7 años cuando lo exija la ley. Los servidores del operador siguen el calendario documentado del operador. Esta función está inactiva a menos que se establezca `ORGANIZE_FILES_LICENSE_SERVER_URL`. | Servidor de licencias de editor u operador |
| Seguimiento opcional de OpenTelemetry (configurado por el operador) | Cuando se configura `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT`, los metadatos del trabajo de automatización (ID de trabajo, ID de correlación, etiquetas de tipo de destino, contexto de seguimiento W3C) se exportan al recopilador OTLP configurado. No se incluyen rutas de archivos ni contenidos de archivos. Esta función está inactiva de forma predeterminada y requiere una configuración explícita del operador. | Recopilador OTLP configurado por el operador |
| Notificaciones por correo opcionales (cuando están habilitadas) | Estado de ejecución y extractos del registro (pueden incluir rutas de archivo) enviados a través del servidor SMTP configurado por el operador | SMTP / proveedor de correo del operador |

Las comprobaciones de actualización comparan **solo metadatos de la versión**. La aplicación de escritorio puede ejecutar esta verificación una vez al día después de la aceptación del EULA, a menos que esté deshabilitada.

## Bases legales (encuadre estilo GDPR, no asesoramiento legal)

| Procesamiento | Base típica |
|------------|----------------|
| Organización/reparación local en carpetas ya seleccionadas | Ejecución del contrato/interés legítimo del operador |
| Archivos locales de sesión, currículum y latidos | Igual: necesario para proporcionar la herramienta |
| Facturación y derechos de tienda | Contrato con la tienda de plataforma |
| Comprobación de manifiesto de actualización opcional | Interés legítimo en actualizaciones de seguridad; se puede desactivar mediante una variable de entorno |
| Correo electrónico de soporte | Interés legítimo / actuaciones precontractuales a petición suya |

## Transferencias internacionales

Las comprobaciones de actualizaciones opcionales pueden llegar a servidores fuera del Espacio Económico Europeo (por ejemplo, GitHub en los Estados Unidos). La facturación de la tienda se maneja según los términos de cada plataforma.

## Autoridad de control y quejas

Si la ley aplicable otorga derechos a los interesados o presenta una queja ante una autoridad supervisora, comuníquese primero con el editor en **razvan.gutulov@outlook.com**. Los residentes de la UE/EEE también pueden presentar una queja ante su autoridad local de protección de datos (para Rumania: ANSPDCP, https://www.dataprotection.ro).

## Procesadores de terceros (cuando se utilizan estas funciones)

- **Microsoft Store / Google Play / Mac App Store**: facturación y derechos. Google Play utiliza facturación en el dispositivo; Los listados de producción deben agregar Play Integrity y/o verificación del lado del servidor según la política de Google.
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

Para obtener los datos que posee el editor (por ejemplo, correspondencia por correo electrónico de soporte), comuníquese con **razvan.gutulov@outlook.com**. Cuando proceda, puede solicitar acceso, rectificación, supresión, limitación, oposición, portabilidad o retirada del consentimiento. El editor procura responder a las solicitudes verificadas en un plazo de **30 días** (puede pedirse verificación de identidad si es razonablemente necesario). Para los datos almacenados solo en su dispositivo, puede eliminar la mayoría de los datos de la aplicación mediante **Borrar datos de la aplicación**, desinstalación o eliminación manual de archivos. **Borrar datos de la aplicación** elimina sesiones, registros y borradores de automatización, pero puede conservar anclajes de prueba de licencia, marcadores de instalación paga y un identificador de instalación anónimo utilizado para verificaciones de licencia opcionales; consulte el texto de confirmación en la aplicación antes de continuar.

## niños

Herramienta de productividad general no dirigida a niños menores de 13 años (o la edad requerida en su jurisdicción).

## Cambios

Los cambios materiales deben aparecer en los listados de tiendas y en la documentación de la aplicación antes del lanzamiento.

## Documentos relacionados

- [CLUF (inglés)](./EULA_EN.md)  
- [Política de privacidad (rumano)](./PRIVACY_POLICY_RO.md)  
- [Política de privacidad (alemán)](./PRIVACY_POLICY_DE.md)  
- [Política de privacidad (francés)](./PRIVACY_POLICY_FR.md)
