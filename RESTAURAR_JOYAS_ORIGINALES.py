#!/usr/bin/env python3
"""
SCRIPT DE RESTAURACIÓN INSTANTÁNEA · JOYAS CANÓNICAS EXTENSAS
Permite restaurar en 1 segundo la versión completa, enciclopédica y extensa
de los 7 niveles desde la Bóveda de Salvaguarda.
"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.join(BASE_DIR, "VAULT_JOYAS_7_NIVELES_EXTENSA")

def restore():
    if not os.path.exists(VAULT_DIR):
        print("ERROR: No se encontró el directorio de la Bóveda:", VAULT_DIR)
        return

    files = [f for f in os.listdir(VAULT_DIR) if f.endswith(".html")]
    print(f"Iniciando restauración de {len(files)} archivos desde la Bóveda...")
    
    restored = 0
    for f in sorted(files):
        src = os.path.join(VAULT_DIR, f)
        dst = os.path.join(BASE_DIR, f)
        shutil.copy2(src, dst)
        print(f"  [OK] Restaurado: {f}")
        restored += 1
        
    print(f"\n¡Éxito! Se han restaurado íntegramente los {restored} archivos de la versión extensa.")

if __name__ == "__main__":
    restore()
