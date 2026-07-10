# -*- coding: utf-8 -*-
"""Construye las páginas del sitio FECAFEB usando parts.py (scaffolding compartido)."""
from parts import *

# ===================== INICIO =====================
slide = lambda src,b,s,act="": f'<div class="hero__slide{act}"><img src="{src}" alt="{b}" loading="lazy" onerror="this.style.display=&quot;none&quot;"><div class="cap"><b>{b}</b><span>{s}</span></div></div>'
def news_card(c,d,t,x,k):
    return f'<article class="news__item reveal"><div class="news__cover"><span class="badge">{c}</span><img src="{U(k,640)}" alt="{t}" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="news__body"><time>{d}</time><h3>{t}</h3><p>{x}</p></div></article>'
NEWS_HOME=[("Café Presidencial","Torneo 2022","VIII Torneo Nacional Taza de Calidad — Café Presidencial","270 muestras de La Paz, Cochabamba y Santa Cruz compitieron por el título, junto al Ministerio de Relaciones Exteriores y el Ministerio de Desarrollo Rural y Tierras.","cupping"),
           ("Comité de Mujeres","Abril 2025","1ra Cumbre Nacional de Mujeres Cafetaleras","Productoras de todo el país se reunieron en Caranavi para fortalecer liderazgo y calidad bajo el lema “Mujeres de cara al Bicentenario”.","hands"),
           ("Trazabilidad","Reglamento UE 2023/1115","Trazabilidad geoespacial rumbo al mercado europeo","FECAFEB avanza en la georreferenciación de parcelas de sus 21 organizaciones afiliadas para cumplir el Reglamento europeo de deforestación (EUDR).","andes")]
NEWS_HOME_HTML=''.join(news_card(*n) for n in NEWS_HOME)
home = f"""
<section class="hero" id="home">
<div class="hero__slider" data-controls aria-label="Galería del café boliviano">
  <div class="hero__slides">
    {slide('assets/img/photos/p_grupo_cumbre.jpg','Una federación unida','Organizaciones y familias productoras de todo el país',' is-active')}
    {slide('assets/img/photos/p_cumbre_liderazgo.jpg','Liderazgo de las productoras','Cumbre Nacional de Mujeres Cafetaleras')}
    {slide('assets/img/photos/p_cerezas.jpg','Café de origen boliviano','Cosecha selectiva en los Yungas de La Paz')}
    {slide('assets/img/photos/p_taza_servida.jpg','Calidad reconocida','Café de especialidad listo para exportación')}
    {slide('assets/img/photos/p_evaluacion_sensorial.jpg','Evaluación sensorial SCA','Catación y control de calidad en cada torneo')}
  </div>
  <div class="hero__scrim" aria-hidden="true"></div>
  <span class="hero__ribbon">Novedades</span>
  <button class="hero__nav prev" aria-label="Anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>
  <button class="hero__nav next" aria-label="Siguiente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 6 6 6-6 6"/></svg></button>
  <div class="hero__dots"></div>
</div>
<div class="container hero__inner">
  <div class="hero__content">
    <span class="hero__badge"><span class="dot"></span><span data-i18n="hero.badge">Café orgánico y de especialidad de Bolivia</span></span>
    <h1 data-i18n="hero.title">Federación de Caficultores <em>Exportadores</em> de Bolivia</h1>
    <p class="hero__lead" data-i18n="hero.lead">21 organizaciones y ~1.389 familias productoras afiliadas, que representan al sector cafetalero boliviano, con trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).</p>
    <div class="hero__actions">
      <a href="afiliados.html" class="btn btn--gold btn--lg" data-i18n="hero.cta1">Importar nuestro café</a>
      <a href="quienes-somos.html" class="btn btn--outline-light btn--lg" data-i18n="hero.cta2">Conocer la Federación</a>
    </div>
    <div class="hero__stats">
      <div><div class="num" data-count="1389" data-sep>0</div><div class="lbl">Familias productoras afiliadas</div></div>
      <div><div class="num" data-count="21">0</div><div class="lbl">Organizaciones afiliadas</div></div>
      <div><div class="num">1991</div><div class="lbl">Año de fundación</div></div>
      <div><div class="num">EUDR</div><div class="lbl">Trazabilidad UE 2023/1115</div></div>
    </div>
  </div>
</div>
</section>
<section class="section section--pattern"><div class="container about">
  <div class="about__media reveal"><div class="frame"><div class="mslider" data-mslider><img src="assets/img/photos/p_equipo.jpg" alt="Equipo e institucionalidad de FECAFEB" class="is-active" loading="lazy"><img src="assets/img/photos/p_mujeres.jpg" alt="Cumbre de Mujeres Cafetaleras" loading="lazy"><img src="assets/img/photos/p_productores.jpg" alt="Productores de café de los Yungas" loading="lazy"><img src="assets/img/photos/p_caranavi.jpg" alt="Caranavi, capital cafetalera" loading="lazy"><span class="mslider__dots"></span></div></div><span class="pill">Único ente regulador del café de calidad</span></div>
  <div class="about__content reveal" data-delay="120">
    <span class="eyebrow">Quiénes Somos</span><h2>Una federación, miles de familias detrás de cada grano</h2>
    <p class="lead">Desde 1991, FECAFEB representa, articula y fortalece a las organizaciones de productores de café de Bolivia, impulsando un sector competitivo, sostenible y con identidad.</p>
    <ul class="values" style="margin:1.4rem 0 1.6rem"><li>{I['chk']} 1.389 familias productoras afiliadas</li><li>{I['chk']} 21 organizaciones afiliadas</li><li>{I['chk']} Café orgánico y de especialidad</li><li>{I['chk']} Trazabilidad lista para la UE</li></ul>
    <a href="quienes-somos.html" class="btn">Conocer más</a>
  </div>
</div></section>
<section class="section section--accent" id="cifras"><div class="container">
  <div class="head-block center"><span class="eyebrow">El sector en cifras</span><h2>Respaldo productivo y alcance nacional</h2><p class="lead">Datos verificados de FECAFEB (2026). Además, la Federación forma parte de un sector cafetalero boliviano de alrededor de 17.500 familias.</p></div>
  <div class="metrics">
    <div class="metric reveal"><div class="num" data-count="21">0</div><div class="lbl">Organizaciones afiliadas</div></div>
    <div class="metric reveal" data-delay="80"><div class="num" data-count="1389" data-sep>0</div><div class="lbl">Familias productoras afiliadas</div></div>
    <div class="metric reveal" data-delay="160"><div class="num" data-count="276">0</div><div class="lbl">Mujeres productoras</div></div>
    <div class="metric reveal" data-delay="240"><div class="num" data-count="1276" data-sep>0</div><div class="lbl">Toneladas de café (producción)</div></div>
  </div>
</div></section>
<section class="section"><div class="container">
  <div class="head-block center"><span class="eyebrow">Noticias</span><h2>Actualidad cafetalera</h2><p class="lead">Hitos recientes de la Federación y sus organizaciones afiliadas.</p></div>
  <div class="news">{NEWS_HOME_HTML}</div>
  <div class="center" style="margin-top:2.2rem"><a href="noticias.html" class="btn btn--ghost">Ver todas las noticias</a></div>
</div></section>
"""

