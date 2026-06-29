# -*- coding: utf-8 -*-
"""Construye las páginas del sitio FECAFEB usando parts.py (scaffolding compartido)."""
from parts import *

# ===================== INICIO =====================
slide = lambda k,alt,b,s,act="": f'<div class="hero__slide{act}"><img src="{U(k,1000)}" alt="{alt}" {"" if act else "loading=lazy"} onerror="this.style.display=&quot;none&quot;"><div class="scrim"></div><div class="cap"><b>{b}</b><span>{s}</span></div></div>'
home = f"""
<section class="hero" id="home"><div class="hero__beans" aria-hidden="true"></div>
<div class="container hero__inner">
  <div class="hero__content">
    <span class="hero__badge"><span class="dot"></span><span data-i18n="hero.badge">Café orgánico y de especialidad de Bolivia</span></span>
    <h1 data-i18n="hero.title">El café boliviano que <em>Europa</em> busca, con trazabilidad garantizada</h1>
    <p class="hero__lead" data-i18n="hero.lead">Federación de Caficultores Exportadores de Bolivia: 17.500 familias productoras, 42 organizaciones y trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).</p>
    <div class="hero__actions">
      <a href="afiliados.html" class="btn btn--gold btn--lg" data-i18n="hero.cta1">Importar nuestro café</a>
      <a href="quienes-somos.html" class="btn btn--ghost btn--lg" data-i18n="hero.cta2">Conocer la Federación</a>
    </div>
    <div class="hero__stats">
      <div><div class="num" data-count="17500" data-sep>0</div><div class="lbl">Familias cafetaleras</div></div>
      <div><div class="num" data-count="42">0</div><div class="lbl">Organizaciones afiliadas</div></div>
      <div><div class="num">1991</div><div class="lbl">Año de fundación</div></div>
      <div><div class="num">EUDR</div><div class="lbl">Trazabilidad UE 2023/1115</div></div>
    </div>
  </div>
  <aside class="hero__slider reveal" data-controls aria-label="Galería del café boliviano">
    <span class="hero__ribbon">EUDR ready</span>
    <div class="hero__slides">
      {slide('cherries','Cosecha de café en los Yungas','Trazabilidad EUDR','Geolocalización de cada parcela para el mercado europeo',' is-active')}
      {slide('field','Cafetales de altura','Café de especialidad','Orgánico y de altura · origen Yungas, Bolivia')}
      {slide('hands','Familias cafetaleras de Bolivia','17.500 familias','Caficultores de Bolivia · 42 organizaciones')}
    </div>
    <button class="hero__nav prev" aria-label="Anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>
    <button class="hero__nav next" aria-label="Siguiente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 6 6 6-6 6"/></svg></button>
    <div class="hero__dots"></div>
  </aside>
</div></section>
{hub()}
<div class="trust"><div class="container trust__row">
  <span>{I['chk']} Comercio Justo · CNCJ-Bolivia</span>
  <span>{I['shield']} Conformidad EUDR (UE 2023/1115)</span>
  <span>{I['globe']} Exportación a Europa, EE.UU. y Asia</span>
  <span>{I['bean']} Orgánico &amp; de especialidad</span>
</div></div>
<section class="section section--pattern"><div class="container about">
  <div class="about__media reveal"><div class="frame">{img('hands','Productoras y productores de café de los Yungas')}</div><span class="pill">Ente rector del café boliviano</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Quiénes Somos</span><h2>Una federación, miles de familias detrás de cada grano</h2>
    <p class="lead">Desde 1991, FECAFEB representa, articula y fortalece a las organizaciones de productores de café de Bolivia, impulsando un sector competitivo, sostenible y con identidad.</p>
    <ul class="values" style="margin:1.4rem 0 1.6rem"><li>{I['chk']} 17.500 familias productoras</li><li>{I['chk']} 42 organizaciones afiliadas</li><li>{I['chk']} Café orgánico y de especialidad</li><li>{I['chk']} Trazabilidad lista para la UE</li></ul>
    <a href="quienes-somos.html" class="btn">Conocer más</a>
  </div>
</div></section>
<section class="section section--accent" id="cifras"><div class="container">
  <div class="head-block center"><span class="eyebrow">El sector en cifras</span><h2>Respaldo productivo y alcance nacional</h2></div>
  <div class="metrics">
    <div class="metric reveal"><div class="num" data-count="17500" data-sep>0</div><div class="lbl">Familias productoras</div></div>
    <div class="metric reveal" data-delay="80"><div class="num" data-count="42">0</div><div class="lbl">Cooperativas, asociaciones y Coracas</div></div>
    <div class="metric reveal" data-delay="160"><div class="num">3</div><div class="lbl">Departamentos: La Paz, Santa Cruz, Cochabamba</div></div>
    <div class="metric reveal" data-delay="240"><div class="num">96%</div><div class="lbl">Producción en La Paz (Yungas / Caranavi)</div></div>
  </div>
</div></section>
{brands_marquee()}
<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Noticias</span><h2>Actualidad cafetalera</h2></div>
  <div class="news">{''.join(__import__('parts').__dict__.get('NEWS3',''))}</div>
  <div class="center" style="margin-top:2.2rem"><a href="noticias.html" class="btn btn--ghost">Ver todas las noticias</a></div>
</div></section>
"""

