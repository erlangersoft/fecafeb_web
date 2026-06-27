# -*- coding: utf-8 -*-
"""Generador estático del sitio FECAFEB (multipágina). Comparte header/footer/flotantes."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

# ---- Iconos reutilizables ----
PH_ICO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.6"/><path d="m21 15-5-5L5 21"/></svg>'
CHK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 11 3 3 8-8"/></svg>'

def ph(label, cls=""):
    return f'<div class="ph {cls}">{PH_ICO}<span>{label}</span></div>'

SOC = '''<a href="https://www.facebook.com/CoordinadoraNacionaldeComercioJustodeBolivia/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8v-2.9h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6v1.9h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12Z"/></svg></a>
<a href="https://x.com/CJustoBolivia" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2H21l-6.5 7.4L22 22h-6.8l-4.7-6.2L4.9 22H2l7-8L2 2h6.9l4.3 5.7L18.2 2Z"/></svg></a>
<a href="https://www.youtube.com/channel/UCpIXQthmTVTEnk9LJOU46yg" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 0 0 1.8-1.8C23 15.2 23 12 23 12Zm-13 3V9l5 3-5 3Z"/></svg></a>'''

NAV_ITEMS = [
    ("index.html","nav.home","Inicio",None),
    ("nosotros.html","nav.about","Nosotros",[("nosotros.html#mvv","Misión, Visión y Valores"),("nosotros.html#historia","Historia"),("nosotros.html#directorio","Directorio"),("index.html#cifras","Cifras del sector")]),
    ("afiliados.html","nav.affiliates","Afiliados",None),
    ("servicios.html","nav.services","Servicios",[("servicios.html#escuela","Escuela de Café"),("servicios.html","Asistencia técnica"),("servicios.html","Comercialización"),("trazabilidad.html","Trazabilidad EUDR")]),
    ("trazabilidad.html","nav.trace","Trazabilidad",None),
    ("prensa.html","nav.press","Prensa",None),
    ("galeria.html","nav.gallery","Galería",None),
    ("contacto.html","nav.contact","Contacto",None),
]

def menu(active):
    out=[]
    for href,key,label,sub in NAV_ITEMS:
        cls=' class="is-active"' if href==active else ''
        if sub:
            chev='<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>'
            subhtml=''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in sub)
            li=f'<li class="has-sub{ "" if href!=active else " is-active"}"><a href="{href}" data-i18n="{key}">{label} {chev}</a><ul class="submenu">{subhtml}</ul></li>'
        else:
            li=f'<li{cls}><a href="{href}" data-i18n="{key}">{label}</a></li>'
        out.append(li)
    return ''.join(out)

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo-fecafeb.png">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>'''

def header(active):
    return f'''
<div class="topbar"><div class="container topbar__row">
  <div class="topbar__info">
    <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3.08 5.18 2 2 0 0 1 5 3h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L9 11a16 16 0 0 0 4 4l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg> +591 71537365</span>
    <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg> fecafebfinanzas@gmail.com</span>
    <span>El Alto · La Paz · Bolivia</span>
  </div>
  <div class="topbar__right">
    <div class="social" aria-label="Redes sociales">{SOC}</div>
    <a href="#" class="topbar__plat">⮞ Plataforma institucional</a>
    <div class="lang" role="group" aria-label="Idioma"><button data-lang="es" class="is-active" type="button">ES</button><button data-lang="en" type="button">EN</button></div>
  </div>
</div></div>
<header class="header"><div class="container nav">
  <a href="index.html" class="brand" aria-label="FECAFEB inicio"><img src="assets/img/logo-fecafeb.png" alt="FECAFEB"></a>
  <nav aria-label="Principal"><ul class="menu" id="menu">{menu(active)}</ul></nav>
  <div class="nav__cta">
    <a href="#" class="btn btn--ghost" data-i18n="cta.platform">Plataforma</a>
    <a href="afiliados.html" class="btn" data-i18n="cta.export">Regístrese como exportador</a>
    <button class="nav__toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</div></header>'''

def subhero(crumb, title, desc):
    return f'''<section class="subhero"><div class="container">
  <div class="crumb"><a href="index.html">Inicio</a> / <span>{crumb}</span></div>
  <h1>{title}</h1><p class="lead">{desc}</p>
</div></section>'''

FLOAT = '''
<a class="fab fab--wa" href="https://wa.me/59171537365?text=Hola%20FECAFEB%2C%20deseo%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20caf%C3%A9%20boliviano." target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M.06 24l1.7-6.2A11.9 11.9 0 1 1 12 24a11.9 11.9 0 0 1-5.7-1.45L.06 24Zm6.6-3.9.37.22a9.9 9.9 0 0 0 5 1.37 9.9 9.9 0 1 0-9.9-9.9 9.9 9.9 0 0 0 1.5 5.25l.24.38-1 3.65 3.8-.97Zm11.4-5.55c-.15-.25-.55-.4-1.15-.7s-1.77-.87-2.04-.97-.47-.15-.67.15-.77.97-.94 1.17-.35.22-.65.07a8.1 8.1 0 0 1-2.4-1.48 9 9 0 0 1-1.66-2.07c-.17-.3 0-.46.13-.6s.3-.35.45-.52a2 2 0 0 0 .3-.5.55.55 0 0 0 0-.52c-.07-.15-.67-1.62-.92-2.22s-.49-.5-.67-.51h-.57a1.1 1.1 0 0 0-.8.37 3.35 3.35 0 0 0-1.04 2.49 5.8 5.8 0 0 0 1.22 3.08 13.3 13.3 0 0 0 5.1 4.5c.71.3 1.27.49 1.7.63.72.23 1.37.2 1.88.12.58-.08 1.77-.72 2.02-1.42s.25-1.3.17-1.42Z"/></svg>
</a>
<button class="fab fab--chat" aria-label="Abrir chat" aria-expanded="false"><span class="badge">1</span>
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/><path d="M8 10h8M8 13h5"/></svg>
</button>
<div class="chat" role="dialog" aria-label="Asistente FECAFEB">
  <div class="chat__head"><img src="assets/img/logo-fecafeb.png" alt="FECAFEB"><div><b>Asistente FECAFEB</b><small>En línea · responde al instante</small></div><button class="x" aria-label="Cerrar chat">&times;</button></div>
  <div class="chat__body" id="chatBody"></div>
  <div class="chat__chips">
    <button class="chip" data-q="exportar comprar cafe">¿Cómo comprar café?</button>
    <button class="chip" data-q="eudr trazabilidad">Trazabilidad EUDR</button>
    <button class="chip" data-q="afiliarme cooperativa">Afiliación</button>
    <button class="chip" data-q="escuela de cafe">Escuela de Café</button>
  </div>
  <div class="chat__input"><input id="chatInput" type="text" placeholder="Escriba su consulta…" aria-label="Mensaje"><button id="chatSend" aria-label="Enviar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></button></div>
</div>
<script src="js/main.js"></script>
</body></html>'''

def footer():
    return f'''
<footer class="footer"><div class="container">
  <div class="footer__grid">
    <div class="footer__brand">
      <img src="assets/img/logo-fecafeb.png" alt="FECAFEB">
      <p>Federación de Caficultores Exportadores de Bolivia. Ente rector del sector cafetalero boliviano desde 1991.</p>
      <div class="social" style="margin-top:1rem">{SOC}</div>
    </div>
    <div><h4>Navegación</h4><ul>
      <li><a href="nosotros.html">Nosotros</a></li><li><a href="afiliados.html">Afiliados</a></li>
      <li><a href="servicios.html">Servicios</a></li><li><a href="trazabilidad.html">Trazabilidad</a></li>
      <li><a href="galeria.html">Galería</a></li></ul></div>
    <div><h4>Recursos</h4><ul>
      <li><a href="prensa.html">Prensa</a></li><li><a href="servicios.html#escuela">Escuela de Café</a></li>
      <li><a href="afiliados.html">Regístrese como exportador</a></li><li><a href="#">Plataforma institucional</a></li>
      <li><a href="contacto.html">Contacto</a></li></ul></div>
    <div><h4>Boletín</h4><p style="font-size:.9rem;color:#9c8f80">Novedades del café boliviano y oportunidades de exportación.</p>
      <form class="footer__news" data-demo><input type="email" placeholder="Su correo" required aria-label="Correo"><button type="submit" aria-label="Suscribirse">→</button></form>
      <p style="font-size:.82rem;margin-top:1rem;color:#9c8f80">Av. Juan Pablo II 2974<br>El Alto · La Paz · Bolivia</p></div>
  </div>
  <div class="footer__bottom"><span>© <span id="year">2026</span> FECAFEB · Federación de Caficultores Exportadores de Bolivia.</span>
  <span>Diseño y desarrollo: ERLANGER-SOFT · Cognitio SRL · Proyecto AAGIL — Ayuda en Acción</span></div>
</div></footer>'''

def page(fname, active, title, desc, body, with_subhero=None):
    html = head(title, desc) + header(active)
    if with_subhero:
        html += subhero(*with_subhero)
    html += "\n<main>\n" + body + "\n</main>\n" + footer() + FLOAT
    open(os.path.join(BASE, fname), "w", encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")

# ================= CONTENIDO =================
SVG = {
 "leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 20A7 7 0 0 1 4 13C4 8 9 3 20 3c0 11-5 16-9 16Z"/><path d="M4 21c2-6 6-9 11-10"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m7 14 3-3 3 3 5-6"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.4 8.5 8 10 4.6-1.5 8-5 8-10V6Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "bean":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="12" rx="7" ry="9"/><path d="M9 5c4 4 4 10 0 14"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3.08 5.18 2 2 0 0 1 5 3h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L9 11a16 16 0 0 0 4 4l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg>',
 "screen":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg>',
}

def services_cards():
    items=[("leaf","Asistencia técnica productiva","Acompañamiento en campo para mejorar rendimientos, calidad de taza y manejo agroforestal sostenible."),
           ("chart","Comercialización &amp; exportación","Vinculación con compradores internacionales, café de stock y promoción de la denominación de origen boliviana."),
           ("shield","Sanidad vegetal e innovación","Manejo integrado de plagas, bioinsumos y transferencia tecnológica para una caficultura resiliente al clima.")]
    return ''.join(f'<article class="card reveal"><div class="card__ico">{SVG[i]}</div><h3>{t}</h3><p>{d}</p></article>' for i,t,d in items)

def escuela_feature():
    return f'''<div class="feature">
  <div class="feature__media reveal"><img src="assets/img/logo-escuela-cafe.png" alt="Escuela de Café FECAFEB"></div>
  <div class="feature__content reveal" data-delay="120">
    <span class="tag tag--gold">Programa insignia</span>
    <h2>Escuela de Café</h2>
    <p class="lead">Formación integral para productores, jóvenes y mujeres cafetaleras: del cultivo a la taza, con enfoque en calidad, catación y gestión.</p>
    <ul>
      <li>{CHK} Producción orgánica y agroforestería</li>
      <li>{CHK} Control de calidad, catación y poscosecha</li>
      <li>{CHK} Administración y gestión de la cooperativa</li>
      <li>{CHK} Liderazgo de mujeres y jóvenes cafetaleros</li>
    </ul>
    <a href="contacto.html" class="btn">Quiero capacitarme</a>
  </div></div>'''

def trace_steps():
    s=[("Geolocalización","Polígonos de cada parcela en GeoJSON / WGS84, georreferenciados en campo."),
       ("Registro del lote","Productor, finca, fecha de cosecha y cadena de custodia en la plataforma institucional."),
       ("Diligencia debida","Generación de la Declaración (DDS) y verificación contra mapas de deforestación."),
       ("TRACES NT","Presentación ante el sistema de la UE para el ingreso conforme del café.")]
    return ''.join(f'<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in s)

def news_items():
    data=[("Eventos","Junio 2026","FECAFEB impulsa la trazabilidad EUDR para sus afiliadas","Nueva plataforma digital para sistematizar datos de productores y parcelas."),
          ("Calidad","Mayo 2026","Taza de Excelencia: el café boliviano brilla en el exterior","Productores de los Yungas destacan por su café de especialidad."),
          ("Escuela de Café","Abril 2026","Nueva generación de catadores se forma en la Escuela de Café","Jóvenes y mujeres lideran la mejora de la calidad en sus cooperativas."),
          ("Comercio","Marzo 2026","Ronda de negocios con compradores europeos","Encuentro comercial para conectar oferta boliviana con la demanda de la UE."),
          ("Sostenibilidad","Febrero 2026","Agroforestería: café que protege el bosque","Modelo productivo alineado a la normativa de deforestación de la UE."),
          ("Institucional","Enero 2026","FECAFEB presenta su Plan Estratégico 2023–2027","Hoja de ruta hacia la sostenibilidad financiera e institucional.")]
    return ''.join(f'''<article class="news__item reveal"><div class="news__cover"><span class="badge">{c}</span>{ph("Fotografía de la noticia")}</div>
      <div class="news__body"><time>{d}</time><h3>{t}</h3><p>{x}</p><a href="#">Leer más →</a></div></article>''' for c,d,t,x in data)

def gallery_items():
    g=[("Cafetales de los Yungas","tall"),("Cosecha selectiva",""),("Beneficiado y secado",""),("Catación y calidad",""),
       ("Familias cafetaleras",""),("Escuela de Café","tall"),("Exportación de café verde",""),("Ferias internacionales","")]
    return ''.join(f'<figure class="{c}">{ph(t)}</figure>' for t,c in g)

def board():
    groups=[("Directorio Ejecutivo Nacional",[("Hugo Poma Maqui","Presidente",""),("Jimmy Gustavo Chávez Quijhua","Tesorero / Coordinador",""),("Juan Pablo Rojas Marino","Secretario","")]),
            ("Comité de Fiscalización",[("José Cori Quispe","Presidente","Cooperativa Mejillones"),("Ever Villca","Secretario","Cooperativa Villa Oriente")]),
            ("Comité de Mujeres",[("Yola Condori Álvarez","Presidenta","Cooperativa Antofagasta"),("Mari Luz Kalla Osco","Tesorera","Cooperativa San Juan"),("Elsa Calle","Secretaria","Cooperativa CENAPROC")])]
    out=[]
    for gname,people in groups:
        cards=''
        for name,role,org in people:
            ini=''.join(w[0] for w in name.split()[:2]).upper()
            orgh=f'<div class="org">{org}</div>' if org else ''
            cards+=f'<div class="person reveal"><div class="av">{ini}</div><b>{name}</b><div class="role">{role}</div>{orgh}</div>'
        out.append(f'<div class="board-group"><h3>{gname}</h3><div class="board">{cards}</div></div>')
    return ''.join(out)

# ---------- HOME ----------
home_body = f'''
<section class="hero" id="home"><div class="hero__beans" aria-hidden="true"></div>
<div class="container hero__inner">
  <div class="hero__content">
    <span class="hero__badge"><span class="dot"></span><span data-i18n="hero.badge">Café orgánico y de especialidad de Bolivia</span></span>
    <h1 data-i18n="hero.title">El café boliviano que <em>Europa</em> busca, con trazabilidad garantizada</h1>
    <p class="hero__lead" data-i18n="hero.lead">Federación de Caficultores Exportadores de Bolivia: 17.500 familias productoras, 42 organizaciones y trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).</p>
    <div class="hero__actions">
      <a href="afiliados.html" class="btn btn--gold btn--lg" data-i18n="hero.cta1">Importar nuestro café</a>
      <a href="nosotros.html" class="btn btn--ghost btn--lg" data-i18n="hero.cta2">Conocer la Federación</a>
    </div>
    <div class="hero__stats">
      <div><div class="num">17.500</div><div class="lbl">Familias cafetaleras</div></div>
      <div><div class="num">42</div><div class="lbl">Organizaciones afiliadas</div></div>
      <div><div class="num">1991</div><div class="lbl">Año de fundación</div></div>
      <div><div class="num">EUDR</div><div class="lbl">Trazabilidad UE 2023/1115</div></div>
    </div>
  </div>
  <aside class="hero__card reveal"><span class="ribbon">EUDR ready</span><img src="assets/img/logo-fecafeb.png" alt="Sello FECAFEB"><div class="cap">Café de calidad · Origen Yungas, Bolivia</div></aside>
</div></section>

<div class="trust"><div class="container trust__row">
  <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 11 3 3 8-8"/><path d="M21 12a9 9 0 1 1-6.2-8.5"/></svg> Comercio Justo · CNCJ-Bolivia</span>
  <span>{SVG["shield"]} Conformidad EUDR (UE 2023/1115)</span>
  <span>{SVG["globe"]} Exportación a Europa, EE.UU. y Asia</span>
  <span>{SVG["bean"]} Orgánico &amp; de especialidad</span>
</div></div>

<section class="section"><div class="container about">
  <div class="about__media reveal"><div class="frame">{ph("Fotografía: productores / cafetal de los Yungas")}</div><span class="pill">Ente rector del café boliviano</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Nosotros</span>
    <h2>Una federación, miles de familias detrás de cada grano</h2>
    <p class="lead">Desde 1991, FECAFEB representa, articula y fortalece a las organizaciones de productores de café de Bolivia, impulsando un sector competitivo, sostenible y con identidad.</p>
    <ul class="values" style="margin:1.4rem 0 1.6rem">
      <li>{CHK} 17.500 familias productoras</li><li>{CHK} 42 organizaciones afiliadas</li>
      <li>{CHK} Café orgánico y de especialidad</li><li>{CHK} Trazabilidad lista para la UE</li>
    </ul>
    <a href="nosotros.html" class="btn">Conocer más</a>
  </div>
</div></section>

<section class="section section--accent" id="cifras"><div class="container">
  <div class="head-block center"><span class="eyebrow">El sector en cifras</span><h2>Respaldo productivo y alcance nacional</h2></div>
  <div class="metrics">
    <div class="metric reveal"><div class="num">17.500</div><div class="lbl">Familias productoras</div></div>
    <div class="metric reveal" data-delay="80"><div class="num">42</div><div class="lbl">Cooperativas, asociaciones y Coracas</div></div>
    <div class="metric reveal" data-delay="160"><div class="num">3</div><div class="lbl">Departamentos: La Paz, Santa Cruz, Cochabamba</div></div>
    <div class="metric reveal" data-delay="240"><div class="num">96%</div><div class="lbl">Producción en La Paz (Yungas / Caranavi)</div></div>
  </div>
</div></section>

<section class="section section--tint"><div class="container">
  <div class="head-block center"><span class="eyebrow">Servicios</span><h2>Servicios para la familia cafetalera y para el comprador</h2>
  <p class="lead">Acompañamos al productor desde la parcela hasta el contrato de exportación.</p></div>
  <div class="grid grid-3" style="margin-bottom:1rem">{services_cards()}</div>
  <div class="center" style="margin-top:2rem"><a href="servicios.html" class="btn btn--ghost">Ver todos los servicios</a></div>
</div></section>

<section class="section section--accent"><div class="container">
  <div class="head-block"><span class="eyebrow">Trazabilidad EUDR</span><h2>Del cafetal a Europa, grano por grano</h2>
  <p class="lead">Cumplimos el Reglamento UE 2023/1115. Cada lote es geolocalizado y verificable.</p></div>
  <div class="steps">{trace_steps()}</div>
  <div class="eudr-note reveal">{SVG["shield"]}<p><b>Acceso preferente al mercado europeo.</b> Nuestra plataforma deja lista la documentación de diligencia debida, reduciendo riesgos y tiempos para el importador.</p></div>
  <div style="margin-top:1.8rem"><a href="trazabilidad.html" class="btn btn--gold">Ver el proceso completo</a></div>
</div></section>

<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Prensa</span><h2>Noticias y actualidad cafetalera</h2></div>
  <div class="news">{''.join(news_items().split('</article>')[:3]).replace('','') }</div>
  <div class="center" style="margin-top:2.2rem"><a href="prensa.html" class="btn btn--ghost">Ver todas las noticias</a></div>
</div></section>
'''
# fix: news teaser (3)
home_body = home_body.replace("{''.join(news_items", "")
def first3_news():
    parts = news_items().split('</article>')
    return '</article>'.join(parts[:3]) + '</article>'
home_body = f'''
<section class="hero" id="home"><div class="hero__beans" aria-hidden="true"></div>
<div class="container hero__inner">
  <div class="hero__content">
    <span class="hero__badge"><span class="dot"></span><span data-i18n="hero.badge">Café orgánico y de especialidad de Bolivia</span></span>
    <h1 data-i18n="hero.title">El café boliviano que <em>Europa</em> busca, con trazabilidad garantizada</h1>
    <p class="hero__lead" data-i18n="hero.lead">Federación de Caficultores Exportadores de Bolivia: 17.500 familias productoras, 42 organizaciones y trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).</p>
    <div class="hero__actions">
      <a href="afiliados.html" class="btn btn--gold btn--lg" data-i18n="hero.cta1">Importar nuestro café</a>
      <a href="nosotros.html" class="btn btn--ghost btn--lg" data-i18n="hero.cta2">Conocer la Federación</a>
    </div>
    <div class="hero__stats">
      <div><div class="num">17.500</div><div class="lbl">Familias cafetaleras</div></div>
      <div><div class="num">42</div><div class="lbl">Organizaciones afiliadas</div></div>
      <div><div class="num">1991</div><div class="lbl">Año de fundación</div></div>
      <div><div class="num">EUDR</div><div class="lbl">Trazabilidad UE 2023/1115</div></div>
    </div>
  </div>
  <aside class="hero__card reveal"><span class="ribbon">EUDR ready</span><img src="assets/img/logo-fecafeb.png" alt="Sello FECAFEB"><div class="cap">Café de calidad · Origen Yungas, Bolivia</div></aside>
</div></section>

<div class="trust"><div class="container trust__row">
  <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 11 3 3 8-8"/><path d="M21 12a9 9 0 1 1-6.2-8.5"/></svg> Comercio Justo · CNCJ-Bolivia</span>
  <span>{SVG["shield"]} Conformidad EUDR (UE 2023/1115)</span>
  <span>{SVG["globe"]} Exportación a Europa, EE.UU. y Asia</span>
  <span>{SVG["bean"]} Orgánico &amp; de especialidad</span>
</div></div>

<section class="section"><div class="container about">
  <div class="about__media reveal"><div class="frame">{ph("Fotografía: productores / cafetal de los Yungas")}</div><span class="pill">Ente rector del café boliviano</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Nosotros</span>
    <h2>Una federación, miles de familias detrás de cada grano</h2>
    <p class="lead">Desde 1991, FECAFEB representa, articula y fortalece a las organizaciones de productores de café de Bolivia, impulsando un sector competitivo, sostenible y con identidad.</p>
    <ul class="values" style="margin:1.4rem 0 1.6rem">
      <li>{CHK} 17.500 familias productoras</li><li>{CHK} 42 organizaciones afiliadas</li>
      <li>{CHK} Café orgánico y de especialidad</li><li>{CHK} Trazabilidad lista para la UE</li>
    </ul>
    <a href="nosotros.html" class="btn">Conocer más</a>
  </div>
</div></section>

<section class="section section--accent" id="cifras"><div class="container">
  <div class="head-block center"><span class="eyebrow">El sector en cifras</span><h2>Respaldo productivo y alcance nacional</h2></div>
  <div class="metrics">
    <div class="metric reveal"><div class="num">17.500</div><div class="lbl">Familias productoras</div></div>
    <div class="metric reveal" data-delay="80"><div class="num">42</div><div class="lbl">Cooperativas, asociaciones y Coracas</div></div>
    <div class="metric reveal" data-delay="160"><div class="num">3</div><div class="lbl">Departamentos: La Paz, Santa Cruz, Cochabamba</div></div>
    <div class="metric reveal" data-delay="240"><div class="num">96%</div><div class="lbl">Producción en La Paz (Yungas / Caranavi)</div></div>
  </div>
</div></section>

<section class="section section--tint"><div class="container">
  <div class="head-block center"><span class="eyebrow">Servicios</span><h2>Servicios para la familia cafetalera y para el comprador</h2>
  <p class="lead">Acompañamos al productor desde la parcela hasta el contrato de exportación.</p></div>
  <div class="grid grid-3">{services_cards()}</div>
  <div class="center" style="margin-top:2.2rem"><a href="servicios.html" class="btn btn--ghost">Ver todos los servicios</a></div>
</div></section>

<section class="section section--accent"><div class="container">
  <div class="head-block"><span class="eyebrow">Trazabilidad EUDR</span><h2>Del cafetal a Europa, grano por grano</h2>
  <p class="lead">Cumplimos el Reglamento UE 2023/1115. Cada lote es geolocalizado y verificable.</p></div>
  <div class="steps">{trace_steps()}</div>
  <div class="eudr-note reveal">{SVG["shield"]}<p><b>Acceso preferente al mercado europeo.</b> Nuestra plataforma deja lista la documentación de diligencia debida, reduciendo riesgos y tiempos para el importador.</p></div>
  <div style="margin-top:1.8rem"><a href="trazabilidad.html" class="btn btn--gold">Ver el proceso completo</a></div>
</div></section>

<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Prensa</span><h2>Noticias y actualidad cafetalera</h2></div>
  <div class="news">{first3_news()}</div>
  <div class="center" style="margin-top:2.2rem"><a href="prensa.html" class="btn btn--ghost">Ver todas las noticias</a></div>
</div></section>
'''
page("index.html","index.html","FECAFEB · Federación de Caficultores Exportadores de Bolivia","FECAFEB agrupa a 17.500 familias y 42 organizaciones cafetaleras de Bolivia. Café orgánico y de especialidad con trazabilidad EUDR.",home_body)

# ---------- NOSOTROS ----------
nosotros_body = f'''
<section class="section" id="mvv"><div class="container about">
  <div class="about__media reveal"><div class="frame">{ph("Fotografía institucional / equipo FECAFEB")}</div><span class="pill">Desde 1991</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Quiénes somos</span>
    <h2>El ente rector del café boliviano</h2>
    <p class="lead">FECAFEB es una entidad civil sin fines de lucro que representa, articula y fortalece a las organizaciones de productores de café de Bolivia.</p>
    <div data-tabs>
      <div class="tabs" role="tablist">
        <button class="tab is-active" data-target="t-mision" role="tab">Misión</button>
        <button class="tab" data-target="t-vision" role="tab">Visión</button>
        <button class="tab" data-target="t-valores" role="tab">Valores</button>
      </div>
      <div class="tab-panel is-active" id="t-mision"><p>Impulsar el desarrollo del productor cafetalero de Bolivia, sus familias y sus organizaciones, mediante una gestión innovadora, eficiente, humana y democrática de FECAFEB.</p></div>
      <div class="tab-panel" id="t-vision"><p>Café de Bolivia reconocido nacional e internacionalmente, posicionando el café orgánico y de especialidad, protegiendo el clima y el medio ambiente e impulsando el consumo masivo de calidad.</p></div>
      <div class="tab-panel" id="t-valores"><ul class="values">
        <li>{CHK} Consagración sectorial</li><li>{CHK} Lealtad</li><li>{CHK} Responsabilidad ambiental</li>
        <li>{CHK} Honestidad</li><li>{CHK} Transparencia</li><li>{CHK} Equidad de género y generacional</li></ul></div>
    </div>
  </div>
</div></section>

<section class="section section--tint" id="historia"><div class="container">
  <div class="head-block"><span class="eyebrow">Historia</span><h2>Una trayectoria al servicio del café</h2>
  <p class="lead">De 10 organizaciones fundadoras a una federación nacional que mira a los mercados internacionales.</p></div>
  <ul class="timeline" style="max-width:820px">
    <li class="reveal"><div class="yr">1991</div><div><h3>Fundación de FECAFEB</h3><p>Nace como ente rector del sector cafetalero con 10 organizaciones de productores. Estatuto protocolizado en 1992 y reconocimiento por Resolución Suprema en 1993.</p></div></li>
    <li class="reveal"><div class="yr">2000s</div><div><h3>Gestión y desarrollo</h3><p>FECAFEB transfiere la exportación a sus afiliadas y se consolida como gestora de proyectos de desarrollo, asistencia técnica y los Torneos de Café de Excelencia.</p></div></li>
    <li class="reveal"><div class="yr">2022</div><div><h3>Directorio renovado</h3><p>Nueva dirigencia con incorporación de jóvenes y fortalecimiento de los comités de mujeres y fiscalización.</p></div></li>
    <li class="reveal"><div class="yr">2023</div><div><h3>Plan Estratégico 2023–2027</h3><p>Hoja de ruta enfocada en sostenibilidad financiera e institucional, calidad y denominación de origen del café boliviano.</p></div></li>
    <li class="reveal"><div class="yr">2026</div><div><h3>Transformación digital y EUDR</h3><p>Plataforma de datos y trazabilidad geoespacial para el acceso preferente al mercado europeo.</p></div></li>
  </ul>
</div></section>

<section class="section" id="directorio"><div class="container">
  <div class="head-block center"><span class="eyebrow">Directorio</span><h2>Quienes lideran la Federación</h2>
  <p class="lead">Estructura de gobierno conformada por el Directorio Ejecutivo Nacional y los comités de fiscalización y de mujeres.</p></div>
  {board()}
</div></section>
'''
page("nosotros.html","nosotros.html","Nosotros · FECAFEB","Misión, visión, valores, historia y directorio de la Federación de Caficultores Exportadores de Bolivia.",nosotros_body,
     ("Nosotros","Nosotros","Conozca la misión, visión, valores, historia y el directorio de FECAFEB."))

# ---------- AFILIADOS ----------
afiliados_body = f'''
<section class="section"><div class="container">
  <div class="split">
    <div class="affil-card reveal">
      <span class="tag">Organizaciones de productores</span>
      <h3>Afíliese a FECAFEB</h3>
      <p>Acceda a representación sectorial, asistencia técnica, capacitación y vinculación comercial.</p>
      <ol>
        <li>Presente la carta de intención de su cooperativa o asociación.</li>
        <li>Entregue documentación legal y de la base de productores.</li>
        <li>Evaluación y aprobación por el Directorio.</li>
        <li>Incorporación a la plataforma y a los servicios.</li>
      </ol>
      <a href="contacto.html" class="btn btn--ghost">Solicitar afiliación</a>
    </div>
    <div class="affil-card affil-card--dark reveal" data-delay="120">
      <span class="tag tag--gold">Compradores UE / internacionales</span>
      <h3>Regístrese como exportador / comprador</h3>
      <p>Conéctese con café verde oro trazable, con declaración de diligencia debida (DDS) lista para la UE.</p>
      <ol>
        <li>Complete el formulario de comprador con su volumen y perfil de taza.</li>
        <li>Reciba muestras y ficha de trazabilidad geoespacial (GeoJSON).</li>
        <li>Validamos conformidad EUDR y emitimos la DDS.</li>
        <li>Cerramos contrato y coordinamos el embarque.</li>
      </ol>
      <a href="contacto.html" class="btn btn--gold">Iniciar registro de comprador</a>
    </div>
  </div>
</div></section>

<section class="section section--tint"><div class="container">
  <div class="head-block center"><span class="eyebrow">Red de afiliadas</span><h2>42 organizaciones en tres departamentos</h2>
  <p class="lead">Cooperativas, asociaciones y Coracas de La Paz, Santa Cruz y Cochabamba integran la Federación. (Directorio completo de afiliadas próximamente.)</p></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{SVG["users"]}</div><h3>Cooperativas</h3><p>Organizaciones de base con gestión productiva y comercial propia.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{SVG["leaf"]}</div><h3>Asociaciones</h3><p>Agrupaciones de productores enfocadas en calidad y sostenibilidad.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{SVG["globe"]}</div><h3>Coracas</h3><p>Corporaciones agropecuarias campesinas integradas a la cadena del café.</p></article>
  </div>
  <div class="map-ph" style="margin-top:2.4rem">{ph("Mapa de cooperativas afiliadas (La Paz · Santa Cruz · Cochabamba)")}</div>
</div></section>
'''
page("afiliados.html","afiliados.html","Afiliados · FECAFEB","Afíliese a FECAFEB o regístrese como comprador/exportador de café boliviano trazable conforme a EUDR.",afiliados_body,
     ("Afiliados","Afiliados &amp; exportadores","Súmese a la red cafetalera de Bolivia: organizaciones de productores y compradores internacionales."))

# ---------- SERVICIOS ----------
servicios_body = f'''
<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Servicios</span><h2>Una plataforma integral de servicios</h2>
  <p class="lead">Del cultivo a la exportación, acompañamos a la familia cafetalera y conectamos al comprador con un origen confiable.</p></div>
  <div class="grid grid-3">{services_cards()}</div>
</div></section>
<section class="section section--warm" id="escuela"><div class="container">{escuela_feature()}</div></section>
<section class="section section--accent"><div class="container center">
  <div class="head-block center"><span class="eyebrow">¿Busca un proveedor de café?</span><h2>Hablemos de su próxima importación</h2>
  <p class="lead">Le orientamos sobre volúmenes, perfiles de taza, certificaciones y trazabilidad EUDR.</p></div>
  <a href="contacto.html" class="btn btn--gold btn--lg">Contactar al equipo comercial</a>
</div></section>
'''
page("servicios.html","servicios.html","Servicios · FECAFEB","Asistencia técnica, comercialización, sanidad vegetal y la Escuela de Café de FECAFEB.",servicios_body,
     ("Servicios","Servicios","Servicios para la familia cafetalera y para el comprador internacional."))

# ---------- TRAZABILIDAD ----------
traz_body = f'''
<section class="section"><div class="container">
  <div class="about">
    <div class="about__media reveal"><div class="frame">{ph("Mapa / parcela geolocalizada (GeoJSON)")}</div><span class="pill">UE 2023/1115</span></div>
    <div class="about__content reveal" data-delay="120">
      <span class="eyebrow">Trazabilidad EUDR</span>
      <h2>Café libre de deforestación, verificable</h2>
      <p class="lead">El Reglamento de la Unión Europea exige geolocalizar cada parcela y demostrar que el café no proviene de zonas deforestadas. FECAFEB lo deja resuelto para el importador.</p>
      <ul class="values" style="margin-top:1.2rem">
        <li>{CHK} Polígonos GeoJSON / WGS84</li><li>{CHK} Declaración de diligencia debida (DDS)</li>
        <li>{CHK} Cadena de custodia por lote</li><li>{CHK} Integración con TRACES NT</li>
      </ul>
    </div>
  </div>
</div></section>
<section class="section section--accent"><div class="container">
  <div class="head-block"><span class="eyebrow">El proceso</span><h2>Del cafetal a Europa, grano por grano</h2></div>
  <div class="steps">{trace_steps()}</div>
  <div class="eudr-note reveal">{SVG["shield"]}<p><b>Acceso preferente al mercado europeo.</b> Reducimos riesgos y tiempos de la diligencia debida para el importador.</p></div>
</div></section>
'''
page("trazabilidad.html","trazabilidad.html","Trazabilidad EUDR · FECAFEB","Trazabilidad geoespacial del café boliviano conforme al Reglamento UE 2023/1115: GeoJSON, DDS y TRACES NT.",traz_body,
     ("Trazabilidad","Trazabilidad EUDR","Cumplimiento del Reglamento UE 2023/1115 sobre productos libres de deforestación."))

# ---------- PRENSA ----------
prensa_body = f'''
<section class="section"><div class="container">
  <div class="news">{news_items()}</div>
</div></section>
'''
page("prensa.html","prensa.html","Prensa · FECAFEB","Noticias y actualidad de la Federación de Caficultores Exportadores de Bolivia.",prensa_body,
     ("Prensa","Prensa","Noticias, eventos y actualidad del café boliviano."))

# ---------- GALERÍA ----------
galeria_body = f'''
<section class="section"><div class="container">
  <p class="lead center" style="margin:0 auto 2.4rem">Reemplace estos espacios por fotografías reales de cafetales, cosecha, beneficiado y comunidades.</p>
  <div class="gallery">{gallery_items()}</div>
</div></section>
'''
page("galeria.html","galeria.html","Galería · FECAFEB","Galería del origen: cafetales, cosecha, beneficiado y comunidades cafetaleras de Bolivia.",galeria_body,
     ("Galería","Galería","El origen del café boliviano, en imágenes."))

# ---------- CONTACTO ----------
contacto_body = f'''
<section class="section"><div class="container contact">
  <div class="contact__info">
    <div class="info-row reveal"><div class="ico">{SVG["pin"]}</div><div><b>Dirección</b><span>Av. Juan Pablo II 2974, El Alto · La Paz, Bolivia</span></div></div>
    <div class="info-row reveal" data-delay="60"><div class="ico">{SVG["phone"]}</div><div><b>Teléfono / WhatsApp</b><a href="https://wa.me/59171537365" target="_blank" rel="noopener">+591 71537365</a></div></div>
    <div class="info-row reveal" data-delay="120"><div class="ico">{SVG["mail"]}</div><div><b>Correo</b><a href="mailto:fecafebfinanzas@gmail.com">fecafebfinanzas@gmail.com</a></div></div>
    <div class="info-row reveal" data-delay="180"><div class="ico">{SVG["screen"]}</div><div><b>Plataforma institucional</b><a href="#">Acceso para afiliados y técnicos (próximamente)</a></div></div>
    <div class="map-ph">{ph("Mapa de ubicación (El Alto · La Paz)")}</div>
  </div>
  <form class="form" data-demo>
    <div class="form__ok">✓ ¡Gracias! Su mensaje fue registrado. Le contactaremos pronto.</div>
    <div class="form__row">
      <div class="field"><label for="n">Nombre</label><input id="n" type="text" required placeholder="Su nombre"></div>
      <div class="field"><label for="e">Correo</label><input id="e" type="email" required placeholder="correo@empresa.com"></div>
    </div>
    <div class="form__row">
      <div class="field"><label for="p">Perfil</label><select id="p"><option>Comprador / importador (UE)</option><option>Cooperativa / asociación</option><option>Prensa</option><option>Otro</option></select></div>
      <div class="field"><label for="c">País</label><input id="c" type="text" placeholder="Ej. Alemania"></div>
    </div>
    <div class="field"><label for="m">Mensaje</label><textarea id="m" required placeholder="Cuéntenos qué café busca o cómo podemos ayudarle…"></textarea></div>
    <button class="btn btn--lg" type="submit" style="width:100%">Enviar mensaje</button>
    <p class="form__note">Demo de plantilla — conectar a backend/CRM en la siguiente fase del proyecto.</p>
  </form>
</div></section>
'''
page("contacto.html","contacto.html","Contacto · FECAFEB","Contacte a FECAFEB: compradores, cooperativas y aliados del café boliviano.",contacto_body,
     ("Contacto","Hablemos de café","Compradores, cooperativas y aliados: escríbanos y le responderemos a la brevedad."))

print("OK - páginas generadas")
