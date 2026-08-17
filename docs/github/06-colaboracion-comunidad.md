# 06 — Colaboración y comunidad

## Situación

`drifting-minsky` crece. Hay preguntas que no son bugs ("¿por qué eligieron PySpark y no
pandas?"), documentación que no cabe en el README, y quieres una pequeña web con la
referencia del pipeline. Además, si algún día lo abres al público, necesitas señales de
proyecto sano para que la gente contribuya. Todo esto es la **capa de colaboración y
comunidad** de GitHub: lo que la diferencia de un simple hosting de Git.

## Objetivo

- Distinguir las herramientas de conversación: **Issues vs Discussions**.
- Conocer **Wiki**, **GitHub Pages** y **Gists** y cuándo usar cada uno.
- Entender **notificaciones**, **watch/star**, menciones y **@mentions**.
- Reconocer los **community health files** y el concepto de **InnerSource**.
- Ubicar los beneficios de la comunidad: open source, **Sponsors**, **Education**.

## Issues vs Discussions

Ambos son conversaciones, pero resuelven cosas distintas — **comparación estrella del
dominio de colaboración**:

| | **Issues** | **Discussions** |
|---|-----------|-----------------|
| Para qué | Trabajo accionable: bugs, tareas | Conversación abierta: preguntas, ideas, anuncios |
| ¿Se "cierra"? | Sí (resuelto/cerrado) | No; se puede marcar una **respuesta** como aceptada |
| Formato | Lista de tickets | Foro con categorías e hilos anidados |
| Ejemplo | "Bug: quantity negativa" | "¿PySpark vs pandas para este tamaño de datos?" |

Discussions se habilita en *Settings → Features*. Tiene categorías (Q&A, Ideas,
Announcements, Show and tell) y permite **votar** respuestas. Un issue que en realidad
era una conversación se puede **convertir en discussion**.

## Wiki

Cada repo puede tener una **Wiki**: un espacio de documentación en páginas Markdown,
con su propio historial (de hecho es un repo Git aparte). Buena para manuales largos,
guías de arquitectura, glosarios. Diferencia con el README: el README es la portada
corta; la wiki es documentación extensa multipágina.

> Para docs que deben versionarse **junto al código** (y revisarse en PRs), muchos
> equipos prefieren una carpeta `docs/` en el propio repo —como este mismo proyecto—
> en vez de la wiki.

## GitHub Pages

**GitHub Pages** publica un **sitio web estático** directamente desde un repo (o una
carpeta `/docs`, o una rama `gh-pages`). Ideal para documentación, portfolios, landing
del proyecto.

- URL por defecto: `https://<usuario>.github.io/<repo>`.
- Soporta HTML plano o generadores estáticos como **Jekyll** (integrado) y otros vía
  Actions.
- Un repo especial `usuario.github.io` sirve como tu sitio personal raíz.

Para el examen: **Pages = hosting de sitios estáticos desde un repo**; no corre backend
ni bases de datos.

## Gists

Un **Gist** es un fragmento compartible (un snippet, un log, una nota) que vive en
`gist.github.com` y **es en sí mismo un repo Git** (tiene historial y se puede clonar).

- **Public gist** — aparece en búsquedas y en tu perfil.
- **Secret gist** — no se lista ni se indexa, pero **cualquiera con el link lo ve**
  (no es privado de verdad; ojo con la pregunta trampa).

Úsalo para compartir código suelto sin crear un repo entero.

## Notificaciones, watch y star

- **Star** — marcador/"me gusta"; guarda el repo en tu lista y es señal de popularidad.
  **No** te suscribe a notificaciones.
- **Watch** — **sí** te suscribe. Puedes elegir "All activity", "Participating and
  @mentions" (por defecto) o eventos personalizados (releases, discussions…).
- **Fork** — copia el repo a tu cuenta ([tema 01](01-repos-y-proyecto.md)); tampoco es
  una suscripción.
- **@menciones** — nombrar a `@usuario` o `@org/equipo` notifica a esa persona/equipo.
- Las notificaciones llegan a la **bandeja** (`github.com/notifications`) y/o al email.

Trampa clásica: **Star ≠ Watch**. Star = guardar/aplaudir; Watch = suscribirse a avisos.

## Community health files

GitHub reconoce archivos que hacen "sano" un proyecto (muchos ya vistos en el
[tema 01](01-repos-y-proyecto.md)). Pueden ir en el repo o, como defaults de toda una
org, en un repo especial **`.github`**:

- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `SUPPORT.md`, `CODEOWNERS`, plantillas de issue/PR, `FUNDING.yml` (botón Sponsor).
- El **Community Standards** checklist (en Insights) te dice cuáles te faltan.

## Open source, InnerSource y la comunidad

- **Open source** — código con licencia que permite usarlo/modificarlo/distribuirlo. El
  flujo de contribución externa es **fork → PR** ([temas 01](01-repos-y-proyecto.md) y
  [03](03-pull-requests.md)); labels como `good first issue` bajan la barrera de entrada.
- **InnerSource** — aplicar prácticas de open source **dentro** de una empresa: repos
  `internal`, PRs abiertos entre equipos, transparencia. Es un término que GH-900 pregunta.
- **GitHub Sponsors** — financiamiento a mantenedores/proyectos; el botón "Sponsor" se
  configura con `FUNDING.yml`.
- **GitHub Education** — GitHub gratis con extras para estudiantes y docentes
  (**Student Developer Pack**, GitHub Classroom). También sale en el examen.
- **GitHub Skills / Docs** — recursos de aprendizaje oficiales.

## En el examen (GH-900)

- **Issues = trabajo accionable; Discussions = conversación abierta** (no se "cierran",
  se acepta una respuesta).
- **Wiki** = documentación multipágina; **Pages** = sitio web estático desde el repo.
- **Gist** = snippet compartible que es un mini-repo; **secret gist** no es privado
  (visible con el link).
- **Star ≠ Watch**: star guarda/aplaude, watch suscribe a notificaciones.
- **InnerSource** = prácticas open source puertas adentro de una empresa.
- **Sponsors** financia mantenedores; **Education / Student Pack** da GitHub gratis a estudiantes.
- Los **community health files** pueden centralizarse en el repo `.github` de la org.

## Conceptos clave

- **Discussions** — foro de conversación por categorías, complementa a Issues.
- **GitHub Pages** — hosting de sitios estáticos desde un repo.
- **Gist** — snippet/nota como mini-repo (public o secret).
- **Watch vs Star** — suscribirse vs marcar.
- **InnerSource / Sponsors / Education** — la dimensión de comunidad de GitHub.

## Siguiente

→ [07 — Seguridad y administración](07-seguridad-y-admin.md)