# noticias data
NEWS=[("Eventos","Junio 2026","FECAFEB impulsa la trazabilidad EUDR para sus afiliadas","Nueva plataforma digital para sistematizar datos de productores y parcelas.","farm"),
      ("Calidad","Mayo 2026","Taza Presidencial: el café boliviano brilla en el exterior","Productores de los Yungas destacan por su café de especialidad.","cherries"),
      ("Comité de Mujeres","Abril 2026","Cumbre de Mujeres Cafetaleras fortalece liderazgos","Productoras lideran la mejora de la calidad y la marca Kullaka.","hands"),
      ("Comercio","Marzo 2026","Ronda de negocios con compradores europeos","Encuentro comercial para conectar la oferta boliviana con la demanda de la UE.","bag"),
      ("Sostenibilidad","Febrero 2026","Agroforestería: café que protege el bosque","Modelo productivo alineado a la normativa de deforestación de la UE.","field"),
      ("Institucional","Enero 2026","FECAFEB presenta su Plan Estratégico 2023–2027","Hoja de ruta hacia la sostenibilidad financiera e institucional.","harvest")]
def news_card(c,d,t,x,k):
    return f'<article class="news__item reveal"><div class="news__cover"><span class="badge">{c}</span><img src="{U(k,640)}" alt="{t}" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="news__body"><time>{d}</time><h3>{t}</h3><p>{x}</p><a href="#">Leer más →</a></div></article>'
NEWS_ALL=''.join(news_card(*n) for n in NEWS)
NEWS_3=''.join(news_card(*n) for n in NEWS[:3])
home=home.replace("{''.join(__import__('parts').__dict__.get('NEWS3',''))}", NEWS_3)
page("index.html","index.html","FECAFEB · Federación de Caficultores Exportadores de Bolivia","FECAFEB agrupa a 17.500 familias y 42 organizaciones cafetaleras de Bolivia. Café orgánico y de especialidad con trazabilidad EUDR.",home)

# ===================== QUIÉNES SOMOS =====================
def board(groups):
    out=[]
    for gid,gname,people in groups:
        cards=''
        for name,role,org in people:
            ini=''.join(w[0] for w in name.split()[:2]).upper()
            orgh=f'<div class="org">{org}</div>' if org else ''
            cards+=f'<div class="person reveal"><div class="av">{ini}</div><b>{name}</b><div class="role">{role}</div>{orgh}</div>'
        out.append(f'<div class="board-group" id="{gid}"><h3>{gname}</h3><div class="board">{cards}</div></div>')
    return ''.join(out)
GROUPS=[("dir","Directorio Ejecutivo Nacional",[("Hugo Poma Maqui","Presidente",""),("Jimmy Gustavo Chávez Quijhua","Tesorero / Coordinador",""),("Juan Pablo Rojas Marino","Secretario","")]),
        ("fiscalizacion","Comité de Fiscalización",[("José Cori Quispe","Presidente","Cooperativa Mejillones"),("Ever Villca","Secretario","Cooperativa Villa Oriente")]),
        ("mujeres-dir","Comité de Mujeres",[("Yola Condori Álvarez","Presidenta","Cooperativa Antofagasta"),("Mari Luz Kalla Osco","Tesorera","Cooperativa San Juan"),("Elsa Calle","Secretaria","Cooperativa CENAPROC")])]
