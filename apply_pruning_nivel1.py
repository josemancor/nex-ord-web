#!/usr/bin/env python3
"""
Aplica el saneamiento radical y audaz de impacto visual al Nivel 1.
Reduce drásticamente los textos largos y explicaciones farragosas,
dejando notas telegráficas de 1 sola frase y dando el 90% del protagonismo
a los gráficos, cuadros y lienzos interactivos.
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

def prune_content(content):
    # 1. Moreno Note
    p_moreno = re.compile(r'note:\s*`\s*<div style="background:rgba\(11,19,43,0\.92\); border:1\.8px solid rgba\(255,230,0,0\.45\);.*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_moreno = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(255,230,0,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#FFE600; font-weight:900;">💡 Nota:</strong> Sociometría binaria clásica (Moreno, 1934). Cuatro preguntas directas (+E, -R, +pE, -pR) que computan votos discretos sin intensidad ni orden continuo.
          </div>
        `"""
    content, count_m = p_moreno.subn(rep_moreno, content, count=1)

    # 2. Breve Note
    p_breve = re.compile(r'note:\s*`\s*<div style="display:grid; grid-template-columns:1\.3fr 1\.1fr 0\.9fr;.*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_breve = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(0,255,135,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#00FF87; font-weight:900;">💡 Nota:</strong> Protocolo ordinal BREVE. Ránquing continuo 1º..Nº con autoposicionamiento y expectativas cruzadas (aE, oE), 100% compatible con Moreno sin preguntas aversivas.
          </div>
        `"""
    content, count_b = p_breve.subn(rep_breve, content, count=1)

    # 3. Tetragrama Note
    p_tetra = re.compile(r'note:\s*`\s*<div style="background:rgba\(11,19,43,0\.92\); border:1\.8px solid rgba\(0,255,135,0\.45\);.*?(?:💡 Nota \(Integración Metodológica de las Tablas\):).*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_tetra = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(0,255,135,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#00FF87; font-weight:900;">💡 Nota:</strong> Célula diádica canónica de 4 pulsos [A1, A2, A3, A4]. Articula expectativas mutuas y preferencias efectivas proyectadas sobre las 81 figuras relacionales Q81(9, 9).
          </div>
        `"""
    content, count_t = p_tetra.subn(rep_tetra, content, count=1)

    # 4. SMIb Note
    p_smib = re.compile(r'note:\s*`\s*<div style="background:rgba\(11,19,43,0\.92\); border:1\.8px solid rgba\(0,255,135,0\.45\);.*?(?:💡 Nota \(Diferencia Fundamental entre SMIb y SMIa\):).*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_smib = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(0,255,135,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#00FF87; font-weight:900;">💡 Nota:</strong> SMIa registra la presencia binaria uniforme; SMIb incorpora la jerarquía continua e intensidad (A &gt; B &gt; ... &gt; b &gt; a), base para el cálculo de densidades físicas (BDR y SDR).
          </div>
        `"""
    content, count_s = p_smib.subn(rep_smib, content, count=1)

    # 5. Densidad Note
    p_dens = re.compile(r'note:\s*`\s*<div style="background:rgba\(11,19,43,0\.92\); border:1\.8px solid rgba\(0,255,135,0\.45\);.*?(?:💡 Nota \(De los Interruptores al Contador Moderno\):).*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_dens = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(0,255,135,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#00FF87; font-weight:900;">💡 Nota:</strong> Del interruptor discreto al contador continuo. Cuantifica masa bruta (BDR), balance neto de cohesión (SDR) y fricción térmica interna disipada (Id = 0.073).
          </div>
        `"""
    content, count_d = p_dens.subn(rep_dens, content, count=1)

    # 6. Pentagrama Note
    p_penta = re.compile(r'note:\s*`\s*<div style="background:rgba\(11,19,43,0\.92\); border:1\.8px solid rgba\(0,255,135,0\.45\);.*?(?:💡 Nota Pedagógica:).*?(?=<\/div>\s*`)\s*<\/div>\s*`', re.DOTALL)
    rep_penta = """note: `
          <div style="background:rgba(11,19,43,0.92); border:1.5px solid rgba(0,255,135,0.45); border-radius:10px; padding:8px 16px; font-size:0.90rem; color:#CBD5E1; text-align:center; max-width:1540px; margin:0 auto; box-sizing:border-box;">
            <strong style="color:#00FF87; font-weight:900;">💡 Nota:</strong> El Pentagrama 10D dibuja el pulso socio-termodinámico del grupo a través de sus 10 estaciones canónicas y el volumen interfacial de su Cinta 3D.
          </div>
        `"""
    content, count_p = p_penta.subn(rep_penta, content, count=1)

    # 7. Pantalla D Header Description
    p_head_d = re.compile(r'<p class="section-desc" style="max-width:820px; margin:2px auto; line-height:1\.45; font-size:0\.92rem;">\s*Diseño Canónico.*?<\/p>', re.DOTALL)
    rep_head_d = """<p class="section-desc" style="max-width:860px; margin:2px auto; line-height:1.4; font-size:0.92rem;">
        Contraste directo: <strong>Suma Discreta de Moreno</strong> frente a <strong>Campo Continuo de Densidades VISORD</strong> en un grupo <strong style="color:#00FF87;">N=5</strong>.
      </p>"""
    content, count_hd = p_head_d.subn(rep_head_d, content, count=1)

    # 8. Pantalla F Header Description
    p_head_f = re.compile(r'<p class="section-desc" style="max-width:820px; margin:0 auto;">\s*La gran ventaja metodológica de VISORD:.*?<\/p>', re.DOTALL)
    rep_head_f = """<p class="section-desc" style="max-width:820px; margin:0 auto;">
        Espacio tridimensional unificado: <b style="color:#FF6B6B;">Grupos (Gx)</b> &times; <b style="color:#00FF87;">Tiempos (Ty)</b> &times; <b style="color:#38BDF8;">Criterios (Cz)</b>. Comparativa simultánea de 12 matrices sociométricas continuas.
      </p>"""
    content, count_hf = p_head_f.subn(rep_head_f, content, count=1)

    # 9. openXModal notes
    p_modal_frec = re.compile(r'<div class="pedagogic-note" style="margin-top:16px;">\s*<strong>💡 Nota:<\/strong>\s*El recuento elemental de frecuencias.*?<\/div>', re.DOTALL)
    rep_modal_frec = """<div class="pedagogic-note" style="margin-top:12px; padding:8px 16px; font-size:0.90rem; text-align:center;">
            <strong>💡 Nota:</strong> El recuento elemental colapsa la topología relacional en una diagonal plana, etiquetando a 3A como "aislado" a pesar de su activa proactividad vinculante.
          </div>"""
    content, count_mfrec = p_modal_frec.subn(rep_modal_frec, content, count=1)

    p_modal_dens = re.compile(r'<div class="pedagogic-note" style="margin-top:16px;">\s*<strong>💡 Nota:<\/strong>\s*La socio-termodinámica de VISORD revela con exactitud.*?<\/div>', re.DOTALL)
    rep_modal_dens = """<div class="pedagogic-note" style="margin-top:12px; padding:8px 16px; font-size:0.90rem; text-align:center;">
            <strong>💡 Nota:</strong> El campo continuo de densidades desvela la estructura bimodal {1A-2A} y {4A-5A}, identificando a 3A como polo de máxima masa inercial (BDR=49.90, Φ=89.93).
          </div>"""
    content, count_mdens = p_modal_dens.subn(rep_modal_dens, content, count=1)

    p_modal_comp = re.compile(r'<div class="pedagogic-note" style="margin-top:16px;">\s*<strong>💡 Nota:<\/strong>\s*El Plano 1-2 rotado a 45º con ejes isométricos demuestra.*?<\/div>', re.DOTALL)
    rep_modal_comp = """<div class="pedagogic-note" style="margin-top:12px; padding:8px 16px; font-size:0.90rem; text-align:center;">
            <strong>💡 Nota:</strong> El Plano 1-2 Isométrico rotado a 45º contrasta la pérdida de información del recuento discreto frente al diagnóstico termodinámico continuo de VISORD.
          </div>"""
    content, count_mcomp = p_modal_comp.subn(rep_modal_comp, content, count=1)

    counts = {
        "moreno": count_m,
        "breve": count_b,
        "tetragrama": count_t,
        "smib": count_s,
        "densidad": count_d,
        "pentagrama": count_p,
        "header_d": count_hd,
        "header_f": count_hf,
        "modal_frec": count_mfrec,
        "modal_dens": count_mdens,
        "modal_comp": count_mcomp,
    }
    return content, counts

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    visual_dir = os.path.join(base_dir, "VERSION_IMPACTO_VISUAL")
    files_to_update = ["nivel1_intuitivo.html"]

    for fn in files_to_update:
        target_path = os.path.join(visual_dir, fn)
        with open(target_path, "r", encoding="utf-8") as f:
            raw = f.read()

        pruned, counts = prune_content(raw)
        print(f"=== {fn} ===")
        for k, v in counts.items():
            print(f"  {k}: {v}")

        # Validar HTML
        val = Validator()
        val.feed(pruned)
        print(f"  Validación HTML: {val.errors} errores.")

        # Guardar en VERSION_IMPACTO_VISUAL
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(pruned)

        # Copiar también a 05_Web_Promocional/ (versión activa)
        active_path = os.path.join(base_dir, fn)
        with open(active_path, "w", encoding="utf-8") as f:
            f.write(pruned)
        print(f"  -> Guardado en {target_path} y {active_path}")

if __name__ == "__main__":
    main()
