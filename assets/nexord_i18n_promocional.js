/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE LA HOME PROMOCIONAL
 * =============================================================================
 * Soporte bilingüe completo (Español canónico / English) con persistencia en
 * localStorage y propagación reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const PROMO_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'NEXORD | La Radiografía 3D de las Relaciones Humanas · VISORD Engine',
      meta_desc: 'NEXORD | Plataforma Científica de Sociometría Ordinal Computacional y Diagnóstico Socio-Termodinámico. Diagnóstico instantáneo, visual y 100% no punitivo.',

      // Barra de navegación
      nav_brand_sub: 'VISORD ENGINE',
      nav_why: '¿Por qué NEXORD?',
      nav_showroom: 'Joyas 3D',
      nav_solutions: 'Soluciones',
      nav_ethics: 'Garantía Ética',
      nav_dial: '🧭 Dial Orbital',
      nav_science: 'Ciencia & Docs ▾',
      nav_custody: '🏛️ Custodia Institucional',
      nav_cta: 'Probar en Vivo 3D',

      // Menú desplegable Ciencia & Docs
      drop_l1: 'Nivel 1: Moviola 3D Dinámica',
      drop_l2: 'Nivel 2: Matrices y Díadas',
      drop_l3: 'Nivel 3: Tetragrama SMIb',
      drop_l4: 'Nivel 4: Casos Forenses',
      drop_l5: 'Nivel 5: Grassmann & Fiedler',
      drop_l6: 'Nivel 6: Informes Forenses',
      drop_l7: 'Nivel 7: Manifiesto Zenodo',
      drop_framework: '📄 Marco de Custodia (PDF)',
      drop_deontology: '⚖️ Código Deontológico & RGPD',
      drop_glossary: 'Glosario Canónico (ES / EN)',
      drop_dial: '🧭 Dial Orbital Epistemológico',

      // Hero
      hero_pill: 'PLATAFORMA CIENTÍFICA DE SOCIOMETRÍA ORDINAL COMPUTACIONAL',
      hero_title: 'La Radiografía 3D de las<br><span class="gradient-text">Relaciones Humanas</span>',
      hero_subtitle: 'Descubre las corrientes invisibles, el liderazgo real, las alianzas latentes y el riesgo de ostracismo en tu grupo antes de que se conviertan en crisis. Diagnóstico instantáneo, visual y 100% no punitivo.',
      hero_btn_3d: '🚀 Explorar las 4 Joyas 3D',
      hero_btn_custody: '🏛️ Custodia Institucional',
      hero_btn_solutions: '💼 Soluciones Sectoriales',

      // Video Hero HUD
      video_badge: 'VISORD 3D ENGINE IN MOTION · DEMO OFICIAL',
      video_meta: '⏱️ 01:09 MIN · AUDIO OPCIONAL · SUBTÍTULOS BILINGÜES',
      bond_attraction_term: 'Verde:',
      bond_attraction_text: 'Atracción Mutua & Cohesión',
      bond_rejection_term: 'Magenta:',
      bond_rejection_text: 'Rechazo & Fricción Oculta',
      bond_ostracism_term: 'Periferia:',
      bond_ostracism_text: 'Ostracismo Invisible',
      video_sub_initial: 'NEXORD · Plataforma de Sociometría Ordinal Computacional y Socio-Termodinámica 3D',
      video_btn_play: 'Pausa',
      video_btn_play_pause: 'Reproducir',
      video_btn_mute_active: 'Mudo (Activar)',
      video_btn_mute_sound: 'Sonido Activo',
      video_btn_subs_es: 'Subtítulos: ES',
      video_btn_subs_en: 'Subtitles: EN',
      video_btn_subs_off: 'Subtítulos: OFF',
      video_btn_fs: 'Pantalla Completa',
      video_cta_pill: '🎮 Manipular Entorno 3D en Vivo',

      // Stats Bar
      stat_1_val: '4 Posiciones SMIb',
      stat_1_lbl: 'Dadores y Receptores Fácticos y Cognitivos',
      stat_2_val: '18 Densidades',
      stat_2_lbl: 'Descomposición Ortogonal en 3 Prismas Duales',
      stat_3_val: '7 Niveles',
      stat_3_lbl: 'De la Intuición 3D a la Topología de Grassmann',
      stat_4_val: '10 Dominios',
      stat_4_lbl: 'Ecosistémicos: Empresa, Sanidad, Deporte, Aula',

      // Sección Dolor
      pain_badge: 'EL DIAGNÓSTICO CIEGO',
      pain_title: 'La sociometría clásica colapsa ante la complejidad moderna',
      pain_desc: 'Los cuestionarios tradicionales de simpatía y clima laboral adolecen de limitaciones estructurales que impiden ver la verdadera salud del grupo:',
      pain_c1_title: 'Empates Artificiales y Pérdida de Jerarquía',
      pain_c1_desc: 'El formato de elecciones binarias ("elige a 3 compañeros") colapsa en empates artificiales donde todos parecen iguales, borrando la intensidad ordinal de atracción y rechazo.',
      pain_c2_title: 'Caja Negra sin Fundamentación Matemática',
      pain_c2_desc: 'Los índices sociométricos clásicos no verifican conservación de energía ni invariantes diádicos, generando diagnósticos no reproducibles y desconectados de leyes formales.',
      pain_c3_title: 'Ostracismo Invisible y Alianzas Latentes',
      pain_c3_desc: 'El aislamiento pasivo o la marginación encubierta quedan completamente ocultos en encuestas medias de satisfacción hasta que estallan en crisis irreversibles.',
      pain_c4_title: 'Riesgo Punitivo y Daño Deontológico',
      pain_c4_desc: 'Sin salvaguardas éticas por diseño, la sociometría tradicional se ha utilizado con fines punitivos (despidos, señalamientos), dañando la autoestima y la confianza grupal.',

      // Sección Showroom (4 Joyas)
      show_badge: 'SHOWROOM INTERACTIVO',
      show_title: 'VISORD: La Ventana 3D/4D a la Dinámica Grupal',
      show_desc: 'Cuatro entornos de exploración interactiva con visualización espacial en tiempo real, dinámica hidrodinámica y análisis espectral.',
      jewel_1_title: '1. VISORD_demo (3D/4D Continuo)',
      jewel_1_desc: 'Simulador de dinámica grupal continua, transiciones de fase líquida/gas y socio-termodinámica para colectivos de N < 51.',
      jewel_2_title: '2. VISORD_cultural (Dramaturgia)',
      jewel_2_desc: 'Sociometría cultural sobre obras maestras sin reactividad (12 Hombres sin Piedad, La Casa de Bernarda Alba).',
      jewel_3_title: '3. VISORD_radiológico (Ostracismo)',
      jewel_3_desc: 'Radiografías relacionales (15-27-54), variedades de Grassmann Gr(k,N) y diagnóstico precoz de ostracismo invisible.',
      jewel_4_title: '4. VISORD_dialéctico (Dilemas)',
      jewel_4_desc: 'Laboratorio de micro-interacciones, dilemas de Bienes Comunes, anfiteatro de tensiones y Moviola Bales IPA ↔ SMIb.',
      btn_jewel_launch: 'Explorar Entorno ➔',

      // Sección 7 Niveles
      sol_badge: 'ARQUITECTURA METODOLÓGICA',
      sol_title: 'Los 7 Niveles de la Sociometría Ordinal',
      sol_desc: 'Un recorrido escalonado desde la intuición visual inmediata hasta la formalización espectral y la custodia científica permanente.',
      l1_title: 'Nivel 1: Intuitivo',
      l1_desc: 'Moviola 3D y campos de fuerza interactivos. La interacción grupal visualizada como fluidos gravitatorios.',
      l2_title: 'Nivel 2: Básico',
      l2_desc: 'Matrices diádicas SMIb y descomposición del tetragrama (DA, RC, pDA, pRC). El circuito dar-recibir.',
      l3_title: 'Nivel 3: Esquema',
      l3_desc: 'Retícula universal Q81 (9×9) y síntesis canónica de figuras sociométricas en código computable.',
      l4_title: 'Nivel 4: Aplicaciones',
      l4_desc: 'Casos forenses de campo y laboratorios presenciales en 10 dominios ecosistémicos reales.',
      l5_title: 'Nivel 5: Matemático',
      l5_desc: 'Operadores de Estrada, Laplaciano de Heider, Fiedler λ₂, variedades de Grassmann Gr(k,N) e integración Φ.',
      l6_title: 'Nivel 6: Informes',
      l6_desc: 'Generación autónoma de informes forenses expertos, balances diádicos y dosieres individuales no punitivos.',
      l7_title: 'Nivel 7: Documentación',
      l7_desc: 'Manifiesto Científico Canónico v9.1, repositorios CERN Zenodo y especificación de Ciencia Abierta.',
      btn_level_enter: 'Entrar al Nivel ➔',

      // Sección Ética y Bóveda
      ethics_badge: 'DEONTOLOGÍA POR DISEÑO',
      ethics_title: 'Compromiso Inviolable de No Punición',
      ethics_desc: 'NEXORD está blindado por diseño para fines exclusivamente formativos, preventivos y de desarrollo grupal saludable. Queda expresamente prohibido su uso para despidos, listas de descarte o clasificación peyorativa.',
      ethics_item1: '<strong>Privacidad por Diseño:</strong> Anonimización matricial estricta (códigos posicionales 1A1a…5B1a).',
      ethics_item2: '<strong>Uso Exclusivamente Formativo:</strong> Devolución constructiva orientada al bienestar integral.',
      ethics_item3: '<strong>Acreditación del Investigador Principal (IP):</strong> Compromiso deontológico explícito y custodia ética.',

      vault_badge: 'SEGURIDAD CRIPTOGRÁFICA',
      vault_title: 'Protocolo Clélie & Sellado SHA3-512',
      vault_desc: 'Toda sociomatriz queda protegida con sellado criptográfico inmutable, verificación de invariantes y custodia descentralizada en el Banco Sociométrico (BSOC).',

      // Sección Custodia Institucional & Zenodo
      cust_badge: 'CIENCIA ABIERTA & REPOSITORIO PERMANENTE',
      cust_title: 'Custodia Internacional en CERN Zenodo',
      cust_desc: 'El corpus teórico, metodológico y los anexos técnicos están depositados a perpetuidad en el repositorio oficial del CERN (OpenAIRE) bajo licencia Creative Commons CC BY 4.0.',
      cust_man_title: 'Manifiesto Científico Central',
      cust_man_desc: 'Tratado fundacional de Sociometría Ordinal Computacional (Edición Canónica v9.1, Octubre 2026).',
      cust_sup_title: 'Material Suplementario & Anexos',
      cust_sup_desc: 'Respuestas a críticas, glosario enciclopédico bilingüe, anexo matemático y tablas canónicas.',
      cust_btn_man_es: '📄 Manifiesto ES (PDF)',
      cust_btn_man_en: '📄 Manifiesto EN (PDF)',
      cust_btn_sup: '📦 Ver en Zenodo (6 Docs) ↗',
      cust_btn_cite: '📜 Citar en BibTeX / APA / RIS',

      // CTA Banner
      cta_title: '¿Preparado para explorar la Física de lo Grupal?',
      cta_desc: 'Sumérgete en la Moviola 3D interactiva o accede a la suite metodológica completa.',
      cta_btn_start: '🚀 Iniciar Nivel 1 (Moviola 3D)',
      cta_btn_dial: '🧭 Explorar Dial Orbital (9 Sectores)',

      // Footer
      footer_lead: 'Hacia una Física de lo Grupal: Sociometría Ordinal Computacional & Ecosistema VISORD.',
      footer_rights: '© 2026 Dr. José Manuel Cornejo Álvarez. Todos los derechos reservados bajo Licencia Creative Commons CC BY 4.0.',
      footer_col_nav: 'Navegación Rápida',
      footer_col_science: 'Ciencia & Docs',
      footer_col_legal: 'Ética & Custodia',
      footer_legal_deont: 'Código Deontológico & RGPD',
      footer_legal_fair: 'Principios FAIR & Open Science',
      footer_legal_license: 'Licencia Abierta CC BY 4.0'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'NEXORD | The 3D Radiography of Human Relationships · VISORD Engine',
      meta_desc: 'NEXORD | Scientific Platform for Computational Ordinal Sociometry & Socio-Thermodynamic Diagnosis. Instantaneous, visual, and 100% non-punitive diagnosis.',

      // Navigation Bar
      nav_brand_sub: 'VISORD ENGINE',
      nav_why: 'Why NEXORD?',
      nav_showroom: '3D Jewels',
      nav_solutions: 'Solutions',
      nav_ethics: 'Ethical Safeguards',
      nav_dial: '🧭 Orbital Dial',
      nav_science: 'Science & Docs ▾',
      nav_custody: '🏛️ Institutional Stewardship',
      nav_cta: 'Try Live 3D',

      // Science & Docs Dropdown
      drop_l1: 'Level 1: Dynamic 3D Moviola',
      drop_l2: 'Level 2: Matrices & Dyads',
      drop_l3: 'Level 3: SMIb Tetragram',
      drop_l4: 'Level 4: Forensic Cases',
      drop_l5: 'Level 5: Grassmann & Fiedler',
      drop_l6: 'Level 6: Forensic Reports',
      drop_l7: 'Level 7: Zenodo Manifesto',
      drop_framework: '📄 Stewardship Framework (PDF)',
      drop_deontology: '⚖️ Deontological Code & GDPR',
      drop_glossary: 'Canonical Glossary (ES / EN)',
      drop_dial: '🧭 Epistemological Orbital Dial',

      // Hero
      hero_pill: 'SCIENTIFIC PLATFORM FOR COMPUTATIONAL ORDINAL SOCIOMETRY',
      hero_title: 'The 3D Radiography of<br><span class="gradient-text">Human Relationships</span>',
      hero_subtitle: 'Uncover invisible currents, authentic leadership, latent alliances, and hidden ostracism risks in your group before they become crises. Instantaneous, visual, and 100% non-punitive diagnosis.',
      hero_btn_3d: '🚀 Explore the 4 3D Jewels',
      hero_btn_custody: '🏛️ Institutional Stewardship',
      hero_btn_solutions: '💼 Sectoral Solutions',

      // Video Hero HUD
      video_badge: 'VISORD 3D ENGINE IN MOTION · OFFICIAL DEMO',
      video_meta: '⏱️ 01:09 MIN · OPTIONAL AUDIO · BILINGUAL SUBTITLES',
      bond_attraction_term: 'Green:',
      bond_attraction_text: 'Mutual Attraction & Cohesion',
      bond_rejection_term: 'Magenta:',
      bond_rejection_text: 'Rejection & Hidden Friction',
      bond_ostracism_term: 'Periphery:',
      bond_ostracism_text: 'Invisible Ostracism',
      video_sub_initial: 'NEXORD · Computational Ordinal Sociometry Platform & 3D Socio-Thermodynamics',
      video_btn_play: 'Pause',
      video_btn_play_pause: 'Play',
      video_btn_mute_active: 'Muted (Enable)',
      video_btn_mute_sound: 'Sound Active',
      video_btn_subs_es: 'Subtitles: ES',
      video_btn_subs_en: 'Subtitles: EN',
      video_btn_subs_off: 'Subtitles: OFF',
      video_btn_fs: 'Full Screen',
      video_cta_pill: '🎮 Manipulate Live 3D Environment',

      // Stats Bar
      stat_1_val: '4 SMIb Positions',
      stat_1_lbl: 'Factual & Cognitive Senders and Receivers',
      stat_2_val: '18 Densities',
      stat_2_lbl: 'Orthogonal Decomposition across 3 Dual Prisms',
      stat_3_val: '7 Levels',
      stat_3_lbl: 'From 3D Intuition to Grassmann Topology',
      stat_4_val: '10 Domains',
      stat_4_lbl: 'Ecosystemic: Corporate, Clinical, Sports, Education',

      // Pain Section
      pain_badge: 'THE BLIND DIAGNOSIS',
      pain_title: 'Classical sociometry collapses before modern complexity',
      pain_desc: 'Traditional climate surveys and binary sociograms suffer from structural handicaps that conceal genuine group health:',
      pain_c1_title: 'Artificial Ties & Loss of Hierarchy',
      pain_c1_desc: 'Binary election formats ("choose 3 colleagues") collapse into artificial ties where everyone appears identical, obliterating ordinal attraction and rejection intensities.',
      pain_c2_title: 'Black-Box Analytics Without Mathematical Grounding',
      pain_c2_desc: 'Classical sociometric metrics fail to verify energy conservation or dyadic invariants, yielding irreproducible diagnostics detached from formal laws.',
      pain_c3_title: 'Invisible Ostracism & Latent Factions',
      pain_c3_desc: 'Passive isolation and covert alienation remain completely hidden in average satisfaction surveys until erupting into irreversible group breakdown.',
      pain_c4_title: 'Punitive Risk & Deontological Harm',
      pain_c4_desc: 'Without security-by-design ethics, traditional sociometry has been misused for punitive dismissals, harming personal dignity and collective psychological safety.',

      // Showroom Section (4 Jewels)
      show_badge: 'INTERACTIVE SHOWROOM',
      show_title: 'VISORD: The 3D/4D Window into Group Dynamics',
      show_desc: 'Four interactive exploration laboratories featuring real-time spatial visualization, hydrodynamic dynamics, and spectral analysis.',
      jewel_1_title: '1. VISORD_demo (Continuous 3D/4D)',
      jewel_1_desc: 'Continuous group dynamics simulator, liquid/gas phase transitions, and socio-thermodynamics for cohorts of N < 51.',
      jewel_2_title: '2. VISORD_cultural (Dramaturgy)',
      jewel_2_desc: 'Cultural sociometry on masterworks with zero reactivity (12 Angry Men, The House of Bernarda Alba).',
      jewel_3_title: '3. VISORD_radiological (Ostracism)',
      jewel_3_desc: 'Relational radiographies (15-27-54), Grassmann manifolds Gr(k,N), and early diagnosis of invisible ostracism.',
      jewel_4_title: '4. VISORD_dialectical (Dilemmas)',
      jewel_4_desc: 'Micro-interaction lab, Common Goods dilemmas, tension amphitheater, and Bales IPA ↔ SMIb Moviola.',
      btn_jewel_launch: 'Explore Environment ➔',

      // 7 Levels Section
      sol_badge: 'METHODOLOGICAL ARCHITECTURE',
      sol_title: 'The 7 Levels of Ordinal Sociometry',
      sol_desc: 'A stepwise itinerary from immediate visual intuition to spectral formalization and permanent scientific stewardship.',
      l1_title: 'Level 1: Intuitive',
      l1_desc: 'Interactive 3D Moviola and vector fields. Interpersonal dynamics modeled as gravitational fluids.',
      l2_title: 'Level 2: Basic',
      l2_desc: 'SMIb dyadic matrices and tetragram decomposition (DA, RC, pDA, pRC). The give-and-receive circuit.',
      l3_title: 'Level 3: Schema',
      l3_desc: 'Universal Q81 (9×9) lattice and canonical synthesis of computable sociometric figures.',
      l4_title: 'Level 4: Applications',
      l4_desc: 'Forensic field case studies and live experimental laboratories across 10 ecosystemic domains.',
      l5_title: 'Level 5: Mathematics',
      l5_desc: 'Estrada communicability, Heider frustration Laplacian, Fiedler λ₂, Grassmann Gr(k,N) geometry, and Φ integration.',
      l6_title: 'Level 6: Reports',
      l6_desc: 'Autonomous expert forensic report engine, dyadic balances, and non-punitive individual dossiers.',
      l7_title: 'Level 7: Documentation',
      l7_desc: 'Canonical Scientific Manifesto v9.1, CERN Zenodo repositories, and Open Science specification.',
      btn_level_enter: 'Enter Level ➔',

      // Ethics & Vault Section
      ethics_badge: 'DEONTOLOGY BY DESIGN',
      ethics_title: 'Inviolable Non-Punitive Commitment',
      ethics_desc: 'NEXORD is strictly safeguarded by design exclusively for formative, preventive, and healthy group development. Its deployment for layoffs, pejorative screening, or psychological harm is strictly prohibited.',
      ethics_item1: '<strong>Privacy by Design:</strong> Strict matrix anonymization (positional matrix codes 1A1a…5B1a).',
      ethics_item2: '<strong>Exclusively Formative Use:</strong> Constructive feedback oriented toward comprehensive collective wellbeing.',
      ethics_item3: '<strong>Principal Investigator (PI) Accreditation:</strong> Explicit deontological pledge and institutional ethical custody.',

      vault_badge: 'CRYPTOGRAPHIC SECURITY',
      vault_title: 'Clélie Protocol & SHA3-512 Sealing',
      vault_desc: 'Every sociomatrix is protected via immutable cryptographic timestamping, invariant verification, and decentralized stewardship in the Sociometric Bank (BSOC).',

      // Institutional Stewardship & Zenodo Section
      cust_badge: 'OPEN SCIENCE & PERMANENT REPOSITORY',
      cust_title: 'International Stewardship at CERN Zenodo',
      cust_desc: 'The theoretical corpus, methodology, and technical annexes are deposited in perpetuity in CERN\'s official repository (OpenAIRE) under a Creative Commons CC BY 4.0 license.',
      cust_man_title: 'Central Scientific Manifesto',
      cust_man_desc: 'Foundational treatise on Computational Ordinal Sociometry (Canonical Edition v9.1, October 2026).',
      cust_sup_title: 'Supplementary Material & Annexes',
      cust_sup_desc: 'Responses to critiques, bilingual encyclopedic glossary, mathematical annex, and canonical tables.',
      cust_btn_man_es: '📄 Manifesto ES (PDF)',
      cust_btn_man_en: '📄 Manifesto EN (PDF)',
      cust_btn_sup: '📦 View on Zenodo (6 Docs) ↗',
      cust_btn_cite: '📜 Cite in BibTeX / APA / RIS',

      // CTA Banner
      cta_title: 'Ready to Explore the Physics of Groups?',
      cta_desc: 'Immerse yourself in the interactive 3D Moviola or access the complete methodological suite.',
      cta_btn_start: '🚀 Launch Level 1 (3D Moviola)',
      cta_btn_dial: '🧭 Explore Orbital Dial (9 Sectors)',

      // Footer
      footer_lead: 'Towards a Physics of the Group: Computational Ordinal Sociometry & VISORD Ecosystem.',
      footer_rights: '© 2026 Dr. José Manuel Cornejo Álvarez. All rights reserved under Creative Commons CC BY 4.0 License.',
      footer_col_nav: 'Quick Navigation',
      footer_col_science: 'Science & Docs',
      footer_col_legal: 'Ethics & Stewardship',
      footer_legal_deont: 'Deontological Code & GDPR',
      footer_legal_fair: 'FAIR Principles & Open Science',
      footer_legal_license: 'Open License CC BY 4.0'
    }
  };

  function setPromoLanguage(lang) {
    if (!PROMO_I18N[lang]) lang = 'es';
    try {
      localStorage.setItem('nexord_lang', lang);
    } catch (e) {}

    document.documentElement.lang = lang;
    const dict = PROMO_I18N[lang];

    // Page title & meta
    document.title = dict.page_title;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', dict.meta_desc);

    // Navbar
    const sub = document.querySelector('.brand-sub');
    if (sub) sub.textContent = dict.nav_brand_sub;

    const navWhy = document.querySelector('a[href="#dolor"]');
    if (navWhy) navWhy.textContent = dict.nav_why;
    const navShow = document.querySelector('a[href="#showroom"]');
    if (navShow) navShow.textContent = dict.nav_showroom;
    const navSol = document.querySelector('a[href="#soluciones"]');
    if (navSol) navSol.textContent = dict.nav_solutions;
    const navEth = document.querySelector('a[href="#etica"]');
    if (navEth) navEth.textContent = dict.nav_ethics;
    const navDial = document.querySelector('a[href="dial_orbital.html"]');
    if (navDial) navDial.textContent = dict.nav_dial;
    const navSci = document.querySelector('a[href="#boveda"]');
    if (navSci) navSci.textContent = dict.nav_science;
    const navCust = document.querySelector('a[href="#custodia"]');
    if (navCust) navCust.textContent = dict.nav_custody;
    const navCta = document.querySelector('.nav-cta');
    if (navCta) navCta.textContent = dict.nav_cta;

    // Dropdown items
    const dropItems = document.querySelectorAll('.dropdown-menu .dropdown-item');
    if (dropItems.length >= 11) {
      dropItems[0].textContent = dict.drop_l1;
      dropItems[1].textContent = dict.drop_l2;
      dropItems[2].textContent = dict.drop_l3;
      dropItems[3].textContent = dict.drop_l4;
      dropItems[4].textContent = dict.drop_l5;
      dropItems[5].textContent = dict.drop_l6;
      dropItems[6].textContent = dict.drop_l7;
      dropItems[7].textContent = dict.drop_framework;
      dropItems[8].textContent = dict.drop_deontology;
      dropItems[9].textContent = dict.drop_glossary;
      dropItems[10].textContent = dict.drop_dial;
    }

    // Hero
    const heroPill = document.querySelector('.hero-pill');
    if (heroPill) heroPill.innerHTML = '<span class="hero-pill-dot"></span>' + dict.hero_pill;
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) heroTitle.innerHTML = dict.hero_title;
    const heroSubtitle = document.querySelector('.hero-subtitle');
    if (heroSubtitle) heroSubtitle.textContent = dict.hero_subtitle;

    const heroBtn3d = document.querySelector('.hero-actions .btn-primary span');
    if (heroBtn3d) heroBtn3d.textContent = dict.hero_btn_3d;
    const heroBtnCust = document.querySelector('.hero-actions a[href="#custodia"] span');
    if (heroBtnCust) heroBtnCust.textContent = dict.hero_btn_custody;
    const heroBtnSol = document.querySelector('.hero-actions a[href="#soluciones"] span');
    if (heroBtnSol) heroBtnSol.textContent = dict.hero_btn_solutions;

    // Video HUD
    const vBadge = document.querySelector('.video-hero-badge span:last-child');
    if (vBadge) vBadge.textContent = dict.video_badge;
    const vMeta = document.querySelector('.video-hero-meta span');
    if (vMeta) vMeta.textContent = dict.video_meta;

    const bondPills = document.querySelectorAll('.video-bonds-decoder-hud .bond-pill');
    if (bondPills.length >= 3) {
      bondPills[0].innerHTML = '<span class="bond-dot dot-green"></span><strong class="bond-term">' + dict.bond_attraction_term + '</strong> ' + dict.bond_attraction_text;
      bondPills[1].innerHTML = '<span class="bond-dot dot-magenta"></span><strong class="bond-term">' + dict.bond_rejection_term + '</strong> ' + dict.bond_rejection_text;
      bondPills[2].innerHTML = '<span class="bond-dot dot-ostracism"></span><strong class="bond-term">' + dict.bond_ostracism_term + '</strong> ' + dict.bond_ostracism_text;
    }

    const vSubText = document.getElementById('hero-subtitles-text');
    if (vSubText && !vSubText.getAttribute('data-dynamic')) vSubText.textContent = dict.video_sub_initial;
    const vCtaPill = document.querySelector('.video-cta-pill span:first-child');
    if (vCtaPill) vCtaPill.textContent = dict.video_cta_pill;

    // Pain section
    const painBadge = document.querySelector('#dolor .section-badge');
    if (painBadge) painBadge.textContent = dict.pain_badge;
    const painTitle = document.querySelector('#dolor .section-title');
    if (painTitle) painTitle.textContent = dict.pain_title;
    const painDesc = document.querySelector('#dolor .section-subtitle');
    if (painDesc) painDesc.textContent = dict.pain_desc;

    // Showroom section
    const showBadge = document.querySelector('#showroom .section-badge');
    if (showBadge) showBadge.textContent = dict.show_badge;
    const showTitle = document.querySelector('#showroom .section-title');
    if (showTitle) showTitle.textContent = dict.show_title;
    const showDesc = document.querySelector('#showroom .section-subtitle');
    if (showDesc) showDesc.textContent = dict.show_desc;

    // Soluciones (7 Niveles)
    const solBadge = document.querySelector('#soluciones .section-badge');
    if (solBadge) solBadge.textContent = dict.sol_badge;
    const solTitle = document.querySelector('#soluciones .section-title');
    if (solTitle) solTitle.textContent = dict.sol_title;
    const solDesc = document.querySelector('#soluciones .section-subtitle');
    if (solDesc) solDesc.textContent = dict.sol_desc;

    // Ética & Bóveda
    const ethBadge = document.querySelector('#etica .section-badge');
    if (ethBadge) ethBadge.textContent = dict.ethics_badge;
    const ethTitle = document.querySelector('#etica .section-title');
    if (ethTitle) ethTitle.textContent = dict.ethics_title;
    const ethDesc = document.querySelector('#etica .section-subtitle');
    if (ethDesc) ethDesc.textContent = dict.ethics_desc;

    const vltBadge = document.querySelector('#boveda .section-badge');
    if (vltBadge) vltBadge.textContent = dict.vault_badge;
    const vltTitle = document.querySelector('#boveda .section-title');
    if (vltTitle) vltTitle.textContent = dict.vault_title;
    const vltDesc = document.querySelector('#boveda .section-subtitle');
    if (vltDesc) vltDesc.textContent = dict.vault_desc;

    // Custodia
    const custBadge = document.querySelector('#custodia .section-badge');
    if (custBadge) custBadge.textContent = dict.cust_badge;
    const custTitle = document.querySelector('#custodia .section-title');
    if (custTitle) custTitle.textContent = dict.cust_title;
    const custDesc = document.querySelector('#custodia .section-subtitle');
    if (custDesc) custDesc.textContent = dict.cust_desc;

    const custBtnManEs = document.querySelector('a[href*="oct_2026_ES.pdf"]');
    if (custBtnManEs) custBtnManEs.innerHTML = '<span>📄</span> ' + dict.cust_btn_man_es;
    const custBtnManEn = document.querySelector('a[href*="oct_2026_EN.pdf"]');
    if (custBtnManEn) custBtnManEn.innerHTML = '<span>📄</span> ' + dict.cust_btn_man_en;
    const custBtnSup = document.querySelector('a[href*="10.5281/zenodo.23329641"]');
    if (custBtnSup) custBtnSup.innerHTML = '<span>📦</span> ' + dict.cust_btn_sup;

    // CTA Banner
    const ctaTitle = document.querySelector('.cta-banner h2');
    if (ctaTitle) ctaTitle.textContent = dict.cta_title;
    const ctaDesc = document.querySelector('.cta-banner p');
    if (ctaDesc) ctaDesc.textContent = dict.cta_desc;
    const ctaBtn1 = document.querySelector('.cta-banner a[href*="nivel1"]');
    if (ctaBtn1) ctaBtn1.textContent = dict.cta_btn_start;
    const ctaBtn2 = document.querySelector('.cta-banner a[href*="dial_orbital"]');
    if (ctaBtn2) ctaBtn2.textContent = dict.cta_btn_dial;

    // Footer
    const footRights = document.querySelector('.footer-bottom p');
    if (footRights) footRights.textContent = dict.footer_rights;

    // Actualizar botones de selector
    const btnEs = document.getElementById('btn-promo-lang-es');
    const btnEn = document.getElementById('btn-promo-lang-en');
    if (btnEs) {
      btnEs.style.color = (lang === 'es') ? 'var(--neon-green)' : '#94A3B8';
      btnEs.style.fontWeight = (lang === 'es') ? '800' : '700';
    }
    if (btnEn) {
      btnEn.style.color = (lang === 'en') ? 'var(--neon-green)' : '#94A3B8';
      btnEn.style.fontWeight = (lang === 'en') ? '800' : '700';
    }

    // Notificar al ecosistema
    try {
      window.dispatchEvent(new CustomEvent('nexordLangChanged', { detail: { lang: lang } }));
    } catch (e) {}
  }

  // Exportar globalmente
  window.setPromoLanguage = setPromoLanguage;
  window.setLanguage = setPromoLanguage; // Alias para compatibilidad

  // Detección inicial
  document.addEventListener('DOMContentLoaded', function () {
    let initialLang = 'es';
    try {
      const p = new URLSearchParams(window.location.search);
      const urlLang = p.get('lang');
      if (urlLang && PROMO_I18N[urlLang]) {
        initialLang = urlLang;
      } else {
        const saved = localStorage.getItem('nexord_lang');
        if (saved && PROMO_I18N[saved]) {
          initialLang = saved;
        } else {
          const browserLang = (navigator.language || '').toLowerCase().split('-')[0];
          if (browserLang === 'en') initialLang = 'en';
        }
      }
    } catch (e) {}
    setPromoLanguage(initialLang);
  });

})();
