/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE DEONTOLOGÍA & RGPD
 * =============================================================================
 * Soporte bilingüe completo (Español oficial / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const DEONTO_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'Código Deontológico, Privacidad por Diseño (RGPD) & Aviso Legal · NEXORD',
      brand_sub: 'DEONTOLOGÍA & RGPD',
      nav_portal: '🏛️ Portal Institucional',
      nav_dial: '🧭 Dial Orbital',
      nav_custody: '🏛️ Custodia',
      nav_visord: '🎮 VISORD 3D',

      hero_pill: '🛡️ MARCO ÉTICO, DEONTOLÓGICO Y REGULATORIO OFICIAL',
      hero_title: 'Código Deontológico, Privacidad por Diseño<br><span style="background: linear-gradient(135deg, #38BDF8, #00FF87); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">& Cumplimiento RGPD</span>',
      hero_subtitle: 'Garantías del Investigador Principal (Regla 21), arquitectura de protección de datos personales (<em>Privacy by Design</em>) y condiciones de licencia abierta para la adopción institucional de NEXORD.',

      tab_deonto: '🛡️ 1. Código Deontológico PI (Regla 21)',
      tab_rgpd: '🔒 2. Privacidad por Diseño & RGPD',
      tab_legal: '📜 3. Aviso Legal & Licencia CC-BY-4.0',

      // Pestaña 1
      p1_title: 'Canon Deontológico del Investigador Principal (Regla 21)',
      p1_highlight_title: 'Declaración Oficial Homologada (Regla Oficial 21 de NEXORD)',
      p1_highlight_text: '«En su aplicación a estudios de campo con personas reales, NEXORD garantiza un <strong>uso exclusivamente formativo, no punitivo</strong>, de los datos. Esta exigencia salvaguarda la <strong>privacidad por diseño (<em>Privacy by Design</em>)</strong> y exige la acreditación profesional e institucional así como el compromiso explícito del Investigador Principal (IP) conforme a los principios de la Ciencia Abierta, de <strong>no dañar jamás con sus informes la autoestima personal ni la reputación social de los participantes</strong>, dando por características intrínsecas de la personalidad individual lo que son fenómenos termodinámicos estrictamente grupales.»',
      p1_lead: 'El ecosistema NEXORD no es una herramienta de clasificación penal, selección punitiva o etiquetado psiquiátrico de sujetos. Es un sistema físico-matemático orientado a comprender la arquitectura de tensiones y equilibrios de un colectivo. Toda entidad (colegio, instituto, empresa, hospital o universidad) que implemente la plataforma suscribe formalmente los siguientes cuatro principios directores:',
      
      p1_box1_title: '⚖️ 1. Finalidad Exclusivamente Formativa',
      p1_box1_text: 'Los resultados diagnósticos tienen por objeto optimizar el clima vincular, resolver el ostracismo latente y enriquecer la convivencia. Queda terminantemente proscrito emplear la sociomatriz para expedientes sancionadores, expulsiones, degradaciones laborales o cualquier forma de castigo individual.',
      
      p1_box2_title: '🌐 2. Atribución Factual Grupal',
      p1_box2_text: 'Toda tensión, aislamiento o fricción detectada es una propiedad emergente del <em>campo gravitatorio relacional</em> del grupo, nunca un déficit moral, cognitivo o psicológico intrínseco del individuo. Ningún informe debe catalogar a un sujeto como "problemático", sino a la red como "polarizada" o "congelada".',
      
      p1_box3_title: '❤️ 3. Protección de la Autoestima y Reputación',
      p1_box3_text: 'El retorno de información a los participantes (alumnos, pacientes, trabajadores) se realiza mediante dinámicas constructivas y agregadas que empoderan al grupo, evitando deliberadamente exponer a personas concretas a la vergüenza, el rechazo explícito o la estigmatización social.',
      
      p1_box4_title: '🔬 4. Principios de Ciencia Abierta (<em>Open Science</em>)',
      p1_box4_text: 'NEXORD promueve la investigación científica abierta, libre de algoritmos de caja negra propietaria. Los comités de ética pueden auditar íntegramente las matrices SMIb, las fórmulas exponenciales de ponderación W(k) = 2^{1-k} y las proyecciones en variedades de Grassmann Gr(k, N).',

      // Pestaña 2
      p2_title: 'Arquitectura de Privacidad por Diseño (<em>Privacy by Design</em>) & RGPD',
      p2_lead: 'NEXORD fue concebido desde sus cimientos matemáticos bajo el principio de <strong>minimización radical de datos</strong> conforme al Reglamento General de Protección de Datos (RGPD UE 2016/679) y la Ley Orgánica 3/2018 (LOPDGDD).',
      
      p2_box1_title: '🔑 Anonimización Criptográfica Q.GID (T1-T9)',
      p2_box1_text: 'Los nombres civiles de los participantes se disocian irreversiblemente antes del procesamiento algebraico mediante el protocolo Q.GID. En el sistema solo viajan códigos matriciales oficiales (ej. <code>1A1a</code>, <code>2A1a</code>... para Grupo A; <code>1B1a</code>... para Grupo B). Ningún identificador personal civil reside en los modelos 3D.',
      
      p2_box2_title: '⚡ Computación en el Cliente (Zero Cloud Leakage)',
      p2_box2_text: 'A diferencia de las plataformas SaaS tradicionales que recopilan sociogramas en servidores centrales, VISORD ejecuta la ingestión matricial, la cinemática de fluidos y los cálculos espectrales localmente en la memoria del navegador (<em>Client-Side Edge Computing</em>). Ninguna matriz nominativa se almacena en bases de datos remotas.',
      
      p2_box3_title: '⏱️ Ciclo de Vida TTL y Purga Forense 0x00',
      p2_box3_text: 'Los conjuntos de datos procesados en entornos controlados cuentan con expiración por tiempo de vida (<em>Time-To-Live</em>). Cuando concluye el periodo de intervención pactado, el sistema ejecuta una sobreescritura binaria con ceros (<code>0x00</code>) garantizando la imposibilidad de recuperación forense.',
      
      p2_box4_title: '📑 Derechos ARCO y Delegado de Protección de Datos',
      p2_box4_text: 'Cualquier participante o tutor legal puede ejercer en cualquier momento sus derechos de Acceso, Rectificación, Supresión, Oposición y Limitación del tratamiento comunicándolo directamente a la dirección del Investigador Principal o al Delegado de Protección de Datos institucional: <code>info@nex-ord.org</code>.',

      // Pestaña 3
      p3_title: 'Aviso Legal, Propiedad Intelectual y Licencia Internacional',
      p3_lead: 'La marca maestra <strong>VISORD</strong> y la plataforma <strong>NEXORD</strong> constituyen un ecosistema de investigación y diagnóstico científico impulsado desde el ámbito universitario:',
      
      p3_attr_title: '🏛️ Atribución Académica e Investigador Principal',
      p3_attr_text: '<strong>Investigador Principal (IP):</strong> Dr. José Manuel Cornejo Álvarez.<br><strong>Filiación Institucional:</strong> NEXORD Research Initiative · Investigación independiente.<br><strong>Depósito Científico Oficial:</strong> CERN Zenodo · Edición Oficial Unificada (Manifiesto y Suplemento): <a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color: var(--neon-green); text-decoration: underline; font-weight:700;">DOI 10.5281/zenodo.23329641</a>.',
      
      p3_lic_title: 'Régimen de Protección: Doble Vía & Licencia CC-BY-4.0',
      p3_lic_text: 'El ecosistema NEXORD / VISORD opera bajo un régimen formal articulado en dos esferas estrictamente diferenciadas y complementarias:<br><br>' +
        '• <strong>ESFERA ABIERTA (CC-BY-4.0):</strong> Manifiesto Científico, canon teórico, métricas formalizadas, dashboards, demos VISORD y documentación. Ciencia abierta verificable y citable por cualquiera bajo licencia Creative Commons Atribución 4.0 Internacional.<br>' +
        '• <strong>ESFERA CUSTODIADA (SIN DISTRIBUCIÓN LIBRE):</strong> Motores Python de cálculo nativo, suite operativa, corpus BSOC con datos y herramientas de credenciales. Acceso exclusivo para equipos de investigación acreditados, con régimen de revocación.<br>' +
        '• <strong>Auditorías («Auditable no significa abierto»):</strong> El código operativo es auditable por comités o terceros acreditados bajo acuerdo de confidencialidad (NDA); los informes de auditoría son públicos, el código no se publica.',
      
      p3_custody_title: '🤝 Custodia Institucional y Adopción Académica',
      p3_custody_text: 'El equipo promotor de NEXORD mantiene una convocatoria abierta para que universidades, centros públicos de I+D o fundaciones científicas asuman la <strong>custodia institucional formal del software</strong>, garantizando su gobernanza democrática, el mantenimiento del repositorio público y la gestión de accesos sin ánimo de lucro punitivo. Consulte la sección <a href="index_promocional.html#custodia" style="color: var(--neon-cyan); text-decoration: underline;">Custodia Institucional</a> o descargue el <a href="dossier_adopcion.html" style="color: var(--neon-green); text-decoration: underline; font-weight: 700;">Marco Oficial de Custodia (PDF/HTML)</a> para remitir una propuesta formal.',

      // Footer
      ft_portal: 'Portal Institucional',
      ft_dial: 'Dial Orbital',
      ft_dossier: 'Marco de Custodia (PDF)',
      ft_custody: 'Custodia Institucional',
      ft_engine: 'VISORD 3D Engine',
      ft_glossary: 'Glosario Oficial',
      ft_pdf: 'Descargar Manifiesto PDF'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'Deontological Code, Privacy by Design (GDPR) & Legal Notice · NEXORD',
      brand_sub: 'DEONTOLOGY & GDPR',
      nav_portal: '🏛️ Institutional Portal',
      nav_dial: '🧭 Orbital Dial',
      nav_custody: '🏛️ Stewardship',
      nav_visord: '🎮 VISORD 3D',

      hero_pill: '🛡️ OFFICIAL ETHICAL, DEONTOLOGICAL & REGULATORY FRAMEWORK',
      hero_title: 'Deontological Code, Privacy by Design<br><span style="background: linear-gradient(135deg, #38BDF8, #00FF87); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">& GDPR Compliance</span>',
      hero_subtitle: 'Guarantees of the Principal Investigator (Rule 21), personal data protection architecture (<em>Privacy by Design</em>), and open license terms for institutional adoption of NEXORD.',

      tab_deonto: '🛡️ 1. PI Deontological Code (Rule 21)',
      tab_rgpd: '🔒 2. Privacy by Design & GDPR',
      tab_legal: '📜 3. Legal Notice & CC-BY-4.0 License',

      // Tab 1
      p1_title: 'Deontological Canon of the Principal Investigator (Rule 21)',
      p1_highlight_title: 'Official Homologated Declaration (NEXORD Official Rule 21)',
      p1_highlight_text: '«In its application to field studies with real human participants, NEXORD guarantees an <strong>exclusively formative, non-punitive use</strong> of data. This mandate safeguards <strong>privacy by design (<em>Privacy by Design</em>)</strong> and requires institutional and professional accreditation as well as the explicit commitment of the Principal Investigator (PI) under Open Science principles, to <strong>never damage personal self-esteem or social reputation of participants with diagnostic reports</strong>, attributing to intrinsic traits of individual personality what are strictly group-level thermodynamic phenomena.»',
      p1_lead: 'The NEXORD ecosystem is not an instrument for punitive screening, sanctioning, or psychiatric labeling of individuals. It is a physical-mathematical system designed to decipher the architecture of tensions and equilibria within human collectives. Any entity (school, institute, corporation, hospital, or university) deploying the platform formally endorses the following four governing principles:',
      
      p1_box1_title: '⚖️ 1. Exclusively Formative Purpose',
      p1_box1_text: 'Diagnostic outcomes aim exclusively to improve relational climate, resolve hidden ostracism, and enrich coexistence. Using sociometric data for disciplinary files, dismissals, demotions, or any form of individual punishment is strictly prohibited.',
      
      p1_box2_title: '🌐 2. Group Factual Attribution',
      p1_box2_text: 'Every tension, isolation, or friction identified is an emergent property of the group\'s <em>relational gravitational field</em>, never an intrinsic moral, cognitive, or psychological deficiency of the individual. No report may classify a subject as "problematic", but rather characterize the network as "polarized" or "frozen".',
      
      p1_box3_title: '❤️ 3. Protection of Self-Esteem and Reputation',
      p1_box3_text: 'Feedback to participants (students, patients, team members) is delivered through constructive and aggregated dynamics that empower the group, deliberately avoiding exposing specific individuals to shame, explicit rejection, or social stigmatization.',
      
      p1_box4_title: '🔬 4. Open Science Principles (<em>Open Science</em>)',
      p1_box4_text: 'NEXORD fosters open scientific research, free from proprietary black-box algorithms. Ethics committees can fully audit the SMIb matrices, exponential weighting formulations W(k) = 2^{1-k}, and Grassmann manifold projections Gr(k, N).',

      // Tab 2
      p2_title: 'Privacy by Design Architecture (<em>Privacy by Design</em>) & GDPR Compliance',
      p2_lead: 'NEXORD was conceived from its mathematical foundations under the principle of <strong>radical data minimization</strong> in full compliance with the European General Data Protection Regulation (GDPR EU 2016/679) and Spanish Organic Law 3/2018 (LOPDGDD).',
      
      p2_box1_title: '🔑 Q.GID Cryptographic Pseudonymization (T1-T9)',
      p2_box1_text: 'Civil names of participants are irreversibly dissociated prior to algebraic processing using the Q.GID protocol. Only official matrix codes travel through the pipeline (e.g. <code>1A1a</code>, <code>2A1a</code>... for Group A; <code>1B1a</code>... for Group B). No civilian personal identifiers reside inside the 3D models.',
      
      p2_box2_title: '⚡ Client-Side Edge Computing (Zero Cloud Leakage)',
      p2_box2_text: 'Unlike traditional SaaS platforms that collect sociograms on central servers, VISORD executes matrix ingestion, fluid kinematics, and spectral calculations locally within the browser\'s memory (<em>Client-Side Edge Computing</em>). No nominative matrix is ever stored in remote databases.',
      
      p2_box3_title: '⏱️ TTL Lifecycle & Forensic 0x00 Purge',
      p2_box3_text: 'Datasets processed in controlled environments include strict Time-To-Live (TTL) expiration. Upon conclusion of the agreed intervention cycle, the system executes a binary overwrite with zeros (<code>0x00</code>), ensuring forensic unrecoverability.',
      
      p2_box4_title: '📑 ARCO Rights & Data Protection Officer',
      p2_box4_text: 'Any participant or legal guardian may at any time exercise their rights of Access, Rectification, Erasure, Objection, and Restriction of processing by contacting the Principal Investigator or institutional Data Protection Officer at: <code>info@nex-ord.org</code>.',

      // Tab 3
      p3_title: 'Legal Notice, Intellectual Property & International License',
      p3_lead: 'The master brand <strong>VISORD</strong> and the platform <strong>NEXORD</strong> constitute a scientific research and diagnostic ecosystem originated in the academic sphere:',
      
      p3_attr_title: '🏛️ Academic Attribution & Principal Investigator',
      p3_attr_text: '<strong>Principal Investigator (PI):</strong> Dr. José Manuel Cornejo Álvarez.<br><strong>Institutional Affiliation:</strong> NEXORD Research Initiative · Independent Research.<br><strong>Official Scientific Deposit:</strong> CERN Zenodo · Unified Official Edition (Manifesto & Supplement): <a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color: var(--neon-green); text-decoration: underline; font-weight:700;">DOI 10.5281/zenodo.23329641</a>.',
      
      p3_lic_title: 'Double-Track Protection Regime & CC-BY-4.0 License',
      p3_lic_text: 'The NEXORD / VISORD ecosystem operates under a formal regime structured into two strictly differentiated, complementary spheres:<br><br>' +
        '• <strong>OPEN SPHERE (CC-BY-4.0):</strong> Scientific Manifesto, theoretical canon, formalized metrics, dashboards, VISORD demos, and public documentation. Open science fully verifiable and citable by anyone under Creative Commons Attribution 4.0 International.<br>' +
        '• <strong>CUSTODIED SPHERE (NO FREE DISTRIBUTION):</strong> Native Python calculation engines, operational suite, BSOC empirical corpus with field data, and credential management tools. Exclusive access for accredited research teams, subject to revocation.<br>' +
        '• <strong>Audits ("Auditable does not mean open"):</strong> Operational code is auditable by ethics committees or accredited third parties under strict non-disclosure agreement (NDA); audit reports are public, but operational code is not published or openly distributed.',
      
      p3_custody_title: '🤝 Institutional Custody & Academic Stewardship',
      p3_custody_text: 'The NEXORD promoter team maintains an open call for universities, public R&D centers, or scientific foundations to assume <strong>formal institutional custody of the software</strong>, ensuring democratic governance, public repository maintenance, and non-punitive access. Visit the <a href="index_promocional.html#custodia" style="color: var(--neon-cyan); text-decoration: underline;">Institutional Custody</a> section or download the <a href="dossier_adopcion.html" style="color: var(--neon-green); text-decoration: underline; font-weight: 700;">Official Custody Framework (PDF/HTML)</a> to submit a formal proposal.',

      // Footer
      ft_portal: 'Institutional Portal',
      ft_dial: 'Orbital Dial',
      ft_dossier: 'Custody Framework (PDF)',
      ft_custody: 'Institutional Custody',
      ft_engine: 'VISORD 3D Engine',
      ft_glossary: 'Official Glossary',
      ft_pdf: 'Download Manifesto PDF'
    }
  };

  function applyLanguage(lang) {
    const d = DEONTO_I18N[lang] || DEONTO_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Actualizar botones de selector
    const btnEs = document.getElementById('btn-deonto-lang-es');
    const btnEn = document.getElementById('btn-deonto-lang-en');
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

    // Título y metadatos
    document.title = d.page_title;

    // Header
    const badge = document.querySelector('.brand-badge');
    if (badge) badge.textContent = d.brand_sub;

    const navLinks = document.querySelectorAll('.header-nav .hdr-btn');
    if (navLinks.length >= 4) {
      navLinks[0].querySelector('span:last-child').textContent = d.nav_portal.replace('🏛️ ', '');
      navLinks[1].querySelector('span:last-child').textContent = d.nav_dial.replace('🧭 ', '');
      navLinks[2].querySelector('span:last-child').textContent = d.nav_custody.replace('🏛️ ', '');
      navLinks[3].querySelector('span:last-child').textContent = d.nav_visord.replace('🎮 ', '');
    }

    // Hero
    const pill = document.querySelector('.legal-hero-pill span');
    if (pill) pill.textContent = d.hero_pill;

    const heroTitle = document.querySelector('.legal-hero-title');
    if (heroTitle) heroTitle.innerHTML = d.hero_title;

    const heroSub = document.querySelector('.legal-hero-subtitle');
    if (heroSub) heroSub.innerHTML = d.hero_subtitle;

    // Pestañas
    const tabDeonto = document.getElementById('tab-btn-deonto');
    if (tabDeonto) tabDeonto.querySelector('span:last-child').textContent = d.tab_deonto.replace('🛡️ ', '');

    const tabRgpd = document.getElementById('tab-btn-rgpd');
    if (tabRgpd) tabRgpd.querySelector('span:last-child').textContent = d.tab_rgpd.replace('🔒 ', '');

    const tabLegal = document.getElementById('tab-btn-legal');
    if (tabLegal) tabLegal.querySelector('span:last-child').textContent = d.tab_legal.replace('📜 ', '');

    // Pane 1
    const p1 = document.getElementById('pane-deonto');
    if (p1) {
      const title = p1.querySelector('.card-title span:last-child');
      if (title) title.textContent = d.p1_title;
      const hlTitle = p1.querySelector('.legal-highlight-box h4');
      if (hlTitle) hlTitle.textContent = d.p1_highlight_title;
      const hlText = p1.querySelector('.legal-highlight-box p');
      if (hlText) hlText.innerHTML = d.p1_highlight_text;
      const lead = p1.querySelector('.legal-p');
      if (lead) lead.innerHTML = d.p1_lead;

      const boxes = p1.querySelectorAll('.legal-box');
      if (boxes.length >= 4) {
        boxes[0].querySelector('h5').innerHTML = '<span>⚖️</span> ' + d.p1_box1_title.replace('⚖️ ', '');
        boxes[0].querySelector('p').innerHTML = d.p1_box1_text;

        boxes[1].querySelector('h5').innerHTML = '<span>🌐</span> ' + d.p1_box2_title.replace('🌐 ', '');
        boxes[1].querySelector('p').innerHTML = d.p1_box2_text;

        boxes[2].querySelector('h5').innerHTML = '<span>❤️</span> ' + d.p1_box3_title.replace('❤️ ', '');
        boxes[2].querySelector('p').innerHTML = d.p1_box3_text;

        boxes[3].querySelector('h5').innerHTML = '<span>🔬</span> ' + d.p1_box4_title.replace('🔬 ', '');
        boxes[3].querySelector('p').innerHTML = d.p1_box4_text;
      }
    }

    // Pane 2
    const p2 = document.getElementById('pane-rgpd');
    if (p2) {
      const title = p2.querySelector('.card-title span:last-child');
      if (title) title.innerHTML = d.p2_title;
      const lead = p2.querySelector('.legal-p');
      if (lead) lead.innerHTML = d.p2_lead;

      const boxes = p2.querySelectorAll('.legal-box');
      if (boxes.length >= 4) {
        boxes[0].querySelector('h5').innerHTML = '<span>🔑</span> ' + d.p2_box1_title.replace('🔑 ', '');
        boxes[0].querySelector('p').innerHTML = d.p2_box1_text;

        boxes[1].querySelector('h5').innerHTML = '<span>⚡</span> ' + d.p2_box2_title.replace('⚡ ', '');
        boxes[1].querySelector('p').innerHTML = d.p2_box2_text;

        boxes[2].querySelector('h5').innerHTML = '<span>⏱️</span> ' + d.p2_box3_title.replace('⏱️ ', '');
        boxes[2].querySelector('p').innerHTML = d.p2_box3_text;

        boxes[3].querySelector('h5').innerHTML = '<span>📑</span> ' + d.p2_box4_title.replace('📑 ', '');
        boxes[3].querySelector('p').innerHTML = d.p2_box4_text;
      }
    }

    // Pane 3
    const p3 = document.getElementById('pane-legal');
    if (p3) {
      const title = p3.querySelector('.card-title span:last-child');
      if (title) title.innerHTML = d.p3_title;
      const lead = p3.querySelector('.legal-p');
      if (lead) lead.innerHTML = d.p3_lead;

      const boxes = p3.querySelectorAll('.legal-box');
      if (boxes.length >= 2) {
        boxes[0].querySelector('h5').innerHTML = '<span>🏛️</span> ' + d.p3_attr_title.replace('🏛️ ', '');
        boxes[0].querySelector('p').innerHTML = d.p3_attr_text;

        boxes[1].querySelector('h5').innerHTML = '<span>🤝</span> ' + d.p3_custody_title.replace('🤝 ', '');
        boxes[1].querySelector('p').innerHTML = d.p3_custody_text;
      }
      const hlTitle = p3.querySelector('.legal-highlight-box h4');
      if (hlTitle) hlTitle.textContent = d.p3_lic_title;
      const hlText = p3.querySelector('.legal-highlight-box p');
      if (hlText) hlText.innerHTML = d.p3_lic_text;
    }

    // Footer links
    const ftLinks = document.querySelectorAll('.footer-links-row a');
    if (ftLinks.length >= 7) {
      ftLinks[0].textContent = d.ft_portal;
      ftLinks[1].textContent = d.ft_dial;
      ftLinks[2].textContent = d.ft_dossier;
      ftLinks[3].textContent = d.ft_custody;
      ftLinks[4].textContent = d.ft_engine;
      ftLinks[5].textContent = d.ft_glossary;
      ftLinks[6].textContent = d.ft_pdf;
    }
  }

  window.setDeontoLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
