/**
 * ==============================================================================
 * MÓDULO EXTENDIDO: visord_compass_navigation.js
 * Plataforma: NEXORD / VISORD Engine Platinum (2026)
 * Autor Científico: Dr. José Manuel Cornejo Álvarez (Universitat de Barcelona)
 * Arquitectura: Cinemática del Compás Tripolar + Sonificación Psicoacústica
 *               Binaural/Térmica a 432 Hz gobernada por ||VT|| y θ_Ψ
 * ==============================================================================
 */

export class VisordAcousticCompassEngine {
  /**
   * @param {Object} config Opciones de montaje gráfico y sonoro
   * @param {string} [config.svgCanvasId='visord-svg-canvas']
   * @param {string} [config.compassGroupId='brujula-astrolabio']
   * @param {string} [config.toponymsLayerId='capa-toponimos-dinamicos']
   * @param {number} [config.frecuenciaBase=432.0] Tono natural áureo de sintonía (Hz)
   * @param {number} [config.volumenMaster=0.18] Nivel sonoro máximo de seguridad
   */
  constructor(config = {}) {
    this.canvasId = config.svgCanvasId || config.svgContainerId || 'visord-svg-canvas';
    this.compassId = config.compassGroupId || config.compassId || 'brujula-astrolabio';
    this.toponymsLayerId = config.toponymsLayerId || 'capa-toponimos-dinamicos';

    // Topónimos de los 14 Reinos (escala proyectiva 1000 x 600 px)
    this.ANCLAJES_REINOS = {
      TYP_01_DEMOCRATICO:        { x: 500, y: 110, nombre: "Concordia Comcon" },
      TYP_02_AUTOCRATICO:         { x: 250, y: 220, nombre: "Torreón del Ojo Único" },
      TYP_03_BIPOLAR:             { x: 750, y: 220, nombre: "Garganta de las Dos Casas" },
      TYP_04_CHIVO_EXPIATORIO:    { x: 870, y: 380, nombre: "Limes del Desahucio" },
      TYP_05_ANOMICO:             { x: 150, y: 470, nombre: "Yermo de las Mónadas" },
      TYP_06_GROUPTHINK:          { x: 440, y: 65,  nombre: "Isla de la Falsa Unanimidad" },
      TYP_07_DESCONFIANZA:        { x: 680, y: 340, nombre: "Estrecho de la Suspicacia" },
      TYP_08_DOBLE_VINCULO:       { x: 330, y: 350, nombre: "Laberinto Disonante" },
      TYP_09_BICEFALICO:          { x: 590, y: 160, nombre: "Señorío Dual de Bastin" },
      TYP_10_CADENA_JERARQUICA:   { x: 200, y: 310, nombre: "Desfiladero Escalonado" },
      TYP_11_CLICAS_EXCLUYENTES:  { x: 800, y: 140, nombre: "Acrópolis de la Oligarquía" },
      TYP_12_LIDER_CONTROVERSIAL: { x: 510, y: 275, nombre: "Vórtice Festinger" },
      TYP_13_ALEATORIO:           { x: 500, y: 365, nombre: "Llanura de Máxima Entropía" },
      TYP_14_CRISIS_TOTAL:        { x: 500, y: 535, nombre: "Sima de la Ruptura W81" }
    };

    this.CENTRO_COMPAS = { x: 100, y: 100 };
    this.RADIO_COMPAS_FLECHA = 52;
    this.RADIO_INFLUENCIA_TOPONIMO = 210;

    // --- SUBSISTEMA PSICOACÚSTICO (Web Audio API) ---
    this.F0 = config.frecuenciaBase || 432.0;
    this.volumenMaximo = config.volumenMaster || 0.18;
    this.audioCtx = null;
    this.audioIniciado = false;

    this.nodosAudio = {
      masterGain: null,
      oscPortadora: null,   // F0 (432 Hz)
      oscBatimento: null,   // F0 + delta_f (Gobernado por ||VT||)
      gainBatimento: null,
      oscDisonancia: null,  // Armónico de fricción (Polo Sur W81)
      gainDisonancia: null,
      filtroResonante: null,
      panner: null
    };

    this.cacheDOM = {
      canvas: null,
      toponymsLayer: null,
      agujaG: null,
      agujaT: null,
      agujaC: null,
      agujaPsi: null,
      vectorVt: null
    };

    this.conectarDOM();
  }

