/* FECAFEB · search.js — Búsqueda global del sitio (índice estático, sin backend) */
(function(){
  "use strict";
  var INDEX = [
    {t:"Inicio",d:"Página principal de FECAFEB",u:"index.html"},
    {t:"Quiénes Somos",d:"Misión, visión, valores, historia e instancias",u:"quienes-somos.html"},
    {t:"Directorio",d:"Directorio Ejecutivo Nacional",u:"quienes-somos.html#directorio"},
    {t:"Comité de Fiscalización",d:"Instancia de control",u:"quienes-somos.html#fiscalizacion"},
    {t:"Comité de Mujeres",d:"Mujeres cafetaleras de Bolivia",u:"comite-mujeres.html"},
    {t:"Afiliados",d:"Cooperativas, asociaciones y zonas productoras",u:"afiliados.html"},
    {t:"Trazabilidad EUDR",d:"Consulta pública de lote y cumplimiento UE 2023/1115",u:"trazabilidad.html"},
    {t:"Servicios",d:"Asistencia técnica, comercialización, sanidad",u:"servicios.html"},
    {t:"Escuela de Café",d:"Formación, catación y barismo",u:"escuela-cafe.html"},
    {t:"Marca Kullaka",d:"Café de especialidad con identidad de mujer",u:"kullaka.html"},
    {t:"Tienda / Pedidos",d:"Compra y pedidos de café para el exterior",u:"tienda.html"},
    {t:"Taza Presidencial",d:"Torneo nacional, catación SCA y resultados",u:"taza-presidencial.html"},
    {t:"Publicaciones",d:"Documentos, blog del café y comunicados",u:"publicaciones.html"},
    {t:"Noticias",d:"Actualidad y boletín semanal",u:"noticias.html"},
    {t:"Contacto",d:"Datos de contacto y formulario",u:"contacto.html"}
  ];
  function norm(s){return (s||"").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"");}
  document.addEventListener("DOMContentLoaded", function(){
    var btn=document.getElementById("searchBtn"), ov=document.getElementById("searchOv"),
        inp=document.getElementById("searchInput"), res=document.getElementById("searchRes"),
        cls=document.querySelector("#searchOv .esc, #searchClose");
    if(!btn||!ov) return;
    var ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/></svg>';
    function render(q){
      var nq=norm(q);
      var list = !nq ? INDEX : INDEX.filter(function(i){return norm(i.t+" "+i.d).indexOf(nq)>-1;});
      if(!list.length){ res.innerHTML='<div class="search-empty">Sin resultados para “'+q+'”.</div>'; return; }
      res.innerHTML=list.map(function(i){return '<a href="'+i.u+'"><span class="ico">'+ICON+'</span><span><b>'+i.t+'</b><span>'+i.d+'</span></span></a>';}).join("");
    }
    function open(){ ov.classList.add("open"); document.body.style.overflow="hidden"; render(""); setTimeout(function(){inp.focus();},120); }
    function close(){ ov.classList.remove("open"); document.body.style.overflow=""; inp.value=""; }
    btn.addEventListener("click", open);
    if(cls) cls.addEventListener("click", close);
    ov.addEventListener("click", function(e){ if(e.target===ov) close(); });
    inp.addEventListener("input", function(){ render(inp.value); });
    document.addEventListener("keydown", function(e){
      if(e.key==="Escape" && ov.classList.contains("open")) close();
      if((e.key==="/"||((e.ctrlKey||e.metaKey)&&e.key==="k")) && !ov.classList.contains("open")){
        var tag=(document.activeElement||{}).tagName;
        if(tag!=="INPUT"&&tag!=="TEXTAREA"){ e.preventDefault(); open(); }
      }
    });
  });
})();
