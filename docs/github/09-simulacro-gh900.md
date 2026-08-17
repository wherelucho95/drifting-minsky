# 09 — Simulacro GH-900

Repaso final: primero una **cheat sheet** con lo que más cae, luego **30 preguntas** de
práctica (mismo estilo que el examen) y al final las **respuestas comentadas**. Tápate
las respuestas, responde a lápiz y solo entonces baja a corregir.

---

## Cheat sheet de repaso rápido

**Git vs GitHub**
- Comandos (`add/commit/push`) → **Git**. Funciones web/sociales (issues, PR, actions) → **GitHub**.

**Repos**
- Visibilidad: **public** (visible ≠ escribible), **private**, **internal** (solo la org).
- Sin **LICENSE** → todos los derechos reservados aunque sea público.
- **Fork** = copia en tu cuenta de GitHub; **Clone** = copia en tu máquina.
- Contribuir a repo ajeno: **fork → PR**.

**Issues**
- Describen trabajo, **no** contienen código. Numeración compartida con PRs.
- **Label** (clasifica) / **Milestone** (agrupa con % y fecha) / **Assignee** (responsable).
- **`Closes/Fixes/Resolves #N`** en un PR cierra el issue al fusionar.
- **Task list** `- [ ]` = progreso.

**Pull Requests**
- Propone fusionar **head → base**; incluye review + checks.
- Reviews: **approve / request changes / comment**.
- Merge methods: **merge commit / squash / rebase**.
- **Draft PR** no se puede fusionar. **CODEOWNERS** = revisores por ruta.

**Projects**
- Multi-repo, a nivel **usuario u org**. Vistas: **Board / Table / Roadmap**.
- Campos: Status, Priority, **Iteration**. Automatizaciones integradas.

**Actions**
- **Workflow → Job → Step → Action**, corre en un **Runner**. YAML en `.github/workflows/`.
- Triggers en `on:` (`push`, `pull_request`, `schedule`, `workflow_dispatch`).
- Jobs en **paralelo** salvo `needs:`. **Secrets** para datos sensibles. **Marketplace** = actions/apps.
- Runners: **GitHub-hosted** (efímero) vs **self-hosted**.

**Colaboración/comunidad**
- **Issues** (accionable) vs **Discussions** (conversación, no se cierra).
- **Wiki** (docs), **Pages** (sitio estático), **Gist** (snippet; secret ≠ privado).
- **Star** (guardar) ≠ **Watch** (suscribir). **InnerSource** = open source puertas adentro.
- **Sponsors** financia; **Education/Student Pack** = GitHub gratis a estudiantes.

**Seguridad/admin**
- Permisos: **Read < Triage < Write < Maintain < Admin**.
- **Org → Teams** (heredan permisos). **Branch protection** = exigir PR/approvals/checks.
- **2FA** obligatoria; **PAT fine-grained** > classic.
- **Dependabot** (deps vulnerables), **secret scanning** (credenciales filtradas),
  **CodeQL/code scanning** (bugs de seguridad). **SECURITY.md** = cómo reportar.

**Productos**
- **Free** (repos privados y colaboradores ilimitados) < **Team** < **Enterprise** (SSO/SAML, Advanced Security).
- **GHEC** (nube) vs **GHES** (auto-hospedado).
- **Copilot** (IA), **Codespaces** (dev en la nube), **Packages** (registro), **Marketplace** (actions/apps).
- Acceso: **web, Desktop, Mobile, CLI (`gh`), IDE**.

---

## Preguntas de práctica (30)

**1.** ¿Cuál de estos es una función de GitHub, no de Git?
a) `git commit`  b) Pull Request  c) `git merge`  d) staging area

**2.** Un repositorio **público** implica que…
a) cualquiera puede hacer push  b) cualquiera puede verlo pero escribir requiere permiso
c) no puede tener licencia  d) es lo mismo que un fork

**3.** Quieres contribuir a un proyecto open source en el que **no** tienes permiso de
escritura. ¿Qué haces primero?
a) clonar el repo original  b) pedir acceso de admin  c) hacer un **fork**  d) abrir una Discussion