qs = f"""
<section class="section section--pattern" id="mvv"><div class="container about">
  <div class="about__media reveal"><div class="frame">{img('people','Equipo e institucionalidad FECAFEB')}</div><span class="pill">Desde 1991</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Quiénes somos</span><h2>El ente rector del café boliviano</h2>
    <p class="lead">FECAFEB es una entidad civil sin fines de lucro que representa, articula y fortalece a las organizaciones de productores de café de Bolivia.</p>
    <div data-tabs>
      <div class="tabs" role="tablist"><button class="tab is-active" data-target="t-mision" role="tab">Misión</button><button class="tab" data-target="t-vision" role="tab">Visión</button><button class="tab" data-target="t-valores" role="tab">Valores</button></div>
      <div class="tab-panel is-active" id="t-mision"><p>Impulsar el desarrollo del productor cafetalero de Bolivia, sus familias y sus organizaciones, mediante una gestión innovadora, eficiente, humana y democrática de FECAFEB.</p></div>
      <div class="tab-panel" id="t-vision"><p>Café de Bolivia reconocido nacional e internacionalmente, posicionando el café orgánico y de especialidad, protegiendo el clima y el medio ambiente e impulsando el consumo masivo de calidad.</p></div>
      <div class="tab-panel" id="t-valores"><ul class="values"><li>{I['chk']} Consagración sectorial</li><li>{I['chk']} Lealtad</li><li>{I['chk']} Responsabilidad ambiental</li><li>{I['chk']} Honestidad</li><li>{I['chk']} Transparencia</li><li>{I['chk']} Equidad de género</li></ul></div>
    </div>
  </div>
</div></section>
<section class="section section--tint" id="instancias"><div class="container">
  <div class="head-block center"><span class="eyebrow">Instancias de FECAFEB</span><h2>Nuestra estructura de gobierno</h2>
  <p class="lead">Directorio Ejecutivo Nacional, Comité de Fiscalización y Comité de Mujeres, conforme al Estatuto Orgánico.</p></div>
  {board(GROUPS)}
  <div class="center" style="margin-top:1.6rem"><a href="comite-mujeres.html" class="btn btn--ghost">Conocer al Comité de Mujeres</a></div>
</div></section>
<section class="section" id="historia"><div class="container">
  <div class="head-block"><span class="eyebrow">Historia</span><h2>Una trayectoria al servicio del café</h2></div>
  <ul class="timeline" style="max-width:820px">
    <li class="reveal"><div class="yr">1991</div><div><h3>Fundación de FECAFEB</h3><p>Nace como ente rector con 10 organizaciones de productores. Estatuto protocolizado en 1992 y reconocimiento por Resolución Suprema en 1993.</p></div></li>
    <li class="reveal"><div class="yr">2000s</div><div><h3>Gestión y desarrollo</h3><p>Transfiere la exportación a sus afiliadas y se consolida como gestora de proyectos, asistencia técnica y la Taza de Excelencia.</p></div></li>
    <li class="reveal"><div class="yr">2023</div><div><h3>Plan Estratégico 2023–2027</h3><p>Sostenibilidad financiera e institucional, calidad y denominación de origen.</p></div></li>
    <li class="reveal"><div class="yr">2026</div><div><h3>Transformación digital y EUDR</h3><p>Plataforma de datos y trazabilidad geoespacial para el acceso preferente al mercado europeo.</p></div></li>
  </ul>
</div></section>
"""
page("quienes-somos.html","quienes-somos.html","Quiénes Somos · FECAFEB","Misión, visión, valores, instancias (Directorio, Comité de Fiscalización, Comité de Mujeres) e historia de FECAFEB.",qs,
     ("Quiénes Somos","Quiénes Somos","Misión, visión, valores, instancias de gobierno e historia de la Federación."))

# ===================== AFILIADOS =====================
MAPBO = open("parts.py").read()  # placeholder to keep import lean
from parts import I as _I
afil = f"""
<section class="section"><div class="container"><div class="split">
  <div class="affil-card reveal"><span class="tag">Organizaciones de productores</span><h3>Afíliese a FECAFEB</h3>
    <p>Acceda a representación sectorial, asistencia técnica, capacitación y vinculación comercial.</p>
    <ol><li>Presente la carta de intención de su cooperativa o asociación.</li><li>Entregue documentación legal y de la base de productores.</li><li>Evaluación y aprobación por el Directorio.</li><li>Incorporación a la plataforma y a los servicios.</li></ol>
    <a href="contacto.html" class="btn btn--ghost">Solicitar afiliación</a></div>
  <div class="affil-card affil-card--dark reveal" data-delay="120"><span class="tag tag--gold">Compradores UE / internacionales</span><h3>Regístrese como exportador / comprador</h3>
    <p>Conéctese con café verde oro trazable, con declaración de diligencia debida (DDS) lista para la UE.</p>
    <ol><li>Complete el formulario de comprador con su volumen y perfil de taza.</li><li>Reciba muestras y ficha de trazabilidad geoespacial (GeoJSON).</li><li>Validamos conformidad EUDR y emitimos la DDS.</li><li>Cerramos contrato y coordinamos el embarque.</li></ol>
    <a href="contacto.html" class="btn btn--gold">Iniciar registro de comprador</a></div>
</div></div></section>
<section class="section section--tint"><div class="container">{access("La base de datos de afiliados se publica en tres niveles, protegiendo la información estratégica de cada cooperativa.")}</div></section>
<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Red de afiliadas</span><h2>Zonas productoras · 42 organizaciones</h2>
  <p class="lead">Cooperativas, asociaciones y Coracas de La Paz, Santa Cruz y Cochabamba. Seleccione un marcador para ver su información.</p></div>
  __MAPBO__
</div></section>
"""
afil = afil.replace("__MAPBO__", '<div class="zonas"><div id="mapZonas"></div><aside class="zona-info" id="zonaInfo"></aside></div><p class="form__note" style="margin-top:1rem">Mapa base OpenStreetMap / CARTO (open source). En el sistema, al acercar el mapa se podrá consultar la parcela de cada productor.</p>')
page("afiliados.html","afiliados.html","Afiliados · FECAFEB","Afíliese a FECAFEB o regístrese como comprador. Tres niveles de acceso y mapa de zonas productoras.",afil,
     ("Afiliados","Afiliados & exportadores","Súmese a la red cafetalera de Bolivia, con tres niveles de acceso a la información."),
     extra_head=LEAFLET_CSS, extra_js=LEAFLET_JS + '<script src="js/maps.js"></script>')

