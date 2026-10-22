/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE VISORD 3D (G2T1C1 & G2T2C2)
 * =============================================================================
 * Soporte bilingüe completo (Español oficial / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const VISORD_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title_g2t1c1: 'VISORD 3D • Dossier General del Caso Empírico G2T1C1 (Ventana Única)',
      page_title_g2t2c2: 'NEXORD G2T2C2 • Motor Universal de Hipercubos Multidimensionales',
      brand_sub_g2t2c2: 'MOTOR UNIVERSAL DE HIPERCUBOS MULTIDIMENSIONALES',

      // HUD actions
      btn_nota: '💡 Nota Explicativa',
      btn_suite: '🗂️ Suite Diagnóstica',
      btn_hipercubo: '🧊 Hipercubo G2T2C2',
      btn_cockpit: '📊 COCKPIT MATRICES',
      btn_load_json: '📂 Cargar Dataset .json',
      btn_methodology: '💡 Metodología',
      btn_web_main: '🏠 Web Principal',

      // Vertical Nav
      vnav_title: 'EXPLORADOR G2T1C1',
      vnav_1: '1. Vista 3D Moviola',
      vnav_2: '2. Motor 10 Densidades',
      vnav_3: '3. Árbol CAJ (Ward)',
      vnav_4: '4. Inter-Proximidades',
      vnav_5: '5. Tablas Oficiales',
      vnav_6: '6. Galería Gráfica',
      vnav_7: '7. Fichas Individuales',
      vnav_8: '8. Dossier Global',

      // HUD Number buttons words
      hud_w1: '3D',
      hud_w2: 'DENSIDAD',
      hud_w3: 'CAJ',
      hud_w4: 'PROXIMIDAD',
      hud_w5: 'TABLAS',
      hud_w6: 'APA7',
      hud_w7: 'FICHAS',
      hud_w8: 'DOSSIER'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title_g2t1c1: 'VISORD 3D • Empirical Case G2T1C1 General Dossier (Single Window)',
      page_title_g2t2c2: 'NEXORD G2T2C2 • Universal Multidimensional Hypertensor Engine',
      brand_sub_g2t2c2: 'UNIVERSAL MULTIDIMENSIONAL HYPERTENSOR ENGINE',

      // HUD actions
      btn_nota: '💡 Explanatory Note',
      btn_suite: '🗂️ Diagnostic Suite',
      btn_hipercubo: '🧊 Hypertensor G2T2C2',
      btn_cockpit: '📊 COCKPIT MATRICES',
      btn_load_json: '📂 Load Dataset .json',
      btn_methodology: '💡 Methodology',
      btn_web_main: '🏠 Main Portal',

      // Vertical Nav
      vnav_title: 'G2T1C1 EXPLORER',
      vnav_1: '1. 3D Moviola View',
      vnav_2: '2. 10 Densities Engine',
      vnav_3: '3. CAJ Tree (Ward)',
      vnav_4: '4. Inter-Proximities',
      vnav_5: '5. Official Tables',
      vnav_6: '6. Graphic Gallery',
      vnav_7: '7. Individual Profiles',
      vnav_8: '8. Global Dossier',

      // HUD Number buttons words
      hud_w1: '3D',
      hud_w2: 'DENSITY',
      hud_w3: 'CAJ',
      hud_w4: 'PROXIMITY',
      hud_w5: 'TABLES',
      hud_w6: 'APA7',
      hud_w7: 'PROFILES',
      hud_w8: 'DOSSIER'
    }
  };

  function applyLanguage(lang) {
    const d = VISORD_I18N[lang] || VISORD_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Selector buttons
    const btnEs = document.getElementById('btn-visord-lang-es');
    const btnEn = document.getElementById('btn-visord-lang-en');
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
    if (window.location.pathname.includes('visord_g2t2c2')) {
      document.title = d.page_title_g2t2c2;
      const sub = document.querySelector('.brand-sub');
      if (sub) sub.textContent = d.brand_sub_g2t2c2;
      const btnLoad = document.getElementById('btn-trigger-file');
      if (btnLoad) btnLoad.textContent = d.btn_load_json;
      const btnNota = document.getElementById('btn-open-nota');
      if (btnNota) btnNota.textContent = d.btn_methodology;
      const btnHome = document.querySelector('.header-actions a[href="index.html"]');
      if (btnHome) btnHome.textContent = d.btn_web_main;
    } else {
      document.title = d.page_title_g2t1c1;

      // Buttons
      const btnNota = document.getElementById('btn-open-nota');
      if (btnNota) btnNota.textContent = d.btn_nota;
      const btnSuite = document.querySelector('.header-actions a[href="suite_g2t1c1.html"]');
      if (btnSuite) btnSuite.textContent = d.btn_suite;
      const btnHiper = document.querySelector('.header-actions a[href="visord_g2t2c2.html"]');
      if (btnHiper) btnHiper.textContent = d.btn_hipercubo;

      // Vertical Nav
      const dockTitle = document.querySelector('.dock-hdr-title');
      if (dockTitle) dockTitle.textContent = d.vnav_title;
      const vnavBtns = document.querySelectorAll('.vnav-btn .vnav-text');
      if (vnavBtns.length >= 8) {
        vnavBtns[0].textContent = d.vnav_1;
        vnavBtns[1].textContent = d.vnav_2;
        vnavBtns[2].textContent = d.vnav_3;
        vnavBtns[3].textContent = d.vnav_4;
        vnavBtns[4].textContent = d.vnav_5;
        vnavBtns[5].textContent = d.vnav_6;
        vnavBtns[6].textContent = d.vnav_7;
        vnavBtns[7].textContent = d.vnav_8;
      }

      // HUD cluster words
      const hudWords = document.querySelectorAll('.hud-num-word');
      if (hudWords.length >= 8) {
        hudWords[0].textContent = d.hud_w1;
        hudWords[1].textContent = d.hud_w2;
        hudWords[2].textContent = d.hud_w3;
        hudWords[3].textContent = d.hud_w4;
        hudWords[4].textContent = d.hud_w5;
        hudWords[5].textContent = d.hud_w6;
        hudWords[6].textContent = d.hud_w7;
        hudWords[7].textContent = d.hud_w8;
      }
    }
  }

  window.setVisordG2Language = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
