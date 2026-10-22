/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DEL MULTIPOLÍGRAFO 18D
 * =============================================================================
 * Soporte bilingüe completo (Español oficial / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const MULTI_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'NEXORD • Multipolígrafo Socio-Termodinámico 18D (Hipertensor G3T3C2)',
      header_title: 'MULTIPOLÍGRAFO SOCIO-TERMODINÁMICO 18D',
      header_sub: 'HIPERTENSOR G3T3C2 · 6 CARRILES PAREADOS · DIAGNÓSTICO PSICOSOCIAL DE CAMPO EN CONTINUO Q81',
      
      pill_design: 'DISEÑO:',
      pill_matrices: 'MATRICES:',
      pill_date: 'FECHA:',

      btn_manifesto: '📖 Manifiesto',
      btn_data: '📊 Datos (CSV)',
      btn_mural: '📸 Mural (PNG)',
      btn_scroll: '📜 Mural Scroll',
      btn_reset: '↺ Reset',
      btn_exit: '✕ Salir',

      flank_time_title: '⏱️ TIEMPO LONGITUDINAL',
      time_desc_all: 'Mostrando los 3 tiempos colapsados en sub-píxeles sucesivos.',
      time_all: 'Todos (T1·T2·T3)',
      time_t1: 'T1: Inicial',
      time_t2: 'T2: Intervención',
      time_t3: 'T3: Final',

      flank_signals_title: '⚡ SEÑALES 18D',
      flank_moviola_title: '🎬 MOVIOLA CINEMÁTICA'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'NEXORD • 18D Socio-Thermodynamic Multipolygraph (Hypertensor G3T3C2)',
      header_title: '18D SOCIO-THERMODYNAMIC MULTIPOLYGRAPH',
      header_sub: 'HYPERTENSOR G3T3C2 · 6 PAIRED LANES · CONTINUOUS FIELD PSYCHOSOCIAL DIAGNOSIS Q81',

      pill_design: 'DESIGN:',
      pill_matrices: 'MATRICES:',
      pill_date: 'DATE:',

      btn_manifesto: '📖 Manifesto',
      btn_data: '📊 Data (CSV)',
      btn_mural: '📸 Mural (PNG)',
      btn_scroll: '📜 Scroll Mural',
      btn_reset: '↺ Reset',
      btn_exit: '✕ Exit',

      flank_time_title: '⏱️ LONGITUDINAL TIME',
      time_desc_all: 'Displaying 3 collapsed waves across successive sub-pixels.',
      time_all: 'All (T1·T2·T3)',
      time_t1: 'T1: Baseline',
      time_t2: 'T2: Intervention',
      time_t3: 'T3: Outcome',

      flank_signals_title: '⚡ 18D SIGNALS',
      flank_moviola_title: '🎬 KINEMATIC MOVIOLA'
    }
  };

  function applyLanguage(lang) {
    const d = MULTI_I18N[lang] || MULTI_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Selector buttons
    const btnEs = document.getElementById('btn-multi-lang-es');
    const btnEn = document.getElementById('btn-multi-lang-en');
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

    // Page title
    document.title = d.page_title;

    // Header title and sub
    const h1 = document.querySelector('.brand-title h1');
    if (h1) h1.textContent = d.header_title;
    const sub = document.querySelector('.brand-title span');
    if (sub) sub.textContent = d.header_sub;

    // Pills
    const pills = document.querySelectorAll('.header-hud-meta .hud-pill strong');
    if (pills.length >= 3) {
      pills[0].textContent = d.pill_design;
      pills[1].textContent = d.pill_matrices;
      pills[2].textContent = d.pill_date;
    }

    // Buttons
    const btnMan = document.querySelector('.btn-manifiesto');
    if (btnMan) btnMan.textContent = d.btn_manifesto;
    const btnData = document.querySelector('.btn-dataset-csv');
    if (btnData) btnData.textContent = d.btn_data;
    const btnMural = document.querySelector('.btn-mural-png');
    if (btnMural) btnMural.textContent = d.btn_mural;
    const btnScroll = document.getElementById('btn-toggle-rolling');
    if (btnScroll) btnScroll.textContent = d.btn_scroll;
    const btnExit = document.getElementById('btn-header-exit');
    if (btnExit) btnExit.textContent = d.btn_exit;

    // Flank titles
    const flankTitles = document.querySelectorAll('.flank-card-title');
    flankTitles.forEach(ft => {
      const txt = ft.textContent;
      if (txt.includes('TIEMPO') || txt.includes('LONGITUDINAL')) ft.textContent = d.flank_time_title;
      else if (txt.includes('SEÑALES') || txt.includes('SIGNALS')) ft.textContent = d.flank_signals_title;
      else if (txt.includes('MOVIOLA')) ft.textContent = d.flank_moviola_title;
    });

    const timeDesc = document.getElementById('temporal-wave-desc');
    if (timeDesc) timeDesc.textContent = d.time_desc_all;

    const tAll = document.querySelector('#btn-t-all strong');
    if (tAll) tAll.textContent = d.time_all;
    const t1 = document.querySelector('#btn-t-1 strong');
    if (t1) t1.textContent = d.time_t1;
    const t2 = document.querySelector('#btn-t-2 strong');
    if (t2) t2.textContent = d.time_t2;
    const t3 = document.querySelector('#btn-t-3 strong');
    if (t3) t3.textContent = d.time_t3;
  }

  window.setMultiLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