  conectarDOM() {
    this.cacheDOM.canvas = document.getElementById(this.canvasId);
    if (!this.cacheDOM.canvas) return;

    this.cacheDOM.toponymsLayer = document.getElementById(this.toponymsLayerId);
    this.cacheDOM.agujaG = this.cacheDOM.canvas.querySelector('.aguja-morfologico-g');
    this.cacheDOM.agujaT = this.cacheDOM.canvas.querySelector('.aguja-temporal-t');
    this.cacheDOM.agujaC = this.cacheDOM.canvas.querySelector('.aguja-criterial-c');
    this.cacheDOM.agujaPsi = this.cacheDOM.canvas.querySelector('.aguja-regimen-psi');
    this.cacheDOM.vectorVt = this.cacheDOM.canvas.querySelector('.vector-deriva-vt');
  }

  /**
   * Despierta el AudioContext tras la primera interacción de usuario (requisito W3C/Navegadores).
   */
  async inicializarAudio() {
    if (this.audioIniciado) {
      if (this.audioCtx && this.audioCtx.state === 'suspended') {
        await this.audioCtx.resume();
      }
      if (this.nodosAudio.masterGain) {
        const t0 = this.audioCtx.currentTime;
        this.nodosAudio.masterGain.gain.cancelScheduledValues(t0);
        this.nodosAudio.masterGain.gain.exponentialRampToValueAtTime(this.volumenMaximo, t0 + 0.6);
      }
      return;
    }

    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) {
      console.warn("Web Audio API no soportada en este entorno.");
      return;
    }

    this.audioCtx = new AudioContextClass();

    if (this.audioCtx.state === 'suspended') {
      await this.audioCtx.resume();
    }

    const t0 = this.audioCtx.currentTime;

    // 1. Bus Master con rampa suave
    this.nodosAudio.masterGain = this.audioCtx.createGain();
    this.nodosAudio.masterGain.gain.setValueAtTime(0.0001, t0);
    this.nodosAudio.masterGain.gain.exponentialRampToValueAtTime(this.volumenMaximo, t0 + 1.2);

    // 2. Filtro Pasabajos Cálido (Modelado de Viento/Pergamino)
    this.nodosAudio.filtroResonante = this.audioCtx.createBiquadFilter();
    this.nodosAudio.filtroResonante.type = 'lowpass';
    this.nodosAudio.filtroResonante.frequency.setValueAtTime(864.0, t0); // Primer armónico
    this.nodosAudio.filtroResonante.Q.setValueAtTime(2.5, t0);

    // 3. Panner Estéreo Dinámico (Inclinación espacial según Oriente/Poniente C vs T)
    if (this.audioCtx.createStereoPanner) {
      this.nodosAudio.panner = this.audioCtx.createStereoPanner();
      this.nodosAudio.panner.pan.setValueAtTime(0.0, t0);
    } else {
      // Fallback para navegadores antiguos
      this.nodosAudio.panner = this.audioCtx.createGain();
    }

    // 4. Oscilador Portador Primario (Onda pura 432 Hz: Estado de Armonía Basal)
    this.nodosAudio.oscPortadora = this.audioCtx.createOscillator();
    this.nodosAudio.oscPortadora.type = 'sine';
    this.nodosAudio.oscPortadora.frequency.setValueAtTime(this.F0, t0);

    // 5. Oscilador Secundario de Batimento Binaural (Δf gobernado por ||VT||)
    this.nodosAudio.oscBatimento = this.audioCtx.createOscillator();
    this.nodosAudio.oscBatimento.type = 'sine';
    this.nodosAudio.oscBatimento.frequency.setValueAtTime(this.F0, t0);

    this.nodosAudio.gainBatimento = this.audioCtx.createGain();
    this.nodosAudio.gainBatimento.gain.setValueAtTime(0.35, t0);

    // 6. Oscilador de Disonancia Rugosa (Triangular: Tensión de Crisis W81 / Polo Sur)
    this.nodosAudio.oscDisonancia = this.audioCtx.createOscillator();
    this.nodosAudio.oscDisonancia.type = 'triangle';
    // Frecuencia en tritono disonante (F0 * sqrt(2) ≈ 610.94 Hz)
    this.nodosAudio.oscDisonancia.frequency.setValueAtTime(this.F0 * Math.SQRT2, t0);

    this.nodosAudio.gainDisonancia = this.audioCtx.createGain();
    this.nodosAudio.gainDisonancia.gain.setValueAtTime(0.0001, t0); // Silencioso en equilibrio

    // Conexiones de la Red Acústica
    this.nodosAudio.oscPortadora.connect(this.nodosAudio.filtroResonante);

    this.nodosAudio.oscBatimento.connect(this.nodosAudio.gainBatimento);
    this.nodosAudio.gainBatimento.connect(this.nodosAudio.filtroResonante);

