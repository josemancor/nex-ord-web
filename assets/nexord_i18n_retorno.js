/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE RETORNO AL PARTICIPANTE
 * =============================================================================
 * Soporte bilingüe completo (Español canónico / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const RETORNO_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'Acceso de Participantes • NEXORD / VISORD',
      portal_sub: 'SISTEMA PRIVADO DE AUTOCONOCIMIENTO Y CLIMA RELACIONAL',
      badge_validating: 'TOKEN: VALIDANDO...',

      prompt_title: '🔐 Acceso Privado del Participante',
      prompt_desc: 'Introduce la clave personal o token intransferible facilitado por el Investigador Principal:',
      prompt_placeholder: 'TOK_1A_...',
      prompt_btn: 'Ingresar al Portal →',

      tab_group: '🌐 El Pulso de Nuestro Equipo',
      tab_personal: '👤 Tu Ficha Personal de Crecimiento',

      group_title: 'Estado Relacional del Colectivo',
      group_intro: 'Este informe ofrece una panorámica global del clima y la energía compartida de tu equipo. Refleja cómo cooperamos y qué valores destacan en nuestra dinámica cotidiana, sin comparaciones individuales.',
      lbl_cohesion: 'Índice de Cohesión (ICE)',
      lbl_vitality: 'Vitalidad Adaptativa (Φ)',
      lbl_focus: 'Enfoque Colaborativo',
      group_virtues_title: '🌟 Virtudes y Valores Más Reconocidos en el Grupo:',

      personal_title: 'Tu Ficha de Autoconocimiento y Fortalezas',
      personal_intro: 'Esta sección es estrictamente confidencial. Refleja tu huella positiva y las percepciones compartidas que enriquecen tu desarrollo personal dentro del colectivo.',
      ethical_title: '🛡️ Garantía Deontológica Inviolable (Regla 21):',
      ethical_text: 'Los datos sociométricos se procesan con fines exclusivamente formativos y no punitivos. Queda terminantemente proscrito cualquier uso disciplinario o lesivo de la autoestima personal.'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'Participant Access • NEXORD / VISORD',
      portal_sub: 'PRIVATE SYSTEM FOR SELF-KNOWLEDGE AND RELATIONAL CLIMATE',
      badge_validating: 'TOKEN: VALIDATING...',

      prompt_title: '🔐 Private Participant Access',
      prompt_desc: 'Enter the personal and non-transferable token provided by the Principal Investigator:',
      prompt_placeholder: 'TOK_1A_...',
      prompt_btn: 'Enter Portal →',

      tab_group: '🌐 Our Team\'s Pulse',
      tab_personal: '👤 Your Personal Growth Profile',

      group_title: 'Collective Relational State',
      group_intro: 'This report offers an overarching overview of the shared relational climate and collective energy of your team, reflecting collaborative dynamics without individual rankings.',
      lbl_cohesion: 'Cohesion Index (ICE)',
      lbl_vitality: 'Adaptive Vitality (Φ)',
      lbl_focus: 'Collaborative Focus',
      group_virtues_title: '🌟 Most Recognized Virtues and Values in the Group:',

      personal_title: 'Your Self-Knowledge & Strengths Profile',
      personal_intro: 'This section is strictly confidential. It highlights your positive imprint and shared strengths that nurture your growth within the collective.',
      ethical_title: '🛡️ Inviolable Deontological Guarantee (Rule 21):',
      ethical_text: 'Sociometric data is processed exclusively for formative, non-punitive development. Any disciplinary usage or damage to individual self-esteem is strictly prohibited.'
    }
  };

  function applyLanguage(lang) {
    const d = RETORNO_I18N[lang] || RETORNO_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Selector buttons
    const btnEs = document.getElementById('btn-retorno-lang-es');
    const btnEn = document.getElementById('btn-retorno-lang-en');
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

    // Header sub
    const sub = document.querySelector('.portal-sub');
    if (sub) sub.textContent = d.portal_sub;

    // Token prompt
    const promptTitle = document.querySelector('#box-token-prompt h2');
    if (promptTitle) promptTitle.textContent = d.prompt_title;
    const promptDesc = document.querySelector('#box-token-prompt p');
    if (promptDesc) promptDesc.textContent = d.prompt_desc;
    const promptInput = document.getElementById('manual-token');
    if (promptInput) promptInput.placeholder = d.prompt_placeholder;
    const promptBtn = document.querySelector('.token-btn');
    if (promptBtn) promptBtn.textContent = d.prompt_btn;

    // Tabs
    const tabs = document.querySelectorAll('.portal-tabs .tab-btn');
    if (tabs.length >= 2) {
      tabs[0].innerHTML = '<span>🌐</span> ' + d.tab_group.replace('🌐 ', '');
      tabs[1].innerHTML = '<span>👤</span> ' + d.tab_personal.replace('👤 ', '');
    }

    // Tab 1 (Group)
    const grpTitle = document.querySelector('#tab-group .section-title');
    if (grpTitle) grpTitle.innerHTML = '<span>🌐</span> ' + d.group_title;
    const grpIntro = document.getElementById('group-intro');
    if (grpIntro) grpIntro.textContent = d.group_intro;

    const metricLabels = document.querySelectorAll('#tab-group .metric-label');
    if (metricLabels.length >= 3) {
      metricLabels[0].textContent = d.lbl_cohesion;
      metricLabels[1].textContent = d.lbl_vitality;
      metricLabels[2].textContent = d.lbl_focus;
    }

    const virtuesH3 = document.querySelector('#tab-group h3');
    if (virtuesH3) virtuesH3.textContent = d.group_virtues_title;

    // Tab 2 (Personal)
    const perTitle = document.querySelector('#tab-personal .section-title');
    if (perTitle) perTitle.innerHTML = '<span>👤</span> ' + d.personal_title;

    // Ethical banner
    const ethH4 = document.querySelector('.ethical-banner h4');
    if (ethH4) ethH4.textContent = d.ethical_title;
    const ethP = document.querySelector('.ethical-banner p');
    if (ethP) ethP.textContent = d.ethical_text;
  }

  window.setRetornoLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
