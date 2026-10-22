/**
 * =============================================================================
 * NEXORD PLATFORM · PERSISTENT GLOBAL NAVIGATION & ZENITH DIAL (SCHEMA ENGINE)
 * Motor universal de barra persistente superior, breadcrumbs y Dial 3-6-9
 * Soporte bilingüe completo y dinámico (Español Canónico / English)
 * =============================================================================
 */

(function () {
  'use strict';

  // Evitar doble inicialización
  if (window.__NEXORD_NAV_INITIALIZED__) return;
  window.__NEXORD_NAV_INITIALIZED__ = true;

  // Detectar profundidad de subdirectorio para prefijo relativo (../)
  const pathname = window.location.pathname.replace(/\\/g, '/');
  const filename = pathname.split('/').pop() || 'index.html';
  const isInSubdir = pathname.includes('/PORTAL_INSTITUCIONAL/') || pathname.includes('/VISORD_demo/') || pathname.includes('/assets/');
  const rootPrefix = isInSubdir ? '../' : '';

  // Detección de idioma
  function getCurrentNavLang() {
    try {
      const p = new URLSearchParams(window.location.search);
      const urlLang = p.get('lang');
      if (urlLang === 'en' || urlLang === 'es') return urlLang;
      const saved = localStorage.getItem('nexord_lang');
      if (saved === 'en' || saved === 'es') return saved;
      if (document.documentElement.lang === 'en') return 'en';
      const browserLang = (navigator.language || '').toLowerCase().split('-')[0];
      if (browserLang === 'en') return 'en';
    } catch (e) {}
    return 'es';
  }

  let currentNavLang = getCurrentNavLang();

  // DICCIONARIO BILINGÜE UNIVERSAL DE NAVEGACIÓN Y DIAL
  const NAV_I18N = {
    es: {
      dial_btn: 'DIAL ORBITAL',
      dial_btn_title: 'Abrir Dial Orbital (Tecla D)',
      modal_title: 'DIAL ORBITAL · NAVEGACIÓN UNIVERSAL',
      modal_aria: 'Dial Orbital 3-6-9',
      btn_fullscreen_title: 'Abrir Dial Orbital en Pantalla Completa',
      btn_fullscreen_text: '⛶ Pantalla Completa ↗',
      btn_close_title: 'Cerrar modal (Esc)',
      btn_close_text: '✕ Cerrar',
      sidebar_header: '📑 MENÚ DE NIVELES 1–9',
      sidebar_tag: 'CANON NEXORD',
      insp_tag: 'CANON NEXORD',
      btn_enter_prefix: 'Entrar al Nivel',
      btn_fs_text: 'Ver en Dial 3D ↗',
      footer_hint: '⌨ Teclas 1-9 seleccionan nivel · Enter o Clic accede · Tecla D o Esc cierran',
      nav_deonto_title: 'Código Deontológico PI (Regla 21) & Privacidad RGPD',
      nav_deonto_text: 'Deontología & RGPD',
      nav_custodia_title: 'Custodia Institucional para Universidades',
      nav_custodia_text: 'Custodia',
      nav_dial_title: 'Dial Orbital Epistemológico',
      nav_home_title: 'Inicio / Portada de Bienvenida',
      pills: {
        nivel1: { text: '1·Int', title: 'Nivel 1: Intuitivo (Moviola 3D)' },
        nivel2: { text: '2·Bás', title: 'Nivel 2: Básico (Matrices SMIa/SMIb)' },
        nivel3: { text: '3·Esq', title: 'Nivel 3: Esquema (Canon Q81)' },
        nivel4: { text: '4·Apl', title: 'Nivel 4: Aplicaciones (Educación/Empresa/Salud)' },
        nivel5: { text: '5·Mat', title: 'Nivel 5: Matemático (Grassmann & Fiedler)' },
        nivel6: { text: '6·Inf', title: 'Nivel 6: Informes Forenses' },
        nivel7: { text: '7·Doc', title: 'Nivel 7: Documentación & Zenodo' },
        recursos: { text: '8·Rec', title: 'Nivel 8: Recursos (Experiencia VISORD)' },
        fundamentos: { text: '9·Fun', title: 'Nivel 9: Fundamentos (Epistemología)' }
      },
      breadcrumbs: {
        nivel1: '1. Intuitivo (Moviola 3D)',
        nivel2: '2. Básico (Matrices SMIa/SMIb)',
        nivel3: '3. Esquema (Canon Q81)',
        nivel4: '4. Aplicaciones (Casos)',
        nivel5: '5. Matemático (Grassmann)',
        nivel6: '6. Informes (Peritaje)',
        nivel7: '7. Documentación (Zenodo)',
        recursos: '8. Recursos (Experiencia VISORD)',
        fundamentos: '9. Fundamentos (Cenit Epistemológico)',
        visord: '8. VISORD 3D Suite',
        deontologia: 'Deontología PI & RGPD',
        glosario: 'Glosario Canónico',
        portal: 'Portal Institucional',
        dial: 'Dial Orbital'
      },
      sectors: {
        "9": {
          short: "FUN",
          title: "Nivel 9: Fundamentos",
          badge: "NIVEL 9 • CENIT EPISTEMOLÓGICO (CANON 3-6-9)",
          subtitle: "Física de Grupos & Urdimbre Vital",
          desc: "Hacia una física de lo grupal: urdimbre vital, vectores DAR+RECIBIR, equilibrio homeostático, Sociometría Sintética in silico y rigor científico."
        },
        "1": {
          short: "INT",
          title: "Nivel 1: Intuitivo",
          badge: "NIVEL 1 • ENTRADA VISUAL",
          subtitle: "Moviola 3D & Densidad Bruta",
          desc: "Simulación de partículas dinámicas, fluidos relacionales y balance de atracción/rechazo sin estrés evaluativo."
        },
        "2": {
          short: "BÁS",
          title: "Nivel 2: Básico",
          badge: "NIVEL 2 • ÁTOMO RELACIONAL",
          subtitle: "Matrices SMIa / SMIb",
          desc: "Transición fundamental de la sociometría tradicional a matrices de preferencia ordinal con metapercepción cruzada."
        },
        "3": {
          short: "ESQ",
          title: "Nivel 3: Esquema",
          badge: "NIVEL 3 • ESTRUCTURA FORMAL (CANON 3-6-9)",
          subtitle: "81 Figuras Sociométricas",
          desc: "El invariante universal Q81: ordenación formal, topología de roles diádicos y partición canónica en 5 zonas."
        },
        "4": {
          short: "APL",
          title: "Nivel 4: Aplicaciones",
          badge: "NIVEL 4 • VIDA GRUPAL & CASOS",
          subtitle: "Casos Sectoriales & Forenses",
          desc: "Soluciones de campo: convivencia escolar, equipos de alto rendimiento corporativo y mediación clínica."
        },
        "5": {
          short: "MAT",
          title: "Nivel 5: Matemático",
          badge: "NIVEL 5 • ÁLGEBRA TENSORIAL",
          subtitle: "Grassmann Gr(k, N) & Fiedler",
          desc: "Geometría diferencial, autovalores del Laplaciano grafal, frustración estructural de Heider y entropía grupal."
        },
        "6": {
          short: "INF",
          title: "Nivel 6: Informes",
          badge: "NIVEL 6 • DIAGNÓSTICO PERICIAL (CANON 3-6-9)",
          subtitle: "Diagnóstico Pericial Forense",
          desc: "Generación automatizada de informes periciales objetivos, mapas de calor relacional y planes no punitivos."
        },
        "7": {
          short: "DOC",
          title: "Nivel 7: Documentación",
          badge: "NIVEL 7 • DEONTOLOGÍA & ZENODO",
          subtitle: "Manifiesto Zenodo & DOI",
          desc: "Depósito científico abierto en CERN Zenodo, manuales de codificación, citación formal BibTeX/APA y licencias."
        },
        "8": {
          short: "REC",
          title: "Nivel 8: Recursos",
          badge: "NIVEL 8 • EXPERIENCIA VISORD",
          subtitle: "Experiencia VISORD (4 Entornos)",
          desc: "Entornos interactivos: VISORD_demo (Nivel 8), VISORD_cultural, VISORD_radiológico y VISORD_dialéctico."
        }
      }
    },
    en: {
      dial_btn: 'ORBITAL DIAL',
      dial_btn_title: 'Open Orbital Dial (Key D)',
      modal_title: 'ORBITAL DIAL · UNIVERSAL NAVIGATION',
      modal_aria: 'Orbital Dial 3-6-9',
      btn_fullscreen_title: 'Open Orbital Dial in Fullscreen',
      btn_fullscreen_text: '⛶ Fullscreen ↗',
      btn_close_title: 'Close modal (Esc)',
      btn_close_text: '✕ Close',
      sidebar_header: '📑 LEVELS 1–9 MENU',
      sidebar_tag: 'NEXORD CANON',
      insp_tag: 'NEXORD CANON',
      btn_enter_prefix: 'Enter Level',
      btn_fs_text: 'View in 3D Dial ↗',
      footer_hint: '⌨ Keys 1-9 select level · Enter or Click navigates · Key D or Esc closes',
      nav_deonto_title: 'PI Deontological Code (Rule 21) & GDPR Privacy',
      nav_deonto_text: 'Deontology & GDPR',
      nav_custodia_title: 'Institutional Stewardship for Universities',
      nav_custodia_text: 'Stewardship',
      nav_dial_title: 'Epistemological Orbital Dial',
      nav_home_title: 'Home / Welcome Page',
      pills: {
        nivel1: { text: '1·Int', title: 'Level 1: Intuitive (3D Moviola)' },
        nivel2: { text: '2·Bas', title: 'Level 2: Basic (SMIa/SMIb Matrices)' },
        nivel3: { text: '3·Sch', title: 'Level 3: Schema (Canon Q81)' },
        nivel4: { text: '4·App', title: 'Level 4: Applications (Education/Corporate/Clinical)' },
        nivel5: { text: '5·Mat', title: 'Level 5: Mathematical (Grassmann & Fiedler)' },
        nivel6: { text: '6·Rep', title: 'Level 6: Reports (Forensic Expert Diagnosis)' },
        nivel7: { text: '7·Doc', title: 'Level 7: Documentation & Zenodo' },
        recursos: { text: '8·Res', title: 'Level 8: Resources (VISORD Suite)' },
        fundamentos: { text: '9·Fnd', title: 'Level 9: Foundations (Epistemology)' }
      },
      breadcrumbs: {
        nivel1: '1. Intuitive (3D Moviola)',
        nivel2: '2. Basic (SMIa/SMIb Matrices)',
        nivel3: '3. Schema (Canon Q81)',
        nivel4: '4. Applications (Cases)',
        nivel5: '5. Mathematical (Grassmann)',
        nivel6: '6. Reports (Forensics)',
        nivel7: '7. Documentation (Zenodo)',
        recursos: '8. Resources (VISORD Suite)',
        fundamentos: '9. Foundations (Epistemology)',
        visord: '8. VISORD 3D Suite',
        deontologia: 'Deontology & GDPR',
        glosario: 'Canonical Glossary',
        portal: 'Institutional Portal',
        dial: 'Orbital Dial'
      },
      sectors: {
        "9": {
          short: "FND",
          title: "Level 9: Foundations",
          badge: "LEVEL 9 • EPISTEMOLOGICAL ZENITH (3-6-9 CANON)",
          subtitle: "Group Physics & Vital Warp",
          desc: "Toward a physics of groups: vital warp, GIVE+RECEIVE vectors, homeostatic balance, Synthetic Sociometry in silico, and scientific rigor."
        },
        "1": {
          short: "INT",
          title: "Level 1: Intuitive",
          badge: "LEVEL 1 • VISUAL ENTRY",
          subtitle: "3D Moviola & Raw Density",
          desc: "Dynamic particle simulation, relational fluids, and attraction/rejection equilibrium without evaluation stress."
        },
        "2": {
          short: "BAS",
          title: "Level 2: Basic",
          badge: "LEVEL 2 • RELATIONAL ATOM",
          subtitle: "SMIa / SMIb Matrices",
          desc: "Fundamental transition from classical sociometry to ordinal preference matrices with crossed metaperception."
        },
        "3": {
          short: "SCH",
          title: "Level 3: Schema",
          badge: "LEVEL 3 • FORMAL STRUCTURE (3-6-9 CANON)",
          subtitle: "81 Sociometric Figures",
          desc: "Universal Q81 invariant: formal ordering, dyadic role topology, and canonical 5-zone partition."
        },
        "4": {
          short: "APP",
          title: "Level 4: Applications",
          badge: "LEVEL 4 • GROUP LIFE & CASES",
          subtitle: "Sectoral & Forensic Cases",
          desc: "Field solutions: school climate, corporate high-performance teams, and clinical mediation."
        },
        "5": {
          short: "MAT",
          title: "Level 5: Mathematical",
          badge: "LEVEL 5 • TENSOR ALGEBRA",
          subtitle: "Grassmann Gr(k, N) & Fiedler",
          desc: "Differential geometry, graph Laplacian eigenvalues, Heiderian structural frustration, and group entropy."
        },
        "6": {
          short: "REP",
          title: "Level 6: Reports",
          badge: "LEVEL 6 • FORENSIC EXPERT DIAGNOSIS (3-6-9 CANON)",
          subtitle: "Forensic Expert Diagnosis",
          desc: "Automated generation of objective expert reports, relational heatmaps, and non-punitive intervention plans."
        },
        "7": {
          short: "DOC",
          title: "Level 7: Documentation",
          badge: "LEVEL 7 • DEONTOLOGY & ZENODO",
          subtitle: "Zenodo Manifesto & DOI",
          desc: "Open scientific repository at CERN Zenodo, encoding manuals, formal BibTeX/APA citation, and licenses."
        },
        "8": {
          short: "RES",
          title: "Level 8: Resources",
          badge: "LEVEL 8 • VISORD EXPERIENCE",
          subtitle: "VISORD Suite (4 Environments)",
          desc: "Interactive environments: VISORD_demo (Level 8), VISORD_cultural, VISORD_radiologico, and VISORD_dialectico."
        }
      }
    }
  };

  // Definición canónica de los 9 sectores del Dial (3-6-9)
  const DIAL_SECTORS = [
    { idx: 0, num: "9", url: rootPrefix + "fundamentos.html", key: "fundamentos", color: "#00FF87", is369: true },
    { idx: 1, num: "1", url: rootPrefix + "nivel1_intuitivo.html", key: "nivel1", color: "#38BDF8", is369: false },
    { idx: 2, num: "2", url: rootPrefix + "nivel2_basico.html", key: "nivel2", color: "#48CAE4", is369: false },
    { idx: 3, num: "3", url: rootPrefix + "nivel3_esquema.html", key: "nivel3", color: "#FFE600", is369: true },
    { idx: 4, num: "4", url: rootPrefix + "nivel4_aplicaciones.html", key: "nivel4", color: "#FF9F1C", is369: false },
    { idx: 5, num: "5", url: rootPrefix + "nivel5_matematico.html", key: "nivel5", color: "#BF5AF2", is369: false },
    { idx: 6, num: "6", url: rootPrefix + "nivel6_informes.html", key: "nivel6", color: "#FF007F", is369: true },
    { idx: 7, num: "7", url: rootPrefix + "nivel7_documentacion.html", key: "nivel7", color: "#E0AAFF", is369: false },
    { idx: 8, num: "8", url: rootPrefix + "recursos.html", key: "recursos", color: "#00F0FF", is369: false }
  ];

  // Helper para obtener sector localizado
  function getLocalizedSector(sec, lang) {
    const d = NAV_I18N[lang] || NAV_I18N.es;
    const sInfo = d.sectors[sec.num] || NAV_I18N.es.sectors[sec.num];
    return {
      ...sec,
      short: sInfo.short,
      title: sInfo.title,
      badge: sInfo.badge,
      subtitle: sInfo.subtitle,
      desc: sInfo.desc
    };
  }

  // Identificar el nivel activo según la página actual
  let activeKey = '';
  if (filename.includes('nivel1')) activeKey = 'nivel1';
  else if (filename.includes('nivel2')) activeKey = 'nivel2';
  else if (filename.includes('nivel3')) activeKey = 'nivel3';
  else if (filename.includes('nivel4')) activeKey = 'nivel4';
  else if (filename.includes('nivel5')) activeKey = 'nivel5';
  else if (filename.includes('nivel6')) activeKey = 'nivel6';
  else if (filename.includes('nivel7')) activeKey = 'nivel7';
  else if (filename.includes('recursos')) activeKey = 'recursos';
  else if (filename.includes('fundamentos')) activeKey = 'fundamentos';
  else if (filename.includes('visord') || filename.includes('radiografias') || filename.includes('acuario') || filename.includes('pentagrama') || filename.includes('suite_g2')) {
    activeKey = 'visord';
  }
  else if (filename.includes('deontologia_legal')) activeKey = 'deontologia';
  else if (filename.includes('glosario')) activeKey = 'glosario';
  else if (filename.includes('index_promocional') || filename === 'index.html' || filename === '') activeKey = 'portal';
  else if (filename.includes('dial_orbital')) activeKey = 'dial';

  function getBreadcrumbName(lang) {
    const d = NAV_I18N[lang] || NAV_I18N.es;
    return d.breadcrumbs[activeKey] || 'NEXORD';
  }

  let currentSelectedIndex = 1;
  const matchedSector = DIAL_SECTORS.find(s => s.key === activeKey);
  if (matchedSector) {
    currentSelectedIndex = matchedSector.idx;
  }

  // Actualizar Inspector dinámico
  function updateInspector(idx) {
    const baseSec = DIAL_SECTORS[idx];
    if (!baseSec) return;
    currentSelectedIndex = idx;
    const sec = getLocalizedSector(baseSec, currentNavLang);
    const d = NAV_I18N[currentNavLang] || NAV_I18N.es;

    const b = document.getElementById('zinsp-badge');
    const t = document.getElementById('zinsp-title');
    const s = document.getElementById('zinsp-sub');
    const descEl = document.getElementById('zinsp-desc');
    const btnEnter = document.getElementById('zinsp-btn-enter');
    const btnFs = document.getElementById('zinsp-btn-fs');

    if (b) b.textContent = sec.badge;
    if (t) t.textContent = sec.title;
    if (s) s.textContent = sec.subtitle;
    if (descEl) descEl.textContent = sec.desc;
    if (btnEnter) {
      btnEnter.href = sec.url;
      btnEnter.innerHTML = `<span>${d.btn_enter_prefix} ${sec.num}</span> <span>➔</span>`;
    }
    if (btnFs) {
      btnFs.href = `${rootPrefix}dial_orbital.html?sector=${sec.num}`;
      btnFs.innerHTML = `<span>${d.btn_fs_text}</span>`;
    }

    const menuItems = document.querySelectorAll('#nexord-zenith-modal .zenith-menu-item');
    menuItems.forEach((item) => {
      if (parseInt(item.dataset.idx) === idx) {
        item.classList.add('selected');
        item.setAttribute('aria-selected', 'true');
      } else {
        item.classList.remove('selected');
        item.setAttribute('aria-selected', 'false');
      }
    });
  }

  // Aplicar traducciones reactivas a la barra y al modal
  function applyNavTranslations(lang) {
    if (!NAV_I18N[lang]) lang = 'es';
    currentNavLang = lang;
    const d = NAV_I18N[lang];

    // 1. Barra superior
    const dialBtn = document.getElementById('btn-open-zenith-dial');
    if (dialBtn) {
      dialBtn.title = d.dial_btn_title;
      const spanText = dialBtn.querySelector('span:last-child');
      if (spanText) spanText.textContent = d.dial_btn;
    }

    const breadcrumbCur = document.querySelector('#nexord-persistent-nav .pnav-breadcrumb .cur');
    if (breadcrumbCur) {
      breadcrumbCur.textContent = getBreadcrumbName(lang);
    }

    // Pills centrales
    Object.keys(d.pills).forEach(k => {
      const pill = document.querySelector(`#nexord-persistent-nav a[data-pill="${k}"]`);
      if (pill) {
        pill.textContent = d.pills[k].text;
        pill.title = d.pills[k].title;
      }
    });

    // Enlaces derechos
    const linkDeonto = document.querySelector('#nexord-persistent-nav a[data-nav-right="deonto"]');
    if (linkDeonto) {
      linkDeonto.title = d.nav_deonto_title;
      const t = linkDeonto.querySelector('.link-text');
      if (t) t.textContent = d.nav_deonto_text;
    }
    const linkCustodia = document.querySelector('#nexord-persistent-nav a[data-nav-right="custodia"]');
    if (linkCustodia) {
      linkCustodia.title = d.nav_custodia_title;
      const t = linkCustodia.querySelector('.link-text');
      if (t) t.textContent = d.nav_custodia_text;
    }
    const linkDial = document.querySelector('#nexord-persistent-nav a[data-nav-right="dial"]');
    if (linkDial) linkDial.title = d.nav_dial_title;
    const linkHome = document.querySelector('#nexord-persistent-nav a[data-nav-right="home"]');
    if (linkHome) linkHome.title = d.nav_home_title;

    // 2. Modal Dial
    const modal = document.getElementById('nexord-zenith-modal');
    if (modal) {
      modal.setAttribute('aria-label', d.modal_aria);
      const mTitle = modal.querySelector('.zenith-title span:last-child');
      if (mTitle) mTitle.textContent = d.modal_title;

      const fsBtn = modal.querySelector('.zenith-header .zenith-btn-fullscreen');
      if (fsBtn) {
        fsBtn.title = d.btn_fullscreen_title;
        fsBtn.textContent = d.btn_fullscreen_text;
      }
      const closeBtn = document.getElementById('btn-close-zenith-dial');
      if (closeBtn) {
        closeBtn.title = d.btn_close_title;
        closeBtn.textContent = d.btn_close_text;
      }

      const sbHeader = modal.querySelector('.zenith-sidebar-header span:first-child');
      if (sbHeader) sbHeader.textContent = d.sidebar_header;
      const sbTag = modal.querySelector('.zenith-sidebar-tag');
      if (sbTag) sbTag.textContent = d.sidebar_tag;

      const inspKey = modal.querySelector('.zenith-insp-key');
      if (inspKey) inspKey.textContent = d.insp_tag;

      const fHint = modal.querySelector('.zenith-footer-hint');
      if (fHint) fHint.textContent = d.footer_hint;

      // Actualizar botones del menú lateral 1-9
      const menuItems = modal.querySelectorAll('.zenith-menu-item');
      menuItems.forEach((btn) => {
        const num = btn.dataset.num;
        const sInfo = d.sectors[num];
        if (sInfo) {
          btn.title = `${sInfo.title} · ${sInfo.subtitle}`;
          const tEl = btn.querySelector('.zenith-menu-title');
          const sEl = btn.querySelector('.zenith-menu-sub');
          if (tEl) tEl.textContent = sInfo.title;
          if (sEl) sEl.textContent = sInfo.subtitle;
        }
      });

      // Actualizar inspector
      updateInspector(currentSelectedIndex);
    }
  }

  // Función constructora del HTML de navegación
  function injectPersistentNav() {
    const hasCanonicalHud = !!document.getElementById('top-floating-hud') || 
                            !!document.querySelector('.top-floating-hud') || 
                            !!document.querySelector('.top-header') || 
                            !!document.querySelector('header.top-header') ||
                            !!document.querySelector('.master-hud') || 
                            !!document.querySelector('.recursos-top-bar');
    const isDialOrbital = filename.includes('dial_orbital');
    const isPromoHome = filename.includes('index_promocional') || filename === 'index.html' || filename === '';

    if (isDialOrbital || isPromoHome) {
      // dial_orbital.html es la propia página de la rueda 3-6-9 interactiva a pantalla completa;
      // no debe tener inyección de persistent-nav ni modal secundario sobrepuesto.
      return;
    }

    const d = NAV_I18N[currentNavLang] || NAV_I18N.es;

    // 1. BARRA SUPERIOR PERSISTENTE (Solo si la página no dispone de HUD canónico ni es la portada/portal)
    if (!hasCanonicalHud && !document.getElementById('nexord-persistent-nav')) {
      document.body.classList.add('has-persistent-nav');
      const nav = document.createElement('nav');
      nav.id = 'nexord-persistent-nav';
      nav.setAttribute('aria-label', 'Navegación Persistente de Niveles NEXORD');

      nav.innerHTML = `
        <div class="pnav-left">
          <button type="button" class="pnav-dial-btn" id="btn-open-zenith-dial" title="${d.dial_btn_title}">
            <span>🧭</span> <span>${d.dial_btn}</span>
          </button>
          <div class="pnav-breadcrumb">
            <a href="${rootPrefix}index.html">NEXORD</a>
            <span class="sep">›</span>
            <span class="cur">${getBreadcrumbName(currentNavLang)}</span>
          </div>
        </div>

        <div class="pnav-center">
          <a href="${rootPrefix}nivel1_intuitivo.html" data-pill="nivel1" class="pnav-lvl-pill ${activeKey === 'nivel1' ? 'active' : ''}" title="${d.pills.nivel1.title}">${d.pills.nivel1.text}</a>
          <a href="${rootPrefix}nivel2_basico.html" data-pill="nivel2" class="pnav-lvl-pill ${activeKey === 'nivel2' ? 'active' : ''}" title="${d.pills.nivel2.title}">${d.pills.nivel2.text}</a>
          <a href="${rootPrefix}nivel3_esquema.html" data-pill="nivel3" class="pnav-lvl-pill ${activeKey === 'nivel3' ? 'active' : ''}" title="${d.pills.nivel3.title}">${d.pills.nivel3.text}</a>
          <a href="${rootPrefix}nivel4_aplicaciones.html" data-pill="nivel4" class="pnav-lvl-pill ${activeKey === 'nivel4' ? 'active' : ''}" title="${d.pills.nivel4.title}">${d.pills.nivel4.text}</a>
          <a href="${rootPrefix}nivel5_matematico.html" data-pill="nivel5" class="pnav-lvl-pill ${activeKey === 'nivel5' ? 'active' : ''}" title="${d.pills.nivel5.title}">${d.pills.nivel5.text}</a>
          <a href="${rootPrefix}nivel6_informes.html" data-pill="nivel6" class="pnav-lvl-pill ${activeKey === 'nivel6' ? 'active' : ''}" title="${d.pills.nivel6.title}">${d.pills.nivel6.text}</a>
          <a href="${rootPrefix}nivel7_documentacion.html" data-pill="nivel7" class="pnav-lvl-pill ${activeKey === 'nivel7' ? 'active' : ''}" title="${d.pills.nivel7.title}">${d.pills.nivel7.text}</a>
          <a href="${rootPrefix}recursos.html" data-pill="recursos" class="pnav-lvl-pill ${activeKey === 'recursos' || activeKey === 'visord' ? 'active' : ''}" title="${d.pills.recursos.title}">${d.pills.recursos.text}</a>
          <a href="${rootPrefix}fundamentos.html" data-pill="fundamentos" class="pnav-lvl-pill ${activeKey === 'fundamentos' ? 'active' : ''}" title="${d.pills.fundamentos.title}">${d.pills.fundamentos.text}</a>
        </div>

        <div class="pnav-right">
          <a href="${rootPrefix}deontologia_legal.html" data-nav-right="deonto" class="pnav-link highlight" title="${d.nav_deonto_title}">
            <span>🛡️</span> <span class="link-text">${d.nav_deonto_text}</span>
          </a>
          <a href="${rootPrefix}index_promocional.html#custodia" data-nav-right="custodia" class="pnav-link" title="${d.nav_custodia_title}">
            <span>🏛️</span> <span class="link-text">${d.nav_custodia_text}</span>
          </a>
          <a href="${rootPrefix}dial_orbital.html" data-nav-right="dial" class="pnav-link" title="${d.nav_dial_title}">
            <span>🧭</span>
          </a>
          <a href="${rootPrefix}index.html" data-nav-right="home" class="pnav-link" title="${d.nav_home_title}">
            <span>🏠</span>
          </a>
        </div>
      `;

      document.body.insertAdjacentElement('afterbegin', nav);
    }

    if (document.getElementById('nexord-zenith-modal')) return;

    // 2. CONSTRUCCIÓN DEL MENÚ LATERAL SIMPLIFICADO 1-9 (ENLACES REALES)
    const sortedLevels = [...DIAL_SECTORS].sort((a, b) => parseInt(a.num) - parseInt(b.num));
    let sidebarMenuHtml = '';
    sortedLevels.forEach(baseSec => {
      const sec = getLocalizedSector(baseSec, currentNavLang);
      const isSecActive = sec.key === activeKey;
      sidebarMenuHtml += `
        <a href="${rootPrefix}${sec.url}"
           class="zenith-menu-item ${isSecActive ? 'is-active-page' : ''}"
           data-idx="${sec.idx}"
           data-num="${sec.num}"
           role="tab"
           aria-selected="${isSecActive ? 'true' : 'false'}"
           style="text-decoration: none;"
           title="${sec.title} · ${sec.subtitle}">
          <span class="zenith-menu-num" style="border-color:${sec.color}; color:${sec.color};">${sec.num}</span>
          <div class="zenith-menu-info">
            <div class="zenith-menu-title">${sec.title}</div>
            <div class="zenith-menu-sub">${sec.subtitle}</div>
          </div>
          <span class="zenith-menu-arrow">➔</span>
        </a>
      `;
    });

    // 3. MODAL DEL DIAL ORBITAL (MENÚ LATERAL 1-9 + INSPECTOR)
    const modal = document.createElement('div');
    modal.id = 'nexord-zenith-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', d.modal_aria);

    const initSec = getLocalizedSector(DIAL_SECTORS[currentSelectedIndex], currentNavLang);

    modal.innerHTML = `
      <div class="zenith-box">
        <div class="zenith-header">
          <div class="zenith-title">
            <span>🧭</span>
            <span>${d.modal_title}</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <a href="${rootPrefix}dial_orbital.html" class="zenith-btn-fullscreen" title="${d.btn_fullscreen_title}" style="padding: 4px 10px; font-size: 0.74rem;">
              ${d.btn_fullscreen_text}
            </a>
            <button type="button" class="zenith-close-btn" id="btn-close-zenith-dial" title="${d.btn_close_title}">
              ${d.btn_close_text}
            </button>
          </div>
        </div>

        <!-- VISTA CANÓNICA: MENÚ LATERAL SIMPLIFICADO 1-9 + INSPECTOR -->
        <div class="zenith-dial-container">
          <div class="zenith-sidebar-col" role="tablist" aria-label="Menú Lateral de Niveles 1-9">
            <div class="zenith-sidebar-header">
              <span>${d.sidebar_header}</span>
              <span class="zenith-sidebar-tag">${d.sidebar_tag}</span>
            </div>
            <div class="zenith-sidebar-menu">
              ${sidebarMenuHtml}
            </div>
          </div>

          <!-- Inspector Dinámico de Sector -->
          <div class="zenith-inspector-col">
            <div>
              <div class="zenith-insp-header">
                <span class="zenith-insp-badge" id="zinsp-badge">${initSec.badge}</span>
                <span class="zenith-insp-key">${d.insp_tag}</span>
              </div>
              <div class="zenith-insp-title" id="zinsp-title">${initSec.title}</div>
              <div class="zenith-insp-sub" id="zinsp-sub">${initSec.subtitle}</div>
              <div class="zenith-insp-desc" id="zinsp-desc">${initSec.desc}</div>
            </div>
            <div class="zenith-insp-actions">
              <a id="zinsp-btn-enter" href="${initSec.url}" class="zenith-btn-enter">
                <span>${d.btn_enter_prefix} ${initSec.num}</span> <span>➔</span>
              </a>
              <a id="zinsp-btn-fs" href="${rootPrefix}dial_orbital.html?sector=${initSec.num}" class="zenith-btn-fullscreen">
                <span>${d.btn_fs_text}</span>
              </a>
            </div>
          </div>
        </div>

        <div class="zenith-footer">
          <span class="zenith-footer-hint">${d.footer_hint}</span>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    // 4. CONTROLADOR DEL INSPECTOR Y EVENTOS DEL MENÚ LATERAL
    updateInspector(currentSelectedIndex);

    const menuItems = modal.querySelectorAll('.zenith-menu-item');
    menuItems.forEach((item) => {
      const idx = parseInt(item.dataset.idx);
      item.addEventListener('mouseenter', () => updateInspector(idx));
      item.addEventListener('click', () => {
        updateInspector(idx);
        const sec = DIAL_SECTORS[idx];
        if (sec && sec.url) {
          window.location.href = sec.url;
        }
      });
      item.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          const sec = DIAL_SECTORS[idx];
          if (sec && sec.url) window.location.href = sec.url;
        }
      });
    });

    // Apertura y Cierre del Modal
    const btnOpen = document.getElementById('btn-open-zenith-dial');
    const btnClose = document.getElementById('btn-close-zenith-dial');

    function openModal() {
      modal.classList.add('open');
      updateInspector(currentSelectedIndex);
    }
    function closeModal() {
      modal.classList.remove('open');
    }

    if (btnOpen) btnOpen.addEventListener('click', openModal);
    if (btnClose) btnClose.addEventListener('click', closeModal);

    // Clic fuera del cuadro para cerrar
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    // Atajos de teclado: Tecla 'D' abre el Dial, 'Escape' cierra, '1'..'9' seleccionan sector, 'Enter' accede
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('open')) {
        closeModal();
      } else if ((e.key === 'd' || e.key === 'D') && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        if (modal.classList.contains('open')) closeModal();
        else openModal();
      } else if (modal.classList.contains('open')) {
        if (e.key >= '1' && e.key <= '9') {
          const num = e.key;
          const targetSector = DIAL_SECTORS.find(s => s.num === num);
          if (targetSector) {
            updateInspector(targetSector.idx);
          }
        } else if (e.key === 'Enter') {
          const sec = DIAL_SECTORS[currentSelectedIndex];
          if (sec && sec.url) {
            window.location.href = sec.url;
          }
        }
      }
    });

    // Sincronización reactiva con eventos de cambio de idioma en el ecosistema
    window.addEventListener('nexordLangChanged', (e) => {
      const newLang = (e.detail && e.detail.lang) ? e.detail.lang : getCurrentNavLang();
      applyNavTranslations(newLang);
    });
    window.addEventListener('storage', (e) => {
      if (e.key === 'nexord_lang') {
        applyNavTranslations(e.newValue || 'es');
      }
    });
  }

  // Exportar helper para actualización forzada
  window.updateNexordNavLanguage = applyNavTranslations;

  // =========================================================================
  // UNIVERSAL FULLSCREEN ENGINE PARA EJERCICIOS PROPUESTOS (CANON NEXORD)
  // Permite abrir cualquier .canonical-exercise-box en Pantalla Completa
  // =========================================================================
  let activeExerciseBox = null;
  let activeExercisePlaceholder = null;

  function getOrCreateExerciseModal() {
    let modal = document.getElementById('universal-exercise-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'universal-exercise-modal';
    modal.className = 'universal-exercise-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Ejercicio Propuesto en Pantalla Completa');

    modal.innerHTML = `
      <div class="universal-exercise-modal-backdrop"></div>
      <div class="universal-exercise-modal-shell">
        <div class="universal-exercise-modal-header">
          <div class="universal-exercise-modal-brand">
            <span class="uem-logo">VISORD / NEXORD</span>
            <span class="uem-sep">·</span>
            <span class="uem-title">EJERCICIO PROPUESTO · PANTALLA COMPLETA</span>
          </div>
          <div class="universal-exercise-modal-actions">
            <button type="button" class="btn-uem-close" title="Cerrar pantalla completa (Esc)" aria-label="Cerrar">
              <span>✕</span> <span class="uem-close-text">Cerrar (Esc)</span>
            </button>
          </div>
        </div>
        <div class="universal-exercise-modal-body"></div>
      </div>
    `;

    document.body.appendChild(modal);

    const btnClose = modal.querySelector('.btn-uem-close');
    const backdrop = modal.querySelector('.universal-exercise-modal-backdrop');
    if (btnClose) btnClose.addEventListener('click', closeExerciseFullscreen);
    if (backdrop) backdrop.addEventListener('click', closeExerciseFullscreen);

    return modal;
  }

  function openExerciseFullscreen(box) {
    if (!box) return;
    const modal = getOrCreateExerciseModal();
    const body = modal.querySelector('.universal-exercise-modal-body');
    if (!body) return;

    if (activeExerciseBox && activeExercisePlaceholder) {
      closeExerciseFullscreen();
    }

    activeExerciseBox = box;
    activeExercisePlaceholder = document.createElement('div');
    activeExercisePlaceholder.className = 'exercise-box-placeholder';
    activeExercisePlaceholder.style.display = 'none';
    box.parentNode.insertBefore(activeExercisePlaceholder, box);

    // Guardar tooltip previo y retirarlo durante la vista ampliada
    box.dataset.prevTitle = box.getAttribute('title') || '';
    box.removeAttribute('title');

    box.classList.add('is-exercise-fullscreen');
    body.innerHTML = '';
    body.appendChild(box);

    // Personalizar el título de la cabecera del modal según el ejercicio activo
    const titleEl = box.querySelector('[id*="exercise-title"], [class*="exercise-title"]');
    const uemTitle = modal.querySelector('.uem-title');
    if (uemTitle) {
      if (titleEl && titleEl.textContent.trim()) {
        uemTitle.textContent = titleEl.textContent.trim().replace(/^[«"']+|[»"']+$/g, '') + ' · PANTALLA COMPLETA';
      } else {
        uemTitle.textContent = 'EJERCICIO PROPUESTO · PANTALLA COMPLETA';
      }
    }

    modal.classList.add('active');
    document.body.classList.add('exercise-modal-open');
  }

  function closeExerciseFullscreen() {
    if (!activeExerciseBox || !activeExercisePlaceholder) {
      const modal = document.getElementById('universal-exercise-modal');
      if (modal) modal.classList.remove('active');
      document.body.classList.remove('exercise-modal-open');
      return;
    }

    const modal = document.getElementById('universal-exercise-modal');
    activeExerciseBox.classList.remove('is-exercise-fullscreen');

    // Restaurar título/tooltip de apertura al volver a la vista normal
    if (activeExerciseBox.dataset.prevTitle !== undefined) {
      if (activeExerciseBox.dataset.prevTitle) {
        activeExerciseBox.setAttribute('title', activeExerciseBox.dataset.prevTitle);
      } else {
        activeExerciseBox.setAttribute('title', 'Haz clic en el cuadro para abrir en Pantalla Completa');
      }
      delete activeExerciseBox.dataset.prevTitle;
    }

    if (activeExercisePlaceholder.parentNode) {
      activeExercisePlaceholder.parentNode.insertBefore(activeExerciseBox, activeExercisePlaceholder);
      activeExercisePlaceholder.remove();
    }

    activeExerciseBox = null;
    activeExercisePlaceholder = null;

    if (modal) modal.classList.remove('active');
    document.body.classList.remove('exercise-modal-open');
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const modal = document.getElementById('universal-exercise-modal');
      if (modal && modal.classList.contains('active')) {
        closeExerciseFullscreen();
      }
    }
  });

  window.openExerciseFullscreen = openExerciseFullscreen;
  window.closeExerciseFullscreen = closeExerciseFullscreen;

  // Delegación de eventos global: pulsar el botón O pulsar en cualquier punto del cuadro de ejercicio abre pantalla completa
  document.addEventListener('click', (e) => {
    // 1. Botón explícito de maximizar/pantalla completa
    const fsBtn = e.target.closest('.btn-exercise-fullscreen');
    if (fsBtn) {
      e.preventDefault();
      e.stopPropagation();
      const box = fsBtn.closest('.canonical-exercise-box, [id^="exercise-box-"], [id*="exercise-box"], [id*="exercise"]');
      if (box && !box.classList.contains('is-exercise-fullscreen')) {
        openExerciseFullscreen(box);
      }
      return;
    }

    // 2. Botón de cerrar del modal o su backdrop
    if (e.target.closest('.btn-uem-close')) {
      e.preventDefault();
      e.stopPropagation();
      closeExerciseFullscreen();
      return;
    }
    if (e.target.classList && e.target.classList.contains('universal-exercise-modal-backdrop')) {
      e.preventDefault();
      closeExerciseFullscreen();
      return;
    }

    // 3. Pulsar en cualquier punto del cuadro de ejercicio para abrir pantalla completa
    const box = e.target.closest('.canonical-exercise-box, [id^="exercise-box-"], [id*="exercise-box"]');
    if (box) {
      // Si el cuadro ya está desplegado en pantalla completa dentro del modal, permitir interacción normal
      if (box.classList.contains('is-exercise-fullscreen') || (activeExerciseBox && activeExerciseBox === box)) {
        return;
      }

      // Si el clic fue sobre controles interactivos internos, respetar su funcionalidad original sin abrir modal
      if (e.target.closest('button, select, input, textarea, a, option, .calc-preset-btn, .calc-select, .calc-step-card, [data-prevent-expand]')) {
        return;
      }

      // En general, basta con pulsar el cuadro de ejercicio para abrir en pantalla completa
      e.preventDefault();
      openExerciseFullscreen(box);
    }
  });

  function setupExerciseBoxes() {
    const boxes = document.querySelectorAll('.canonical-exercise-box, [id^="exercise-box-"], [id*="exercise-box"]');
    boxes.forEach(box => {
      if (!box.classList.contains('canonical-exercise-box')) {
        box.classList.add('canonical-exercise-box');
      }

      if (!box.classList.contains('is-exercise-fullscreen')) {
        box.style.cursor = 'pointer';
        if (!box.hasAttribute('title') || box.getAttribute('title').trim() === '') {
          box.setAttribute('title', 'Haz clic en este cuadro para abrir en Pantalla Completa');
        }
      }

      if (box.querySelector('.btn-exercise-fullscreen')) return;

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'btn-exercise-fullscreen';
      btn.title = 'Abrir este Ejercicio Propuesto en Pantalla Completa (Maximizar)';
      btn.setAttribute('aria-label', 'Maximizar Ejercicio Propuesto');
      btn.innerHTML = '<span class="btn-fs-icon">⛶</span> <span class="btn-fs-label">Pantalla Completa</span>';

      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openExerciseFullscreen(box);
      });

      // Búsqueda del mejor punto de anclaje en la cabecera del cuadro
      const headerRow = box.querySelector('.exercise-header-row') ||
                        box.querySelector('[style*="justify-content:space-between"]') ||
                        box.querySelector('[style*="justify-content: space-between"]');

      if (headerRow) {
        // Si la fila tiene un contenedor de acciones a la derecha, añadir allí
        const rightGroup = headerRow.children.length > 1 ? headerRow.lastElementChild : null;
        if (rightGroup && (rightGroup.tagName === 'DIV' || rightGroup.tagName === 'SPAN') && rightGroup.children.length > 0) {
          rightGroup.appendChild(btn);
        } else {
          headerRow.appendChild(btn);
        }
      } else {
        const firstRow = box.firstElementChild;
        if (firstRow) {
          firstRow.appendChild(btn);
        } else {
          box.insertBefore(btn, box.firstChild);
        }
      }
    });
  }

  window.setupExerciseBoxes = setupExerciseBoxes;

  // Observador de mutaciones del DOM para capturar ejercicios inyectados dinámicamente
  let observerTimer = null;
  const domObserver = new MutationObserver(() => {
    if (observerTimer) clearTimeout(observerTimer);
    observerTimer = setTimeout(setupExerciseBoxes, 120);
  });

  // Inicializar al cargar el DOM y activar observador
  function initExerciseEngine() {
    injectPersistentNav();
    setupExerciseBoxes();
    if (document.body) {
      domObserver.observe(document.body, { childList: true, subtree: true });
    }
    setTimeout(setupExerciseBoxes, 400);
    setTimeout(setupExerciseBoxes, 1200);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initExerciseEngine);
  } else {
    initExerciseEngine();
  }
})();
