# 07 — Seguridad y administración

## Situación

`drifting-minsky` deja de ser un experimento personal: se mueve a la organización
`acme-data`, entra más gente y `main` ya no puede aceptar cualquier push. Necesitas
decidir **quién puede hacer qué**, blindar `main`, activar 2FA y dejar que GitHub avise
si una dependencia tiene una vulnerabilidad o si alguien filtró un token. Este es el
dominio de **privacidad, seguridad y administración**.

## Objetivo

- Distinguir cuentas **personales** vs **organizaciones**, y **teams**.
- Entender los **niveles de permiso** de un repo (Read → Admin).
- Configurar **branch protection / rulesets** sobre `main`.
- Conocer autenticación: **2FA**, **PAT**, **SSH**, **passkeys**.
- Reconocer las funciones de seguridad: **Dependabot**, **secret scanning**, **code
  scanning (CodeQL)**, **security advisories** y **SECURITY.md**.

## Cuentas personales vs organizaciones

- **Cuenta personal** — un usuario. Posee repos, gists, y puede colaborar en otros.
- **Organización** — cuenta compartida por muchos usuarios para gestionar repos en común.
  No inicia sesión "como org"; las personas entran con **su** cuenta y reciben roles.
  Añade **teams**, permisos granulares, facturación centralizada y políticas.
- **Enterprise** — capa por encima que agrupa varias organizaciones (grandes empresas),
  con SSO/SAML y controles globales.

### Teams

Dentro de una org, un **team** es un grupo de personas. Das permiso a un team sobre un
repo y todos sus miembros lo heredan (más fácil que persona por persona). Los teams
pueden **anidarse** (un team hijo hereda accesos del padre) y se mencionan con
`@org/equipo`.

## Niveles de permiso de un repositorio

De menos a más poder (muy preguntado — memoriza el orden):

| Rol | Puede… |
|-----|--------|
| **Read** | Ver y clonar el repo, abrir issues, comentar |
| **Triage** | Lo de Read + gestionar issues/PRs (labels, asignar, cerrar) sin escribir código |
| **Write** | Lo de Triage + **push** a ramas, crear PRs, correr Actions |
| **Maintain** | Lo de Write + gestionar algunos settings (no los sensibles) |
| **Admin** | Control total: settings, colaboradores, borrar el repo, branch protection |

En un repo personal el modelo es más simple: el dueño (admin) + **colaboradores**
invitados (que reciben, de hecho, acceso de escritura).

## Branch protection y rulesets

Para que `main` no reciba cambios sin control, aplicas reglas en
*Settings → Branches* (branch protection rules) o con los más nuevos **Rulesets**:

- **Require a pull request before merging** — prohíbe push directo a `main`.
- **Require approvals** — N revisiones aprobatorias (opcional: de **CODEOWNERS**).
- **Require status checks to pass** — el CI de [Actions](05-actions.md) debe estar verde.
- **Require branches up to date** — la rama debe estar al día con `main`.
- **Require conversation resolution** / **signed commits** / **linear history**.
- **Restrict who can push** / bloquear **force-push** y borrado de la rama.

Así se materializan las reglas que el [tema 03](03-pull-requests.md) aplicaba vía PR.

## Autenticación y acceso

- **2FA (autenticación en dos factores)** — segundo factor además de la contraseña (app
  TOTP, llave de seguridad, SMS). GitHub la **exige** ya a quienes contribuyen código.
- **Passkeys** — inicio de sesión sin contraseña (biometría/llave), opción moderna.
- **Personal Access Token (PAT)** — reemplaza la contraseña para Git sobre HTTPS y para
  la API. Dos tipos: **fine-grained** (permisos y repos acotados, recomendado) y **classic**.
- **SSH keys** — autenticación con par de claves ([tema 01](01-repos-y-proyecto.md)).
- **Deploy keys** — clave SSH con acceso a **un solo** repo (para servidores/CI).
- **GitHub Apps / OAuth Apps** — integraciones de terceros con permisos acotados.
- **SSO/SAML** — inicio de sesión corporativo (planes Enterprise).

Principio que cae: usa siempre el **menor privilegio** (tokens fine-grained, deploy keys
por repo) y **nunca** subas secretos al repo (para eso están los **Actions secrets**).

## Funciones de seguridad de GitHub

Agrupadas bajo *Security* del repo / **GitHub Advanced Security** en planes altos:

- **Dependabot**:
  - **Alerts** — te avisa si una dependencia tiene una vulnerabilidad conocida (CVE).
  - **Security updates** — abre PRs automáticos que suben la versión al parche.
  - **Version updates** — PRs periódicos para mantener dependencias al día (`dependabot.yml`).
- **Secret scanning** — detecta credenciales filtradas en el código (tokens, llaves API)
  y puede **bloquear el push** que las introduce (**push protection**).
- **Code scanning (CodeQL)** — análisis estático que busca vulnerabilidades en tu código
  y las reporta como alertas en la pestaña Security. Suele correr como un workflow de Actions.
- **Security advisories** — espacio **privado** para coordinar el arreglo de una
  vulnerabilidad antes de divulgarla; se publican como GHSA.
- **Dependency graph** — mapa de tus dependencias (base de Dependabot).
- **SECURITY.md** — documento que indica **cómo reportar** una vulnerabilidad de forma
  responsable.

## Visibilidad y privacidad (repaso)

- **Public / Private / Internal** ([tema 01](01-repos-y-proyecto.md)). Cambiar de private
  a public expone TODO el historial: cuidado con secretos ya commiteados.
- El **audit log** (en orgs) registra quién hizo qué: clave para administración.

## En el examen (GH-900)

- Orden de permisos: **Read < Triage < Write < Maintain < Admin**. Sabe qué desbloquea
  cada uno (Triage gestiona issues sin escribir código; Admin borra/configura).
- **Organizations** agrupan personas en **teams**; los teams heredan permisos y se anidan.
- **Branch protection** = exigir PR, approvals y checks antes de tocar `main`.
- **2FA** obligatoria para contribuidores; **PAT fine-grained** > classic (menor privilegio).
- **Dependabot** (dependencias vulnerables), **secret scanning** (credenciales filtradas),
  **code scanning/CodeQL** (bugs de seguridad en tu código). Sabe distinguirlos.
- **SECURITY.md** dice cómo reportar; **security advisories** coordinan el fix en privado.

## Conceptos clave

- **Organization / Team** — cuenta compartida y grupos con permisos heredados.
- **Niveles de permiso** — Read, Triage, Write, Maintain, Admin.
- **Branch protection / Ruleset** — reglas que blindan una rama.
- **2FA / PAT / SSH** — mecanismos de autenticación.
- **Dependabot / Secret scanning / CodeQL** — las tres patas de seguridad automatizada.

## Siguiente

→ [08 — Productos y ecosistema](08-productos-y-ecosistema.md)