# noticias data
NEWS=[("Boletín","Julio 2026","El café boliviano que Europa busca, con trazabilidad garantizada","Nota de prensa: origen, calidad y trazabilidad EUDR del café boliviano para el mercado europeo.","cherries"),
      ("Eventos","Junio 2026","FECAFEB impulsa la trazabilidad EUDR para sus afiliadas","Nueva plataforma digital para sistematizar datos de productores y parcelas.","farm"),
      ("Calidad","Mayo 2026","Taza Presidencial: el café boliviano brilla en el exterior","Productores de los Yungas destacan por su café de especialidad.","cup"),
      ("Comité de Mujeres","Abril 2026","Cumbre de Mujeres Cafetaleras fortalece liderazgos","Productoras lideran la mejora de la calidad y la marca Kullaka.","hands"),
      ("Comercio","Marzo 2026","Ronda de negocios con compradores europeos","Encuentro comercial para conectar la oferta boliviana con la demanda de la UE.","bag"),
      ("Sostenibilidad","Febrero 2026","Agroforestería: café que protege el bosque","Modelo productivo alineado a la normativa de deforestación de la UE.","field"),
      ("Institucional","Enero 2026","FECAFEB presenta su Plan Estratégico 2023–2027","Hoja de ruta hacia la sostenibilidad financiera e institucional.","people")]
NEWS_ALL=''.join(news_card(*n) for n in NEWS)
page("index.html","index.html","FECAFEB · Federación de Caficultores Exportadores de Bolivia","FECAFEB agrupa a 21 organizaciones y ~1.389 familias productoras afiliadas de Bolivia. Café orgánico y de especialidad con trazabilidad EUDR.",home)

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
    <span class="eyebrow">Quiénes somos</span><h2>El único ente regulador del café de calidad de Bolivia</h2>
    <p class="lead">FECAFEB es la máxima organización gremial y el <b>único ente regulador del café de calidad</b> en Bolivia, responsable del control de calidad bajo estándares internacionales. Como <b>Federación Nacional de tercer nivel</b>, actúa de puente oficial ante el Estado, la cooperación internacional y los compradores del exterior.</p>
    <div data-tabs>
      <div class="tabs" role="tablist"><button class="tab is-active" data-target="t-mision" role="tab">Misión</button><button class="tab" data-target="t-vision" role="tab">Visión</button><button class="tab" data-target="t-valores" role="tab">Valores</button></div>
      <div class="tab-panel-wrap">
        <div class="tab-panel is-active" id="t-mision"><p>Impulsar el desarrollo del productor cafetalero de Bolivia, sus familias y sus organizaciones, mediante una gestión innovadora, eficiente, humana y democrática de FECAFEB.</p></div>
        <div class="tab-panel" id="t-vision"><p>Café de Bolivia reconocido nacional e internacionalmente, posicionando el café orgánico y de especialidad, protegiendo el clima y el medio ambiente e impulsando el consumo masivo de calidad.</p></div>
        <div class="tab-panel" id="t-valores"><ul class="values"><li>{I['chk']} Consagración sectorial</li><li>{I['chk']} Lealtad</li><li>{I['chk']} Responsabilidad ambiental</li><li>{I['chk']} Honestidad</li><li>{I['chk']} Transparencia</li><li>{I['chk']} Equidad de género</li></ul></div>
      </div>
    </div>
  </div>
</div></section>
<section class="section section--tint" id="instancias"><div class="container">
  <div class="head-block center"><span class="eyebrow">Instancias de FECAFEB</span><h2>Nuestra estructura</h2>
  <p class="lead">Directorio Ejecutivo Nacional, Comité de Fiscalización y Comité de Mujeres, conforme al Estatuto Orgánico.</p></div>
  {board(GROUPS)}
  <div class="center" style="margin-top:1.6rem"><a href="comite-mujeres.html" class="btn btn--ghost">Conocer al Comité de Mujeres</a></div>
</div></section>
<section class="section" id="historia"><div class="container">
  <div class="head-block"><span class="eyebrow">Historia</span><h2>Una trayectoria al servicio del café</h2></div>
  <div class="timeline-wrap"><ul class="timeline" style="max-width:820px">
    <li class="reveal"><span class="yr">1991</span><h3>Fundación de FECAFEB</h3><p>Nace como ente rector con 10 organizaciones de productores. Estatuto protocolizado en 1992 y reconocimiento por Resolución Suprema en 1993.</p></li>
    <li class="reveal"><span class="yr">2006</span><h3>Nace la Escuela del Café</h3><p>FECAFEB instaura su Escuela del Café como brazo de formación técnica para catadores y productores.</p></li>
    <li class="reveal"><span class="yr">2007–2022</span><h3>Consolidación institucional</h3><p>Sucesión de directorios (Ángel Condori, Eustaquio Huiza, Eugenio Villca, Víctor Calla, Raúl Mamani, Ruth Vidaurre) y crecimiento hasta 42 organizaciones afiliadas, con participación en 8 versiones de la Taza de Excelencia.</p></li>
    <li class="reveal"><span class="yr">Oct 2022</span><h3>Nueva gestión directiva</h3><p>Hugo Poma Maqui asume la presidencia del Directorio Ejecutivo Nacional.</p></li>
    <li class="reveal"><span class="yr">2023</span><h3>Plan Estratégico 2023–2027</h3><p>Sostenibilidad financiera e institucional, calidad y denominación de origen.</p></li>
    <li class="reveal"><span class="yr">2026</span><h3>Transformación digital y EUDR</h3><p>Plataforma de datos y trazabilidad geoespacial para el acceso preferente al mercado europeo.</p></li>
  </ul></div>
</div></section>
<section class="section section--tint" id="cooperacion"><div class="container"><div class="head-block center"><span class="eyebrow">Cooperación internacional</span><h2>Aliados que fortalecen a FECAFEB</h2><p class="lead">Proyectos ejecutados con cooperación nacional e internacional en los últimos años (2022–2026).</p></div><div class="grid grid-3">
  <article class="card reveal"><div class="aliado__logo"><img src="assets/img/logos/logo_ayuda_en_accion.png" alt="Ayuda en Acción" loading="lazy"></div><h3>Ayuda en Acción Bolivia</h3><p>Emprendimientos inclusivos en la cadena del café y comercialización con identidad de género (2025–2026).</p></article>
  <article class="card reveal" data-delay="80"><div class="aliado__logo"><img src="assets/img/logos/logo_embajada_francia.png" alt="Embajada de Francia en Bolivia" loading="lazy"></div><h3>Embajada de Francia — PISCCA</h3><p>Café sin violencia ni discriminación, dedicado a jóvenes y mujeres cafetaleras (2024–2025).</p></article>
  <article class="card reveal" data-delay="160"><div class="aliado__logo"><img src="assets/img/logos/logo_rabobank_trim.png" alt="Fundación Rabobank" loading="lazy"></div><h3>Fundación Rabobank</h3><p>Asistencia técnica financiera, administrativa y de marketing; módulo de Administración de la Escuela del Café (2024–2025).</p></article>
  <article class="card reveal"><div class="aliado__logo"><img src="assets/img/logos/logo_fecafeb_comercial_trim.png" alt="FECAFEB" loading="lazy"></div><h3>OIT (ILO)</h3><p>Plan Estratégico Institucional y consolidación institucional de FECAFEB (2023).</p></article>
  <article class="card reveal" data-delay="80"><div class="aliado__logo"><img src="assets/img/logos/logo_fecafeb_comercial_trim.png" alt="FECAFEB" loading="lazy"></div><h3>Kooperationen</h3><p>Consolidación de métodos de producción, viveros, bioinsumos y riego tecnificado (2022–2023).</p></article>
  <article class="card reveal" data-delay="160"><div class="aliado__logo"><img src="assets/img/logos/logo_ue.png" alt="Unión Europea" loading="lazy"></div><h3>Proyecto AAGIL</h3><p>Ayuda en Acción con cofinanciamiento de la Unión Europea — transformación digital y trazabilidad EUDR.</p></article>
