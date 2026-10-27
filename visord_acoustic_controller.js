/**
 * ==============================================================================
 * CONTROLADOR: visord_acoustic_controller.js
 * Plataforma: NEXORD / VISORD Engine Platinum (2026)
 * Autor Científico: Dr. José Manuel Cornejo Álvarez (Universitat de Barcelona)
 * Finalidad: Gestiona el desbloqueo del AudioContext mediante el Sello de Lacra
 *            y refresca las lecturas del HUD acústico en cada fotograma.
 * ==============================================================================
 */

export class VisordAcousticController {
  /**
   * @param {VisordAcousticCompassEngine} compassEngine Instancia del motor cinemático-acústico
   */
  constructor(compassEngine) {
    this.engine = compassEngine;

    // Cache de nodos del HUD
    this.btnToggle = document.getElementById('btn-toggle-audio');
    this.lblEstado = document.getElementById('audio-estado-texto');
    this.lblF0 = document.getElementById('val-f0');
    this.lblBatimento = document.getElementById('val-batimento');
    this.lblTension = document.getElementById('val-tension');

    this.activo = false;
    this.vincularEventos();
  }

  vincularEventos() {
    if (!this.btnToggle) return;

    this.btnToggle.addEventListener('click', async () => {
      if (!this.activo) {
        // Despertar AudioContext bajo evento de usuario
        await this.engine.inicializarAudio();
        this.activo = true;

        this.btnToggle.classList.add('resonando');
        this.btnToggle.setAttribute('title', 'Haga clic para silenciar la resonancia');
        
        if (this.lblEstado) {
          this.lblEstado.textContent = 'ACTIVO (432 Hz)';
          this.lblEstado.className = 'valor-estado activo';
        }
      } else {
        // Silenciar motor
        this.engine.apagarAudio(0.4);
        this.activo = false;

        this.btnToggle.classList.remove('resonando');
        this.btnToggle.setAttribute('title', 'Haga clic para despertar la resonancia');

        if (this.lblEstado) {
          this.lblEstado.textContent = 'SILENCIADO';
          this.lblEstado.className = 'valor-estado silenciado';
        }
        
        // Poner telemetría en reposo
        if (this.lblBatimento) this.lblBatimento.textContent = '0.00';
        if (this.lblTension) this.lblTension.textContent = '0%';
      }
    });
  }

  /**
   * Actualiza las cifras del HUD con los cálculos del último fotograma.
   * Invocado inmediatamente después de compas.sincronizar(payload).
   *
   * @param {Object} metricas
   * @param {number} metricas.magnitudVt Tasa de deriva ||VT||
   * @param {number} metricas.theta_Psi Rumbo azimutal de la aguja de régimen
   * @param {number} metricas.frecuenciaBatimentoHz Frecuencia resultante del segundo oscilador
   */
  actualizarHUD(metricas) {
    if (!this.activo) return;

    const deltaF = Math.max(0, metricas.frecuenciaBatimentoHz - this.engine.F0);

    // Tensión hacia el Polo Sur W81 (0% en Norte / 100% en Sur)
    const rad = (metricas.theta_Psi * Math.PI) / 180.0;
    const porcentajeTension = Math.round(((1.0 - Math.cos(rad)) / 2.0) * 100);

    if (this.lblBatimento) {
      this.lblBatimento.textContent = deltaF.toFixed(2);
    }

    if (this.lblTension) {
      this.lblTension.textContent = `${porcentajeTension}%`;
      // Resalte cromático si la tensión de ruptura supera el 60%
      this.lblTension.style.color = porcentajeTension > 60 ? 'var(--carmesí-lacra, #8b1e1e)' : 'inherit';
    }
  }
}
