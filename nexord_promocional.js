/**
 * NEXORD Plataforma Promocional · Scripts Maestros
 * Control de Video Hero 3D, Citas Académicas y Custodia Institucional
 * Versión Canónica 2026
 */

let activeCitationFormat = 'bibtex';

function switchCitationFormat(fmt) {
  activeCitationFormat = fmt;
  const tabBib = document.getElementById('tab-bibtex');
  const tabApa = document.getElementById('tab-apa');
  const tabRis = document.getElementById('tab-ris');
  
  const blockBib = document.getElementById('bibtex-code-block');
  const blockApa = document.getElementById('apa-code-block');
  const blockRis = document.getElementById('ris-code-block');
  const hint = document.getElementById('citation-format-hint');
  
  [tabBib, tabApa, tabRis].forEach(t => {
    if (t) {
      t.style.borderBottomColor = 'transparent';
      t.style.color = 'var(--text-muted)';
    }
  });

  [blockBib, blockApa, blockRis].forEach(b => {
    if (b) b.style.display = 'none';
  });

  if (fmt === 'bibtex') {
    if (tabBib) { tabBib.style.borderBottomColor = 'var(--neon-green)'; tabBib.style.color = 'var(--neon-green)'; }
    if (blockBib) blockBib.style.display = 'block';
    if (hint) {
      hint.setAttribute('data-fmt', 'bibtex');
      hint.innerText = (document.documentElement.lang === 'en')
        ? 'Entry for LaTeX, Overleaf, and compatible citation managers:'
        : 'Entrada para LaTeX, Overleaf y gestores bibliográficos compatibles:';
    }
  } else if (fmt === 'apa') {
    if (tabApa) { tabApa.style.borderBottomColor = 'var(--neon-green)'; tabApa.style.color = 'var(--neon-green)'; }
    if (blockApa) blockApa.style.display = 'block';
    if (hint) {
      hint.setAttribute('data-fmt', 'apa');
      hint.innerText = (document.documentElement.lang === 'en')
        ? 'Citation in standard APA 7th Edition format for reports and theses:'
        : 'Cita en formato estándar APA 7ª Edición para informes y tesis:';
    }
  } else if (fmt === 'ris') {
    if (tabRis) { tabRis.style.borderBottomColor = 'var(--neon-green)'; tabRis.style.color = 'var(--neon-green)'; }
    if (blockRis) blockRis.style.display = 'block';
    if (hint) {
      hint.setAttribute('data-fmt', 'ris');
      hint.innerText = (document.documentElement.lang === 'en')
        ? 'Standard RIS format for direct import into Zotero, Mendeley, and EndNote:'
        : 'Formato RIS estándar para importación directa en Zotero, Mendeley y EndNote:';
    }
  }
}

function toggleBibtexModal(e) {
  if (e && e.preventDefault) e.preventDefault();
  const m = document.getElementById('nexord-bibtex-modal');
  if (!m) return;
  const isOpen = m.classList.contains('open') || m.classList.contains('active') || m.style.display === 'flex';
  if (isOpen) {
    m.classList.remove('open');
    m.classList.remove('active');
    m.style.setProperty('display', 'none', 'important');
    document.body.style.overflow = '';
  } else {
    m.classList.add('open');
    m.style.setProperty('display', 'flex', 'important');
    document.body.style.overflow = 'hidden';
  }
}

// Cerrar modal BibTeX con la tecla Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const m = document.getElementById('nexord-bibtex-modal');
    if (m && (m.classList.contains('open') || m.classList.contains('active') || m.style.display === 'flex')) {
      toggleBibtexModal();
    }
  }
});

