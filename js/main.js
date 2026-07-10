/* ===================================================================
   FECAFEB · main.js — Interacciones de la plantilla institucional
   ERLANGER-SOFT / Cognitio SRL
   Módulos: nav móvil · header scroll · scroll reveal · tabs ·
            galería lightbox · formularios · i18n ES/EN ·
            chatbot · botón WhatsApp · año dinámico
   =================================================================== */
(function () {
  "use strict";

  /* ---- Config editable por el cliente ---- */
  const CONFIG = {
    whatsapp: "59171537365",          // número CNCJ/FECAFEB (sin +)
    whatsappMsg: "Hola FECAFEB, deseo más información sobre el café boliviano.",
    email: "fecafebfinanzas@gmail.com",
    platformUrl: "#plataforma"        // reemplazar por URL real del sistema
  };

  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const on = (el, ev, fn) => el && el.addEventListener(ev, fn);

  document.addEventListener("DOMContentLoaded", init);

  function init() {
    wirePortalLinks();
    mobileNav();
    headerScroll();
    scrollReveal();
    heroParallax();
    heroSlider();
    counters();
    tabs();
    gallery();
    forms();
    i18n();
    chatbot();
    whatsapp();
    const y = $("#year"); if (y) y.textContent = new Date().getFullYear();
  }

  /* ---- Enlace del portal institucional (candado) ---- */
  function wirePortalLinks() {
    var targets = $$("a.tbtn--icon[aria-label='Portal Institucional'], .siderail a[title*='Portal Institucional']");
    targets.forEach(function (a) {
      a.setAttribute("href", "login.html");
      a.setAttribute("title", "Portal Institucional");
    });
  }

  /* ---- Parallax sutil del hero (respeta reduce-motion) ---- */
  function heroParallax() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const beans = $(".hero__beans");
    if (!beans) return;
    let ticking = false;
    on(window, "scroll", () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const y = window.scrollY;
        if (y < 900) beans.style.transform = "translateY(" + (y * 0.12) + "px)";
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---- Carrusel del hero ---- */
  function heroSlider() {
    const slider = $(".hero__slider");
    if (!slider) return;
    const slides = $$(".hero__slide", slider);
    const dotsBox = $(".hero__dots", slider);
    if (slides.length < 2) return;
    let i = 0, timer;
    slides.forEach((_, n) => {
      const b = document.createElement("button");
      b.setAttribute("aria-label", "Ir a la diapositiva " + (n + 1));
      if (n === 0) b.classList.add("is-active");
      b.addEventListener("click", () => go(n, true));
      dotsBox && dotsBox.appendChild(b);
    });
    const dots = dotsBox ? $$("button", dotsBox) : [];
    function go(n, manual) {
      slides[i].classList.remove("is-active");
      dots[i] && dots[i].classList.remove("is-active");
      i = (n + slides.length) % slides.length;
      slides[i].classList.add("is-active");
      dots[i] && dots[i].classList.add("is-active");
      if (manual) restart();
    }
    function restart() {
      clearInterval(timer);
      timer = setInterval(() => go(i + 1), 5500);
    }
    const prev = $(".hero__nav.prev", slider), next = $(".hero__nav.next", slider);
    on(prev, "click", () => go(i - 1, true));
    on(next, "click", () => go(i + 1, true));
    restart();
  }

  /* ---- Contadores animados ---- */
  function counters() {
    const els = $$("[data-count]");
    if (!els.length) return;
    const reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const run = el => {
      const target = parseFloat(el.dataset.count) || 0;
      const sep = el.hasAttribute("data-sep");
      const dur = 1400, t0 = performance.now();
      const fmt = v => sep ? Math.round(v).toLocaleString("es-BO") : Math.round(v).toString();
      if (reduceMotion) {
        el.textContent = fmt(target);
        return;
      }
      const tick = now => {
        const p = Math.min(1, (now - t0) / dur);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(target * eased);
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if (!("IntersectionObserver" in window)) { els.forEach(run); return; }
    const io = new IntersectionObserver((ents, obs) => {
      ents.forEach(e => { if (e.isIntersecting) { run(e.target); obs.unobserve(e.target); } });
    }, { threshold: 0.5 });
    els.forEach(e => io.observe(e));
  }

  /* ---- Navegación móvil ---- */
  function mobileNav() {
    const toggle = $(".nav__toggle");
    const menu = $("#menu");
    if (!toggle || !menu) return;
    on(toggle, "click", () => {
      const open = menu.classList.toggle("is-open");
      toggle.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open && window.innerWidth <= 860 ? "hidden" : "";
    });
    $$(".menu a").forEach(a => on(a, "click", () => {
      if (window.innerWidth <= 860 && !a.parentElement.classList.contains("has-sub")) {
        menu.classList.remove("is-open");
        toggle.classList.remove("is-open");
        document.body.style.overflow = "";
      }
    }));
  }

  /* ---- Sombra del header (+ section-spy solo en el Home) ---- */
  function headerScroll() {
    const header = $(".header");
    const isHome = !!$(".hero");
    const links = isHome ? $$('.menu > li > a[href^="index.html#"], .menu > li > a[href^="#"]') : [];
    const onScroll = () => {
      header && header.classList.toggle("is-scrolled", window.scrollY > 8);
      if (!isHome) return;
      let current = "";
      $$("section[id]").forEach(sec => { if (window.scrollY >= sec.offsetTop - 140) current = sec.id; });
      if (!current) return;
      links.forEach(l => {
        const href = l.getAttribute("href");
        if (href && href.includes("#"))
          l.parentElement.classList.toggle("is-active", href.endsWith("#" + current));
      });
    };
    on(window, "scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---- Aparición al hacer scroll ---- */
  function scrollReveal() {
    const els = $$(".reveal");
    if (!("IntersectionObserver" in window) || !els.length) {
      els.forEach(e => e.classList.add("in")); return;
    }
    // auto-stagger: reveals sin data-delay reciben un retraso escalonado entre hermanos
    const groups = new Map();
    els.forEach(e => { if (!e.dataset.delay) { const p = e.parentElement; const a = groups.get(p) || []; a.push(e); groups.set(p, a); } });
    groups.forEach(a => { if (a.length > 1) a.forEach((e, i) => { e.dataset.delay = String(Math.min(i * 70, 300)); }); });
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach(en => {
        if (en.isIntersecting) {
          en.target.style.transitionDelay = (en.target.dataset.delay || "0") + "ms";
          en.target.classList.add("in");
          obs.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    els.forEach(e => io.observe(e));
  }

  /* ---- Pestañas (Nosotros) ---- */
  function tabs() {
    $$("[data-tabs]").forEach(group => {
      const btns = $$(".tab", group);
      const panels = $$(".tab-panel", group);
      let idx = 0;
      let timer = null;
      const activate = (i) => {
        idx = i;
        btns.forEach(b => b.classList.remove("is-active"));
        panels.forEach(p => p.classList.remove("is-active"));
        btns[idx].classList.add("is-active");
        const panel = $("#" + btns[idx].dataset.target, group);
        panel && panel.classList.add("is-active");
      };
      const restart = () => {
        if (timer) clearInterval(timer);
        timer = setInterval(() => activate((idx + 1) % btns.length), 5000);
      };
      btns.forEach((btn, i) => on(btn, "click", () => { activate(i); restart(); }));
      if (btns.length > 1) restart();
    });
  }

  /* ---- Galería: lightbox ---- */
  function gallery() {
    const figs = $$(".gallery figure");
    if (!figs.length) return;
    let box;
    const open = (src, label) => {
      box = document.createElement("div");
      box.style.cssText = "position:fixed;inset:0;z-index:200;display:grid;place-items:center;" +
        "background:rgba(20,12,8,.88);backdrop-filter:blur(4px);padding:24px;cursor:zoom-out";
      const media = src
        ? '<img src="' + src + '" alt="' + label + '" style="width:100%;height:100%;object-fit:cover">'
        : '<div class="ph" style="height:100%"><span>' + label + '</span></div>';
      box.innerHTML = '<figure style="max-width:820px;width:100%;aspect-ratio:16/10;border-radius:18px;overflow:hidden;position:relative;' +
        'box-shadow:0 30px 80px rgba(0,0,0,.5)">' + media +
        '<figcaption style="position:absolute;left:0;right:0;bottom:0;padding:16px 20px;color:#fff;font-weight:700;' +
        'background:linear-gradient(0deg,rgba(0,0,0,.7),transparent)">' + label + '</figcaption></figure>';
      document.body.appendChild(box);
      document.body.style.overflow = "hidden";
      on(box, "click", close);
    };
    const close = () => { box && box.remove(); document.body.style.overflow = ""; };
    figs.forEach(f => on(f, "click", () => {
      const im = $("img", f), cap = $("figcaption", f);
      open(im ? im.getAttribute("src") : "", cap ? cap.textContent : "FECAFEB");
    }));
    on(document, "keydown", e => e.key === "Escape" && close());
  }

  /* ---- Formularios (demo, sin backend) ---- */
  function forms() {
    $$("form[data-demo]").forEach(form => on(form, "submit", e => {
      e.preventDefault();
      const ok = $(".form__ok", form);
      if (ok) { ok.classList.add("show"); }
      form.querySelectorAll("input,textarea,select").forEach(i => { if (i.type !== "submit") i.value = ""; });
      if (ok) setTimeout(() => ok.classList.remove("show"), 6000);
    }));
  }

  /* ---- i18n ES/EN (claves mínimas; ampliable) ---- */
  const DICT = {
    es: {
      "nav.home":"Inicio","nav.about":"Quiénes Somos","nav.affiliates":"Afiliados","nav.trace":"Trazabilidad",
      "nav.services":"Servicios","nav.press":"Prensa","nav.library":"Biblioteca","nav.contact":"Contacto",
      "cta.platform":"Portal","cta.platform2":"Portal Institucional","cta.escuela":"Escuela de Café","cta.register":"Regístrese",
      "hero.badge":"Café orgánico y de especialidad de Bolivia",
      "hero.title":"Federación de Caficultores <em>Exportadores</em> de Bolivia",
      "hero.lead":"21 organizaciones y ~1.389 familias productoras afiliadas, que representan al sector cafetalero boliviano, con trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).",
      "hero.cta1":"Importar nuestro café","hero.cta2":"Conocer la Federación"
    },
    en: {
      "nav.home":"Home","nav.about":"About Us","nav.affiliates":"Members","nav.trace":"Traceability",
      "nav.services":"Services","nav.press":"Press","nav.library":"Library","nav.contact":"Contact",
      "cta.platform":"Portal","cta.platform2":"Institutional Portal","cta.escuela":"Coffee School","cta.register":"Register",
      "hero.badge":"Organic & specialty coffee from Bolivia",
      "hero.title":"Federation of Coffee <em>Exporting</em> Growers of Bolivia",
      "hero.lead":"21 organizations and ~1,389 affiliated producer families, representing the Bolivian coffee sector, with geospatial traceability compliant with EU Regulation 2023/1115 (EUDR).",
      "hero.cta1":"Source our coffee","hero.cta2":"About the Federation"
    }
  }
  function i18n() {
    const apply = lang => {
      $$("[data-i18n]").forEach(el => {
        const k = el.dataset.i18n, v = DICT[lang] && DICT[lang][k];
        if (v != null) el.innerHTML = v;
      });
      document.documentElement.lang = lang;
      $$(".lang button").forEach(b => b.classList.toggle("is-active", b.dataset.lang === lang));
    };
    $$(".lang button").forEach(b => on(b, "click", () => apply(b.dataset.lang)));
    apply("es");
  }

  /* ---- Botón flotante WhatsApp ---- */
  function whatsapp() {
    const wa = $(".fab--wa");
    if (wa) wa.href = "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(CONFIG.whatsappMsg);
  }

  /* ---- Mini chatbot simulado (reglas locales, con indicador de escritura) ---- */
  function chatbot() {
    const fab = $(".fab--chat"), panel = $(".chat"), body = $(".chat__body"),
          input = $("#chatInput"), send = $("#chatSend"), close = $(".chat .x"),
          badge = $(".fab--chat .badge");
    if (!fab || !panel) return;

    const KB = [
      { k:["export","comprar","import","proveedor","precio","buy","supplier","cotiz","muestra"],
        a:["Con gusto 🙌 Exportamos café verde oro orgánico y de especialidad a la UE, EE.UU. y Asia.",
           "¿Qué volumen y perfil de taza busca? Puedo derivarle al equipo comercial por WhatsApp o al correo " + CONFIG.email + "."] },
      { k:["eudr","trazab","trace","geo","2023","1115","dds","deforest","traces"],
        a:["Cumplimos el Reglamento UE 2023/1115 (EUDR) ✅","Geolocalizamos cada parcela (GeoJSON/WGS84), emitimos la DDS y la presentamos en TRACES NT. Puede ver el detalle en la página de Trazabilidad."] },
      { k:["afili","member","cooperativ","socio","unirme","asociac"],
        a:["Agrupamos 42 organizaciones: cooperativas, asociaciones y Coracas.","Si representa a una organización de productores, en la página de Afiliados está el proceso paso a paso."] },
      { k:["escuela","school","capacit","formaci","curso","cata","catacion","catación"],
        a:["La Escuela de Café forma a productores, jóvenes y mujeres ☕","Cubre producción orgánica, calidad, catación y gestión. ¿Le interesa capacitarse?"] },
      { k:["contacto","telefono","teléfono","correo","email","ubica","direccion","dónde","donde"],
        a:["Estamos en Av. Juan Pablo II 2974, El Alto, La Paz, Bolivia 📍","Tel/WhatsApp: +591 71537365 · Correo: " + CONFIG.email] },
      { k:["mision","misión","vision","visión","valor","quienes","quiénes","historia","directorio"],
        a:["Somos el ente rector del café boliviano desde 1991.","Encontrará misión, visión, valores, historia y directorio en la página Nosotros."] },
      { k:["hola","buenas","hello","hi","saludos"],
        a:["¡Hola! 👋 Soy el asistente virtual de FECAFEB.","¿Le interesa comprar café, afiliarse o conocer la trazabilidad EUDR?"] }
    ];
    const FALLBACK = ["Gracias por su mensaje 🙏","Un asesor de FECAFEB puede ayudarle en detalle. Para respuesta inmediata escríbanos por WhatsApp o a " + CONFIG.email + "."];
    const match = txt => {
      const t = txt.toLowerCase();
      const hit = KB.find(e => e.k.some(k => t.includes(k)));
      return hit ? hit.a : FALLBACK;
    };
    const now = () => new Date().toLocaleTimeString("es-BO", { hour: "2-digit", minute: "2-digit" });
    const add = (text, who) => {
      const m = document.createElement("div");
      m.className = "msg " + who;
      m.innerHTML = text + '<span class="time">' + now() + "</span>";
      body.appendChild(m); body.scrollTop = body.scrollHeight;
    };
    const typing = () => {
      const t = document.createElement("div");
      t.className = "typing"; t.innerHTML = "<span></span><span></span><span></span>";
      body.appendChild(t); body.scrollTop = body.scrollHeight;
      return t;
    };
    const botRespond = lines => {
      let i = 0;
      const step = () => {
        if (i >= lines.length) return;
        const t = typing();
        const delay = 650 + Math.min(1400, lines[i].length * 22);
        setTimeout(() => {
          t.remove(); add(lines[i], "bot"); i++;
          if (i < lines.length) setTimeout(step, 350);
        }, delay);
      };
      step();
    };
    let opened = false;
    const toggle = open => {
      panel.classList.toggle("is-open", open);
      fab.setAttribute("aria-expanded", String(open));
      if (open) {
        if (badge) badge.style.display = "none";
        if (!opened) { opened = true; botRespond(["¡Hola! 👋 Soy el asistente virtual de FECAFEB.", "¿En qué puedo ayudarle hoy?"]); }
        setTimeout(() => input && input.focus(), 300);
      }
    };
    on(fab, "click", () => toggle(!panel.classList.contains("is-open")));
    on(close, "click", () => toggle(false));
    const submit = () => {
      const v = (input.value || "").trim();
      if (!v) return;
      add(v, "user"); input.value = "";
      botRespond(match(v));
    };
    on(send, "click", submit);
    on(input, "keydown", e => e.key === "Enter" && submit());
    $$(".chip").forEach(c => on(c, "click", () => { add(c.textContent, "user"); botRespond(match(c.dataset.q || c.textContent)); }));
  }
})();

/* Mini-slider del Home (sección Nosotros) */
(function(){
  var s=document.querySelector('[data-mslider]'); if(!s) return;
  var imgs=[].slice.call(s.querySelectorAll('img')); if(imgs.length<2) return;
  var dots=s.querySelector('.mslider__dots');
  imgs.forEach(function(_,n){var b=document.createElement('b'); if(n===0)b.className='is-active'; b.addEventListener('click',function(){go(n);}); if(dots)dots.appendChild(b);});
  var db=dots?[].slice.call(dots.children):[], i=0;
  function go(n){imgs[i].classList.remove('is-active'); if(db[i])db[i].classList.remove('is-active'); i=(n+imgs.length)%imgs.length; imgs[i].classList.add('is-active'); if(db[i])db[i].classList.add('is-active');}
  setInterval(function(){go(i+1);},4200);
})();
