#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la Imagen Oficial en Alta Resolución del Protocolo BREVE (Excel N=8)
Destaca con claridad pedagógica y tipográfica perfecta:
- Cada emisor (fila) lista en 1º, 2º y 3º lugar a los miembros preferidos.
- Autoposicionamiento (Tú).
- Metapercepciones de frontera (aE 1º, oE 8º).
- Estilo Excel auténtico, claro, nítido y de alto contraste (sin glifos rotos).
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_excel_breve_image(output_path):
    width = 1720
    height = 1040
    
    # Crear lienzo base con fondo oscuro elegante que contrasta con el marco de Excel
    img = Image.new('RGBA', (width, height), (11, 19, 43, 255)) # #0B132B
    draw = ImageDraw.Draw(img)

    # Tipografías del sistema (utilizamos fuentes que garantizan soporte completo de caracteres)
    font_title = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 25)
    font_sub = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
    font_callout_title = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 15)
    font_callout_body = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 13)
    
    font_excel_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 14)
    font_formula = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 14)
    font_header_grp = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 14)
    font_col_header = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 15)
    font_cell = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 16)
    font_cell_tu = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 14)
    font_row_num = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 12)
    font_badge = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 12)

    # 1. CABECERA INSTITUCIONAL SUPERIOR DEL GRÁFICO
    header_y = 18
    draw.text((width // 2, header_y), "PROTOCOLO OFICIAL BREVE · REGISTRO ORDINAL EN EXCEL (N=8)", 
              fill=(255, 255, 255, 255), font=font_title, anchor="mt")
    draw.text((width // 2, header_y + 34), 
              "Cada fila es un sujeto EMISOR que ordena a todos los miembros: las columnas 1º, 2º y 3º recogen las preferencias prioritarias", 
              fill=(56, 189, 248, 255), font=font_sub, anchor="mt")

    # 2. MARCO DE LA VENTANA EXCEL
    ex_x = 40
    ex_y = 86
    ex_w = 1640
    ex_h = 754

    # Sombra de elevación para la ventana
    for i in range(8):
        alpha = int(35 - i * 4)
        draw.rounded_rectangle([ex_x - i, ex_y - i, ex_x + ex_w + i, ex_y + ex_h + i], 
                               radius=10 + i, outline=(0, 0, 0, alpha), width=1)

    # Borde exterior de la ventana Excel
    draw.rounded_rectangle([ex_x, ex_y, ex_x + ex_w, ex_y + ex_h], radius=10, fill=(255, 255, 255, 255), outline=(56, 189, 248, 180), width=2)

    # 2.1 Barra de título Excel (Verde Excel #107C41)
    bar_h = 38
    draw.rounded_rectangle([ex_x, ex_y, ex_x + ex_w, ex_y + bar_h + 10], radius=10, fill=(16, 124, 65, 255))
    draw.rectangle([ex_x, ex_y + bar_h, ex_x + ex_w, ex_y + bar_h + 10], fill=(16, 124, 65, 255)) # tapa redondeo inferior

    # Ícono y texto de la barra de título
    draw.rectangle([ex_x + 14, ex_y + 11, ex_x + 30, ex_y + 27], fill=(255, 255, 255, 230))
    draw.text((ex_x + 18, ex_y + 12), "X", fill=(16, 124, 65, 255), font=font_excel_title)
    draw.text((ex_x + 42, ex_y + 11), "AutoSave [ON]   |   BREVE_ORDINAL_N8.xlsx - Excel   [Grupo Canonico G1 · N=8]", 
              fill=(255, 255, 255, 255), font=font_excel_title)

    # Botones minimizar, maximizar, cerrar ventana
    btn_right = ex_x + ex_w - 20
    draw.text((btn_right - 60, ex_y + 10), "—", fill=(255, 255, 255, 220), font=font_excel_title)
    draw.text((btn_right - 35, ex_y + 9), "□", fill=(255, 255, 255, 220), font=font_excel_title)
    draw.text((btn_right - 10, ex_y + 10), "✕", fill=(255, 255, 255, 220), font=font_excel_title)

    # 2.2 Barra de fórmulas Excel
    fbar_y = ex_y + bar_h + 8
    fbar_h = 32
    draw.rectangle([ex_x, fbar_y, ex_x + ex_w, fbar_y + fbar_h], fill=(243, 244, 246, 255), outline=(209, 213, 219, 255), width=1)

    # Caja de nombre A1
    draw.rectangle([ex_x + 10, fbar_y + 4, ex_x + 65, fbar_y + fbar_h - 4], fill=(255, 255, 255, 255), outline=(209, 213, 219, 255))
    draw.text((ex_x + 37, fbar_y + 7), "A1", fill=(31, 41, 55, 255), font=font_formula, anchor="mt")

    # Botón fx
    draw.text((ex_x + 85, fbar_y + 7), "fx", fill=(107, 114, 128, 255), font=font_formula, anchor="mt")
    draw.line([ex_x + 105, fbar_y + 4, ex_x + 105, fbar_y + fbar_h - 4], fill=(209, 213, 219, 255), width=1)

    # Fórmula activa
    draw.text((ex_x + 120, fbar_y + 7), "=RANKING_ORDINAL_BREVE(emisor=1A..8A; orden=1o..8o; autoposicionamiento=Tu; meta={aE, oE})", 
              fill=(17, 24, 39, 255), font=font_formula)

    # 2.3 Área de la Hoja de Cálculo
    grid_y = fbar_y + fbar_h
    row_num_col_w = 46
    
    col_w_id = 90
    col_w_ord = 135 # 8 columnas x 135 = 1080 px
    col_w_meta = 160 # 2 columnas x 160 = 320 px
    col_widths = [col_w_id] + [col_w_ord] * 8 + [col_w_meta] * 2
    
    total_grid_w = row_num_col_w + sum(col_widths) # 1536 px
    start_grid_x = ex_x + (ex_w - total_grid_w) // 2

    row_h_headers = 34
    row_h_data = 44

    # Coordenadas X de cada columna
    x_positions = [start_grid_x + row_num_col_w]
    for w in col_widths:
        x_positions.append(x_positions[-1] + w)

    # Encabezados de letras de columna (A a K)
    col_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    let_h = 24
    draw.rectangle([start_grid_x, grid_y, x_positions[-1], grid_y + let_h], 
                   fill=(243, 244, 246, 255), outline=(209, 213, 219, 255))
    
    for c_idx, letter in enumerate(col_letters):
        x1 = x_positions[c_idx]
        x2 = x_positions[c_idx + 1]
        draw.line([x2, grid_y, x2, grid_y + let_h], fill=(209, 213, 219, 255), width=1)
        draw.text(((x1 + x2) // 2, grid_y + 4), letter, fill=(107, 114, 128, 255), font=font_row_num, anchor="mt")

    # FILA 1 DE EXCEL (Fila de Macro-Grupos)
    r1_y1 = grid_y + let_h
    r1_y2 = r1_y1 + row_h_headers

    # Columna A (G1)
    draw.rectangle([x_positions[0], r1_y1, x_positions[1], r1_y2], fill=(15, 23, 42, 255), outline=(51, 65, 85, 255))
    draw.text(((x_positions[0] + x_positions[1]) // 2, r1_y1 + 8), "G1", fill=(56, 189, 248, 255), font=font_header_grp, anchor="mt")

    # Columnas B..I (BREVE: ORDEN DE PREFERENCIAS 1º a 8º)
    draw.rectangle([x_positions[1], r1_y1, x_positions[9], r1_y2], fill=(15, 23, 42, 255), outline=(51, 65, 85, 255))
    draw.text(((x_positions[1] + x_positions[9]) // 2, r1_y1 + 8), 
              "ORDEN CONTINUO DE PREFERENCIAS DE CADA EMISOR (1o al 8o Lugar)", 
              fill=(255, 230, 0, 255), font=font_header_grp, anchor="mt")

    # Columnas J..K (PREGUNTAS ADICIONALES)
    draw.rectangle([x_positions[9], r1_y1, x_positions[11], r1_y2], fill=(30, 27, 75, 255), outline=(79, 70, 229, 255))
    draw.text(((x_positions[9] + x_positions[11]) // 2, r1_y1 + 8), 
              "METAPERCEPCIONES", fill=(216, 180, 254, 255), font=font_header_grp, anchor="mt")

    # Números de fila de Excel en la columna lateral
    draw.rectangle([start_grid_x, r1_y1, x_positions[0], r1_y2], fill=(243, 244, 246, 255), outline=(209, 213, 219, 255))
    draw.text((start_grid_x + 23, r1_y1 + 9), "1", fill=(107, 114, 128, 255), font=font_row_num, anchor="mt")

    # FILA 2 DE EXCEL (Encabezados de Columna Oficiales)
    r2_y1 = r1_y2
    r2_y2 = r2_y1 + row_h_headers
    
    draw.rectangle([start_grid_x, r2_y1, x_positions[0], r2_y2], fill=(243, 244, 246, 255), outline=(209, 213, 219, 255))
    draw.text((start_grid_x + 23, r2_y1 + 9), "2", fill=(107, 114, 128, 255), font=font_row_num, anchor="mt")

    # Col A: id
    draw.rectangle([x_positions[0], r2_y1, x_positions[1], r2_y2], fill=(30, 41, 59, 255), outline=(71, 85, 105, 255))
    draw.text(((x_positions[0] + x_positions[1]) // 2, r2_y1 + 7), "id (Emisor)", fill=(56, 189, 248, 255), font=font_col_header, anchor="mt")

    # Cols B..D: 1º, 2º, 3º (ZONA VERDE ESMERALDA DE PREFERENCIA DESTACADA)
    for c_i, label in enumerate(['1o (Max)', '2o', '3o']):
        draw.rectangle([x_positions[1 + c_i], r2_y1, x_positions[2 + c_i], r2_y2], fill=(6, 95, 70, 255), outline=(16, 185, 129, 255))
        draw.text(((x_positions[1 + c_i] + x_positions[2 + c_i]) // 2, r2_y1 + 7), label, fill=(255, 255, 255, 255), font=font_col_header, anchor="mt")

    # Cols E..F: 4º, 5º (ZONA INTERMEDIA)
    for c_i, label in enumerate(['4o', '5o']):
        draw.rectangle([x_positions[4 + c_i], r2_y1, x_positions[5 + c_i], r2_y2], fill=(51, 65, 85, 255), outline=(100, 116, 139, 255))
        draw.text(((x_positions[4 + c_i] + x_positions[5 + c_i]) // 2, r2_y1 + 7), label, fill=(241, 245, 249, 255), font=font_col_header, anchor="mt")

    # Cols G..I: 6º, 7º, 8º (ZONA DE COLA / RECHAZO IMPLÍCITO)
    for c_i, label in enumerate(['6o', '7o', '8o (Min)']):
        draw.rectangle([x_positions[6 + c_i], r2_y1, x_positions[7 + c_i], r2_y2], fill=(136, 19, 55, 255), outline=(244, 63, 94, 255))
        draw.text(((x_positions[6 + c_i] + x_positions[7 + c_i]) // 2, r2_y1 + 7), label, fill=(255, 228, 230, 255), font=font_col_header, anchor="mt")

    # Cols J..K: aE (1º), oE (8º)
    for c_i, label in enumerate(['aE (+1o)', 'oE (-8o)']):
        draw.rectangle([x_positions[9 + c_i], r2_y1, x_positions[10 + c_i], r2_y2], fill=(67, 56, 202, 255), outline=(99, 102, 241, 255))
        draw.text(((x_positions[9 + c_i] + x_positions[10 + c_i]) // 2, r2_y1 + 7), label, fill=(238, 242, 255, 255), font=font_col_header, anchor="mt")

    # DATOS OFICIALES DE LAS 8 FILAS (Sujetos 1A a 8A)
    table_data = [
        ['1A', '2', '3', '8', '1 (Tu)', '4', '7', '5', '6', '2A', '6A'],
        ['2A', '1', '4', '2 (Tu)', '8', '3', '7', '5', '6', '1A', '6A'],
        ['3A', '1', '5', '7', '3 (Tu)', '2', '8', '4', '6', '1A', '6A'],
        ['4A', '1', '2', '4 (Tu)', '8', '3', '7', '5', '6', '1A', '6A'],
        ['5A', '3', '5 (Tu)', '7', '1', '2', '8', '4', '6', '3A', '6A'],
        ['6A', '6 (Tu)', '5', '4', '7', '3', '8', '2', '1', '5A', '1A'],
        ['7A', '2', '3', '7 (Tu)', '1', '5', '8', '4', '6', '2A', '6A'],
        ['8A', '1', '4', '8 (Tu)', '2', '3', '7', '5', '6', '1A', '6A'],
    ]

    curr_y = r2_y2
    for r_idx, row in enumerate(table_data):
        row_y1 = curr_y
        row_y2 = row_y1 + row_h_data
        curr_y = row_y2

        # Número de fila de Excel
        draw.rectangle([start_grid_x, row_y1, x_positions[0], row_y2], fill=(243, 244, 246, 255), outline=(209, 213, 219, 255))
        draw.text((start_grid_x + 23, row_y1 + 14), str(r_idx + 3), fill=(107, 114, 128, 255), font=font_row_num, anchor="mt")

        # Color alternante suave para legibilidad cristalina
        is_even = (r_idx % 2 == 0)

        for c_idx, val in enumerate(row):
            x1 = x_positions[c_idx]
            x2 = x_positions[c_idx + 1]

            # Fondo de la celda según columna
            if c_idx == 0: # ID
                bg = (241, 245, 249, 255) if is_even else (248, 250, 252, 255)
                text_col = (15, 23, 42, 255)
            elif 1 <= c_idx <= 3: # 1º, 2º, 3º (PREFERENCIA DESTACADA EN ESMERALDA)
                bg = (236, 253, 245, 255) if is_even else (209, 250, 229, 255)
                text_col = (6, 95, 70, 255)
            elif 4 <= c_idx <= 5: # 4º, 5º
                bg = (255, 255, 255, 255) if is_even else (248, 250, 252, 255)
                text_col = (30, 41, 59, 255)
            elif 6 <= c_idx <= 8: # 6º, 7º, 8º (COLA / DESCARTE)
                bg = (255, 241, 242, 255) if is_even else (255, 228, 230, 255)
                text_col = (159, 18, 57, 255)
            else: # aE, oE (METAPERCEPCIONES)
                bg = (245, 243, 255, 255) if is_even else (237, 233, 254, 255)
                text_col = (76, 29, 149, 255)

            # Dibujar fondo y cuadrícula
            draw.rectangle([x1, row_y1, x2, row_y2], fill=bg, outline=(209, 213, 219, 255), width=1)

            # Si es el autoposicionamiento "(Tu)", destacarlo con una insignia luminosa
            if "(Tu)" in val:
                tu_w = 96
                tu_h = 28
                tu_x1 = (x1 + x2 - tu_w) // 2
                tu_y1 = (row_y1 + row_y2 - tu_h) // 2
                draw.rounded_rectangle([tu_x1, tu_y1, tu_x1 + tu_w, tu_y1 + tu_h], radius=6, 
                                       fill=(2, 132, 199, 255), outline=(56, 189, 248, 255), width=2)
                draw.text(((x1 + x2) // 2, tu_y1 + 5), val, fill=(255, 255, 255, 255), font=font_cell_tu, anchor="mt")
            else:
                draw.text(((x1 + x2) // 2, row_y1 + 12), val, fill=text_col, font=font_cell, anchor="mt")

    # Pestaña inferior de la hoja Excel
    tab_y = curr_y + 1
    tab_h = 32
    draw.rectangle([start_grid_x, tab_y, x_positions[-1], tab_y + tab_h], fill=(243, 244, 246, 255), outline=(209, 213, 219, 255))
    
    # Pestaña activa 'Protocolo_BREVE'
    tab_w = 170
    draw.rectangle([start_grid_x + 46, tab_y, start_grid_x + 46 + tab_w, tab_y + tab_h - 1], fill=(255, 255, 255, 255))
    draw.line([start_grid_x + 46, tab_y, start_grid_x + 46 + tab_w, tab_y], fill=(16, 124, 65, 255), width=3)
    draw.text((start_grid_x + 46 + tab_w // 2, tab_y + 8), "Protocolo_BREVE", fill=(16, 124, 65, 255), font=font_formula, anchor="mt")

    # 3. MARCADOR Y ANOTACIÓN DESTACADA SOBRE 1º, 2º Y 3º LUGAR (REQUERIMIENTO CENTRAL)
    pref_x1 = x_positions[1]
    pref_x2 = x_positions[4]
    pref_y1 = r1_y1
    pref_y2 = curr_y

    # Marco exterior brillante verde neón sobre las columnas 1º, 2º y 3º
    draw.rectangle([pref_x1 - 2, pref_y1 - 2, pref_x2 + 2, pref_y2 + 2], outline=(0, 255, 135, 255), width=3)

    # 4. CARTELAS EXPLICATIVAS PEDAGÓGICAS (PIE DEL GRÁFICO)
    call_y = ex_y + ex_h + 16
    box_h = 100
    
    # 4.1 Cartela 1: Preferencia 1º, 2º, 3º (Verde Neón)
    c1_w = 460
    c1_x = ex_x
    draw.rounded_rectangle([c1_x, call_y, c1_x + c1_w, call_y + box_h], radius=10, 
                           fill=(6, 78, 59, 230), outline=(0, 255, 135, 255), width=2)
    draw.text((c1_x + 16, call_y + 12), "1. PREFERENCIAS / ELECCION (1o, 2o y 3o LUGAR)", 
              fill=(0, 255, 135, 255), font=font_callout_title)
    draw.text((c1_x + 16, call_y + 38), 
              "Cada emisor (fila) situa obligatoriamente a sus preferidos\nen 1o, 2o y 3o lugar, capturando la afinidad positiva (+E)\ncon intensidad y orden continuo real (pesos 1.0, 0.8, 0.6).", 
              fill=(226, 232, 240, 255), font=font_callout_body)

    # 4.2 Cartela 2: Emisores / Filas (Azul Cian)
    c2_w = 380
    c2_x = c1_x + c1_w + 16
    draw.rounded_rectangle([c2_x, call_y, c2_x + c2_w, call_y + box_h], radius=10, 
                           fill=(12, 74, 110, 230), outline=(56, 189, 248, 255), width=2)
    draw.text((c2_x + 16, call_y + 12), "2. CADA FILA ES UN SUJETO EMISOR", 
              fill=(56, 189, 248, 255), font=font_callout_title)
    draw.text((c2_x + 16, call_y + 38), 
              "Filas 1A a 8A: Cada persona del colectivo\nexpresa su criterio ordenando a los demas miembros.\nNo hay omisiones ni respuestas en blanco.", 
              fill=(226, 232, 240, 255), font=font_callout_body)

    # 4.3 Cartela 3: Autoposicionamiento (Amarillo Ámbar)
    c3_w = 370
    c3_x = c2_x + c2_w + 16
    draw.rounded_rectangle([c3_x, call_y, c3_x + c3_w, call_y + box_h], radius=10, 
                           fill=(120, 53, 15, 230), outline=(255, 230, 0, 255), width=2)
    draw.text((c3_x + 16, call_y + 12), "3. AUTOPOSICIONAMIENTO «(Tu)»", 
              fill=(255, 230, 0, 255), font=font_callout_title)
    draw.text((c3_x + 16, call_y + 38), 
              "El emisor se incluye a si mismo en la escala.\nPermite medir autoestima relacional, modestia o\nprotagonismo sin requerir preguntas invasivas.", 
              fill=(226, 232, 240, 255), font=font_callout_body)

    # 4.4 Cartela 4: Metapercepciones aE / oE (Púrpura)
    c4_w = 380
    c4_x = c3_x + c3_w + 16
    draw.rounded_rectangle([c4_x, call_y, c4_x + c4_w, call_y + box_h], radius=10, 
                           fill=(76, 29, 149, 230), outline=(192, 132, 252, 255), width=2)
    draw.text((c4_x + 16, call_y + 12), "4. METAPERCEPCIONES (aE / oE)", 
              fill=(192, 132, 252, 255), font=font_callout_title)
    draw.text((c4_x + 16, call_y + 38), 
              "aE: Quien crees que te eligio 1o? (+pE)\noE: Quien crees que te relego al 8o? (-pR)\nGenera las 4 coordenadas del Tetragrama SMIb.", 
              fill=(226, 232, 240, 255), font=font_callout_body)

    # Guardar en alta resolución
    img.save(output_path, 'PNG', optimize=True)
    print(f"✅ Imagen generada con éxito en: {output_path} ({width}x{height} px)")

if __name__ == '__main__':
    target = os.path.abspath('05_Web_Promocional/assets/tabla_breve_excel_n8.png')
    create_excel_breve_image(target)
