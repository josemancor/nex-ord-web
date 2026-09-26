#!/bin/bash
# Script de Activación Inmediata de la Versión Impacto Visual
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VISUAL="$DIR/VERSION_IMPACTO_VISUAL"

if [ ! -d "$VISUAL" ]; then
    echo "ERROR: No existe el directorio en $VISUAL"
    exit 1
fi

echo "Activando la Versión de Impacto Visual (90% Visual / 10% Texto)..."
cp -p "$VISUAL"/*.html "$DIR/"
echo "¡Completado! Los archivos HTML de la Versión Impacto Visual están activos."
