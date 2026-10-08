# 🏛️ PROTOCOLO CANÓNICO: CARTELERA ACTIVA Y FONDO DE RESERVA CULTURAL
## Regla de no saturación cognitiva y rotación periódica de obras en VISORD Cultural

**Ecosistema:** NEXORD / VISORD 2026  
**Norma de Calidad:** Platinum Grade v6.0  
**Área:** Sociometría Cultural, Humanidades Digitales y Psicología de Grupos  
**Autoría & Custodia:** Prof. Dr. José Manuel Cornejo (IP) & NEXORD Engineering Core • CERN Zenodo DOI: `10.5281/zenodo.18941691`  

---

### 🎭 1. PRINCIPIO DE ECONOMÍA COGNITIVA: LA TRÍADA CANÓNICA ACTIVA
Para evitar sobrecargar la red, prevenir la fatiga perceptual de los visitantes y optimizar el aprendizaje, la cartelera pública de **VISORD Cultural** (`visord_cultural.html`) se estructura en torno a una **Tríada Paradigmática Activa de 3 Obras Maestras**:

1. **`hombres12` — 12 Hombres sin Piedad (Reginald Rose / Sidney Lumet • N=12)**:
   - **Régimen Socio-Termodinámico:** Consenso progresivo y reversión de la inercia masiva.
   - **Dinámica:** La influencia minoritaria de Davis (Jurado 8) disuelve el prejuicio inicial (11-1) hasta el consenso unánime de la duda razonable (12-0) a lo largo de 5 actos.
2. **`lorca` — La Casa de Bernarda Alba (Federico García Lorca • N=8)**:
   - **Régimen Socio-Termodinámico:** Autocracia matriarcal, luto cerrado y compresión adiabática.
   - **Dinámica:** El vector represivo de Bernarda (el bastón) colisiona frontalmente con el deseo de Adela por Pepe el Romano, desatando una red oculta de tensiones y suicidio.
3. **`moscas` — El Señor de las Moscas (William Golding • N=9)**:
   - **Régimen Socio-Termodinámico:** Colapso institucional, fractura civilizatoria y tribalismo salvaje.
   - **Dinámica:** La democracia deliberativa articulada por Ralph en torno a la caracola y el fuego es absorbida por el atavismo cinegético de Jack y el asesinato ritual.

---

### 📦 2. CATÁLOGO DEL FONDO DE RESERVA CULTURAL (BOVEDA DE ROTACIÓN)
Las obras adicionales se conservan archivadas en la carpeta `/data/reserva_cultural/`, listas para ser sustituidas o rotadas en la cartelera activa periódicamente:

| Obra en Reserva | Archivo Payload | N | Régimen Demostrativo |
| :--- | :--- | :---: | :--- |
| **La Ola (Die Welle)** | `OBRA_RESERVA_01_LA_OLA_N7.json` | 7 | Sincronización disciplinaria colectiva, hostigamiento a disidentes y fanatismo escolar armado. |
| **Clara Campoamor: El Debate** | `OBRA_RESERVA_02_CLARA_CAMPOAMOR_N9.json` | 9 | Debate parlamentario histórico sobre el voto femenino en las Cortes Constituyentes de 1931. |
| **Hamlet** | *En preparación* | 8 | Paranoia cortesana, simulación de locura, espionaje y sospecha fratricida. |
| **Fuenteovejuna** | *En preparación* | 10 | Rebelión comunitaria y responsabilidad colectiva ante el abuso feudal. |

---

### 🔄 3. PROCEDIMIENTO DE ROTACIÓN EN CARTELERA
Para reemplazar una de las 3 obras activas por una obra de la reserva:
1. Acceder al código fuente de `visord_cultural.html`.
2. Sustituir la clave de la tarjeta en `.hub-cards-grid` (por ejemplo, reemplazar `moscas` por `la_ola`).
3. Actualizar la clave por defecto en `activeWorkKey`.
4. Los investigadores pueden además cargar cualquier obra de la reserva directamente en el visor utilizando el botón protegido **`[ 📂 Cargar Obra de Reserva ]`** mediante la contraseña institucional **`NEX_ORD`**.
