#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_visord_dialectico.py
Generador y Sincronizador Maestro del VISORD DIALÉCTICO:
Observador Universal de Textos, Diálogos y Dilemas Dialécticos.
Ecosistema VISORD / NEXORD.
"""
import os
import shutil

def main():
    base_dir = os.path.dirname(__file__)
    source_path = os.path.abspath(os.path.join(base_dir, '..', 'visord_dialectico.html'))
    if not os.path.exists(source_path):
        print(f"Error: {source_path} no encontrado.")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Targets to synchronize
    targets = [
        os.path.abspath(os.path.join(base_dir, '..', 'visord_procesual.html')),
        os.path.abspath(os.path.join(base_dir, '..', 'VERSION_IMPACTO_VISUAL', 'visord_dialectico.html')),
        os.path.abspath(os.path.join(base_dir, '..', 'VERSION_IMPACTO_VISUAL', 'visord_procesual.html'))
    ]

    for target in targets:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Sincronizado: {target}")

    print("Compilación y sincronización del VISORD DIALÉCTICO completada con éxito.")

if __name__ == '__main__':
    main()