function copyActiveCitation() {
  let targetBlock = document.getElementById('bibtex-code-block');
  if (activeCitationFormat === 'apa') targetBlock = document.getElementById('apa-code-block');
  if (activeCitationFormat === 'ris') targetBlock = document.getElementById('ris-code-block');
  
  const btnText = document.getElementById('bibtex-copy-text');
  const btnIcon = document.getElementById('bibtex-copy-icon');
  const status = document.getElementById('bibtex-copy-status');
  if (!targetBlock) return;
  
  const isEn = (document.documentElement.lang === 'en');
  const copiedLabel = isEn ? 'Copied!' : '¡Copiado!';
  const defaultLabel = isEn ? 'Copy to Clipboard' : 'Copiar al Portapapeles';
  const statusLabel = isEn ? `Citation (${activeCitationFormat.toUpperCase()}) copied` : `Cita (${activeCitationFormat.toUpperCase()}) copiada`;

  const text = targetBlock.innerText || targetBlock.textContent;
  navigator.clipboard.writeText(text).then(() => {
    if (btnText) btnText.innerText = copiedLabel;
    if (btnIcon) btnIcon.innerText = '✅';
    if (status) status.innerText = statusLabel;
    setTimeout(() => {
      if (btnText) btnText.innerText = defaultLabel;
      if (btnIcon) btnIcon.innerText = '📋';
      if (status) status.innerText = '';
    }, 2500);
  }).catch(() => {
    const range = document.createRange();
    range.selectNode(targetBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
    if (btnText) btnText.innerText = copiedLabel;
    setTimeout(() => { if (btnText) btnText.innerText = defaultLabel; }, 2500);
  });
}

function handleCustodiaSubmit(e) {
  if (e && e.preventDefault) e.preventDefault();
  const inst = document.getElementById('cust-institution').value.trim();
  const rep = document.getElementById('cust-representative').value.trim();
  const email = document.getElementById('cust-email').value.trim();
  const type = document.getElementById('cust-type').value;
  const msg = document.getElementById('cust-message').value.trim();
  const status = document.getElementById('cust-status');
  const isEn = (document.documentElement.lang === 'en');

  const subject = isEn
    ? encodeURIComponent(`[NEXORD] Institutional Stewardship Proposal - ${inst}`)
    : encodeURIComponent(`[NEXORD] Propuesta de Custodia Institucional - ${inst}`);

  const bodyEs = 
`A la atención del Dr. José Manuel Cornejo Álvarez
Plataforma Científica NEXORD / VISORD Engine
NEXORD Research Initiative · Investigación independiente

Estimado Dr. Cornejo:

Por la presente, nos ponemos en contacto con el equipo promotor de la Plataforma NEXORD en relación al llamamiento de Custodia Institucional y Transferencia Tecnológica.

DATOS DE LA ENTIDAD / CONTACTO:
- Institución: ${inst}
- Representante / Cargo: ${rep}
- Correo institucional: ${email}
- Modalidad de interés: ${type}

DETALLE DE LA PROPUESTA / MOTIVACIÓN:
${msg || 'Deseamos explorar las condiciones de custodia, alojamiento en infraestructura institucional y gobernanza del software NEXORD.'}

Agradecemos de antemano su atención y quedamos a su disposición para coordinar una reunión técnica o presentación institucional.

Atentamente,
${rep}
${inst}`;

  const bodyEn = 
`To the attention of Dr. José Manuel Cornejo Álvarez
NEXORD Scientific Platform / VISORD Engine
NEXORD Research Initiative · Independent Research

Dear Dr. Cornejo:

We hereby contact the promoter team of the NEXORD Platform regarding the Call for Institutional Stewardship and Technology Transfer.

ENTITY / CONTACT DETAILS:
- Institution: ${inst}
- Representative / Title: ${rep}
- Institutional Email: ${email}
- Interest Track: ${type}

PROPOSAL DETAILS / MOTIVATION:
${msg || 'We wish to explore terms of stewardship, institutional infrastructure hosting, and long-term governance of NEXORD software.'}

Thank you in advance for your consideration. We remain available to coordinate a technical briefing or institutional presentation.

Sincerely,
${rep}
${inst}`;

  const body = encodeURIComponent(isEn ? bodyEn : bodyEs);
  const mailtoUrl = `mailto:josmancor@gmail.com?cc=info@nex-ord.org&subject=${subject}&body=${body}`;
  window.location.href = mailtoUrl;

  if (status) {
    status.innerText = isEn
      ? '✅ Email client opened with the preformatted proposal. You may also write directly to info@nex-ord.org'
      : '✅ Cliente de correo abierto con la propuesta preformateada. También puede escribir directamente a info@nex-ord.org';
    setTimeout(() => { status.innerText = ''; }, 6000);
  }
}

function copyCustodiaDraft() {
  const isEn = (document.documentElement.lang === 'en');
  const inst = (document.getElementById('cust-institution') ? document.getElementById('cust-institution').value.trim() : '') || (isEn ? '[Institution/University]' : '[Institución/Universidad]');
  const rep = (document.getElementById('cust-representative') ? document.getElementById('cust-representative').value.trim() : '') || (isEn ? '[Name & Title]' : '[Nombre y Cargo]');
  const email = (document.getElementById('cust-email') ? document.getElementById('cust-email').value.trim() : '') || (isEn ? '[institutional email]' : '[email institucional]');
  const type = document.getElementById('cust-type') ? document.getElementById('cust-type').value : (isEn ? 'Permanent Institutional Stewardship' : 'Custodia y Gobernanza Institucional');
  const msg = (document.getElementById('cust-message') ? document.getElementById('cust-message').value.trim() : '') || (isEn ? 'Formal interest in stewardship and institutional hosting of NEXORD software.' : 'Interés formal en la custodia y alojamiento del software NEXORD.');
  const status = document.getElementById('cust-status');

  const draftEs = 
`A la atención del Dr. José Manuel Cornejo Álvarez
Plataforma Científica NEXORD / VISORD Engine
NEXORD Research Initiative · Investigación independiente

Estimado Dr. Cornejo:

Por la presente, nos ponemos en contacto con el equipo promotor de la Plataforma NEXORD en relación al llamamiento de Custodia Institucional y Transferencia Tecnológica.

DATOS DE LA ENTIDAD / CONTACTO:
- Institución: ${inst}
- Representante / Cargo: ${rep}
- Correo institucional: ${email}
- Modalidad de interés: ${type}

DETALLE DE LA PROPUESTA / MOTIVACIÓN:
${msg}

Agradecemos de antemano su atención y quedamos a su disposición para coordinar una reunión técnica o presentación institucional.

Atentamente,
${rep}
${inst}`;

  const draftEn = 
`To the attention of Dr. José Manuel Cornejo Álvarez
NEXORD Scientific Platform / VISORD Engine
NEXORD Research Initiative · Independent Research

Dear Dr. Cornejo:

We hereby contact the promoter team of the NEXORD Platform regarding the Call for Institutional Stewardship and Technology Transfer.

ENTITY / CONTACT DETAILS:
- Institution: ${inst}
- Representative / Title: ${rep}
- Institutional Email: ${email}
- Interest Track: ${type}

PROPOSAL DETAILS / MOTIVATION:
${msg}

Thank you in advance for your consideration. We remain available to coordinate a technical briefing or institutional presentation.

Sincerely,
${rep}
${inst}`;

  const draft = isEn ? draftEn : draftEs;
  const successMsg = isEn ? '📋 Draft copied to clipboard. Ready to paste into your email.' : '📋 Borrador copiado al portapapeles. Listo para pegar en su correo.';

  navigator.clipboard.writeText(draft).then(() => {
    if (status) {
      status.innerText = successMsg;
      setTimeout(() => { status.innerText = ''; }, 4000);
    }
  }).catch(() => {
    const range = document.createRange();
    const tempDiv = document.createElement('textarea');
    tempDiv.value = draft;
    document.body.appendChild(tempDiv);
    tempDiv.select();
    document.execCommand('copy');
    document.body.removeChild(tempDiv);
    if (status) {
      status.innerText = successMsg;
      setTimeout(() => { status.innerText = ''; }, 4000);
    }
  });
}

/* =========================================================================
   CONTROLADOR VIDEO HERO 3D (REPRODUCCIÓN LIMPIA + AUDIO INFALIBLE)
   ========================================================================= */
function initHeroVideo() {
  const vid = document.getElementById('hero-master-video');
  if (!vid) return;

  const btnPlay = document.getElementById('btn-video-play');
  const btnAudio = document.getElementById('btn-video-audio');
  const btnFs = document.getElementById('btn-video-fs');
  const playIcon = document.getElementById('video-play-icon');
  const playLabel = document.getElementById('video-play-label');
  const audioIcon = document.getElementById('video-audio-icon');
  const audioLabel = document.getElementById('video-audio-label');
  const playerWrap = document.getElementById('hero-player-wrap');

  // Asegurar reproducción única (sin bucle), playsinline y silencio inicial para permitir Autoplay
  vid.loop = false;
  vid.muted = true;
  vid.defaultMuted = true;
  vid.setAttribute('playsinline', '');
  vid.setAttribute('webkit-playsinline', '');
  vid.removeAttribute('loop');

  function updateAudioUI(isMuted) {
    const isEn = (document.documentElement.lang === 'en');
    if (isMuted) {
      if (btnAudio) {
        btnAudio.classList.remove('audio-active');
      }
      if (audioIcon) audioIcon.textContent = '🔇';
      if (audioLabel) audioLabel.textContent = isEn ? 'Enable Audio' : 'Activar Audio';
    } else {
      if (btnAudio) {
        btnAudio.classList.add('audio-active');
      }
      if (audioIcon) audioIcon.textContent = '🔊';
      if (audioLabel) audioLabel.textContent = isEn ? 'Mute Audio' : 'Silenciar Audio';
    }
  }

  function activateSound() {
    vid.muted = false;
    vid.volume = 1.0;
    const playPromise = vid.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        updateAudioUI(false);
      }).catch(err => {
        console.warn("Video sound activate error:", err);
        vid.muted = false;
        vid.volume = 1.0;
        updateAudioUI(false);
      });
    } else {
      updateAudioUI(false);
    }
  }

  function toggleAudio(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (vid.muted) {
      activateSound();
    } else {
      vid.muted = true;
      updateAudioUI(true);
    }
  }

  // Controlador de Reproducción / Pausa
  function togglePlayPause(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (vid.paused || vid.ended) {
      if (vid.ended) {
        vid.currentTime = 0;
      }
      const p = vid.play();
      if (p !== undefined) {
        p.catch(err => console.warn("Video play error:", err));
      }
    } else {
      vid.pause();
    }
  }

  if (btnPlay) {
    btnPlay.addEventListener('click', togglePlayPause);
  }

  if (btnAudio) {
    btnAudio.addEventListener('click', toggleAudio);
  }

  // Pulsar sobre el video conmuta Play / Pausa (salvo si se pulsa sobre botones de control)
  if (playerWrap) {
    playerWrap.addEventListener('click', (e) => {
      if (e.target.closest('.video-ctrl-btn')) {
        return;
      }
      togglePlayPause(e);
    });
  }

  // Sincronizar botones e iconos con el estado real del reproductor
  vid.addEventListener('play', () => {
    const isEn = (document.documentElement.lang === 'en');
    if (playIcon) playIcon.textContent = '⏸️';
    if (playLabel) playLabel.textContent = isEn ? 'Pause' : 'Pausa';
    if (btnPlay) btnPlay.classList.add('playing');
  });

  vid.addEventListener('pause', () => {
    const isEn = (document.documentElement.lang === 'en');
    if (playIcon) playIcon.textContent = '▶️';
    if (playLabel) playLabel.textContent = isEn ? 'Play' : 'Reproducir';
    if (btnPlay) btnPlay.classList.remove('playing');
  });

  vid.addEventListener('ended', () => {
    // Al concluir la reproducción única (sin bucle)
    const isEn = (document.documentElement.lang === 'en');
    if (playIcon) playIcon.textContent = '🔄';
    if (playLabel) playLabel.textContent = isEn ? 'Replay' : 'Repetir';
    if (btnPlay) btnPlay.classList.remove('playing');
  });

  vid.addEventListener('volumechange', () => {
    updateAudioUI(vid.muted);
  });

  // Autoplay continuo y seguro
  function startAutoplaySafe() {
    vid.muted = true;
    const p = vid.play();
    if (p !== undefined) {
      p.catch(() => {
        // En navegadores móviles con políticas estrictas de ahorro de datos
        const oneTouch = () => {
          vid.play().catch(() => {});
          ['touchstart', 'click'].forEach(ev => window.removeEventListener(ev, oneTouch));
        };
        ['touchstart', 'click'].forEach(ev => window.addEventListener(ev, oneTouch, { once: true, passive: true }));
      });
    }
    updateAudioUI(true);
  }

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    startAutoplaySafe();
  } else {
    window.addEventListener('DOMContentLoaded', startAutoplaySafe, { once: true });
  }

  // Pantalla Completa
  if (btnFs) {
    btnFs.addEventListener('click', (e) => {
      e.stopPropagation();
      const wrap = document.getElementById('video-hero-block');
      if (!wrap) return;
      if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        if (wrap.requestFullscreen) wrap.requestFullscreen();
        else if (wrap.webkitRequestFullscreen) wrap.webkitRequestFullscreen();
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
        else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
      }
    });
  }
}

