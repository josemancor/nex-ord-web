/**
 * =============================================================================
 * NEXORD / VISORD — MOTOR DE INTERNACIONALIZACIÓN DE LA HOME PROMOCIONAL
 * =============================================================================
 * Soporte bilingüe integral (Español oficial / English) con persistencia en
 * localStorage ('nexord_lang') y sincronización reactiva en todo el ecosistema.
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
      drop_glossary: 'Glosario Oficial (ES / EN)',
      drop_dial: '🧭 Dial Orbital Epistemológico',

      // Hero
      hero_pill: 'PLATAFORMA CIENTÍFICA DE SOCIOMETRÍA ORDINAL COMPUTACIONAL',
      hero_title: 'La Radiografía 3D de las<br><span class="gradient-text">Relaciones Humanas</span>',
      hero_subtitle: 'Descubre las corrientes invisibles, el liderazgo real, las alianzas latentes y el riesgo de ostracismo en tu grupo antes de que se conviertan en crisis. Diagnóstico instantáneo, visual y 100% no punitivo.',
      hero_btn_3d: '🚀 Explorar las 4 Joyas 3D',
      hero_btn_dial: '🧭 Dial Orbital',
      hero_btn_manifesto: '📜 Manifiesto Global (HTML)',
      hero_btn_custody: '🏛️ Custodia Institucional',
      hero_btn_solutions: '💼 Soluciones Sectoriales',

      // Video Hero HUD & Controls
      video_badge: 'VISORD 3D ENGINE IN MOTION · DEMO OFICIAL',
      video_meta: '⏱️ 01:09 MIN · VISUALIZADOR RELACIONAL 3D',
      video_btn_play: 'Pausa',
      video_btn_play_pause: 'Reproducir',
      video_btn_repeat: 'Repetir',
      video_btn_audio_on: 'Activar Audio',
      video_btn_audio_off: 'Silenciar Audio',
      video_btn_fs: 'Pantalla Completa',
      video_player_title: 'Pulsa para reproducir o pausar el video',
      video_btn_play_title: 'Reproducir / Pausar Video',
      video_btn_audio_title: 'Activar o Silenciar Audio de la Demostración',
      video_btn_fs_title: 'Pantalla Completa',
      bond_attraction_term: 'Verde:',
      bond_attraction_text: 'Atracción Mutua & Cohesión',
      bond_rejection_term: 'Magenta:',
      bond_rejection_text: 'Rechazo & Fricción Oculta',
      bond_ostracism_term: 'Periferia:',
      bond_ostracism_text: 'Ostracismo Invisible',
      video_sub_initial: 'NEXORD · Plataforma de Sociometría Ordinal Computacional y Socio-Termodinámica 3D',
      video_cta_pill: '🎮 Manipular Entorno 3D en Vivo',

      // Anatomía de los Vínculos
      bonds_tag: 'Física Relacional Visible',
      bonds_title: 'Qué estás viendo en el simulador: Las 3 Fuerzas que Deciden el Destino del Grupo',
      bonds_subtitle: 'La sociometría clásica de los años 50 solo dibujaba flechas estáticas. NEXORD captura la tensión viva de atracción y rechazo en tiempo real.',
      bond_c1_badge: '🟢 LA FUERZA QUE UNE',
      bond_c1_title: 'Atracción & Elección Mutua',
      bond_c1_text: 'Haces luminosos en <strong>verde neón</strong>. Afinidad espontánea, reciprocidad afectiva y admiración operativa. Es el pegamento relacional que retiene el talento, crea liderazgos naturales y sostiene al equipo bajo presión.',
      bond_c1_metric_label: 'Impacto Grupal:',
      bond_c1_metric_val: 'Resiliencia y Sinergia Colectiva',
      bond_c2_badge: '🔴 LA FUERZA QUE FRACTURA',
      bond_c2_title: 'Rechazo & Fricción Latente',
      bond_c2_text: 'Haces tensos en <strong>magenta neón</strong>. Incompatibilidades soterradas, desconfianza no dicha y vetos cruzados. El 85% de las crisis nunca estallan en público: se incuban aquí en silencio hasta destruir proyectos y desintegrar departamentos.',
      bond_c2_metric_label: 'Impacto Grupal:',
      bond_c2_metric_val: 'Fugas de Talento y Boicot Silencioso',
      bond_c3_badge: '⚪ LA HERIDA INVISIBLE',
      bond_c3_title: 'Ostracismo & Vacío Pasivo',
      bond_c3_text: 'Nodos aislados que flotan en la <strong>periferia oscura</strong>. Personas a las que nadie elige ni rechaza abiertamente: la indiferencia absoluta. Destroza la autoestima silenciosamente y es invisible para los tests de clima laboral convencionales.',
      bond_c3_metric_label: 'Impacto Grupal:',
      bond_c3_metric_val: 'Aislamiento y Desconexión Profunda',

      // Métricas Rápidas Hero
      hero_stat_1_val: '3 Min',
      hero_stat_1_desc: 'Tiempo de pasación individual por ordenación (Breve → ORBIT).',
      hero_stat_2_val: 'Q81',
      hero_stat_2_desc: 'Figuras Relacionales Sociométricas oficiales computadas en retícula diádica.',
      hero_stat_3_val: '18D',
      hero_stat_3_desc: 'Índices de Densidad Relacional en 3 prismas duales (BDR / SDR).',
      hero_stat_4_val: '5',
      hero_stat_4_desc: 'VISORD\'s grupales: gemelos digitales 3D/4D de diagnóstico continuo.',

      // Sección 1: Dolor / Contraste
      pain_tag: 'Diagnóstico de Precisión',
      pain_title: 'Por qué los métodos tradicionales están ciegos',
      pain_subtitle: 'Los cuestionarios de clima y los tests habituales capturan opiniones superficiales. NEXORD revela la estructura profunda de atracción y rechazo.',
      pain_trad_badge: 'Enfoque Clásico (Años 50)',
      pain_trad_heading: 'Cuestionarios y Sociogramas Planos',
      pain_trad_item1: '<strong>Sesgo de complacencia:</strong> La gente contesta lo políticamente correcto para no quedar mal.',
      pain_trad_item2: '<strong>Ceguera ante el ostracismo:</strong> Un miembro ignorado pasivamente pasa totalmente desapercibido.',
      pain_trad_item3: '<strong>Fotos fijas estáticas:</strong> Muestran un dibujo 2D congelado sin capturar la tensión viva del grupo.',
      pain_trad_item4: '<strong>Procesos lentos y tediosos:</strong> Cuestionarios densos de 30 minutos que provocan fatiga y respuestas al azar.',
      pain_nex_badge: 'Ecosistema NEXORD / VISORD',
      pain_nex_heading: 'Sociometría Ordinal & Física Grupal',
      pain_nex_item1: '<strong>Sociometría Breve en 3 minutos:</strong> Ordenación intuitiva sin agobio, con aleatorización anti-sesgo.',
      pain_nex_item2: '<strong>Detección del rechazo sutil:</strong> El algoritmo de hidrostática identifica de inmediato el aislamiento invisible.',
      pain_nex_item3: '<strong>Gemelo Digital 3D/4D:</strong> Visualización viva de cuencas de atracción, camarillas y liderazgo real en movimiento.',
      pain_nex_item4: '<strong>Retorno Ético no punitivo:</strong> Enfoque constructivo que preserva siempre la autoestima y la cohesión.',

      // Sección 2: Showroom (4 Joyas)
      show_tag: 'Showroom Tecnológico',
      show_title: 'Las 4 Joyas Interactivas VISORD',
      show_subtitle: 'Explora directamente nuestros laboratorios en tiempo real. Toca los nodos, rota las órbitas y siente la física de las relaciones.',
      jewel_1_title: 'Acuario Reactor 3D',
      jewel_1_subtitle: 'Hidrostática & Ostracismo',
      jewel_1_desc: 'Física de fluidos y boyado relacional. Detecta en qué estrato flota cada miembro e ilumina el ostracismo pasivo y la sedimentación antes de una crisis de grupo.',
      jewel_1_btn: 'Abrir Acuario 3D ↗',
      jewel_2_title: 'VISORD Cultural',
      jewel_2_subtitle: 'Dramaturgia & Obras Maestras',
      jewel_2_desc: 'Sociometría viva de hitos dramáticos: <em>12 Hombres sin Piedad</em>, <em>La Casa de Bernarda Alba</em> y <em>El Señor de las Moscas</em>. Comprueba cómo la matemática predice la trama.',
      jewel_2_btn: 'Explorar Obras ↗',
      jewel_3_title: 'VISORD Dialéctico',
      jewel_3_subtitle: 'Tensiones & Micro-Interacciones',
      jewel_3_desc: 'Anfiteatro experimental de micro-interacciones, Moviola Bales IPA y dilemas cooperativos vs competitivos (bienes comunes y dilema del prisionero).',
      jewel_3_btn: 'Abrir Dialéctico ↗',
      jewel_4_title: 'VISORD Demo 3D',
      jewel_4_subtitle: 'Dinámica Continua N < 51',
      jewel_4_desc: 'Simulador 3D continuo de transiciones de fase, campos gravitatorios relacionales y cuencas de atracción para grupos de hasta 50 participantes.',
      jewel_4_btn: 'Lanzar Simulador ↗',

      // Sección 3: Soluciones Sectoriales
      sol_tag: 'Impacto Aplicado',
      sol_title: 'Soluciones Especializadas por Sector',
      sol_subtitle: 'Adaptado a las necesidades específicas de centros educativos, empresas y entornos clínicos.',
      sol_s1_title: 'Educación & Aulas',
      sol_s1_prob: '<strong>El Desafío:</strong> El acoso escolar (bullying) ocurre en la sombra. Quien lo sufre calla, y los agresores suelen aparentar popularidad.',
      sol_s1_sol: '<strong>La Solución NEXORD:</strong> Radiografía en 3 minutos. Identifica inmediatamente al alumno desconectado o en riesgo sin interrogarlo directamente.',
      sol_s1_b1: 'Detección temprana del aislamiento sutil y silencioso.',
      sol_s1_b2: 'Optimización de grupos de trabajo y seating pedagógico.',
      sol_s1_b3: 'Garantía total de no estigmatizar a ningún menor.',
      sol_s2_title: 'Empresas & Equipos',
      sol_s2_prob: '<strong>El Desafío:</strong> Organigramas formales que no reflejan quién manda de verdad, silos departamentales y fuga de talento por burnout relacional.',
      sol_s2_sol: '<strong>La Solución NEXORD:</strong> Identificación del liderazgo informal, camarillas aisladas y cuellos de botella de comunicación interna.',
      sol_s2_b1: 'Mapeo de la confianza real frente al poder jerárquico formal.',
      sol_s2_b2: 'Integración ágil en fusiones, adquisiciones y reestructuraciones.',
      sol_s2_b3: 'Informes de auditoría pericial para comités de dirección.',
      sol_s3_title: 'Salud & Ámbito Clínico',
      sol_s3_prob: '<strong>El Desafío:</strong> Resistencias dialécticas, alianzas patológicas y dinámicas tóxicas no declaradas en terapias de grupo y mediación familiar.',
      sol_s3_sol: '<strong>La Solución NEXORD:</strong> Moviola temporal de micro-interacciones. Mide la evolución sesión a sesión de la alianza terapéutica.',
      sol_s3_b1: 'Auditoría de reciprocidad en adicciones y grupos de apoyo.',
      sol_s3_b2: 'Seguimiento longitudinal de la cohesión interpersonal.',
      sol_s3_b3: 'Retorno reflexivo individualizado que refuerza el compromiso.',

      // Sección 4: Cómo Funciona (3 Pasos)
      flow_tag: 'Flujo Operativo Simple',
      flow_title: 'De la recogida al informe en 3 pasos',
      flow_subtitle: 'Diseñado para que cualquier institución pueda desplegarlo sin fricción tecnológica ni desgaste.',
      flow_s1_title: 'Pasación Breve (3 min)',
      flow_s1_desc: 'Cada participante accede desde su móvil o tablet mediante un enlace tokenizado seguro. Ordena a sus compañeros de forma visual sin fatiga cognitiva ni preguntas invasivas.',
      flow_s2_title: 'Ingestión y Física SMIb',
      flow_s2_desc: 'El motor VISORD calcula al instante la matriz diádica de emisión y recepción, descomponiendo los 255 indicadores de densidad absoluta (BDR) y relativa (SDR).',
      flow_s3_title: 'Gemelo 3D e Informe Forense',
      flow_s3_desc: 'La dirección recibe un informe ejecutivo claro, acompañado de las visualizaciones interactivas en 3D/4D y recomendaciones prácticas de intervención inmediata.',

      // Sección 5: Garantía Ética
      ethics_heading: '<span>🛡️</span> Mandato Deontológico',
      ethics_text_1: 'En NEXORD, la ciencia relacional está al servicio exclusivo del crecimiento humano. Cumplimos con los principios más estrictos de <strong>Privacidad por Diseño (Privacy by Design)</strong> y el mandato ético del Investigador Principal: <em>lo que detectamos son fenómenos termodinámicos estrictamente grupales, nunca defectos intrínsecos de la personalidad</em>. Queda formalmente garantizado el uso no punitivo de los datos para salvaguardar la dignidad y autoestima de cada persona.',
      ethics_text_2: '✓ Cumplimiento RGPD &bull; Encriptación de extremo a extremo &bull; Destrucción forense de datos efímeros',
      ethics_btn: 'Ver Portal del Participante ↗',

      // Sección 6: Bóveda de Investigación
      vault_tag: 'Bóveda de Investigación',
      vault_title: 'Rigor Científico & Documentación',
      vault_subtitle: 'Para investigadores, psicómetras y auditores técnicos: acceso abierto a toda la arquitectura matemática, manifiesto y niveles de formalización.',
      v_l1_title: 'Nivel 1: Intuitivo',
      v_l1_desc: 'Moviola de dinámicas grupales, micro-interacciones y animación de partículas.',
      v_l1_btn: 'Consultar Nivel 1 →',
      v_l2_title: 'Nivel 2: Básico',
      v_l2_desc: 'Matrices elementales de adyacencia, reciprocidad diádica y grafos fundamentales.',
      v_l2_btn: 'Consultar Nivel 2 →',
      v_l3_title: 'Nivel 3: Esquema SMIb',
      v_l3_desc: 'Tetragrama oficial de 4 posiciones: expectativa emisor, preferencia y recepción.',
      v_l3_btn: 'Consultar Nivel 3 →',
      v_l4_title: 'Nivel 4: Aplicaciones',
      v_l4_desc: 'Batería de casos periciales resueltos en contextos escolares, laborales y clínicos.',
      v_l4_btn: 'Consultar Nivel 4 →',
      v_l5_title: 'Nivel 5: Matemático',
      v_l5_desc: 'Variedad de Grassmann Gr(k,N), autovalores de Fiedler λ2 y física de campos tensoriales.',
      v_l5_btn: 'Consultar Nivel 5 →',
      v_l6_title: 'Nivel 6: Informes',
      v_l6_desc: 'Generador y plantillas de informes periciales socio-termodinámicos de alta fidelidad.',
      v_l6_btn: 'Consultar Nivel 6 →',
      v_l7_title: 'Nivel 7: Manifiesto',
      v_l7_desc: 'Manifiesto Científico 2026, DOI Zenodo, licencias académicas y bibliografía.',
      v_l7_btn: 'Consultar Nivel 7 →',
      v_glo_title: 'Glosario Oficial',
      v_glo_desc: 'Diccionario normativo oficial de términos, operadores y métricas NEXORD.',
      v_glo_btn: 'Abrir Glosario →',

      // Sección 7: Custodia Institucional
      cust_tag: 'Transferencia Tecnológica & Ciencia Abierta',
      cust_title: 'Llamamiento a la Custodia Institucional',
      cust_subtitle: 'Buscamos una universidad, centro de supercomputación o institución científica que asuma la custodia tecnológica y gobernanza a largo plazo del ecosistema NEXORD / VISORD.',
      cust_banner_title: 'MARCO OFICIAL DE CUSTODIA INSTITUCIONAL Y LEGADO CIENTÍFICO',
      cust_banner_desc: 'Bases y condiciones de depósito tecnológico universitario: dote de software, asesoría honoraria voluntaria del autor (3 a 5 años), blindaje ético y cláusula de reversión (custodia responsable y no cesión a ciegas).',
      cust_banner_btn: 'Ver Marco de Custodia (PDF / Web) →',

      // ¿Qué es NEXORD?
      what_title: '¿QUÉ ES NEXORD?',
      what_p1: '<strong>1.</strong> Plataforma científica de sociometría ordinal computacional y termodinámica relacional que formaliza la microfísica de los colectivos humanos mediante matrices diádicas continuas SMIb y variedades de Grassmann Gr(k, N).',
      what_p2: '<strong>2.</strong> Supera el sociograma tradicional mediante una pasación intuitiva de 3 minutos y un motor 3D/4D (VISORD) que revela cuencas gravitatorias de afinidad, liderazgos emergentes y ostracismo invisible en tiempo real.',
      what_p3: '<strong>3.</strong> Diseñada bajo el principio hipocrático <em>primum non nocere</em>, traduce la energía vincular a tres escalas decisionales (Dirección, Dinámica y Sujeto) garantizando anonimato ciego y uso exclusivamente formativo no punitivo.',

      // Díptico: Ofrece vs Pide
      offer_title: '¿QUÉ SE OFRECE?',
      offer_lead: 'Una dote científica completa, operativa, validada empíricamente y lista para su transferencia:',
      offer_i1: '<strong style="color: #FFF;">Plataforma Integral:</strong> Motores computacionales de sociometría ordinal en Python y el ecosistema visual 3D/4D VISORD (Acuario D18, Dialéctico, Cultural y Demo Moviola).',
      offer_i2: '<strong style="color: #FFF;">Canon Metodológico:</strong> Formalización axiomática de la matriz de 4 posiciones SMIb (DA, RC, pDA, pRC), retícula universal Q81(9×9), densidades BDR/SDR e invarianza baricéntrica demostrada.',
      offer_i3: '<strong style="color: #FFF;">Corpus Empírico (BSOC):</strong> Banco de Datos Sociométricos Oficiales con series longitudinales homologadas (matrices de campo reales, simuladas Monte Carlo y de dramaturgia cultural).',
      offer_i4: '<strong style="color: #FFF;">Identificador Persistente &amp; DOI:</strong> Registro permanente en CERN Zenodo (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color: var(--neon-green); text-decoration: underline; font-weight:700;">DOI: 10.5281/zenodo.23329641</a>) indexado en Google Académico, integrando la Edición Oficial del Manifiesto y sus 6 anexos técnicos bilingües.',
      offer_i5: '<strong style="color: #FFF;">Comunidad Open Science:</strong> Metodología de código abierto para investigación interuniversitaria en psicología de grupos, sociología relacional y ciencias de redes complejas.',
      offer_i6: '<strong style="color: #FFF;">Vocación Universal y Transferencia Multilingüe:</strong> Plataforma homologada en Español  e Inglés para investigación internacional, con arquitectura abierta e idiomas para futuras localizaciones....',
      offer_note: '💡 Transferencia sin royalties comerciales con fines estrictamente científicos y docentes.',

      req_title: '¿QUÉ SE PIDE A LA INSTITUCIÓN?',
      req_lead: 'Un marco institucional y técnico que garantice la sostenibilidad, seguridad y solvencia del sistema:',
      req_i1: '<strong style="color: #FFF;">Custodia Institucional &amp; Gobernanza:</strong> Adopción por una universidad, cátedra o instituto de investigación que asegure la preservación patrimonial y continuidad académica del proyecto.',
      req_i2: '<strong style="color: #FFF;">Entorno de Accesos Controlados:</strong> Alojamiento en servidores o nube institucional segura que garantice alta disponibilidad, copias de seguridad auditadas y estricta soberanía de los datos.',
      req_i3: '<strong style="color: #FFF;">Mantenimiento Tecnológico Evolutivo:</strong> Supervisión técnica de dependencias (WebGL/Three.js, Python, navegadores web) y soporte para actualizaciones metodológicas y técnicas.',
      req_i4: '<strong style="color: #FFF;">Gestión de Credenciales &amp; Deontología:</strong> Habilitación, control y revocación de accesos para Investigadores Principales (IPs) acreditados, velando por el cumplimiento del protocolo deontológico.',
      req_note: '🏛️ Ideal para departamentos de Psicología Social, Sociología Cuantitativa, Ciencia de Datos o Centros TIC.',

      // Blindaje técnico y legal
      guard_title: 'GARANTÍAS EXISTENTES DE BLINDAJE TÉCNICO Y LEGAL',
      guard_b1_title: '🔒 Privacy by Design (Q.GID / T1-T9)',
      guard_b1_desc: 'Anonimización oficial obligatoria (1A..5A, 1B..5B), tokens ciegos de sesión, disociación nominal absoluta y secreto matemático del voto. Imposible reconstruir delaciones individuales.',
      guard_b2_title: '📜 Licencia Abierta CC-BY-4.0',
      guard_b2_desc: 'Licencia Creative Commons Atribución 4.0 Internacional: libertad para compartir, adaptar y desplegar con fines docentes y de investigación, preservando la autoría científica original.',
      guard_b3_title: '🌐 Depósito CERN Zenodo (Inmutable)',
      guard_b3_desc: 'DOI persistente <code style="color:var(--neon-green);">10.5281/zenodo.23329641</code> (Edición Oficial: Manifiesto Central y Material Suplementario), con archivo de metadatos científicos Highwire Press y Dublin Core.',
      guard_b4_title: '🔍 Código Auditable &amp; Determinista',
      guard_b4_desc: 'Matemática verificable (descomposición SVD, χ², operadores de Estrada, Grassmann). Sin algoritmos de caja negra no reproducibles.',
      guard_b5_title: '🌍 Universalidad y Nodos Federados (UNESCO Open Science)',
      guard_b5_desc: 'Patrimonio Abierto de la Humanidad. Cláusula de salvaguarda que impide el secuestro territorial o lingüístico: arquitectura desacoplada homologada en Español e Inglés, con idiomas para futuras localizaciones..., garantizando su réplica y despliegue en redes universitarias sin fronteras geopolíticas.',

      // Formulario de Contacto
      contact_tag: 'CANAL DIRECTO DE CONTACTO',
      contact_title: 'Proponer Custodia Institucional o Proyecto Piloto',
      contact_subtitle: 'Envíe su propuesta institucional directamente al equipo promotor o copie el borrador estructurado para tramitación rectoral o departamental.',
      contact_pi_label: 'INVESTIGADOR PRINCIPAL PROMOTOR:',
      contact_pi_sub: 'NEXORD Research Initiative · Investigación independiente',
      form_inst_label: 'Institución / Universidad / Organismo *',
      form_inst_ph: 'Ej. Universidad Complutense / CSIC / Instituto...',
      form_rep_label: 'Nombre del Representante / Cargo *',
      form_rep_ph: 'Ej. Dra. Carmen Morales / Decana, Dir. Dpto.',
      form_email_label: 'Correo Electrónico Institucional *',
      form_type_label: 'Modalidad de Interés *',
      form_type_opt1: 'Custodia y Gobernanza Institucional Permanente',
      form_type_opt2: 'Alojamiento de Servidores / Infraestructura Segura',
      form_type_opt3: 'Convenio de Investigación / Adopción de Baterías',
      form_type_opt4: 'Nodo Federado Internacional / Adopción Lingüística (RU, ZH, EN...)',
      form_type_opt5: 'Proyecto Piloto de Transferencia en Campo',
      form_type_opt6: 'Otra propuesta institucional',
      form_msg_label: 'Mensaje / Alcance de la Propuesta',
      form_msg_ph: 'Indique brevemente el interés de su entidad, capacidades de alojamiento o marco de colaboración propuesto...',
      form_btn_pdf: '📄 Ver Marco Oficial (PDF)',
      form_btn_copy: '📋 Copiar Borrador al Portapapeles',
      form_btn_send: '📤 Enviar Propuesta (Abrir Correo)',

      // CTA Banner Final
      cta_title: '¿Listo para ver lo que otros no pueden ver?',
      cta_subtitle: 'Descubre cómo NEXORD transforma la convivencia, el rendimiento de tus equipos y la prevención del conflicto en tu institución.',
      cta_btn_demos: '🚀 Lanzar Demostraciones 3D',
      cta_btn_custody: '🏛️ Propuesta de Custodia Institucional',

      // Footer
      foot_inicio: 'Inicio',
      foot_custodia: 'Custodia Institucional',
      foot_demo: 'VISORD Demo 3D',
      foot_cultural: 'VISORD Cultural',
      foot_acuario: 'VISORD Acuario',
      foot_dialectico: 'VISORD Dialéctico',
      foot_retorno: 'Portal del Participante',
      foot_glosario: 'Glosario Oficial',
      foot_dial: 'Dial Orbital 3-6-9',
      foot_cite_btn: 'CITAR CON BibTeX',
      foot_platform_lead: '<strong>NEXORD / VISORD Engine</strong> &copy; 2026 &bull; Plataforma Científica de Sociometría Ordinal Computacional y Diagnóstico Socio-Termodinámico.',
      foot_open_science: 'Desarrollado bajo el mandato deontológico de Ciencia Abierta (Open Science). Prohibido el uso punitivo o difamatorio de los datos.',
      foot_lang_future: 'Idiomas para futuras localizaciones...',

      // Vertical Nav Band Tooltips
      vnav_tip_inicio: 'Inicio',
      vnav_tip_dolor: '¿Por qué?',
      vnav_tip_showroom: 'Joyas 3D',
      vnav_tip_soluciones: 'Soluciones',
      vnav_tip_etica: 'Ética',
      vnav_tip_boveda: 'Ciencia',
      vnav_tip_custodia: 'Custodia',

      // Modal de Citación
      modal_title: 'Cita Académica Oficial · NEXORD / VISORD Engine',
      modal_hint_bibtex: 'Entrada para LaTeX, Overleaf y gestores bibliográficos compatibles:',
      modal_link_manifesto_web: 'Ver Manifiesto Web ↗',
      modal_link_supp: 'Material Suplementario (6 Docs) ↗',
      modal_link_summary_en: 'Summary EN (PDF) ↗',
      modal_link_man_es: 'Manifiesto ES (PDF) ↗',
      modal_link_man_en: 'Manifesto EN (PDF) ↗',
      modal_link_zenodo: 'Repositorio CERN Zenodo ↗',
      modal_btn_copy: 'Copiar al Portapapeles',

      // Extras & Accesibilidad
      video_fallback: 'Tu navegador no soporta el elemento de video.',
      brand_home_title: 'Volver a la Portada de Bienvenida NEXORD',
      nav_dial_btn_title: 'Abrir Dial Orbital Epistemológico (9 Sectores)',
      btn_lang_es_title: 'Español',
      btn_lang_en_title: 'English (International)',
      doi_license_title: 'Creative Commons Atribución 4.0 Internacional',
      nav_main_aria: 'Navegación Principal',
      video_hero_aria: 'Demostración Oficial de VISORD 3D',
      vnav_band_aria: 'Navegación vertical por secciones',
      vnav_btn_up_title: 'Sección anterior (▲)',
      vnav_btn_up_aria: 'Ir a sección anterior',
      vnav_btn_down_title: 'Siguiente sección (▼)',
      vnav_btn_down_aria: 'Ir a siguiente sección',
      vnav_dots_aria: 'Indicadores de sección',
      vnav_btn_dial_title: 'Abrir Dial Orbital Epistemológico (9 Sectores)',
      vnav_btn_home_title: 'Volver a la Portada de Bienvenida NEXORD (🏠)',
      vnav_dot_titles: ['1. Inicio / Hero', '2. ¿Por qué NEXORD?', '3. Joyas 3D', '4. Soluciones', '5. Garantía Ética', '6. Bóveda Científica', '7. Custodia Institucional'],
      modal_close_aria: 'Cerrar',
      modal_link_man_web_title: 'Abrir Manifiesto Científico Oficial en la Web (Zero-Install, 29 Láminas y Glosario)',
      modal_link_supp_title: 'Ver Material Suplementario y Anexos Técnicos (6 Documentos)',
      modal_link_sum_en_title: 'Descargar Resumen Ejecutivo Oficial (Edición en Inglés, PDF ~500 kB)',
      modal_link_man_es_title: 'Descargar Manifiesto Científico Oficial (Edición en Español, PDF 58 MB)',
      modal_link_man_en_title: 'Descargar Manifiesto Científico Oficial (Edición en Inglés, PDF 58 MB)',
      modal_link_zenodo_title: 'Ver Registro y Custodia Oficial en CERN Zenodo (DOI: 10.5281/zenodo.23329641)'
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
      drop_glossary: 'Official Glossary (ES / EN)',
      drop_dial: '🧭 Epistemological Orbital Dial',

      // Hero
      hero_pill: 'SCIENTIFIC PLATFORM FOR COMPUTATIONAL ORDINAL SOCIOMETRY',
      hero_title: 'The 3D Radiography of<br><span class="gradient-text">Human Relationships</span>',
      hero_subtitle: 'Uncover invisible currents, authentic leadership, latent factions, and hidden ostracism risks in your group before they become crises. Instantaneous, visual, and 100% non-punitive diagnosis.',
      hero_btn_3d: '🚀 Explore the 4 3D Jewels',
      hero_btn_dial: '🧭 Orbital Dial',
      hero_btn_manifesto: '📜 Global Manifesto (HTML)',
      hero_btn_custody: '🏛️ Institutional Stewardship',
      hero_btn_solutions: '💼 Sectoral Solutions',

      // Video Hero HUD & Controls
      video_badge: 'VISORD 3D ENGINE IN MOTION · OFFICIAL DEMO',
      video_meta: '⏱️ 01:09 MIN · 3D RELATIONAL VISUALIZER',
      video_btn_play: 'Pause',
      video_btn_play_pause: 'Play',
      video_btn_repeat: 'Replay',
      video_btn_audio_on: 'Enable Audio',
      video_btn_audio_off: 'Mute Audio',
      video_btn_fs: 'Full Screen',
      video_player_title: 'Click to play or pause the video',
      video_btn_play_title: 'Play / Pause Video',
      video_btn_audio_title: 'Enable or Mute Demonstration Audio',
      video_btn_fs_title: 'Full Screen',
      bond_attraction_term: 'Green:',
      bond_attraction_text: 'Mutual Attraction & Cohesion',
      bond_rejection_term: 'Magenta:',
      bond_rejection_text: 'Rejection & Hidden Friction',
      bond_ostracism_term: 'Periphery:',
      bond_ostracism_text: 'Invisible Ostracism',
      video_sub_initial: 'NEXORD · Computational Ordinal Sociometry Platform & 3D Socio-Thermodynamics',
      video_cta_pill: '🎮 Manipulate Live 3D Environment',

      // Anatomy of Bonds
      bonds_tag: 'Visible Relational Physics',
      bonds_title: 'What you are seeing in the simulator: The 3 Forces that Shape Group Destiny',
      bonds_subtitle: 'Classical 1950s sociometry only drew static arrows. NEXORD captures the living tension of attraction and rejection in real time.',
      bond_c1_badge: '🟢 THE UNITING FORCE',
      bond_c1_title: 'Attraction & Mutual Choice',
      bond_c1_text: 'Luminous beams in <strong>neon green</strong>. Spontaneous affinity, affective reciprocity, and operational admiration. The relational glue that retains talent, fosters natural leadership, and sustains the team under pressure.',
      bond_c1_metric_label: 'Group Impact:',
      bond_c1_metric_val: 'Resilience & Collective Synergy',
      bond_c2_badge: '🔴 THE FRACTURING FORCE',
      bond_c2_title: 'Rejection & Latent Friction',
      bond_c2_text: 'Tense beams in <strong>neon magenta</strong>. Covert incompatibilities, unspoken distrust, and cross-vetoes. 85% of crises never erupt in public: they incubate here in silence until destroying projects and fracturing departments.',
      bond_c2_metric_label: 'Group Impact:',
      bond_c2_metric_val: 'Talent Drain & Covert Friction',
      bond_c3_badge: '⚪ THE INVISIBLE WOUND',
      bond_c3_title: 'Ostracism & Passive Void',
      bond_c3_text: 'Isolated nodes drifting in the <strong>dark periphery</strong>. Individuals neither openly chosen nor rejected: absolute indifference. It silently erodes self-esteem and remains invisible to conventional climate surveys.',
      bond_c3_metric_label: 'Group Impact:',
      bond_c3_metric_val: 'Isolation & Deep Disconnection',

      // Hero Quick Stats
      hero_stat_1_val: '3 Min',
      hero_stat_1_desc: 'Individual completion time via ordinal ranking (Breve → ORBIT).',
      hero_stat_2_val: 'Q81',
      hero_stat_2_desc: 'Official Sociometric Relational Figures computed in dyadic lattice.',
      hero_stat_3_val: '18D',
      hero_stat_3_desc: 'Relational Density Indices across 3 dual prisms (BDR / SDR).',
      hero_stat_4_val: '5',
      hero_stat_4_desc: 'Group VISORDs: 3D/4D digital twins for continuous diagnosis.',

      // Section 1: Pain / Contrast
      pain_tag: 'Precision Diagnosis',
      pain_title: 'Why traditional methods are blind',
      pain_subtitle: 'Climate surveys and conventional tests capture superficial opinions. NEXORD reveals the deep architecture of attraction and rejection.',
      pain_trad_badge: 'Classical Approach (1950s)',
      pain_trad_heading: 'Questionnaires & Flat Sociograms',
      pain_trad_item1: '<strong>Social desirability bias:</strong> People answer politically correctly to avoid social awkwardness.',
      pain_trad_item2: '<strong>Blindness to ostracism:</strong> A passively ignored member goes completely undetected.',
      pain_trad_item3: '<strong>Static snapshots:</strong> They show a frozen 2D diagram without capturing living group tension.',
      pain_trad_item4: '<strong>Slow & tedious processes:</strong> 30-minute dense surveys causing fatigue and random answers.',
      pain_nex_badge: 'NEXORD / VISORD Ecosystem',
      pain_nex_heading: 'Ordinal Sociometry & Group Physics',
      pain_nex_item1: '<strong>Brief Sociometry in 3 minutes:</strong> Intuitive ranking without stress, with anti-bias randomization.',
      pain_nex_item2: '<strong>Subtle rejection detection:</strong> Hydrostatic algorithm immediately identifies invisible isolation.',
      pain_nex_item3: '<strong>3D/4D Digital Twin:</strong> Living visualization of attraction basins, factions, and emergent leadership in motion.',
      pain_nex_item4: '<strong>Non-punitive Ethical Feedback:</strong> Constructive approach that always preserves self-esteem and cohesion.',

      // Section 2: Showroom (4 Jewels)
      show_tag: 'Technological Showroom',
      show_title: 'The 4 Interactive VISORD Jewels',
      show_subtitle: 'Explore our laboratories directly in real time. Touch the nodes, rotate orbits, and feel the physics of relationships.',
      jewel_1_title: '3D Reactor Aquarium',
      jewel_1_subtitle: 'Hydrostatics & Ostracism',
      jewel_1_desc: 'Fluid physics and relational buoyancy. Detects each member\'s flotation layer and illuminates passive ostracism and sedimentation before group crises.',
      jewel_1_btn: 'Open 3D Aquarium ↗',
      jewel_2_title: 'VISORD Cultural',
      jewel_2_subtitle: 'Dramaturgy & Masterworks',
      jewel_2_desc: 'Living sociometry of dramatic milestones: <em>12 Angry Men</em>, <em>The House of Bernarda Alba</em>, and <em>Lord of the Flies</em>. See how mathematics predicts narrative plot.',
      jewel_2_btn: 'Explore Masterworks ↗',
      jewel_3_title: 'VISORD Dialectical',
      jewel_3_subtitle: 'Tensions & Micro-Interactions',
      jewel_3_desc: 'Experimental amphitheater of micro-interactions, Bales IPA Moviola, and cooperative vs competitive dilemmas (Common Goods and Prisoner\'s Dilemma).',
      jewel_3_btn: 'Open Dialectical ↗',
      jewel_4_title: 'VISORD Demo 3D',
      jewel_4_subtitle: 'Continuous Dynamics N < 51',
      jewel_4_desc: 'Continuous 3D simulator of phase transitions, relational gravitational fields, and attraction basins for groups up to 50 participants.',
      jewel_4_btn: 'Launch Simulator ↗',

      // Section 3: Sector Solutions
      sol_tag: 'Applied Impact',
      sol_title: 'Specialized Sector Solutions',
      sol_subtitle: 'Tailored to the specific needs of educational institutions, enterprises, and clinical environments.',
      sol_s1_title: 'Education & Classrooms',
      sol_s1_prob: '<strong>The Challenge:</strong> Bullying happens in the shadows. Victims stay silent, while aggressors often project superficial popularity.',
      sol_s1_sol: '<strong>The NEXORD Solution:</strong> 3-minute radiography. Immediately pinpoints disconnected or at-risk students without direct interrogation.',
      sol_s1_b1: 'Early detection of subtle, silent isolation.',
      sol_s1_b2: 'Optimization of study groups and pedagogical seating.',
      sol_s1_b3: 'Total safeguard against stigmatizing any youth.',
      sol_s2_title: 'Enterprises & Teams',
      sol_s2_prob: '<strong>The Challenge:</strong> Formal organizational charts masking actual influence, departmental silos, and talent drain driven by relational burnout.',
      sol_s2_sol: '<strong>The NEXORD Solution:</strong> Identification of informal leadership, isolated cliques, and internal communication bottlenecks.',
      sol_s2_b1: 'Mapping genuine trust versus formal hierarchical authority.',
      sol_s2_b2: 'Agile onboarding and alignment in mergers, acquisitions, and restructuring.',
      sol_s2_b3: 'Expert forensic audit reports for executive boards.',
      sol_s3_title: 'Healthcare & Clinical Settings',
      sol_s3_prob: '<strong>The Challenge:</strong> Dialectical resistance, covert alliances, and undeclared friction in group therapy and mediation.',
      sol_s3_sol: '<strong>The NEXORD Solution:</strong> Longitudinal Moviola of micro-interactions. Measures session-by-session evolution of the therapeutic alliance.',
      sol_s3_b1: 'Reciprocity auditing in addiction and support groups.',
      sol_s3_b2: 'Longitudinal tracking of interpersonal cohesion.',
      sol_s3_b3: 'Individualized reflective feedback reinforcing engagement.',

      // Section 4: How It Works (3 Steps)
      flow_tag: 'Simple Operational Workflow',
      flow_title: 'From data collection to expert report in 3 steps',
      flow_subtitle: 'Designed for frictionless institutional deployment without technical overhead.',
      flow_s1_title: 'Brief Assessment (3 min)',
      flow_s1_desc: 'Each participant accesses via secure tokenized link on mobile or tablet. Rank peers visually without cognitive fatigue or intrusive questions.',
      flow_s2_title: 'Ingestion & SMIb Physics',
      flow_s2_desc: 'The VISORD engine instantaneously computes emission and reception dyadic matrices, decomposing relational densities across BDR and SDR.',
      flow_s3_title: '3D Digital Twin & Forensic Report',
      flow_s3_desc: 'Leadership receives a clear executive report accompanied by interactive 3D/4D visualizers and actionable immediate recommendations.',

      // Section 5: Ethical Safeguards
      ethics_heading: '<span>🛡️</span> Deontological Mandate',
      ethics_text_1: 'At NEXORD, relational science serves human flourishing exclusively. We adhere to the strictest <strong>Privacy by Design</strong> principles and the Principal Investigator\'s ethical pledge: <em>we identify strictly group thermodynamic phenomena, never intrinsic personality flaws</em>. Non-punitive data use is formally guaranteed to safeguard personal dignity and self-esteem.',
      ethics_text_2: '✓ GDPR Compliant &bull; End-to-end encryption &bull; Forensic purging of ephemeral data',
      ethics_btn: 'View Participant Portal ↗',

      // Section 6: Research Vault
      vault_tag: 'Research Vault',
      vault_title: 'Scientific Rigor & Documentation',
      vault_subtitle: 'For researchers, psychometricians, and technical auditors: open access to full mathematical architecture, manifesto, and formalization levels.',
      v_l1_title: 'Level 1: Intuitive',
      v_l1_desc: 'Group dynamic Moviola, micro-interactions, and particle animation.',
      v_l1_btn: 'Explore Level 1 →',
      v_l2_title: 'Level 2: Basic',
      v_l2_desc: 'Elementary adjacency matrices, dyadic reciprocity, and fundamental graphs.',
      v_l2_btn: 'Explore Level 2 →',
      v_l3_title: 'Level 3: SMIb Schema',
      v_l3_desc: 'Official 4-position tetragram: sender expectation, preference, and reception.',
      v_l3_btn: 'Explore Level 3 →',
      v_l4_title: 'Level 4: Applications',
      v_l4_desc: 'Forensic case studies solved across school, workplace, and clinical domains.',
      v_l4_btn: 'Explore Level 4 →',
      v_l5_title: 'Level 5: Mathematical',
      v_l5_desc: 'Grassmann manifolds Gr(k,N), Fiedler eigenvalues λ2, and tensor field physics.',
      v_l5_btn: 'Explore Level 5 →',
      v_l6_title: 'Level 6: Reports',
      v_l6_desc: 'High-fidelity socio-thermodynamic expert forensic report templates and generator.',
      v_l6_btn: 'Explore Level 6 →',
      v_l7_title: 'Level 7: Manifesto',
      v_l7_desc: '2026 Scientific Manifesto, Zenodo DOI, academic licensing, and bibliography.',
      v_l7_btn: 'Explore Level 7 →',
      v_glo_title: 'Official Glossary',
      v_glo_desc: 'Official normative dictionary of NEXORD terms, operators, and metrics.',
      v_glo_btn: 'Open Glossary →',

      // Section 7: Institutional Stewardship
      cust_tag: 'Technology Transfer & Open Science',
      cust_title: 'Call for Institutional Stewardship',
      cust_subtitle: 'We invite a university, supercomputing facility, or scientific institution to assume long-term technological stewardship and governance of the NEXORD / VISORD ecosystem.',
      cust_banner_title: 'OFFICIAL FRAMEWORK FOR INSTITUTIONAL STEWARDSHIP & SCIENTIFIC LEGACY',
      cust_banner_desc: 'Terms of university technology transfer: software endowment, honorary author advisory (3-5 years), ethical safeguards, and reversion clause (responsible stewardship, no blind assignment).',
      cust_banner_btn: 'View Stewardship Framework (PDF / Web) →',

      // What is NEXORD?
      what_title: 'WHAT IS NEXORD?',
      what_p1: '<strong>1.</strong> Scientific platform for computational ordinal sociometry and relational thermodynamics formalizing human collective microphysics via SMIb continuous dyadic matrices and Grassmann manifolds Gr(k, N).',
      what_p2: '<strong>2.</strong> Transcends traditional sociograms through an intuitive 3-minute completion and a 3D/4D engine (VISORD) revealing gravitational affinity basins, emergent leadership, and invisible ostracism in real time.',
      what_p3: '<strong>3.</strong> Engineered under the Hippocratic principle <em>primum non nocere</em>, translating bond energy into three decision tiers (Leadership, Dynamics, and Subject), guaranteeing blind anonymity and strictly formative, non-punitive use.',

      // Diptych: What is offered vs What is requested
      offer_title: 'WHAT IS OFFERED?',
      offer_lead: 'A comprehensive, operational, empirically validated scientific endowment ready for transfer:',
      offer_i1: '<strong style="color: #FFF;">Full Platform:</strong> Computational ordinal sociometry engines in Python and the 3D/4D VISORD visual ecosystem (D18 Aquarium, Dialectical, Cultural, and Demo Moviola).',
      offer_i2: '<strong style="color: #FFF;">Methodological Canon:</strong> Axiomatic formalization of the 4-position SMIb matrix (DA, RC, pDA, pRC), universal Q81 (9×9) lattice, BDR/SDR densities, and proven barycentric invariance.',
      offer_i3: '<strong style="color: #FFF;">Empirical Corpus (BSOC):</strong> Official Sociometric Database with standardized longitudinal series (real field matrices, Monte Carlo simulations, and cultural dramaturgy series).',
      offer_i4: '<strong style="color: #FFF;">Persistent Identifier &amp; DOI:</strong> Permanent record at CERN Zenodo (<a href="https://doi.org/10.5281/zenodo.23329641" target="_blank" rel="noopener" style="color: var(--neon-green); text-decoration: underline; font-weight:700;">DOI: 10.5281/zenodo.23329641</a>) indexed in Google Scholar, integrating the Official Edition of the Manifesto and its 6 bilingual technical annexes.',
      offer_i5: '<strong style="color: #FFF;">Open Science Community:</strong> Open methodology for interuniversity research in group psychology, relational sociology, and complex network science.',
      offer_i6: '<strong style="color: #FFF;">Universal Scope &amp; Multilingual Transfer:</strong> Platform certified in Spanish  and English for international research, with open architecture and languages for future localizations....',
      offer_note: '💡 Royalty-free transfer strictly for scientific and educational purposes.',

      req_title: 'WHAT IS REQUESTED FROM THE INSTITUTION?',
      req_lead: 'An institutional and technical framework ensuring sustainability, security, and systemic robustness:',
      req_i1: '<strong style="color: #FFF;">Institutional Stewardship &amp; Governance:</strong> Adoption by a university, academic chair, or research institute ensuring heritage preservation and academic continuity of the project.',
      req_i2: '<strong style="color: #FFF;">Controlled Access Infrastructure:</strong> Hosting on secure institutional servers or cloud ensuring high availability, audited backups, and strict European data sovereignty.',
      req_i3: '<strong style="color: #FFF;">Evolutionary Technical Maintenance:</strong> Technical supervision of dependencies (WebGL/Three.js, Python, modern web standards) and support for methodological updates.',
      req_i4: '<strong style="color: #FFF;">Credential Management &amp; Deontology:</strong> Provisioning, auditing, and revocation of credentials for accredited Principal Investigators (PIs), upholding deontological protocols.',
      req_note: '🏛️ Ideal for departments of Social Psychology, Quantitative Sociology, Data Science, or IT Centers.',

      // Technical & legal safeguards
      guard_title: 'EXISTING TECHNICAL & LEGAL SAFEGUARDS',
      guard_b1_title: '🔒 Privacy by Design (Q.GID / T1-T9)',
      guard_b1_desc: 'Mandatory official anonymization (1A..5A, 1B..5B), blind session tokens, absolute nominal dissociation, and mathematical secrecy of choices. Individual cross-identification is impossible.',
      guard_b2_title: '📜 Open License CC-BY-4.0',
      guard_b2_desc: 'Creative Commons Attribution 4.0 International License: freedom to share, adapt, and deploy for educational and research purposes while preserving original scientific authorship.',
      guard_b3_title: '🌐 CERN Zenodo Repository (Immutable)',
      guard_b3_desc: 'Persistent DOI <code style="color:var(--neon-green);">10.5281/zenodo.23329641</code> (Official Edition: Central Manifesto and Supplementary Material), with Highwire Press and Dublin Core scientific metadata archiving.',
      guard_b4_title: '🔍 Auditable &amp; Deterministic Code',
      guard_b4_desc: 'Verifiable mathematics (SVD decomposition, χ², Estrada communicability, Grassmann manifolds). Free from non-reproducible black-box heuristics.',
      guard_b5_title: '🌍 Universality &amp; Federated Nodes (UNESCO Open Science)',
      guard_b5_desc: 'Global Open Heritage. Safeguard clause preventing territorial or linguistic capture: decoupled architecture certified in Spanish and English, with languages for future localizations..., ensuring seamless replication and deployment across university networks across borders.',

      // Contact Form
      contact_tag: 'DIRECT CONTACT CHANNEL',
      contact_title: 'Propose Institutional Stewardship or Pilot Project',
      contact_subtitle: 'Submit your institutional proposal directly to the promoter team or copy the structured draft for rectoral or departmental processing.',
      contact_pi_label: 'LEAD RESEARCHER & PROMOTER:',
      contact_pi_sub: 'NEXORD Research Initiative · Independent Research',
      form_inst_label: 'Institution / University / Organization *',
      form_inst_ph: 'E.g., Complutense University / Research Institute...',
      form_rep_label: 'Representative Name / Title *',
      form_rep_ph: 'E.g., Dr. Jane Doe / Dean, Department Chair',
      form_email_label: 'Institutional Email *',
      form_type_label: 'Interest Track *',
      form_type_opt1: 'Permanent Institutional Stewardship & Governance',
      form_type_opt2: 'Secure Server Hosting & Infrastructure',
      form_type_opt3: 'Research Agreement & Methodology Adoption',
      form_type_opt4: 'International Federated Node / Linguistic Localization (RU, ZH, EN...)',
      form_type_opt5: 'Field Pilot Transfer Project',
      form_type_opt6: 'Other institutional proposal',
      form_msg_label: 'Message / Proposal Scope',
      form_msg_ph: 'Briefly outline your entity\'s interest, hosting capabilities, or proposed collaboration framework...',
      form_btn_pdf: '📄 View Official Framework (PDF)',
      form_btn_copy: '📋 Copy Draft to Clipboard',
      form_btn_send: '📤 Submit Proposal (Open Email)',

      // Final CTA Banner
      cta_title: 'Ready to see what others cannot see?',
      cta_subtitle: 'Discover how NEXORD elevates group cohesion, team performance, and proactive conflict prevention in your institution.',
      cta_btn_demos: '🚀 Launch 3D Demonstrations',
      cta_btn_custody: '🏛️ Institutional Stewardship Proposal',

      // Footer
      foot_inicio: 'Home',
      foot_custodia: 'Institutional Stewardship',
      foot_demo: 'VISORD Demo 3D',
      foot_cultural: 'VISORD Cultural',
      foot_acuario: 'VISORD Aquarium',
      foot_dialectico: 'VISORD Dialectical',
      foot_retorno: 'Participant Portal',
      foot_glosario: 'Official Glossary',
      foot_dial: 'Orbital Dial 3-6-9',
      foot_cite_btn: 'CITE WITH BibTeX',
      foot_platform_lead: '<strong>NEXORD / VISORD Engine</strong> &copy; 2026 &bull; Scientific Platform for Computational Ordinal Sociometry and Socio-Thermodynamic Diagnosis.',
      foot_open_science: 'Developed under the ethical mandate of Open Science. Punitive or defamatory data usage is strictly prohibited.',
      foot_lang_future: 'Languages for future localizations...',

      // Vertical Nav Band Tooltips
      vnav_tip_inicio: 'Home',
      vnav_tip_dolor: 'Why?',
      vnav_tip_showroom: '3D Jewels',
      vnav_tip_soluciones: 'Solutions',
      vnav_tip_etica: 'Ethics',
      vnav_tip_boveda: 'Science',
      vnav_tip_custodia: 'Custody',

      // Citation Modal
      modal_title: 'Official Academic Citation · NEXORD / VISORD Engine',
      modal_hint_bibtex: 'Entry for LaTeX, Overleaf, and compatible citation managers:',
      modal_link_manifesto_web: 'View Web Manifesto ↗',
      modal_link_supp: 'Supplementary Material (6 Docs) ↗',
      modal_link_summary_en: 'Summary EN (PDF) ↗',
      modal_link_man_es: 'Manifesto ES (PDF) ↗',
      modal_link_man_en: 'Manifesto EN (PDF) ↗',
      modal_link_zenodo: 'CERN Zenodo Repository ↗',
      modal_btn_copy: 'Copy to Clipboard',

      // Extras & Accessibility
      video_fallback: 'Your browser does not support the video tag.',
      brand_home_title: 'Return to NEXORD Welcome Portal',
      nav_dial_btn_title: 'Open Epistemological Orbital Dial (9 Sectors)',
      btn_lang_es_title: 'Spanish',
      btn_lang_en_title: 'English (International)',
      doi_license_title: 'Creative Commons Attribution 4.0 International',
      nav_main_aria: 'Main Navigation',
      video_hero_aria: 'Official VISORD 3D Demonstration',
      vnav_band_aria: 'Vertical section navigation',
      vnav_btn_up_title: 'Previous section (▲)',
      vnav_btn_up_aria: 'Go to previous section',
      vnav_btn_down_title: 'Next section (▼)',
      vnav_btn_down_aria: 'Go to next section',
      vnav_dots_aria: 'Section indicators',
      vnav_btn_dial_title: 'Open Epistemological Orbital Dial (9 Sectors)',
      vnav_btn_home_title: 'Return to NEXORD Welcome Portal (🏠)',
      vnav_dot_titles: ['1. Home / Hero', '2. Why NEXORD?', '3. 3D Jewels', '4. Solutions', '5. Ethical Guarantee', '6. Scientific Vault', '7. Institutional Stewardship'],
      modal_close_aria: 'Close',
      modal_link_man_web_title: 'Open Official Scientific Manifesto on the Web (Zero-Install, 29 Plates & Glossary)',
      modal_link_supp_title: 'View Supplementary Material & Technical Annexes (6 Documents)',
      modal_link_sum_en_title: 'Download Official Executive Summary (English Edition, PDF ~500 kB)',
      modal_link_man_es_title: 'Download Official Scientific Manifesto (Spanish Edition, PDF 58 MB)',
      modal_link_man_en_title: 'Download Official Scientific Manifesto (English Edition, PDF 58 MB)',
      modal_link_zenodo_title: 'View Official Record & Custody on CERN Zenodo (DOI: 10.5281/zenodo.23329641)'
    }
  };

  function setPromoLanguage(lang) {
    if (!PROMO_I18N[lang]) lang = 'es';
    try {
      localStorage.setItem('nexord_lang', lang);
    } catch (e) {}

    document.documentElement.lang = lang;
    const dict = PROMO_I18N[lang];
    if (!dict) return;

    // Helper functions for safe DOM updates without crashing
    function safeText(el, val) {
      if (el && val !== undefined) el.textContent = val;
    }
    function safeHTML(el, val) {
      if (el && val !== undefined) el.innerHTML = val;
    }
    function safeAttr(el, attr, val) {
      if (el && val !== undefined) el.setAttribute(attr, val);
    }

    // 0. ACTUALIZAR DE INMEDIATO LOS BOTONES DE IDIOMA EN LA CABECERA
    try {
      const btnEs = document.getElementById('btn-promo-lang-es');
      const btnEn = document.getElementById('btn-promo-lang-en');
      if (btnEs) {
        btnEs.style.color = (lang === 'es') ? 'var(--neon-green)' : '#94A3B8';
        btnEs.style.fontWeight = (lang === 'es') ? '800' : '700';
        btnEs.classList.toggle('active', lang === 'es');
        if (dict.btn_lang_es_title) btnEs.setAttribute('title', dict.btn_lang_es_title);
      }
      if (btnEn) {
        btnEn.style.color = (lang === 'en') ? 'var(--neon-green)' : '#94A3B8';
        btnEn.style.fontWeight = (lang === 'en') ? '800' : '700';
        btnEn.classList.toggle('active', lang === 'en');
        if (dict.btn_lang_en_title) btnEn.setAttribute('title', dict.btn_lang_en_title);
      }
    } catch (e) {
      console.warn("i18n buttons error:", e);
    }

    // Page title & meta
    try {
      if (dict.page_title) document.title = dict.page_title;
      const metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc && dict.meta_desc) metaDesc.setAttribute('content', dict.meta_desc);
    } catch (e) {}

    // 1. NAVBAR
    try {
      const sub = document.querySelector('nav .brand-sub');
      if (sub && dict.nav_brand_sub) sub.textContent = dict.nav_brand_sub;

      const navWhy = document.querySelector('nav a[href="#dolor"]');
      if (navWhy && dict.nav_why) navWhy.textContent = dict.nav_why;
      const navShow = document.querySelector('nav a[href="#showroom"]');
      if (navShow && dict.nav_showroom) navShow.textContent = dict.nav_showroom;
      const navSol = document.querySelector('nav a[href="#soluciones"]');
      if (navSol && dict.nav_solutions) navSol.textContent = dict.nav_solutions;
      const navEth = document.querySelector('nav a[href="#etica"]');
      if (navEth && dict.nav_ethics) navEth.textContent = dict.nav_ethics;
      const navDial = document.querySelector('nav a[href="dial_orbital.html"]');
      if (navDial && dict.nav_dial) navDial.textContent = dict.nav_dial;
      const navSci = document.querySelector('nav a[href="#boveda"]');
      if (navSci && dict.nav_science) navSci.textContent = dict.nav_science;
      const navCust = document.querySelector('nav a[href="#custodia"]');
      if (navCust && dict.nav_custody) navCust.textContent = dict.nav_custody;
      const navCta = document.querySelector('nav .nav-cta');
      if (navCta && dict.nav_cta) navCta.textContent = dict.nav_cta;

      const brandLink = document.querySelector('a.brand');
      if (brandLink && dict.brand_home_title) brandLink.setAttribute('title', dict.brand_home_title);

      const navDialBtn = document.querySelector('a.nav-dial-btn');
      if (navDialBtn && dict.nav_dial_btn_title) navDialBtn.setAttribute('title', dict.nav_dial_btn_title);

      const mainNav = document.querySelector('nav[aria-label]');
      if (mainNav && dict.nav_main_aria) mainNav.setAttribute('aria-label', dict.nav_main_aria);

      const dropItems = document.querySelectorAll('.dropdown-menu .dropdown-item');
      if (dropItems && dropItems.length >= 11) {
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
    } catch (e) {}

    // 2. HERO
    try {
      const heroPill = document.querySelector('.hero-pill');
      if (heroPill && dict.hero_pill) heroPill.innerHTML = '<span class="hero-pill-dot"></span>' + dict.hero_pill;
      const heroTitle = document.querySelector('.hero-title');
      if (heroTitle && dict.hero_title) heroTitle.innerHTML = dict.hero_title;
      const heroSubtitle = document.querySelector('.hero-subtitle');
      if (heroSubtitle && dict.hero_subtitle) heroSubtitle.textContent = dict.hero_subtitle;

      const heroBtnDial = document.querySelector('.hero-actions a[href="dial_orbital.html"] span');
      if (heroBtnDial) heroBtnDial.textContent = dict.hero_btn_dial || '🧭 Dial Orbital';
      const heroBtnMan = document.querySelector('.hero-actions a.btn-manifiesto span');
      if (heroBtnMan) heroBtnMan.textContent = dict.hero_btn_manifesto || '📜 Manifiesto Global (HTML)';
      const heroBtnCust = document.querySelector('.hero-actions a[href="#custodia"] span');
      if (heroBtnCust) heroBtnCust.textContent = dict.hero_btn_custody || '🏛️ Custodia Institucional';
      const heroBtn3d = document.querySelector('.hero-actions .btn-primary span');
      if (heroBtn3d && !heroBtnDial) heroBtn3d.textContent = dict.hero_btn_3d;
      const heroBtnSol = document.querySelector('.hero-actions a[href="#soluciones"] span');
      if (heroBtnSol) heroBtnSol.textContent = dict.hero_btn_solutions;

      const statusPillText = document.getElementById('lbl-status-pill');
      if (statusPillText) {
        const vid = document.getElementById('hero-master-video');
        const isMuted = vid ? (vid.muted || vid.volume === 0) : false;
        if (isMuted) {
          statusPillText.textContent = (lang === 'en') ? 'VISORD 3D · MUTED' : 'VISORD 3D · SILENCIADO';
        } else {
          statusPillText.textContent = (lang === 'en') ? 'VISORD 3D · AUDIO ACTIVE' : 'VISORD 3D · AUDIO ACTIVADO';
        }
      }

      // Video Hero HUD & Controls
      const vHeroBlock = document.getElementById('video-hero-block');
      if (vHeroBlock && dict.video_hero_aria) vHeroBlock.setAttribute('aria-label', dict.video_hero_aria);

      const vFb = document.getElementById('video-fallback-msg');
      if (vFb && dict.video_fallback) vFb.textContent = dict.video_fallback;

      const vBadge = document.querySelector('.video-hero-badge span:last-child');
      if (vBadge && dict.video_badge) vBadge.textContent = dict.video_badge;
      const vMeta = document.querySelector('.video-hero-meta span');
      if (vMeta && dict.video_meta) vMeta.textContent = dict.video_meta;

      const vPlayLabel = document.getElementById('video-play-label');
      if (vPlayLabel) {
        const vid = document.getElementById('hero-master-video');
        if (vid && !vid.paused && !vid.ended) {
          vPlayLabel.textContent = dict.video_btn_play || 'Pausa';
        } else if (vid && vid.ended) {
          vPlayLabel.textContent = dict.video_btn_repeat || 'Repetir';
        } else {
          vPlayLabel.textContent = dict.video_btn_play_pause || 'Play';
        }
      }
      const vAudioLabel = document.getElementById('video-audio-label');
      if (vAudioLabel) {
        const vid = document.getElementById('hero-master-video');
        const isMuted = vid ? (vid.muted || vid.volume === 0) : false;
        vAudioLabel.textContent = isMuted ? (dict.video_btn_audio_on || 'Activar Audio') : (dict.video_btn_audio_off || 'Audio Activado');
      }
      const vFsBtn = document.querySelector('#btn-video-fs span:last-child');
      if (vFsBtn && dict.video_btn_fs) vFsBtn.textContent = dict.video_btn_fs;

      const heroWrap = document.getElementById('hero-player-wrap');
      if (heroWrap && dict.video_player_title) heroWrap.setAttribute('title', dict.video_player_title);
      const btnPlayEl = document.getElementById('btn-video-play');
      if (btnPlayEl && dict.video_btn_play_title) btnPlayEl.setAttribute('title', dict.video_btn_play_title);
      const btnAudioEl = document.getElementById('btn-video-audio');
      if (btnAudioEl && dict.video_btn_audio_title) btnAudioEl.setAttribute('title', dict.video_btn_audio_title);
      const btnFsEl = document.getElementById('btn-video-fs');
      if (btnFsEl && dict.video_btn_fs_title) btnFsEl.setAttribute('title', dict.video_btn_fs_title);

      const bondPills = document.querySelectorAll('.video-bonds-decoder-hud .bond-pill');
      if (bondPills && bondPills.length >= 3) {
        bondPills[0].innerHTML = '<span class="bond-dot dot-green"></span><strong class="bond-term">' + dict.bond_attraction_term + '</strong> ' + dict.bond_attraction_text;
        bondPills[1].innerHTML = '<span class="bond-dot dot-magenta"></span><strong class="bond-term">' + dict.bond_rejection_term + '</strong> ' + dict.bond_rejection_text;
        bondPills[2].innerHTML = '<span class="bond-dot dot-ostracism"></span><strong class="bond-term">' + dict.bond_ostracism_term + '</strong> ' + dict.bond_ostracism_text;
      }

      const vSubText = document.getElementById('hero-subtitles-text');
      if (vSubText && !vSubText.getAttribute('data-dynamic') && dict.video_sub_initial) vSubText.textContent = dict.video_sub_initial;
      const vCtaPill = document.querySelector('.video-cta-pill span:first-child');
      if (vCtaPill && dict.video_cta_pill) vCtaPill.textContent = dict.video_cta_pill;
    } catch (e) {}

    // 3. ANATOMÍA DE LOS VÍNCULOS GRUPALES
    try {
      const bTag = document.querySelector('#vinculos-insight .bonds-tag, .bonds-anatomy-section .section-tag');
      if (bTag && dict.bonds_tag) bTag.textContent = dict.bonds_tag;
      const bTitle = document.querySelector('#vinculos-insight .bonds-title, .bonds-anatomy-section .section-title');
      if (bTitle && dict.bonds_title) bTitle.textContent = dict.bonds_title;
      const bSub = document.querySelector('#vinculos-insight .bonds-subtitle, .bonds-anatomy-section .section-subtitle');
      if (bSub && dict.bonds_subtitle) bSub.textContent = dict.bonds_subtitle;

      const cardAttr = document.querySelector('.bond-insight-card.card-attraction');
      if (cardAttr) {
        safeText(cardAttr.querySelector('.bond-card-badge'), dict.bond_c1_badge);
        safeText(cardAttr.querySelector('.bond-card-title'), dict.bond_c1_title);
        safeHTML(cardAttr.querySelector('.bond-card-text'), dict.bond_c1_text);
        safeText(cardAttr.querySelector('.metric-label'), dict.bond_c1_metric_label);
        safeText(cardAttr.querySelector('.metric-val'), dict.bond_c1_metric_val);
      }
      const cardRej = document.querySelector('.bond-insight-card.card-rejection');
      if (cardRej) {
        safeText(cardRej.querySelector('.bond-card-badge'), dict.bond_c2_badge);
        safeText(cardRej.querySelector('.bond-card-title'), dict.bond_c2_title);
        safeHTML(cardRej.querySelector('.bond-card-text'), dict.bond_c2_text);
        safeText(cardRej.querySelector('.metric-label'), dict.bond_c2_metric_label);
        safeText(cardRej.querySelector('.metric-val'), dict.bond_c2_metric_val);
      }
      const cardOst = document.querySelector('.bond-insight-card.card-ostracism');
      if (cardOst) {
        safeText(cardOst.querySelector('.bond-card-badge'), dict.bond_c3_badge);
        safeText(cardOst.querySelector('.bond-card-title'), dict.bond_c3_title);
        safeHTML(cardOst.querySelector('.bond-card-text'), dict.bond_c3_text);
        safeText(cardOst.querySelector('.metric-label'), dict.bond_c3_metric_label);
        safeText(cardOst.querySelector('.metric-val'), dict.bond_c3_metric_val);
      }
    } catch (e) {}

    // 4. MÉTRICAS RÁPIDAS HERO
    try {
      const statCards = document.querySelectorAll('.hero-stats-grid .stat-card, .hero-stats-band .stat-card');
      if (statCards && statCards.length >= 4) {
        safeText(statCards[0].querySelector('.stat-number'), dict.hero_stat_1_val);
        safeText(statCards[0].querySelector('.stat-desc'), dict.hero_stat_1_desc);

        safeText(statCards[1].querySelector('.stat-number'), dict.hero_stat_2_val);
        safeText(statCards[1].querySelector('.stat-desc'), dict.hero_stat_2_desc);

        safeText(statCards[2].querySelector('.stat-number'), dict.hero_stat_3_val);
        safeText(statCards[2].querySelector('.stat-desc'), dict.hero_stat_3_desc);

        safeText(statCards[3].querySelector('.stat-number'), dict.hero_stat_4_val);
        safeText(statCards[3].querySelector('.stat-desc'), dict.hero_stat_4_desc);
      }
    } catch (e) {}

    // 5. SECCIÓN 1: EL DOLOR INVISIBLE (#dolor)
    try {
      const dTag = document.querySelector('#dolor .section-tag');
      if (dTag && dict.pain_tag) dTag.textContent = dict.pain_tag;
      const dTitle = document.querySelector('#dolor .section-title');
      if (dTitle && dict.pain_title) dTitle.textContent = dict.pain_title;
      const dSub = document.querySelector('#dolor .section-subtitle');
      if (dSub && dict.pain_subtitle) dSub.textContent = dict.pain_subtitle;

      const cardTrad = document.querySelector('.comparison-card.traditional');
      if (cardTrad) {
        safeText(cardTrad.querySelector('.card-badge'), dict.pain_trad_badge);
        safeText(cardTrad.querySelector('.card-heading'), dict.pain_trad_heading);
        const tradItems = cardTrad.querySelectorAll('.feature-item div');
        if (tradItems.length >= 4) {
          safeHTML(tradItems[0], dict.pain_trad_item1);
          safeHTML(tradItems[1], dict.pain_trad_item2);
          safeHTML(tradItems[2], dict.pain_trad_item3);
          safeHTML(tradItems[3], dict.pain_trad_item4);
        }
      }

      const cardNex = document.querySelector('.comparison-card.nexord');
      if (cardNex) {
        safeText(cardNex.querySelector('.card-badge'), dict.pain_nex_badge);
        safeText(cardNex.querySelector('.card-heading'), dict.pain_nex_heading);
        const nexItems = cardNex.querySelectorAll('.feature-item div');
        if (nexItems.length >= 4) {
          safeHTML(nexItems[0], dict.pain_nex_item1);
          safeHTML(nexItems[1], dict.pain_nex_item2);
          safeHTML(nexItems[2], dict.pain_nex_item3);
          safeHTML(nexItems[3], dict.pain_nex_item4);
        }
      }
    } catch (e) {}

    // 6. SECCIÓN 2: SHOWROOM INTERACTIVO (#showroom)
    try {
      const sTag = document.querySelector('#showroom .section-tag');
      if (sTag && dict.show_tag) sTag.textContent = dict.show_tag;
      const sTitle = document.querySelector('#showroom .section-title');
      if (sTitle && dict.show_title) sTitle.textContent = dict.show_title;
      const sSub = document.querySelector('#showroom .section-subtitle');
      if (sSub && dict.show_subtitle) sSub.textContent = dict.show_subtitle;

      const jewelCards = document.querySelectorAll('#showroom .jewel-card');
      if (jewelCards.length >= 4) {
        safeText(jewelCards[0].querySelector('.jewel-title'), dict.jewel_1_title);
        safeText(jewelCards[0].querySelector('.jewel-subtitle'), dict.jewel_1_subtitle);
        safeHTML(jewelCards[0].querySelector('.jewel-desc'), dict.jewel_1_desc);
        safeText(jewelCards[0].querySelector('.btn-jewel'), dict.jewel_1_btn);

        safeText(jewelCards[1].querySelector('.jewel-title'), dict.jewel_2_title);
        safeText(jewelCards[1].querySelector('.jewel-subtitle'), dict.jewel_2_subtitle);
        safeHTML(jewelCards[1].querySelector('.jewel-desc'), dict.jewel_2_desc);
        safeText(jewelCards[1].querySelector('.btn-jewel'), dict.jewel_2_btn);

        safeText(jewelCards[2].querySelector('.jewel-title'), dict.jewel_3_title);
        safeText(jewelCards[2].querySelector('.jewel-subtitle'), dict.jewel_3_subtitle);
        safeHTML(jewelCards[2].querySelector('.jewel-desc'), dict.jewel_3_desc);
        safeText(jewelCards[2].querySelector('.btn-jewel'), dict.jewel_3_btn);

        safeText(jewelCards[3].querySelector('.jewel-title'), dict.jewel_4_title);
        safeText(jewelCards[3].querySelector('.jewel-subtitle'), dict.jewel_4_subtitle);
        safeHTML(jewelCards[3].querySelector('.jewel-desc'), dict.jewel_4_desc);
        safeText(jewelCards[3].querySelector('.btn-jewel'), dict.jewel_4_btn);
      }
    } catch (e) {}

    // 7. SECCIÓN 3: SOLUCIONES SECTORIALES (#soluciones)
    try {
      const solTag = document.querySelector('#soluciones .section-tag');
      if (solTag && dict.sol_tag) solTag.textContent = dict.sol_tag;
      const solTitle = document.querySelector('#soluciones .section-title');
      if (solTitle && dict.sol_title) solTitle.textContent = dict.sol_title;
      const solSub = document.querySelector('#soluciones .section-subtitle');
      if (solSub && dict.sol_subtitle) solSub.textContent = dict.sol_subtitle;

      const sectorCards = document.querySelectorAll('#soluciones .sector-card');
      if (sectorCards.length >= 3) {
        safeText(sectorCards[0].querySelector('.sector-name'), dict.sol_s1_title);
        safeHTML(sectorCards[0].querySelector('.sector-problem'), dict.sol_s1_prob);
        safeHTML(sectorCards[0].querySelector('.sector-solution'), dict.sol_s1_sol);
        const b1 = sectorCards[0].querySelectorAll('.sector-bullets li');
        if (b1.length >= 3) {
          safeText(b1[0], dict.sol_s1_b1);
          safeText(b1[1], dict.sol_s1_b2);
          safeText(b1[2], dict.sol_s1_b3);
        }

        safeText(sectorCards[1].querySelector('.sector-name'), dict.sol_s2_title);
        safeHTML(sectorCards[1].querySelector('.sector-problem'), dict.sol_s2_prob);
        safeHTML(sectorCards[1].querySelector('.sector-solution'), dict.sol_s2_sol);
        const b2 = sectorCards[1].querySelectorAll('.sector-bullets li');
        if (b2.length >= 3) {
          safeText(b2[0], dict.sol_s2_b1);
          safeText(b2[1], dict.sol_s2_b2);
          safeText(b2[2], dict.sol_s2_b3);
        }

        safeText(sectorCards[2].querySelector('.sector-name'), dict.sol_s3_title);
        safeHTML(sectorCards[2].querySelector('.sector-problem'), dict.sol_s3_prob);
        safeHTML(sectorCards[2].querySelector('.sector-solution'), dict.sol_s3_sol);
        const b3 = sectorCards[2].querySelectorAll('.sector-bullets li');
        if (b3.length >= 3) {
          safeText(b3[0], dict.sol_s3_b1);
          safeText(b3[1], dict.sol_s3_b2);
          safeText(b3[2], dict.sol_s3_b3);
        }
      }
    } catch (e) {}

    // 8. SECCIÓN 4: CÓMO FUNCIONA (#como-funciona)
    try {
      const fTag = document.querySelector('#como-funciona .section-tag');
      if (fTag && dict.flow_tag) fTag.textContent = dict.flow_tag;
      const fTitle = document.querySelector('#como-funciona .section-title');
      if (fTitle && dict.flow_title) fTitle.textContent = dict.flow_title;
      const fSub = document.querySelector('#como-funciona .section-subtitle');
      if (fSub && dict.flow_subtitle) fSub.textContent = dict.flow_subtitle;

      const stepCards = document.querySelectorAll('#como-funciona .step-card');
      if (stepCards.length >= 3) {
        safeText(stepCards[0].querySelector('.step-title'), dict.flow_s1_title);
        safeText(stepCards[0].querySelector('.step-desc'), dict.flow_s1_desc);

        safeText(stepCards[1].querySelector('.step-title'), dict.flow_s2_title);
        safeText(stepCards[1].querySelector('.step-desc'), dict.flow_s2_desc);

        safeText(stepCards[2].querySelector('.step-title'), dict.flow_s3_title);
        safeText(stepCards[2].querySelector('.step-desc'), dict.flow_s3_desc);
      }
    } catch (e) {}

    // 9. SECCIÓN 5: GARANTÍA ÉTICA (#etica)
    try {
      const eTag = document.querySelector('#etica .section-tag');
      if (eTag && dict.ethics_tag) eTag.textContent = dict.ethics_tag;
      const eTitle = document.querySelector('#etica .section-title');
      if (eTitle && dict.ethics_title) eTitle.textContent = dict.ethics_title;
      const eSub = document.querySelector('#etica .section-subtitle');
      if (eSub && dict.ethics_subtitle) eSub.textContent = dict.ethics_subtitle;

      const eHead = document.querySelector('#etica .ethics-heading');
      if (eHead && dict.ethics_heading) eHead.innerHTML = dict.ethics_heading;
      const eTexts = document.querySelectorAll('#etica .ethics-text');
      if (eTexts.length >= 2) {
        safeHTML(eTexts[0], dict.ethics_text_1);
        safeHTML(eTexts[1], dict.ethics_text_2);
      }
      const eCta = document.querySelector('#etica .ethics-cta a');
      if (eCta && dict.ethics_btn) eCta.textContent = dict.ethics_btn;
    } catch (e) {}

    // 10. SECCIÓN 6: BÓVEDA CIENTÍFICA (#boveda)
    try {
      const bTag = document.querySelector('#boveda .section-tag');
      if (bTag && dict.vault_tag) bTag.textContent = dict.vault_tag;
      const bTitle = document.querySelector('#boveda .section-title');
      if (bTitle && dict.vault_title) bTitle.textContent = dict.vault_title;
      const bSub = document.querySelector('#boveda .section-subtitle');
      if (bSub && dict.vault_subtitle) bSub.textContent = dict.vault_subtitle;

      const vaultCards = document.querySelectorAll('#boveda .vault-card');
      if (vaultCards.length >= 8) {
        const vMap = [
          { t: dict.v_l1_title, d: dict.v_l1_desc, a: dict.v_l1_btn },
          { t: dict.v_l2_title, d: dict.v_l2_desc, a: dict.v_l2_btn },
          { t: dict.v_l3_title, d: dict.v_l3_desc, a: dict.v_l3_btn },
          { t: dict.v_l4_title, d: dict.v_l4_desc, a: dict.v_l4_btn },
          { t: dict.v_l5_title, d: dict.v_l5_desc, a: dict.v_l5_btn },
          { t: dict.v_l6_title, d: dict.v_l6_desc, a: dict.v_l6_btn },
          { t: dict.v_l7_title, d: dict.v_l7_desc, a: dict.v_l7_btn },
          { t: dict.v_glo_title, d: dict.v_glo_desc, a: dict.v_glo_btn }
        ];
        vaultCards.forEach((vc, idx) => {
          if (vMap[idx]) {
            safeText(vc.querySelector('.vault-card-title'), vMap[idx].t);
            safeText(vc.querySelector('.vault-card-desc'), vMap[idx].d);
            safeText(vc.querySelector('.vault-card-arrow'), vMap[idx].a);
          }
        });
      }
    } catch (e) {}

    // 11. SECCIÓN 7: CUSTODIA INSTITUCIONAL (#custodia)
    try {
      const cTag = document.querySelector('#custodia .section-tag');
      if (cTag && dict.cust_tag) cTag.textContent = dict.cust_tag;
      const cTitle = document.querySelector('#custodia .section-title');
      if (cTitle && dict.cust_title) cTitle.textContent = dict.cust_title;
      const cSub = document.querySelector('#custodia .section-subtitle');
      if (cSub && dict.cust_subtitle) cSub.textContent = dict.cust_subtitle;

      // Banner marco oficial
      const mBanner = document.getElementById('custodia-marco-banner');
      if (mBanner) {
        safeText(mBanner.querySelector('h3'), dict.cust_banner_title);
        safeText(mBanner.querySelector('p'), dict.cust_banner_desc);
        safeText(mBanner.querySelector('a span:last-child'), dict.cust_banner_btn);
      }

      // Qué es NEXORD
      const qBlock = document.getElementById('que-es-nexord-block');
      if (qBlock) {
        safeText(qBlock.querySelector('h3'), dict.what_title);
        const qPs = qBlock.querySelectorAll('p');
        if (qPs.length >= 3) {
          safeHTML(qPs[0], dict.what_p1);
          safeHTML(qPs[1], dict.what_p2);
          safeHTML(qPs[2], dict.what_p3);
        }
      }

      // Díptico: Ofrece
      const ofBlock = document.getElementById('custodia-diptico-ofrece');
      if (ofBlock) {
        safeText(ofBlock.querySelector('h3'), dict.offer_title);
        safeText(ofBlock.querySelector('p'), dict.offer_lead);
        const ofLis = ofBlock.querySelectorAll('ul li div');
        if (ofLis.length >= 5) {
          safeHTML(ofLis[0], dict.offer_i1);
          safeHTML(ofLis[1], dict.offer_i2);
          safeHTML(ofLis[2], dict.offer_i3);
          safeHTML(ofLis[3], dict.offer_i4);
          safeHTML(ofLis[4], dict.offer_i5);
        }
        const ofNote = ofBlock.querySelector('div[style*="dashed"]');
        if (ofNote && dict.offer_note) ofNote.textContent = dict.offer_note;
      }

      // Díptico: Pide
      const reqBlock = document.getElementById('custodia-diptico-pide');
      if (reqBlock) {
        safeText(reqBlock.querySelector('h3'), dict.req_title);
        safeText(reqBlock.querySelector('p'), dict.req_lead);
        const reqLis = reqBlock.querySelectorAll('ul li div');
        if (reqLis.length >= 4) {
          safeHTML(reqLis[0], dict.req_i1);
          safeHTML(reqLis[1], dict.req_i2);
          safeHTML(reqLis[2], dict.req_i3);
          safeHTML(reqLis[3], dict.req_i4);
        }
        const reqNote = reqBlock.querySelector('div[style*="dashed"]');
        if (reqNote && dict.req_note) reqNote.textContent = dict.req_note;
      }

      // Garantías existentes
      const garBlock = document.getElementById('custodia-garantias-block');
      if (garBlock) {
        safeText(garBlock.querySelector('h3'), dict.guard_title);
        const gCards = garBlock.querySelectorAll('div[style*="padding: 16px"]');
        if (gCards.length >= 5) {
          safeText(gCards[0].children[0], dict.guard_b1_title);
          safeText(gCards[0].children[1], dict.guard_b1_desc);

          safeText(gCards[1].children[0], dict.guard_b2_title);
          safeText(gCards[1].children[1], dict.guard_b2_desc);

          safeHTML(gCards[2].children[0], dict.guard_b3_title);
          safeHTML(gCards[2].children[1], dict.guard_b3_desc);

          safeText(gCards[3].children[0], dict.guard_b4_title);
          safeText(gCards[3].children[1], dict.guard_b4_desc);

          safeText(gCards[4].children[0], dict.guard_b5_title);
          safeText(gCards[4].children[1], dict.guard_b5_desc);
        }
      }

      // Formulario y contacto
      const cWrap = document.getElementById('custodia-contact-wrap');
      if (cWrap) {
        const cTagF = cWrap.querySelector('div[style*="color: var(--neon-green)"]');
        if (cTagF && dict.contact_tag) cTagF.textContent = dict.contact_tag;
        const cTitleF = cWrap.querySelector('h3');
        if (cTitleF && dict.contact_title) cTitleF.textContent = dict.contact_title;
        const cSubF = cWrap.querySelector('p');
        if (cSubF && dict.contact_subtitle) cSubF.textContent = dict.contact_subtitle;
      }

      const btnPdf = document.querySelector('#custodia-contact-form a.btn-secondary');
      if (btnPdf && dict.form_btn_pdf) btnPdf.textContent = dict.form_btn_pdf;
      const btnCopyDraft = document.querySelector('#custodia-contact-form button[type="button"]');
      if (btnCopyDraft && dict.form_btn_copy) btnCopyDraft.textContent = dict.form_btn_copy;
      const btnSubmitProposal = document.querySelector('#custodia-contact-form button[type="submit"]');
      if (btnSubmitProposal && dict.form_btn_send) btnSubmitProposal.textContent = dict.form_btn_send;
    } catch (e) {}

    // 12. FOOTER
    try {
      const fLinks = document.querySelectorAll('.footer-links a');
      if (fLinks && fLinks.length >= 8) {
        safeText(fLinks[0], dict.foot_inicio);
        safeText(fLinks[1], dict.foot_custodia);
        safeText(fLinks[2], dict.foot_demo);
        safeText(fLinks[3], dict.foot_cultural);
        safeText(fLinks[4], dict.foot_acuario);
        safeText(fLinks[5], dict.foot_dialectico);
        safeText(fLinks[6], dict.foot_retorno);
        safeText(fLinks[7], dict.foot_glosario);
      }
    } catch (e) {}

    // 13. MODAL DE CITACIÓN
    try {
      const mTitle = document.querySelector('#modal-bibtex h3');
      if (mTitle && dict.modal_title) mTitle.innerHTML = '<span>📑</span> ' + dict.modal_title;
      const mHint = document.getElementById('modal-bibtex-hint');
      if (mHint && dict.modal_hint_bibtex) mHint.textContent = dict.modal_hint_bibtex;
      const mBtnCopy = document.getElementById('btn-copy-citation');
      if (mBtnCopy && dict.modal_btn_copy) mBtnCopy.textContent = dict.modal_btn_copy;
    } catch (e) {}

    // Notificar al ecosistema
    try {
      window.dispatchEvent(new CustomEvent('nexordLangChanged', { detail: { lang: lang } }));
    } catch (e) {}
  }

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
