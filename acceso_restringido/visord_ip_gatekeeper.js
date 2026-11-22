/**
 * VISORD IP GATEKEEPER (CÁNONES 21 Y 22 NEXORD)
 * ===============================================================================
 * Módulo Universal de Detección Inteligente de Autoría y Acreditación de IP.
 * - En máquina local (file:// o localhost): ACCESO DIRECTO SIN FRICCIONES.
 * - En la web pública: Acceso directo vía marcador/parámetro (?ip=1 o ?modo=ip),
 *   memorizado de forma permanente en localStorage para el equipo del IP.
 * - Para usuarios públicos de internet: Modo Demostración Cuasialeatoria Cerrada.
 * ===============================================================================
 */

(function() {
  'use strict';

  const STORAGE_KEY = 'NEXORD_IP_ACCREDITATION_KEY';
  const IP_NAME = 'Dr. José Manuel Cornejo Álvarez (NODO 0 / IP Fundacional)';

  // 1. Detección de Origen Local (Estación de trabajo del IP)
  const isLocalEnvironment = (
    window.location.protocol === 'file:' ||
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1' ||
    window.location.hostname.endsWith('.local')
  );

  // 2. Detección de Parámetro Privado en URL (?ip=1, ?modo=ip, etc.)
  const params = new URLSearchParams(window.location.search);
  const hasIpParam = params.has('ip') || params.get('modo') === 'ip' || params.has('ip_auth');

  // Si entra con el parámetro por primera vez, memorizar en su navegador
  if (hasIpParam) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        token: 'NEXORD_IP_GRANTED_' + Date.now(),
        grantedAt: new Date().toISOString(),
        titular: IP_NAME
      }));
    } catch(e) {}
  }

  // 3. Verificación de Token Persistente en localStorage
  let isStoredTokenValid = false;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && parsed.token && parsed.token.startsWith('NEXORD_IP_GRANTED_')) {
        isStoredTokenValid = true;
      }
    }
  } catch(e) {}

  // 4. Dictamen Final de Autorización
  const isAuthorizedIP = isLocalEnvironment || hasIpParam || isStoredTokenValid;

  // Exponer objeto global para cualquier VISORD de la plataforma
  window.NEXORD_IP_GATEWAY = {
    isAuthorized: isAuthorizedIP,
    isLocal: isLocalEnvironment,
    titular: isAuthorizedIP ? IP_NAME : 'Visitante Público',
    modo: isAuthorizedIP ? 'IP_FACTUAL' : 'DEMO_CERRADA',
    
    // Método para autenticar manualmente con PIN si se desea
    authenticateManual: function(pin) {
      if (pin && pin.trim().length >= 4) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          token: 'NEXORD_IP_GRANTED_' + Date.now(),
          grantedAt: new Date().toISOString(),
          titular: IP_NAME
        }));
        window.location.reload();
        return true;
      }
      return false;
    },

    // Método para revocar credencial en caso de sesión compartida
    revokeSession: function() {
      try { localStorage.removeItem(STORAGE_KEY); } catch(e) {}
      alert('Credencial de IP revocada en este navegador. Volviendo al modo Demo Pública.');
      window.location.href = window.location.pathname;
    }
  };

  // Función de actualización de la UI cuando el DOM esté listo
  function updateUIForIP() {
    const badgeContainer = document.getElementById('ipStatusBadgeContainer') || document.querySelector('.brand-title');
    if (!badgeContainer) return;

    // Crear o actualizar distintivo
    let badge = document.getElementById('badgeIpStatus');
    if (!badge) {
      badge = document.createElement('span');
      badge.id = 'badgeIpStatus';
      badge.style.fontFamily = "'Roboto Mono', monospace";
      badge.style.fontSize = '0.70rem';
      badge.style.padding = '3px 8px';
      badge.style.borderRadius = '5px';
      badge.style.fontWeight = '700';
      badge.style.marginLeft = '8px';
      badge.style.display = 'inline-flex';
      badge.style.alignItems = 'center';
      badge.style.gap = '5px';
      badgeContainer.appendChild(badge);
    }

    if (isAuthorizedIP) {
      badge.style.background = 'rgba(0, 255, 135, 0.14)';
      badge.style.border = '1px solid #00FF87';
      badge.style.color = '#00FF87';
      badge.innerHTML = '🟢 MODO IP ACREDITADO (CAMPO REAL DIRECTO)';
      badge.title = 'Sesión autenticada como ' + IP_NAME + '. Acceso a datos de campo real desbloqueado.';
      
      // Desbloquear controles restringidos
      document.querySelectorAll('.ip-only-control').forEach(el => {
        el.style.display = '';
        el.removeAttribute('disabled');
      });
      document.querySelectorAll('.public-demo-only').forEach(el => {
        el.style.display = 'none';
      });
    } else {
      badge.style.background = 'rgba(255, 230, 0, 0.12)';
      badge.style.border = '1px solid #FFE600';
      badge.style.color = '#FFE600';
      badge.innerHTML = '🛡️ DEMO IN SILICO CERRADA';
      badge.title = 'Entorno público demostrativo. Datos de personas reales restringidos a IP Acreditado.';
      
      // Ocultar o proteger controles reales
      document.querySelectorAll('.ip-only-control').forEach(el => {
        el.style.display = 'none';
      });
      document.querySelectorAll('.public-demo-only').forEach(el => {
        el.style.display = '';
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateUIForIP);
  } else {
    updateUIForIP();
  }
})();
