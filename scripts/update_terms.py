#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_terms.py
Replaces 'Procesual' with 'Dialéctico' across all web promotional assets.
"""
import os
import shutil

def update_file(path, replacements):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return False
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old, new in replacements:
        if old not in content:
            print(f"Note: '{old}' not present in {os.path.basename(path)}")
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
    # 1. Update recursos.html (Root)
    # -------------------------------------------------------------
    rec_path = os.path.join(base_dir, 'recursos.html')
    rec_reps = [
        ('VISORD_procesual.', 'VISORD_dialectico.'),
        ('VISORD procesual,', 'VISORD dialectico,'),
        ('"name": "VISORD Procesual",', '"name": "VISORD Dialéctico",'),
        ('"url": "https://josemancor.github.io/nex-ord-web/visord_procesual.html"', '"url": "https://josemancor.github.io/nex-ord-web/visord_dialectico.html"'),
        ('/* 4. VISORD_PROCESUAL */', '/* 4. VISORD_DIALÉCTICO */'),
        ('.card-procesual { border-color: rgba(0, 255, 135, 0.4); }', '.card-dialectico, .card-procesual { border-color: rgba(0, 255, 135, 0.4); }'),
        ('.card-procesual:hover { border-color: #00FF87; box-shadow: 0 16px 40px rgba(0, 255, 135, 0.25); }', '.card-dialectico:hover, .card-procesual:hover { border-color: #00FF87; box-shadow: 0 16px 40px rgba(0, 255, 135, 0.25); }'),
        ('.card-procesual .card-badge { color: #00FF87; background: rgba(0, 255, 135, 0.2); border: 1.5px solid rgba(0, 255, 135, 0.6); }', '.card-dialectico .card-badge, .card-procesual .card-badge { color: #00FF87; background: rgba(0, 255, 135, 0.2); border: 1.5px solid rgba(0, 255, 135, 0.6); }'),
        ('.card-procesual .card-title { color: #00FF87; }', '.card-dialectico .card-title, .card-procesual .card-title { color: #00FF87; }'),
        ('.card-procesual .card-action-btn {', '.card-dialectico .card-action-btn, .card-procesual .card-action-btn {'),
        ('.card-procesual:hover .card-action-btn,', '.card-dialectico:hover .card-action-btn, .card-procesual:hover .card-action-btn,'),
        ('.card-procesual .card-action-btn:hover {', '.card-dialectico .card-action-btn:hover, .card-procesual .card-action-btn:hover {'),
        ('class="card-experience card-procesual"', 'class="card-experience card-dialectico card-procesual"'),
        ('"nav_proc": "◀ VISORD_PROCESUAL",', '"nav_proc": "◀ VISORD_DIALÉCTICO",'),
        ('"nav_proc_title": "◀ VISORD Anterior: VISORD_PROCESUAL",', '"nav_proc_title": "◀ VISORD Anterior: VISORD_DIALÉCTICO",'),
        ('"arrow_left_label": "VISORD_PROCESUAL",', '"arrow_left_label": "VISORD_DIALÉCTICO",'),
        ('"arrow_left_title": "◀ VISORD Anterior: VISORD_PROCESUAL (Laboratorio)",', '"arrow_left_title": "◀ VISORD Anterior: VISORD_DIALÉCTICO (Laboratorio)",'),
        ('"pod_proc_title": "◀ VISORD Anterior: VISORD_PROCESUAL",', '"pod_proc_title": "◀ VISORD Anterior: VISORD_DIALÉCTICO",'),
        ('"card4_title": "VISORD_PROCESUAL",', '"card4_title": "VISORD_DIALÉCTICO",'),
        ('"card4_desc": "Laboratorio experimental de micro-procesos: Cuadrilátero interactivo, Moviola Bales IPA ⇄ SMIb ⇄ Dilema Moral de Bienes Comunes (N=5).",', '"card4_desc": "Laboratorio experimental de micro-interacciones: Anfiteatro interactivo, Moviola Bales IPA ⇄ SMIb ⇄ Dilema Moral de Bienes Comunes (N=5).",'),
        ('y VISORD Procesual, nuestro laboratorio experimental de microprocesos y dilemas morales.', 'y VISORD Dialéctico, nuestro laboratorio experimental de microprocesos y dilemas dialécticos.'),
        ('"nav_proc": "◀ VISORD_PROCESSUAL",', '"nav_proc": "◀ VISORD_DIALECTICAL",'),
        ('"nav_proc_title": "◀ Previous VISORD: VISORD_PROCESSUAL",', '"nav_proc_title": "◀ Previous VISORD: VISORD_DIALECTICAL",'),
        ('"arrow_left_label": "VISORD_PROCESSUAL",', '"arrow_left_label": "VISORD_DIALECTICAL",'),
        ('"arrow_left_title": "◀ Previous VISORD: VISORD_PROCESSUAL (Laboratory)",', '"arrow_left_title": "◀ Previous VISORD: VISORD_DIALECTICAL (Laboratory)",'),
        ('"pod_proc_title": "◀ Previous VISORD: VISORD_PROCESSUAL",', '"pod_proc_title": "◀ Previous VISORD: VISORD_DIALECTICAL",'),
        ('"card4_title": "VISORD_PROCESSUAL",', '"card4_title": "VISORD_DIALECTICAL",'),
        ('card4_desc": "Experimental micro-process laboratory: Interactive Quadrilateral, Moviola Bales IPA ⇄ SMIb ⇄ Commons Moral Dilemma (N=5).",', 'card4_desc": "Experimental micro-process laboratory: Interactive Arena, Moviola Bales IPA ⇄ SMIb ⇄ Commons Moral Dilemma (N=5).",'),
        ('and VISORD Processual, our experimental laboratory for micro-processes and moral dilemmas.', 'and VISORD Dialectical, our experimental laboratory for micro-processes and moral dilemmas.'),
        ('"nav_proc": "◀ VISORD_ПРОЦЕССУАЛЬНЫЙ",', '"nav_proc": "◀ VISORD_ДИАЛЕКТИЧЕСКИЙ",'),
        ('"nav_proc_title": "◀ Предыдущий VISORD: VISORD_ПРОЦЕССУАЛЬНЫЙ",', '"nav_proc_title": "◀ Предыдущий VISORD: VISORD_ДИАЛЕКТИЧЕСКИЙ",'),
        ('"arrow_left_label": "VISORD_ПРОЦЕССУАЛЬНЫЙ",', '"arrow_left_label": "VISORD_ДИАЛЕКТИЧЕСКИЙ",'),
        ('"arrow_left_title": "◀ Предыдущий VISORD: VISORD_ПРОЦЕССУАЛЬНЫЙ (Лаборатория)",', '"arrow_left_title": "◀ Предыдущий VISORD: VISORD_ДИАЛЕКТИЧЕСКИЙ (Лаборатория)",'),
        ('"pod_proc_title": "◀ Предыдущий VISORD: VISORD_ПРОЦЕССУАЛЬНЫЙ",', '"pod_proc_title": "◀ Предыдущий VISORD: VISORD_ДИАЛЕКТИЧЕСКИЙ",'),
        ('"card4_title": "VISORD_ПРОЦЕССУАЛЬНЫЙ",', '"card4_title": "VISORD_ДИАЛЕКТИЧЕСКИЙ",'),
        ('card4_desc": "Экспериментальная лаборатория микропроцессов: интерактивный четырехугольник, мовиола Bales IPA ⇄ SMIb ⇄ моральная дилемма общественных благ (N=5).",', 'card4_desc": "Экспериментальная лаборатория микропроцессов: интерактивный амфитеатр, мовиола Bales IPA ⇄ SMIb ⇄ моральная дилемма общественных благ (N=5).",'),
        ('и VISORD Processual — нашей экспериментальной лаборатории микропроцессов и моральных дилемм.', 'и VISORD Dialectical — нашей экспериментальной лаборатории микропроцессов и моральных дилемм.'),
        ('"nav_proc": "◀ VISORD_过程仿真",', '"nav_proc": "◀ VISORD_辩证演化",'),
        ('"nav_proc_title": "◀ 上一 VISORD 环境：VISORD_过程仿真",', '"nav_proc_title": "◀ 上一 VISORD 环境：VISORD_辩证演化",'),
        ('"arrow_left_label": "VISORD_过程仿真",', '"arrow_left_label": "VISORD_辩证演化",'),
        ('"arrow_left_title": "◀ 上一 VISORD：VISORD_过程实验室",', '"arrow_left_title": "◀ 上一 VISORD：VISORD_辩证实验室",'),
        ('"pod_proc_title": "◀ 上一 VISORD 环境：VISORD_过程仿真",', '"pod_proc_title": "◀ 上一 VISORD 环境：VISORD_辩证演化",'),
        ('"card4_title": "VISORD_过程仿真",', '"card4_title": "VISORD_辩证演化",'),
        ('card4_desc": "微观动态过程实验实验室：交互式四边形张力图、Bales IPA ⇄ SMIb ⇄ 公地悲剧道德困境连续回放录像机（N=5）。",', 'card4_desc": "微观动态交互实验实验室：交互式剧场张力图、Bales IPA ⇄ SMIb ⇄ 公地悲剧道德困境连续回放录像机（N=5）。",')
    ]
    update_file(rec_path, rec_reps)

    # -------------------------------------------------------------
    # 2. Update VERSION_IMPACTO_VISUAL/recursos.html
    # -------------------------------------------------------------
    rec_v_path = os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL', 'recursos.html')
    rec_v_reps = list(rec_reps) + [
        ('<a href="visord_procesual.html" class="recursos-nav-btn btn-dial" id="nav-btn-proc" title="◀ VISORD Anterior: VISORD_PROCESUAL" aria-label="VISORD Anterior: VISORD Procesual" data-i18n="nav_proc">', '<a href="visord_dialectico.html" class="recursos-nav-btn btn-dial" id="nav-btn-proc" title="◀ VISORD Anterior: VISORD_DIALÉCTICO" aria-label="VISORD Anterior: VISORD Dialéctico" data-i18n="nav_proc">'),
        ('<a href="visord_procesual.html" class="floating-side-arrow arrow-left" id="floating-arrow-left" title="◀ VISORD Anterior: VISORD_PROCESUAL (Laboratorio)" aria-label="VISORD Anterior: VISORD Procesual">', '<a href="visord_dialectico.html" class="floating-side-arrow arrow-left" id="floating-arrow-left" title="◀ VISORD Anterior: VISORD_DIALÉCTICO (Laboratorio)" aria-label="VISORD Anterior: VISORD Dialéctico">'),
        ('<a href="visord_procesual.html" class="nav-pod-btn" id="nav-pod-proc" title="◀ VISORD Anterior: VISORD_PROCESUAL" aria-label="VISORD Anterior: VISORD Procesual">', '<a href="visord_dialectico.html" class="nav-pod-btn" id="nav-pod-proc" title="◀ VISORD Anterior: VISORD_DIALÉCTICO" aria-label="VISORD Anterior: VISORD Dialéctico">'),
        ('<a href="visord_procesual.html" class="card-experience card-procesual" title="Acceder al Laboratorio VISORD_procesual" aria-label="Acceder al Laboratorio VISORD_procesual">', '<a href="visord_dialectico.html" class="card-experience card-dialectico card-procesual" title="Acceder al Laboratorio VISORD_dialéctico" aria-label="Acceder al Laboratorio VISORD_dialéctico">')
    ]
    update_file(rec_v_path, rec_v_reps)

    # -------------------------------------------------------------
    # 3. Synchronize visord_procesual.html and VERSION_IMPACTO_VISUAL
    # -------------------------------------------------------------
    diag_path = os.path.join(base_dir, 'visord_dialectico.html')
    proc_path = os.path.join(base_dir, 'visord_procesual.html')
    diag_v_path = os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL', 'visord_dialectico.html')
    proc_v_path = os.path.join(base_dir, 'VERSION_IMPACTO_VISUAL', 'visord_procesual.html')

    # Copy updated visord_dialectico.html to visord_procesual.html (transparent mirror for zero 404s)
    shutil.copy2(diag_path, proc_path)
    print(f"Mirrored {diag_path} -> {proc_path}")

    # Copy to VERSION_IMPACTO_VISUAL
    shutil.copy2(diag_path, diag_v_path)
    print(f"Copied to {diag_v_path}")
    shutil.copy2(diag_path, proc_v_path)
    print(f"Copied to {proc_v_path}")

    # -------------------------------------------------------------
    # 4. Update prototipo_portada_interactiva_nexord.html
    # -------------------------------------------------------------
    proto_path = os.path.join(base_dir, 'prototipo_portada_interactiva_nexord.html')
    proto_reps = [
        ('(VISORD_demo, Cultural, Radiológico y Procesual)', '(VISORD_demo, Cultural, Radiológico y Dialéctico)'),
        ('{ label: "VISORD PROCESUAL", link: "visord_procesual.html" }', '{ label: "VISORD DIALÉCTICO", link: "visord_dialectico.html" }')
    ]
    update_file(proto_path, proto_reps)

    # -------------------------------------------------------------
    # 5. Update README.md
    # -------------------------------------------------------------
    readme_path = os.path.join(base_dir, 'README.md')
    readme_reps = [
        ('3. ⚡ **VISORD Procesual (Observador Universal de Textos)**: [visord_procesual.html](https://josemancor.github.io/nex-ord-web/visord_procesual.html)',
         '3. ⚡ **VISORD Dialéctico (Observador Universal de Textos)**: [visord_dialectico.html](https://josemancor.github.io/nex-ord-web/visord_dialectico.html)')
    ]
    update_file(readme_path, readme_reps)

    # -------------------------------------------------------------
    # 6. Update js/cultural_synthesis_engine.js
    # -------------------------------------------------------------
    syn_path = os.path.join(base_dir, 'js', 'cultural_synthesis_engine.js')
    syn_reps = [
        ('Inercia Procesual', 'Inercia Dialéctica')
    ]
    update_file(syn_path, syn_reps)

    # -------------------------------------------------------------
    # 7. Update MANIFIESTO_CIENTIFICO_NEXORD_ZENODO_2026.md and .html
    # -------------------------------------------------------------
    mani_md = os.path.join(base_dir, 'assets', 'MANIFIESTO_CIENTIFICO_NEXORD_ZENODO_2026.md')
    mani_html = os.path.join(base_dir, 'assets', 'MANIFIESTO_CIENTIFICO_NEXORD_ZENODO_2026.html')
    mani_reps = [
        ('Laboratorio Físico, Sociometría Procesual y Diagnóstico Multimodal / Experimental Research: Physical Lab, Processual Sociometry & Multimodal Diagnostics',
         'Laboratorio Físico, Sociometría Dialéctica y Diagnóstico Multimodal / Experimental Research: Physical Lab, Dialectical Sociometry & Multimodal Diagnostics'),
        ('### 6.2. Sociometría Procesual y Estudio de Dilemas Sociales / Processual Sociometry & Social Dilemmas',
         '### 6.2. Sociometría Dialéctica y Estudio de Dilemas Sociales / Dialectical Sociometry & Social Dilemmas'),
        ('Superando la limitación de la sociometría concebida como una mera fotografía estática, la Sociometría Procesual registra',
         'Superando la limitación de la sociometría concebida como una mera fotografía estática, la Sociometría Dialéctica registra')
    ]
    update_file(mani_md, mani_reps)

    mani_html_reps = [
        ('Laboratorio Físico, Sociometría Procesual y Diagnóstico Multimodal / Experimental Research: Physical Lab, Processual Sociometry &amp; Multimodal Diagnostics',
         'Laboratorio Físico, Sociometría Dialéctica y Diagnóstico Multimodal / Experimental Research: Physical Lab, Dialectical Sociometry &amp; Multimodal Diagnostics'),
        ('### 6.2. Sociometría Procesual y Estudio de Dilemas Sociales / Processual Sociometry &amp; Social Dilemmas',
         '### 6.2. Sociometría Dialéctica y Estudio de Dilemas Sociales / Dialectical Sociometry &amp; Social Dilemmas'),
        ('Superando la limitación de la sociometría concebida como una mera fotografía estática, la Sociometría Procesual registra',
         'Superando la limitación de la sociometría concebida como una mera fotografía estática, la Sociometría Dialéctica registra')
    ]
    update_file(mani_html, mani_html_reps)

    print("\nAll web assets updated systematically!")

if __name__ == '__main__':
    main()