</div>
<p class="form__note" style="margin-top:1.2rem">FECAFEB · organización civil sin fines de lucro (Ley N° 351 de 2013) · NIT 1000949028 · fundada el 15 de mayo de 1991 · El Alto, Bolivia.</p></div></section>
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
  <div class="head-block center"><span class="eyebrow">Red de afiliadas</span><h2>Zonas productoras · 21 organizaciones afiliadas</h2>
  <p class="lead">Cooperativas, asociaciones y Coracas de La Paz, Santa Cruz y Cochabamba (datos verificados 2026). Seleccione un marcador para ver su información.</p></div>
  __MAPBO__
</div></section>
<section class="section"><div class="container"><div class="head-block"><span class="eyebrow">Directorio de afiliadas</span><h2>Organizaciones afiliadas a FECAFEB (2026)</h2><p class="lead">Listado verificado de las 21 organizaciones de productores afiliadas, con producción y familias reportadas.</p></div><div style="overflow-x:auto"><table class="ptable"><thead><tr><th>N°</th><th>Sigla</th><th>Organización</th><th>Zona / Cantón</th><th>Producción (TM)</th><th>Familias</th></tr></thead><tbody><tr><td class="rank">1</td><td class="score">CORACA CRC</td><td>Corporación Agrop. Campesina Regional Carrasco La Reserva</td><td>Carrasco La Reserva</td><td>168</td><td>40</td></tr><tr><td class="rank">2</td><td class="score">ILLAMPU</td><td>Coop. Agrop. Integral Corpus Cristhy Illampu R.L.</td><td>Entre Ríos</td><td>126</td><td>50</td></tr><tr><td class="rank">3</td><td class="score">APCERME</td><td>Asoc. Prod. de Café Ecológico Río Mercedes</td><td>Caranavi</td><td>1</td><td>20</td></tr><tr><td class="rank">4</td><td class="score">MONTAÑA VERDE</td><td>Asoc. Agrop. Prod. Ecológicos de Café Montaña Verde</td><td>San Lorenzo</td><td>63</td><td>61</td></tr><tr><td class="rank">5</td><td class="score">ALTO SAJAMA</td><td>Coop. Agropecuaria Alto Sajama</td><td>San Lorenzo</td><td>63</td><td>76</td></tr><tr><td class="rank">6</td><td class="score">CENAPROC</td><td>Central Asociados Prod. de Café de Montaña</td><td>San Lorenzo</td><td>21</td><td>38</td></tr><tr><td class="rank">7</td><td class="score">UNIÓN PROAGRO</td><td>Unión de Productores Agropecuarios</td><td>Chijchipani</td><td>105</td><td>150</td></tr><tr><td class="rank">8</td><td class="score">AIPEP</td><td>Asoc. Integral de Prod. Ecológicos Pumiri</td><td>Calama</td><td>42</td><td>49</td></tr><tr><td class="rank">9</td><td class="score">MEJILLONES</td><td>Coop. Agropecuaria Mejillones R.L.</td><td>Calama</td><td>105</td><td>92</td></tr><tr><td class="rank">10</td><td class="score">SAN JUAN</td><td>Coop. Agrícola Cafetalera San Juan R.L.</td><td>Carrasco La Reserva</td><td>63</td><td>36</td></tr><tr><td class="rank">11</td><td class="score">ANTOFAGASTA</td><td>Coop. Agropecuaria Antofagasta</td><td>Carrasco La Reserva</td><td>63</td><td>54</td></tr><tr><td class="rank">12</td><td class="score">CELCCAR</td><td>Central Local de Cooperativas Caranavi</td><td>Caranavi</td><td>21</td><td>325</td></tr><tr><td class="rank">13</td><td class="score">COAINE</td><td>Coop. Agropecuaria Integral Nor Este</td><td>Caranavi</td><td>0</td><td>98</td></tr><tr><td class="rank">14</td><td class="score">VILLA ORIENTE</td><td>Coop. Agrícola Villa Oriente R.L.</td><td>Entre Ríos</td><td>105</td><td>70</td></tr><tr><td class="rank">15</td><td class="score">ASOCAFE</td><td>Asoc. de Caficultores de Taypiplaya</td><td>Taypiplaya</td><td>120</td><td>138</td></tr><tr><td class="rank">16</td><td class="score">APROCAFE</td><td>Asoc. de Productores de Café Ecológico</td><td>Caranavi</td><td>42</td><td>37</td></tr><tr><td class="rank">17</td><td class="score">CIAPEC</td><td>Coop. Integral Agrícola de Prod. Ecológicos</td><td>Entre Ríos</td><td>126</td><td>55</td></tr><tr><td class="rank">18</td><td class="score">APCERL</td><td>Asoc. Prod. Cafetaleros Ecológicos Regional Larecaja</td><td>Larecaja</td><td>0</td><td>—</td></tr><tr><td class="rank">19</td><td class="score">AGROCAM</td><td>Asociación Agropecuaria Calama Mojsa</td><td>Calama</td><td>42</td><td>—</td></tr><tr><td class="rank">20</td><td class="score">ASPAGRO</td><td>Asociación Productores Santa Cruz</td><td>Santa Cruz</td><td>0</td><td>250</td></tr><tr><td class="rank">21</td><td class="score">Café Tropic</td><td>Café Tropic Cochabamba</td><td>Cochabamba</td><td>0</td><td>150</td></tr></tbody></table></div><p class="form__note" style="margin-top:1rem">Fuente: Lista de Afiliados FECAFEB 2026. Producción total ~1.276 TM · exportación 66 contenedores · 1.389 familias (276 mujeres).</p></div></section>
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
  <div class="about__media reveal"><div class="frame">{img('field','Caranavi, corazón cafetalero de los Yungas')}</div><span class="pill">UE 2023/1115</span></div>
  <div class="about__content reveal" data-delay="120"><span class="eyebrow">Trazabilidad EUDR</span><h2>Café libre de deforestación, verificable</h2>
    <p class="lead">El Reglamento de la Unión Europea exige geolocalizar cada parcela y demostrar que el café no proviene de zonas deforestadas. FECAFEB lo deja resuelto para el importador — su <b>pasaporte para exportar a Europa</b>.</p>
    <ul class="values" style="margin-top:1.2rem"><li>{I['chk']} Polígonos GeoJSON / WGS84</li><li>{I['chk']} Declaración de diligencia debida (DDS)</li><li>{I['chk']} Cadena de custodia por lote</li><li>{I['chk']} Integración con TRACES NT</li></ul>
  </div>
</div></section>
<section class="section"><div class="container"><div class="lookup"><span class="eyebrow" style="color:var(--gold-soft)">Consulta pública</span><h2>Verifique la trazabilidad de su café</h2><p>¿Compró café boliviano? Ingrese el código de lote impreso en el empaque para ver su origen, parcela y cumplimiento EUDR, y descargar las certificaciones.</p><form class="lookup__form" id="lotForm"><input id="lotInput" type="text" placeholder="Ej. LOT-000123" aria-label="Código de lote"><button class="btn btn--gold btn--lg" type="submit">Consultar</button></form><p class="lookup__hint">Pruebe con: <b>LOT-000123</b> · <b>LOT-000456</b> · <b>LOT-000789</b></p></div><div class="lot" id="lotResult"></div></div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Garantías para el comprador</span><h2>Transparencia y trazabilidad global</h2></div><div class="grid grid-3">{traz_cards()}</div></div></section>
<section class="section section--accent"><div class="container"><div class="head-block"><span class="eyebrow">El proceso</span><h2>Del cafetal a Europa, grano por grano</h2></div><div class="steps">{steps()}</div>
  <div class="eudr-note reveal">{I['shield']}<p><b>Acceso preferente al mercado europeo.</b> Reducimos riesgos y tiempos de la diligencia debida para el importador.</p></div></div></section>
