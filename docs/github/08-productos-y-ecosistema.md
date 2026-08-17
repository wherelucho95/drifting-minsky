# 08 — Productos y ecosistema

## Situación

Ya sabes trabajar en GitHub. Ahora el examen quiere que reconozcas el **catálogo**: qué
planes existen, qué incluye cada uno, y las herramientas del ecosistema —Copilot,
Codespaces, Packages, Marketplace, y las apps Mobile/Desktop/CLI—. Son preguntas de
"¿qué producto resuelve esto?" más que de configuración.

## Objetivo

- Distinguir los **planes** (Free, Team, Enterprise) para cuentas personales y orgs.
- Entender cómo se **factura** Actions, Packages y Codespaces (minutos/almacenamiento).
- Conocer **Copilot**, **Codespaces**, **Packages** y el **Marketplace**.
- Ubicar las formas de acceder a GitHub: **web, Desktop, Mobile, CLI, IDE**.

## Planes de GitHub

Los detalles de precio cambian; el examen pide el **concepto** de cada nivel:

| Plan | Para | Incluye (idea general) |
|------|------|------------------------|
| **Free** | Personas y orgs | Repos públicos y privados **ilimitados**, colaboradores ilimitados, Actions/Packages con cuota gratuita, funciones de comunidad |
| **Team** | Organizaciones | Todo lo de Free + herramientas de equipo: revisores requeridos, repos internos, más minutos de Actions, controles de acceso |
| **Enterprise** | Grandes empresas | Todo lo de Team + **SAML SSO**, audit log avanzado, **GitHub Advanced Security**, y opción **EMU** (Enterprise Managed Users) |

Dos formas de desplegar Enterprise (aparece a veces):

- **GitHub Enterprise Cloud (GHEC)** — alojado por GitHub (en github.com).
- **GitHub Enterprise Server (GHES)** — instalado en la infraestructura del cliente
  (auto-hospedado).

> Antes existía **GitHub AE**; hoy la oferta gira en torno a GHEC/GHES. Si ves "AE" en
> material viejo, mentalmente mapéalo a la variante gestionada de Enterprise.

Nota histórica que confunde: los repos **privados con colaboradores ilimitados** son
gratis desde 2020; el viejo "Pro" quedó como extras menores para cuentas personales.

## Facturación de lo que se consume

GitHub cobra por **uso** en tres servicios (con cuota gratuita según el plan; **gratis
e ilimitado en repos públicos**):

- **Actions** — por **minutos** de runner (los de Windows/macOS cuestan más que Linux)
  y almacenamiento de artefactos.
- **Packages** / **Codespaces** — por **almacenamiento** y transferencia / horas de cómputo.
- Se controla con **spending limits** en la facturación de la cuenta u organización.

## GitHub Copilot

**Copilot** es el asistente de IA de GitHub: autocompletado y generación de código en el
editor, **Copilot Chat** para preguntar y explicar, y funciones en PRs e IDE. Se ofrece
en planes (Copilot Free limitado, Individual/Pro, Business, Enterprise) y es **gratis
para estudiantes y mantenedores open source verificados**. En GH-900 aparece como parte
del "desarrollo moderno": reconoce **qué es** y que respeta políticas de la org.

## GitHub Codespaces

**Codespaces** es un **entorno de desarrollo en la nube**: un contenedor con VS Code (en
el navegador o conectado a tu VS Code local) ya configurado para el repo. Se define con
un `.devcontainer/`. Ventaja: clonar+configurar en segundos, mismo entorno para todo el
equipo, sin "en mi máquina sí funciona". Se factura por horas de cómputo y almacenamiento.

Para `drifting-minsky` un devcontainer con Python 3.11 + Java (para PySpark) evitaría el
setup manual de cada persona.

## GitHub Packages

**Packages** es un **registro de paquetes** integrado al repo: publica y consume
librerías/imágenes (npm, PyPI-like, Maven, NuGet, RubyGems y **contenedores** vía
`ghcr.io`). Se autentica con el mismo `GITHUB_TOKEN`/PAT y respeta los permisos del repo.
Encaja con [Actions](05-actions.md): un workflow puede **construir y publicar** el paquete
en un release.

## GitHub Marketplace

El **Marketplace** es la tienda del ecosistema. Dos tipos de productos:

- **Actions** — piezas reutilizables para workflows ([tema 05](05-actions.md)).
- **Apps** (GitHub Apps / integraciones) — herramientas de terceros (CI externos, Slack,
  gestión de proyectos, seguridad) que se instalan con permisos acotados.

Distinción para el examen: **Action** = paso dentro de un workflow; **App** = integración
instalada a nivel repo/org.

## Formas de usar GitHub

- **Web** (github.com) — todo desde el navegador; incluso un **editor web** (tecla `.`
  en un repo abre github.dev, un VS Code ligero).
- **GitHub Desktop** — app de escritorio (Windows/Mac) que envuelve Git con GUI; buena
  para quien no domina la terminal.
- **GitHub Mobile** — app iOS/Android para issues, PRs, revisiones y notificaciones en marcha.
- **GitHub CLI (`gh`)** — la terminal oficial; la usamos en todos los temas.
- **Integración con IDEs** — VS Code, Visual Studio, JetBrains (PRs, Codespaces, Copilot).

## En el examen (GH-900)

- **Free** ya incluye repos privados y colaboradores **ilimitados**; **Team** añade
  herramientas de organización; **Enterprise** añade SSO/SAML, Advanced Security y EMU.
- **GHEC** (nube) vs **GHES** (auto-hospedado) son las dos entregas de Enterprise.
- **Actions/Packages/Codespaces** se facturan por uso y son **gratis en repos públicos**.
- **Copilot** = IA de código; **Codespaces** = dev environment en la nube; **Packages** =
  registro de paquetes; distínguelos.
- **Marketplace** vende **Actions** y **Apps**.
- GitHub se usa desde **web, Desktop, Mobile, CLI (`gh`) e IDE**.

## Conceptos clave

- **Free / Team / Enterprise** — los tres niveles y qué desbloquea cada uno.
- **GHEC vs GHES** — Enterprise en la nube vs auto-hospedado.
- **Copilot / Codespaces / Packages** — IA, entorno en nube, registro de paquetes.
- **Marketplace** — Actions y Apps.
- **Desktop / Mobile / CLI** — las apps oficiales para acceder a GitHub.

## Siguiente

→ [09 — Simulacro GH-900](09-simulacro-gh900.md)
