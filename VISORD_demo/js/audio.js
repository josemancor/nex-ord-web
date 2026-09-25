/// Motor de Audio Procedural para VISORD (Web Audio API)
// Genera sonidos cinematográficos sin necesidad de archivos externos.

class VisordAudio {
    constructor() {
        try {
            this.ctx = new (window.AudioContext || window.webkitAudioContext)();
            this.masterGain = this.ctx.createGain();
            this.masterGain.connect(this.ctx.destination);
            this.masterGain.gain.value = 0.5;
            this.activeOscillators = [];
        } catch (e) {
            console.warn("AudioContext no disponible:", e);
        }
    }
    
    stopAll() {
        try {
            if (this.masterGain && this.ctx) {
                this.masterGain.gain.setValueAtTime(this.masterGain.gain.value, this.ctx.currentTime);
                this.masterGain.gain.linearRampToValueAtTime(0, this.ctx.currentTime + 0.3);
            }
        } catch(e) {}
        if (this.activeOscillators) {
            this.activeOscillators.forEach(osc => {
                try { osc.stop(this.ctx ? this.ctx.currentTime + 0.3 : 0); } catch(e){}
            });
            this.activeOscillators = [];
        }
    }

    playDrone() {
        try {
            if (!this.ctx) return;
            if (this.ctx.state === 'suspended') {
                this.ctx.resume().catch(e => {});
            }
            if (this.masterGain) {
                this.masterGain.gain.setValueAtTime(0.5, this.ctx.currentTime);
            }
            const osc1 = this.ctx.createOscillator();
            const osc2 = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            
            osc1.type = 'sine';
            osc2.type = 'triangle';
            osc1.frequency.value = 55;
            osc2.frequency.value = 55.5;
            
            osc1.connect(gain);
            osc2.connect(gain);
            gain.connect(this.masterGain);
            
            gain.gain.setValueAtTime(0, this.ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.3, this.ctx.currentTime + 3);
            
            osc1.start();
            osc2.start();
            this.activeOscillators.push(osc1, osc2);
        } catch (e) {
            console.warn("Error reproduciendo drone de audio:", e);
        }
    }
    
    playPulse() {
        try {
            if (!this.ctx) return;
            if (this.ctx.state === 'suspended') {
                this.ctx.resume().catch(e => {});
            }
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            
            osc.type = 'sine';
            osc.frequency.setValueAtTime(110, this.ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(55, this.ctx.currentTime + 0.5);
            
            osc.connect(gain);
            gain.connect(this.masterGain);
            
            gain.gain.setValueAtTime(0.5, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 1);
            
            osc.start();
            osc.stop(this.ctx.currentTime + 1);
        } catch (e) {}
    }
    
    playChime() {
        try {
            if (!this.ctx) return;
            if (this.ctx.state === 'suspended') {
                this.ctx.resume().catch(e => {});
            }
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            
            osc.type = 'sine';
            osc.frequency.value = 880;
            
            osc.connect(gain);
            gain.connect(this.masterGain);
            
            gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 2);
            
            osc.start();
            osc.stop(this.ctx.currentTime + 2);
        } catch (e) {}
    }
    
