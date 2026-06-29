# -*- coding: utf-8 -*-
"""Scaffolding compartido del sitio FECAFEB (header/footer/flotantes/helpers)."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

# ---- Iconos ----
def ico(p, sw=2):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s">%s</svg>' % (sw, p)
I = {
 "chk": ico('<path d="m9 11 3 3 8-8"/>'),
 "lock": ico('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
 "arrow": ico('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 "bean": ico('<ellipse cx="12" cy="12" rx="7" ry="9"/><path d="M9 5c4 4 4 10 0 14"/>'),
 "users": ico('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
 "cap": ico('<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1 2.7 2.5 6 2.5s6-1.5 6-2.5v-5"/>'),
 "venus": ico('<circle cx="12" cy="8" r="5"/><path d="M12 13v8M9 18h6"/>'),
 "cup": ico('<path d="M4 8h13v4a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5Z"/><path d="M17 9h2a2 2 0 0 1 0 4h-2"/><path d="M6 2v2M10 2v2M14 2v2"/>'),
 "trophy": ico('<path d="M8 21h8M12 17v4M7 4h10v4a5 5 0 0 1-10 0Z"/><path d="M5 5H3v2a3 3 0 0 0 3 3M19 5h2v2a3 3 0 0 1-3 3"/>'),
 "shield": ico('<path d="M12 2 4 6v6c0 5 3.4 8.5 8 10 4.6-1.5 8-5 8-10V6Z"/><path d="m9 12 2 2 4-4"/>'),
 "globe": ico('<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>'),
 "share": ico('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5 8.6 10.5"/>'),
 "pin": ico('<path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/>'),
 "phone": ico('<path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3.08 5.18 2 2 0 0 1 5 3h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L9 11a16 16 0 0 0 4 4l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>'),
 "mail": ico('<path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/>'),
 "screen": ico('<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/>'),
 "leaf": ico('<path d="M11 20A7 7 0 0 1 4 13C4 8 9 3 20 3c0 11-5 16-9 16Z"/><path d="M4 21c2-6 6-9 11-10"/>'),
 "chart": ico('<path d="M3 3v18h18"/><path d="m7 14 3-3 3 3 5-6"/>'),
 "doc": ico('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>'),
 "dl": ico('<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/>'),
 "ph": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.6"/><path d="m21 15-5-5L5 21"/></svg>',
}
CHK = I["chk"]

# ---- Imágenes provisionales (origen boliviano/andino · reemplazables vía CMS) ----
PHOTOS = {
  "cherries":"https://images.unsplash.com/photo-1442550528053-c431ecb55509",
  "farm":"https://images.unsplash.com/photo-1429277096327-11ee3b761c93",
  "field":"https://images.unsplash.com/photo-1500423079914-b65af272b8db",
  "hands":"https://images.unsplash.com/photo-1559056199-641a0ac8b55e",
  "harvest":"https://images.unsplash.com/photo-1611854779393-1b2da9d400fe",
  "andes":"https://images.unsplash.com/photo-1531065208531-4036c0dba3ca",
  "bag":"https://images.unsplash.com/photo-1521302080334-4bebac2763a6",
  "green":"https://images.unsplash.com/photo-1518057111178-44a106bad636",
  "cup":"https://images.unsplash.com/photo-1461023058943-07fcbe16d735",
  "specialty":"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085",
  "roast":"https://images.unsplash.com/photo-1498804103079-a6351b050096",
  "shop":"https://images.unsplash.com/photo-1509042239860-f550ce710b93",
  "woman":"https://images.unsplash.com/photo-1530541930197-ff16ac917b0e",
  "people":"https://images.unsplash.com/photo-1530541930197-ff16ac917b0e",
}
def U(key, w=900):
    return PHOTOS[key] + ("?auto=format&fit=crop&w=%d&q=70" % w)
def img(key, alt, w=900, cls=""):
    return ('<div class="imgwrap %s" style="height:100%%"><img src="%s" alt="%s" loading="lazy" '
            'onerror="this.style.display=&quot;none&quot;"></div>') % (cls, U(key, w), alt)
def ph(label, cls=""):
    return '<div class="ph %s">%s<span>%s</span></div>' % (cls, I["ph"], label)

# ---- Navegación (orden solicitado por el directivo) ----
NAV = [
 ("index.html","Inicio",None),
 ("quienes-somos.html","Quiénes Somos",[("quienes-somos.html#mvv","Misión, Visión y Valores"),
     ("quienes-somos.html#directorio","Directorio"),("quienes-somos.html#fiscalizacion","Comité de Fiscalización"),
     ("comite-mujeres.html","Comité de Mujeres"),("quienes-somos.html#historia","Historia")]),
 ("afiliados.html","Afiliados",None),
 ("trazabilidad.html","Trazabilidad",None),
 ("servicios.html","Servicios",[("escuela-cafe.html","Escuela de Café"),("kullaka.html","Marca Kullaka"),
     ("taza-presidencial.html","Taza Presidencial"),("servicios.html","Asistencia técnica")]),
 ("publicaciones.html","Publicaciones",None),
 ("noticias.html","Noticias",None),
 ("contacto.html","Contacto",None),
]
NAVKEY={"index.html":"nav.home","quienes-somos.html":"nav.about","afiliados.html":"nav.affiliates","trazabilidad.html":"nav.trace","servicios.html":"nav.services","publicaciones.html":"nav.pubs","noticias.html":"nav.news","contacto.html":"nav.contact"}
def menu(active):
    chev='<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>'
    out=[]
    for href,label,sub in NAV:
        act=' is-active' if href==active else ''
        k=NAVKEY.get(href,"")
        if sub:
            subhtml=''.join('<li><a href="%s">%s</a></li>'%(h,t) for h,t in sub)
            out.append('<li class="has-sub%s"><a href="%s"><span data-i18n="%s">%s</span> %s</a><ul class="submenu">%s</ul></li>'%(act,href,k,label,chev,subhtml))
        else:
            out.append('<li class="%s"><a href="%s" data-i18n="%s">%s</a></li>'%(act.strip(),href,k,label))
    return ''.join(out)

SOC = ('<a href="https://www.facebook.com/CoordinadoraNacionaldeComercioJustodeBolivia/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8v-2.9h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6v1.9h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12Z"/></svg></a>'
       '<a href="https://x.com/CJustoBolivia" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2H21l-6.5 7.4L22 22h-6.8l-4.7-6.2L4.9 22H2l7-8L2 2h6.9l4.3 5.7L18.2 2Z"/></svg></a>'
       '<a href="https://www.youtube.com/channel/UCpIXQthmTVTEnk9LJOU46yg" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 0 0 1.8-1.8C23 15.2 23 12 23 12Zm-13 3V9l5 3-5 3Z"/></svg></a>')

def head(title, desc, extra_head=""):
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      '<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="index,follow">\n'
      '<meta property="og:type" content="website"><meta property="og:title" content="%s">\n'
      '<meta property="og:image" content="assets/img/logo-fecafeb.png">\n'
      '<link rel="icon" type="image/png" href="assets/img/favicon.png">\n'
      '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
      '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
      '<link rel="stylesheet" href="css/styles.css">\n<link rel="stylesheet" href="css/pages.css">\n' + extra_head + '</head>\n<body>') % (title, desc, title)

def header(active):
    return ('<div class="topbar"><div class="container topbar__row">'
      '<div class="topbar__info">'
      '<a class="topbar__tel topbar__lnk" href="tel:+59171537365">%s +591 71537365</a><a class="topbar__lnk" href="mailto:contacto@fecafeb.org">%s contacto@fecafeb.org</a><span>El Alto · La Paz · Bolivia</span></div>'
      '<div class="topbar__right"><div class="social" aria-label="Redes sociales">%s</div>'
      '<a href="#" class="topbar__plat">⮞ <span data-i18n="cta.platform2">Portal Institucional</span></a>'
      '<div class="lang" role="group" aria-label="Idioma"><button data-lang="es" class="is-active" type="button">ES</button><button data-lang="en" type="button">EN</button></div>'
      '</div></div></div>'
      '<header class="header"><div class="container nav">'
      '<a href="index.html" class="brand" aria-label="FECAFEB inicio"><img src="assets/img/logo-fecafeb.png" alt="FECAFEB"></a>'
      '<nav aria-label="Principal"><ul class="menu" id="menu">%s</ul></nav>'
      '<div class="nav__cta">'
      '<a href="escuela-cafe.html" class="btn btn--escuela btn--icon" title="Escuela de Café">%s<span data-i18n="cta.escuela">Escuela de Café</span></a>'
      '<a href="#" class="btn btn--portal btn--icon" title="Portal Institucional">%s<span data-i18n="cta.platform">Portal</span></a>'
      '<a href="afiliados.html" class="btn btn--gold" data-i18n="cta.register">Regístrese</a>'
      '<button class="nav__toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu"><span></span></button>'
      '</div></div></header>') % (I["phone"], I["mail"], SOC, menu(active), I["cap"], I["lock"])

def subhero(crumb, title, desc):
    return ('<section class="subhero"><div class="container"><div class="crumb"><a href="index.html">Inicio</a> / <span>%s</span></div>'
            '<h1>%s</h1><p class="lead">%s</p></div></section>') % (crumb, title, desc)

SIDERAIL = ('<div class="siderail" aria-label="Accesos rápidos">'
  '<a href="#" title="Portal Institucional">%s<span>Portal Institucional</span></a>'
  '<a class="is-gold" href="afiliados.html" title="Regístrese como exportador">%s<span>Regístrese como exportador</span></a>'
  '<a href="trazabilidad.html" title="Trazabilidad EUDR">%s<span>Trazabilidad EUDR</span></a>'
  '<a href="escuela-cafe.html" title="Escuela de Café">%s<span data-i18n="cta.escuela">Escuela de Café</span></a>'
  '</div>') % (I["lock"], I["arrow"], I["shield"], I["cap"])

FLOAT = SIDERAIL + ('\n<a class="fab fab--wa" href="https://wa.me/59171537365?text=Hola%20FECAFEB" target="_blank" rel="noopener" aria-label="WhatsApp">'
  '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M.06 24l1.7-6.2A11.9 11.9 0 1 1 12 24a11.9 11.9 0 0 1-5.7-1.45L.06 24Zm6.6-3.9.37.22a9.9 9.9 0 0 0 5 1.37 9.9 9.9 0 1 0-9.9-9.9 9.9 9.9 0 0 0 1.5 5.25l.24.38-1 3.65 3.8-.97Zm11.4-5.55c-.15-.25-.55-.4-1.15-.7s-1.77-.87-2.04-.97-.47-.15-.67.15-.77.97-.94 1.17-.35.22-.65.07a8.1 8.1 0 0 1-2.4-1.48 9 9 0 0 1-1.66-2.07c-.17-.3 0-.46.13-.6s.3-.35.45-.52a2 2 0 0 0 .3-.5.55.55 0 0 0 0-.52c-.07-.15-.67-1.62-.92-2.22s-.49-.5-.67-.51h-.57a1.1 1.1 0 0 0-.8.37 3.35 3.35 0 0 0-1.04 2.49 5.8 5.8 0 0 0 1.22 3.08 13.3 13.3 0 0 0 5.1 4.5c.71.3 1.27.49 1.7.63.72.23 1.37.2 1.88.12.58-.08 1.77-.72 2.02-1.42s.25-1.3.17-1.42Z"/></svg></a>'
  '<button class="fab fab--chat" aria-label="Abrir chat" aria-expanded="false"><span class="badge">1</span>'
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/><path d="M8 10h8M8 13h5"/></svg></button>'
  '<div class="chat" role="dialog" aria-label="Asistente FECAFEB">'
  '<div class="chat__head"><img src="assets/img/logo-fecafeb.png" alt="FECAFEB"><div><b>Asistente FECAFEB</b><small>En línea · responde al instante</small></div><button class="x" aria-label="Cerrar chat">&times;</button></div>'
  '<div class="chat__body" id="chatBody"></div>'
  '<div class="chat__chips"><button class="chip" data-q="exportar comprar cafe">¿Cómo comprar café?</button>'
  '<button class="chip" data-q="eudr trazabilidad">Trazabilidad EUDR</button>'
  '<button class="chip" data-q="afiliarme cooperativa">Afiliación</button>'
  '<button class="chip" data-q="escuela de cafe">Escuela de Café</button></div>'
  '<div class="chat__input"><input id="chatInput" type="text" placeholder="Escriba su consulta…" aria-label="Mensaje"><button id="chatSend" aria-label="Enviar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></button></div></div>'
  '')

def footer():
    return ('<footer class="footer"><div class="container"><div class="footer__grid">'
      '<div class="footer__brand"><img src="assets/img/logo-fecafeb.png" alt="FECAFEB">'
      '<p>Federación de Caficultores Exportadores de Bolivia. Ente rector del sector cafetalero boliviano desde 1991.</p>'
      '<div class="social" style="margin-top:1rem">%s</div></div>'
      '<div><h4>Federación</h4><ul><li><a href="quienes-somos.html">Quiénes Somos</a></li><li><a href="quienes-somos.html#directorio">Directorio</a></li>'
      '<li><a href="comite-mujeres.html">Comité de Mujeres</a></li><li><a href="afiliados.html">Afiliados</a></li></ul></div>'
      '<div><h4>Café & Mercados</h4><ul><li><a href="escuela-cafe.html">Escuela de Café</a></li><li><a href="kullaka.html">Marca Kullaka</a></li>'
      '<li><a href="taza-presidencial.html">Taza Presidencial</a></li><li><a href="trazabilidad.html">Trazabilidad EUDR</a></li></ul></div>'
      '<div><h4>Boletín semanal</h4><p style="font-size:.9rem;color:#9c8f80">Precios, clima y convocatorias del café boliviano.</p>'
      '<form class="footer__news" data-demo><input type="email" placeholder="Su correo" required aria-label="Correo"><button type="submit" aria-label="Suscribirse">→</button></form>'
      '<p style="font-size:.82rem;margin-top:1rem;color:#9c8f80">Av. Juan Pablo II 2974<br>El Alto · La Paz · Bolivia</p></div></div>'
      '<div class="footer__bottom"><span>© <span id="year">2026</span> FECAFEB · Federación de Caficultores Exportadores de Bolivia.</span>'
      '<span>Diseño y desarrollo: ERLANGER-SOFT · Cognitio SRL · Proyecto AAGIL — Ayuda en Acción</span></div></div></footer>') % SOC

def page(fname, active, title, desc, body, sub=None, extra_head="", extra_js=""):
    html = head(title, desc, extra_head) + header(active)
    if sub: html += subhero(*sub)
    html += "\n<main>\n" + body + "\n</main>\n" + footer() + FLOAT
    html += extra_js + '\n<script src="js/main.js"></script>\n</body></html>'
    open(os.path.join(BASE, fname), "w", encoding="utf-8").write(html)
    return len(html)

# ---- Bloques reutilizables ----
def hub():
    p=[("afiliados.html","users","Socios Afiliados","Cooperativas y productores"),
       ("escuela-cafe.html","cap","Escuela del Café","Formación y catación"),
       ("comite-mujeres.html","venus","Comité de Mujeres","Equidad y liderazgo"),
       ("kullaka.html","cup","Marca Kullaka","Vitrina comercial"),
       ("taza-presidencial.html","trophy","Taza Presidencial","Torneo nacional SCA"),
       ("trazabilidad.html","shield","Reglamento EUDR","Cumplimiento UE")]
    cards=''.join('<a class="pillar reveal" href="%s"><span class="pillar__ico">%s</span><b>%s</b><span>%s</span></a>'%(h,I[ic],t,d) for h,ic,t,d in p)
    return '<section class="hub"><div class="container"><div class="hub__grid">%s</div></div></section>'%cards

def access(intro):
    a=('<div class="access-card lvl-a reveal"><div class="access-card__top"><span class="access-card__ico">%s</span><span class="access-badge">General · Abierto</span></div>'
       '<h3>Información pública</h3><p>Datos de todas las afiliadas disponibles para cualquier visitante, sin registro.</p>'
       '<ul><li>%s Perfil institucional y del sector</li><li>%s Mapa general de regiones</li><li>%s Noticias y publicaciones abiertas</li></ul></div>') % (I["globe"],CHK,CHK,CHK)
    b=('<div class="access-card lvl-b reveal" data-delay="80"><div class="access-card__top"><span class="access-card__ico">%s</span><span class="access-badge">Compartido · con autorización</span></div>'
       '<h3>Datos compartidos</h3><p>Información que cada afiliado decide publicar en su perfil para vista pública.</p>'
       '<ul><li>%s Ficha de trazabilidad por lote</li><li>%s Perfil de cooperativa / productora</li><li>%s Muestras y certificaciones</li></ul>'
       '<div class="lockmsg">%s Requiere consentimiento del afiliado</div></div>') % (I["share"],CHK,CHK,CHK,I["lock"])
    c=('<div class="access-card lvl-c reveal" data-delay="160"><div class="access-card__top"><span class="access-card__ico">%s</span><span class="access-badge">Exclusivo · afiliados</span></div>'
       '<h3>Exclusivo para afiliados</h3><p>Datos sensibles, privados, gestionados a nivel de sistema en el Portal (usuario y rol).</p>'
       '<ul><li>%s Polígonos GeoJSON y DDS</li><li>%s Precios, subastas y reportes</li><li>%s Gestión de su organización</li></ul>'
       '<div class="lockmsg">%s Ingreso por Portal Institucional</div></div>') % (I["lock"],CHK,CHK,CHK,I["lock"])
    return ('<div class="head-block center"><span class="eyebrow">Niveles de acceso</span><h2>Tres niveles de desagregación</h2>'
            '<p class="lead">%s</p></div><div class="access">%s%s%s</div>') % (intro,a,b,c)

def _pin(x,y):
    return ('<g class="map-bo__pin" transform="translate(%d,%d)"><circle class="map-bo__pulse" r="6" style="transform-box:fill-box;transform-origin:center"/><circle r="5.5"/><circle class="core" r="2.4"/></g>')%(x,y)
MAP_BO = ('<div class="map-bo"><svg class="map-bo__svg" viewBox="0 0 320 320" role="img" aria-label="Mapa de Bolivia con regiones cafetaleras">'
  '<path class="map-bo__region is-active" d="M118 38 L172 52 L206 44 L236 72 L258 78 L270 110 L258 140 L276 166 L262 202 L240 216 L250 250 L224 278 L194 272 L172 288 L148 274 L134 246 L108 252 L78 236 L68 206 L50 186 L60 150 L46 120 L70 94 L96 88 L104 58 Z"/>'
  + _pin(96,128)+_pin(112,142)+_pin(150,170)+_pin(208,176) +
  '</svg><ul class="map-bo__legend">'
  '<li><span class="mk"></span><div><b>La Paz · Yungas</b><span>Núcleo cafetalero: ~96% de la producción nacional.</span></div></li>'
  '<li><span class="mk"></span><div><b>Caranavi</b><span>Principal municipio productor de café de altura.</span></div></li>'
  '<li><span class="mk"></span><div><b>Cochabamba</b><span>Organizaciones afiliadas del valle.</span></div></li>'
  '<li><span class="mk"></span><div><b>Santa Cruz</b><span>Afiliadas del oriente boliviano.</span></div></li>'
  '</ul></div>')

LEAFLET_CSS = '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">\n'
LEAFLET_JS  = '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>\n'

def brands_marquee():
    items=[("logo-fecafeb.png","FECAFEB institucional"),("logo-fecafeb-comercial.png","FECAFEB comercial 2024"),
           ("logo-kullaka.png","Café Kullaka"),("logo-comite-mujeres.jpg","Comité de Mujeres Cafetaleras"),
           ("logo-escuela-cafe.png","Escuela de Café")]
    one="".join('<div class="brand-logo"><img src="assets/img/%s" alt="%s" loading="lazy"></div>'%(f,a) for f,a in items)
    return ('<section class="section brands" style="padding:2.8rem 0"><div class="container">'
            '<p class="partners__title">Nuestras marcas e instancias</p>'
            '<div class="brand-marquee"><div class="brand-track">%s%s</div></div></div></section>') % (one+one, one+one)
