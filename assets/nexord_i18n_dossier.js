/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DEL DOSSIER DE ADOPCIÓN
 * =============================================================================
 * Soporte bilingüe completo (Español canónico / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
 * =============================================================================
 */

(function () {
  'use strict';

  const DOSSIER_I18N = {
    es: {
      flag: '🇪🇸',
      code: 'ES',
      page_title: 'Dossier Ejecutivo: Oferta de Legado Tecnológico y Custodia Científica · NEXORD',
      brand_sub: 'DOSSIER INSTITUCIONAL',
      nav_portal: '🏛️ Portal Institucional',
      nav_dial: '🧭 Dial Orbital',
      nav_deonto: '🛡️ Deontología',
      nav_print: '🖨️ Imprimir / PDF',

      // Hero
      meta_badge: '🏛️ OFERTA PÚBLICA DE CUSTODIA INSTITUCIONAL',
      hero_title: 'Marco Canónico de Legado Tecnológico &amp; Custodia Científica',
      hero_subtitle: 'Bases y condiciones de transferencia del ecosistema de Sociometría Ordinal Computacional y Gemelos Digitales 3D/4D (NEXORD / VISORD Engine v8.3) para <strong>Universidades Públicas, Centros de I+D y Consorcios Científicos</strong>.',
      hero_principle: '<strong>PRINCIPIO FUNDACIONAL:</strong> Cesión de custodia responsable y fiduciaria académica, no enajenación a ciegas. El software se transfiere para su custodia, mantenimiento y uso docente/investigador bajo salvaguarda del mandato deontológico estricto (Regla 21).',

      // Sección 1
      s1_title: 'El Activo Científico Transferido (La Dote Tecnológica)',
      s1_lead: 'El promotor cede formalmente los derechos de custodia, gobernanza académica y operación del ecosistema completo de investigación, desarrollado a lo largo de más de dos décadas de investigación científica independiente:',
      s1_b1_title: '🐍 Motores de Cálculo Nativo en Python',
      s1_b1_desc: 'Pipelines automatizados de ingestión, transcripción de ordenaciones *Breve → Moreno*, matrices de 4 posiciones SMIb ($DA, RC, pDA, pRC$), descomposición factorial Benzécri ($\chi^2$), densidades absolutas (BDR) y saldos relativos continuos ponderados físicamente (SDR, $W(k)=2^{1-k}$).',
      s1_b2_title: '🌐 Ecosistema de Gemelos Digitales 3D/4D',
      s1_b2_desc: 'Laboratorios interactivos WebGL Three.js con simulación cinemática continua: <code>VISORD_demo</code> (transiciones de fase y gravedad de redes), <code>VISORD_acuario</code> (reactor de hidrostática relacional y detección de ostracismo sutil) y <code>VISORD_dialectico</code> (anfiteatro de dilemas dialécticos y Moviola Bales IPA).',
      s1_b3_title: '📐 Álgebra Tensorial y Espectral',
      s1_b3_desc: 'Módulos computacionales para proyección en variedades de Grassmann $\\operatorname{Gr}(k, N)$, cálculo del gap espectral y conectividad algebraica de Fiedler ($\\lambda_2$), frustración estructural de Heider y operadores de Estrada ($EE$).',
      s1_b4_title: '📚 Banco Canónico de Datos BSOC &amp; Zenodo',
      s1_b4_desc: 'Corpus empírico homologado de sociogramas de campo reales, matrices simuladas Monte Carlo y series culturales. Registro permanente en CERN Zenodo: Manifiesto Científico Central (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color:var(--neon-cyan);">DOI: 10.5281/zenodo.23329641</a>) y Material Suplementario con 6 Anexos Técnicos (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color:#F59E0B;">DOI: 10.5281/zenodo.23329641</a>) con metadatos Google Académico listos.',

      // Sección 2
      s2_title: 'Objeto de la Oferta: Custodia Responsable sin Royalties',
      s2_lead: 'La cesión no exige contraprestación económica por derechos de propiedad intelectual. La <strong>Institución Depositaria / Universidad Custodia</strong> asume la preservación del legado bajo cuatro compromisos institucionales estructurados:',
      s2_th1: 'Eje de Custodia',
      s2_th2: 'Compromiso Asumido por la Institución Depositaria',
      s2_r1_h: '1. Alojamiento e Infraestructura',
      s2_r1_t: 'Proveer servidores institucionales seguros o alojamiento en nube homologada con copias de seguridad continuas y garantía de soberanía de datos europea (RGPD).',
      s2_r2_h: '2. Mantenimiento Tecnológico',
      s2_r2_t: 'Supervisar la compatibilidad periódica de dependencias de renderizado (Three.js/WebGL), entornos de ejecución en Python y estándares W3C.',
      s2_r3_h: '3. Gestión de Credenciales y Deontología',
      s2_r3_t: 'Habilitar accesos a Investigadores Principales acreditados, comités éticos y proyectos docentes, velando por el cumplimiento de la Regla 21.',
      s2_r4_h: '4. Salvaguarda de Ciencia Abierta',
      s2_r4_t: 'Preservar la disponibilidad del repositorio institucional bajo licencia abierta CC-BY-4.0 para usos de investigación y docencia.',
      s2_r5_h: '5. Mandato de Universalidad Cosmopolita',
      s2_r5_t: 'Preservar la vocación del software como patrimonio abierto de la humanidad (UNESCO Open Science), manteniendo activos y homologados el Español e Inglés, con arquitectura preparada para futuras localizaciones.',

      // Sección 3
      s3_title: 'Plan de Mantenimiento y Asesoría Voluntaria del Autor',
      s3_lead: 'Para asegurar una transición tecnológica impecable y descargar al personal de la Fundación de incertidumbres matemáticas o metodológicas, el autor formaliza una dote de mentoría científica activa:',
      s3_card_title: '🎓 Compromiso de Mentoría Honoraria: 3 Años (Prorrogables a 5)',
      s3_card_intro: 'El <strong>Dr. José Manuel Cornejo Álvarez</strong> se ofrece a ejercer como <strong>Asesor Metodológico y Tecnológico Voluntario (ad honorem)</strong> durante un periodo de 3 a 5 años, asumiendo:',
      s3_li1: 'Transferencia presencial o telemática de la arquitectura matemática a los investigadores o técnicos que designe la entidad depositaria.',
      s3_li2: 'Supervisión de calidad en la calibración de núcleos KDE, densidades BDR/SDR y adaptaciones a nuevas tesis doctorales.',
      s3_li3: 'Resolución de dudas sobre el pipeline de simulación cinemática y generación de informes forenses.',

      // Sección 4
      s4_title: 'Cláusula Inviolable de Reversión Ética (Regla 21 &amp; Privacidad)',
      s4_lead: 'La cesión no constituye una renuncia a ciegas. El depósito queda formalmente sujeto a una <strong>condición resolutoria expresa de reversión automática</strong> para blindar el destino ético del proyecto:',
      s4_causes_title: '⚖️ Causales de Reversión Automática',
      s4_c1: '<strong>Uso Punitivo de los Datos (Regla 21):</strong> Empleo de las sociomatrices para sanciones, despidos, señalamientos o daño a la autoestima personal.',
      s4_c2: '<strong>Violación de la Privacidad por Diseño:</strong> Eliminación de la anonimización Q.GID o filtrado de nombres civiles de participantes.',
      s4_c3: '<strong>Privatización Restrictiva:</strong> Conversión del software a código cerrado o imposición de muros de pago contrarios a CC-BY-4.0.',
      s4_c4: '<strong>Secuestro Territorial o Bloqueo a la Universalidad:</strong> Impedir arbitrariamente la libre traducción, replicación federada o acceso científico internacional en los grandes troncos lingüísticos mundiales bajo el marco UNESCO de Ciencia Abierta.',
      s4_c5: '<strong>Abandono Prolongado:</strong> Inoperatividad del sistema por más de doce (12) meses consecutivos sin subsanación.',
      s4_effects_title: '🛡️ Efectos de la Reversión y Fideicomiso',
      s4_effects_text: 'Ante el incumplimiento acreditado de cualquiera de las causales éticas, la titularidad, repositorios y administración del ecosistema <strong>revierten de inmediato al autor</strong>. En caso de fallecimiento o incapacidad sobrevenida, se transfieren de pleno derecho al <strong>Guardián Sustituto</strong> designado en el protocolo de sucesión.',

      // Sección 5
      s5_title: 'Protocolo de Sucesión Abierta (Guardián Sustituto)',
      s5_lead: 'Para garantizar la preservación incondicional de este legado y evitar que el ecosistema quede huérfano, inactivo o privatizado, el protocolo canónico de custodia establece un orden estructurado de prelación institucional para su depósito y salvaguarda continua:',
      s5_th1: 'Orden de Prelación',
      s5_th2: 'Tipología de Entidad Guardiana',
      s5_th3: 'Naturaleza de la Adopción',
      s5_r1_h: '1. Sede Principal',
      s5_r1_ent: 'Universidades Públicas (Departamentos de Psicología Social, Metodología o Sociología Cuantitativa)',
      s5_r1_nat: 'Custodia académica fundacional, gobernanza del software y docencia de posgrado.',
      s5_r2_h: '2. Centros Estatales de I+D',
      s5_r2_ent: 'Institutos del Consejo Superior de Investigaciones Científicas (CSIC) y centros afines',
      s5_r2_nat: 'Integración en centros de ciencias sociales cuantitativas, redes complejas y supercomputación.',
      s5_r3_h: '3. Redes Universitarias',
      s5_r3_ent: 'Consorcios Interuniversitarios Nacionales e Internacionales',
      s5_r3_nat: 'Adopción colegiada interdepartamental en red abierta de investigación.',
      s5_r4_h: '4. Salvaguarda Abierta',
      s5_r4_ent: 'Consorcio Internacional Open Science / Fundación CERN Zenodo',
      s5_r4_nat: 'Custodia perpetua, inmutable y auditable como patrimonio abierto de la ciencia relacional.',

      // Firma
      sig_role: 'Profesor Titular de Psicología Social (jubilado)',
      sig_dept: 'NEXORD Research Initiative · Investigación independiente',
      sig_btn_pdf: '🖨️ Descargar Dossier en PDF',
      sig_btn_email: '✉️ Iniciar Tramitación Formal'
    },

    en: {
      flag: '🇬🇧',
      code: 'EN',
      page_title: 'Executive Dossier: Technological Legacy & Scientific Custody Offer · NEXORD',
      brand_sub: 'INSTITUTIONAL DOSSIER',
      nav_portal: '🏛️ Institutional Portal',
      nav_dial: '🧭 Orbital Dial',
      nav_deonto: '🛡️ Deontology',
      nav_print: '🖨️ Print / PDF',

      // Hero
      meta_badge: '🏛️ PUBLIC CALL FOR INSTITUTIONAL STEWARDSHIP',
      hero_title: 'Canonical Framework for Technological Legacy &amp; Scientific Custody',
      hero_subtitle: 'Terms and conditions for the transfer of the Computational Ordinal Sociometry and 3D/4D Digital Twin ecosystem (NEXORD / VISORD Engine v8.3) for <strong>Public Universities, R&D Centers, and Scientific Consortia</strong>.',
      hero_principle: '<strong>FOUNDATIONAL PRINCIPLE:</strong> Academic fiduciary and responsible stewardship transfer, not blind alienation. The software is transferred for preservation, maintenance, and research/teaching under strict deontological mandate (Rule 21).',

      // Section 1
      s1_title: 'The Transferred Scientific Asset (The Technological Endowment)',
      s1_lead: 'The promoter formally transfers the rights of custody, academic governance, and operation of the complete research ecosystem, developed over more than two decades within the Faculty of Psychology of the University of Barcelona:',
      s1_b1_title: '🐍 Native Python Calculation Engines',
      s1_b1_desc: 'Automated pipelines for data ingestion, ranking transcription *Breve → Moreno*, 4-position SMIb matrices ($DA, RC, pDA, pRC$), Benzécri correspondence analysis ($\chi^2$), absolute densities (BDR), and continuous physically-weighted relative balances (SDR, $W(k)=2^{1-k}$).',
      s1_b2_title: '🌐 3D/4D Digital Twin Ecosystem',
      s1_b2_desc: 'Interactive Three.js WebGL laboratories featuring continuous kinematic simulation: <code>VISORD_demo</code> (phase transitions and network gravity), <code>VISORD_acuario</code> (relational hydrostatics reactor and subtle ostracism detection), and <code>VISORD_dialectico</code> (dialectical dilemma amphitheater and Bales IPA Moviola).',
      s1_b3_title: '📐 Tensorial and Spectral Algebra',
      s1_b3_desc: 'Computational modules for projection on Grassmann manifolds $\\operatorname{Gr}(k, N)$, spectral gap evaluation, Fiedler algebraic connectivity ($\\lambda_2$), Heider structural frustration, and Estrada operators ($EE$).',
      s1_b4_title: '📚 BSOC Canonical Dataset &amp; Zenodo Depository',
      s1_b4_desc: 'Homologated empirical corpus of field sociomatrices, Monte Carlo simulations, and cultural works. Permanent CERN Zenodo records: Core Scientific Manifesto (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color:var(--neon-cyan);">DOI: 10.5281/zenodo.23329641</a>) and Supplementary Material with 6 Technical Annexes (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color:#F59E0B;">DOI: 10.5281/zenodo.23329641</a>) with full Google Scholar indexing.',

      // Section 2
      s2_title: 'Object of the Offer: Royalty-Free Responsible Custody',
      s2_lead: 'The handover requires no financial compensation for intellectual property rights. The <strong>Depository Institution / Custodial University</strong> assumes the preservation of the legacy under four structured institutional commitments:',
      s2_th1: 'Custody Axis',
      s2_th2: 'Commitment Assumed by Depository Institution',
      s2_r1_h: '1. Hosting & Infrastructure',
      s2_r1_t: 'Provide secure institutional servers or homologated cloud hosting with continuous backups and European data sovereignty guarantee (GDPR).',
      s2_r2_h: '2. Technological Maintenance',
      s2_r2_t: 'Periodically monitor compatibility of rendering dependencies (Three.js/WebGL), Python runtime environments, and W3C web standards.',
      s2_r3_h: '3. Credentials & Deontological Management',
      s2_r3_t: 'Provide authenticated access to accredited Principal Investigators, ethics review boards, and teaching curricula, ensuring compliance with Rule 21.',
      s2_r4_h: '4. Open Science Safeguard',
      s2_r4_t: 'Preserve the availability of the institutional repository under the open CC-BY-4.0 license for research and academic dissemination.',
      s2_r5_h: '5. Cosmopolitan Universal Mandate',
      s2_r5_t: 'Preserve the software\'s purpose as open human heritage (UNESCO Open Science), maintaining active and homologated Spanish and English, with architecture ready for future localizations.',

      // Section 3
      s3_title: 'Author\'s Maintenance and Voluntary Advisory Plan',
      s3_lead: 'To ensure an impeccable technological handover and relieve institutional personnel from mathematical or methodological uncertainties, the author formalizes an active honorary scientific advisory endowment:',
      s3_card_title: '🎓 Honorary Mentorship Commitment: 3 Years (Extendable to 5)',
      s3_card_intro: '<strong>Dr. José Manuel Cornejo Álvarez</strong> commits to act as <strong>Voluntary Methodological and Technological Advisor (ad honorem)</strong> for a period of 3 to 5 years, undertaking:',
      s3_li1: 'On-site or remote knowledge transfer of the mathematical architecture to researchers or engineers designated by the depository entity.',
      s3_li2: 'Quality supervision of KDE kernel calibrations, BDR/SDR densities, and adaptations to doctoral dissertations.',
      s3_li3: 'Advisory on the kinematic simulation pipeline and expert forensic reporting.',

      // Section 4
      s4_title: 'Inviolable Ethical Reversion Clause (Rule 21 &amp; Privacy)',
      s4_lead: 'The transfer is not an uncritical surrender. The deposit is subject to an <strong>express resolutory condition of automatic reversion</strong> to shield the ethical mission of the project:',
      s4_causes_title: '⚖️ Causes of Automatic Reversion',
      s4_c1: '<strong>Punitive Use of Data (Rule 21):</strong> Employing sociomatrices for sanctions, dismissals, public shaming, or damage to personal self-esteem.',
      s4_c2: '<strong>Violation of Privacy by Design:</strong> Disabling Q.GID anonymization or exposing participants\' legal civilian names.',
      s4_c3: '<strong>Restrictive Privatization:</strong> Converting the codebase into closed source or imposing paywalls violating CC-BY-4.0.',
      s4_c4: '<strong>Territorial Sequestration or Universal Blockade:</strong> Arbitrarily preventing free translation, federated replication, or international academic access across global linguistic trunks under the UNESCO Open Science framework.',
      s4_c5: '<strong>Prolonged Abandonment:</strong> System non-operation or downtime exceeding twelve (12) consecutive months without remedy.',
      s4_effects_title: '🛡️ Effects of Reversion & Trust Governance',
      s4_effects_text: 'Upon documented breach of any ethical cause, software ownership, repositories, and administration <strong>immediately revert to the author</strong>. In the event of death or sudden disability, they transfer by right to the designated <strong>Substitute Guardian</strong>.',

      // Section 5
      s5_title: 'Open Succession Protocol (Substitute Guardian)',
      s5_lead: 'To guarantee unconditional preservation of this legacy and prevent the ecosystem from becoming orphaned, inactive, or privatized, the canonical custody protocol establishes a structured order of institutional priority:',
      s5_th1: 'Priority Order',
      s5_th2: 'Type of Guardian Entity',
      s5_th3: 'Nature of Adoption',
      s5_r1_h: '1. Primary Headquarters',
      s5_r1_ent: 'Public Universities (Departments of Social Psychology, Methodology, or Quantitative Sociology)',
      s5_r1_nat: 'Foundational academic custody, software governance, and graduate-level teaching.',
      s5_r2_h: '2. State R&D Centers',
      s5_r2_ent: 'CSIC Research Institutes (Spanish National Research Council) and affiliated centers',
      s5_r2_nat: 'Integration into quantitative social sciences, complex networks, and supercomputing centers.',
      s5_r3_h: '3. University Networks',
      s5_r3_ent: 'National and International Inter-University Consortia',
      s5_r3_nat: 'Interdepartmental collegiate adoption across open research networks.',
      s5_r4_h: '4. Open Science Depository',
      s5_r4_ent: 'International Open Science Consortium / CERN Zenodo Foundation',
      s5_r4_nat: 'Perpetual, immutable, and auditable custody as open relational science heritage.',

      // Signature
      sig_role: 'Associate Professor of Social Psychology · University of Barcelona',
      sig_dept: 'Department of Social and Quantitative Psychology · Faculty of Psychology',
      sig_btn_pdf: '🖨️ Download Dossier in PDF',
      sig_btn_email: '✉️ Initiate Formal Application'
    }
  };

  function applyLanguage(lang) {
    const d = DOSSIER_I18N[lang] || DOSSIER_I18N.es;
    localStorage.setItem('nexord_lang', lang);
    document.documentElement.lang = lang;

    // Selector buttons
    const btnEs = document.getElementById('btn-dossier-lang-es');
    const btnEn = document.getElementById('btn-dossier-lang-en');
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

    // Header badge
    const badge = document.querySelector('.brand-badge');
    if (badge) badge.textContent = d.brand_sub;

    const navLinks = document.querySelectorAll('.header-nav .hdr-btn');
    if (navLinks.length >= 4) {
      navLinks[0].querySelector('span:last-child').textContent = d.nav_portal.replace('🏛️ ', '');
      navLinks[1].querySelector('span:last-child').textContent = d.nav_dial.replace('🧭 ', '');
      navLinks[2].querySelector('span:last-child').textContent = d.nav_deonto.replace('🛡️ ', '');
      navLinks[3].querySelector('span:last-child').textContent = d.nav_print.replace('🖨️ ', '');
    }

    // Hero
    const metaBadge = document.querySelector('.meta-badge-inst');
    if (metaBadge) metaBadge.textContent = d.meta_badge;

    const heroTitle = document.querySelector('.dossier-title');
    if (heroTitle) heroTitle.innerHTML = d.hero_title;

    const heroSub = document.querySelector('.dossier-subtitle');
    if (heroSub) heroSub.innerHTML = d.hero_subtitle;

    const heroPrinciple = document.querySelector('.hero-callout-principle');
    if (heroPrinciple) heroPrinciple.innerHTML = d.hero_principle;

    // Sections
    const cards = document.querySelectorAll('.dossier-card');
    if (cards.length >= 5) {
      // Sec 1
      cards[0].querySelector('.section-title span:last-child').innerHTML = d.s1_title;
      cards[0].querySelector('.dossier-p').innerHTML = d.s1_lead;
      const s1Boxes = cards[0].querySelectorAll('.feature-box');
      if (s1Boxes.length >= 4) {
        s1Boxes[0].querySelector('h4').innerHTML = '<span>🐍</span> ' + d.s1_b1_title.replace('🐍 ', '');
        s1Boxes[0].querySelector('p').innerHTML = d.s1_b1_desc;
        s1Boxes[1].querySelector('h4').innerHTML = '<span>🌐</span> ' + d.s1_b2_title.replace('🌐 ', '');
        s1Boxes[1].querySelector('p').innerHTML = d.s1_b2_desc;
        s1Boxes[2].querySelector('h4').innerHTML = '<span>📐</span> ' + d.s1_b3_title.replace('📐 ', '');
        s1Boxes[2].querySelector('p').innerHTML = d.s1_b3_desc;
        s1Boxes[3].querySelector('h4').innerHTML = '<span>📚</span> ' + d.s1_b4_title.replace('📚 ', '');
        s1Boxes[3].querySelector('p').innerHTML = d.s1_b4_desc;
      }

      // Sec 2
      cards[1].querySelector('.section-title span:last-child').innerHTML = d.s2_title;
      cards[1].querySelector('.dossier-p').innerHTML = d.s2_lead;
      const s2Th = cards[1].querySelectorAll('.dossier-table th');
      if (s2Th.length >= 2) {
        s2Th[0].textContent = d.s2_th1;
        s2Th[1].textContent = d.s2_th2;
      }
      const s2Rows = cards[1].querySelectorAll('.dossier-table tbody tr');
      if (s2Rows.length >= 5) {
        s2Rows[0].children[0].innerHTML = '<strong>' + d.s2_r1_h + '</strong>';
        s2Rows[0].children[1].textContent = d.s2_r1_t;
        s2Rows[1].children[0].innerHTML = '<strong>' + d.s2_r2_h + '</strong>';
        s2Rows[1].children[1].textContent = d.s2_r2_t;
        s2Rows[2].children[0].innerHTML = '<strong>' + d.s2_r3_h + '</strong>';
        s2Rows[2].children[1].textContent = d.s2_r3_t;
        s2Rows[3].children[0].innerHTML = '<strong>' + d.s2_r4_h + '</strong>';
        s2Rows[3].children[1].textContent = d.s2_r4_t;
        s2Rows[4].children[0].innerHTML = '<strong>' + d.s2_r5_h + '</strong>';
        s2Rows[4].children[1].textContent = d.s2_r5_t;
      }

      // Sec 3
      cards[2].querySelector('.section-title span:last-child').innerHTML = d.s3_title;
      cards[2].querySelector('.dossier-p').innerHTML = d.s3_lead;
      const s3Box = cards[2].querySelector('.feature-box');
      if (s3Box) {
        s3Box.querySelector('h4').innerHTML = '<span>🎓</span> ' + d.s3_card_title.replace('🎓 ', '');
        s3Box.querySelector('p').innerHTML = d.s3_card_intro;
        const s3Lis = s3Box.querySelectorAll('li');
        if (s3Lis.length >= 3) {
          s3Lis[0].textContent = d.s3_li1;
          s3Lis[1].textContent = d.s3_li2;
          s3Lis[2].textContent = d.s3_li3;
        }
      }

      // Sec 4
      cards[3].querySelector('.section-title span:last-child').innerHTML = d.s4_title;
      cards[3].querySelector('.dossier-p').innerHTML = d.s4_lead;
      const s4Boxes = cards[3].querySelectorAll('.feature-box');
      if (s4Boxes.length >= 2) {
        s4Boxes[0].querySelector('h4').innerHTML = '<span>⚖️</span> ' + d.s4_causes_title.replace('⚖️ ', '');
        const s4Lis = s4Boxes[0].querySelectorAll('li');
        if (s4Lis.length >= 5) {
          s4Lis[0].innerHTML = d.s4_c1;
          s4Lis[1].innerHTML = d.s4_c2;
          s4Lis[2].innerHTML = d.s4_c3;
          s4Lis[3].innerHTML = d.s4_c4;
          s4Lis[4].innerHTML = d.s4_c5;
        }
        s4Boxes[1].querySelector('h4').innerHTML = '<span>🛡️</span> ' + d.s4_effects_title.replace('🛡️ ', '');
        s4Boxes[1].querySelector('p').innerHTML = d.s4_effects_text;
      }

      // Sec 5
      cards[4].querySelector('.section-title span:last-child').innerHTML = d.s5_title;
      cards[4].querySelector('.dossier-p').innerHTML = d.s5_lead;
      const s5Th = cards[4].querySelectorAll('.dossier-table th');
      if (s5Th.length >= 3) {
        s5Th[0].textContent = d.s5_th1;
        s5Th[1].textContent = d.s5_th2;
        s5Th[2].textContent = d.s5_th3;
      }
      const s5Rows = cards[4].querySelectorAll('.dossier-table tbody tr');
      if (s5Rows.length >= 4) {
        s5Rows[0].children[0].innerHTML = '<strong>' + d.s5_r1_h + '</strong>';
        s5Rows[0].children[1].textContent = d.s5_r1_ent;
        s5Rows[0].children[2].textContent = d.s5_r1_nat;
        s5Rows[1].children[0].innerHTML = '<strong>' + d.s5_r2_h + '</strong>';
        s5Rows[1].children[1].textContent = d.s5_r2_ent;
        s5Rows[1].children[2].textContent = d.s5_r2_nat;
        s5Rows[2].children[0].innerHTML = '<strong>' + d.s5_r3_h + '</strong>';
        s5Rows[2].children[1].textContent = d.s5_r3_ent;
        s5Rows[2].children[2].textContent = d.s5_r3_nat;
        s5Rows[3].children[0].innerHTML = '<strong>' + d.s5_r4_h + '</strong>';
        s5Rows[3].children[1].textContent = d.s5_r4_ent;
        s5Rows[3].children[2].textContent = d.s5_r4_nat;
      }
    }

    // Signature Block
    const sigInfo = document.querySelector('.sig-info');
    if (sigInfo) {
      const ps = sigInfo.querySelectorAll('p');
      if (ps.length >= 2) {
        ps[0].textContent = d.sig_role;
        ps[1].textContent = d.sig_dept;
      }
    }
    const sigBtns = document.querySelectorAll('.sig-actions .btn-action-primary');
    if (sigBtns.length >= 2) {
      sigBtns[0].querySelector('span:last-child').textContent = d.sig_btn_pdf.replace('🖨️ ', '');
      sigBtns[1].querySelector('span:last-child').textContent = d.sig_btn_email.replace('✉️ ', '');
    }
  }

  window.setDossierLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', function () {
    const saved = localStorage.getItem('nexord_lang') || 'es';
    applyLanguage(saved);
  });
})();
