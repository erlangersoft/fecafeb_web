# FECAFEB — Sitio web institucional (plantilla)

Sitio multipágina, **mobile-first**, estático (HTML/CSS/JS), para la **Federación de Caficultores Exportadores de Bolivia (FECAFEB)**, orientado a compradores de la Unión Europea y a la familia cafetalera. Diseño y desarrollo: **ERLANGER-SOFT · Cognitio SRL** — Proyecto AAGIL (Ayuda en Acción).

> Estado: prototipo navegable con datos/imágenes **de ejemplo**. Pensado para conectarse luego a un **CMS autogestionable** y al **sistema/Portal** (datos de afiliados, trazabilidad, tienda y pedidos).

---

## 1. Cómo verlo y publicarlo
- **Ver localmente:** abrir `index.html` en el navegador (doble clic). Requiere conexión a internet para fuentes (Google Fonts), mapas (Leaflet + OpenStreetMap/CARTO) e imágenes de ejemplo (Unsplash). Sin conexión, degrada con elegancia.
- **Publicado (GitHub Pages):** subir el contenido de `fecafeb_web/` al repositorio. Las rutas son relativas, funciona tal cual.

## 2. Estructura de archivos
```
fecafeb_web/
├── index.html              Inicio (hero-carrusel, hub de 6 pilares, cifras, marcas, noticias)
├── quienes-somos.html      Misión/Visión/Valores · Instancias (Directorio, Fiscalización, Mujeres) · Historia
├── afiliados.html          Afiliación + registro de comprador · 3 niveles de acceso · mapa de zonas (Leaflet)
├── trazabilidad.html       EUDR · consulta pública de lote · 3 niveles de acceso
├── servicios.html          Servicios + accesos a Escuela, Kullaka, Taza
├── escuela-cafe.html       Escuela de Café (formación)
├── comite-mujeres.html     Comité de Mujeres + sinergia con Kullaka
├── kullaka.html            Marca Café Kullaka (vitrina comercial)
├── taza-presidencial.html  Torneo Nacional (SCA) + tabla de resultados
├── tienda.html             Catálogo + pedidos (carrito + registro de comprador)
├── publicaciones.html      Documentos · Blog del Café · Comunicados · Galería
├── noticias.html           Noticias + boletín semanal
├── contacto.html           Datos + formulario + mapa
├── nosotros.html / prensa.html / galeria.html   → redirecciones a las páginas nuevas
│
├── css/
│   ├── styles.css          Base: tokens, layout, cabecera, hero, footer, tarjetas, chatbot, responsivo
│   └── pages.css           Componentes: hub, niveles de acceso, mapa, consulta de lote, blog,
│                           carrusel de marcas, búsqueda, tienda/carrito, modal de compra, topbar acciones
├── js/
│   ├── main.js             Navegación, scroll, reveal, carrusel del hero, contadores, tabs, galería,
│   │                       formularios demo, i18n ES/EN, chatbot, WhatsApp
│   ├── maps.js             Mapa de zonas productoras (Leaflet) + panel de información
│   ├── trace.js            Consulta pública de trazabilidad por lote (+ polígono de parcela)
│   ├── search.js           Búsqueda global del sitio (overlay)
│   └── shop.js             Tienda, carrito, registro/login de comprador y pedido (demo, localStorage)
├── assets/img/             Logos (institucional, comercial 2024, Kullaka, Comité de Mujeres, Escuela) + favicon
│
├── parts.py                GENERADOR · scaffolding compartido (cabecera, pie, flotantes, helpers, nav)
├── build.py                GENERADOR · contenido de cada página → escribe los .html
└── README.md
```
> Nota: `build_pages.py` y `assets/img/new1..4` son restos antiguos sin uso (pueden borrarse manualmente).

## 3. Cómo regenerar las páginas
Las páginas HTML se generan con Python (no se editan a mano):
```
python3 build.py
```
`build.py` importa `parts.py`. Para cambiar cabecera, pie, menú o flotantes globales → editar `parts.py`. Para cambiar el contenido de una página → editar `build.py` y regenerar. Estilos y scripts (`css/`, `js/`) se editan directamente.