<section class="section"><div class="container feature">
  <div class="feature__media reveal"><img class="photo" src="assets/img/logo-coraca-crc.png" alt="CORACA CRC — café orgánico certificado"></div>
  <div class="feature__content reveal" data-delay="120"><span class="tag tag--gold">Caso real · afiliada CORACA CRC</span><h2>Georreferenciación y certificación en marcha</h2>
    <p class="lead">La Corporación Agropecuaria Campesina Regional Carrasco La Reserva (CORACA CRC) ya tiene sus parcelas georreferenciadas y su base de productores certificada, lista para la diligencia debida europea.</p>
    <ul class="values" style="margin-top:1rem"><li>{I['chk']} 32 productores certificados · 216 ha registradas</li><li>{I['chk']} Certificación orgánica IMOcert (UE 848 / NOP)</li><li>{I['chk']} Parcelas georreferenciadas en UTM 19S, altitud 1.040–1.465 m.s.n.m.</li><li>{I['chk']} Padrón de miembros y productos listos para TRACES NT</li></ul>
  </div>
</div></section>
<section class="section"><div class="container"><div class="head-block"><span class="eyebrow">Comité de Geolocalización y Tecnología</span><h2>Monitoreo, trazabilidad e innovación en campo</h2><p class="lead">Comité responsable del monitoreo de parcelas, la trazabilidad y la innovación tecnológica de las organizaciones afiliadas.</p></div><div class="head-block" style="margin-top:1rem"><span class="eyebrow">Autoevaluación EUDR</span><h2>Escala de calificación</h2><p class="lead">Herramienta para medir el nivel de preparación de cada organización frente al Reglamento EUDR.</p></div><div class="access"><div class="access-card lvl-c"><div class="access-card__top"><span class="access-card__ico" style="font-family:var(--f-head);font-weight:700">1–5</span><span class="access-badge">Nivel Crítico</span></div><h3>Requiere acciones inmediatas</h3><p>Cumplimiento incipiente o no conforme; alto riesgo residual.</p></div><div class="access-card lvl-b"><div class="access-card__top"><span class="access-card__ico" style="font-family:var(--f-head);font-weight:700">6–8</span><span class="access-badge">Nivel Moderado</span></div><h3>Requiere seguimiento y fortalecimiento</h3><p>Requisito funcional y en proceso de mejora; riesgo moderado.</p></div><div class="access-card lvl-a"><div class="access-card__top"><span class="access-card__ico" style="font-family:var(--f-head);font-weight:700">9–10</span><span class="access-badge">Nivel Sólido</span></div><h3>Buenas prácticas consolidadas</h3><p>Requisito plenamente integrado y verificable; riesgo bajo o nulo.</p></div></div><div class="eudr-tool reveal"><div class="eudr-tool__b"><span class="eyebrow" style="color:var(--gold)">AL-INVEST Verde · financiado por la Unión Europea</span><h2>Sistema de autoevaluación y cumplimiento EUDR</h2><p class="lead">Herramienta oficial (SENAVEX) para que cada organización mida su nivel de cumplimiento del Reglamento de la UE sobre productos libres de deforestación, con base en su documentación y georreferenciación.</p></div><a class="btn btn--gold btn--lg" href="https://autoevaluacioneudr.senavex.gob.bo/" target="_blank" rel="noopener">Abrir autoevaluación EUDR →</a></div><div class="head-block" style="margin-top:2.6rem"><span class="eyebrow">Recursos de interés</span><h2>EUDR · enlaces oficiales</h2></div><div class="docs"><div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>Comisión Europea</b><span>Regulation on Deforestation-free products</span></div><a class="doc__dl" href="https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en" target="_blank" rel="noopener">Abrir →</a></div><div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>Ministerio para la Transición Ecológica (España)</b><span>Información sobre el EUDR</span></div><a class="doc__dl" href="https://www.miteco.gob.es" target="_blank" rel="noopener">Abrir →</a></div><div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>Team Europe · Cadenas de valor libres de deforestación</b><span>Iniciativa del equipo Europa</span></div><a class="doc__dl" href="https://international-partnerships.ec.europa.eu" target="_blank" rel="noopener">Abrir →</a></div><div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>EUDR Community of Practice</b><span>European Forest Institute</span></div><a class="doc__dl" href="https://www.efi.int" target="_blank" rel="noopener">Abrir →</a></div><div class="doc reveal"><div class="doc__ico">{I['shield']}</div><div class="doc__b"><b>SENAVEX · Autoevaluación EUDR (Bolivia)</b><span>Sistema nacional de cumplimiento</span></div><a class="doc__dl" href="https://autoevaluacioneudr.senavex.gob.bo/" target="_blank" rel="noopener">Abrir →</a></div></div></div></section>
<section class="section"><div class="container">{access("El portal de trazabilidad expone la información en tres niveles, garantizando la seguridad de los datos GIS estratégicos de exportación.")}</div></section>
"""
page("trazabilidad.html","trazabilidad.html","Trazabilidad EUDR · FECAFEB","Consulta pública de trazabilidad por lote y cumplimiento EUDR (UE 2023/1115).",traz,
     ("Trazabilidad","Trazabilidad EUDR","Consulta pública por lote y cumplimiento del Reglamento UE 2023/1115."),
     extra_head=LEAFLET_CSS, extra_js=LEAFLET_JS + '<script src="js/trace.js"></script>')

# ===================== SERVICIOS =====================
serv = f"""
<section class="section section--pattern"><div class="container">
  <div class="head-block center"><span class="eyebrow">Servicios</span><h2>Una plataforma integral de servicios</h2>
  <p class="lead">Del cultivo a la exportación, acompañamos a la familia cafetalera y conectamos al comprador con un origen confiable. La oferta de servicios responde directamente a los ejes del Plan Estratégico Institucional 2023–2027.</p></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{I['leaf']}</div><h3>Asistencia técnica productiva</h3><p>Acompañamiento en campo para elevar rendimientos y calidad de taza mediante el modelo agroforestal —consolidado con cooperación de KOOPERATIONEN (viveros, bioinsumos, riego tecnificado, 2022–2023)— y el impulso al Programa de Expansión, Renovación y Mejora de Cultivos del PEI.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['chart']}</div><h3>Comercialización & exportación</h3><p>Vinculación con compradores internacionales y promoción del <b>Sistema de Denominación de Origen del Café Boliviano (SDO)</b>, uno de los ejes de aprendizaje del PEI 2023–2027, junto a la trazabilidad EUDR para el mercado europeo.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['shield']}</div><h3>Sanidad vegetal e innovación</h3><p>Manejo Integrado de Plagas (MIP) y transferencia tecnológica frente a la broca del café y el cambio climático, dos de las amenazas identificadas en el diagnóstico sectorial del PEI.</p></article>
  </div>
</div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Servicios destacados</span><h2>Pilares del ecosistema FECAFEB</h2></div>
  <div class="grid grid-3">
    <a class="card reveal" href="escuela-cafe.html"><div class="card__ico">{I['cap']}</div><h3>Escuela de Café</h3><p>Formación en administración de organizaciones exportadoras, catación/barismo bajo protocolo SCA y manejo tecnológico de parcela — nacida en 2006 como FORCAFE.</p></a>
    <a class="card reveal" data-delay="80" href="kullaka.html"><div class="card__ico">{I['cup']}</div><h3>Marca Kullaka</h3><p>Vitrina comercial del café de especialidad producido y liderado por las mujeres cafetaleras de Bolivia, con trazabilidad de impacto hasta la cooperativa de origen.</p></a>
    <a class="card reveal" data-delay="160" href="taza-presidencial.html"><div class="card__ico">{I['trophy']}</div><h3>Taza Presidencial</h3><p>Torneo nacional bajo estándares SCA, organizado desde 2015 junto a Cancillería y el Ministerio de Desarrollo Rural y Tierras, con subasta internacional de los mejores lotes.</p></a>
  </div>
