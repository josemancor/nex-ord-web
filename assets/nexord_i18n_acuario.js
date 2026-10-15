/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE VISORD ACUARIO 3D
 * =============================================================================
 * Soporte bilingüe completo (Español canónico / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const ACUARIO_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'VISORD • Acuario Socio-Termodinámico 3D & Ecosistema D18',
      header_sub: 'Espacio Volumétrico Continuo • Pecera de Cristal • Fondo Arenoso vs Superficie Libre • Burbujas Vivas',
      badge_eco: 'ECOSISTEMA D18',
      badge_hydro: '3D HIDRODINÁMICO',

      // Botones de Cabecera
      btn_action_motion: 'ACCIÓN: EN MOVIMIENTO',
      btn_action_paused: 'ACCIÓN: EN PAUSA',
      btn_guide: 'GUÍA PEDAGÓGICA',
      btn_editor: 'EDITOR SMIb',
      btn_resources: 'RECURSOS',

      // Módulo 1: Escenarios
      sec1_title: '1. ESCENARIOS MULTIESCALA (N×N)',
      sec1_series_title: '3 EJERCICIOS DE SERIE (EXPLORACIÓN)',
      sec1_series_badge: 'Activos',
      scen_20_title: 'EJERCICIO 1: Dinámica Cohesiva Canónica',
      scen_20_desc: 'Flotabilidad Z_mar, Baricentro y 6 Prismas',
      scen_simul2_title: 'EJERCICIO 2: Ostracismo y Ruptura Diádica',
      scen_simul2_desc: 'Marginación invisible nodo 5B1a vs Núcleo',
      scen_simul3_title: 'EJERCICIO 3: Alta Entropía y Fricción Polar',
      scen_simul3_desc: 'Dispersión caótica y gradiente de escape',
      scen_custom_title: 'MATRIZ PERSONALIZADA SMIb',
      scen_custom_desc: 'Cargar JSON / CSV o editar en vivo',

      // Módulo 2: Proyección
      sec2_title: '2. PROYECCIÓN 1 A 1 & MODOS DA / RC',
      sec2_mode_badge: 'Baricentro',
      btn_mode_dual: 'DUAL',
      btn_mode_da: 'EMISIÓN (DA)',
      btn_mode_rc: 'RECEPCIÓN (RC)',
      lbl_step_play: 'Sujetos',

      // Módulo 3: Figuras
      sec3_title: '3. FIGURAS RELACIONALES',
      fig_all: 'Todas',
      fig_ee: 'Elección Mutua',
      fig_rr: 'Rechazo Mutuo',
      fig_opp: 'Oposición',
      fig_neu: 'Indiferencia',

      // Módulo 4: Densidades
      sec4_title: '4. LAS 18 DENSIDADES (D18)',
      dens_desc: 'Espectro continuo de masas de emisión (SDA), recepción (SRC) y saldos relativos (SDR).',

      // Módulo 5: Lámina marina
      sec5_title: '5. LÁMINA DE AGUA (Z_mar)',
      sec5_desc: 'Nivel hidrostático de flotabilidad relacional.',

      // Módulo 6: Cámara
      sec6_title: '6. CÁMARA 360º & VISTAS',
      cam_front: '👁️ Frontal',
      cam_top: '📐 Cenital 2D',
      cam_reset: '↺ Reset',

      // Modal Guía Pedagógica
      guide_title: 'GUÍA MAESTRA • VISORD ACUARIO 3D',
      guide_sub: 'Comprensión hidrodinámica del clima grupal mediante gemelo digital 3D',
      guide_p1_h: '1. ¿Qué es el VISORD Acuario?',
      guide_p1_t: 'Es una metáfora hidrostática de precisión física donde cada sujeto es un pez u organismo cuya <strong>profundidad (Z)</strong> representa su nivel de aceptación o flotabilidad (saldo SDR), su <strong>velocidad</strong> traduce la entropía o reactividad, y las <strong>burbujas</strong> señalan las micro-interacciones del campo relacional.',
      guide_p2_h: '2. Resolución de la «Figura Sintética» sin Cancelaciones',
      guide_p2_t: 'A diferencia de las sumas sociométricas clásicas que anulan atracciones y rechazos contrarios, VISORD calcula simultáneamente la masa absoluta (BDR) y el saldo de densidad relativa (SDR) con ponderación física $W(k)=2^{1-k}$.',
      guide_close: 'Cerrar Guía'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'VISORD • 3D Socio-Thermodynamic Aquarium & D18 Ecosystem',
      header_sub: 'Continuous Volumetric Space • Glass Aquarium • Sandy Seabed vs Free Surface • Living Bubbles',
      badge_eco: 'D18 ECOSYSTEM',
      badge_hydro: '3D HYDRODYNAMIC',

      // Header buttons
      btn_action_motion: 'ACTION: IN MOTION',
      btn_action_paused: 'ACTION: PAUSED',
      btn_guide: 'PEDAGOGICAL GUIDE',
      btn_editor: 'SMIb EDITOR',
      btn_resources: 'RESOURCES',

      // Module 1: Scenarios
      sec1_title: '1. MULTISCALE SCENARIOS (N×N)',
      sec1_series_title: '3 STANDARD EXERCISES (EXPLORATION)',
      sec1_series_badge: 'Active',
      scen_20_title: 'EXERCISE 1: Canonical Cohesive Dynamics',
      scen_20_desc: 'Z_sea Buoyancy, Barycenter & 6 Prisms',
      scen_simul2_title: 'EXERCISE 2: Ostracism & Dyadic Rupture',
      scen_simul2_desc: 'Invisible exclusion node 5B1a vs Core',
      scen_simul3_title: 'EXERCISE 3: High Entropy & Polar Friction',
      scen_simul3_desc: 'Chaotic dispersion and escape gradient',
      scen_custom_title: 'CUSTOM SMIb MATRIX',
      scen_custom_desc: 'Upload JSON / CSV or live editor',

      // Module 2: Projection
      sec2_title: '2. 1-ON-1 PROJECTION & DA / RC MODES',
      sec2_mode_badge: 'Barycenter',
      btn_mode_dual: 'DUAL',
      btn_mode_da: 'EMISSION (DA)',
      btn_mode_rc: 'RECEPTION (RC)',
      lbl_step_play: 'Subjects',

      // Module 3: Figures
      sec3_title: '3. RELATIONAL FIGURES',
      fig_all: 'All',
      fig_ee: 'Mutual Choice',
      fig_rr: 'Mutual Reject',
      fig_opp: 'Opposition',
      fig_neu: 'Indifference',

      // Module 4: Densities
      sec4_title: '4. THE 18 DENSITIES (D18)',
      dens_desc: 'Continuous spectrum of emission masses (SDA), reception masses (SRC), and relative balances (SDR).',

      // Module 5: Water Level
      sec5_title: '5. WATER SURFACE LEVEL (Z_sea)',
      sec5_desc: 'Hydrostatic relational buoyancy waterline.',

      // Module 6: Camera
      sec6_title: '6. 360º CAMERA & VIEWS',
      cam_front: '👁️ Frontal',
      cam_top: '📐 Top 2D',
      cam_reset: '↺ Reset',

      // Pedagogical Modal
      guide_title: 'MASTER GUIDE • VISORD AQUARIUM 3D',
      guide_sub: 'Hydrodynamic understanding of relational climate via 3D digital twin',
      guide_p1_h: '1. What is the VISORD Aquarium?',
      guide_p1_t: 'It is a physical-hydrostatic metaphor where each participant is represented as an organism whose <strong>depth (Z)</strong> denotes their acceptance or buoyancy level (SDR balance), their <strong>swimming speed</strong> denotes relational entropy or reactivity, and <strong>bubbles</strong> visualize emergent micro-interactions.',
      guide_p2_h: '2. Synthetic Figure Resolution without Cancellation',
      guide_p2_t: 'Unlike classical sociometric sums that cancel out opposing attractions and rejections, VISORD computes absolute mass (BDR) and relative density balance (SDR) simultaneously with physical weighting $W(k)=2^{1-k}$.',
      guide_close: 'Close Guide'
    }
  };

  function applyLanguage(lang) {
    const d = ACUARIO_I18N[lang] || ACUARIO_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Selector buttons
    const btnEs = document.getElementById('btn-acuario-lang-es');
    const btnEn = document.getElementById('btn-acuario-lang-en');
    if (btnEs && btnEn) {
      if (lang === 'en') {
        btnEn.style.background = '#00FF87';
        btnEn.style.color = '#030308';
        btnEs.style.background = 'transparent';
        btnEs.style.color = '#94A3B8';
      } else {
        btnEs.style.background = '#00FF87';
        btnEs.style.color = '#030308';
        btnEn.style.background = 'transparent';
        btnEn.style.color = '#94A3B8';
      }
    }

    // Page title & subtitle
    document.title = d.page_title;
    const subP = document.querySelector('header p.mono');
    if (subP) subP.textContent = d.header_sub;

    // Header buttons
    const lblMaster = document.getElementById('lbl-master-top');
    if (lblMaster) {
      const isPaused = document.getElementById('btn-master-top')?.classList.contains('bg-rose-950');
      lblMaster.textContent = isPaused ? d.btn_action_paused : d.btn_action_motion;
    }

    const headerBtns = document.querySelectorAll('header .action-btn');
    headerBtns.forEach(btn => {
      const txt = btn.textContent;
      if (txt.includes('PEDAGÓGICA') || txt.includes('PEDAGOGICAL')) {
        btn.querySelector('span:last-child').textContent = d.btn_guide;
      } else if (txt.includes('EDITOR')) {
        btn.querySelector('span:last-child').textContent = d.btn_editor;
      } else if (txt.includes('RECURSOS') || txt.includes('RESOURCES')) {
        btn.querySelector('span:last-child').textContent = d.btn_resources;
      }
    });

    // Section headers
    const h2s = document.querySelectorAll('aside h2');
    h2s.forEach(h2 => {
      const t = h2.textContent;
      if (t.includes('1. ESCENARIOS') || t.includes('1. MULTISCALE')) h2.textContent = d.sec1_title;
      else if (t.includes('2. PROYECCIÓN') || t.includes('2. 1-ON-1')) h2.textContent = d.sec2_title;
      else if (t.includes('3. FIGURAS') || t.includes('3. RELATIONAL')) h2.textContent = d.sec3_title;
      else if (t.includes('4. LAS 18') || t.includes('4. THE 18')) h2.textContent = d.sec4_title;
      else if (t.includes('5. LÁMINA') || t.includes('5. WATER')) h2.textContent = d.sec5_title;
      else if (t.includes('6. CÁMARA') || t.includes('6. 360º')) h2.textContent = d.sec6_title;
    });

    // Scenario titles
    const scen20 = document.getElementById('btn-scen-20x20');
    if (scen20) {
      const t = scen20.querySelector('.outfit');
      if (t) t.textContent = d.scen_20_title;
      const desc = scen20.querySelector('.mono');
      if (desc) desc.textContent = d.scen_20_desc;
    }

    const scenSimul2 = document.getElementById('btn-scen-simul_02');
    if (scenSimul2) {
      const t = scenSimul2.querySelector('.outfit');
      if (t) t.textContent = d.scen_simul2_title;
      const desc = scenSimul2.querySelector('.mono');
      if (desc) desc.textContent = d.scen_simul2_desc;
    }

    const scenSimul3 = document.getElementById('btn-scen-simul_03');
    if (scenSimul3) {
      const t = scenSimul3.querySelector('.outfit');
      if (t) t.textContent = d.scen_simul3_title;
      const desc = scenSimul3.querySelector('.mono');
      if (desc) desc.textContent = d.scen_simul3_desc;
    }

    // Modal
    const modalTitle = document.getElementById('modal-pedagogic-title');
    if (modalTitle) modalTitle.textContent = d.guide_title;
    const modalClose = document.getElementById('btn-modal-pedagogic-close');
    if (modalClose) modalClose.textContent = d.guide_close;
  }

  window.setAcuarioLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