    this.nodosAudio.oscDisonancia.connect(this.nodosAudio.gainDisonancia);
    this.nodosAudio.gainDisonancia.connect(this.nodosAudio.filtroResonante);

    this.nodosAudio.filtroResonante.connect(this.nodosAudio.panner);
    this.nodosAudio.panner.connect(this.nodosAudio.masterGain);
    this.nodosAudio.masterGain.connect(this.audioCtx.destination);

    // Arranque de fuentes continuas
    this.nodosAudio.oscPortadora.start();
    this.nodosAudio.oscBatimento.start();
    this.nodosAudio.oscDisonancia.start();

    this.audioIniciado = true;
  }

  /**
   * Modula en tiempo real la síntesis sonora a partir de la cinemática relacional.
   *
   * @param {number} magnitudVt Rapidez de deriva ||VT|| = sqrt(vx² + vy²)
   * @param {number} thetaPsi Rumbo azimutal de la aguja de régimen Ψ (0° a 360°)
   * @param {number} deltaT Tiempo de transición paramétrica para suavizado (segundos)
   */
  modularAcustica(magnitudVt, thetaPsi, deltaT = 0.08) {
    if (!this.audioIniciado || !this.audioCtx || !this.nodosAudio.oscBatimento) return;

    const t = this.audioCtx.currentTime;
    const tau = t + deltaT;

    // --- A. BATIMENTO ARMÓNICO MODULADO POR ||VT|| ---
    // Si ||VT|| = 0 (estabilidad absoluta) -> Delta f = 0 Hz (unísono puro 432 Hz).
    // Si ||VT|| crece -> Delta f escala hasta 14 Hz (ritmos alfa/theta y batimento acústico perceptible).
    const maxDeltaF = 14.0;
    const deltaF = Math.min(maxDeltaF, magnitudVt * maxDeltaF);
    const frecuenciaBatimento = this.F0 + deltaF;

    this.nodosAudio.oscBatimento.frequency.cancelScheduledValues(t);
    this.nodosAudio.oscBatimento.frequency.linearRampToValueAtTime(frecuenciaBatimento, tau);

    // --- B. TENSIÓN DISONANTE MODULADA POR θ_Ψ (RUMBO DE RÉGIMEN) ---
    // Norte (0° / Democrático): Cero disonancia, armónico apagado.
    // Sur (180° / Colapso W81): Máxima ganancia del tritono e incremento del filtro pasabajos.
    const rad = (thetaPsi * Math.PI) / 180.0;
    // factorSur: 0.0 en el Norte (cos = 1), 1.0 en el Sur (cos = -1)
    const factorSur = (1.0 - Math.cos(rad)) / 2.0;

    // Ganancia del armónico de fricción
    const gananciaDisonancia = Math.pow(factorSur, 2) * 0.45;
    this.nodosAudio.gainDisonancia.gain.cancelScheduledValues(t);
    this.nodosAudio.gainDisonancia.gain.linearRampToValueAtTime(gananciaDisonancia, tau);

    // El filtro se abre con la crisis, permitiendo agudos ásperos
    const corteFiltro = 864.0 + (factorSur * 1800.0);
    this.nodosAudio.filtroResonante.frequency.cancelScheduledValues(t);
    this.nodosAudio.filtroResonante.frequency.linearRampToValueAtTime(corteFiltro, tau);

    // --- C. ESPACIALIZACIÓN ESTÉREO (PANNER) ---
    // Este (90° / Criterial): Pan hacia la derecha (+0.65).
    // Oeste (270° / Temporal): Pan hacia la izquierda (-0.65).
    if (this.nodosAudio.panner && this.nodosAudio.panner.pan) {
      const panX = Math.sin(rad) * 0.65;
      this.nodosAudio.panner.pan.cancelScheduledValues(t);
      this.nodosAudio.panner.pan.linearRampToValueAtTime(panX, tau);
    }
  }

  /**
   * Cálculo de rumbos náuticos de las 4 agujas
   */
  calcularAngulosCompas(estado, omega) {
    const { G = {}, T = {}, C = {} } = estado;

    const faultlines = G.faultlines ?? 0.0;
    const holgura = G.holgura ?? 0.5;
    const deflexionG = (-faultlines * 45.0) + ((1.0 - holgura) * 30.0);
    const theta_G = (deflexionG + 360.0) % 360.0;

    const s13 = Math.max(-1.0, Math.min(1.0, T.memoriaS13 ?? 0.0));
    const deflexionT = s13 * 42.0;
    const theta_T = (270.0 - deflexionT + 360.0) % 360.0;

    const cuadrantesOffset = [-25.0, 10.0, 25.0, -10.0];
    const cId = Math.max(0, Math.min(3, C.cuadranteId ?? C.cuadrante ?? 0));
    const esclerosis = 1.0 - Math.max(0.0, Math.min(1.0, C.plasticidadEc ?? 0.5));
    const deflexionC = cuadrantesOffset[cId] + (esclerosis * 35.0);
    const theta_C = (90.0 + deflexionC + 360.0) % 360.0;

    let fasorX = 0.0;
    let fasorY = 0.0;
    const claves = Object.keys(this.ANCLAJES_REINOS);
    const totalReinos = claves.length;

    for (let i = 0; i < totalReinos; i++) {
      const peso = omega[i] || 0.0;
      const phi = (i / totalReinos) * (2.0 * Math.PI);
      fasorX += peso * Math.sin(phi);
      fasorY += peso * Math.cos(phi);
    }

    let theta_Psi = (Math.atan2(fasorX, fasorY) * 180.0) / Math.PI;
    theta_Psi = (theta_Psi + 360.0) % 360.0;

    return {
      theta_G: Number(theta_G.toFixed(2)),
      theta_T: Number(theta_T.toFixed(2)),
      theta_C: Number(theta_C.toFixed(2)),
      theta_Psi: Number(theta_Psi.toFixed(2))
    };
  }

  calcularCoordenadasBaricentricas(omega) {
    let px = 0.0;
    let py = 0.0;
    const claves = Object.keys(this.ANCLAJES_REINOS);

    for (let i = 0; i < claves.length; i++) {
      const peso = omega[i] || 0.0;
      const reino = this.ANCLAJES_REINOS[claves[i]];
      px += peso * reino.x;
      py += peso * reino.y;
    }

    return {
      x: Number(px.toFixed(2)),
      y: Number(py.toFixed(2))
    };
  }

  renderizarCompas(angulos, vectorVt = { x: 0, y: 0 }) {
    if (this.cacheDOM.agujaG) {
      this.cacheDOM.agujaG.setAttribute('transform', `rotate(${angulos.theta_G}, ${this.CENTRO_COMPAS.x}, ${this.CENTRO_COMPAS.y})`);
      this.cacheDOM.agujaG.style.transform = `rotate(${angulos.theta_G}deg)`;
    }
    if (this.cacheDOM.agujaT) {
      this.cacheDOM.agujaT.setAttribute('transform', `rotate(${angulos.theta_T}, ${this.CENTRO_COMPAS.x}, ${this.CENTRO_COMPAS.y})`);
      this.cacheDOM.agujaT.style.transform = `rotate(${angulos.theta_T}deg)`;
    }
    if (this.cacheDOM.agujaC) {
      this.cacheDOM.agujaC.setAttribute('transform', `rotate(${angulos.theta_C}, ${this.CENTRO_COMPAS.x}, ${this.CENTRO_COMPAS.y})`);
      this.cacheDOM.agujaC.style.transform = `rotate(${angulos.theta_C}deg)`;
    }
    if (this.cacheDOM.agujaPsi) {
      this.cacheDOM.agujaPsi.setAttribute('transform', `rotate(${angulos.theta_Psi}, ${this.CENTRO_COMPAS.x}, ${this.CENTRO_COMPAS.y})`);
      this.cacheDOM.agujaPsi.style.transform = `rotate(${angulos.theta_Psi}deg)`;
    }

    if (this.cacheDOM.vectorVt) {
      const x1 = this.CENTRO_COMPAS.x;
      const y1 = this.CENTRO_COMPAS.y;
      const x2 = x1 + Math.max(-this.RADIO_COMPAS_FLECHA, Math.min(this.RADIO_COMPAS_FLECHA, vectorVt.x * this.RADIO_COMPAS_FLECHA));
      const y2 = y1 + Math.max(-this.RADIO_COMPAS_FLECHA, Math.min(this.RADIO_COMPAS_FLECHA, vectorVt.y * this.RADIO_COMPAS_FLECHA));

      this.cacheDOM.vectorVt.setAttribute('x1', x1);
      this.cacheDOM.vectorVt.setAttribute('y1', y1);
      this.cacheDOM.vectorVt.setAttribute('x2', x2.toFixed(2));
      this.cacheDOM.vectorVt.setAttribute('y2', y2.toFixed(2));
    }
  }

  posicionarToponimos(posBaricentro, omega) {
    if (!this.cacheDOM.toponymsLayer) return;

    const claves = Object.keys(this.ANCLAJES_REINOS);
    const fragmento = document.createDocumentFragment();

    for (let i = 0; i < claves.length; i++) {
      const clave = claves[i];
      const reino = this.ANCLAJES_REINOS[clave];
      const peso = omega[i] || 0.0;

      const dist = Math.hypot(reino.x - posBaricentro.x, reino.y - posBaricentro.y);
      const factorCercania = Math.max(0.0, 1.0 - (dist / this.RADIO_INFLUENCIA_TOPONIMO));
      const opacidad = Math.min(1.0, 0.20 + (peso * 0.75) + (factorCercania * 0.40));
      const escala = (0.85 + (peso * 0.45) + (factorCercania * 0.15)).toFixed(2);

      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("class", "nodo-toponimo-tendre");
      g.setAttribute("transform", `translate(${reino.x}, ${reino.y}) scale(${escala})`);
      g.style.opacity = opacidad.toFixed(2);
      g.style.transition = "transform 0.45s ease-out, opacity 0.45s ease-out";

      const texto = document.createElementNS("http://www.w3.org/2000/svg", "text");
      texto.setAttribute("class", "toponimo-afectivo");
      texto.setAttribute("text-anchor", "middle");
      texto.setAttribute("dy", "-8");
      texto.textContent = reino.nombre;

      if (peso > 0.35) {
        texto.setAttribute("class", "toponimo-afectivo dominante");
        texto.style.fill = "var(--carmesí-lacra, #8b1e1e)";
        texto.style.fontWeight = "700";

        const circuloSello = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circuloSello.setAttribute("r", "5");
        circuloSello.setAttribute("cy", "6");
        circuloSello.setAttribute("fill", "var(--carmesí-lacra, #8b1e1e)");
        g.appendChild(circuloSello);
      }

      g.appendChild(texto);
      fragmento.appendChild(g);
    }

    this.cacheDOM.toponymsLayer.innerHTML = '';
    this.cacheDOM.toponymsLayer.appendChild(fragmento);
  }

  /**
   * Ciclo unificado: cinemática de compás, proyección en Tendre y modulación acústica.
   *
   * @param {Object} payload Paquete de telemetría de NEXORD
   * @param {Object} payload.estado Anclajes G, T, C
   * @param {Array<number>} payload.omega Ponderación en Delta^13
   * @param {Object} [payload.vectorVt={x:0, y:0}] Vector cinemático de deriva
   * @returns {Object} Diagnóstico consolidado del fotograma
   */
  sincronizar(payload) {
    if (!this.cacheDOM.canvas) this.conectarDOM();

    const { estado, omega, vectorVt = { x: 0, y: 0 } } = payload;

    const angulos = this.calcularAngulosCompas(estado, omega);
    const coordsLienzo = this.calcularCoordenadasBaricentricas(omega);
    const magnitudVt = Math.hypot(vectorVt.x, vectorVt.y);

    // 1. Render Gráfico
    this.renderizarCompas(angulos, vectorVt);
    this.posicionarToponimos(coordsLienzo, omega);

    // 2. Modulación Acústica Dinámica a 432 Hz
    this.modularAcustica(magnitudVt, angulos.theta_Psi);

    return {
      coordenadasLienzo: coordsLienzo,
      angulosCompas: angulos,
      magnitudVt: Number(magnitudVt.toFixed(4)),
      frecuenciaBatimentoHz: Number((this.F0 + Math.min(14.0, magnitudVt * 14.0)).toFixed(2))
    };
  }

  /**
   * Alias de compatibilidad retroactiva para sincronizarVista
   */
  sincronizarVista(payload) {
    const res = this.sincronizar(payload);
    return {
      posicionLienzo: res.coordenadasLienzo,
      angulosCompas: res.angulosCompas,
      magnitudVt: res.magnitudVt,
      frecuenciaBatimentoHz: res.frecuenciaBatimentoHz
    };
  }

  /**
   * Silencia el motor sonoro con rampa suave (muteo de cortesía).
   */
  apagarAudio(duracionRampa = 0.5) {
    if (!this.audioIniciado || !this.audioCtx || !this.nodosAudio.masterGain) return;
    const t = this.audioCtx.currentTime;
    this.nodosAudio.masterGain.gain.cancelScheduledValues(t);
    this.nodosAudio.masterGain.gain.exponentialRampToValueAtTime(0.0001, t + duracionRampa);
  }
}

// Alias de compatibilidad
export const VisordCompassEngine = VisordAcousticCompassEngine;