</div></section>
<section class="section"><div class="container"><div class="head-block center"><span class="eyebrow">Programas emblemáticos</span><h2>Del Plan Estratégico Institucional 2023–2027</h2></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{I['leaf']}</div><h3>Programa Café 2024–2030</h3><p>Hoja de ruta de expansión y renovación de cultivos a mediano plazo.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['chart']}</div><h3>Casa del Café Caranavi</h3><p>Infraestructura sectorial para procesamiento y valor agregado en la capital cafetalera de Bolivia.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['venus']}</div><h3>Café Sin Violencia</h3><p>Programa con la Embajada de Francia (PISCCA) para jóvenes y mujeres cafetaleras, 2024–2025.</p></article>
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
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Los tres módulos</span><h2>Programa formativo</h2><p class="lead">La Escuela del Café nace en 2006 como <b>FORCAFE</b> (Fortalecimiento Cafetalero), la escuela de los futuros presidentes de las organizaciones; hoy se consolida con tres módulos.</p></div>
  <div class="grid grid-3">
    <article class="card reveal"><div class="card__ico">{I['chart']}</div><h3>1 · Administración de Organizaciones Exportadoras de Café</h3><p>Gestión, microfinanzas y comercialización para las organizaciones exportadoras.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['cup']}</div><h3>2 · Calidad — Cata y Barismo</h3><p>Análisis sensorial, protocolo SCA y preparación de café de especialidad.</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['leaf']}</div><h3>3 · Manejo Tecnológico de la Parcela</h3><p>EUDR, buenas prácticas de instalación y manejo de cafetales, e innovación sobre saberes ancestrales.</p></article>
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
  <div class="card reveal"><div class="card__ico">{I['venus']}</div><h3>Nuestra misión</h3><p>Empoderar a las mujeres y jóvenes líderes cafetaleras, garantizando su visibilización y el fortalecimiento de sus liderazgos en la cadena de valor, mediante cursos de capacitación en <b>microfinanzas</b> y <b>Administración de Organizaciones Exportadoras de Café</b>, entre otros.</p></div>
  <div class="card reveal" data-delay="120"><div class="card__ico">{I['users']}</div><h3>Valores del Comité</h3><ul class="values"><li>{I['chk']} Sororidad — apoyo mutuo entre las bases</li><li>{I['chk']} Transparencia — información clara y accesible</li><li>{I['chk']} Cooperación — trabajo conjunto por fines comunes</li></ul></div>
</div></section>
<section class="section"><div class="container"><div class="head-block center"><span class="eyebrow">Impacto en territorio</span><h2>Proyectos de desarrollo activos</h2></div><div class="grid grid-3">
  <article class="card reveal"><div class="card__ico">{I['chart']}</div><h3>Microcrédito y Ahorro</h3><p>Fondo de finanzas comunitarias para adquirir herramientas de campo y renovar parcelas.</p></article>
  <article class="card reveal" data-delay="80"><div class="card__ico">{I['cap']}</div><h3>Escuela de Liderazgo</h3><p>Capacitación en gestión administrativa de fincas, oratoria y toma de decisiones comunitarias.</p></article>
  <article class="card reveal" data-delay="160"><div class="card__ico">{I['leaf']}</div><h3>Diversificación de ingresos</h3><p>Apicultura, huertos orgánicos y comercialización de artesanías locales.</p></article>
</div></div></section>
<section class="section section--pattern"><div class="container about">
  <div class="about__media reveal"><div class="frame"><div class="mslider" data-mslider><img src="assets/img/photos/p_cumbre_ponente.jpg" alt="Ponente en la 1ra Cumbre Nacional de Mujeres Cafetaleras, Caranavi" class="is-active" loading="lazy"><img src="assets/img/photos/p_mujeres.jpg" alt="Productoras reunidas en la Cumbre de Mujeres" loading="lazy"><img src="assets/img/photos/p_mujeres2.jpg" alt="Certificación de productoras en la Cumbre" loading="lazy"></div></div><span class="pill">1ra Cumbre Nacional</span></div>
  <div class="about__content reveal" data-delay="120"><span class="eyebrow">4 y 5 de abril · Caranavi</span><h2>1ra Cumbre Nacional de Mujeres Cafetaleras</h2>
    <p class="lead">Bajo el lema <b>"Mujeres de cara al Bicentenario"</b>, la Cumbre reunió en el salón "Ex Cisne" de Caranavi a productoras de las cooperativas afiliadas para reconocer trayectorias, entregar certificaciones y proyectar la agenda de género y generacional de FECAFEB.</p>
  </div>
</div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Gobernanza</span><h2>Directorio del Comité de Mujeres</h2><p class="lead">Representantes vigentes electas por la Asamblea General de Bases.</p></div><div style="overflow-x:auto"><table class="ptable"><thead><tr><th>Nombre</th><th>Cargo</th><th>Cooperativa de base</th></tr></thead><tbody><tr><td>Sra. Yola Condori Álvarez</td><td class="score">Presidenta</td><td>Cooperativa Antofagasta</td></tr><tr><td>Sra. Mari Luz Kalla Osco</td><td class="score">Tesorera</td><td>Cooperativa San Juan</td></tr><tr><td>Sra. Elsa Calle</td><td class="score">Secretaria</td><td>Cooperativa CENAPROC</td></tr></tbody></table></div></div></section>
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
  <p class="lead">La marca de café de especialidad de FECAFEB enfocada en la calidad del café de las productoras. Kullaka muestra la <b>esencia de la mujer en la taza</b>: el trabajo, el compromiso y la dedicación, reflejados en los sabores más complejos y exóticos de cada taza.</p>
  <div class="hero__actions" style="margin-top:1.2rem"><a href="tienda.html" class="btn btn--gold">Comprar / hacer pedido</a><a href="comite-mujeres.html" class="btn btn--ghost">Comité de Mujeres</a></div></div>
</div></section>
<section class="section section--tint"><div class="container grid grid-3">
  <article class="card reveal"><div class="card__ico">{I['venus']}</div><h3>Identidad de mujer</h3><p>Café producido y liderado por las mujeres cafetaleras de Bolivia.</p></article>
  <article class="card reveal" data-delay="80"><div class="card__ico">{I['bean']}</div><h3>Especialidad de altura</h3><p>Origen Yungas, orgánico, perfiles de taza diferenciados.</p></article>
  <article class="card reveal" data-delay="160"><div class="card__ico">{I['globe']}</div><h3>Mercado nacional e internacional</h3><p>Comercialización con identidad y trazabilidad de impacto.</p></article>
