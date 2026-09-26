#!/bin/bash
# Script de Restauración Inmediata de los 7 Niveles desde la Bóveda
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT="$DIR/VAULT_JOYAS_7_NIVELES_EXTENSA"

if [ ! -d "$VAULT" ]; then
    echo "ERROR: No existe la Bóveda en $VAULT"
    exit 1
fi

echo "Restaurando las joyas canónicas extensas de los 7 niveles..."
cp -p "$VAULT"/*.html "$DIR/"
echo "¡Completado! Todos los archivos HTML de la versión extensa han sido restaurados con éxito."
