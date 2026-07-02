/* FECAFEB · trace.js — Consulta pública de trazabilidad por lote (demo, datos de ejemplo) */
(function(){
  "use strict";
  var DB = {
    "LOT-000123":{coop:"ASOCAFE Taipiplaya",com:"Comunidad Taipiplaya",region:"Caranavi · La Paz",prod:"Productor verificado (anonimizado)",camp:"Campaña 2025–2026",cos:"12 jul 2025",proc:"Lavado",vol:"1.380 kg",sca:"86,5",alt:"1.560 msnm",area:"2,4 ha",vari:"Caturra / Typica",sis:"Bajo sombra (SAF)",dds:"DDS-BO-2026-000123",ddsf:"14 ago 2025",certs:["Orgánica UE/USDA","Fairtrade FLO"],lat:-15.8386,lng:-67.5603,prodName:"Café Kullaka — Caranavi 250 g",img:"https://images.unsplash.com/photo-1521302080334-4bebac2763a6?auto=format&fit=crop&w=400&q=70"},
    "LOT-000456":{coop:"Coop. Antofagasta",com:"Munaypata",region:"Coroico · La Paz",prod:"Productor verificado (anonimizado)",camp:"Campaña 2025–2026",cos:"3 ago 2025",proc:"Honey",vol:"920 kg",sca:"87,75",alt:"1.640 msnm",area:"1,8 ha",vari:"Java / Geisha",sis:"Agroforestal",dds:"DDS-BO-2026-000456",ddsf:"21 ago 2025",certs:["Orgánica UE/USDA"],lat:-16.190,lng:-67.730,prodName:"Café Kullaka — Coroico Honey 250 g",img:"https://images.unsplash.com/photo-1447933601403-0c6688de566e?auto=format&fit=crop&w=400&q=70"},
    "LOT-000789":{coop:"Coop. San Juan",com:"Atén",region:"Apolo · La Paz",prod:"Comité de Mujeres (Kullaka)",camp:"Campaña 2025–2026",cos:"19 jul 2025",proc:"Natural",vol:"640 kg",sca:"88,25",alt:"1.720 msnm",area:"1,2 ha",vari:"Typica",sis:"Bajo sombra (SAF)",dds:"DDS-BO-2026-000789",ddsf:"30 ago 2025",certs:["Orgánica UE/USDA","Fairtrade FLO"],lat:-14.720,lng:-68.420,prodName:"Café Kullaka — Mujeres de Apolo 250 g",img:"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=70"}
  };
  function parcel(lat,lng){
    var d=0.0011;
    return [[lat+d,lng-d*0.6],[lat+d*0.75,lng+d],[lat-d*0.5,lng+d*1.15],[lat-d,lng-d*0.35],[lat-d*0.25,lng-d*1.1]];
  }
  document.addEventListener("DOMContentLoaded", function(){
    var form = document.getElementById("lotForm");
    var input = document.getElementById("lotInput");
    var box = document.getElementById("lotResult");
    if(!form || !box) return;
    var miniMap = null;
    function row(k,v){ return '<div class="kv"><span>'+k+'</span><b>'+v+'</b></div>'; }
    function card(d){
      var certs = d.certs.map(function(c){return '<span class="cert-tag">'+c+'</span>';}).join(" ");
      var prod = d.img ? '<div class="lot__product"><img src="'+d.img+'" alt="'+d.prodName+'" onerror="this.style.display=&quot;none&quot;"><div><b>Producto adquirido</b><span>'+d.prodName+' · imagen referencial</span></div></div>' : '';
      return ''+
      '<div class="lot__hd"><div class="lot__hd-left">'+(d.img?'<img class="lot__prod" src="'+d.img+'" alt="'+d.prodName+'" onerror="this.style.display=&quot;none&quot;">':'')+
      '<div><div class="k">Lote</div><h3>'+box.dataset.code+'</h3></div></div>'+
      '<div class="lot__verified"><span class="dot"></span> Verificado · EUDR</div></div>'+
      '<div class="lot__grid">'+
      '<div>'+prod+'<h4>Origen</h4>'+row("Cooperativa",d.coop)+row("Comunidad",d.com)+row("Región",d.region)+row("Productor",d.prod)+
      '<h4 style="margin-top:1.2rem">Cosecha y proceso</h4>'+
      '<div class="chipset"><div class="chip-card"><div class="k">Campaña</div><b>'+d.camp+'</b></div><div class="chip-card"><div class="k">Cosecha</div><b>'+d.cos+'</b></div></div>'+
      '<div class="chipset"><div class="chip-card"><div class="k">Proceso</div><b>'+d.proc+'</b></div><div class="chip-card"><div class="k">Volumen</div><b>'+d.vol+'</b></div></div>'+
      '<div class="lot__score"><span>Puntaje SCA</span><b>'+d.sca+'</b></div></div>'+
      '<div><h4>Parcela georreferenciada</h4><div id="lotMap"></div>'+
      '<div class="chipset" style="margin-top:.8rem"><div class="chip-card"><div class="k">Altitud</div><b>'+d.alt+'</b></div><div class="chip-card"><div class="k">Área</div><b>'+d.area+'</b></div></div>'+
      '<div class="chipset"><div class="chip-card"><div class="k">Variedad</div><b>'+d.vari+'</b></div><div class="chip-card"><div class="k">Sistema</div><b>'+d.sis+'</b></div></div></div>'+
      '</div>'+
      '<div class="lot__eudr"><div class="top"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.4 8.5 8 10 4.6-1.5 8-5 8-10V6Z"/><path d="m9 12 2 2 4-4"/></svg> Cumplimiento EUDR — libre de deforestación posterior al 31-dic-2020 (verificado)</div>'+
      '<div class="chipset" style="margin-top:.8rem"><div class="chip-card"><div class="k">N° Declaración DDS</div><b>'+d.dds+'</b></div><div class="chip-card"><div class="k">Fecha DDS</div><b>'+d.ddsf+'</b></div><div class="chip-card"><div class="k">Certificaciones</div><b>'+certs+'</b></div></div></div>'+
      '<div class="lot__actions"><a class="btn" href="#" onclick="return false">Descargar certificado PDF</a><a class="btn btn--ghost" href="#" onclick="return false">Verificar autenticidad</a></div>';
    }
    function show(code){
      var d = DB[code];
      box.dataset.code = code;
      if(!d){
        box.innerHTML = '<div class="lot__hd"><div><div class="k">Lote</div><h3>'+code+'</h3></div></div>'+
          '<div style="padding:1.6rem"><p>No se encontró el lote <b>'+code+'</b>. Verifique el código impreso en el empaque o escríbanos a <a href="mailto:fecafebfinanzas@gmail.com">fecafebfinanzas@gmail.com</a>.</p></div>';
        box.classList.add("show"); return;
      }
      box.innerHTML = card(d);
      box.classList.add("show");
      if(typeof L !== "undefined"){
        if(miniMap){ miniMap.remove(); miniMap = null; }
        var mEl = document.getElementById("lotMap");
        miniMap = L.map(mEl, {scrollWheelZoom:false, attributionControl:false}).setView([d.lat,d.lng], 16);
        L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",{subdomains:"abcd",maxZoom:19}).addTo(miniMap);
        var poly = L.polygon(parcel(d.lat,d.lng), {color:"#4E342E",weight:2,fillColor:"#C8962E",fillOpacity:.28}).addTo(miniMap);
        poly.bindTooltip("Parcela · "+d.area, {permanent:false});
        var pin = L.divIcon({className:"",html:'<div style="width:16px;height:16px;border-radius:50% 50% 50% 0;background:#4E342E;transform:rotate(-45deg);border:2px solid #fff"></div>',iconSize:[16,16],iconAnchor:[8,16]});
        L.marker([d.lat,d.lng],{icon:pin}).addTo(miniMap);
        miniMap.fitBounds(poly.getBounds().pad(0.8));
        setTimeout(function(){ miniMap.invalidateSize(); miniMap.fitBounds(poly.getBounds().pad(0.8)); }, 160);
      }
      box.scrollIntoView({behavior:"smooth", block:"nearest"});
    }
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var code = (input.value||"").trim().toUpperCase();
      if(!code) return;
      if(!/^LOT-/.test(code)) code = "LOT-" + code.replace(/^LOT-?/,"");
      show(code);
    });
  });
})();
