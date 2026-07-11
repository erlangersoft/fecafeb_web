# Contexto del proyecto — Sitio web FECAFEB

**Instrucción para Claude: lee este archivo completo ANTES de tocar cualquier archivo o de revisar la Drive sincronizada.** Evita recorrer la Drive o los .md de nuevo salvo que el ajuste lo requiera explícitamente.

## Directorio de trabajo (único, no crear nada fuera de aquí)

- Carpeta del sitio (repo git real, con remoto GitHub): `fecafeb_web/` — dentro de la carpeta seleccionada por el usuario en Cowork.
- Generador estático: `fecafeb_web/build.py` (contenido de cada página vía f-strings) + `fecafeb_web/parts.py` (scaffolding compartido: `head()`, `header()`, `subhero()`, `footer()`, `page()`, `board()`, `img()`, diccionario `PHOTOS`, diccionario de iconos `I`).
- Rebuild (regenera todos los .html a partir de build.py/parts.py):
  ```
  cd fecafeb_web && PYTHONDONTWRITEBYTECODE=1 PYTHONPYCACHEPREFIX=/tmp/pyc_fresh_X python3 build.py
  ```
  (incrementar X cada vez; el mount reutiliza .pyc viejos si no se cambia el prefijo).
- Cache-buster: `parts.py` línea ~105 tiene `?v=20260710X` en los `<link>` de `styles.css`/`pages.css`. Subir la letra (a→b→c…) cada vez que se edite CSS/JS, antes de rebuild.

**Base de conocimiento preprocesada (fuentes verificadas, NO reprocesar la Drive salvo que falte algo):** `fecafeb_md/*.md`, un nivel arriba de `fecafeb_web/`. Contiene actas, estatutos, listas de afiliados, notas de ajustes ya hechas, etc. Todo dato/cifra/nombre usado en el sitio debe salir de aquí o de assets reales ya colocados — nunca inventar cifras, logos ni afiliaciones no confirmadas.

**Archivo a IGNORAR / no es parte del sitio:** `bosque_de_altura_preview.html` en la raíz de la carpeta de trabajo — es un artefacto de un error temprano en el proyecto (página inventada que no correspondía). No editarlo, no referenciarlo, no recrearlo. El sitio real son solo los `.html` dentro de `fecafeb_web/`.

## Convenciones establecidas

- Motion: clases genéricas `.reveal`/`.reveal.in` (scroll-reveal vía IntersectionObserver en `main.js`, con stagger automático). Contadores animados: atributo `data-count` (+ `data-sep` opcional).
- Nunca poner iconitos genéricos (SVG) en tabs ni en tarjetas de Misión/Valores/Proyectos — a los caficultores/usuarios no les gusta esa estética. Se prefieren fotos reales, numeración tipográfica o acentos de línea dorada.
- No duplicar la misma foto dos veces dentro de una misma página (sí se puede repetir entre páginas distintas).
- Git: este repo sufre un bug recurrente del mount — `.git/index.lock` queda huérfano tras casi cualquier operación y bloquea el siguiente `git add`/`commit` con "File exists". Se resuelve moviendo el archivo (no borrando): `mv .git/index.lock _gitjunk/index.lock.$(date +%s)`. Si `git add -A` no deja stageado `parts.py` (ha pasado varias veces), usar plumbing directo: `git hash-object -w parts.py` + `git update-index --cacheinfo 100644,<hash>,parts.py`, y verificar con `git diff --cached --stat -- parts.py` antes de commitear.
- Verificación estándar tras cada edición de `build.py`/`css/styles.css`/`js/main.js` (el mount trunca escrituras con cierta frecuencia): revisar `ast.parse()` (py) / conteo de `{`/`}` (css) / `node -c` (js), barrido de bytes nulos, y `diff` contra el HEAD de git antes de dar la edición por buena.

## Estado actual (última sesión de ajustes, página Comité de Mujeres)

- Hero: slider de 2 diapositivas (Comité de Mujeres ⇄ Café Kullaka, `feature-hero`/`data-hslider`), cruza sola cada 6s.
- Misión/Valores: tarjetas `mv-card` sin iconos, solo borde dorado y subrayado bajo el título.
- Proyectos: carrusel de fotos reales (`proj-carousel`/`data-carousel`), 5 slides con texto superpuesto.
- Momentos de la Cumbre: marquee infinito.
- El widget de "cifras" (276 mujeres, 21 orgs, etc.) se intentó varias veces (banda ancha → burbuja flotante sobre el hero → burbuja en el subhero) y finalmente **se quitó por completo** a pedido del usuario tras no lograr un resultado legible — no reintroducirlo salvo pedido explícito.
- Último commit local antes de handoff: revisar `git log --oneline -5` al empezar.

## Cómo continuar en una conversación nueva

Al abrir un chat nuevo dentro del proyecto FECAFEB, el primer mensaje debería ser algo como:
> "Lee fecafeb_web/CONTEXTO_PROYECTO.md y sigue ajustando [lo que corresponda]."

Esto evita que Claude vuelva a explorar la Drive, recree páginas erróneas, o pierda las convenciones ya acordadas.
