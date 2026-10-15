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
    if (hint) hint.innerText = 'Entrada para LaTeX, Overleaf y gestores bibliográficos compatibles:';
  } else if (fmt === 'apa') {
    if (tabApa) { tabApa.style.borderBottomColor = 'var(--neon-green)'; tabApa.style.color = 'var(--neon-green)'; }
    if (blockApa) blockApa.style.display = 'block';
    if (hint) hint.innerText = 'Cita en formato estándar APA 7ª Edición para informes y tesis:';
  } else if (fmt === 'ris') {
    if (tabRis) { tabRis.style.borderBottomColor = 'var(--neon-green)'; tabRis.style.color = 'var(--neon-green)'; }
    if (blockRis) blockRis.style.display = 'block';
    if (hint) hint.innerText = 'Formato RIS estándar para importación directa en Zotero, Mendeley y EndNote:';
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
  
  const text = targetBlock.innerText || targetBlock.textContent;
  navigator.clipboard.writeText(text).then(() => {
    if (btnText) btnText.innerText = '¡Copiado!';
    if (btnIcon) btnIcon.innerText = '✅';
    if (status) status.innerText = `Cita (${activeCitationFormat.toUpperCase()}) copiada`;
    setTimeout(() => {
      if (btnText) btnText.innerText = 'Copiar al Portapapeles';
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
    if (btnText) btnText.innerText = '¡Copiado!';
    setTimeout(() => { if (btnText) btnText.innerText = 'Copiar al Portapapeles'; }, 2500);
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

  const subject = encodeURIComponent(`[NEXORD] Propuesta de Custodia Institucional - ${inst}`);
  const body = encodeURIComponent(
`A la atención del Dr. José Manuel Cornejo Álvarez
Plataforma Científica NEXORD / VISORD Engine
Facultat de Psicologia · Universitat de Barcelona (UB)

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
${inst}`
  );

  const mailtoUrl = `mailto:josmancor@gmail.com?cc=info@nexord.org&subject=${subject}&body=${body}`;
  window.location.href = mailtoUrl;

  if (status) {
    status.innerText = '✅ Cliente de correo abierto con la propuesta preformateada. También puede escribir directamente a info@nexord.org';
    setTimeout(() => { status.innerText = ''; }, 6000);
  }
}

function copyCustodiaDraft() {
  const inst = (document.getElementById('cust-institution') ? document.getElementById('cust-institution').value.trim() : '') || '[Institución/Universidad]';
  const rep = (document.getElementById('cust-representative') ? document.getElementById('cust-representative').value.trim() : '') || '[Nombre y Cargo]';
  const email = (document.getElementById('cust-email') ? document.getElementById('cust-email').value.trim() : '') || '[email institucional]';
  const type = document.getElementById('cust-type') ? document.getElementById('cust-type').value : 'Custodia y Gobernanza Institucional';
  const msg = (document.getElementById('cust-message') ? document.getElementById('cust-message').value.trim() : '') || 'Interés formal en la custodia y alojamiento del software NEXORD.';
  const status = document.getElementById('cust-status');

  const draft = 
`A la atención del Dr. José Manuel Cornejo Álvarez
Plataforma Científica NEXORD / VISORD Engine
Facultat de Psicologia · Universitat de Barcelona (UB)

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

  navigator.clipboard.writeText(draft).then(() => {
    if (status) {
      status.innerText = '📋 Borrador copiado al portapapeles. Listo para pegar en su correo.';
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
      status.innerText = '📋 Borrador copiado al portapapeles. Listo para pegar en su correo.';
      setTimeout(() => { status.innerText = ''; }, 4000);
    }
  });
}

/* =========================================================================
   CONTROLADOR VIDEO HERO 3D (MUDO + SUBTÍTULOS ES/EN/ZH/RU + CONTROLES)
   ========================================================================= */
function initHeroVideo() {
  const vid = document.getElementById('hero-master-video');
  if (!vid) return;

  const btnPlay = document.getElementById('btn-video-play');
  const btnAudio = document.getElementById('btn-video-audio');
  const btnSubs = document.getElementById('btn-video-subs');
  const btnFs = document.getElementById('btn-video-fs');
  const playIcon = document.getElementById('video-play-icon');
  const playLabel = document.getElementById('video-play-label');
  const audioIcon = document.getElementById('video-audio-icon');
  const audioLabel = document.getElementById('video-audio-label');
  const subsLabel = document.getElementById('video-subs-label');
  const subsBox = document.getElementById('hero-subtitles-box');
  const subsText = document.getElementById('hero-subtitles-text');
  const wrap = document.getElementById('video-hero-block');

  const subsData = {
    es: [
      { start: 0.5, end: 9.5, text: "En todo grupo humano conviven dos fuerzas invisibles: los lazos de atracción que unen y las tensiones de rechazo que fracturan." },
      { start: 9.8, end: 21.0, text: "🟢 VERDE NEÓN · Vínculos de Atracción Mutua: Afinidad, sinergia y confianza espontánea. El núcleo gravitatorio que cohesiona al equipo." },
      { start: 21.3, end: 32.5, text: "🔴 MAGENTA NEÓN · Vínculos de Rechazo y Fricción: Incompatibilidades soterradas y vetos silenciosos que desgastan y fugan talento." },
      { start: 32.8, end: 44.0, text: "⚪ PERIFERIA · Ostracismo Invisible: Nodos desconectados. El dolor de la exclusión pasiva que los cuestionarios tradicionales jamás detectan." },
      { start: 44.3, end: 55.5, text: "🧭 METAPERCEPCIÓN CRUZADA: ¿Quién cree que le eligen cuando en realidad le rechazan? El punto ciego donde nace el conflicto grupal." },
      { start: 55.8, end: 68.5, text: "NEXORD hace visible lo invisible: Diagnóstico socio-termodinámico no punitivo para sanar la convivencia y potenciar al equipo." }
    ],
    en: [
      { start: 0.5, end: 9.5, text: "In every human group, two invisible forces coexist: bonds of attraction that unite, and rejections that fracture." },
      { start: 9.8, end: 21.0, text: "🟢 NEON GREEN · Mutual Attraction Bonds: Natural affinity, synergy, and trust. The gravitational core holding the team together." },
      { start: 21.3, end: 32.5, text: "🔴 NEON MAGENTA · Rejection & Friction Bonds: Underground hostility and silent vetos that erode teams from within." },
      { start: 32.8, end: 44.0, text: "⚪ PERIPHERY · Invisible Ostracism: Disconnected nodes. The silent pain of passive exclusion that traditional surveys miss." },
      { start: 44.3, end: 55.5, text: "🧭 CROSS METAPERCEPTION: Who believes they are chosen while actually being rejected? The blind spot where group conflict begins." },
      { start: 55.8, end: 68.5, text: "NEXORD makes the invisible visible: Non-punitive socio-thermodynamic diagnosis to heal coexistence and empower teams." }
    ],
    zh: [
      { start: 0.5, end: 9.5, text: "在任何群体中，存在两股无形力量：凝聚团队的吸引力与撕裂团队的排斥力。" },
      { start: 9.8, end: 21.0, text: "🟢 荧光绿 · 互选吸引力纽带：自发信任与协同合作。维系群体的引力核心。" },
      { start: 21.3, end: 32.5, text: "🔴 荧光品红 · 隐蔽排斥力纽带：未表露的敌意与潜意识抵制，悄然破坏团队。" },
      { start: 32.8, end: 44.0, text: "⚪ 边缘节点 · 隐形排斥与孤立：传统问卷永远无法识别的被动疏离。" },
      { start: 44.3, end: 55.5, text: "🧭 交叉元知觉：谁以为自己被选择而实际上被排斥？冲突隐患之源。" },
      { start: 55.8, end: 68.5, text: "NEXORD 令隐形关系透明可见：非惩罚性诊断，赋能组织健康生长。" }
    ],
    ru: [
      { start: 0.5, end: 9.5, text: "В любой группе действуют две скрытые силы: притяжение, которое объединяет, и отторжение, которое разрушает." },
      { start: 9.8, end: 21.0, text: "🟢 НЕОНОВЫЙ ЗЕЛЕНЫЙ · Взаимное притяжение: сплоченность, доверие и гравитационное ядро команды." },
      { start: 21.3, end: 32.5, text: "🔴 НЕОНОВЫЙ МАДЖЕНТА · Скрытое отторжение и трение: скрытая неприязнь, разрушающая команду изнутри." },
      { start: 32.8, end: 44.0, text: "⚪ ПЕРИФЕРИЯ · Невидимый остракизм: изолированные узлы, которые не замечают традиционные тесты." },
      { start: 44.3, end: 55.5, text: "🧭 КРОСС-МЕТАВОСПРИЯТИЕ: кто уверен, что его выбирают, хотя на деле отвергают? Источник конфликтов." },
      { start: 55.8, end: 68.5, text: "NEXORD делает невидимое видимым: непокарательная диагностика для исцеления климата группы." }
    ]
  };

  let currentSubMode = 'es'; // 'es' | 'en' | 'zh' | 'ru' | 'off'

  // Sincronización continua de subtítulos en milisegundos
  vid.addEventListener('timeupdate', () => {
    if (currentSubMode === 'off' || !subsText) {
      if (subsBox) subsBox.style.display = 'none';
      return;
    }
    const t = vid.currentTime;
    const cues = subsData[currentSubMode] || [];
    const activeCue = cues.find(c => t >= c.start && t <= c.end);
    if (activeCue) {
      subsText.textContent = activeCue.text;
      if (subsBox) subsBox.style.display = 'block';
    } else {
      if (subsBox) subsBox.style.display = 'none';
    }
  });

  // Garantizar silenciado nativo en propiedades DOM para que Android autorice el Autoplay
  vid.muted = true;
  vid.defaultMuted = true;
  vid.setAttribute('playsinline', '');
  vid.setAttribute('webkit-playsinline', '');

  // Sincronizar iconos con el estado real del reproductor
  vid.addEventListener('play', () => {
    if (playIcon) playIcon.textContent = '⏸️';
    if (playLabel) playLabel.textContent = 'Pausa';
  });
  vid.addEventListener('pause', () => {
    if (playIcon) playIcon.textContent = '▶️';
    if (playLabel) playLabel.textContent = 'Reproducir';
  });

  // Play / Pausa manual
  if (btnPlay) {
    btnPlay.addEventListener('click', () => {
      if (vid.paused) {
        vid.play().catch(() => {});
      } else {
        vid.pause();
      }
    });
  }

  // Arranque seguro de Autoplay en Android / Chrome
  function launchSafeAutoplay() {
    vid.muted = true;
    const playPromise = vid.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        // En Android con ahorro de batería o datos, el navegador requiere interacción previa
        const unlockOnTouch = () => {
          vid.muted = true;
          vid.play().catch(() => {});
          ['touchstart', 'touchend', 'scroll', 'click'].forEach(evt => {
            window.removeEventListener(evt, unlockOnTouch);
          });
        };
        ['touchstart', 'touchend', 'scroll', 'click'].forEach(evt => {
          window.addEventListener(evt, unlockOnTouch, { passive: true, once: true });
        });
      });
    }
  }

  // Disparar en carga de DOM
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    launchSafeAutoplay();
  } else {
    window.addEventListener('DOMContentLoaded', launchSafeAutoplay, { once: true });
  }

  // Sincronización automática de subtítulos con estado Mute
  function syncSubsWithMute() {
    if (vid.muted) {
      if (currentSubMode === 'off') {
        const prefLang = (localStorage.getItem('nexord_lang') || 'es').toLowerCase();
        currentSubMode = prefLang === 'en' ? 'en' : 'es';
      }
      if (btnSubs) btnSubs.classList.add('active');
      if (subsLabel) subsLabel.textContent = `Subtítulos: ${currentSubMode.toUpperCase()}`;
    }
  }

  // Audio Mudo / Activar
  if (btnAudio) {
    btnAudio.addEventListener('click', () => {
      vid.muted = !vid.muted;
      if (vid.muted) {
        btnAudio.classList.add('active');
        if (audioIcon) audioIcon.textContent = '🔇';
        if (audioLabel) audioLabel.textContent = 'Mudo (Activar)';
        // Regla de Oro: Si mute video -> se activan subtítulos automáticamente
        syncSubsWithMute();
      } else {
        btnAudio.classList.remove('active');
        if (audioIcon) audioIcon.textContent = '🔊';
        if (audioLabel) audioLabel.textContent = 'Audio Activo';
        vid.volume = 1.0;
      }
    });
  }

  // Evento nativo de cambio de volumen/silencio
  vid.addEventListener('volumechange', () => {
    if (vid.muted) {
      syncSubsWithMute();
      if (btnAudio) btnAudio.classList.add('active');
      if (audioIcon) audioIcon.textContent = '🔇';
      if (audioLabel) audioLabel.textContent = 'Mudo (Activar)';
    }
  });

  // Si arranca en mudo (autoplay nativo), forzar subtítulos encendidos
  if (vid.muted) {
    syncSubsWithMute();
  }

  // Alternar Subtítulos (ES -> EN -> OFF) — ZH/RU preservados en subsData para despliegue en nodos federados
  if (btnSubs) {
    btnSubs.addEventListener('click', () => {
      if (currentSubMode === 'es') {
        currentSubMode = 'en';
        if (subsLabel) subsLabel.textContent = 'Subtítulos: EN';
        btnSubs.classList.add('active');
      } else if (currentSubMode === 'en') {
        currentSubMode = 'off';
        if (subsLabel) subsLabel.textContent = 'Subtítulos: OFF';
        btnSubs.classList.remove('active');
        if (subsBox) subsBox.style.display = 'none';
      } else {
        currentSubMode = 'es';
        if (subsLabel) subsLabel.textContent = 'Subtítulos: ES';
        btnSubs.classList.add('active');
      }
    });
  }

  // Pantalla Completa
  if (btnFs && wrap) {
    btnFs.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        if (wrap.requestFullscreen) wrap.requestFullscreen();
        else if (wrap.webkitRequestFullscreen) wrap.webkitRequestFullscreen();
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
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