**4.** ¿Qué hace `Fixes #42` en la descripción de un PR al fusionarlo?
a) borra el issue 42  b) crea el issue 42  c) cierra el issue 42  d) asigna el issue 42

**5.** ¿Cuál agrupa varios issues con una fecha objetivo y muestra % de progreso?
a) label  b) milestone  c) assignee  d) gist

**6.** En Actions, ¿cuál es la jerarquía correcta?
a) Job → Workflow → Step  b) Workflow → Job → Step  c) Step → Job → Runner  d) Action → Workflow → Job

**7.** ¿Dónde viven los archivos de workflow de Actions?
a) `/actions/`  b) `.github/workflows/`  c) `.git/hooks/`  d) `/workflows.yml`

**8.** Por defecto, los **jobs** de un workflow…
a) corren en serie  b) corren en paralelo  c) no corren sin aprobación  d) comparten runner

**9.** Necesitas guardar un token de API para que lo use un workflow. ¿Dónde?
a) en el YAML del workflow  b) en el README  c) en **Actions secrets**  d) en un gist secreto

**10.** ¿Qué vista de GitHub Projects se parece a un diagrama de Gantt sobre el tiempo?
a) Board  b) Table  c) **Roadmap**  d) Insights

**11.** ¿Cuál NO se cierra, sino que permite marcar una respuesta como aceptada?
a) Issue  b) Pull Request  c) Discussion  d) Milestone

**12.** **Star** vs **Watch**: ¿cuál te suscribe a notificaciones de un repo?
a) Star  b) Watch  c) Fork  d) ninguno

**13.** ¿Qué producto publica un **sitio web estático** directamente desde un repo?
a) Codespaces  b) Packages  c) GitHub Pages  d) Gist

**14.** Un **secret gist**…
a) es totalmente privado  b) es visible por cualquiera que tenga el enlace
c) requiere plan Enterprise  d) no puede clonarse

**15.** Orden correcto de permisos de repo, de menor a mayor:
a) Read, Write, Triage, Admin  b) Read, Triage, Write, Maintain, Admin
c) Triage, Read, Write, Admin  d) Read, Maintain, Admin, Write

**16.** Quieres que **nadie** pueda hacer push directo a `main` sin PR aprobado y CI verde.
¿Qué configuras?
a) un gist  b) branch protection / ruleset  c) un milestone  d) CODEOWNERS únicamente

**17.** ¿Qué función abre PRs automáticos cuando una dependencia tiene una vulnerabilidad?
a) CodeQL  b) Dependabot  c) secret scanning  d) Copilot

**18.** ¿Qué detecta **secret scanning**?
a) dependencias desactualizadas  b) credenciales/tokens filtrados en el código
c) errores de estilo  d) tests que fallan

**19.** ¿Cuál es un **entorno de desarrollo en la nube** con VS Code preconfigurado?
a) Codespaces  b) Copilot  c) Actions  d) Pages

**20.** ¿Qué plan de GitHub incluye **repos privados con colaboradores ilimitados** sin costo?
a) ninguno  b) solo Enterprise  c) Free  d) solo Team

**21.** Aplicar prácticas de open source **dentro** de una empresa se llama…
a) forking  b) InnerSource  c) squashing  d) triage

**22.** ¿Qué archivo indica **cómo reportar** una vulnerabilidad de forma responsable?
a) LICENSE  b) CONTRIBUTING.md  c) SECURITY.md  d) CODEOWNERS

**23.** Un **draft pull request**…
a) ya está fusionado  b) no puede fusionarse hasta marcarlo "ready"
c) no dispara Actions  d) es un issue

**24.** ¿Qué método de merge aplasta todos los commits del PR en **uno solo**?
a) merge commit  b) rebase and merge  c) squash and merge  d) fast-forward

**25.** ¿Con qué se autentica Git sobre **HTTPS** hoy (ya no con contraseña)?
a) SSH key  b) Personal Access Token  c) 2FA por SMS  d) deploy key

**26.** ¿Dónde se publican y descubren las **Actions** reutilizables?
a) Packages  b) Marketplace  c) Gists  d) Wiki

**27.** ¿Qué agrupa a personas dentro de una **organización** para dar permisos en bloque?
a) un milestone  b) un team  c) un label  d) un project

