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
    mobileNav();
    headerScroll();
    scrollReveal();
    tabs();
    gallery();
    forms();
    i18n();
    chatbot();
    whatsapp();
    const y = $("#year"); if (y) y.textContent = new Date().getFullYear();
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

  /* ---- Sombra del header + activación de sección ---- */
  function headerScroll() {
    const header = $(".header");
    const links = $$('.menu > li > a[href^="#"]');
    const onScroll = () => {
      header && header.classList.toggle("is-scrolled", window.scrollY > 8);
      let current = "";
      $$("section[id]").forEach(sec => {
        if (window.scrollY >= sec.offsetTop - 140) current = sec.id;
      });
      links.forEach(l => l.parentElement.classList
        .toggle("is-active", l.getAttribute("href") === "#" + current));
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
      btns.forEach(btn => on(btn, "click", () => {
        btns.forEach(b => b.classList.remove("is-active"));
        panels.forEach(p => p.classList.remove("is-active"));
        btn.classList.add("is-active");
        const panel = $("#" + btn.dataset.target, group);
        panel && panel.classList.add("is-active");
      }));
    });
  }

  /* ---- Galería: lightbox simple ---- */
  function gallery() {
    const figs = $$(".gallery figure");
    if (!figs.length) return;
    let box;
    const open = (label, bg) => {
      box = document.createElement("div");
      box.style.cssText = "position:fixed;inset:0;z-index:200;display:grid;place-items:center;" +
        "background:rgba(20,12,8,.86);backdrop-filter:blur(4px);padding:24px;cursor:zoom-out";
      box.innerHTML = '<figure style="max-width:760px;width:100%;aspect-ratio:16/10;border-radius:18px;' +
        'box-shadow:0 30px 80px rgba(0,0,0,.5);background:' + bg + ';position:relative;display:grid;place-items:end start">' +
        '<figcaption style="color:#fff;font-weight:700;padding:18px 22px;font-size:1.05rem">' + label + '</figcaption></figure>';
      document.body.appendChild(box);
      document.body.style.overflow = "hidden";
      on(box, "click", close);
    };
    const close = () => { box && box.remove(); document.body.style.overflow = ""; };
    figs.forEach(f => on(f, "click", () => {
      const cap = $("figcaption", f);
      open(cap ? cap.textContent : "FECAFEB", getComputedStyle(f).background);
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
      "nav.home": "Inicio", "nav.about": "Nosotros", "nav.affiliates": "Afiliados",
      "nav.services": "Servicios", "nav.trace": "Trazabilidad", "nav.press": "Prensa",
      "nav.gallery": "Galería", "nav.contact": "Contacto", "cta.platform": "Plataforma",
      "cta.export": "Regístrese como exportador",
      "hero.badge": "Café orgánico y de especialidad de Bolivia",
      "hero.title": "El café boliviano que <em>Europa</em> busca, con trazabilidad garantizada",
      "hero.lead": "Federación de Caficultores Exportadores de Bolivia: 17.500 familias productoras, 42 organizaciones y trazabilidad geoespacial conforme al Reglamento UE 2023/1115 (EUDR).",
      "hero.cta1": "Importar nuestro café", "hero.cta2": "Conocer la Federación"
    },
    en: {
      "nav.home": "Home", "nav.about": "About", "nav.affiliates": "Members",
      "nav.services": "Services", "nav.trace": "Traceability", "nav.press": "Press",
      "nav.gallery": "Gallery", "nav.contact": "Contact", "cta.platform": "Platform",
      "cta.export": "Register as exporter",
      "hero.badge": "Organic & specialty coffee from Bolivia",
      "hero.title": "The Bolivian coffee <em>Europe</em> is looking for, with guaranteed traceability",
      "hero.lead": "Federation of Coffee Exporting Growers of Bolivia: 17,500 producing families, 42 organizations and geospatial traceability compliant with EU Regulation 2023/1115 (EUDR).",
      "hero.cta1": "Source our coffee", "hero.cta2": "About the Federation"
    }
  };
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

  /* ---- Mini chatbot (reglas locales, sin servicios externos) ---- */
  function chatbot() {
    const fab = $(".fab--chat"), panel = $(".chat"),
          body = $(".chat__body"), input = $("#chatInput"),
          send = $("#chatSend"), close = $(".chat .x");
    if (!fab || !panel) return;

    const KB = [
      { k: ["export", "comprar", "import", "proveedor", "precio", "buy", "supplier"],
        a: "Exportamos café verde oro orgánico y de especialidad a la UE, EE.UU. y Asia. Escríbenos a " + CONFIG.email + " o usa el botón de WhatsApp para cotizar." },
      { k: ["eudr", "trazab", "trace", "geo", "2023/1115", "dds"],
        a: "Cumplimos el Reglamento UE 2023/1115 (EUDR): geolocalización de parcelas (GeoJSON/WGS84), declaración de diligencia debida (DDS) e integración con TRACES NT. Visita la sección Trazabilidad." },
      { k: ["afili", "member", "cooperativ", "socio", "unirme"],
        a: "Agrupamos 42 organizaciones (cooperativas, asociaciones y Coracas). Mira la sección Afiliados o regístrate como exportador." },
      { k: ["escuela", "school", "capacit", "formaci", "curso"],
        a: "La Escuela de Café ofrece formación en producción, calidad, catación y administración para la familia cafetalera." },
      { k: ["contacto", "telefono", "correo", "email", "ubica", "direccion", "contact"],
        a: "Estamos en Av. Juan Pablo II 2974, El Alto, La Paz, Bolivia. Correo: " + CONFIG.email + "." },
      { k: ["mision", "vision", "valor", "quienes", "about", "history", "historia"],
        a: "Somos el ente rector del café boliviano desde 1991. Conoce nuestra misión, visión, valores e historia en la sección Nosotros." }
    ];
    const reply = txt => {
      const t = txt.toLowerCase();
      const hit = KB.find(e => e.k.some(k => t.includes(k)));
      return hit ? hit.a : "Gracias por tu mensaje. Un asesor de FECAFEB te atenderá. Para respuesta inmediata usa el botón de WhatsApp o escribe a " + CONFIG.email + ".";
    };
    const add = (text, who) => {
      const m = document.createElement("div");
      m.className = "msg " + who; m.textContent = text;
      body.appendChild(m); body.scrollTop = body.scrollHeight;
    };
    const botSay = text => setTimeout(() => add(text, "bot"), 380);
    const toggle = open => {
      panel.classList.toggle("is-open", open);
      fab.setAttribute("aria-expanded", String(open));
      if (open && !body.dataset.init) {
        add("¡Hola! 👋 Soy el asistente de FECAFEB. ¿En qué puedo ayudarte?", "bot");
        body.dataset.init = "1";
      }
      if (open) setTimeout(() => input && input.focus(), 300);
    };
    on(fab, "click", () => toggle(!panel.classList.contains("is-open")));
    on(close, "click", () => toggle(false));
    const submit = () => {
      const v = (input.value || "").trim();
      if (!v) return;
      add(v, "user"); input.value = "";
      botSay(reply(v));
    };
    on(send, "click", submit);
    on(input, "keydown", e => e.key === "Enter" && submit());
    $$(".chip").forEach(c => on(c, "click", () => { add(c.textContent, "user"); botSay(reply(c.dataset.q || c.textContent)); }));
  }
})();