</div></section>
<section class="section"><div class="container feature"><div class="feature__media reveal"><img class="photo" src="assets/img/logo-kullaka.png" alt="Kullaka de Altura — Edición Limitada"></div><div class="feature__content reveal" data-delay="120"><span class="tag tag--gold">Edición limitada de lujo</span><h2>Kullaka de Altura</h2><p class="lead">En homenaje a la 1ra Cumbre de Mujeres Cafetaleras de Bolivia — “Mujeres de cara al Bicentenario”.</p><ul><li>{I['chk']} Variedad Catuai, cultivada a 1.700 m.s.n.m.</li><li>{I['chk']} Proceso natural, con secado artesanal</li><li>{I['chk']} Aroma: flores blancas y frutos rojos</li><li>{I['chk']} En boca: frutas tropicales, notas de vino, chocolate intenso y resabio jugoso</li></ul><p class="form__note">Su compra apoya directamente a las mujeres que cultivan el futuro del café boliviano · Bolivia 2025.</p></div></div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Compradores</span><h2>Lleve Kullaka a su mercado</h2><p class="lead">Café con historia, calidad y respaldo institucional de FECAFEB.</p></div><a href="contacto.html" class="btn btn--gold btn--lg">Solicitar información comercial</a></div></section>
"""
page("kullaka.html","servicios.html","Marca Kullaka · FECAFEB","Café Kullaka, la marca de especialidad con identidad de mujer de FECAFEB. Esencia que abraza.",kul,
     ("Servicios / Marca Kullaka","Marca Kullaka","Café de especialidad con identidad de mujer."))

# ===================== TIENDA / PEDIDOS =====================
tienda = f"""
<section class="section section--pattern"><div class="container">
  <div class="head-block"><span class="eyebrow">Tienda</span><h2>Café de la Federación — pedidos</h2>
  <p class="lead">Compre café <b>Kullaka</b> (tostado) y <b>café verde de exportación</b>. Agregue productos a su pedido; para finalizar, regístrese o inicie sesión como comprador.</p></div>
  <div class="shop-grid" id="shopGrid"></div>
  <p class="form__note" style="margin-top:1.2rem">Precios referenciales en USD. El pedido es una solicitud de cotización; FECAFEB confirma disponibilidad, precios FOB y logística.</p>
</div></section>
<section class="section section--tint"><div class="container">
  <div class="head-block center"><span class="eyebrow">¿Cómo pedir?</span><h2>Pedidos para el exterior en 4 pasos</h2></div>
  <div class="grid grid-4">
    <article class="card reveal"><div class="card__ico">{I['cup']}</div><h3>1. Explore</h3><p>Revise el catálogo y agregue productos a su pedido.</p></article>
    <article class="card reveal" data-delay="80"><div class="card__ico">{I['users']}</div><h3>2. Regístrese</h3><p>Cree su cuenta de comprador (queda en revisión para ser dada de alta por FECAFEB).</p></article>
    <article class="card reveal" data-delay="160"><div class="card__ico">{I['doc']}</div><h3>3. Solicite</h3><p>Envíe su pedido como solicitud de cotización.</p></article>
    <article class="card reveal" data-delay="240"><div class="card__ico">{I['globe']}</div><h3>4. Exporte</h3><p>Confirmamos disponibilidad, precios FOB, trazabilidad EUDR y logística.</p></article>
  </div>
</div></section>
"""
page("tienda.html","servicios.html","Tienda · FECAFEB","Compra y pedidos de café boliviano (Kullaka y café verde de exportación) para compradores del exterior.",tienda,
     ("Servicios / Tienda","Tienda & pedidos","Café Kullaka y café verde de exportación. Pedidos con registro de comprador."))


# ===================== TAZA PRESIDENCIAL =====================
results=[("1°","Senda Salvaje — Deysi Ramos Carrillo","Caranavi, La Paz","Geisha","89,60"),("2°","Finca San José — Estefanía Parra de Callejas","Villa Tunari, Cochabamba","Catuaí Rojo","89,00"),("3°","Café Amazonia — Filomena Mamani Mamani","Caranavi, La Paz","Java","88,90"),("4°","Café Villa 32 — Camila Barrientos Ascarrunz","Caranavi, La Paz","Java","88,45"),("5°","Finca Marcelina — Marcelina Colque Gabriel","Villa Tunari, Cochabamba","Catuaí Rojo","88,25"),("6°","Finca Calani — Juan Calani Vargas","Villa Tunari, Cochabamba","Catuaí Rojo","88,23"),("7°","Finca Callejas — Valeriano Callejas Ticona","Villa Tunari, Cochabamba","Catuaí Rojo","87,75")]
rows=''.join(f'<tr><td class="rank">{r}</td><td>{c}</td><td>{z}</td><td>{v}</td><td class="score">{s}</td></tr>' for r,c,z,v,s in results)
taza = f"""
<section class="section"><div class="container about">
  <div class="about__media reveal"><div class="frame">{img('specialty','Catación de café — Taza Presidencial')}</div><span class="pill">Estándares SCA</span></div>
  <div class="about__content reveal" data-delay="120"><span class="eyebrow">Orgullo boliviano</span><h2>Taza de Calidad Café Presidencial</h2>
    <p class="lead">Torneo nacional organizado desde 2015 por el <b>Ministerio de Relaciones Exteriores</b> y el <b>Ministerio de Desarrollo Rural y Tierras</b>, en coordinación con el Consejo Nacional de Productores de Café y FECAFEB, bajo estándares de catación SCA. La edición VIII (2022) recibió 270 muestras de La Paz, Cochabamba y Santa Cruz, con subasta internacional de los mejores lotes.</p>
    <ul class="values" style="margin-top:1.2rem"><li>{I['chk']} Convocatoria digitalizada y reglamentos descargables</li><li>{I['chk']} Resultados oficiales y perfiles reales de los productores ganadores</li><li>{I['chk']} Directorio de jueces nacionales e internacionales</li></ul>
  </div>
</div></section>
<section class="section"><div class="container"><div class="head-block center"><span class="eyebrow">Cronograma 2026–2027</span><h2>Ciclo de 10 fases de trabajo</h2><p class="lead">Ruta técnica y comercial coordinada con el Gobierno Autónomo Municipal de Caranavi (GAM), sede central del torneo.</p></div><div class="phases"><article class="phase reveal"><div class="phase__n">01</div><div class="phase__b"><span class="phase__date">Mié. 8 de julio</span><h3>Lanzamiento</h3><p>Presentación pública del plan nacional y apertura de inscripciones.</p></div></article><article class="phase reveal"><div class="phase__n">02</div><div class="phase__b"><span class="phase__date">Julio–agosto</span><h3>Capacitaciones técnicas</h3><p>Talleres de poscosecha, secado y cata en Caranavi y zonas solicitantes.</p></div></article><article class="phase reveal"><div class="phase__n">03</div><div class="phase__b"><span class="phase__date">3 de agosto</span><h3>Plantel de jurados</h3><p>Convocatoria y formación de catadores con capacitador internacional.</p></div></article><article class="phase reveal"><div class="phase__n">04</div><div class="phase__b"><span class="phase__date">3–10 de agosto</span><h3>Recepción de muestras</h3><p>Acopio oficial de microlotes coordinado con el GAM Caranavi.</p></div></article><article class="phase reveal"><div class="phase__n">05</div><div class="phase__b"><span class="phase__date">7–14 de septiembre</span><h3>Preselección</h3><p>Trillado, codificación ciega e inicio de la cata.</p></div></article><article class="phase reveal"><div class="phase__n">06</div><div class="phase__b"><span class="phase__date">5–12 de octubre</span><h3>Etapa nacional</h3><p>Mesas de cata con jueces y productores finalistas.</p></div></article><article class="phase reveal"><div class="phase__n">07</div><div class="phase__b"><span class="phase__date">2–10 de noviembre</span><h3>Chuquiago Marka</h3><p>Feria comercial, fase internacional y campeonatos de barismo.</p></div></article><article class="phase reveal"><div class="phase__n">08</div><div class="phase__b"><span class="phase__date">Desde el 10 de nov.</span><h3>Degustaciones</h3><p>Promoción del Top 10 en cafeterías de especialidad.</p></div></article><article class="phase reveal"><div class="phase__n">09</div><div class="phase__b"><span class="phase__date">15–22 de noviembre</span><h3>Subasta electrónica</h3><p>Puja global en tiempo real por los lotes de rango presidencial.</p></div></article><article class="phase reveal"><div class="phase__n">10</div><div class="phase__b"><span class="phase__date">Dic. 2026 – ene. 2027</span><h3>Procesado y exportación</h3><p>Trillado, envasado al vacío y despacho a compradores globales.</p></div></article></div></div></section>
<section class="section section--tint"><div class="container"><div class="head-block center"><span class="eyebrow">Resultados oficiales</span><h2>VIII Torneo Nacional — Café Presidencial 2022</h2><p class="lead">Deysi Ramos Carrillo y su esposo Carmelo Yujra (Senda Salvaje, Caranavi) se impusieron con un café Geisha de 89,60 puntos, cultivado a 1.750 msnm bajo sombra inga. El segundo puesto fue para Estefanía Parra de Callejas (Finca San José, Villa Tunari), migrante potosina que encontró en el café de especialidad una nueva fuente de ingreso para su familia.</p></div>
  <div style="overflow-x:auto"><table class="ptable"><thead><tr><th>Puesto</th><th>Productor / Finca</th><th>Zona</th><th>Variedad</th><th>Puntaje</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="form__note" style="margin-top:1rem">Fuente: Fichas de Ganadores VIII Torneo Nacional Taza de Calidad "Café Presidencial" 2022.</p>
