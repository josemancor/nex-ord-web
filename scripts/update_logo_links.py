#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_logo_links.py
Configura el clic en el LOGO institucional para llevar directamente al Dial NEXORD
en todas las páginas de la plataforma web (05_Web_Promocional y VERSION_IMPACTO_VISUAL).
"""
import os
import re

def update_file(path, replacements):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return False
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in replacements:
        if old not in content:
            print(f"Note: pattern not found in {os.path.basename(path)}: {old[:50]}...")
        content = content.replace(old, new)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {path}")
        return True
    else:
        print(f"No changes made to {path}")
        return False

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # -------------------------------------------------------------
    # 1. index.html (Homepage)
    # -------------------------------------------------------------
    # On index.html, clicking brand-box should run openDial() and display official logo icon
    idx_path = os.path.join(base_dir, 'index.html')
    idx_reps = [
        # In CSS: vertically align logo with text in brand-box
        ('.brand-box {\n  display: flex;\n  align-items: baseline;\n  gap: 12px;\n}',
         '.brand-box {\n  display: flex;\n  align-items: center;\n  gap: 12px;\n  cursor: pointer;\n}'),
        # In HTML header: brand-box runs openDial() and includes official logo image
        ('<div class="brand-box" onclick="closeDial()" style="cursor: pointer;" title="Inicio (Imagen de Portada)">\n      <span class="brand-title">NEXORD</span>\n      <span class="brand-subtitle" id="hdr-subtitle">Hacia una Física de lo Grupal</span>\n    </div>',
         '<div class="brand-box" onclick="openDial()" style="cursor: pointer;" title="Abrir el Dial de Navegación NEXORD">\n      <img src="LOGO_NEXORD_OFICIAL.png" alt="Logo NEXORD" onerror="this.src=\'assets/logo_nexord_base.png\'" style="height: 38px; border-radius: 6px; flex-shrink: 0;">\n      <div style="display: flex; align-items: baseline; gap: 12px;">\n        <span class="brand-title">NEXORD</span>\n        <span class="brand-subtitle" id="hdr-subtitle">Hacia una Física de lo Grupal</span>\n      </div>\n    </div>')
    ]
    update_file(idx_path, idx_reps)

    # -------------------------------------------------------------
    # 2. visord_dialectico.html & visord_procesual.html
    # -------------------------------------------------------------
    for root_dir in [base_dir, os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL')]:
        for fname in ['visord_dialectico.html', 'visord_procesual.html']:
            fpath = os.path.join(root_dir, fname)
            f_reps = [
                ('<a href="index.html" class="brand-section">',
                 '<a href="index.html?dial=open&sector=8" class="brand-section" title="Volver al Dial NEXORD (Sector 8: Recursos)">')
            ]
            update_file(fpath, f_reps)

    # -------------------------------------------------------------
    # 3. visord_cultural.html
    # -------------------------------------------------------------
    for root_dir in [base_dir, os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL')]:
        fpath = os.path.join(root_dir, 'visord_cultural.html')
        f_reps = [
            ('<a href="index.html" style="display:flex; align-items:center; text-decoration:none;">\n                        <img src="assets/logo_nexord_base.png" alt="VISORD" class="hub-logo">\n                    </a>',
             '<a href="index.html?dial=open&sector=8" style="display:flex; align-items:center; text-decoration:none;" title="Volver al Dial NEXORD (Sector 8: Recursos)">\n                        <img src="assets/logo_nexord_base.png" alt="VISORD" class="hub-logo">\n                    </a>'),
            ('<a href="index.html" style="display:flex; align-items:center; text-decoration:none;">\n                <img src="assets/logo_nexord_base.png" alt="VISORD" class="brand-logo">\n            </a>',
             '<a href="index.html?dial=open&sector=8" style="display:flex; align-items:center; text-decoration:none;" title="Volver al Dial NEXORD (Sector 8: Recursos)">\n                <img src="assets/logo_nexord_base.png" alt="VISORD" class="brand-logo">\n            </a>')
        ]
        update_file(fpath, f_reps)

    # -------------------------------------------------------------
    # 4. visord_g2t1c1.html & visord_g2t2c2.html
    # -------------------------------------------------------------
    for root_dir in [base_dir, os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL')]:
        fpath1 = os.path.join(root_dir, 'visord_g2t1c1.html')
        f_reps1 = [
            ('<a href="index.html" style="display:flex; align-items:center; text-decoration:none;">\n                <img src="assets/logo_nexord_base.png" alt="VISORD Logo" class="brand-logo" style="max-height: 38px; border-radius: 6px;">\n            </a>',
             '<a href="index.html?dial=open&sector=8" style="display:flex; align-items:center; text-decoration:none;" title="Volver al Dial NEXORD (Sector 8: Recursos)">\n                <img src="assets/logo_nexord_base.png" alt="VISORD Logo" class="brand-logo" style="max-height: 38px; border-radius: 6px;">\n            </a>')
        ]
        update_file(fpath1, f_reps1)

        fpath2 = os.path.join(root_dir, 'visord_g2t2c2.html')
        f_reps2 = [
            ('<a href="index.html" style="text-decoration:none; display:flex; align-items:center; gap:12px;">',
             '<a href="index.html?dial=open&sector=8" style="text-decoration:none; display:flex; align-items:center; gap:12px;" title="Volver al Dial NEXORD (Sector 8: Recursos)">')
        ]
        update_file(fpath2, f_reps2)

    # -------------------------------------------------------------
    # 5. glosario.html & fundamentos.html & retorno_participante.html & 404.html
    # -------------------------------------------------------------
    for root_dir in [base_dir, os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL')]:
        glo_path = os.path.join(root_dir, 'glosario.html')
        glo_reps = [
            ('<div class="brand-container">\n      <img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.src=\'assets/logo_nexord_base.png\'" class="brand-logo">\n      <div class="brand-titles">\n        <div class="brand-main" id="brand-title">NEXORD <span>GLOSARIO</span></div>\n      </div>\n    </div>',
             '<a href="index.html?dial=open&sector=8" class="brand-container" style="text-decoration:none; cursor:pointer;" title="Volver al Dial NEXORD">\n      <img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.src=\'assets/logo_nexord_base.png\'" class="brand-logo">\n      <div class="brand-titles">\n        <div class="brand-main" id="brand-title">NEXORD <span>GLOSARIO</span></div>\n      </div>\n    </a>')
        ]
        update_file(glo_path, glo_reps)

    fund_path = os.path.join(base_dir, 'fundamentos.html')
    fund_reps = [
        ('<a href="index.html" class="brand-link" title="Volver a Portada Principal (Dial de Menús)">',
         '<a href="index.html?dial=open&sector=0" class="brand-link" title="Volver al Dial NEXORD (Sector 9: Fundamentos Epistemológicos)">')
    ]
    update_file(fund_path, fund_reps)

    ret_path = os.path.join(base_dir, 'retorno_participante.html')
    ret_reps = [
        ('<a href="index.html" style="text-decoration: none;">\n                    <img src="assets/logo_nexord_base.png" alt="VISORD Logo" style="max-height: 38px; border-radius: 6px;">\n                </a>',
         '<a href="index.html?dial=open" style="text-decoration: none;" title="Volver al Dial NEXORD">\n                    <img src="assets/logo_nexord_base.png" alt="VISORD Logo" style="max-height: 38px; border-radius: 6px;">\n                </a>')
    ]
    update_file(ret_path, ret_reps)

    err_path = os.path.join(base_dir, '404.html')
    err_reps = [
        ('<div class="logo-container">\n        <img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.style.display=\'none\'">\n    </div>',
         '<div class="logo-container">\n        <a href="index.html?dial=open" title="Volver al Dial NEXORD">\n            <img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.style.display=\'none\'">\n        </a>\n    </div>')
    ]
    update_file(err_path, err_reps)

    # -------------------------------------------------------------
    # 6. Niveles 1 a 7 (Navegación HUD & Carátulas)
    # -------------------------------------------------------------
    levels_map = [
        ('nivel1_intuitivo.html', 1, 1),
        ('nivel2_basico.html', 2, 2),
        ('nivel3_esquema.html', 3, 3),
        ('nivel4_aplicaciones.html', 4, 4),
        ('nivel5_matematico.html', 5, 5),
        ('nivel6_informes.html', 6, 6),
        ('nivel7_documentacion.html', 7, 7)
    ]

    for root_dir in [base_dir, os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL')]:
        for fname, lvl_num, sector_idx in levels_map:
            lpath = os.path.join(root_dir, fname)
            if not os.path.exists(lpath):
                continue
            with open(lpath, 'r', encoding='utf-8') as f:
                c = f.read()

            orig_c = c

            # A) Top floating HUD brand pill: make it a link to index.html?dial=open&sector={sector_idx}
            old_pill = '<div class="hud-brand-pill">'
            new_pill = f'<a href="index.html?dial=open&sector={sector_idx}" class="hud-brand-pill" style="text-decoration:none; cursor:pointer;" title="Volver al Dial NEXORD (Nivel {lvl_num})">'
            # Only replace the opening div if followed by hud-brand-logo
            pattern_pill = r'<div class="hud-brand-pill">(\s*<span class="hud-brand-logo">NEXORD:</span>)'
            c = re.sub(pattern_pill, rf'<a href="index.html?dial=open&sector={sector_idx}" class="hud-brand-pill" style="text-decoration:none; cursor:pointer;" title="Volver al Dial NEXORD (Nivel {lvl_num})">\1', c)

            # Close the tag: replace </div> following level span with </a>
            pattern_close = rf'(<span class="hud-brand-level"[^>]*>{lvl_num}\.</span>\s*)</div>'
            c = re.sub(pattern_close, r'\1</a>', c)

            # B) Transit carátula logo: wrap img in link to index.html?dial=open&sector={sector_idx}
            pattern_transit = r'<div class="transit-logo-wrap">\s*<img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.src=\'LOGO_NEXORD_OFICIAL.png\'" class="transit-logo-img">\s*</div>'
            replacement_transit = f'<div class="transit-logo-wrap">\n          <a href="index.html?dial=open&sector={sector_idx}" title="Volver al Dial NEXORD (Nivel {lvl_num})">\n            <img src="assets/logo_nexord_base.png" alt="NEXORD Logo" onerror="this.src=\'LOGO_NEXORD_OFICIAL.png\'" class="transit-logo-img">\n          </a>\n        </div>'
            c = re.sub(pattern_transit, replacement_transit, c)

            if c != orig_c:
                with open(lpath, 'w', encoding='utf-8') as f:
                    f.write(c)
                print(f"Updated Level: {lpath}")

    print("\nLogo links successfully configured to open the Dial directly!")

if __name__ == '__main__':
    main()
