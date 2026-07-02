/* FECAFEB · maps.js — Mapa de zonas productoras (Leaflet + OpenStreetMap/CARTO) */
(function(){
  "use strict";
  document.addEventListener("DOMContentLoaded", function(){
    var el = document.getElementById("mapZonas");
    if(!el || typeof L === "undefined") return;
    var zonas = [
      {n:"Caranavi", dep:"La Paz", alt:"1.300–1.700 m", taza:"Chocolate, frutos rojos, cuerpo medio.", lat:-15.838, lng:-67.560},
      {n:"Coroico", dep:"La Paz", alt:"1.200–1.700 m", taza:"Dulzor a caña, cítricos suaves.", lat:-16.190, lng:-67.730},
      {n:"Franz Tamayo (Apolo)", dep:"La Paz", alt:"1.400–1.800 m", taza:"Frutas tropicales y miel, acidez vibrante, cafés de altura.", lat:-14.720, lng:-68.420},
      {n:"Palos Blancos", dep:"La Paz", alt:"800–1.300 m", taza:"Cuerpo pronunciado, notas a frutos secos.", lat:-15.620, lng:-67.180},
      {n:"Chapare", dep:"Cochabamba", alt:"600–1.200 m", taza:"Dulce, baja acidez.", lat:-16.900, lng:-65.400},
      {n:"Caballero", dep:"Santa Cruz", alt:"1.500–1.900 m", taza:"Floral, acidez cítrica.", lat:-18.000, lng:-64.300}
    ];
    var map = L.map(el, {scrollWheelZoom:false, attributionControl:true}).setView([-16.3,-66.8], 6);
    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution:'&copy; OpenStreetMap &middot; &copy; CARTO', subdomains:"abcd", maxZoom:19
    }).addTo(map);
    var pin = L.divIcon({className:"", html:'<div style="width:18px;height:18px;border-radius:50% 50% 50% 0;background:#6E0D12;transform:rotate(-45deg);border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.4)"></div>', iconSize:[18,18], iconAnchor:[9,18]});
    var panel = document.getElementById("zonaInfo");
    function render(z){
      if(!panel) return;
      panel.innerHTML =
        '<div class="zona-info__hd"><div class="k">Zona productora</div><h3>'+z.n+'</h3></div>'+
        '<div class="zona-info__bd">'+
        '<div class="zona-info__row"><div class="k">Altitud</div><div class="v">'+z.alt+'</div></div>'+
        '<div class="zona-info__row"><div class="k">Departamento</div><div class="v">'+z.dep+'</div></div>'+
        '<div class="zona-info__row"><div class="k">Perfil de taza</div><div class="v sm">'+z.taza+'</div></div>'+
        '</div>';
    }
    zonas.forEach(function(z, i){
      var m = L.marker([z.lat, z.lng], {icon:pin, title:z.n}).addTo(map);
      m.on("click", function(){ render(z); map.panTo([z.lat, z.lng]); });
      if(i===2) render(z); // por defecto Apolo
    });
    setTimeout(function(){ map.invalidateSize(); }, 200);

    // ---- Mapa de la oficina de FECAFEB (Contacto) ----
    var oe = document.getElementById("mapOffice");
    if (oe && typeof L !== "undefined") {
      var off = [-16.5045, -68.1631]; // El Alto · La Paz (aprox. Av. Juan Pablo II)
      var om = L.map(oe, {scrollWheelZoom:false}).setView(off, 14);
      L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",{attribution:"&copy; OpenStreetMap &middot; &copy; CARTO",subdomains:"abcd",maxZoom:19}).addTo(om);
      var opin = L.divIcon({className:"",html:'<div style="width:18px;height:18px;border-radius:50% 50% 50% 0;background:#4E342E;transform:rotate(-45deg);border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.4)"></div>',iconSize:[18,18],iconAnchor:[9,18]});
      L.marker(off,{icon:opin}).addTo(om).bindPopup("FECAFEB · Av. Juan Pablo II 2974, El Alto");
      setTimeout(function(){ om.invalidateSize(); }, 200);
    }

  });
})();
