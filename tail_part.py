# ===================== PRENSA =====================
comun=('<div class="comunicados">'
 '<div class="comunicado reveal"><time>15 jun 2026</time><div><b>Convocatoria Taza Presidencial 2026–2027</b><span>Apertura de inscripciones para cooperativas y asociaciones afiliadas.</span></div><a href="#">Ver comunicado →</a></div>'
 '<div class="comunicado reveal"><time>28 may 2026</time><div><b>Lineamientos de cumplimiento EUDR para afiliadas</b><span>Plazos y requisitos de georreferenciación de parcelas.</span></div><a href="#">Ver comunicado →</a></div>'
 '<div class="comunicado reveal"><time>10 abr 2026</time><div><b>Asamblea General Ordinaria — citación</b><span>Orden del día y documentación para las organizaciones afiliadas.</span></div><a href="#">Ver comunicado →</a></div>'
 '</div>')
EXT=[("El Deber","Café boliviano gana espacio en ferias europeas","Cobertura sobre exportación y calidad del café de los Yungas.","farm"),
     ("Los Tiempos","Mujeres cafetaleras impulsan la marca Kullaka","Reportaje sobre el liderazgo femenino en la cadena del café.","hands"),
     ("Página Siete","Bolivia se prepara para el Reglamento EUDR","Análisis del impacto de la normativa europea en el sector.","field")]
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
  <div class="head-block"><span class="eyebrow">Noticias externas · medios</span><h2>El café boliviano en los medios</h2><p class="lead">Cobertura de medios de comunicación (enlaces de ejemplo).</p></div>
  <div class="news">{extnews}</div>
</div></section>
<section class="section" id="otras"><div class="container">
  <div class="head-block"><span class="eyebrow">Otras fuentes de prensa</span><h2>Más fuentes</h2><p class="lead">Gremios, organismos aliados y boletines (por completar).</p></div>
  <div class="docs">
    <div class="doc reveal"><div class="doc__ico">{I['globe']}</div><div class="doc__b"><b>CNCJ-Bolivia · Comercio Justo</b><span>Comunicación del sistema de comercio justo</span></div><a class="doc__dl" href="https://www.comerciojustobolivia.org.bo/" target="_blank" rel="noopener">Visitar →</a></div>
    <div class="doc reveal"><div class="doc__ico">{I['doc']}</div><div class="doc__b"><b>Boletín semanal FECAFEB</b><span>Precios, clima y convocatorias</span></div><a class="doc__dl" href="#">Suscribirse →</a></div>
  </div>
</div></section>
<section class="section section--accent"><div class="container center"><div class="head-block center"><span class="eyebrow">Boletín semanal</span><h2>Reciba precios, clima y convocatorias</h2><p class="lead">Resumen semanal para socios y aliados del café boliviano.</p></div>
  <form class="footer__news" data-demo style="max-width:420px;margin:0 auto"><input type="email" placeholder="Su correo" required aria-label="Correo"><button type="submit" aria-label="Suscribirse">→</button></form></div></section>
"""
page("prensa.html","prensa.html","Prensa · FECAFEB","Notas de prensa, comunicados oficiales, noticias en medios y boletín semanal de FECAFEB.",prensa,
     ("Prensa","Prensa & noticias","Comunicación oficial, cobertura en medios y boletín del café boliviano."))

# ===================== CONTACTO =====================
_PIN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
_TEL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3.08 5.18 2 2 0 0 1 5 3h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L9 11a16 16 0 0 0 4 4l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>'
_MAIL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg>'
_LOCK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg>'
contacto = f"""
<section class="section"><div class="container contact">
  <div class="contact__info">
    <div class="info-row reveal"><div class="ico">{_PIN}</div><div><b>Dirección</b><span>Av. Juan Pablo II 2974, El Alto · La Paz, Bolivia</span></div></div>
    <div class="info-row reveal" data-delay="60"><div class="ico">{_TEL}</div><div><b>Teléfono / WhatsApp</b><a href="https://wa.me/59171537365" target="_blank" rel="noopener">+591 71537365</a></div></div>
    <div class="info-row reveal" data-delay="120"><div class="ico">{_MAIL}</div><div><b>Correo</b><a href="mailto:fecafebfinanzas@gmail.com">fecafebfinanzas@gmail.com</a></div></div>
    <div class="info-row reveal" data-delay="180"><div class="ico">{_LOCK}</div><div><b>Portal Institucional</b><a href="#">Acceso para afiliados y técnicos (próximamente)</a></div></div>
    <div id="mapOffice" style="height:300px;border-radius:var(--radius);border:1px solid var(--line);z-index:1;margin-top:.4rem"></div>
  </div>
  <form class="form" data-demo>
    <div class="form__ok">✓ ¡Gracias! Su mensaje fue registrado. Le contactaremos pronto.</div>
    <div class="form__row"><div class="field"><label for="n">Nombre</label><input id="n" type="text" required placeholder="Su nombre"></div><div class="field"><label for="e">Correo</label><input id="e" type="email" required placeholder="correo@empresa.com"></div></div>
    <div class="form__row"><div class="field"><label for="p">Perfil</label><select id="p"><option>Comprador / importador (UE)</option><option>Cooperativa / asociación</option><option>Prensa</option><option>Otro</option></select></div><div class="field"><label for="c">País</label><input id="c" type="text" placeholder="Ej. Alemania"></div></div>
    <div class="form__row"><div class="field"><label for="tel">Teléfono</label><input id="tel" type="tel" placeholder="+591 ..."></div><div class="field"><label for="asu">Asunto</label><select id="asu"><option>Consulta comercial</option><option>Afiliación</option><option>Prensa</option><option>Escuela de Café</option><option>Otro</option></select></div></div>
    <div class="field"><label for="m">Mensaje</label><textarea id="m" required placeholder="Cuéntenos qué café busca o cómo podemos ayudarle…"></textarea></div>
    <button class="btn btn--lg" type="submit" style="width:100%">Enviar mensaje</button>
    <p class="form__note">Demo de plantilla — conectar a backend/CRM en la siguiente fase.</p>
  </form>
</div></section>
"""
page("contacto.html","contacto.html","Contacto · FECAFEB","Contáctenos: consultas comerciales, afiliación, prensa y Escuela de Café. El Alto, La Paz, Bolivia.",contacto,
     ("Contacto","Contacto","Hablemos de café: comercio, afiliación, prensa y formación."),
     extra_head=LEAFLET_CSS, extra_js=LEAFLET_JS + '<script src="js/maps.js"></script>')

# ===================== REDIRECCIONES (compatibilidad de URLs antiguas) =====================
def redir(fname, target):
    html=('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
          '<meta http-equiv="refresh" content="0; url=%s"><link rel="canonical" href="%s">'
          '<title>Redirigiendo…</title></head><body><p>Esta página se movió. '
          '<a href="%s">Ir a %s</a>.</p><script>location.replace("%s")</script></body></html>'
          % (target,target,target,target,target))
    open(fname,"w",encoding="utf-8").write(html)
redir("nosotros.html","quienes-somos.html")
redir("noticias.html","prensa.html")
redir("publicaciones.html","biblioteca.html")
redir("galeria.html","publicaciones.html")
