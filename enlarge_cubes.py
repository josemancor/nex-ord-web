#!/usr/bin/env python3
"""
Agranda sustancialmente los cubos en la pantalla 1e (pantalla-f):
1. Elimina las restricciones de altura fija (300px/290px) en .cube-schematic-svg y #canvas-cube-container,
   permitiéndoles ocupar todo el alto disponible de las tarjetas (flex: 1 1 auto, min-height: 400px).
2. Agranda el Cubo Axonométrico SVG aplicando un factor de escala del 32% sobre sus vóxeles
   (transform="translate(207.5, 147) scale(1.32) translate(-207.5, -147)") y permitiendo
   que el SVG crezca hasta llenar la tarjeta con max-height: 440px.
3. Agranda el Cubo 3D WebGL (Three.js):
   - Aumenta el tamaño de cada vóxel de 4.6 a 6.6 (un 43% mayor).
   - Ajusta las posiciones relativas (3.85 en X/Z, 7.7 en Y).
   - Calibra la cámara (pos 24, 16, 26) para que el cubo ocupe el ~85% del lienzo 3D.
   - Agranda los ejes ortogonales proporcionales (longitudes 21, 26, 21) y el pedestal base (radio 15).
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

def enlarge_cubes(content):
    # 1. Modificar CSS para que los contenedores llenen el alto disponible
    p_css = re.compile(
        r'\.cube-schematic-svg\s*\{[^}]*\}\s*#canvas-cube-container\s*\{[^}]*\}',
        re.DOTALL
    )
    new_css = """.cube-schematic-svg {
      width: 100%;
      height: 100%;
      flex: 1 1 auto;
      min-height: 380px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #canvas-cube-container {
      width: 100%;
      height: 100%;
      flex: 1 1 auto;
      min-height: 380px;
      border-radius: 12px;
      overflow: hidden;
      position: relative;
      background: radial-gradient(circle at center, rgba(16, 30, 65, 0.75) 0%, rgba(5, 8, 17, 0.95) 100%);
      border: 1px solid rgba(56, 189, 248, 0.25);
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.7);
      cursor: grab;
    }"""
    content, c_css = p_css.subn(new_css, content, count=1)

    # 2. Modificar el tag del SVG y el grupo de vóxeles en pantalla-f
    p_svg_tag = re.compile(
        r'<svg width="100%" height="100%" viewBox="0 0 380 300" style="max-height: 290px; width: auto; margin: 0 auto; display: block;">'
    )
    new_svg_tag = '<svg width="100%" height="100%" viewBox="0 0 380 300" style="width: 100%; height: 100%; max-height: 440px; margin: 0 auto; display: block;">'
    content, c_svg_tag = p_svg_tag.subn(new_svg_tag, content, count=1)

    p_vox_group = re.compile(r'<g id="svg-voxels-group">')
    new_vox_group = '<g id="svg-voxels-group" transform="translate(207.5, 147) scale(1.32) translate(-207.5, -147)">'
    content, c_vox_group = p_vox_group.subn(new_vox_group, content, count=1)

    # 3. Modificar Three.js en initCubeGxTyCz
    p_box_geo = re.compile(r'const boxGeo = new THREE\.BoxGeometry\(4\.6, 4\.6, 4\.6\);')
    new_box_geo = 'const boxGeo = new THREE.BoxGeometry(6.6, 6.6, 6.6);'
    content, c_box_geo = p_box_geo.subn(new_box_geo, content, count=1)

    p_mesh_pos = re.compile(r'mesh\.position\.set\(item\.x \* 2\.7, item\.y \* 5\.4, item\.z \* 2\.7\);')
    new_mesh_pos = 'mesh.position.set(item.x * 3.85, item.y * 7.7, item.z * 3.85);'
    content, c_mesh_pos = p_mesh_pos.subn(new_mesh_pos, content, count=1)

    p_origin = re.compile(r'const origin = new THREE\.Vector3\(-6\.5, -8\.6, -6\.5\);')
    new_origin = 'const origin = new THREE.Vector3(-9.2, -12.2, -9.2);'
    content, c_origin = p_origin.subn(new_origin, content, count=1)

    p_arrows = re.compile(
        r'const arrowX = new THREE\.ArrowHelper\(new THREE\.Vector3\(1, 0, 0\), origin, 15, 0xFF6B6B, 1\.6, 0\.8\);\s*'
        r'const arrowY = new THREE\.ArrowHelper\(new THREE\.Vector3\(0, 1, 0\), origin, 18, 0x00FF87, 1\.6, 0\.8\);\s*'
        r'const arrowZ = new THREE\.ArrowHelper\(new THREE\.Vector3\(0, 0, 1\), origin, 15, 0x38BDF8, 1\.6, 0\.8\);'
    )
    new_arrows = """const arrowX = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), origin, 21, 0xFF6B6B, 2.2, 1.1);
      const arrowY = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), origin, 26, 0x00FF87, 2.2, 1.1);
      const arrowZ = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), origin, 21, 0x38BDF8, 2.2, 1.1);"""
    content, c_arrows = p_arrows.subn(new_arrows, content, count=1)

    p_pedestal = re.compile(
        r'const pedestalGeo = new THREE\.CylinderGeometry\(10\.5, 11, 0\.4, 32\);\s*'
        r'const pedestalMat = new THREE\.MeshBasicMaterial\(\{\s*color: 0x0E1A36,\s*wireframe: true,\s*transparent: true,\s*opacity: 0\.35\s*\}\);\s*'
        r'const pedestal = new THREE\.Mesh\(pedestalGeo, pedestalMat\);\s*'
        r'pedestal\.position\.set\(0, -9\.2, 0\);'
    )
    new_pedestal = """const pedestalGeo = new THREE.CylinderGeometry(15, 15.8, 0.6, 36);
      const pedestalMat = new THREE.MeshBasicMaterial({
        color: 0x0E1A36,
        wireframe: true,
        transparent: true,
        opacity: 0.35
      });
      const pedestal = new THREE.Mesh(pedestalGeo, pedestalMat);
      pedestal.position.set(0, -13.0, 0);"""
    content, c_pedestal = p_pedestal.subn(new_pedestal, content, count=1)

    # Cámara ajustada para vista amplia e imponente
    p_cam = re.compile(r'camera\.position\.set\(24, 16, 26\);')
    new_cam = 'camera.position.set(23, 16, 25);'
    content, c_cam = p_cam.subn(new_cam, content, count=1)

    counts = {
        "css": c_css,
        "svg_tag": c_svg_tag,
        "vox_group": c_vox_group,
        "box_geo": c_box_geo,
        "mesh_pos": c_mesh_pos,
        "origin": c_origin,
        "arrows": c_arrows,
        "pedestal": c_pedestal,
        "cam": c_cam
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

        fixed, counts = enlarge_cubes(raw)
        print(f"=== {fn} ===")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        val = Validator()
        val.feed(fixed)
        print(f"  Validación HTML: {val.errors} errores.")

        # Guardar en VERSION_IMPACTO_VISUAL
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(fixed)

        # Copiar también a 05_Web_Promocional/ (activo)
        active_path = os.path.join(base_dir, fn)
        with open(active_path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  -> Guardado en {target_path} y {active_path}")

if __name__ == "__main__":
    main()
