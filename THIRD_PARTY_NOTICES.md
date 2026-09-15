# Third-Party Notices

This notice lists the third-party components redistributed with Organize Files and the licence each one is used under.

## Included in the app package

### Microsoft .NET runtime and Windows desktop components

Release builds are self-contained and include Microsoft .NET runtime / desktop runtime components needed to run the Avalonia desktop application.

- Project: .NET
- Provider: Microsoft and .NET contributors
- License: MIT for the open-source .NET runtime components; Microsoft binary/runtime terms may also apply to official distribution artifacts.
- License/cost information: https://dotnet.microsoft.com/en-us/platform/free, https://dotnet.microsoft.com/platform/open-source, and https://github.com/dotnet/runtime/blob/main/LICENSE.TXT

Copyright (c) .NET Foundation and Contributors.

### Application assets

The application icon and local UI assets in this project are project-owned assets created for Organize Files. They are not copied from third-party branding packs.

### Avalonia (UI framework)

The desktop, Android, and iOS heads are built on Avalonia and its Fluent theme. The assemblies are redistributed inside the app package.

- Project: Avalonia
- Version used by this project: 12.0.2
- License: MIT
- Source/license information: https://github.com/AvaloniaUI/Avalonia and https://licenses.nuget.org/MIT

Copyright 2013-2026 (c) The AvaloniaUI Project.

### CommunityToolkit.Mvvm

MVVM source generators and helpers used by the view models. Redistributed inside the app package.

- Project: .NET Community Toolkit
- Version used by this project: 8.4.0
- License: MIT
- Source/license information: https://github.com/CommunityToolkit/dotnet and https://licenses.nuget.org/MIT

Copyright (c) .NET Foundation and Contributors. All rights reserved.

### Microsoft.ML.OnnxRuntime (neural backend)

The Guide Assistant ranks documentation chapters by meaning with a local sentence-embedding model, and the look-alike picture scan can describe a picture with a local image model. ONNX Runtime executes both on the device. Managed assemblies and per-platform native binaries are redistributed inside the app package.

Three packages from the same project are used, all under the same license:

- `Microsoft.ML.OnnxRuntime.Managed` — the API, with no native library. The shared project compiles against this one.
- `Microsoft.ML.OnnxRuntime.DirectML` — the native build for Windows. It reaches every adapter that speaks DirectX 12, whichever vendor made it, and contains the processor build as well.
- `Microsoft.ML.OnnxRuntime` — the native build for Android, Apple platforms and Linux.

- Project: ONNX Runtime
- Version used by this project: 1.24.3
- License: MIT
- Source/license information: https://github.com/microsoft/onnxruntime

Copyright (c) Microsoft Corporation.

On Windows the DirectML build calls `DirectML.dll`, which is part of Windows itself and is not redistributed with this application.

### Semantic sentence-embedding model (bundled asset)

`Assets/semantic/model.onnx` and `Assets/semantic/vocab.txt` are a third-party pretrained sentence-embedding model redistributed inside the app package. Nothing is sent off the device: the model runs locally, needs no API key, and carries no per-use cost.

- Model: `distiluse-base-multilingual-cased-v2`
- Redistributed export: `Xenova/distiluse-base-multilingual-cased-v2`, file `onnx/model_quantized.onnx`
- License: Apache License 2.0
- Source/license information: https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2 and https://huggingface.co/Xenova/distiluse-base-multilingual-cased-v2

**Statement of modification (Apache-2.0 section 4b).** The bundled file is not the original upstream model file. It is an int8-quantized ONNX export of the upstream model, obtained from the export repository named above and copied unchanged from that repository. Organize Files does not retrain, fine-tune, or otherwise alter the weights.

**License copy (Apache-2.0 section 4a).** A verbatim copy of the Apache License 2.0 that governs this model ships beside the model as `Assets/semantic/MODEL_LICENSE.txt`, together with `Assets/semantic/MODEL_PROVENANCE.txt` recording the exact source repository, file, and license identifier the asset was provisioned from.

Builds made without the model contain no model asset and no ONNX Runtime component. The app then uses its own encoder, which is project-owned code with no third-party dependency.

### Microsoft.Data.Sqlite and SQLitePCLRaw

The file catalog index behind Explore files uses SQLite through Microsoft.Data.Sqlite and the SQLitePCLRaw bundle, including the native `e_sqlite3` library. Redistributed inside the app package.

- Projects: Microsoft.Data.Sqlite (10.0.10), SQLitePCLRaw (3.0.4 bundle / 3.53.3 native)
- Licenses: MIT for Microsoft.Data.Sqlite; Apache License 2.0 for SQLitePCLRaw
- Source/license information: https://github.com/dotnet/efcore and https://github.com/ericsink/SQLitePCL.raw

Copyright (c) Microsoft Corporation. All rights reserved.
Copyright 2014-2024 SourceGear, LLC.

