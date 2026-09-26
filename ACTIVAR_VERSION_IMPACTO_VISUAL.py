#!/usr/bin/env python3
"""
SCRIPT DE ACTIVACIÓN INSTANTÁNEA · VERSIÓN IMPACTO VISUAL
Activa en 1 segundo la versión simplificada y de máximo impacto visual
(90% gráfico / 10% texto) de la plataforma.
"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VISUAL_DIR = os.path.join(BASE_DIR, "VERSION_IMPACTO_VISUAL")

def activate():
    if not os.path.exists(VISUAL_DIR):
        print("ERROR: No se encontró el directorio:", VISUAL_DIR)
        return

    files = [f for f in os.listdir(VISUAL_DIR) if f.endswith(".html")]
    print(f"Activando versión de impacto visual ({len(files)} archivos)...")
    
    activated = 0
    for f in sorted(files):
        src = os.path.join(VISUAL_DIR, f)
        dst = os.path.join(BASE_DIR, f)
        shutil.copy2(src, dst)
        print(f"  [OK] Activado: {f}")
        activated += 1
        
    print(f"\n¡Éxito! Se han activado los {activated} archivos de la Versión Impacto Visual.")

if __name__ == "__main__":
    activate()
