# FECAFEB — Plantilla de sitio web institucional

Base profesional, responsiva y de vanguardia para la Federación de Caficultores Exportadores de Bolivia. Pensada como **plantilla de diseño del sistema completo** (orientada a compradores de la UE que buscan proveedores latinos de café).

## Estructura (multipágina · HTML / CSS / JS separados)

```
fecafeb_web/
├── index.html              # Home (hero, cifras, teasers de servicios/trazabilidad/prensa)
├── nosotros.html           # Misión/Visión/Valores + Historia + Directorio
├── afiliados.html          # Afiliación + registro de comprador/exportador + red
├── servicios.html          # Servicios + Escuela de Café
├── trazabilidad.html       # Proceso EUDR detallado
├── prensa.html             # Noticias
├── galeria.html            # Galería (placeholders de foto)
├── contacto.html           # Datos + formulario + mapa
├── css/styles.css          # Sistema de diseño (tokens, layout, responsivo)
├── js/main.js              # nav, tabs, i18n, chatbot, WhatsApp, reveal, lightbox
├── build_pages.py          # Generador (header/footer compartidos) — re-ejecutar para regenerar
├── assets/img/             # logo-fecafeb.png · logo-escuela-cafe.png (fondo removido) · favicon.png
└── README.md
```

Abrir: doble clic en `index.html` (no requiere servidor). Para regenerar todas las páginas tras editar el generador: `python3 build_pages.py`. Para fuentes/CDN se necesita conexión; sin ella degrada a fuentes del sistema.

## Imágenes
Donde irá una fotografía hay un **placeholder con ícono** (`.ph`). Reemplácelo por `<img src="...">` real en galería, prensa, "Nosotros", "Escuela de Café", mapas y trazabilidad.

## Identidad visual (v2 · blanco / moderno)
Estilo limpio tipo plantilla profesional: **fondo blanco**, mucho aire, tarjetas suaves y acentos café + verde. Variables CSS en `:root`:

- Fondo `#ffffff` · Sección alterna `#F7F8F6` · Crema `#FBF8F3`
- Café (marca/texto fuerte) `#4E342E` · Verde acento (orgánico/EUDR) `#2F7D57`
- Oro (detalles) `#C8962E` · Títulos `#23302A` · Texto `#51605A`
- Bandas de acento en **verde profundo** (`section--accent`) para dar ritmo sin saturar
- Tipografía: **Fraunces** (títulos) + **Inter** (texto)

> El fondo turquesa del logo de la Escuela de Café fue eliminado (ahora transparente) para que luzca pulcro sobre blanco.

Cambiar toda la apariencia = editar las variables en `css/styles.css`.

## Secciones / navegación
Inicio (hero) · Nosotros (Misión/Visión/Valores/Historia en pestañas) · Cifras · Servicios (+ Escuela de Café) · Afiliados (afiliación + registro de exportador/comprador) · Trazabilidad EUDR · Prensa · Galería · Contacto · Footer · Plataforma institucional · Redes sociales · **Chatbot** + **botón flotante de WhatsApp**.

## Funcionalidades JS
- Menú móvil, header con sombra al scroll y resaltado de sección activa.
- Animaciones de aparición (IntersectionObserver) y pestañas de "Nosotros".
- Galería con lightbox.
- Conmutador de idioma **ES/EN** (diccionario en `main.js → DICT`, atributos `data-i18n`).
- Mini chatbot por reglas locales (sin servicios externos) y botón de WhatsApp.
- Formularios en modo demo (sin backend).

## Personalización rápida (editar en `js/main.js → CONFIG`)
```js
whatsapp: "59171537365",            // número real (sin +)
email: "fecafebfinanzas@gmail.com",
platformUrl: "#plataforma"          // URL real del sistema institucional
```
- **Fotos:** reemplazar los bloques de degradado de `.gallery`, `.news__cover` y `.feature__media` por imágenes reales.
- **Idiomas:** ampliar el diccionario `DICT` y añadir `data-i18n="clave"` a más elementos.
- **Misión/Visión:** la web usa la versión del PEI 2023–2027. Confirmar con FECAFEB el enunciado oficial.

## Pendientes para fase de desarrollo
Conectar formularios a backend/CRM · login real de la plataforma · CMS para Prensa/Galería · sitemap.xml y robots.txt · imágenes reales optimizadas (WebP) · integración del chatbot con la plataforma de trazabilidad.

---
Diseño y desarrollo: **ERLANGER-SOFT · Cognitio SRL** — Proyecto AAGIL (Ayuda en Acción).
