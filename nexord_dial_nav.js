/**
 * =============================================================================
 * NEXORD PLATFORM · PERSISTENT GLOBAL NAVIGATION & ZENITH DIAL (SCHEMA ENGINE)
 * Motor universal de barra persistente superior, breadcrumbs y Dial 3-6-9
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

  // Definición canónica de los 9 sectores del Dial (3-6-9)
  // idx 0 es Nivel 9 (Cenit a 0° / 12 en punto), luego 1..8 en sentido horario (40° cada sector)
  const DIAL_SECTORS = [
    {
      idx: 0,
      num: "9",
      short: "FUN",
      title: "Nivel 9: Fundamentos",
      badge: "NIVEL 9 • CENIT EPISTEMOLÓGICO (CANON 3-6-9)",
      subtitle: "Física de Grupos & Urdimbre Vital",
      desc: "Hacia una física de lo grupal: urdimbre vital, vectores DAR+RECIBIR, equilibrio homeostático, Sociometría Sintética in silico y rigor científico.",
      url: rootPrefix + "fundamentos.html",
      key: "fundamentos",
      color: "#00FF87",
      is369: true
    },
    {
      idx: 1,
      num: "1",
      short: "INT",
      title: "Nivel 1: Intuitivo",
      badge: "NIVEL 1 • ENTRADA VISUAL",
      subtitle: "Moviola 3D & Densidad Bruta",
      desc: "Simulación de partículas dinámicas, fluidos relacionales y balance de atracción/rechazo sin estrés evaluativo.",
      url: rootPrefix + "nivel1_intuitivo.html",
      key: "nivel1",
      color: "#38BDF8",
      is369: false
    },
    {
      idx: 2,
      num: "2",
      short: "BÁS",
      title: "Nivel 2: Básico",
      badge: "NIVEL 2 • ÁTOMO RELACIONAL",
      subtitle: "Matrices SMIa / SMIb",
      desc: "Transición fundamental de la sociometría tradicional a matrices de preferencia ordinal con metapercepción cruzada.",
      url: rootPrefix + "nivel2_basico.html",
      key: "nivel2",
      color: "#48CAE4",
      is369: false
    },
    {
      idx: 3,
      num: "3",
      short: "ESQ",
      title: "Nivel 3: Esquema",
      badge: "NIVEL 3 • ESTRUCTURA FORMAL (CANON 3-6-9)",
      subtitle: "81 Figuras Sociométricas",
      desc: "El invariante universal Q81: ordenación formal, topología de roles diádicos y partición canónica en 5 zonas.",
      url: rootPrefix + "nivel3_esquema.html",
      key: "nivel3",
      color: "#FFE600",
      is369: true
    },
    {
      idx: 4,
      num: "4",
      short: "APL",
      title: "Nivel 4: Aplicaciones",
      badge: "NIVEL 4 • VIDA GRUPAL & CASOS",
      subtitle: "Casos Sectoriales & Forenses",
      desc: "Soluciones de campo: convivencia escolar, equipos de alto rendimiento corporativo y mediación clínica.",
      url: rootPrefix + "nivel4_aplicaciones.html",
      key: "nivel4",
      color: "#FF9F1C",
      is369: false
    },
    {
      idx: 5,
      num: "5",
      short: "MAT",
      title: "Nivel 5: Matemático",
      badge: "NIVEL 5 • ÁLGEBRA TENSORIAL",
      subtitle: "Grassmann Gr(k, N) & Fiedler",
      desc: "Geometría diferencial, autovalores del Laplaciano grafal, frustración estructural de Heider y entropía grupal.",
      url: rootPrefix + "nivel5_matematico.html",
      key: "nivel5",
      color: "#BF5AF2",
      is369: false
    },
    {
      idx: 6,
      num: "6",
      short: "INF",
      title: "Nivel 6: Informes",
      badge: "NIVEL 6 • DIAGNÓSTICO PERICIAL (CANON 3-6-9)",
      subtitle: "Diagnóstico Pericial Forense",
      desc: "Generación automatizada de informes periciales objetivos, mapas de calor relacional y planes no punitivos.",
      url: rootPrefix + "nivel6_informes.html",
      key: "nivel6",
      color: "#FF007F",
      is369: true
    },
    {
      idx: 7,
      num: "7",
      short: "DOC",
      title: "Nivel 7: Documentación",
      badge: "NIVEL 7 • DEONTOLOGÍA & ZENODO",
      subtitle: "Manifiesto Zenodo & DOI",
      desc: "Depósito científico abierto en CERN Zenodo, manuales de codificación, citación formal BibTeX/APA y licencias.",
      url: rootPrefix + "nivel7_documentacion.html",
      key: "nivel7",
      color: "#E0AAFF",
      is369: false
    },
    {
      idx: 8,
      num: "8",
      short: "REC",
      title: "Nivel 8: Recursos",
      badge: "NIVEL 8 • EXPERIENCIA VISORD",
      subtitle: "Experiencia VISORD (4 Entornos)",
      desc: "Entornos interactivos: VISORD_demo (Nivel 8), VISORD_cultural, VISORD_radiológico y VISORD_dialéctico.",
      url: rootPrefix + "recursos.html",
      key: "recursos",
      color: "#00F0FF",
      is369: false
    }
  ];

  // Identificar el nivel activo según la página actual
  let activeKey = '';
  let currentBreadcrumbName = 'NEXORD';

  if (filename.includes('nivel1')) { activeKey = 'nivel1'; currentBreadcrumbName = '1. Intuitivo (Moviola 3D)'; }
  else if (filename.includes('nivel2')) { activeKey = 'nivel2'; currentBreadcrumbName = '2. Básico (Matrices SMIa/SMIb)'; }
  else if (filename.includes('nivel3')) { activeKey = 'nivel3'; currentBreadcrumbName = '3. Esquema (Canon Q81)'; }
  else if (filename.includes('nivel4')) { activeKey = 'nivel4'; currentBreadcrumbName = '4. Aplicaciones (Casos)'; }
  else if (filename.includes('nivel5')) { activeKey = 'nivel5'; currentBreadcrumbName = '5. Matemático (Grassmann)'; }
  else if (filename.includes('nivel6')) { activeKey = 'nivel6'; currentBreadcrumbName = '6. Informes (Peritaje)'; }
  else if (filename.includes('nivel7')) { activeKey = 'nivel7'; currentBreadcrumbName = '7. Documentación (Zenodo)'; }
  else if (filename.includes('recursos')) { activeKey = 'recursos'; currentBreadcrumbName = '8. Recursos (Experiencia VISORD)'; }
  else if (filename.includes('fundamentos')) { activeKey = 'fundamentos'; currentBreadcrumbName = '9. Fundamentos (Cenit Epistemológico)'; }
  else if (filename.includes('visord') || filename.includes('radiografias') || filename.includes('acuario') || filename.includes('pentagrama') || filename.includes('suite_g2')) {
    activeKey = 'recursos';
    currentBreadcrumbName = '8. VISORD 3D Suite';
  }
  else if (filename.includes('deontologia_legal')) { activeKey = 'portal'; currentBreadcrumbName = 'Deontología PI & RGPD'; }
  else if (filename.includes('glosario')) { activeKey = 'portal'; currentBreadcrumbName = 'Glosario Canónico'; }
  else if (filename.includes('index_promocional') || filename === 'index.html' || filename === '') { activeKey = 'portal'; currentBreadcrumbName = 'Portal Institucional'; }
  else if (filename.includes('dial_orbital')) { activeKey = 'dial'; currentBreadcrumbName = 'Dial Orbital'; }

  // Geometría polar para el Dial SVG
  function polarToCartesian(cx, cy, r, angleDeg) {
    const rad = ((angleDeg - 90) * Math.PI) / 180.0;
    return {
      x: cx + r * Math.cos(rad),
      y: cy + r * Math.sin(rad)
    };
  }

  function createSectorPath(cx, cy, rIn, rOut, startAngle, endAngle) {
    const p1 = polarToCartesian(cx, cy, rOut, startAngle);
    const p2 = polarToCartesian(cx, cy, rOut, endAngle);
    const p3 = polarToCartesian(cx, cy, rIn, endAngle);
    const p4 = polarToCartesian(cx, cy, rIn, startAngle);
    return `M ${p1.x.toFixed(2)} ${p1.y.toFixed(2)} A ${rOut} ${rOut} 0 0 1 ${p2.x.toFixed(2)} ${p2.y.toFixed(2)} L ${p3.x.toFixed(2)} ${p3.y.toFixed(2)} A ${rIn} ${rIn} 0 0 0 ${p4.x.toFixed(2)} ${p4.y.toFixed(2)} Z`;
  }

  // Función constructora del HTML de navegación
  function injectPersistentNav() {
    // Si ya existe la barra, no duplicar
    if (document.getElementById('nexord-persistent-nav')) return;

    // Inyectar clase al body para el padding-top
    document.body.classList.add('has-persistent-nav');

    // 1. BARRA SUPERIOR PERSISTENTE
    const nav = document.createElement('nav');
    nav.id = 'nexord-persistent-nav';
    nav.setAttribute('aria-label', 'Navegación Persistente de Niveles NEXORD');

    nav.innerHTML = `
      <div class="pnav-left">
        <button type="button" class="pnav-dial-btn" id="btn-open-zenith-dial" title="Abrir Dial Orbital Cenital (Tecla D)">
          <span>🧭</span> <span>DIAL ORBITAL</span>
        </button>
        <div class="pnav-breadcrumb">
          <a href="${rootPrefix}index.html">NEXORD</a>
          <span class="sep">›</span>
          <span class="cur">${currentBreadcrumbName}</span>
        </div>
      </div>

      <div class="pnav-center">
        <a href="${rootPrefix}nivel1_intuitivo.html" class="pnav-lvl-pill ${activeKey === 'nivel1' ? 'active' : ''}" title="Nivel 1: Intuitivo (Moviola 3D)">1·Int</a>
        <a href="${rootPrefix}nivel2_basico.html" class="pnav-lvl-pill ${activeKey === 'nivel2' ? 'active' : ''}" title="Nivel 2: Básico (Matrices SMIa/SMIb)">2·Bás</a>
        <a href="${rootPrefix}nivel3_esquema.html" class="pnav-lvl-pill ${activeKey === 'nivel3' ? 'active' : ''}" title="Nivel 3: Esquema (Canon Q81)">3·Esq</a>
        <a href="${rootPrefix}nivel4_aplicaciones.html" class="pnav-lvl-pill ${activeKey === 'nivel4' ? 'active' : ''}" title="Nivel 4: Aplicaciones (Educación/Empresa/Salud)">4·Apl</a>
        <a href="${rootPrefix}nivel5_matematico.html" class="pnav-lvl-pill ${activeKey === 'nivel5' ? 'active' : ''}" title="Nivel 5: Matemático (Grassmann & Fiedler)">5·Mat</a>
        <a href="${rootPrefix}nivel6_informes.html" class="pnav-lvl-pill ${activeKey === 'nivel6' ? 'active' : ''}" title="Nivel 6: Informes Forenses">6·Inf</a>
        <a href="${rootPrefix}nivel7_documentacion.html" class="pnav-lvl-pill ${activeKey === 'nivel7' ? 'active' : ''}" title="Nivel 7: Documentación & Zenodo">7·Doc</a>
        <a href="${rootPrefix}recursos.html" class="pnav-lvl-pill ${activeKey === 'recursos' ? 'active' : ''}" title="Nivel 8: Recursos (Experiencia VISORD)">8·Rec</a>
        <a href="${rootPrefix}fundamentos.html" class="pnav-lvl-pill ${activeKey === 'fundamentos' ? 'active' : ''}" title="Nivel 9: Fundamentos (Cenit Epistemológico)">9·Fun</a>
      </div>

      <div class="pnav-right">
        <a href="${rootPrefix}deontologia_legal.html" class="pnav-link highlight" title="Código Deontológico PI (Regla 21) & Privacidad RGPD">
          <span>🛡️</span> <span class="link-text">Deontología & RGPD</span>
        </a>
        <a href="${rootPrefix}index_promocional.html#custodia" class="pnav-link" title="Custodia Institucional para Universidades">
          <span>🏛️</span> <span class="link-text">Custodia</span>
        </a>
        <a href="${rootPrefix}dial_orbital.html" class="pnav-link" title="Dial Orbital Epistemológico">
          <span>🧭</span>
        </a>
        <a href="${rootPrefix}index.html" class="pnav-link" title="Inicio / Portada de Bienvenida">
          <span>🏠</span>
        </a>
      </div>
    `;

    document.body.insertAdjacentElement('afterbegin', nav);

    // 2. CONSTRUCCIÓN GEOMÉTRICA DE LA RUEDA SVG (DIAL 3-6-9)
    const CX = 200, CY = 200, R_IN = 70, R_OUT = 185;
    const ANGLE_STEP = 40.0;

    let slicesSvg = '';
    DIAL_SECTORS.forEach((sec, i) => {
      const startAngle = i * ANGLE_STEP - ANGLE_STEP / 2;
      const endAngle = startAngle + ANGLE_STEP;
      const midAngle = (startAngle + endAngle) / 2;
      const pathD = createSectorPath(CX, CY, R_IN, R_OUT, startAngle, endAngle);
      const labelPos = polarToCartesian(CX, CY, (R_IN + R_OUT) / 2, midAngle);

      slicesSvg += `
        <path d="${pathD}"
              class="zenith-slice ${sec.key === activeKey ? 'active' : ''}"
              data-idx="${sec.idx}"
              data-num="${sec.num}"
              fill="${sec.color}"
              role="button"
              tabindex="0"
              aria-label="Sector ${sec.num}: ${sec.title}">
        </path>
        <text x="${labelPos.x.toFixed(1)}" y="${(labelPos.y + 3).toFixed(1)}" class="zenith-slice-text">
          ${sec.num}·${sec.short}
        </text>
      `;
    });

    // Vértices del Triángulo de Resonancia 3-6-9 (0° Sector 9, 120° Sector 3, 240° Sector 6)
    const rTri = 145;
    const p9 = polarToCartesian(CX, CY, rTri, 0);
    const p3 = polarToCartesian(CX, CY, rTri, 120);
    const p6 = polarToCartesian(CX, CY, rTri, 240);

    // Fichas alternativas (ordenadas numéricamente 1..9)
    const cardsSorted = [...DIAL_SECTORS].sort((a, b) => parseInt(a.num) - parseInt(b.num));
    let sectorsCardsHtml = '';
    cardsSorted.forEach(sec => {
      const isSecActive = sec.key === activeKey;
      sectorsCardsHtml += `
        <a href="${sec.url}" class="zenith-sector-card ${isSecActive ? 'active' : ''}">
          <div>
            <div class="zenith-card-num">SECTOR ${sec.num} · CANON</div>
            <div class="zenith-card-title">${sec.title}</div>
            <div class="zenith-card-desc">${sec.desc}</div>
          </div>
          <div class="zenith-card-action">
            <span>${isSecActive ? '📍 Estás aquí' : 'Acceder'}</span>
            <span>→</span>
          </div>
        </a>
      `;
    });

    // 3. MODAL DEL DIAL CENITAL 3-6-9
    const modal = document.createElement('div');
    modal.id = 'nexord-zenith-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Selector Cenital Dial 3-6-9');

    modal.innerHTML = `
      <div class="zenith-box">
        <div class="zenith-header">
          <div class="zenith-title">
            <span>🧭</span>
            <span>DIAL ORBITAL CENITAL · NAVEGACIÓN UNIVERSAL</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <a href="${rootPrefix}dial_orbital.html" class="zenith-btn-fullscreen" title="Abrir Dial 3-6-9 en Pantalla Completa" style="padding: 4px 10px; font-size: 0.74rem;">
              ⛶ Pantalla Completa ↗
            </a>
            <button type="button" class="zenith-close-btn" id="btn-close-zenith-dial" title="Cerrar modal (Esc)">
              ✕ Cerrar
            </button>
          </div>
        </div>

        <!-- VISTA CANÓNICA: RUEDA SVG INTERACTIVA (DIAL) -->
        <div class="zenith-dial-container">
          <div class="zenith-wheel-col">
            <svg class="zenith-wheel-svg" viewBox="0 0 400 400" aria-label="Rueda Orbital Dial 3-6-9">
              <defs>
                <radialGradient id="hubGrad" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stop-color="#0E1A38" />
                  <stop offset="100%" stop-color="#070C1C" />
                </radialGradient>
              </defs>
              <!-- Triángulo de Resonancia 3-6-9 -->
              <polygon points="${p9.x.toFixed(1)},${p9.y.toFixed(1)} ${p3.x.toFixed(1)},${p3.y.toFixed(1)} ${p6.x.toFixed(1)},${p6.y.toFixed(1)}"
                       fill="rgba(0, 240, 255, 0.06)" stroke="#00F0FF" stroke-width="1.8" stroke-dasharray="4 3" />
              <!-- 9 Sectores SVG -->
              ${slicesSvg}
              <!-- Centro Hub -->
              <circle cx="200" cy="200" r="66" fill="url(#hubGrad)" stroke="#00F0FF" stroke-width="2" />
              <circle cx="200" cy="200" r="62" fill="none" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1" stroke-dasharray="2 3" />
              <text x="200" y="194" fill="#00FF87" font-family="'Roboto Mono', monospace" font-size="11" font-weight="900" letter-spacing="1.5" text-anchor="middle">NEXORD</text>
              <text x="200" y="210" fill="#38BDF8" font-family="'Roboto Mono', monospace" font-size="8.5" font-weight="700" letter-spacing="1" text-anchor="middle">DIAL 3·6·9</text>
            </svg>
          </div>

          <!-- Inspector Dinámico de Sector -->
          <div class="zenith-inspector-col">
            <div>
              <div class="zenith-insp-header">
                <span class="zenith-insp-badge" id="zinsp-badge">NIVEL 1 • ENTRADA VISUAL</span>
                <span class="zenith-insp-key">CANON NEXORD</span>
              </div>
              <div class="zenith-insp-title" id="zinsp-title">Nivel 1: Intuitivo</div>
              <div class="zenith-insp-sub" id="zinsp-sub">Moviola 3D & Densidad Bruta</div>
              <div class="zenith-insp-desc" id="zinsp-desc">Simulación de partículas dinámicas, fluidos relacionales y balance de atracción/rechazo sin estrés evaluativo.</div>
            </div>
            <div class="zenith-insp-actions">
              <a id="zinsp-btn-enter" href="${rootPrefix}nivel1_intuitivo.html" class="zenith-btn-enter">
                <span>Entrar al Nivel ➔</span>
              </a>
              <a id="zinsp-btn-fs" href="${rootPrefix}dial_orbital.html" class="zenith-btn-fullscreen">
                <span>Ver en Dial 3D ↗</span>
              </a>
            </div>
          </div>
        </div>

        <!-- VISTA ALTERNATIVA: LISTA DE FICHAS (OCULTA POR DEFECTO) -->
        <div class="zenith-body" style="display: none;">
          ${sectorsCardsHtml}
        </div>

        <div class="zenith-footer">
          <button type="button" class="zenith-toggle-view" id="zinsp-toggle-view">📋 Ver como Lista</button>
          <span class="zenith-footer-hint">⌨ Teclas 1-9 seleccionan nivel · Enter o Clic accede · Tecla D o Esc cierran</span>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    // 4. CONTROLADOR DEL INSPECTOR Y EVENTOS DEL DIAL
    let currentSelectedIndex = 1; // Por defecto Sector 1 (o sector activo)
    const matchedSector = DIAL_SECTORS.find(s => s.key === activeKey);
    if (matchedSector) {
      currentSelectedIndex = matchedSector.idx;
    }

    function updateInspector(idx) {
      const sec = DIAL_SECTORS[idx];
      if (!sec) return;
      currentSelectedIndex = idx;

      const b = document.getElementById('zinsp-badge');
      const t = document.getElementById('zinsp-title');
      const s = document.getElementById('zinsp-sub');
      const d = document.getElementById('zinsp-desc');
      const btnEnter = document.getElementById('zinsp-btn-enter');
      const btnFs = document.getElementById('zinsp-btn-fs');

      if (b) b.textContent = sec.badge;
      if (t) t.textContent = sec.title;
      if (s) s.textContent = sec.subtitle;
      if (d) d.textContent = sec.desc;
      if (btnEnter) {
        btnEnter.href = sec.url;
        btnEnter.innerHTML = `<span>Entrar al Nivel ${sec.num}</span> <span>➔</span>`;
      }
      if (btnFs) {
        btnFs.href = `${rootPrefix}dial_orbital.html?sector=${sec.num}`;
      }

      // Resaltar porción activa en el SVG
      const slices = modal.querySelectorAll('.zenith-slice');
      slices.forEach((sl) => {
        if (parseInt(sl.dataset.idx) === idx) {
          sl.classList.add('active');
        } else {
          sl.classList.remove('active');
        }
      });
    }

    // Interacción con porciones SVG
    const slices = modal.querySelectorAll('.zenith-slice');
    slices.forEach((sl) => {
      const idx = parseInt(sl.dataset.idx);
      sl.addEventListener('mouseenter', () => updateInspector(idx));
      sl.addEventListener('click', () => {
        updateInspector(idx);
        const sec = DIAL_SECTORS[idx];
        if (sec && sec.url) {
          window.location.href = sec.url;
        }
      });
      sl.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          const sec = DIAL_SECTORS[idx];
          if (sec && sec.url) window.location.href = sec.url;
        }
      });
    });

    // Alternar entre Vista Rueda y Vista Lista
    const toggleBtn = document.getElementById('zinsp-toggle-view');
    const dialView = modal.querySelector('.zenith-dial-container');
    const listView = modal.querySelector('.zenith-body');
    let isDialView = true;

    if (toggleBtn && dialView && listView) {
      toggleBtn.addEventListener('click', () => {
        isDialView = !isDialView;
        if (isDialView) {
          dialView.style.display = 'flex';
          listView.style.display = 'none';
          toggleBtn.textContent = '📋 Ver como Lista';
        } else {
          dialView.style.display = 'none';
          listView.style.display = 'grid';
          toggleBtn.textContent = '🧭 Ver como Rueda';
        }
      });
    }

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
  }

  // Inicializar al cargar el DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectPersistentNav);
  } else {
    injectPersistentNav();
  }
})();