    playGrandFinale() {
        try {
            if (!this.ctx) return;
            if (this.ctx.state === 'suspended') {
                this.ctx.resume().catch(e => {});
            }
            const osc1 = this.ctx.createOscillator();
            const osc2 = this.ctx.createOscillator();
            const osc3 = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            
            osc1.type = 'sawtooth';
            osc2.type = 'square';
            osc3.type = 'sine';
            
            osc1.frequency.setValueAtTime(30, this.ctx.currentTime);
            osc2.frequency.setValueAtTime(60, this.ctx.currentTime);
            osc3.frequency.setValueAtTime(15, this.ctx.currentTime);
            
            osc1.connect(gain);
            osc2.connect(gain);
            osc3.connect(gain);
            
            const filter = this.ctx.createBiquadFilter();
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(100, this.ctx.currentTime);
            filter.frequency.exponentialRampToValueAtTime(2000, this.ctx.currentTime + 2);
            filter.frequency.exponentialRampToValueAtTime(100, this.ctx.currentTime + 8);
            
            gain.connect(filter);
            filter.connect(this.masterGain);
            
            gain.gain.setValueAtTime(0, this.ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.8, this.ctx.currentTime + 0.5);
            gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 10);
            
            osc1.start();
            osc2.start();
            osc3.start();
            osc1.stop(this.ctx.currentTime + 10);
            osc2.stop(this.ctx.currentTime + 10);
            osc3.stop(this.ctx.currentTime + 10);
        } catch (e) {}
    }

    ensureContext() {
        try {
            if (!this.ctx) {
                const AudioCtx = window.AudioContext || window.webkitAudioContext;
                if (!AudioCtx) return false;
                this.ctx = new AudioCtx();
                this.masterGain = this.ctx.createGain();
                this.masterGain.connect(this.ctx.destination);
                this.masterGain.gain.value = 0.5;
                this.activeOscillators = [];
            }
            if (this.ctx.state === 'suspended') {
                this.ctx.resume().catch(() => {});
            }
            return true;
        } catch (e) {
            return false;
        }
    }

    /**
     * Sonificación Procedural Reactiva para un vínculo individual SMIb
     * @param {number} order - Rango de preferencia (1 = 1º, 2 = 2º, ...)
     * @param {string} sign - Signo ('A' / Mayúscula = Elección, '0' = Neutro, 'a' / Minúscula = Rechazo)
     * @param {number} totalN - Tamaño total del grupo (por defecto 5)
     */
    playLinkStep(order = 1, sign = '0', totalN = 5) {
        try {
            if (!this.ensureContext()) return;
            const now = this.ctx.currentTime;
            const isPos = (typeof sign === 'string' && sign >= 'A' && sign <= 'Z') || sign === '+' || sign === 1 || sign === 'E';
            const isNeg = (typeof sign === 'string' && sign >= 'a' && sign <= 'z') || sign === '-' || sign === -1 || sign === 'R';
            const isZero = (!isPos && !isNeg) || sign === '0';

            if (isPos) {
                // 🔔 ELECCIÓN: Campana armónica cristalina (onda senoidal pura)
                // Pitch descendente según el rango (1º más agudo, ~880 Hz; rangos menores bajan a ~523 Hz)
                const pitches = [880.0, 783.99, 659.25, 587.33, 523.25, 493.88, 440.0, 392.0];
                const rIdx = Math.max(0, Math.min(pitches.length - 1, (order || 1) - 1));
                const freq = pitches[rIdx];

                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now);

                // Segundo armónico sutil para brillo cristalino
                const oscH = this.ctx.createOscillator();
                const gainH = this.ctx.createGain();
                oscH.type = 'sine';
                oscH.frequency.setValueAtTime(freq * 2.0, now);

                gain.gain.setValueAtTime(0.0001, now);
                gain.gain.linearRampToValueAtTime(0.14, now + 0.012);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.35);

                gainH.gain.setValueAtTime(0.0001, now);
                gainH.gain.linearRampToValueAtTime(0.03, now + 0.010);
                gainH.gain.exponentialRampToValueAtTime(0.0001, now + 0.20);

                osc.connect(gain);
                gain.connect(this.masterGain);
                oscH.connect(gainH);
                gainH.connect(this.masterGain);

                osc.start(now);
                osc.stop(now + 0.36);
                oscH.start(now);
                oscH.stop(now + 0.22);

            } else if (isZero) {
                // 🪵 INDIFERENCIA / NEUTRALIDAD ('0'): Tick orgánico amortiguado de madera
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(240, now);
                osc.frequency.exponentialRampToValueAtTime(90, now + 0.045);

                gain.gain.setValueAtTime(0.0001, now);
                gain.gain.linearRampToValueAtTime(0.045, now + 0.004);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.050);

                osc.connect(gain);
                gain.connect(this.masterGain);

                osc.start(now);
                osc.stop(now + 0.055);

            } else if (isNeg) {
                // 🎻 RECHAZO: Resonancia cálida y sosegada en registro grave
                const negPitches = [110.0, 123.47, 138.59, 155.56, 174.61];
                const rIdx = Math.max(0, Math.min(negPitches.length - 1, (order || 1) - 1));
                const freq = negPitches[rIdx];

                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now);

                gain.gain.setValueAtTime(0.0001, now);
                gain.gain.linearRampToValueAtTime(0.10, now + 0.020);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.42);

                osc.connect(gain);
                gain.connect(this.masterGain);

                osc.start(now);
                osc.stop(now + 0.45);
            }
        } catch (e) {
            // Audio Web API silenciado con elegancia
        }
    }

    /**
     * Sonificación Procedural del Cierre Diádico Q81 (Consolidación simultánea)
     * @param {string} q81Type - 'Ee' (mutua elección), 'Rr' (mutuo rechazo), 'Er'/'Re' (oposición/asimetría), '??' (indiferencia)
     */
    playDyadClosure(q81Type = 'Ee') {
        try {
            if (!this.ensureContext()) return;
            const now = this.ctx.currentTime;

            if (q81Type === 'Ee' || (typeof q81Type === 'string' && (q81Type.includes('E') || q81Type.includes('e')))) {
                // 🌟 Acorde Tríada Mayor Arpegiada (C5 - E5 - G5): Consonancia y Victoria Social
                const freqs = [523.25, 659.25, 783.99];
                freqs.forEach((f, idx) => {
                    const t = now + (idx * 0.035);
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(f, t);

                    gain.gain.setValueAtTime(0.0001, t);
                    gain.gain.linearRampToValueAtTime(0.09, t + 0.015);
                    gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.45);

                    osc.connect(gain);
                    gain.connect(this.masterGain);

                    osc.start(t);
                    osc.stop(t + 0.48);
                });
            } else if (q81Type === 'Rr') {
                // ⚡ Intervalo de Fricción Amortiguado (Tritono armónico 110 Hz + 155.5 Hz)
                [110.0, 155.56].forEach(f => {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(f, now);

                    gain.gain.setValueAtTime(0.0001, now);
                    gain.gain.linearRampToValueAtTime(0.08, now + 0.015);
                    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.32);

                    osc.connect(gain);
                    gain.connect(this.masterGain);

                    osc.start(now);
                    osc.stop(now + 0.35);
                });
            } else if (typeof q81Type === 'string' && (q81Type.includes('Er') || q81Type.includes('Re'))) {
                // 🔄 Asimetría / Oposición: Cuarta Justa abierta (220 Hz + 293 Hz)
                [220.0, 293.66].forEach(f => {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(f, now);

                    gain.gain.setValueAtTime(0.0001, now);
                    gain.gain.linearRampToValueAtTime(0.07, now + 0.015);
                    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.38);

                    osc.connect(gain);
                    gain.connect(this.masterGain);

                    osc.start(now);
                    osc.stop(now + 0.40);
                });
            }
        } catch (e) {}
    }

    /**
     * Aviso Psicoacústico de Fricción Oculta (Sistema I255)
     * Emite una micro-pulsación de tensión disonante sutil cuando cristaliza una patología relacional latente.
     * @param {string} dynamicType - Código de patología ('[Ee]', '<Re', '<r', 'R>', '?!', 'E]', '[E', '[e')
     */
    playInvisibleFrictionWarning(dynamicType = '<r') {
        try {
            if (!this.ensureContext()) return;
            const now = this.ctx.currentTime;

            // Micro-pulsación de tensión armónica (146.8 Hz + 155.5 Hz) con batimiento lento
            const freqs = [146.83, 155.56];
            freqs.forEach(f => {
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(f, now);

                gain.gain.setValueAtTime(0.0001, now);
                gain.gain.linearRampToValueAtTime(0.065, now + 0.025);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.48);

                osc.connect(gain);
                gain.connect(this.masterGain);

                osc.start(now);
                osc.stop(now + 0.50);
            });
        } catch (e) {}
    }
}
window.VisordAudio = VisordAudio;