// =============================================================================
// BANDA VERTICAL DE NAVEGACIÓN (FLECHAS SECCIONALES & ACCESOS RÁPIDOS)
// =============================================================================
function initVerticalNavBand() {
  const band = document.getElementById('vertical-nav-band');
  if (!band) return;

  const btnUp = document.getElementById('btn-vnav-up');
  const btnDown = document.getElementById('btn-vnav-down');
  const dots = document.querySelectorAll('.vnav-dot');

  const sectionIds = ['inicio', 'dolor', 'showroom', 'soluciones', 'etica', 'boveda', 'custodia'];
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);

  function getCurrentSectionIndex() {
    const scrollPos = window.scrollY + 160;
    let currentIdx = 0;
    for (let i = 0; i < sections.length; i++) {
      if (sections[i].offsetTop <= scrollPos) {
        currentIdx = i;
      }
    }
    return currentIdx;
  }

  function scrollToSectionIndex(idx) {
    if (idx < 0) idx = 0;
    if (idx >= sections.length) idx = sections.length - 1;
    const target = sections[idx];
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  if (btnUp) {
    btnUp.addEventListener('click', () => {
      const cur = getCurrentSectionIndex();
      scrollToSectionIndex(cur - 1);
    });
  }

  if (btnDown) {
    btnDown.addEventListener('click', () => {
      const cur = getCurrentSectionIndex();
      scrollToSectionIndex(cur + 1);
    });
  }

  // ScrollSpy para actualizar el dot activo
  function updateActiveDot() {
    const curIdx = getCurrentSectionIndex();
    const curId = sections[curIdx] ? sections[curIdx].id : '';
    dots.forEach(d => {
      if (d.getAttribute('data-target') === curId) {
        d.classList.add('active');
      } else {
        d.classList.remove('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveDot, { passive: true });
  updateActiveDot();

  // Navegación con teclado: Alt + Flecha Arriba / Abajo
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
    if (e.altKey && e.key === 'ArrowUp') {
      e.preventDefault();
      const cur = getCurrentSectionIndex();
      scrollToSectionIndex(cur - 1);
    } else if (e.altKey && e.key === 'ArrowDown') {
      e.preventDefault();
      const cur = getCurrentSectionIndex();
      scrollToSectionIndex(cur + 1);
    }
  });
}

// Inicialización reactiva al cargar el DOM
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    initHeroVideo();
    initVerticalNavBand();
  });
} else {
  initHeroVideo();
  initVerticalNavBand();
}

