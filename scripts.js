// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 20, // offset sin navbar fijo superior
                behavior: 'smooth'
            });
        }
    });
});

// Parallax effect for the hero particles background
window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const particlesBg = document.getElementById('particles-bg');
    
    if (particlesBg && scrollY < window.innerHeight) {
        particlesBg.style.transform = `translateY(${scrollY * 0.4}px)`;
        particlesBg.style.opacity = 1 - (scrollY / window.innerHeight);
    }
});

// Simple intersection observer to animate elements fading in
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .showcase-item, .manual-content').forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});

// Video placeholder interaction (for future videos)
document.getElementById('video-overlay-1')?.addEventListener('click', function() {
    // If user adds a real video later, this will hide the overlay and play the video
    const video = this.previousElementSibling;
    if (video && video.tagName === 'VIDEO') {
        this.style.display = 'none';
        video.style.display = 'block';
        video.play().catch(e => {
            console.log("Video source not found or playback prevented.", e);
            this.style.display = 'flex'; // show overlay again if it fails
            video.style.display = 'none';
        });
    }
});

// Lightbox logic
document.addEventListener('DOMContentLoaded', () => {
    // Create lightbox HTML and inject it
    const lightboxHtml = `
        <div id="lightbox" class="lightbox">
            <span class="lightbox-close">&times;</span>
            <img class="lightbox-content" id="lightbox-img" src="" alt="Ampliada">
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', lightboxHtml);

    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');

    // Make gallery images and showcase videos clickable
    document.querySelectorAll('.gallery-img, .image-placeholder img, video').forEach(media => {
        media.classList.add('clickable-media');
        media.addEventListener('click', function(e) {
            // only handle images for now (videos have controls)
            if (this.tagName === 'IMG') {
                lightbox.classList.add('active');
                lightboxImg.src = this.src;
            }
        });
    });

    closeBtn.addEventListener('click', () => {
        lightbox.classList.remove('active');
    });

    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg) {
            lightbox.classList.remove('active');
        }
    });
});

// Toggle profundizacion sections (Accordions)
window.toggleProf = function(id, returnId = null) {
    const targetSection = document.getElementById(id);
    const allSections = document.querySelectorAll('.prof-section');
    
    const isVisible = targetSection.style.display === 'block';
    
    allSections.forEach(section => {
        section.style.display = 'none';
    });
    
    if (!isVisible) {
        targetSection.style.display = 'block';
        window.scrollTo({
            top: targetSection.offsetTop - 80,
            behavior: 'smooth'
        });
    } else {
        if (returnId) {
             const returnEl = document.getElementById(returnId);
             if (returnEl) {
                 window.scrollTo({
                     top: returnEl.offsetTop - 80,
                     behavior: 'smooth'
                 });
                 return;
             }
        }
        
        const engineeringSection = targetSection.previousElementSibling;
        window.scrollTo({
            top: engineeringSection ? engineeringSection.offsetTop - 50 : 0,
            behavior: 'smooth'
        });
    }
};


window.openLightbox = function(src) {
    const lightbox = document.getElementById('global-lightbox');
    const img = document.getElementById('global-lightbox-img');
    if (lightbox && img) {
        img.src = src;
        lightbox.style.display = 'flex';
    }
};


// Función maestra para navegación en el Menú de Lectura
window.openSection = function(id) {
    const el = document.getElementById(id);
    if (!el) return;
    
    // Si la sección es desplegable (.prof-section), asegurar visibilidad
    if (el.classList.contains('prof-section')) {
        el.style.display = 'block';
    }
    
    const yOffset = -20;
    const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
    window.scrollTo({ top: y, behavior: 'smooth' });
    
    // Si estamos en vista móvil, cerrar el menú desplegable tras pulsar
    const menu = document.getElementById('reading-nav');
    if (menu && window.innerWidth <= 1024) {
        menu.classList.remove('menu-open');
    }
};

window.toggleReadingMenu = function() {
    const menu = document.getElementById('reading-nav');
    if (menu) {
        menu.classList.toggle('menu-open');
    }
};

// ScrollSpy: Sincronización del paso activo en el Menú de Lectura
window.addEventListener('scroll', () => {
    const sectionIds = [
        'hero',
        'about',
        'prof-termodinamica',
        'prof-figuras',
        'prof-rigor',
        'modules',
        'prof-galeria',
        'manual',
        'portales-visord',
        'bsoc-cta',
        'community'
    ];
    
    let current = '';
    const scrollPos = window.scrollY + 160;
    
    sectionIds.forEach(id => {
        const el = document.getElementById(id);
        if (el && el.offsetTop <= scrollPos && el.style.display !== 'none') {
            current = id;
        }
    });
    
    document.querySelectorAll('.vertical-reading-menu .nav-step').forEach(step => {
        const target = step.getAttribute('data-target');
        if (target === current || (target === 'about' && (current === 'hero' || current === '')) || (target === 'prof-galeria' && current === 'modules')) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
});

window.activatePresentation = function(e) {
    if (e && typeof e.preventDefault === 'function') {
        e.preventDefault();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // Cerrar menú móvil si estuviera desplegado
    const menu = document.getElementById('reading-nav');
    if (menu && menu.classList.contains('menu-open')) {
        menu.classList.remove('menu-open');
    }

    // Efecto visual: pulso neón sobre la tarjeta de presentación
    const heroCard = document.querySelector('.hero-content');
    if (heroCard) {
        heroCard.style.transition = 'box-shadow 0.4s ease, border-color 0.4s ease, transform 0.4s ease';
        heroCard.style.borderColor = '#00FF87';
        heroCard.style.boxShadow = '0 0 50px rgba(0, 255, 135, 0.45), 0 24px 60px rgba(0, 0, 0, 0.85)';
        heroCard.style.transform = 'scale(1.008)';
        setTimeout(() => {
            heroCard.style.borderColor = 'rgba(56, 189, 248, 0.35)';
            heroCard.style.boxShadow = '0 24px 60px rgba(0, 0, 0, 0.75), 0 0 35px rgba(0, 162, 255, 0.15)';
            heroCard.style.transform = 'scale(1)';
        }, 800);
    }
    
    // Activar audio/locución institucional de presentación
    if (typeof toggleHeroAudio === 'function') {
        if (!heroAudioPlaying) {
            toggleHeroAudio();
        }
    }
};

// Auto-activación si se accede mediante hash #hero o parámetro ?presentacion=1
window.addEventListener('DOMContentLoaded', () => {
    if (window.location.hash === '#hero' || window.location.search.includes('presentacion=1')) {
        setTimeout(() => {
            if (typeof window.activatePresentation === 'function') {
                window.activatePresentation();
            }
        }, 500);
    }
});

// =========================================================================
// MANDO UNIVERSAL MINIMALISTA (ACCIONES PARA PORTADA PRINCIPAL)
// =========================================================================
if (typeof window.navigateStep !== 'function') {
    window.navigateStep = function(dir) {
        if (dir > 0) {
            // En Portada Principal única, avanzar lleva directamente a Nivel 1
            window.location.href = "nivel1_intuitivo.html";
        } else {
            window.scrollTo({ top: 0, behavior: "smooth" });
        }
    };
}

window.handleSalirPlatform = function() {
    if (confirm("¿Desea cerrar la sesión y salir del ecosistema NEXORD?")) {
        window.location.href = "about:blank";
    }
};

// Escucha de teclado para navegación fluida
window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return;
    if (e.key === 'ArrowDown' || e.key === 'PageDown') {
        navigateStep(1);
    } else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
        navigateStep(-1);
    }
});

// =========================================================================
// REPRODUCTOR DE AUDIO / LOCUCIÓN INSTITUCIONAL DE PORTADA (NEXORD)
// =========================================================================
let heroAudioPlaying = false;
let heroSpeechUtter = null;

function getOptimalSpanishVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    return voices.find(v => (v.lang.startsWith('es') || v.lang.includes('ES')) && 
              (v.name.includes('Natural') || v.name.includes('Neural') || v.name.includes('Premium') || v.name.includes('Google') || v.name.includes('Jorge') || v.name.includes('Diego') || v.name.includes('Carlos') || v.name.includes('Paulina') || v.name.includes('Monica') || v.name.includes('Helena') || v.name.includes('Laura') || v.name.includes('Mónica')))
        || voices.find(v => v.lang.startsWith('es') || v.lang.includes('ES'))
        || (voices.length > 0 ? voices[0] : null);
}

// Pre-cargar voces y desbloquear síntesis en la primera interacción
if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        try { window.speechSynthesis.getVoices(); } catch(e){}
    };
    try { window.speechSynthesis.getVoices(); } catch(e){}

    const unlockSpeechEngine = () => {
        try {
            if (window.speechSynthesis.paused) {
                window.speechSynthesis.resume();
            }
        } catch(e){}
    };
    window.addEventListener('click', unlockSpeechEngine, { once: true });
    window.addEventListener('touchstart', unlockSpeechEngine, { once: true });
}

function playHeroChime() {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        if (ctx.state === "suspended") {
            ctx.resume();
        }
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.10);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.22);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.50);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.50);
    } catch(e) {}
}

window.toggleHeroAudio = function() {
    playHeroChime(); // Sonido instantáneo garantizado al pulsar

    const btn = document.getElementById("btn-hero-audio");
    const icon = document.getElementById("hero-audio-icon");
    const text = document.getElementById("hero-audio-text");

    if (!("speechSynthesis" in window)) {
        return;
    }

    function syncHeroNavPodUI(isPlaying) {
        const navBtn = document.getElementById("nav-pod-btn-play");
        const navIcon = document.getElementById("nav-pod-play-icon");
        if (navIcon) navIcon.textContent = isPlaying ? "⏸" : "▶";
        if (navBtn) {
            navBtn.classList.toggle("playing", isPlaying);
            navBtn.title = isPlaying ? "Pausar Presentación (Play/Stop)" : "Reproducir Presentación (Play/Stop)";
        }
    }

    if (heroAudioPlaying) {
        window.speechSynthesis.cancel();
        heroAudioPlaying = false;
        if (btn) btn.classList.remove("playing");
        if (icon) icon.textContent = "🔊";
        if (text) text.textContent = "Escuchar Presentación";
        window._heroActiveUtterance = null;
        syncHeroNavPodUI(false);
        return;
    }

    window.speechSynthesis.cancel();

    const locucionTexto = "Bienvenido a NEXORD: Sociometría Ordinal Computacional. Hacia una Física de lo Grupal. Ecosistema científico diseñado para cartografiar y cuantificar la dinámica relacional y socio-termodinámica de los colectivos humanos.";
    
    const utter = new SpeechSynthesisUtterance(locucionTexto);
    window._heroActiveUtterance = utter;
    utter.lang = "es-ES";

    const esVoice = getOptimalSpanishVoice();
    if (esVoice) utter.voice = esVoice;

    utter.rate = 0.82;
    utter.pitch = 0.95;
    utter.volume = 1.0;

    utter.onstart = () => {
        heroAudioPlaying = true;
        if (btn) btn.classList.add("playing");
        if (icon) icon.textContent = "❚❚";
        if (text) text.textContent = "Pausar Locución";
        syncHeroNavPodUI(true);
    };

    utter.onend = () => {
        heroAudioPlaying = false;
        if (btn) btn.classList.remove("playing");
        if (icon) icon.textContent = "🔊";
        if (text) text.textContent = "Escuchar Presentación";
        window._heroActiveUtterance = null;
        syncHeroNavPodUI(false);
    };

    utter.onerror = () => {
        heroAudioPlaying = false;
        if (btn) btn.classList.remove("playing");
        if (icon) icon.textContent = "🔊";
        if (text) text.textContent = "Escuchar Presentación";
        window._heroActiveUtterance = null;
        syncHeroNavPodUI(false);
    };

    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
    }

    setTimeout(() => {
        window.speechSynthesis.speak(utter);
    }, 120);
};

// Cancelar locución de cabecera si el usuario navega
window.addEventListener('beforeunload', () => {
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
});

window.toggleUniversalNavPodPlay = function() {
    if (typeof togglePlayComplex === 'function') {
        togglePlayComplex();
    } else if (typeof toggleMoviolaPlay === 'function') {
        toggleMoviolaPlay();
    } else if (typeof toggleNavPodPlayWaves === 'function') {
        toggleNavPodPlayWaves();
    } else if (typeof toggleNavPodPlayAcuario === 'function') {
        toggleNavPodPlayAcuario();
    } else if (typeof toggleNavPodPlayPentagrama === 'function') {
        toggleNavPodPlayPentagrama();
    } else if (typeof toggleHeroAudio === 'function') {
        toggleHeroAudio();
    }
};

