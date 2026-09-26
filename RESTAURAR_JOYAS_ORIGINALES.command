#!/bin/bash
# Doble clic en Mac Finder para restaurar inmediatamente todas las Joyas Originales Extensas
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
"$DIR/RESTAURAR_JOYAS_ORIGINALES.sh"
read -p "Presiona ENTER para cerrar..."