</div></section>
<section class="section"><div class="container"><div class="head-block"><span class="eyebrow">Documentos del torneo</span><h2>Reglamentos y bases</h2><p class="lead">Documentos oficiales del Torneo Taza de Calidad Café Presidencial, disponibles para descarga.</p></div><div class="docs"><div class="doc reveal"><div class="doc__ico">{I['doc']}</div><div class="doc__b"><b>Reglamento del Torneo 2022</b><span>Bases y reglas de participación</span></div><a class="doc__dl" href="assets/docs/reglamento-torneo-2022.pdf" download>{I['dl']} Descargar</a></div><div class="doc reveal"><div class="doc__ico">{I['doc']}</div><div class="doc__b"><b>Reglamento de Subasta 2022</b><span>Procedimiento de subasta electrónica de microlotes</span></div><a class="doc__dl" href="assets/docs/reglamento-subasta-2022.pdf" download>{I['dl']} Descargar</a></div><div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>Más publicaciones del torneo</b><span>Repositorio · Biblioteca</span></div><a class="doc__dl" href="publicaciones.html#publicaciones">Ver repositorio →</a></div></div></div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Convocatoria abierta</span><h2>Participe en la Taza Presidencial 2026–2027</h2><p class="lead">Inscriba su lote y compita por llegar a la subasta internacional.</p></div><a href="contacto.html" class="btn btn--gold btn--lg">Ver convocatoria</a></div></section>
"""
page("taza-presidencial.html","servicios.html","Taza Presidencial · FECAFEB","Torneo Nacional Taza Presidencial de Bolivia: catación SCA, resultados y subasta internacional.",taza,
     ("Servicios / Taza Presidencial","Taza Presidencial","El evento cumbre del café boliviano, bajo estándares SCA."))

# ===================== BIBLIOTECA · PUBLICACIONES =====================
import json as _json
# Publicaciones reales (portada + PDF descargable + categoría para taxonomía)
PUBS=[
 ("Estatuto Orgánico y Reglamento Interno","Institucional","c_estatuto.jpg","estatuto.pdf","Instrumento constitutivo de FECAFEB — Testimonio N° 092/2026."),
 ("Plan Estratégico Institucional 2023–2027","Institucional","c_pei.jpg","pei-2023-2027.pdf","Objetivos, líneas estratégicas y hoja de ruta de la Federación."),
 ("Reglamento del Torneo Taza Presidencial 2022","Taza Presidencial","c_reglamento_torneo.jpg","reglamento-torneo-2022.pdf","Reglas del torneo nacional de calidad de café boliviano."),
 ("Reglamento de Subasta de Café 2022","Taza Presidencial","c_reglamento_subasta.jpg","reglamento-subasta-2022.pdf","Procedimiento de la subasta electrónica de microlotes."),
 ("Kullaka de Altura — Edición Limitada","Marca Kullaka","c_kullaka.jpg","kullaka.pdf","Ficha del café de especialidad con identidad de mujer."),
]
_cats=[]
for _,c,_,_,_ in PUBS:
    if c not in _cats: _cats.append(c)
chips='<button class="chip is-active" data-cat="all">Todas</button>'+''.join(f'<button class="chip" data-cat="{c}">{c}</button>' for c in _cats)
def pub_card(t,cat,cover,pdf,desc):
    return (f'<article class="pub reveal" data-cat="{cat}" data-title="{t.lower()}">'
            f'<div class="pub__cover"><img src="assets/img/covers/{cover}" alt="{t}" loading="lazy"><span class="pub__cat">{cat}</span></div>'
            f'<div class="pub__b"><h3>{t}</h3><p>{desc}</p><div class="pub__act">'
            f'<button class="btn btn--sm btn--ghost" data-pdf="assets/docs/{pdf}" data-title="{t}">{I["doc"]} Ver</button>'
            f'<a class="btn btn--sm btn--gold" href="assets/docs/{pdf}" download>{I["dl"]} Descargar</a>'
            f'</div></div></article>')
pubcards=''.join(pub_card(*p) for p in PUBS)
# Normativa (enlaces oficiales reales)
NORM=[("Ley N° 511 — Adhesión al Convenio Internacional del Café 2007","SENAVEX · Normativa del café","https://senavex.gob.bo/normativa-cafe/"),
      ("Sistema de autoevaluación y cumplimiento EUDR","SENAVEX · AL-INVEST Verde (UE)","https://autoevaluacioneudr.senavex.gob.bo/"),
      ("Reglamento (UE) 2023/1115 — Productos libres de deforestación","Comisión Europea","https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en"),
      ("Estatuto Orgánico — Testimonio N° 092/2026","Instrumento legal · descarga PDF","assets/docs/estatuto.pdf")]
def norm_row(t,sub,href):
    ext = href.startswith("http")
    lab = "Visitar →" if ext else "Descargar"
    at = ' target="_blank" rel="noopener"' if ext else ' download'
    return (f'<div class="doc reveal"><div class="doc__ico">{I["shield"] if ext else I["doc"]}</div>'
            f'<div class="doc__b"><b>{t}</b><span>{sub}</span></div>'
            f'<a class="doc__dl" href="{href}"{at}>{lab}</a></div>')
normlist=''.join(norm_row(*n) for n in NORM)
publicaciones = f"""
<section class="section section--pattern" id="publicaciones"><div class="container">
  <div class="head-block"><span class="eyebrow">Repositorio · Publicaciones</span><h2>Documentos y descargas</h2><p class="lead">Documentos institucionales y técnicos de FECAFEB. Filtre por categoría o busque por título; visualice en línea o descargue el PDF.</p></div>
  <div class="repo-bar"><div class="chips" data-pubfilter>{chips}</div><label class="repo-search">{I['globe']}<input type="search" id="pubSearch" placeholder="Buscar publicación…" aria-label="Buscar publicación"></label></div>
  <div class="pubs" id="pubGrid">{pubcards}</div>
  <p class="repo-empty" id="pubEmpty" hidden>No se encontraron publicaciones con ese criterio.</p>
