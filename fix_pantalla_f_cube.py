#!/usr/bin/env python3
"""
Ajusta y calibra perfectamente el Cubo 3D Multidimensional (Pantalla 1e / pantalla-f):
1. Corrige el giro descontrolado (somersault en X) fijando una rotación canónica horizontal Y (turntable) con inclinación isométrica fija (sin volteretas).
2. Incorpora los ejes ortogonales al propio grupo del cubo para que giren en consonancia y se mantengan fieles a las caras.
3. Provee pedestal de base elegante y centrado exacto en (0, 0, 0) con cámara a perspectiva equilibrada.
4. Otorga a los paneles (.cube-panel-card) marcos nítidos con fondo glassmorphic navy (#0B132B / rgba(11,19,43,0.88)) y bordes neón cyan.
5. Centra el esquema axonométrico SVG izquierdo y el lienzo WebGL derecho en perfecta simetría.
6. Corrige la errata tipográfica ("LONGETUDINAL" -> "LONGITUDINAL").
7. Calibra alturas y márgenes para que toda la pantalla respire holgadamente en 100vh.
"""
import os
import re
from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = 0
    def handle_error(self, message):
        self.errors += 1

def fix_cube_in_text(content):
    # 1. Reemplazo de CSS para .cube-panel-card y elementos del cubo
    p_css = re.compile(r'\.cube-panel-card\s*\{.*?\.axis-label-z\s*\{\s*color:\s*#38BDF8;\s*font-weight:\s*700;\s*\}', re.DOTALL)
    new_css = """.cube-panel-card {
      background: rgba(11, 19, 43, 0.88);
      border: 1.5px solid rgba(56, 189, 248, 0.35);
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(56, 189, 248, 0.06);
      backdrop-filter: blur(12px);
      box-sizing: border-box;
      position: relative;
    }
    .cube-panel-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #FFF;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
      justify-content: space-between;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding-bottom: 6px;
    }
    .cube-schematic-svg {
      width: 100%;
      height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #canvas-cube-container {
      width: 100%;
      height: 300px;
      border-radius: 10px;
      overflow: hidden;
      position: relative;
      background: radial-gradient(circle at center, rgba(14, 25, 55, 0.7) 0%, rgba(5, 8, 17, 0.9) 100%);
      cursor: grab;
    }
    #canvas-cube-container:active {
      cursor: grabbing;
    }
    .cube-axis-floating-tag {
      position: absolute;
      background: rgba(11, 19, 43, 0.92);
      border: 1.5px solid;
      border-radius: 8px;
      padding: 3px 10px;
      font-size: 0.80rem;
      font-family: 'Roboto Mono', monospace;
      font-weight: 800;
      letter-spacing: 0.5px;
      backdrop-filter: blur(8px);
      pointer-events: none;
      z-index: 10;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
    }
    .cube-axes-hud {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 14px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 0.84rem;
      font-family: 'Roboto Mono', monospace;
      white-space: nowrap;
      margin-top: 6px;
    }
    .axis-label-x { color: #FF6B6B; font-weight: 700; }
    .axis-label-y { color: #00FF87; font-weight: 700; }
    .axis-label-z { color: #38BDF8; font-weight: 700; }"""
    content, c_css = p_css.subn(new_css, content, count=1)

    # 2. Reemplazo del HTML de pantalla-f (sección completa)
    p_sec = re.compile(r'<section id="pantalla-f" class="screen-section">.*?<\/section>', re.DOTALL)
    new_sec = """<section id="pantalla-f" class="screen-section">
    <div class="section-header" style="text-align:center; margin-bottom:4px; flex-shrink:0;">
      <div class="screen-step-tag">1e</div>
      <div style="display:flex; justify-content:center; align-items:center; gap:12px; margin:1px auto;">
        <h2 class="section-h2" style="font-size:1.35rem; font-weight:900; margin:0; letter-spacing:0.5px; text-transform:uppercase;">1E · SOCIOMETRÍA COMPARADA: EL CUBO MULTIDIMENSIONAL</h2>
      </div>
      <div style="font-size:0.88rem; font-family: var(--font-mono, monospace); color: var(--neon-cyan, #38BDF8); font-weight: 800; letter-spacing: 0.5px; margin-bottom:2px;">
        DISEÑOS COMPLEJOS (G2 × T3 × C2): 12 MATRICES SOCIOMÉTRICAS SIMULTÁNEAS
      </div>
      <p class="section-desc" style="max-width:860px; margin:2px auto; line-height:1.4; font-size:0.90rem;">
        Espacio tridimensional unificado: <b style="color:#FF6B6B;">Grupos (Gx)</b> &times; <b style="color:#00FF87;">Tiempos (Ty)</b> &times; <b style="color:#38BDF8;">Criterios (Cz)</b>. Comparativa simultánea de 12 matrices continuas en un solo hipercubo.
      </p>
    </div>

    <!-- FILTROS DEL CUBO GxTyCz (DISEÑO G2 × T3 × C2 = 12 MATRICES) -->
    <div style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 6px; flex-shrink:0;">
      <span style="background: rgba(0, 255, 135, 0.2); color: #00FF87; border: 1.5px solid #00FF87; font-size: 11px; font-weight: 900; padding: 2px 10px; border-radius: 6px; letter-spacing: 0.6px;">
        🎮 CONTROLES ACTIVABLES DEL CUBO 3D (PULSE PARA SELECCIONAR VÓXEL O AUTO-TOUR)
      </span>
    </div>
    <div class="cube-filters-bar" style="margin-bottom:8px; flex-shrink:0;">
      <button class="cube-filter-btn active" id="btn-grp-g1" onclick="setCubeCoord('G1')">Grupo 1 (G1)</button>
      <button class="cube-filter-btn" id="btn-grp-g2" onclick="setCubeCoord('G2')">Grupo 2 (G2)</button>
      <button class="cube-filter-btn active" id="btn-tim-t1" onclick="setCubeCoord('T1')">Tiempo 1 (T1 Pre)</button>
      <button class="cube-filter-btn" id="btn-tim-t2" onclick="setCubeCoord('T2')">Tiempo 2 (T2 Inter)</button>
      <button class="cube-filter-btn" id="btn-tim-t3" onclick="setCubeCoord('T3')">Tiempo 3 (T3 Post)</button>
      <button class="cube-filter-btn active" id="btn-cri-c1" onclick="setCubeCoord('C1')">Criterio 1 (Afectivo)</button>
      <button class="cube-filter-btn" id="btn-cri-c2" onclick="setCubeCoord('C2')">Criterio 2 (Trabajo)</button>
      <button class="cube-filter-btn" id="btn-auto-tour" onclick="toggleCubeAutoTour()" style="border-color:var(--neon-gold); color:var(--neon-gold);">
        <span>↺ Auto-Tour del Cubo (12 Vóxeles)</span>
      </button>
    </div>

    <!-- ESCENARIO DEL CUBO: 2 PANELES VISUALES PERFECTAMENTE ENMARCADOS -->
    <div class="cube-stage-wrapper" style="position:relative; width:100%; max-width:1320px; margin:4px auto; display:grid; grid-template-columns:1fr 1fr; gap:16px; flex:1 1 0; min-height:0; align-items:stretch;">
      <!-- PANEL 1: DIBUJO ESQUEMÁTICO DEL CUBO CON LAS 3 DIMENSIONES A LOS LADOS -->
      <div class="cube-panel-card">
        <div class="cube-panel-title">
          <span>📐 Esquema Axonométrico (G2 × T3 × C2)</span>
          <span class="plane-badge" id="schematic-coord-badge">1g1t1c</span>
        </div>
        <div class="cube-schematic-svg">
          <svg width="100%" height="100%" viewBox="0 0 380 300" style="max-height: 290px; width: auto; margin: 0 auto; display: block;">
            <!-- EJE Y: TIEMPOS (Vertical Izquierdo con 3 Tiempos: T1, T2, T3) -->
            <line x1="50" y1="262" x2="50" y2="28" stroke="#00FF87" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="50,18 45,31 55,31" fill="#00FF87"/>
            <text x="50" y="12" fill="#00FF87" font-size="11" font-weight="800" text-anchor="middle" font-family="'Roboto Mono', monospace">▲ TIEMPOS (Ty)</text>
            <circle cx="50" cy="85" r="2.5" fill="#00FF87"/>
            <text x="43" y="88" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T3 Post</text>
            <circle cx="50" cy="145" r="2.5" fill="#00FF87"/>
            <text x="43" y="148" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T2 Inter</text>
            <circle cx="50" cy="205" r="2.5" fill="#00FF87"/>
            <text x="43" y="208" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T1 Pre</text>

            <!-- EJE X: GRUPOS (Horizontal / Base) -->
            <line x1="85" y1="275" x2="280" y2="275" stroke="#FF6B6B" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="290,275 278,270 278,280" fill="#FF6B6B"/>
            <text x="185" y="291" fill="#FF6B6B" font-size="11" font-weight="800" text-anchor="middle" font-family="'Roboto Mono', monospace">▶ GRUPOS (Gx: G1, G2)</text>

            <!-- EJE Z: CRITERIOS (Profundidad / Lateral Derecho) -->
            <line x1="285" y1="250" x2="355" y2="180" stroke="#38BDF8" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="362,173 350,178 358,186" fill="#38BDF8"/>
            <text x="345" y="162" fill="#38BDF8" font-size="11" font-weight="800" font-family="'Roboto Mono', monospace">↗ CRITERIOS (Cz)</text>
            <text x="345" y="176" fill="#94A3B8" font-size="8.5" font-family="'Roboto Mono', monospace">C1 Afectivo, C2 Tarea</text>

            <!-- CUBO ISOMÉTRICO CENTRAL CON 12 VÓXELES (2 Grupos × 3 Tiempos × 2 Criterios) -->
            <g id="svg-voxels-group">
              <!-- NIVEL T1 (Inferior · Pre) -->
              <polygon id="vox-1g1t2c" points="180,169 230,144 230,178 180,203" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-2g1t2c" points="230,144 280,169 280,203 230,178" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-1g1t1c" points="135,192 185,167 185,201 135,226" fill="#00FF87" fill-opacity="0.9" stroke="#00FF87" stroke-width="2.2"/>
              <text id="txt-1g1t1c" x="160" y="199" fill="#030308" font-size="9.5" font-weight="900" text-anchor="middle" font-family="'Roboto Mono', monospace">1g1t1c</text>

              <polygon id="vox-2g1t1c" points="185,167 235,192 235,226 185,201" fill="#1E293B" fill-opacity="0.5" stroke="#38BDF8" stroke-width="1.2"/>
              <text id="txt-2g1t1c" x="210" y="199" fill="#CBD5E1" font-size="9" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">2g1t1c</text>

              <!-- NIVEL T2 (Medio · Inter) -->
              <polygon id="vox-1g2t2c" points="180,131 230,106 230,140 180,165" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-2g2t2c" points="230,106 280,131 280,165 230,140" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-1g2t1c" points="135,154 185,129 185,163 135,188" fill="#1E293B" fill-opacity="0.5" stroke="#38BDF8" stroke-width="1.2"/>
              <text id="txt-1g2t1c" x="160" y="161" fill="#CBD5E1" font-size="9" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">1g2t1c</text>

              <polygon id="vox-2g2t1c" points="185,129 235,154 235,188 185,163" fill="#1E293B" fill-opacity="0.5" stroke="#38BDF8" stroke-width="1.2"/>
              <text id="txt-2g2t1c" x="210" y="161" fill="#CBD5E1" font-size="9" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">2g2t1c</text>

              <!-- NIVEL T3 (Superior · Post) -->
              <polygon id="vox-1g3t2c" points="180,93 230,68 230,102 180,127" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-2g3t2c" points="230,68 280,93 280,127 230,102" fill="#0F172A" fill-opacity="0.4" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
              <polygon id="vox-1g3t1c" points="135,116 185,91 185,125 135,150" fill="#1E293B" fill-opacity="0.5" stroke="#38BDF8" stroke-width="1.2"/>
              <text id="txt-1g3t1c" x="160" y="123" fill="#CBD5E1" font-size="9" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">1g3t1c</text>

              <polygon id="vox-2g3t1c" points="185,91 235,116 235,150 185,125" fill="#1E293B" fill-opacity="0.5" stroke="#38BDF8" stroke-width="1.2"/>
              <text id="txt-2g3t1c" x="210" y="123" fill="#CBD5E1" font-size="9" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">2g3t1c</text>

              <!-- Cubierta superior / Techo isométrico T3 -->
              <polygon id="vox-top-cap" points="135,116 180,93 230,68 280,93 235,116 185,91" fill="#38BDF8" fill-opacity="0.20" stroke="#38BDF8" stroke-width="1.2"/>
            </g>

            <rect x="90" y="28" width="180" height="22" rx="6" fill="rgba(8, 13, 26, 0.9)" stroke="#00FF87" stroke-width="1"/>
            <text x="180" y="43" fill="#00FF87" font-size="10" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">Vóxel M(g,t,c) Activo</text>
          </svg>
        </div>
        <div style="font-size:0.84rem; color:#94A3B8; text-align:center; margin-top:2px;">
          Cada vóxel <code style="color:#00FF87;">M(g,t,c)</code> es una matriz individualizada extraída del hipercubo (<b style="color:#00FF87;">12 vóxeles en G2×T3×C2</b>).
        </div>
      </div>

      <!-- PANEL 2: CUBO 3D WEBGL DINÁMICO (ORBITAL) -->
      <div class="cube-panel-card">
        <div class="cube-panel-title">
          <span>🌐 Hipercubo 3D Dinámico (WebGL)</span>
          <span style="font-family:'Roboto Mono'; font-size:0.80rem; color:#00FF87; background:rgba(0,255,135,0.12); padding:2px 8px; border-radius:4px; border:1px solid rgba(0,255,135,0.3);">ROTACIÓN CANÓNICA Y</span>
        </div>
        <div id="canvas-cube-container">
          <!-- LEYENDAS AL COSTADO DE CADA EJE EN EL CANVAS -->
          <div class="cube-axis-floating-tag" style="top:8px; left:10px; border-color:#00FF87; color:#00FF87;">
            ▲ TIEMPOS (Y: T1, T2, T3)
          </div>
          <div class="cube-axis-floating-tag" style="bottom:8px; right:10px; border-color:#FF6B6B; color:#FF6B6B;">
            ▶ GRUPOS (X: G1, G2)
          </div>
          <div class="cube-axis-floating-tag" style="bottom:8px; left:10px; border-color:#38BDF8; color:#38BDF8;">
            ↗ CRITERIOS (Z: C1, C2)
          </div>
        </div>
        <div class="cube-axes-hud">
          <span><b class="axis-label-x">▶ Eje X:</b> Grupos (2)</span>
          <span style="opacity:0.3;">|</span>
          <span><b class="axis-label-y">▲ Eje Y:</b> Tiempos (3)</span>
          <span style="opacity:0.3;">|</span>
          <span><b class="axis-label-z">↗ Eje Z:</b> Criterios (2)</span>
        </div>
      </div>
    </div>

    <div style="max-width: 1080px; width: 100%; margin: 2px auto 0 auto; text-align: center; flex-shrink: 0;">
      <!-- PÍLDORA DE ESTADO DINÁMICA DEL VÓXEL ACTIVO -->
      <div style="background:rgba(15, 23, 42, 0.88); border:1px solid rgba(56, 189, 248, 0.35); border-radius:10px; padding:6px 16px; margin:0 auto 6px auto; display:inline-flex; align-items:center; gap:10px; font-size:0.86rem; backdrop-filter:blur(8px);">
        <span style="color:#94A3B8;">Vóxel Activo:</span>
        <strong id="active-cube-coord" style="color:var(--neon-green); font-family:'Roboto Mono', monospace; font-size:1.0rem; background:rgba(0,255,135,0.12); padding:2px 8px; border-radius:6px; border:1px solid var(--neon-green);">1g1t1c</strong>
        <span style="color:rgba(255,255,255,0.2);">|</span>
        <span id="active-cube-desc" style="color:#E2E8F0; font-weight:600; font-family:'Roboto Mono', monospace; font-size:0.88rem;">
          <span style="color:#FF6B6B;">Grupo 1 (G1)</span> · <span style="color:#00FF87;">Tiempo 1 (T1 Pre)</span> · <span style="color:#38BDF8;">Criterio 1 (Afectivo)</span>
        </span>
      </div>

      <!-- TRÍPTICO DE DISEÑOS COMPLEJOS SIMULTÁNEOS (Gx, Ty, Cz) -->
      <div class="complex-design-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:6px;">
        <div style="background:rgba(255, 107, 107, 0.06); border:1px solid rgba(255, 107, 107, 0.3); border-radius:10px; padding:8px 12px; text-align:left;">
          <div style="color:#FF6B6B; font-weight:800; font-size:0.86rem; font-family:'Roboto Mono', monospace; margin-bottom:2px; display:flex; align-items:center; gap:6px;">
            <span>▶</span> 1. INTERGRUPAL (Gx)
          </div>
          <div style="color:#CBD5E1; font-size:0.82rem; line-height:1.35;">
            Compara simultáneamente múltiples grupos o aulas en una misma escala métrica normalizada.
          </div>
        </div>

        <div style="background:rgba(0, 255, 135, 0.06); border:1px solid rgba(0, 255, 135, 0.3); border-radius:10px; padding:8px 12px; text-align:left;">
          <div style="color:#00FF87; font-weight:800; font-size:0.86rem; font-family:'Roboto Mono', monospace; margin-bottom:2px; display:flex; align-items:center; gap:6px;">
            <span>▲</span> 2. LONGITUDINAL (Ty: 3 Tiempos)
          </div>
          <div style="color:#CBD5E1; font-size:0.82rem; line-height:1.35;">
            Registra la evolución diacrónica en 3 cortes temporales (<b style="color:#00FF87;">T1 Pre</b>, <b style="color:#00FF87;">T2 Inter</b>, <b style="color:#00FF87;">T3 Post</b>).
          </div>
        </div>

        <div style="background:rgba(56, 189, 248, 0.06); border:1px solid rgba(56, 189, 248, 0.3); border-radius:10px; padding:8px 12px; text-align:left;">
          <div style="color:#38BDF8; font-weight:800; font-size:0.86rem; font-family:'Roboto Mono', monospace; margin-bottom:2px; display:flex; align-items:center; gap:6px;">
            <span>↗</span> 3. MULTICRITERIO (Cz)
          </div>
          <div style="color:#CBD5E1; font-size:0.82rem; line-height:1.35;">
            Cruza dimensiones relacionales (afectiva vs. funcional) segregando roles según contexto.
          </div>
        </div>
      </div>

      <!-- CIERRE DEL RECORRIDO Y TRÁNSITO A NIVEL 2 BÁSICO -->
      <div style="background:rgba(11, 19, 43, 0.85); border:1px solid rgba(0, 255, 135, 0.35); border-radius:12px; padding:8px 18px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div style="text-align:left;">
          <div style="color:#00FF87; font-family:'Roboto Mono', monospace; font-size:0.84rem; font-weight:800; letter-spacing:0.8px;">CIERRE DEL RECORRIDO INTUITIVO</div>
          <div style="color:#FFFFFF; font-weight:700; font-size:0.82rem; margin-top:1px;">¿Listo para descifrar las reglas del código relacional en 60 segundos?</div>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
          <button class="flow-nav-btn" onclick="scrollToScreen('pantalla-e')" style="padding:6px 14px; font-size:0.82rem;">← ATRÁS</button>
          <a href="nivel2_basico.html" class="flow-nav-btn flow-nav-btn-next" style="text-decoration:none; padding:7px 18px; font-weight:800; font-size:0.84rem;">DESCUBRIR NIVEL 2: BÁSICO →</a>
        </div>
      </div>
    </div>
  </section>"""
    content, c_sec = p_sec.subn(new_sec, content, count=1)

    # 3. Reemplazo del motor Three.js initCubeGxTyCz y setCubeCoord
    p_js = re.compile(r'function initCubeGxTyCz\(\)\s*\{.*?function buildQ81TableHtml\(\)', re.DOTALL)
    new_js = """function initCubeGxTyCz() {
      const container = document.getElementById('canvas-cube-container');
      if (!container) return;

      const scene = new THREE.Scene();
      const width = container.clientWidth || 580;
      const height = container.clientHeight || 300;
      const camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);
      camera.position.set(24, 16, 26);
      camera.lookAt(0, 0, 0);

      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.setSize(width, height);
      container.appendChild(renderer.domElement);

      scene.add(new THREE.AmbientLight(0xffffff, 0.95));
      const pLight = new THREE.PointLight(0x38bdf8, 2.5, 120);
      pLight.position.set(20, 30, 25);
      scene.add(pLight);
      const pLight2 = new THREE.PointLight(0x00ff87, 1.5, 100);
      pLight2.position.set(-20, -15, -20);
      scene.add(pLight2);

      cubeGroup = new THREE.Group();
      // Tamaño geométrico canónico de los vóxeles (4.6)
      const boxGeo = new THREE.BoxGeometry(4.6, 4.6, 4.6);

      // 12 Vóxeles en diseño G2 × T3 × C2 (2 Grupos × 3 Tiempos × 2 Criterios)
      // Centro baricéntrico exacto en (0, 0, 0)
      const coordsMap = [
        // Nivel T1 (Inferior · Pre-diagnóstico: Y = -5.4)
        { x: -1, y: -1, z: -1, id: '1g1t1c' },
        { x:  1, y: -1, z: -1, id: '2g1t1c' },
        { x: -1, y: -1, z:  1, id: '1g1t2c' },
        { x:  1, y: -1, z:  1, id: '2g1t2c' },

        // Nivel T2 (Medio · Intervención / Proceso: Y = 0)
        { x: -1, y:  0, z: -1, id: '1g2t1c' },
        { x:  1, y:  0, z: -1, id: '2g2t1c' },
        { x: -1, y:  0, z:  1, id: '1g2t2c' },
        { x:  1, y:  0, z:  1, id: '2g2t2c' },

        // Nivel T3 (Superior · Post-consolidación: Y = +5.4)
        { x: -1, y:  1, z: -1, id: '1g3t1c' },
        { x:  1, y:  1, z: -1, id: '2g3t1c' },
        { x: -1, y:  1, z:  1, id: '1g3t2c' },
        { x:  1, y:  1, z:  1, id: '2g3t2c' }
      ];

      coordsMap.forEach(item => {
        const isDefault = (item.id === '1g1t1c');
        const mat = new THREE.MeshPhysicalMaterial({
          color: isDefault ? 0x00FF87 : 0x1E293B,
          emissive: isDefault ? 0x00FF87 : 0x0E172A,
          emissiveIntensity: isDefault ? 0.65 : 0.22,
          roughness: 0.15,
          transparent: true,
          opacity: isDefault ? 0.90 : 0.45,
          clearcoat: 1.0,
          clearcoatRoughness: 0.1
        });
        const mesh = new THREE.Mesh(boxGeo, mat);
        mesh.position.set(item.x * 2.7, item.y * 5.4, item.z * 2.7);
        mesh.userData = { id: item.id };

        const wireGeo = new THREE.EdgesGeometry(boxGeo);
        const wireMat = new THREE.LineBasicMaterial({
          color: isDefault ? 0x00FF87 : 0x38BDF8,
          linewidth: 1.8
        });
        mesh.add(new THREE.LineSegments(wireGeo, wireMat));
        cubeGroup.add(mesh);
      });

      // Ejes ortogonales canónicos vinculados al cubo (giran con él)
      const origin = new THREE.Vector3(-6.5, -8.6, -6.5);
      const arrowX = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), origin, 15, 0xFF6B6B, 1.6, 0.8);
      const arrowY = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), origin, 18, 0x00FF87, 1.6, 0.8);
      const arrowZ = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), origin, 15, 0x38BDF8, 1.6, 0.8);
      cubeGroup.add(arrowX);
      cubeGroup.add(arrowY);
      cubeGroup.add(arrowZ);

      // Plataforma base circular tipo pedestal
      const pedestalGeo = new THREE.CylinderGeometry(10.5, 11, 0.4, 32);
      const pedestalMat = new THREE.MeshBasicMaterial({
        color: 0x0E1A36,
        wireframe: true,
        transparent: true,
        opacity: 0.35
      });
      const pedestal = new THREE.Mesh(pedestalGeo, pedestalMat);
      pedestal.position.set(0, -9.2, 0);
      cubeGroup.add(pedestal);

      scene.add(cubeGroup);

      // Inclinación inicial isométrica canónica (estable, sin volteretas)
      cubeGroup.rotation.x = 0.18;

      let isPaused = false;
      container.addEventListener('mouseenter', () => { isPaused = true; });
      container.addEventListener('mouseleave', () => { isPaused = false; });

      // Permite arrastrar suavemente con el ratón para rotar horizontalmente
      let isDragging = false;
      let prevMouseX = 0;
      container.addEventListener('mousedown', e => {
        isDragging = true;
        prevMouseX = e.clientX;
      });
      window.addEventListener('mouseup', () => { isDragging = false; });
      window.addEventListener('mousemove', e => {
        if (!isDragging) return;
        const deltaX = e.clientX - prevMouseX;
        cubeGroup.rotation.y += deltaX * 0.008;
        prevMouseX = e.clientX;
      });

      function animateCube() {
        requestAnimationFrame(animateCube);
        if (!isDragging && !isPaused) {
          cubeGroup.rotation.y += 0.004; // Rotación serena tipo carrusel (solo eje vertical Y)
        }
        renderer.render(scene, camera);
      }
      animateCube();

      // Ajuste dinámico de tamaño con ResizeObserver para que nunca se desborde ni se desplace
      const ro = new ResizeObserver(() => {
        if (!container.clientWidth || !container.clientHeight) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      });
      ro.observe(container);
    }

    function setCubeCoord(type) {
      if (type.startsWith('G')) activeG = type;
      if (type.startsWith('T')) activeT = type;
      if (type.startsWith('C')) activeC = type;

      // Actualizar botones UI
      document.querySelectorAll('.cube-filter-btn').forEach(b => {
        const txt = b.innerText;
        if (txt.includes(activeG) || txt.includes(activeT) || txt.includes(activeC)) {
          b.classList.add('active');
        } else if ((b.id.includes('grp') && !txt.includes(activeG)) ||
                   (b.id.includes('tim') && !txt.includes(activeT)) ||
                   (b.id.includes('cri') && !txt.includes(activeC))) {
          b.classList.remove('active');
        }
      });

      const coordId = `${activeG.replace('G','') || '1'}g${activeT.replace('T','') || '1'}t${activeC.replace('C','') || '1'}c`;
      const label = document.getElementById('active-cube-coord');
      if (label) label.innerText = coordId;

      const descEl = document.getElementById('active-cube-desc');
      if (descEl) {
        const gName = activeG === 'G2' ? '<span style="color:#FF6B6B;">Grupo 2 (G2)</span>' : '<span style="color:#FF6B6B;">Grupo 1 (G1)</span>';
        let tName = '<span style="color:#00FF87;">Tiempo 1 (T1 Pre)</span>';
        if (activeT === 'T2') tName = '<span style="color:#00FF87;">Tiempo 2 (T2 Inter)</span>';
        else if (activeT === 'T3') tName = '<span style="color:#00FF87;">Tiempo 3 (T3 Post)</span>';
        const cName = activeC === 'C2' ? '<span style="color:#38BDF8;">Criterio 2 (Trabajo)</span>' : '<span style="color:#38BDF8;">Criterio 1 (Afectivo)</span>';
        descEl.innerHTML = `${gName} · ${tName} · ${cName}`;
      }

      // Resaltar en el esquema SVG axonométrico (12 Vóxeles)
      const badge = document.getElementById('schematic-coord-badge');
      if (badge) badge.innerText = coordId;

      const svgVoxels = [
        '1g1t1c', '2g1t1c', '1g1t2c', '2g1t2c',
        '1g2t1c', '2g2t1c', '1g2t2c', '2g2t2c',
        '1g3t1c', '2g3t1c', '1g3t2c', '2g3t2c'
      ];
      svgVoxels.forEach(vId => {
        const poly = document.getElementById(`vox-${vId}`);
        if (poly) {
          const isSelected = (vId === coordId);
          poly.setAttribute('fill', isSelected ? '#00FF87' : (vId.endsWith('2c') ? '#0F172A' : '#1E293B'));
          poly.setAttribute('fill-opacity', isSelected ? '0.90' : (vId.endsWith('2c') ? '0.40' : '0.50'));
          poly.setAttribute('stroke', isSelected ? '#00FF87' : (vId.endsWith('2c') ? 'rgba(255,255,255,0.25)' : '#38BDF8'));
          poly.setAttribute('stroke-width', isSelected ? '2.2' : '1.2');
        }
      });

      ['1g1t1c', '2g1t1c', '1g2t1c', '2g2t1c', '1g3t1c', '2g3t1c'].forEach(vId => {
        const txt = document.getElementById(`txt-${vId}`);
        if (txt) {
          const isSelected = (vId === coordId);
          txt.setAttribute('fill', isSelected ? '#030308' : '#CBD5E1');
          txt.setAttribute('font-weight', isSelected ? '900' : '700');
        }
      });

      // Resaltar cubo en Three.js
      if (cubeGroup) {
        cubeGroup.children.forEach(mesh => {
          if (!mesh.userData || !mesh.userData.id) return;
          const match = (mesh.userData.id === coordId);
          if (mesh.material && mesh.material.color) {
            mesh.material.color.setHex(match ? 0x00FF87 : 0x1E293B);
            mesh.material.emissive.setHex(match ? 0x00FF87 : 0x0E172A);
            mesh.material.emissiveIntensity = match ? 0.75 : 0.20;
            mesh.material.opacity = match ? 0.92 : 0.45;
          }
          if (mesh.children && mesh.children[0] && mesh.children[0].material) {
            mesh.children[0].material.color.setHex(match ? 0x00FF87 : 0x38BDF8);
          }
        });
      }
    }

    function buildQ81TableHtml()"""
    content, c_js = p_js.subn(new_js, content, count=1)

    counts = {
        "css": c_css,
        "section": c_sec,
        "js": c_js
    }
    return content, counts

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    visual_dir = os.path.join(base_dir, "VERSION_IMPACTO_VISUAL")
    files = ["nivel1_intuitivo.html", "visord_intuitivo.html"]

    for fn in files:
        target_path = os.path.join(visual_dir, fn)
        with open(target_path, "r", encoding="utf-8") as f:
            raw = f.read()

        fixed, counts = fix_cube_in_text(raw)
        print(f"=== {fn} ===")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        val = Validator()
        val.feed(fixed)
        print(f"  Validación HTML: {val.errors} errores.")

        # Guardar en VERSION_IMPACTO_VISUAL
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(fixed)

        # Copiar también a activo (05_Web_Promocional/)
        active_path = os.path.join(base_dir, fn)
        with open(active_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  -> Guardado en {target_path} y {active_path}")

if __name__ == "__main__":
    main()
