/* FECAFEB · shop.js — Tienda, carrito y pedidos (demo). Registro/login simulado del comprador.
   Persistencia local (localStorage); en producción se conecta al backend/CRM. */
(function(){
  "use strict";
  var IMG="";
  var PRODUCTS=[
    {id:"k-caranavi",name:"Café Kullaka Tostado — Caranavi",tag:"Tostado · 250 g",desc:"Especialidad lavado, notas a chocolate y frutos rojos.",price:12,unit:"250 g",img:"assets/img/photos/p_kullaka.jpg"+IMG},
    {id:"k-apolo",name:"Café Kullaka — Mujeres de Apolo",tag:"Tostado · 250 g",desc:"Natural de altura del Comité de Mujeres, frutas tropicales y miel.",price:14,unit:"250 g",img:"assets/img/photos/p_mujeres2.jpg"+IMG},
    {id:"k-molido",name:"Café Kullaka Molido",tag:"Molido · 250 g",desc:"Molienda media, ideal para filtrado.",price:12,unit:"250 g",img:"assets/img/photos/p_barismo.jpg"+IMG},
    {id:"verde-shb",name:"Café Verde de Exportación — Lavado SHB",tag:"Exportación · saco 69 kg",desc:"Café verde oro trazable EUDR, listo para embarque.",price:310,unit:"saco 69 kg",img:"assets/img/photos/p_cafeverde.jpg"+IMG},
    {id:"verde-org",name:"Café Verde Orgánico de Especialidad",tag:"Exportación · saco 69 kg",desc:"Orgánico certificado, puntaje SCA 86+.",price:360,unit:"saco 69 kg",img:"assets/img/photos/p_cata.jpg"+IMG},
    {id:"set-yungas",name:"Set Degustación Yungas",tag:"Regalo · 3×100 g",desc:"Tres orígenes de los Yungas para descubrir perfiles.",price:20,unit:"3×100 g",img:"assets/img/photos/p_caranavi.jpg"+IMG}
  ];
  var CART_KEY="fecafeb_cart", USER_KEY="fecafeb_user", USERS_KEY="fecafeb_users";
  var $=function(s,c){return (c||document).querySelector(s);};
  var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));};
  function load(k,d){try{return JSON.parse(localStorage.getItem(k))||d;}catch(e){return d;}}
  function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
  var cart=load(CART_KEY,{});
  function count(){return Object.keys(cart).reduce(function(a,id){return a+cart[id];},0);}
  function total(){return Object.keys(cart).reduce(function(a,id){var p=byId(id);return a+(p?p.price*cart[id]:0);},0);}
  function byId(id){for(var i=0;i<PRODUCTS.length;i++)if(PRODUCTS[i].id===id)return PRODUCTS[i];return null;}
  function money(n){return "$"+n.toLocaleString("en-US");}
  function badge(){ $$(".cartcount").forEach(function(b){var n=count();b.textContent=n;b.setAttribute("data-n",n);}); }

  function renderShop(){
    var grid=$("#shopGrid"); if(!grid) return;
    grid.innerHTML=PRODUCTS.map(function(p){
      return '<article class="product"><div class="product__img"><span class="product__tag">'+p.tag+'</span>'
        +'<img src="'+p.img+'" alt="'+p.name+'" loading="lazy" onerror="this.style.display=&quot;none&quot;"></div>'
        +'<div class="product__b"><h3>'+p.name+'</h3><p>'+p.desc+'</p>'
        +'<div class="product__row"><span class="product__price">'+money(p.price)+' <small>/ '+p.unit+'</small></span>'
        +'<button class="addbtn" data-add="'+p.id+'"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6h15l-1.5 9h-12z"/><circle cx="9" cy="20" r="1"/><circle cx="18" cy="20" r="1"/><path d="M6 6 5 3H2"/></svg> Agregar</button></div></div></article>';
    }).join("");
    $$("[data-add]",grid).forEach(function(b){b.addEventListener("click",function(){add(b.getAttribute("data-add"));});});
  }
  function renderCart(){
    var body=$("#cartBody"); if(!body) return;
    var ids=Object.keys(cart);
    if(!ids.length){ body.innerHTML='<p class="cart-empty">Su pedido está vacío.<br>Agregue productos desde la tienda.</p>'; }
    else{
      body.innerHTML=ids.map(function(id){var p=byId(id);if(!p)return"";return ''+
        '<div class="cart-item"><img src="'+p.img+'" alt="'+p.name+'" onerror="this.style.display=&quot;none&quot;">'+
        '<div class="ci-b"><b>'+p.name+'</b><span>'+money(p.price)+' / '+p.unit+'</span>'+
        '<div class="qty"><button data-dec="'+id+'">−</button><span>'+cart[id]+'</span><button data-inc="'+id+'">+</button></div></div>'+
        '<button class="ci-rm" data-rm="'+id+'">Quitar</button></div>';}).join("");
    }
    var t=$("#cartTotal"); if(t) t.innerHTML='<span>Total estimado</span><span>'+money(total())+'</span>';
    $$("[data-inc]",body).forEach(function(b){b.onclick=function(){add(b.getAttribute("data-inc"));};});
    $$("[data-dec]",body).forEach(function(b){b.onclick=function(){dec(b.getAttribute("data-dec"));};});
    $$("[data-rm]",body).forEach(function(b){b.onclick=function(){delete cart[b.getAttribute("data-rm")];persist();};});
  }
  function persist(){ save(CART_KEY,cart); badge(); renderCart(); }
  function add(id){ cart[id]=(cart[id]||0)+1; persist(); openCart(); }
  function dec(id){ cart[id]=(cart[id]||0)-1; if(cart[id]<=0) delete cart[id]; persist(); }

  function openCart(){var d=$("#cartDrawer"),b=$("#cartBd");if(d){d.classList.add("open");b.classList.add("open");document.body.style.overflow="hidden";renderCart();}}
  function closeCart(){var d=$("#cartDrawer"),b=$("#cartBd");if(d){d.classList.remove("open");b.classList.remove("open");document.body.style.overflow="";}}

  /* ---- Auth (registro/login simulados) ---- */
  function currentUser(){return load(USER_KEY,null);}
  function openAuth(){var m=$("#authModal");if(m){m.classList.add("open");document.body.style.overflow="hidden";showPane("authLogin");}}
  function closeAuth(){var m=$("#authModal");if(m){m.classList.remove("open");document.body.style.overflow="";}}
  function showPane(id){$$(".modal__pane").forEach(function(p){p.classList.toggle("is-active",p.id===id);});
    $$(".modal__tabs button").forEach(function(b){b.classList.toggle("is-active",b.getAttribute("data-pane")===id);});}
  function setUser(u){save(USER_KEY,u);reflectUser();}
  function reflectUser(){
    var u=currentUser(); var slot=$("#userSlot");
    if(slot) slot.innerHTML = u ? '<span class="userchip">👤 '+u.name.split(" ")[0]+'</span>' : '';
  }
  function placeOrder(){
    var u=currentUser(); if(!u){openAuth();return;}
    var n=Object.keys(cart).length; if(!n) return;
    var ord="FCB-"+Date.now().toString().slice(-6);
    cart={}; persist(); closeCart();
    var m=$("#authModal"); showPane("authOk");
    var o=$("#orderNo"); if(o)o.textContent=ord;
    if(m){m.classList.add("open");document.body.style.overflow="hidden";}
  }

  document.addEventListener("DOMContentLoaded", function(){
    renderShop(); badge(); reflectUser();
    var cb=$("#cartBtn"); if(cb) cb.addEventListener("click",openCart);
    var cx=$("#cartClose"); if(cx) cx.addEventListener("click",closeCart);
    var bd=$("#cartBd"); if(bd) bd.addEventListener("click",closeCart);
    var co=$("#checkoutBtn"); if(co) co.addEventListener("click",placeOrder);
    // auth modal wiring
    $$(".modal__tabs button").forEach(function(b){b.addEventListener("click",function(){showPane(b.getAttribute("data-pane"));});});
    var ax=$("#authClose"); if(ax) ax.addEventListener("click",closeAuth);
    var abd=$("#authModal"); if(abd) abd.addEventListener("click",function(e){if(e.target===abd)closeAuth();});
    var rf=$("#regForm");
    if(rf) rf.addEventListener("submit",function(e){e.preventDefault();
      var u={name:$("#regName").value||"Comprador",email:$("#regEmail").value,country:$("#regCountry").value,company:$("#regCompany").value,approved:false};
      var users=load(USERS_KEY,[]); users.push(u); save(USERS_KEY,users); setUser(u); closeAuth();
      if(Object.keys(cart).length) placeOrder();
    });
    var lf=$("#logForm");
    if(lf) lf.addEventListener("submit",function(e){e.preventDefault();
      var email=$("#logEmail").value; var users=load(USERS_KEY,[]);
      var u=users.filter(function(x){return x.email===email;})[0] || {name:email.split("@")[0]||"Comprador",email:email};
      setUser(u); closeAuth(); if(Object.keys(cart).length) placeOrder();
    });
    var okc=$("#okClose"); if(okc) okc.addEventListener("click",function(){closeAuth();});
  });
})();