## 4. Identidad visual
Estilo limpio sobre **fondo blanco**, alto contraste, **café + dorado** con detalles crema. Tokens en `css/styles.css :root`:
- Café `#4E342E` · Espresso `#241712` · Dorado `#C8962E` / `#F0E0BE` · Crema `#F4ECDD`
- Títulos `#241C17` · Texto `#574C44` · Fondos `#FFFFFF` / `#F6F4F0` / `#FBF8F2`
- Tipografía: **Fraunces** (títulos) + **Inter** (texto). Bandas oscuras puntuales en espresso para dar ritmo.

## 5. Navegación (orden aprobado por el directivo)
Inicio · Quiénes Somos · Afiliados · Trazabilidad · Servicios · Publicaciones · Noticias · Contacto.
- **Barra superior (café):** teléfono (clic-para-llamar) y correo, redes sociales animadas, switch **ES/EN**, y a su derecha los accesos **Escuela de Café**, **Portal** (candado) y **Regístrese**.
- **Menú principal:** logo + navegación + **búsqueda** (lupa) y **carrito**. Submenús en Quiénes Somos (Directorio, Fiscalización, Comité de Mujeres, Historia) y Servicios (Escuela, Kullaka, Taza, Tienda, Asistencia técnica).
- **Riel lateral fijo** (desktop) con accesos rápidos y tooltip deslizante.

## 6. Funcionalidades implementadas (demo)
- **Hero con carrusel** de imágenes (auto-rotación, flechas, puntos) y **contadores animados**.
- **Hub Lineal**: 6 pilares de acceso directo (Afiliados, Escuela, Comité de Mujeres, Kullaka, Taza Presidencial, EUDR).
- **Carrusel de marcas/instancias** propio (logos en movimiento, efecto al hover).
- **Tres niveles de acceso** (Afiliados y Trazabilidad): público abierto / compartido con autorización / exclusivo de afiliado (se gestionará a nivel de sistema).
- **Mapa de zonas productoras** (Leaflet + OpenStreetMap/CARTO) con marcadores y panel de información.
- **Consulta pública de trazabilidad** por código de lote: ficha de origen, foto del producto, **polígono de la parcela** en mapa, cumplimiento EUDR y descarga de certificados (demo). Lotes de prueba: `LOT-000123`, `LOT-000456`, `LOT-000789`.
- **Tienda y pedidos**: catálogo (Kullaka + café verde de exportación), **carrito** lateral, **registro/login de comprador** (cuenta queda "en revisión para alta") y confirmación de pedido con N°. Persistencia local.
- **Búsqueda global** (overlay; atajos `/` o `Ctrl/⌘+K`).
- **Chatbot** simulado con indicador de escritura, **botón flotante de WhatsApp**, **i18n ES/EN** (nav, hero y CTAs), animaciones al hacer scroll.

## 7. Datos y medios de ejemplo (a reemplazar con CMS/sistema)
- **Imágenes**: fotos de Unsplash (referenciales, contexto andino/cafetalero). Reemplazar por fotografías propias de FECAFEB.
- **Productos, precios, lotes, polígonos, resultados de la Taza, noticias y documentos**: contenido demo.
- **Pedidos y registro de compradores**: simulados en `localStorage`; se conectarán a backend/CRM y al alta real de clientes.

## 8. Pendiente para la fase de sistema/CMS
- CMS autogestionable (noticias, blog, documentos, productos, galería) sin depender de programadores.
- Portal Institucional (login real con roles) y los 3 niveles de acceso a nivel de datos.
- Trazabilidad real: carga de polígonos **GeoJSON** por el afiliado, DDS y **TRACES NT**; mapa de intervención por parcela.
- Tienda real: pasarela de pago/cotización, alta y aprobación de compradores, gestión de pedidos.
- Escuela de Café: preinscripción, sílabos y pago en línea.
- Boletín (Mailchimp/Brevo). Internacionalización EN definitiva (i18next o LibreTranslate) con URLs `/en/` para SEO.
- Reemplazo de imágenes y textos definitivos; sitemap.xml y robots.txt.

---
© FECAFEB · Plantilla desarrollada por ERLANGER-SOFT · Cognitio SRL.