</div></section>
<section class="section section--tint" id="normativa"><div class="container">
  <div class="head-block"><span class="eyebrow">Normativa</span><h2>Leyes, reglamentos y cumplimiento</h2><p class="lead">Marco legal nacional e internacional del café boliviano y enlaces oficiales de cumplimiento.</p></div>
  <div class="docs">{normlist}</div>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Biblioteca</span><h2>Explore también fotos y videos</h2></div><div class="hero__actions" style="justify-content:center"><a class="btn btn--gold btn--lg" href="fotos.html">Ver galería de fotos</a><a class="btn btn--ghost btn--lg" href="videos.html">Ver videoteca</a></div></div></section>
"""
page("publicaciones.html","publicaciones.html","Publicaciones · Biblioteca FECAFEB","Repositorio de documentos institucionales y técnicos de FECAFEB, con buscador, categorías y descargas en PDF.",publicaciones,
     ("Biblioteca / Publicaciones","Publicaciones","Repositorio documental de FECAFEB: institucional, normativa y técnica."),
     extra_js='<script src="js/repo.js"></script>')

# ===================== BIBLIOTECA · FOTOS =====================
_caps=_json.load(open("assets/img/gallery/_captions.json",encoding="utf-8"))
GKEYS=["g01","g02","g03","g04","g05","g06","g07","g08","g09","g10","g11","g12","g13","g14","g15","g16"]
gitems=''.join(
  f'<figure class="gcell reveal" data-full="assets/img/gallery/{k}.jpg" data-cap="{_caps.get(k,"")}">'
  f'<img src="assets/img/gallery/{k}.jpg" alt="{_caps.get(k,"")}" loading="lazy">'
  f'<figcaption>{_caps.get(k,"")}</figcaption></figure>' for k in GKEYS)
fotos = f"""
<section class="section"><div class="container">
  <div class="head-block"><span class="eyebrow">Galería</span><h2>Fotografías de FECAFEB</h2><p class="lead">Archivo real de la Federación: Cumbre de Mujeres Cafetaleras, Taza / Café Presidencial y actividades de campo. Haga clic en cualquier imagen para ampliarla.</p></div>
  <div class="gallery-grid">{gitems}</div>
</div></section>
"""
page("fotos.html","publicaciones.html","Fotos · Biblioteca FECAFEB","Galería fotográfica real de FECAFEB: Cumbre de Mujeres, Taza Presidencial y actividades de campo.",fotos,
     ("Biblioteca / Fotos","Galería de fotos","Archivo fotográfico real de la Federación."),
     extra_js='<script src="js/lightbox.js"></script>')

# ===================== BIBLIOTECA · VIDEOS =====================
VIDS=[("Cumbre de Mujeres Cafetaleras — CMCB25","Resumen del encuentro nacional de productoras 2025.","g01"),
      ("Taza / Café Presidencial — etapa internacional","Catación y subasta con jurados internacionales.","g05"),
      ("Escuela del Café — catación y barismo","Formación técnica de la familia cafetalera.","g06")]
vcards=''.join(
  f'<article class="vcard reveal"><div class="vcard__cover"><img src="assets/img/gallery/{k}.jpg" alt="{t}" loading="lazy"><span class="vcard__play" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span><span class="vcard__badge">Video</span></div>'
  f'<div class="vcard__b"><h3>{t}</h3><p>{d}</p></div></article>' for t,d,k in VIDS)
videos = f"""
<section class="section"><div class="container">
  <div class="head-block"><span class="eyebrow">Videoteca</span><h2>Videos de FECAFEB</h2><p class="lead">Material audiovisual institucional. La reproducción se integrará con el gestor de contenidos (CMS); el archivo original de alta resolución permanece en el repositorio de la Federación.</p></div>
  <div class="vgrid">{vcards}</div>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Más videos</span><h2>Síganos en Facebook</h2><p class="lead">Publicamos transmisiones y videos de nuestras actividades en el canal oficial de FECAFEB.</p></div><a class="btn btn--gold btn--lg" href="https://www.facebook.com/profile.php?id=100091538775267" target="_blank" rel="noopener">Ver videos en Facebook →</a></div></section>
"""
page("videos.html","publicaciones.html","Videos · Biblioteca FECAFEB","Videoteca institucional de FECAFEB: Cumbre de Mujeres, Taza Presidencial y Escuela del Café.",videos,
     ("Biblioteca / Videos","Videoteca","Material audiovisual de la Federación."))

# biblioteca.html -> redirección a publicaciones

# ===================== PRENSA =====================
comun=('<div class="comunicados">'
 '<div class="comunicado reveal"><time>15 jun 2026</time><div><b>Convocatoria Taza Presidencial 2026–2027</b><span>Apertura de inscripciones para cooperativas y asociaciones afiliadas.</span></div><a href="taza-presidencial.html">Ver convocatoria →</a></div>'
 '<div class="comunicado reveal"><time>28 may 2026</time><div><b>Lineamientos de cumplimiento EUDR para afiliadas</b><span>Plazos y requisitos de georreferenciación de parcelas.</span></div><a href="trazabilidad.html">Ver detalles →</a></div>'
 '<div class="comunicado reveal"><time>10 abr 2026</time><div><b>Asamblea General Ordinaria — citación</b><span>Orden del día y documentación para las organizaciones afiliadas.</span></div><a href="quienes-somos.html#instancias">Más información →</a></div>'
 '</div>')
EXT=[("El Deber","Café boliviano gana espacio en ferias europeas","Cobertura sobre exportación y calidad del café de los Yungas.","farm"),
     ("Los Tiempos","Mujeres cafetaleras impulsan la marca Kullaka","Reportaje sobre el liderazgo femenino en la cadena del café.","woman"),
     ("Página Siete","Bolivia se prepara para el Reglamento EUDR","Análisis del impacto de la normativa europea en el sector.","andes")]
def ext_card(src,t,x,k):
    return f'<article class="news__item reveal"><div class="news__cover"><span class="badge">{src}</span><img src="{U(k,640)}" alt="{t}" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div><div class="news__body"><time>Medios · 2026</time><h3>{t}</h3><p>{x}</p><a href="#">Ver nota →</a></div></article>'
extnews=''.join(ext_card(*e) for e in EXT)
prensa = f"""
<section class="section" id="notas"><div class="container">
  <div class="head-block"><span class="eyebrow">Notas de prensa · FECAFEB</span><h2>Comunicación oficial</h2><p class="lead">Notas y actualidad emitidas por la Federación.</p></div>
  <div class="news">{NEWS_ALL}</div>
</div></section>
<section class="section section--tint" id="comunicados"><div class="container">
  <div class="head-block"><span class="eyebrow">Comunicados oficiales</span><h2>Comunicados</h2></div>
  {comun}
</div></section>
<section class="section" id="externas"><div class="container">
  <div class="head-block"><span class="eyebrow">Noticias externas</span><h2>FECAFEB en la web y redes</h2><p class="lead">Actividad, campañas y cobertura del café boliviano en nuestros canales oficiales y de aliados.</p></div>
  <div class="docs">
    <div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>Facebook · FECAFEB</b><span>Actividades, convocatorias y transmisiones en vivo</span></div><a class="doc__dl" href="https://www.facebook.com/profile.php?id=100091538775267" target="_blank" rel="noopener">Visitar →</a></div>
    <div class="doc reveal"><div class="doc__ico">{I['share']}</div><div class="doc__b"><b>Instagram · @fecafeb</b><span>Fotografía y campañas del café boliviano</span></div><a class="doc__dl" href="https://www.instagram.com/fecafeb/" target="_blank" rel="noopener">Visitar →</a></div>
  </div>
</div></section>
"""
page("prensa.html","prensa.html","Prensa · FECAFEB","Notas de prensa, comunicados oficiales, noticias en medios y boletín semanal de FECAFEB.",prensa,
     ("Prensa","Prensa & noticias","Comunicación oficial, cobertura en medios y boletín del café boliviano."))