**28.** ¿Qué trigger permite ejecutar un workflow **manualmente** desde la UI?
a) `push`  b) `schedule`  c) `workflow_dispatch`  d) `pull_request`

**29.** ¿Qué archivo asigna **revisores automáticos** según la ruta modificada en un PR?
a) `.gitignore`  b) CODEOWNERS  c) `dependabot.yml`  d) SUPPORT.md

**30.** ¿Cuál es la diferencia entre **GHEC** y **GHES**?
a) GHEC es gratis y GHES de pago  b) GHEC está alojado por GitHub; GHES es auto-hospedado
c) son lo mismo  d) GHES no soporta Actions

---

## Respuestas comentadas

1. **b** — el PR es función de GitHub; las otras son de Git ([foundations](../github-foundations.md)).
2. **b** — público = visible; escribir necesita permiso ([01](01-repos-y-proyecto.md)).
3. **c** — sin permiso de escritura, primero **fork**, luego PR ([01](01-repos-y-proyecto.md)).
4. **c** — closing keyword: cierra el issue al fusionar ([02](02-issues.md)).
5. **b** — milestone agrupa con fecha y %; label solo clasifica ([02](02-issues.md)).
6. **b** — Workflow → Job → Step (dentro de un Runner) ([05](05-actions.md)).
7. **b** — `.github/workflows/` ([05](05-actions.md)).
8. **b** — en paralelo salvo `needs:` ([05](05-actions.md)).
9. **c** — Actions secrets; nunca en el YAML ni en gists ([05](05-actions.md)).
10. **c** — Roadmap es la vista temporal tipo Gantt ([04](04-projects.md)).
11. **c** — Discussions no se cierran; se acepta una respuesta ([06](06-colaboracion-comunidad.md)).
12. **b** — Watch suscribe; Star solo guarda ([06](06-colaboracion-comunidad.md)).
13. **c** — GitHub Pages ([06](06-colaboracion-comunidad.md)).
14. **b** — un secret gist es visible con el enlace, **no** es privado ([06](06-colaboracion-comunidad.md)).
15. **b** — Read, Triage, Write, Maintain, Admin ([07](07-seguridad-y-admin.md)).
16. **b** — branch protection / ruleset ([07](07-seguridad-y-admin.md)).
17. **b** — Dependabot (security updates) ([07](07-seguridad-y-admin.md)).
18. **b** — secret scanning detecta credenciales filtradas ([07](07-seguridad-y-admin.md)).
19. **a** — Codespaces ([08](08-productos-y-ecosistema.md)).
20. **c** — Free ya incluye repos privados y colaboradores ilimitados ([08](08-productos-y-ecosistema.md)).
21. **b** — InnerSource ([06](06-colaboracion-comunidad.md)).
22. **c** — SECURITY.md ([07](07-seguridad-y-admin.md)).
23. **b** — draft PR no se fusiona hasta marcarlo "ready" (sí dispara Actions) ([03](03-pull-requests.md)).
24. **c** — squash and merge ([03](03-pull-requests.md)).
25. **b** — Personal Access Token ([01](01-repos-y-proyecto.md) / [07](07-seguridad-y-admin.md)).
26. **b** — Marketplace ([05](05-actions.md) / [08](08-productos-y-ecosistema.md)).
27. **b** — un team ([07](07-seguridad-y-admin.md)).
28. **c** — `workflow_dispatch` ([05](05-actions.md)).
29. **b** — CODEOWNERS ([03](03-pull-requests.md)).
30. **b** — GHEC en la nube, GHES auto-hospedado ([08](08-productos-y-ecosistema.md)).

---

## Cómo interpretar tu resultado

- **27–30** — listo para presentar. Repasa solo lo que fallaste.
- **21–26** — casi; vuelve a los temas de las preguntas erradas y rehaz el simulacro.
- **< 21** — relee los temas 01–08 con calma y practica en un repo real antes de repetir.

> Estas preguntas son de elaboración propia para practicar el **estilo** y los conceptos
> del examen; no son preguntas oficiales. Complementa con el study guide oficial y los
> exámenes de práctica de GitHub.

## Siguiente

← Volver al [índice de la guía](../github-foundations.md)