SQLite itself is in the public domain (https://www.sqlite.org/copyright.html).

### Mobile-only components

The Android and iOS heads additionally redistribute:

- Xamarin.Android.Google.BillingClient 6.2.1, Xamarin.AndroidX.Core.SplashScreen 1.0.1.15, Xamarin.AndroidX.DocumentFile 1.0.1.11 — Apache License 2.0 — https://github.com/dotnet/android-libraries

Copyright (c) Microsoft Corporation and the Android Open Source Project.

### OpenTelemetry (automation metrics and traces)

The automation layer exports metrics and traces over OTLP when an operator configures an endpoint. The assemblies are redistributed inside the app package whether or not that export is switched on.

- Project: OpenTelemetry .NET
- Version used by this project: 1.15.3
- Assemblies redistributed: OpenTelemetry, OpenTelemetry.Api, OpenTelemetry.Api.ProviderBuilderExtensions, OpenTelemetry.Exporter.OpenTelemetryProtocol
- License: Apache-2.0
- Source/license information: https://github.com/open-telemetry/opentelemetry-dotnet and https://www.apache.org/licenses/LICENSE-2.0

### Microsoft.IdentityModel and System.IdentityModel.Tokens.Jwt

Signed-token validation on the automation webhook and store notification paths. The assemblies are redistributed inside the app package.

- Projects: Microsoft.IdentityModel.JsonWebTokens, Microsoft.IdentityModel.Protocols.OpenIdConnect and the Microsoft.IdentityModel assemblies they depend on, System.IdentityModel.Tokens.Jwt
- Version used by this project: 8.3.1
- License: MIT
- Source/license information: https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet and https://licenses.nuget.org/MIT

### Avalonia rendering and platform-interop dependencies

These arrive with the UI framework rather than being referenced directly, and they are redistributed inside the app package.

- Projects: SkiaSharp (with the native libSkiaSharp), HarfBuzzSharp, Tmds.DBus.Protocol, MicroCom.Runtime
- License: MIT for each of the four packages
- Source/license information: https://github.com/mono/SkiaSharp, https://github.com/tmds/Tmds.DBus, https://github.com/AvaloniaUI/MicroComGenerator and https://licenses.nuget.org/MIT

### ICU (globalization data, Linux kits only)

.NET refuses to start on a Linux machine that has no ICU: the runtime fails fast inside
`System.Globalization` before any application code runs, and tells the customer to install a system
package. The Linux kits therefore carry the library themselves and the
`System.Globalization.AppLocalIcu` switch points the runtime at that copy. Windows uses its own
built-in globalization and macOS uses the copy inside the operating system, so neither of those kits
carries this component.

- Project: Microsoft.ICU.ICU4C.Runtime (Microsoft build of ICU4C, redistributed unmodified)
- Version used by this project: 72.1.0.3
- Files redistributed: `libicuuc`, `libicui18n` and `libicudata`, in the Linux kits only
- License: Unicode License (Unicode, Inc. License Agreement - Data Files and Software)
- License copy: a verbatim copy ships beside the binary as `ICU_LICENSE.txt`
- Source/license information: https://github.com/unicode-org/icu and https://www.unicode.org/copyright.html

## Integrated media engine (not third-party redistributables)

Organize Files performs media validation and file repair with integrated components inside OrganizeFilesEngine. The commercial-safe package does **not** bundle, invoke, or require separate third-party media executables.

### SixLabors.ImageSharp (managed image decode)

Image pixel repair (decode → PNG, including TIFF frames and embedded JPEG previews) uses SixLabors.ImageSharp as a managed library dependency of OrganizeFilesEngine.

- Project: ImageSharp
- Provider: Six Labors and contributors
- Version used by this project: 3.1.12
- License: Six Labors Split License v1.0 (see package license on NuGet / https://sixlabors.com/licensing/)
- Source: https://github.com/SixLabors/ImageSharp

Copyright (c) Six Labors.

## Apache License 2.0 components

The Apache-2.0 licensed components listed above (the bundled semantic model, SQLitePCLRaw, OpenTelemetry, and the AndroidX components on the Android head) are redistributed under the Apache License, Version 2.0. The full license text is available at https://www.apache.org/licenses/LICENSE-2.0 and, for the bundled model, ships inside the app package as `Assets/semantic/MODEL_LICENSE.txt`.

Where a component is redistributed in a form that differs from its upstream release, the difference is stated in that component's entry above, as required by section 4b of that license.

## Unicode license (ICU)

The Unicode license permits redistribution of the data files and software, in source or binary form,
provided the copyright notice and permission notice travel with them. The Linux kits meet that by
shipping a verbatim copy of the license as `ICU_LICENSE.txt` beside the binary, and by naming the
component in this file. The library is redistributed as built and published by Microsoft, with no
modification of our own.

## MIT license text

The following MIT license text applies to the MIT-licensed components listed above.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the Software), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