# ===================== TRAZABILIDAD =====================
def traz_cards():
    items=[("pin","Geolocalización satelital","Monitoreo de cada parcela de origen, con polígonos en GeoJSON/WGS84."),
           ("leaf","Cero deforestación","Verificación de que el café no proviene de zonas deforestadas, conforme a EUDR."),
           ("doc","Código único de lote","Historial completo: producción, lavado, secado y cadena de custodia.")]
    return ''.join(f'<article class="card reveal"><div class="card__ico">{I[i]}</div><h3>{t}</h3><p>{d}</p></article>' for i,t,d in items)
def steps():
    s=[("Geolocalización","Polígonos GeoJSON / WGS84 georreferenciados en campo."),("Registro del lote","Productor, finca, fecha de cosecha y cadena de custodia."),("Diligencia debida","Generación de la DDS y verificación contra mapas de deforestación."),("TRACES NT","Presentación ante el sistema de la UE para el ingreso conforme.")]
    return ''.join(f'<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in s)
traz = f"""
<section class="section section--pattern"><div class="container about">
  <div class="about__media reveal"><div class="frame">{img('field','Parcela cafetalera georreferenciada')}</div><span class="pill">UE 2023/1115</span></div>
  <div class="about__content reveal" data-delay="120"><span class="eyebrow">Trazabilidad EUDR</span><h2>Café libre de deforestación, verificable</h2>
    <p class="lead">El Reglamento de la Unión Europea exige geolocalizar cada parcela y demostrar que el café no proviene de zonas deforestadas. FECAFEB lo deja resuelto para el importador — su <b>pasaporte para exportar a Europa</b>.</p>
    <ul class="values" style="margin-top:1.2rem"><li>{I['chk']} Polígonos GeoJSON / WGS84</li><li>{I['chk']} Declaración de diligencia debida (DDS)</li><li>{I['chk']} Cadena de custodia por lote</li><li>{I['chk']} Integración con TRACES NT</li></ul>
  </div>
</div></section>
<section class="section"><div class="container"><div class="lookup"><span class="eyebrow" style="color:var(--gold-soft)">Consulta pública</span><h2>Verifique la trazabilidad de su café</h2><p>¿Compró café boliviano? Ingrese el código de lote impreso en el empaque para ver su origen, parcela y cumplimiento EUDR, y descargar las certificaciones.</p><form class="lookup__form" id="lotForm"><input id="lotInput" type="text" placeholder="Ej. LOT-000123" aria-label="Código de lote"><button class="btn btn--gold btn--lg" type="submit">Consultar</button></form><p class="lookup__hint">Pruebe con: <b>LOT-000123</b> · <b>LOT-000456</b> · <b>LOT-000789</b></p></div><div class="lot" id="lotResult"></div></div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Garantías para el comprador</span><h2>Transparencia y trazabilidad global</h2></div><div class="grid grid-3">{traz_cards()}</div></div></section>
<section class="section section--accent"><div class="container"><div class="head-block"><span class="eyebrow">El proceso</span><h2>Del cafetal a Europa, grano por grano</h2></div><div class="steps">{steps()}</div>
  <div class="eudr-note reveal">{I['shield']}<p><b>Acceso preferente al mercado europeo.</b> Reducimos riesgos y tiempos de la diligencia debida para el importador.</p></div></div></section>
<section class="section"><div class="container">{access("El portal de trazabilidad expone la información en tres niveles, garantizando la seguridad de los datos GIS estratégicos de exportación.")}</div></section>
"""
page("trazabilidad.html","trazabilidad.html","Trazabilidad EUDR · FECAFEB","Consulta pública de trazabilidad por lote y cumplimiento EUDR (UE 2023/1115).",traz,
     ("Trazabilidad","Trazabilidad EUDR","Consulta pública por lote y cumplimiento del Reglamento UE 2023/1115."),
     extra_head=LEAFLET_CSS, extra_js=LEAFLET_JS + '<script src="js/trace.js"></script>')

# ===================== SERVICIOS =====================
serv = f"""
<section class="section section--pattern"><div class="container">
  <div class="head-block center"><span class="eyebrow">Servicios</span><h2>Una plataforma integral de servicios</h2>
  <p class="lead">Del cultivo a la exportación, acompañamos a la familia cafetalera y conectamos al comprador con un origen confiable.</p></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{I['leaf']}</div><h3>Asistencia técnica productiva</h3><p>Acompañamiento en campo para rendimientos, calidad de taza y manejo agroforestal sostenible.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['chart']}</div><h3>Comercialización & exportación</h3><p>Vinculación con compradores internacionales y promoción de la denominación de origen.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['shield']}</div><h3>Sanidad vegetal e innovación</h3><p>Manejo integrado de plagas, bioinsumos y transferencia tecnológica.</p></article>
  </div>
</div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Servicios destacados</span><h2>Pilares del ecosistema FECAFEB</h2></div>
  <div class="grid grid-3">
    <a class="card reveal" href="escuela-cafe.html"><div class="card__ico">{I['cap']}</div><h3>Escuela de Café</h3><p>Formación en producción, calidad, catación y gestión.</p></a>
    <a class="card reveal" data-delay="80" href="kullaka.html"><div class="card__ico">{I['cup']}</div><h3>Marca Kullaka</h3><p>Vitrina comercial del café con identidad de mujer.</p></a>
    <a class="card reveal" data-delay="160" href="taza-presidencial.html"><div class="card__ico">{I['trophy']}</div><h3>Taza Presidencial</h3><p>Torneo nacional bajo estándares de catación SCA.</p></a>
  </div>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">¿Busca un proveedor de café?</span><h2>Hablemos de su próxima importación</h2><p class="lead">Le orientamos sobre volúmenes, perfiles de taza, certificaciones y trazabilidad EUDR.</p></div><a href="contacto.html" class="btn btn--gold btn--lg">Contactar al equipo comercial</a></div></section>
"""
page("servicios.html","servicios.html","Servicios · FECAFEB","Asistencia técnica, comercialización, Escuela de Café, Marca Kullaka y Taza Presidencial.",serv,
     ("Servicios","Servicios","Servicios para la familia cafetalera y para el comprador internacional."))

# ===================== ESCUELA DE CAFÉ =====================
esc = f"""
<section class="section"><div class="container feature">
  <div class="feature__media reveal"><img class="photo" src="assets/img/logo-escuela-cafe.png" alt="Escuela de Café FECAFEB"></div>
  <div class="feature__content reveal" data-delay="120"><span class="tag tag--gold">Programa insignia</span><h2>Escuela de Café</h2>
    <p class="lead">Plataforma educativa para la formación técnica de productores, jóvenes y mujeres cafetaleras: del cultivo a la taza.</p>
    <ul><li>{I['chk']} Producción orgánica y agroforestería</li><li>{I['chk']} Catación, barismo y tueste</li><li>{I['chk']} Buenas prácticas y poscosecha</li><li>{I['chk']} Administración y gestión cooperativa</li></ul>
    <a href="contacto.html" class="btn">Preinscribirme</a>
  </div>
</div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Oferta formativa</span><h2>Cursos cuatrimestrales</h2><p class="lead">Orientados especialmente a jóvenes hijos de productores, con descarga de sílabos y pago en línea (próximamente).</p></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{I['leaf']}</div><h3>Producción & agroforestería</h3><p>Manejo del cultivo, suelos y sombra; café orgánico de altura.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['cup']}</div><h3>Catación & barismo</h3><p>Análisis sensorial, protocolo SCA y preparación de especialidad.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['chart']}</div><h3>Gestión cooperativa</h3><p>Administración, costos y comercialización para la organización.</p></article>
  </div>
</div></section>
"""
page("escuela-cafe.html","servicios.html","Escuela de Café · FECAFEB","Plataforma educativa de FECAFEB: catación, barismo, producción y gestión para la familia cafetalera.",esc,
     ("Servicios / Escuela de Café","Escuela de Café","Formación técnica del cultivo a la taza, con enfoque en jóvenes y mujeres."))

# ===================== COMITÉ DE MUJERES =====================
muj = f"""
<section class="section"><div class="container pillar-hero reveal">
  <img src="assets/img/logo-comite-mujeres.jpg" alt="Comité de Mujeres Cafetaleras de Bolivia">
  <div><span class="eyebrow">Equidad de género</span><h2>Comité de Mujeres Cafetaleras de Bolivia</h2>
  <p class="lead">Visibiliza y fortalece el liderazgo de las productoras de café asociadas a FECAFEB en toda la cadena de valor.</p></div>
</div></section>
<section class="section section--tint"><div class="container grid grid-2">
  <div class="card reveal"><div class="card__ico">{I['venus']}</div><h3>Nuestra misión</h3><p>Impulsar el empoderamiento social y económico de las productoras de café asociadas a FECAFEB, garantizando su visibilización y el fortalecimiento de sus liderazgos cooperativos en la cadena de valor.</p></div>
  <div class="card reveal" data-delay="120"><div class="card__ico">{I['users']}</div><h3>Valores del Comité</h3><ul class="values"><li>{I['chk']} Sororidad — apoyo mutuo entre las bases</li><li>{I['chk']} Transparencia — información clara y accesible</li><li>{I['chk']} Cooperación — trabajo conjunto por fines comunes</li></ul></div>
</div></section>
<section class="section"><div class="container feature">
  <div class="feature__media reveal"><img class="photo" src="assets/img/logo-kullaka.png" alt="Café Kullaka"></div>
  <div class="feature__content reveal" data-delay="120"><span class="tag">Sinergia institucional y comercial</span><h2>Del liderazgo a la taza: Café Kullaka</h2>
    <p class="lead">El Comité conecta su trabajo social con un brazo comercial tangible: la marca de café de especialidad <b>Kullaka</b>.</p>
    <ul><li>{I['chk']} Perfil de la productora (storytelling) que da valor agregado al café</li><li>{I['chk']} Trazabilidad de impacto: el comprador ve qué cooperativa de mujeres produjo su lote</li><li>{I['chk']} Cumbre de Mujeres: intercambio de experiencias y liderazgo</li></ul>
    <a href="kullaka.html" class="btn">Conocer la Marca Kullaka</a>
  </div>
</div></section>
"""
page("comite-mujeres.html","quienes-somos.html","Comité de Mujeres · FECAFEB","Comité de Mujeres Cafetaleras de Bolivia: empoderamiento, liderazgo y la marca Café Kullaka.",muj,
     ("Quiénes Somos / Comité de Mujeres","Comité de Mujeres","Empoderamiento y liderazgo de las productoras de café de Bolivia."))

# ===================== MARCA KULLAKA =====================
kul = f"""
<section class="section"><div class="container pillar-hero reveal">
  <img src="assets/img/logo-kullaka.png" alt="Café Kullaka">
  <div><span class="eyebrow">Vitrina comercial</span><h2>Café Kullaka — “Esencia que abraza”</h2>
  <p class="lead">La marca de café de especialidad de FECAFEB con identidad de mujer, que impulsa la comercialización nacional e internacional.</p>
  <div class="hero__actions" style="margin-top:1.2rem"><a href="contacto.html" class="btn btn--gold">Comprar / cotizar</a><a href="comite-mujeres.html" class="btn btn--ghost">Comité de Mujeres</a></div></div>
</div></section>
<section class="section section--tint"><div class="container grid grid-3">
  <article class="card reveal"><div class="card__ico">{I['venus']}</div><h3>Identidad de mujer</h3><p>Café producido y liderado por las mujeres cafetaleras de Bolivia.</p></article>
  <article class="card reveal" data-delay="80"><div class="card__ico">{I['bean']}</div><h3>Especialidad de altura</h3><p>Origen Yungas, orgánico, perfiles de taza diferenciados.</p></article>
  <article class="card reveal" data-delay="160"><div class="card__ico">{I['globe']}</div><h3>Mercado nacional e internacional</h3><p>Comercialización con identidad y trazabilidad de impacto.</p></article>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Compradores</span><h2>Lleve Kullaka a su mercado</h2><p class="lead">Café con historia, calidad y respaldo institucional de FECAFEB.</p></div><a href="contacto.html" class="btn btn--gold btn--lg">Solicitar información comercial</a></div></section>
"""
page("kullaka.html","servicios.html","Marca Kullaka · FECAFEB","Café Kullaka, la marca de especialidad con identidad de mujer de FECAFEB. Esencia que abraza.",kul,
     ("Servicios / Marca Kullaka","Marca Kullaka","Café de especialidad con identidad de mujer."))

# ===================== TAZA PRESIDENCIAL =====================
results=[("1°","Coop. Mejillones","Caranavi, La Paz","Geisha","89,5"),("2°","Coop. Antofagasta","Caranavi, La Paz","Java","88,75"),("3°","Coop. San Juan","Coroico, La Paz","Caturra","88,25"),("4°","Coop. Villa Oriente","Palos Blancos","Catuaí","87,9"),("5°","CENAPROC","Caranavi, La Paz","Typica","87,5")]
rows=''.join(f'<tr><td class="rank">{r}</td><td>{c}</td><td>{z}</td><td>{v}</td><td class="score">{s}</td></tr>' for r,c,z,v,s in results)
taza = f"""
<section class="section"><div class="container about">
  <div class="about__media reveal"><div class="frame">{img('specialty','Catación de café — Taza Presidencial')}</div><span class="pill">Estándares SCA</span></div>
  <div class="about__content reveal" data-delay="120"><span class="eyebrow">Orgullo boliviano</span><h2>Torneo Nacional Taza Presidencial</h2>
    <p class="lead">El evento cumbre del café de Bolivia, bajo estándares de catación de la SCA, con subasta internacional de los mejores lotes.</p>
    <ul class="values" style="margin-top:1.2rem"><li>{I['chk']} Convocatoria digitalizada y reglamentos descargables</li><li>{I['chk']} Resultados y precios históricos de subastas</li><li>{I['chk']} Directorio de jueces nacionales e internacionales</li></ul>
  </div>
</div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Resultados (referenciales)</span><h2>Tabla de puntajes — edición 2025</h2><p class="lead">Datos de ejemplo; se cargarán los resultados oficiales al integrar el módulo de subastas.</p></div>
  <div style="overflow-x:auto"><table class="ptable"><thead><tr><th>Puesto</th><th>Cooperativa</th><th>Zona</th><th>Variedad</th><th>Puntaje</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Convocatoria abierta</span><h2>Participe en la Taza Presidencial 2026–2027</h2><p class="lead">Inscriba su lote y compita por llegar a la subasta internacional.</p></div><a href="contacto.html" class="btn btn--gold btn--lg">Ver convocatoria</a></div></section>
"""
page("taza-presidencial.html","servicios.html","Taza Presidencial · FECAFEB","Torneo Nacional Taza Presidencial de Bolivia: catación SCA, resultados y subasta internacional.",taza,
     ("Servicios / Taza Presidencial","Taza Presidencial","El evento cumbre del café boliviano, bajo estándares SCA."))

# ===================== PUBLICACIONES =====================
docs=[("doc","Estatuto Orgánico y Reglamento Interno","Documento institucional · PDF"),
      ("doc","Plan Estratégico Institucional 2023–2027","Estrategia · PDF"),
      ("doc","Reglamento Taza Presidencial 2026–2027","Convocatoria · PDF"),
      ("doc","Guía de cumplimiento EUDR para afiliadas","Trazabilidad · PDF"),
      ("doc","Memoria anual FECAFEB","Rendición de cuentas · PDF")]
doclist=''.join(f'<div class="doc reveal"><div class="doc__ico">{I[ic]}</div><div class="doc__b"><b>{t}</b><span>{s}</span></div><a class="doc__dl" href="#">{I["dl"]} Descargar</a></div>' for ic,t,s in docs)
GAL=[("Cafetales de los Yungas","tall","field"),("Cosecha selectiva","","cherries"),("Beneficiado y secado","","bag"),("Catación y calidad","","cup"),("Familias cafetaleras","","hands"),("Escuela de Café","tall","shop"),("Café verde de exportación","","green"),("Comité de Mujeres","","harvest")]
gal=''.join(f'<figure class="{c}"><img src="{U(k,700)}" alt="{t}" loading="lazy" onerror="this.style.display=&quot;none&quot;"><figcaption>{t}</figcaption></figure>' for t,c,k in GAL)
pub = f"""
<section class="section"><div class="container">
  <div class="head-block"><span class="eyebrow">Documentos</span><h2>Publicaciones y descargas</h2><p class="lead">Documentos institucionales, reglamentos y reportes. (Descargas de ejemplo; se gestionarán desde el CMS.)</p></div>
  <div class="docs">{doclist}</div>
</div></section>
<section class="section section--pattern"><div class="container"><div class="head-block"><span class="eyebrow">Blog del Café</span><h2>Historias, técnica y mercado</h2><p class="lead">Artículos sobre producción, calidad, mercados y vida cafetalera boliviana.</p></div><div class="blog"><article class="post reveal"><div class="cover"><span class="cat">Calidad</span><img src="https://images.unsplash.com/photo-1442550528053-c431ecb55509?auto=format&fit=crop&w=640&q=70" alt="Cómo la altura define el perfil de taza del café yungueño" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="post__b"><time>Junio 2026</time><h3>Cómo la altura define el perfil de taza del café yungueño</h3><p>Acidez, dulzor y aromas: la altitud de los Yungas marca la diferencia.</p><a href="#">Leer artículo →</a></div></article><article class="post reveal"><div class="cover"><span class="cat">Sostenibilidad</span><img src="https://images.unsplash.com/photo-1500423079914-b65af272b8db?auto=format&fit=crop&w=640&q=70" alt="Agroforestería: producir café cuidando el bosque" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="post__b"><time>Mayo 2026</time><h3>Agroforestería: producir café cuidando el bosque</h3><p>Sistemas bajo sombra que protegen suelos, agua y biodiversidad.</p><a href="#">Leer artículo →</a></div></article><article class="post reveal"><div class="cover"><span class="cat">Mercado</span><img src="https://images.unsplash.com/photo-1521302080334-4bebac2763a6?auto=format&fit=crop&w=640&q=70" alt="EUDR: qué cambia para el exportador boliviano en 2026" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="post__b"><time>Abril 2026</time><h3>EUDR: qué cambia para el exportador boliviano en 2026</h3><p>Claves de la diligencia debida y la georreferenciación de parcelas.</p><a href="#">Leer artículo →</a></div></article></div></div></section>
<section class="section"><div class="container"><div class="head-block"><span class="eyebrow">Comunicados</span><h2>Comunicados oficiales</h2></div><div class="comunicados"><div class="comunicado reveal"><time>15 jun 2026</time><div><b>Convocatoria Taza Presidencial 2026–2027</b><span>Apertura de inscripciones para cooperativas y asociaciones afiliadas.</span></div><a href="#">Ver comunicado →</a></div><div class="comunicado reveal"><time>28 may 2026</time><div><b>Lineamientos de cumplimiento EUDR para afiliadas</b><span>Plazos y requisitos de georreferenciación de parcelas.</span></div><a href="#">Ver comunicado →</a></div><div class="comunicado reveal"><time>10 abr 2026</time><div><b>Asamblea General Ordinaria — citación</b><span>Orden del día y documentación para las organizaciones afiliadas.</span></div><a href="#">Ver comunicado →</a></div></div></div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Galería</span><h2>El origen, en imágenes</h2><p class="lead">Imágenes de referencia, reemplazables por fotografías propias de FECAFEB.</p></div>
  <div class="gallery">{gal}</div>
</div></section>
"""
page("publicaciones.html","publicaciones.html","Publicaciones · FECAFEB","Documentos institucionales, reglamentos, reportes y galería del café boliviano.",pub,
     ("Publicaciones","Publicaciones","Documentos, reglamentos, reportes y galería de FECAFEB."))

# ===================== NOTICIAS =====================
noti = f"""
<section class="section"><div class="container"><div class="news">{NEWS_ALL}</div></div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Boletín semanal</span><h2>Reciba precios, clima y convocatorias</h2><p class="lead">Resumen semanal para socios y aliados del café boliviano.</p></div>
  <form class="footer__news" data-demo style="max-width:420px;margin:0 auto"><input type="email" placeholder="Su correo" required aria-label="Correo"><button type="submit" aria-label="Suscribirse">→</button></form></div></section>
"""
page("noticias.html","noticias.html","Noticias · FECAFEB","Noticias, eventos, boletín semanal y actualidad del café boliviano.",noti,
     ("Noticias","Noticias","Actualidad, eventos y boletín del café boliviano."))

# ===================== CONTACTO =====================
con = f"""
<section class="section"><div class="container contact">
  <div class="contact__info">
    <div class="info-row reveal"><div class="ico">{I['pin']}</div><div><b>Dirección</b><span>Av. Juan Pablo II 2974, El Alto · La Paz, Bolivia</span></div></div>
    <div class="info-row reveal" data-delay="60"><div class="ico">{I['phone']}</div><div><b>Teléfono / WhatsApp</b><a href="https://wa.me/59171537365" target="_blank" rel="noopener">+591 71537365</a></div></div>
    <div class="info-row reveal" data-delay="120"><div class="ico">{I['mail']}</div><div><b>Correo</b><a href="mailto:contacto@fecafeb.org">contacto@fecafeb.org</a></div></div>
    <div class="info-row reveal" data-delay="180"><div class="ico">{I['screen']}</div><div><b>Portal Institucional</b><a href="#">Acceso para afiliados y técnicos (próximamente)</a></div></div>
    <div class="map-ph">{ph("Mapa de ubicación (El Alto · La Paz) — integrar Google Maps / Leaflet")}</div>
  </div>
  <form class="form" data-demo>
    <div class="form__ok">✓ ¡Gracias! Su mensaje fue registrado. Le contactaremos pronto.</div>
    <div class="form__row"><div class="field"><label for="n">Nombre</label><input id="n" type="text" required placeholder="Su nombre"></div><div class="field"><label for="e">Correo</label><input id="e" type="email" required placeholder="correo@empresa.com"></div></div>
    <div class="form__row"><div class="field"><label for="p">Perfil</label><select id="p"><option>Comprador / importador (UE)</option><option>Cooperativa / asociación</option><option>Prensa</option><option>Otro</option></select></div><div class="field"><label for="c">País</label><input id="c" type="text" placeholder="Ej. Alemania"></div></div>
    <div class="field"><label for="m">Mensaje</label><textarea id="m" required placeholder="Cuéntenos qué café busca o cómo podemos ayudarle…"></textarea></div>
    <button class="btn btn--lg" type="submit" style="width:100%">Enviar mensaje</button>
    <p class="form__note">Demo de plantilla — conectar a backend/CRM en la siguiente fase.</p>
  </form>
</div></section>
"""
page("contacto.html","contacto.html","Contacto · FECAFEB","Contacte a FECAFEB: compradores, cooperativas y aliados del café boliviano.",con,
     ("Contacto","Hablemos de café","Compradores, cooperativas y aliados: escríbanos y le responderemos a la brevedad."))

print("OK - sitio generado")
