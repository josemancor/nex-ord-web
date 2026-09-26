#!/usr/bin/env python3
"""
Calibra con proporción áurea y armonía visual el Cubo 1e (pantalla-f):
1. Corrige el tamaño desmesurado del Cubo 3D WebGL:
   - Reduce el tamaño de los vóxeles a 4.8 (proporción equilibrada).
   - Calibra la cámara a (28, 19, 30) con distancia ~45 para que el cubo ocupe
     un armónico 58% del marco 3D, con amplio aire perimetral.
   - Suaviza la velocidad de giro horizontal a un majestuoso 0.0025.
   - Calibra flechas y pedestal a escala exacta.
2. Corrige el recorte de texto "↗ CRITER" en el esquema SVG izquierdo:
   - Amplía el viewBox a "0 0 430 300" para que "↗ CRITERIOS (Cz)" y "C1 Afectivo, C2 Tarea"
     se lean completos sin tocar el borde.
   - Aplica una escala armónica de 1.15 al grupo de vóxeles.
3. Fija una altura equilibrada de 340px para ambos contenedores (.cube-schematic-svg y #canvas-cube-container),
   evitando tanto el apiñamiento como la sobredimensión vertical.
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

def calibrate_cube(content):
    # 1. CSS de los contenedores
    p_css = re.compile(
        r'\.cube-schematic-svg\s*\{[^}]*\}\s*#canvas-cube-container\s*\{[^}]*\}',
        re.DOTALL
    )
    new_css = """.cube-schematic-svg {
      width: 100%;
      height: 340px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #canvas-cube-container {
      width: 100%;
      height: 340px;
      border-radius: 12px;
      overflow: hidden;
      position: relative;
      background: radial-gradient(circle at center, rgba(16, 30, 65, 0.65) 0%, rgba(5, 8, 17, 0.95) 100%);
      border: 1px solid rgba(56, 189, 248, 0.25);
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.7);
      cursor: grab;
    }"""
    content, c_css = p_css.subn(new_css, content, count=1)

    # 2. SVG izquierdo: viewBox 0 0 430 300 y texto completo de Criterios
    p_svg = re.compile(
        r'<div class="cube-schematic-svg">\s*<svg[^>]*>.*?<\/svg>\s*<\/div>',
        re.DOTALL
    )
    new_svg = """<div class="cube-schematic-svg">
          <svg width="100%" height="100%" viewBox="0 0 430 300" style="max-height: 330px; width: auto; margin: 0 auto; display: block;">
            <!-- EJE Y: TIEMPOS (Vertical Izquierdo con 3 Tiempos: T1, T2, T3) -->
            <line x1="55" y1="262" x2="55" y2="28" stroke="#00FF87" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="55,18 50,31 60,31" fill="#00FF87"/>
            <text x="55" y="12" fill="#00FF87" font-size="11" font-weight="800" text-anchor="middle" font-family="'Roboto Mono', monospace">▲ TIEMPOS (Ty)</text>
            <circle cx="55" cy="85" r="2.5" fill="#00FF87"/>
            <text x="47" y="88" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T3 Post</text>
            <circle cx="55" cy="145" r="2.5" fill="#00FF87"/>
            <text x="47" y="148" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T2 Inter</text>
            <circle cx="55" cy="205" r="2.5" fill="#00FF87"/>
            <text x="47" y="208" fill="#94A3B8" font-size="8.5" text-anchor="end" font-family="'Roboto Mono', monospace">T1 Pre</text>

            <!-- EJE X: GRUPOS (Horizontal / Base) -->
            <line x1="85" y1="275" x2="295" y2="275" stroke="#FF6B6B" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="305,275 293,270 293,280" fill="#FF6B6B"/>
            <text x="195" y="291" fill="#FF6B6B" font-size="11" font-weight="800" text-anchor="middle" font-family="'Roboto Mono', monospace">▶ GRUPOS (Gx: G1, G2)</text>

            <!-- EJE Z: CRITERIOS (Profundidad / Lateral Derecho) -->
            <line x1="290" y1="245" x2="365" y2="175" stroke="#38BDF8" stroke-width="2.5" stroke-dasharray="3,2"/>
            <polygon points="372,168 360,173 368,181" fill="#38BDF8"/>
            <text x="355" y="156" fill="#38BDF8" font-size="10.5" font-weight="800" font-family="'Roboto Mono', monospace">↗ CRITERIOS (Cz)</text>
            <text x="355" y="170" fill="#94A3B8" font-size="8.5" font-family="'Roboto Mono', monospace">C1 Afectivo, C2 Tarea</text>

            <!-- CUBO ISOMÉTRICO CENTRAL CON 12 VÓXELES (Escala armónica 1.15) -->
            <g id="svg-voxels-group" transform="translate(207.5, 147) scale(1.15) translate(-207.5, -147)">
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

            <rect x="105" y="28" width="180" height="22" rx="6" fill="rgba(8, 13, 26, 0.9)" stroke="#00FF87" stroke-width="1"/>
            <text x="195" y="43" fill="#00FF87" font-size="10" font-weight="700" text-anchor="middle" font-family="'Roboto Mono', monospace">Vóxel M(g,t,c) Activo</text>
          </svg>
        </div>"""
    content, c_svg = p_svg.subn(new_svg, content, count=1)

    # 3. Three.js: proporciones armónicas equilibradas
    p_js = re.compile(r'function initCubeGxTyCz\(\)\s*\{.*?function buildQ81TableHtml\(\)', re.DOTALL)
    new_js = """function initCubeGxTyCz() {
      const container = document.getElementById('canvas-cube-container');
      if (!container) return;

      const scene = new THREE.Scene();
      const width = container.clientWidth || 580;
      const height = container.clientHeight || 340;
      const camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);
      camera.position.set(28, 19, 30);
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
      // Geometría armónica de los vóxeles (4.8)
      const boxGeo = new THREE.BoxGeometry(4.8, 4.8, 4.8);

      // 12 Vóxeles en diseño G2 × T3 × C2 (2 Grupos × 3 Tiempos × 2 Criterios)
      // Centro baricéntrico exacto en (0, 0, 0)
      const coordsMap = [
        // Nivel T1 (Inferior · Pre-diagnóstico: Y = -5.6)
        { x: -1, y: -1, z: -1, id: '1g1t1c' },
        { x:  1, y: -1, z: -1, id: '2g1t1c' },
        { x: -1, y: -1, z:  1, id: '1g1t2c' },
        { x:  1, y: -1, z:  1, id: '2g1t2c' },

        // Nivel T2 (Medio · Intervención / Proceso: Y = 0)
        { x: -1, y:  0, z: -1, id: '1g2t1c' },
        { x:  1, y:  0, z: -1, id: '2g2t1c' },
        { x: -1, y:  0, z:  1, id: '1g2t2c' },
        { x:  1, y:  0, z:  1, id: '2g2t2c' },

        // Nivel T3 (Superior · Post-consolidación: Y = +5.6)
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
        mesh.position.set(item.x * 2.85, item.y * 5.6, item.z * 2.85);
        mesh.userData = { id: item.id };

        const wireGeo = new THREE.EdgesGeometry(boxGeo);
        const wireMat = new THREE.LineBasicMaterial({
          color: isDefault ? 0x00FF87 : 0x38BDF8,
          linewidth: 1.8
        });
        mesh.add(new THREE.LineSegments(wireGeo, wireMat));
        cubeGroup.add(mesh);
      });

      // Ejes ortogonales canónicos solidarios al cubo
      const origin = new THREE.Vector3(-7.0, -9.0, -7.0);
      const arrowX = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), origin, 16, 0xFF6B6B, 1.8, 0.9);
      const arrowY = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), origin, 20, 0x00FF87, 1.8, 0.9);
      const arrowZ = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), origin, 16, 0x38BDF8, 1.8, 0.9);
      cubeGroup.add(arrowX);
      cubeGroup.add(arrowY);
      cubeGroup.add(arrowZ);

      // Pedestal base circular
      const pedestalGeo = new THREE.CylinderGeometry(11.5, 12.2, 0.45, 32);
      const pedestalMat = new THREE.MeshBasicMaterial({
        color: 0x0E1A36,
        wireframe: true,
        transparent: true,
        opacity: 0.35
      });
      const pedestal = new THREE.Mesh(pedestalGeo, pedestalMat);
      pedestal.position.set(0, -9.6, 0);
      cubeGroup.add(pedestal);

      scene.add(cubeGroup);

      // Inclinación inicial isométrica canónica (estable, sin volteretas)
      cubeGroup.rotation.x = 0.16;

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
          cubeGroup.rotation.y += 0.0025; // Rotación serena, sutil y elegante (solo eje Y)
        }
        renderer.render(scene, camera);
      }
      animateCube();

      // Ajuste dinámico de tamaño con ResizeObserver
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
        "svg": c_svg,
        "js": c_js
    }
    return content, counts

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    visual_dir = os.path.join(base_dir, "VERSION_IMPACTO_VISUAL")
    files = ["nivel1_intuitivo.html"]

    for fn in files:
        target_path = os.path.join(visual_dir, fn)
        with open(target_path, "r", encoding="utf-8") as f:
            raw = f.read()

        fixed, counts = calibrate_cube(raw)
        print(f"=== {fn} ===")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        val = Validator()
        val.feed(fixed)
        print(f"  Validación HTML: {val.errors} errores.")

        # Guardar en VERSION_IMPACTO_VISUAL
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(fixed)

        # Copiar a activo (05_Web_Promocional/)
        active_path = os.path.join(base_dir, fn)
        with open(active_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  -> Guardado en {target_path} y {active_path}")

if __name__ == "__main__":
    main()
