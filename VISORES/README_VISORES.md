# 📂 CARPETA VISORES: COMODINES UNIVERSALES SMIb PARA VISORD
## Banco Universal de Sociomatrices de Simulación y Prueba

Esta carpeta contiene los **archivos comodín universales (.json)** que pueden ser cargados e intercambiados de manera simultánea en cualquiera de los entornos VISORD de la plataforma:
- **`VISORD_Acuario`** (`visord_acuario.html`)
- **`VISORD_demo`** (`VISORD_demo/index_demo.html`)
- **`VISORD_cultural`** (`visord_cultural.html`)
- **`VISORD_dialéctico`** (`visord_dialectico.html`)
- **`VISORD_radiológico`** (`radiografias_relacionales.html`)

---

### 📦 Archivos Comodín Disponibles:

1. **`SIMUL_01_COHESION_CANONICA_20x20.json`**:
   - **Clave:** `SIMUL-AA-G1-T2-C2-V10-A16-ES-20`
   - **Dimensión:** $N=20$ sujetos, 380 díadas dirigidas.
   - **Régimen:** Cohesión equilibrada, dinámica fluida, baricentro exacto y 6 prismas opuestos ($ho=0.784$).
   
2. **`SIMUL_02_POLARIZACION_FACCIONES_12x12.json`**:
   - **Clave:** `SIMUL-AA-G2-T1-C1-V10-A16-ES-12`
   - **Dimensión:** $N=12$ sujetos, 132 díadas dirigidas.
   - **Régimen:** Dos facciones polarizadas ($1..6$ vs $7..12$) con rechazo frontal intergrupal y dos nodos puente en tensión.

3. **`SIMUL_03_ASFIXIA_HALO_JERARQUIA_8x8.json`**:
   - **Clave:** `SIMUL-AA-G1-T1-C1-V10-A16-ES-8`
   - **Dimensión:** $N=8$ sujetos, 56 díadas dirigidas.
   - **Régimen:** Autocracia y **Asfixia por Halo** ($BDF/BDC = 0.28 < 0.40$). Hipertrofia de conjeturas y bloqueo factual.

---

### 📐 Principio de Ingestión Canónica:
**Siempre partiendo de matrices SMIb:** Cada celda contiene el tetragrama canónico $[A_1, A_2, A_3, A_4]$:
- $A_1 (p\_DA)$: Expectativa del emisor.
- $A_2 (DA)$: Elección efectiva del emisor.
- $A_3 (REC)$: Elección efectiva del receptor ($REC_{ij} \equiv DA_{ji}$).
- $A_4 (p\_REC)$: Expectativa del receptor.

*Homologado por el Research Core de NEXORD Platinum 2026.*
