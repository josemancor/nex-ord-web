/**
 * =============================================================================
 * VISORD-BUS.JS · NÚCLEO DE INTERACCIÓN REACTIVA & MINI-TACÓMETRO HUD
 * Ecosistema VISORD / NEXORD (Canon 2026)
 * =============================================================================
 * Proporciona:
 *   1. Bus de eventos global bidireccional (BroadcastChannel + CustomEvents).
 *   2. Sincronización de Selección Nodal (foco simultáneo 2D, 3D y Tablas).
 *   3. Moviola Temporal Unificada (T1 -> Tt con interpolación cinemática).
 *   4. Conmutador Fasorial Tri-Modo ("Acción vs. Expectativas vs. Tensión").
 *   5. Mini-Tacómetro Socio-Termodinámico en el Control Universal (nav-pod).
 * =============================================================================
 */

(function (window, document) {
  'use strict';

  if (window.__VISORD_BUS_INITIALIZED__) return;
  window.__VISORD_BUS_INITIALIZED__ = true;

  // Canal de difusión multi-pestaña / multi-iframe
  let broadcast = null;
  try {
    if (typeof BroadcastChannel !== 'undefined') {
      broadcast = new BroadcastChannel('nexord_visord_bus');
    }
  } catch (e) {
    console.warn('[VisordBus] BroadcastChannel no disponible; usando bus in-page.');
  }

  // Estado reactivo global compartido
  const state = {
    activeNodeId: null,
    activeTime: 1,
    maxTime: 5,
    prismMode: 'action', // 'action' (Fáctico), 'expectations' (Perceptual), 'tension' (Cizalladura tau)
    regime: {
      rho: 0.38,
      eta: 0.69,
      omega_rot: 0.285,
      name: 'Régimen Orgánico con Vorticidad',
      color: '#38BDF8'
    }
  };

  // ---------------------------------------------------------------------------
  // 1. API DEL BUS DE EVENTOS
  // ---------------------------------------------------------------------------
  const VisordBus = {
    getState() {
      return { ...state };
    },

    // Emisión de eventos a toda la suite
    emit(eventType, payload, origin = 'local') {
      // Actualizar estado interno según evento
      if (eventType === 'NODE_SELECT') {
        state.activeNodeId = payload.nodeId;
      } else if (eventType === 'TIME_CHANGE') {
        state.activeTime = payload.t;
        if (payload.maxT) state.maxTime = payload.maxT;
      } else if (eventType === 'PRISM_MODE_CHANGE') {
        state.prismMode = payload.mode; // 'action', 'expectations', 'tension'
      } else if (eventType === 'REGIME_UPDATE') {
        state.regime = { ...state.regime, ...payload };
        updateMiniTacometroUI();
      }

      // Evento local in-page
      const customEvt = new CustomEvent(`visord:${eventType}`, { detail: { ...payload, origin } });
      window.dispatchEvent(customEvt);

      // Si es local, retransmitir a otras pestañas/iframes
      if (origin === 'local' && broadcast) {
        try {
          broadcast.postMessage({ eventType, payload });
        } catch (err) {
          console.warn('[VisordBus] Error en broadcast:', err);
        }
      }
    },

    // Suscripción a eventos
    on(eventType, callback) {
      window.addEventListener(`visord:${eventType}`, (e) => callback(e.detail));
    },

    // Atajos de emisión operativa
    selectNode(nodeId, source = 'user') {
      this.emit('NODE_SELECT', { nodeId, source });
    },

    setTime(t, maxT = state.maxTime, source = 'user') {
      this.emit('TIME_CHANGE', { t, maxT, source });
    },

    setPrismMode(mode, source = 'user') {
      this.emit('PRISM_MODE_CHANGE', { mode, source });
    },

    updateRegime(regimeData) {
      this.emit('REGIME_UPDATE', regimeData);
    }
  };

  // Escuchar mensajes entrantes desde otras pestañas/ventanas
  if (broadcast) {
    broadcast.onmessage = (msg) => {
      if (msg.data && msg.data.eventType) {
        VisordBus.emit(msg.data.eventType, msg.data.payload, 'remote');
      }
    };
  }

  window.VisordBus = VisordBus;

  // ---------------------------------------------------------------------------
  // 2. INYECCIÓN DEL MINI-TACÓMETRO EN EL CONTROL UNIVERSAL (nav-pod)
  // ---------------------------------------------------------------------------
  function injectMiniTacometro() {
    let navPod = document.querySelector('.universal-nav-pod');
    if (!navPod) {
      // Si no existe, crear uno discreto en esquina inferior derecha
      navPod = document.createElement('nav');
      navPod.className = 'universal-nav-pod';
      navPod.setAttribute('aria-label', 'Mando Universal NEXORD');
      document.body.appendChild(navPod);
    }

    if (document.getElementById('nav-pod-tacometro-btn')) return;

    // Estilos complementarios para el Mini-Tacómetro y su Popover
    const style = document.createElement('style');
    style.id = 'visord-bus-tacometro-style';
    style.innerHTML = `
      .nav-pod-tacometro {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 35%, #1E293B, #0B132B);
        border: 1.5px solid var(--border-highlight, #38BDF8);
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        position: relative;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-top: 4px;
      }
      .nav-pod-tacometro:hover {
        transform: scale(1.18);
        box-shadow: 0 0 16px rgba(0, 255, 135, 0.8);
      }
      .tacometro-indicator-ring {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #00FF87;
        box-shadow: 0 0 8px #00FF87;
        transition: background 0.3s ease, box-shadow 0.3s ease;
      }
      .tacometro-indicator-ring.vort {
        background: #FF007F;
        box-shadow: 0 0 12px #FF007F;
        animation: pulseVort 1.2s infinite alternate;
      }
      @keyframes pulseVort {
        from { transform: scale(0.9); opacity: 0.8; }
        to { transform: scale(1.15); opacity: 1.0; }
      }

      /* POPOVER DIAGNÓSTICO FLOTANTE */
      #nav-pod-tacometro-popover {
        position: fixed;
        right: 64px;
        bottom: 24px;
        width: 300px;
        background: rgba(11, 19, 43, 0.96);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1.5px solid #38BDF8;
        border-radius: 12px;
        padding: 14px 16px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
        color: #E2E8F0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 11.5px;
        z-index: 999999;
        display: none;
        flex-direction: column;
        gap: 10px;
      }
      #nav-pod-tacometro-popover.active {
        display: flex;
      }
      .popover-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 6px;
      }
      .popover-header h4 {
        margin: 0;
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
        color: #38BDF8;
        letter-spacing: 0.5px;
      }
      .popover-close {
        cursor: pointer;
        color: #94A3B8;
        font-weight: bold;
        font-size: 13px;
      }
      .popover-close:hover { color: #FFF; }
      .tacometro-kpis {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        font-family: 'Roboto Mono', Menlo, monospace;
        font-size: 10.5px;
      }
      .tacometro-kpi-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 6px;
        padding: 6px 8px;
      }
      .tacometro-kpi-box .lbl { color: #94A3B8; font-size: 9px; display: block; }
      .tacometro-kpi-box .val { color: #00FF87; font-weight: bold; font-size: 12px; }
      .prism-toggle-strip {
        display: flex;
        gap: 4px;
        margin-top: 4px;
      }
      .prism-toggle-btn {
        flex: 1;
        padding: 5px 4px;
        font-size: 9.5px;
        font-weight: bold;
        border-radius: 4px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255,255,255,0.05);
        color: #94A3B8;
        cursor: pointer;
        text-align: center;
        transition: all 0.15s ease;
      }
      .prism-toggle-btn.active {
        background: #0284C7;
        color: #FFF;
        border-color: #38BDF8;
      }
      .popover-btn-spectral {
        margin-top: 4px;
        background: linear-gradient(135deg, #0284C7, #0369A1);
        border: 1px solid #38BDF8;
        color: #FFF;
        padding: 6px 10px;
        border-radius: 6px;
        font-size: 10.5px;
        font-weight: bold;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        display: block;
      }
      .popover-btn-spectral:hover {
        background: #38BDF8;
        color: #0B132B;
      }
    `;
    document.head.appendChild(style);

    // Botón tacómetro en el pod
    const btn = document.createElement('button');
    btn.id = 'nav-pod-tacometro-btn';
    btn.className = 'nav-pod-btn nav-pod-tacometro';
    btn.setAttribute('title', 'Tacómetro Socio-Termodinámico (Canon 2026)');
    btn.setAttribute('aria-label', 'Tacómetro de Régimen Grupal');
    btn.innerHTML = `<div class="tacometro-indicator-ring" id="tacometro-dot"></div>`;
    btn.onclick = toggleTacometroPopover;

    navPod.appendChild(btn);

    // Popover diagnóstico
    const popover = document.createElement('div');
    popover.id = 'nav-pod-tacometro-popover';
    popover.innerHTML = `
      <div class="popover-header">
        <h4>Tacómetro Relacional • VISORD</h4>
        <span class="popover-close" onclick="toggleTacometroPopover()">✕</span>
      </div>
      <div id="tacometro-regime-txt" style="font-weight:bold; font-size:11.5px; color:#FFF;">
        ${state.regime.name}
      </div>
      <div class="tacometro-kpis">
        <div class="tacometro-kpi-box">
          <span class="lbl">Reciprocidad ρ:</span>
          <span class="val" id="pop-rho">+0.38</span>
        </div>
        <div class="tacometro-kpi-box">
          <span class="lbl">Cristalización η:</span>
          <span class="val" id="pop-eta">0.69</span>
        </div>
        <div class="tacometro-kpi-box">
          <span class="lbl">Vorticidad Ω:</span>
          <span class="val" id="pop-vort" style="color:#FF007F;">0.285</span>
        </div>
        <div class="tacometro-kpi-box">
          <span class="lbl">Corte Temporal:</span>
          <span class="val" id="pop-time">T1</span>
        </div>
      </div>
      <div>
        <span style="font-size:9.5px; color:#94A3B8; text-transform:uppercase; font-weight:bold;">Eje Perceptual:</span>
        <div class="prism-toggle-strip">
          <button class="prism-toggle-btn active" id="btn-prism-act" onclick="VisordBus.setPrismMode('action')">⚡ Acción</button>
          <button class="prism-toggle-btn" id="btn-prism-exp" onclick="VisordBus.setPrismMode('expectations')">🧠 Expectativas</button>
          <button class="prism-toggle-btn" id="btn-prism-tau" onclick="VisordBus.setPrismMode('tension')">⚖️ Tensión</button>
        </div>
      </div>
      <a href="nexord_visor_universal.html" target="_blank" class="popover-btn-spectral">
        🪐 Abrir Estación Espectral (4 Paneles) ↗
      </a>
    `;
    document.body.appendChild(popover);

    updateMiniTacometroUI();
  }

  function toggleTacometroPopover() {
    const pop = document.getElementById('nav-pod-tacometro-popover');
    if (pop) {
      pop.classList.toggle('active');
    }
  }

  function updateMiniTacometroUI() {
    const dot = document.getElementById('tacometro-dot');
    const popRho = document.getElementById('pop-rho');
    const popEta = document.getElementById('pop-eta');
    const popVort = document.getElementById('pop-vort');
    const popTime = document.getElementById('pop-time');
    const popRegime = document.getElementById('tacometro-regime-txt');

    if (!dot) return;

    // Actualizar indicador según vorticidad / cohesión
    const isVort = state.regime.omega_rot > 0.15;
    if (isVort) {
      dot.className = 'tacometro-indicator-ring vort';
    } else {
      dot.className = 'tacometro-indicator-ring';
      dot.style.background = state.regime.color || '#00FF87';
      dot.style.boxShadow = `0 0 8px ${state.regime.color || '#00FF87'}`;
    }

    if (popRho) popRho.innerText = (state.regime.rho >= 0 ? '+' : '') + Number(state.regime.rho).toFixed(2);
    if (popEta) popEta.innerText = Number(state.regime.eta).toFixed(2);
    if (popVort) popVort.innerText = Number(state.regime.omega_rot).toFixed(3);
    if (popTime) popTime.innerText = `T${state.activeTime}`;
    if (popRegime) popRegime.innerText = state.regime.name;

    // Actualizar botones de prisma
    ['action', 'expectations', 'tension'].forEach(m => {
      const b = document.getElementById(`btn-prism-${m.slice(0,3)}`);
      if (b) {
        if (state.prismMode === m) b.classList.add('active');
        else b.classList.remove('active');
      }
    });
  }

  // Reactividad interna ante cambios de prisma y tiempo
  VisordBus.on('PRISM_MODE_CHANGE', (d) => {
    state.prismMode = d.mode;
    updateMiniTacometroUI();
  });

  VisordBus.on('TIME_CHANGE', (d) => {
    state.activeTime = d.t;
    updateMiniTacometroUI();
  });

  // Auto-inyección cuando el DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectMiniTacometro);
  } else {
    injectMiniTacometro();
  }

})(window, document);
