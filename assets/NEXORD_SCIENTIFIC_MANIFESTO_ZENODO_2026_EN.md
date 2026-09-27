![NEXORD Institutional Logo](logo_nexord_base.png)

# COMPUTATIONAL ORDINAL SOCIOMETRY AND GROUP DYNAMICS DIAGNOSTICS (NEXORD PLATFORM)
## Scientific Manifesto, Theoretical-Methodological Framework, and Open Science Governance Guidelines (Canonical Edition 2026)

**Author:** Dr. José Manuel Cornejo Álvarez  
*Full Professor of Social Psychology*  
*Faculty of Psychology, University of Barcelona (UB)*  
*Creator of the NEXORD Platform and Promotor of the Sociometric Data Bank (BSOC)*  
**ORCID:** `0000-0002-1234-5678`  
**Concept DOI (Zenodo / CERN):** [10.5281/zenodo.18926396](https://doi.org/10.5281/zenodo.18926396)  
**Homologated Edition DOI:** [10.5281/zenodo.18941691](https://doi.org/10.5281/zenodo.18941691)  
**Canonical Certified Version:** v8.0 (2026)  
**Master Ecosystem:** VISORD (Visual Ordinal Sociometry & Group Dynamics Diagnostics)  
**Official Web Platform:** [https://josemancor.github.io/soc-ord-web/](https://josemancor.github.io/soc-ord-web/)  
**Open Source Repository:** [https://github.com/josemancor/soc-ord-web](https://github.com/josemancor/soc-ord-web)  

---

## Executive Summary

The scientific investigation of interpersonal networks and human collectives has historically been constrained by two methodological limits: reliance on discrete binary tallies (choice/rejection) and dispositional models detached from interactive field dynamics. The **NEXORD Platform (Ordinal Nexus)** formalizes a continuous, processual approach to group dynamics, translating classical psychosocial foundations into advanced computational methods.

NEXORD integrates foundational traditions (Jacob L. Moreno, Kurt Lewin, Fritz Heider, Robert F. Bales) into a continuous ordinal formulation where **active relational interaction is placed at the ontological core of group reality**. The dynamics of **GIVING and RECEIVING constitute indissociable moments of a single relational circuit**.

The platform is designed both for academic research and applied group diagnostics across educational, organizational, clinical, and community domains. It incorporates:
1. The **BRIEF Strategic Format** of full hierarchical ranking without ties, mathematically articulated in two complementary matrices: **A(i, rank)** (direct emitted ordinal sequences) and **B(i, j)** (rank distribution sociomatrix), coupled with **reflexive diagonal self-anchoring** (sensors of self-image misalignment IDA, hierarchical tension ITA, and structural cohesion ICE).
2. The **GxTyCz multidimensional design space**, imposing no a priori restrictions on analytical designs across groups (G), longitudinal waves (T), multiplex criteria (C), and contextual attributes (Z).
3. The **Q81 tensorial lattice** (81 dyadic configurations and 255 Boolean indicators I255), structured within the **10 canonical densities pentagram** and polarized into the complementary macro-dimensions **DA** (outbound emission) and **RECIBE** (inbound reception).
4. The **psychologization of group field regimes**, recognizing relational friction (Φ) as a necessary condition for adaptive viability against the risks of Groupthink (Janis, 1972), guiding intervention toward non-punitive unjamming or dignified ecosystemic relocation.
5. Versatile **graphical solutions** for continuous spatial navigation, including 3D sociograms, 2D(6) factorial projections (Benzécri, 1973; Cornejo, 1988) with slender vertical axes (COR, CTA, CTR), and comparative structurograms.
6. The capability to **monitor face-to-face experimental designs in the physical laboratory**, capturing real-time interpersonal micro-processes and social dilemma resolution.
7. **Multimodal diagnostics grounded in the iceberg model**, rendering visible and audible both surface interactions and deep relational currents through graphical solutions and hydrodynamic sonification (calibrated at 432 Hz).
8. Scale-invariant comparison via **Grassmannian manifolds Gr(k, N)** and zero-reactivity experimental validation via **CULTURAL Sociometry** (dramatic and literary corpora).
9. An institutional governance framework rooted in **Ethics by Design**, Open Science (FAIR Data), SHA3-512 cryptographic sealing (Clélie Protocol), and custodianship under the **Sociometric Data Bank (BSOC / University of Barcelona)**.

*Keywords:* Computational Ordinal Sociometry, NEXORD Platform, VISORD Ecosystem, Sociometric Data Bank (BSOC), BRIEF Format, Matrix Duality, Reflexive Diagonal Closure, Relational Densities Pentagram, Field Regimes, Groupthink, GxTyCz Design Space, Physical Laboratory Monitoring, Graphical Solutions, Iceberg Model, Hydrodynamic Sonification, Grassmann Manifold, CULTURAL Sociometry, Clélie Protocol, Ethics by Design, Open Science.

---

## 1. Epistemological Framework: The Ontology of the Relational Tie

### 1.1. From Discrete Topology to the Continuous Group Field
Sociometry, in the formulation introduced by Jacob Levy Moreno (1934), made visible the affective structure of human groups. However, computational constraints forced classical sociometry to rely on discrete binary nominations (three choices and three rejections).

Computational Ordinal Sociometry represents the contemporary realization of this heritage: it mathematizes interpersonal psychological distance by quantifying hierarchical preferential rank through the inverse rank function:

![Formula 1: Relational Decay](formulas/Formula_1_Decaimiento_Relacional.png)

where r_ij denotes the strict ordinal rank assigned by sender i to receiver j, and gamma > 0 governs the relational decay and openness of the group field. This law transforms qualitative ordering into continuous relational magnitude, formalizing the historical intuition of the «Carte de Tendre» (Scudéry, 1654) into a measurable, continuous field.

![Figure 1: Continuous 3D Sociogram of the Relational Field](Figure_Sociogram_3D_Continuous_Plasma_N50.png)  
*Figure 1: Continuous 3D Sociogram of the relational field in a high-density collective (N=50). Modeling the group as a continuous field with active relational vectors (cyan: attraction; magenta: friction), real-time telemetry HUD, and longitudinal tracking.*

### 1.2. The Fundamental Axiom: GIVING and RECEIVING as Indissociable Elements
Social psychology has often oscillated between dispositional models (attributing group phenomena to isolated individual traits) and structural network models (analyzing formal graphs devoid of phenomenological meaning).

NEXORD establishes as its core epistemological axiom that **active relational interaction is the constitutive substance of group reality**. In any collective, the acts of **GIVING** (outbound choices, expectations, demands) and **RECEIVING** (inbound peer evaluations, appraisals, discards) are neither independent variables nor exclusive properties of isolated actors: they are **indissociable moments of a single relational circuit**. Collective health or dysfunction resides in the fluidity, symmetry, and friction of these mutual flows. Detaching these two polar moments produces incomplete diagnostics blind to latent structural isolation, such as when an actor emits positive choices while facing unanimous peer exclusion.

---

## 2. Capture Protocol: The BRIEF Strategic Format, Matrix Duality, and Diagonal Closure

### 2.1. Full Hierarchical Ranking without Ties & Matrix Duality: A(i, rank) vs. B(i, j)
The BRIEF Strategic Format replaces fragmented questionnaires with a **single cognitive task of full hierarchical ranking** across group members based on a unified functional or affective criterion.
* **Elimination of arbitrary quotas:** Transcends traditional restrictions ("choose up to 3 peers"), preventing information truncation.
* **Forced drag without ties:** Participants rank peers vertically between maximum preference and rejection poles under a strict zero-ties rule (r_ij != r_ik), eliminating acquiescence bias.
* **Formalization in two complementary matrices:**
  * **Matrix A(i, rank) BRIEF:** Captures raw emitted ordinal sequences. Rows represent senders i, columns represent ordinal ranks k in {1st, ..., Nth}, and cell contents identify the peer placed at that rank: A(i, k) = j.
  * **Matrix B(i, j) RANK DISTRIBUTION:** Square sociomatrix (N × N) where rows represent senders i, columns represent receivers j, and cell values record the assigned numerical rank: B(i, j) = k if and only if A(i, k) = j.

![Figure 2: Data Ingestion and Transformation Architecture](Figure_Section_2_1_Input_Data_BREVE.png)  
*Figure 2: Data ingestion and transformation architecture: from raw rankings to Q81 perceptual space, demonstrating the convergence of matrix structures.*

### 2.2. The GxTyCz Multidimensional Design Space without a Priori Constraints
The mathematical formulation of NEXORD imposes no a priori limitations or restrictions on research and diagnostic designs:
* **Groups (G):** Accommodates any number of independent collectives, organizational departments, educational cohorts, or experimental teams.
* **Temporal Waves (T):** Supports longitudinal tracking across T timepoints (T1, T2, ..., Tn), tracing diachronic structural evolution.
* **Multiplex Criteria (C):** Models multiple functional and affective criteria simultaneously (C1 task competence, C2 social bonding, C3 crisis leadership), capturing topological shifts across evaluative lenses.
* **Contextual Variables (Z):** Seamlessly incorporates demographic attributes (age, gender, tenure) and group activity scales (AAG; Vicente, Cornejo & Barbero, 2006).

### 2.3. Diagonal Self-Anchoring and the Triple Nuclear Sensor
In contrast to classical sociometry, which leaves the main diagonal empty (r_ii = empty), the BRIEF Format requires participants to **locate themselves within their estimated hierarchical rank** (r_ii in {1, ..., N}). This reflexive self-anchoring closes the sociomatrix as a continuous manifold and deploys three analytical sensors:

1. **Self-Image Discrepancy Index (IDA_i):** Measures the angular deviation between subjective self-image (r_ii) and received peer consensus (R_ext_i):

![Formula 2: Self-Image Discrepancy IDA](formulas/Formula_2_Desajuste_Autoimagen_IDA.png)

where IDA < 0 marks status overestimation, IDA > 0 indicates self-deprecation or timidity, and IDA = 0 reflects balanced social calibration. Group dispersion is computed quadratically:

![Formula 3: Group Discrepancy IDA_group](formulas/Formula_3_Desajuste_Grupo_IDA_grupo.png)

2. **Hierarchical Tension Index (ITA) and Structural Cohesion (ICE):** ITA in [0, 1] captures friction when multiple members compete for top leadership (r_ii = 1). Combining ITA with IDA_group, NEXORD defines the **Relational Friction Coefficient (Φ)** and the **Structural Cohesion Index (ICE)**:

![Formula 4: Relational Friction and Structural Cohesion ICE](formulas/Formula_4_Friccion_Cohesion_ICE.png)

3. **Cognitive Anchoring and Combinatorial Reduction P(k):** By positioning oneself at rank k, the combinatorial evaluation space conditions to P(k) = (k-1)!(N-k)!, formalizing that interpersonal evaluations are projected upward or downward from the self:

![Formula 5: Combinatorial Anchoring P(k)](formulas/Formula_5_Anclaje_Combinatorio_Pk.png)

---

## 3. Relational Dynamics: Psychologization of Field Regimes, Friction, and Viability

### 3.1. Friction Coefficient (Φ) and Structural Cohesion (ICE)
The Relational Friction Coefficient (Φ) and the Structural Cohesion Index (ICE) provide a synthesized metric of systemic tension. Moderate levels of friction reflect internal dynamism and cognitive diversity, whereas extreme values warn of structural deadlock or fragmentation.

### 3.2. Psychologization of Field Regimes and Prevention of Groupthink
NEXORD deliberately avoids treating collective dynamics as mere inanimate physics: field states represent qualitative regimes of psychosocial articulation:
* **Regime of Structural Rigidity and Inertia:** Characterized by frozen hierarchies, rigid roles, and low communicative permeability.
* **Regime of Fluidity and Adaptive Cohesion:** Characterized by open relational homeostasis, flexible roles, and constructive mutual feedback.
* **Regime of Dispersion and Anomie:** Characterized by low coupling density, disengagement, and weak collective grounding.
* **Regime of Effervescence and Collective Fusion:** Characterized by shared emotional activation and intense interactive mobilization.

Within this framework, NEXORD questions the assumption that optimal functioning equals absolute cohesion (ICE = 1.0, Φ = 0). A collective devoid of internal friction represents a vulnerable system prone to **Groupthink** (Janis, 1972), where unanimity pressures suppress critical deliberation. Relational friction and transactional gradients supply the necessary energy for collective plasticity and adaptive learning.

### 3.3. The Living Puzzle: Unjamming vs. Dignified Ecosystemic Relocation
When an individual generates friction or appears misaligned within a team, conventional systems frequently resort to punitive exclusion. In NEXORD, the group is conceptualized as a living puzzle. An actor experiencing friction is not inherently defective: they typically face a positional mismatch or flow asymmetry within their immediate network.

Diagnostic intervention prioritizes **non-punitive unjamming** via minimal local adjustment: clarifying roles, modulating tasks, and facilitating collaboration. When persistent structural incompatibility remains after systematic intervention, the framework recognizes the appropriateness of **dignified ecosystemic relocation**, preserving personal wellbeing and preventing chronic ostracism.

---

## 4. Matrix Algebra, Primary Relational Densities, and the Densities Pentagram

### 4.1. The Canonical Tetragram and Primary Moments
Within NEXORD's matrix architecture, each cell (i, j) integrates four atomic moments:
* **A1 = pDA:** Emitted expectation (what sender i expects receiver j will choose).
* **A2 = DA:** Emitted choice (effective preference emitted by sender i to receiver j).
* **A3 = RECIBE:** Received choice (effective preference received by sender i from receiver j).
* **A4 = pRECIBE:** Received expectation (what receiver j expects sender i will choose).

The system articulates the 81 exhaustive relational configurations of dyadic space (Q81 = 3^4 = 81) and 255 Boolean indicators (I255).

![Table 1: Canonical 9x9 Lattice of Q81 Relational Figures](Tabla_Anexo_I_Matriz_Q81.png)  
*Table 1: Canonical 9x9 lattice of Q81 relational figures, showing how sender rows and receiver columns generate the 81 dyadic configurations.*

### 4.2. The Densities Pentagram: Macro-Dimensions DA (Sender) and RECIBE (Receiver)
The ten continuous relational densities are harmoniously structured within the Densities Pentagram, organized across two polar macro-dimensions:
* **Macro-Dimension DA (Sender Block):** Encompasses outbound kinetic mass to effective choice: BDA (kinetic mass) -> SDA (net potential) -> A1 (pDA) -> A2 (DA).
* **Macro-Dimension RECIBE (Receiver Block):** Encompasses inbound effective choice to received kinetic mass: A3 (RECIBE) -> A4 (pRECIBE) -> SRC (net potential) -> BRC (kinetic mass).
* **Relational System Closure:** The collective couples through Net Relational Potential (SDR = SDA + SRC) and Total Kinetic Mass (BDR = BDA + BRC), monitoring positional asymmetry through Dif-DR = SDA - SRC.

![Formula 6: Tetragram Decomposition into Densities Dk](formulas/Formula_6_Descomposicion_Tetragrama_Dk.png)

---

## 5. Graphical Solutions, Experimental Laboratories, and Multimodal Perception

### 5.1. Continuous Graphical Solutions: 3D Sociograms and 2D(6) Factorial Planes
NEXORD deploys versatile graphical solutions to represent the continuous relational field with clarity:
* **Three-Dimensional Continuous Sociograms:** Spatial rendering of attraction basins (neon green, <Ee>), opposition zones (orange), and friction regions (magenta, [Rr]), equipped with longitudinal temporal controls.
* **2D(6) Factorial Planes and Slender Vertical Axes:** Projections derived from correspondence analysis and principal component analysis (Benzécri, 1973; Cornejo, 1988), flanked by slender vertical axes displaying absolute contribution (CTA) and representation quality (COR).
* **Intergroup Structurograms:** Relational support polygons supporting comparative morphological diagnostics across teams.

![Figure 3: Graphical Solutions for 3D Relational Exploration](Figure_Section_4_1_VISORD_3D_Engine.png)  
*Figure 3: Operational console displaying graphical solutions for 3D relational navigation.*

![Figure 4: Comparative Factorial Plane and Structurograms](Figure_Section_4_2_Comparative_Factorial_Plane_G1_G2.png)  
*Figure 4: Comparative 2D factorial plane showing relational structurograms and tension vectors between groups.*

### 5.2. Monitoring Face-to-Face Experimental Designs in the Physical Laboratory
The platform supports the systematic monitoring of face-to-face experimental designs in physical social psychology laboratories. In observation rooms, group dynamics seminars, and team behavioral facilities, NEXORD captures interpersonal dynamics in real time, tracking the emergence of informal leadership structures, reciprocity, and network centrality during collaborative tasks.

### 5.3. Processual Sociometry and Social Dilemma Resolution
Moving beyond static cross-sectional sociometry, Processual Sociometry records continuous communicative events. By defining an **interaction space** and tracking **interaction counters** (speaking turns, intervention frequency, listening ratios), the platform models social dilemma dynamics. It quantifies behaviors of cooperation, caution, skepticism, and free-riding, enabling experimental studies on trust building and social capital formation under strict anonymization.

### 5.4. Multimodal Perception: The Iceberg Model and Hydrodynamic Sonification
In all human groups, a visible surface layer (formal roles, explicit agreements, observable behavior) is sustained by a deep, submerged relational foundation (unspoken expectations, latent tensions, unvoiced affinities, and subtle rejections). The fundamental methodological objective is to **render visible and audible the dynamics and processes of group interaction**:
* **Visual Dimension:** Articulated through continuous graphical solutions and 3D sociograms.
* **Auditory Dimension (Hydrodynamic Sonification):** Translates friction gradients (Φ), net potential (SDR), and flow asymmetries into harmonic acoustic frequencies (calibrated at 432 Hz with distinct timbral textures). This auditory mapping allows researchers to listen to relational tension or harmony, providing a complementary perceptual modality for detecting dynamics submerged beneath the visible surface.

### 5.5. Scale-Invariant Geodesic Distance on Grassmann Manifolds Gr(k, N)
To compare formally independent collectives without enforcing artificial cross-group links, each group is modeled as a k-dimensional subspace in R^N. From canonical Jordan angles cos(theta_m) = sigma_m(U_1^T U_2), scale-invariant geodesic distance is calculated:

![Formula 7: Geodesic Distance on Grassmann Manifolds](formulas/Formula_7_Distancia_Geodesica_Grassmann.png)

This metric quantitatively determines whether two collectives share structural morphology regardless of sample size differences.

### 5.6. CULTURAL Sociometry: Complete Relational Biographies with Zero Reactivity
Through the CULTURAL data category, NEXORD transcribes dramatic, cinematic, and narrative masterpieces into ordinal sociomatrices. Serving as complete and finalized relational records, literary corpora enable the forensic analysis of extreme dynamics (such as polarization or authoritarianism in works by Lorca, Sartre, or Rose) within an experimental framework with zero evaluation reactivity.

---

## 6. Governance, Ethics by Design, and Open Science

### 6.1. Ethics by Design and Non-Punitive Interdiction
The platform embeds ethical safeguards directly into technical algorithms (*Ethics by Design*). The system explicitly prohibits punitive deployments, negative selection, or elimination rankings. Analysis on empirical field datasets (REAL category) requires authentication and formal accountability by an accredited Principal Investigator (PI).

### 6.2. Open Science, Clélie Protocol, and Academic Custodianship (BSOC)
In accordance with Open Science and FAIR Data principles, NEXORD's mathematical and methodological formulations are publicly accessible. To protect participant confidentiality, empirical field datasets undergo canonical anonymization (1A1a..5A1a) and cryptographic hash sealing (SHA3-512, Clélie Protocol), under the academic custodianship of the Sociometric Data Bank (BSOC / University of Barcelona).

### 6.3. Participant Rights and Constructive Feedback
Participants receive individual codes to audit data processing fidelity without accessing peer records. Node re-identification is strictly restricted to the responsible PI within guidance or supportive group mediation. All feedback is constructive, non-stigmatizing, and dedicated to promoting collective health.

---

## 7. Canonical Technical Annexes

### ANNEX I: Dual Matrices (SMIb/SMIa), Master 9x9 Lattice of Q81, and I255 Catalog
* **SMIb Matrix:** Stores the numerical tetragram (A1 · A2 · A3 · A4) = (pDA · DA · RECIBE · pRECIBE) in each cell (i, j).
* **SMIa Matrix:** Condenses the tetragram into the 81 dyadic configurations (1 = [Rr], 41 = ¡¿?!, 81 = <Ee>).
* **Boolean Indicator Catalog I255:** Disjunctive partitioning of dyadic space along the diagonal of perceptual consonance.

### ANNEX II: Factorial Quality Metrics (COR, CTA, CTR), Vertical Axes, and 2D(6) Projection
* **Factorial Metrics (Cornejo, 1988):**
  * COR measures representation quality of node i on factor alpha.
  * CTA expresses the percentage of factor inertia explained by element i.
  * CTR reflects global cumulative explained variance.
* **Vertical Factorial Axes:** Slender vertical axes rank nodes by structural weight, preventing visual crowding in saturated 2D scatter plots.

![Figure Annex II: Dual 1D Factorial Vertical Axes](Figura_Anexo_II_Ejes_Verticales_Factoriales.png)  
*Figure Annex II: Dual 1D factorial vertical axes (COR, CTA, CTR) sorting elements by representation quality and inertia contribution.*

### ANNEX III: Catalog of the 10 Ecosystemic Domains
NEXORD calibrates Relational Inertia (alpha) and Relational Decay (gamma) across 10 institutional domains:

![Table Annex III: Catalog of 10 Ecosystemic Domains](Table_Annex_III_10_Ecosystemic_Domains_EN.png)  
*Table Annex III: Parametric calibration across 10 institutional and ecosystemic domains.*

### ANNEX IV: Sender - Receiver Rank Interdistances and Isometry Diagonal
Euclidean distances for sender emission (d_DA) and receiver reception (d_RC) preserving strict sender ordering:
* **Isometry Diagonal (d_DA = d_RC):** Evaluates relational symmetry and verifies the Relational Asymmetry Principle (reception dispersion systematically exceeds emission dispersion).

![Figure Annex IV: Dispersion Plot of Euclidean Interdistances](Figura_Anexo_IV_Plano_Interdistancias_G2T1C1.png)  
*Figure Annex IV: Dispersion plot of Euclidean interdistances d_DA vs d_RC.*

![Table Annex IV: Euclidean Interdistances Table](Table_Annex_IV_Interdistances_G2T1C1_EN.png)  
*Table Annex IV: Euclidean range interdistances (d_DA vs d_RC) for study G2T1C1.*

---

## 8. Canonical References

1. Absil, P.-A., Mahony, R., & Sepulchre, R. (2008). *Optimization algorithms on matrix manifolds*. Princeton University Press.
2. Avramidis, E., Strogilos, V., Aroni, K., & Kankaraki, C. T. (2017). Using sociometric techniques to assess the social impacts of inclusion. *Educational Research Review*, 20, 68–80.
3. Bales, R. F. (1950). *Interaction process analysis: A method for the study of small groups*. Addison-Wesley.
4. Benzécri, J.-P. (1973). *L'Analyse des Données: T. 2, L'Analyse des Correspondances*. Dunod.
5. Borsboom, D., et al. (2021). Network analysis of multivariate data in psychological science. *Nature Reviews Methods Primers*, 1(1), 58.
6. Cornejo, J. M. (1988). *Técnicas de investigación social: El análisis de correspondencias*. PPU.
7. Cornejo, J. M. (2026). *Computational Ordinal Sociometry (NEXORD): An Algorithmic, Matrix, and 4D Socio-Thermodynamic Framework*. Zenodo. https://doi.org/10.5281/zenodo.18926396
8. Festinger, L. (1950). Informal social communication. *Psychological Review*, 57(5), 271–282.
9. Heider, F. (1958). *The psychology of interpersonal relations*. John Wiley & Sons.
10. Janis, I. L. (1972). *Victims of Groupthink: A psychological study of foreign-policy decisions and fiascoes*. Houghton Mifflin.
11. Kenny, D. A., & Garcia, R. L. (2012). Using the Actor–Partner Interdependence Model to study the effects of group composition. *Small Group Research*, 43(4), 468–496.
12. Lewin, K. (1951). *Field theory in social science: Selected theoretical papers*. Harper & Row.
13. Morales Domínguez, J. F., & Cornejo Álvarez, J. M. (2026). Sociometría Ordinal Computacional. La Plataforma NEXORD: Hacia una Física de lo Grupal. *Psicothema* (in review).
14. Moreno, J. L. (1934). *Who shall survive? A new approach to the problem of human interrelations*. Nervous and Mental Disease Publishing Co.
15. Nicolis, G., & Prigogine, I. (1977). *Self-organization in nonequilibrium systems: From dissipative structures to order through fluctuations*. John Wiley & Sons.
16. Scudéry, M. de (1654). *Clélie, histoire romaine*. Augustin Courbé.
17. Tsankova, E., & Tair, E. (2021). Meta-accuracy in sociometric status perceptions. *Frontiers in Psychology*, 12, 642398.
18. Vicente, R., Cornejo, J. M., & Barbero, F. (2006). Análisis de la Actividad Grupal (AAG). *Psicothema*, 18(3), 445–452.
19. Ye, K., & Lim, L.-H. (2016). Schubert varieties and distances on Grassmann manifolds. *SIAM Journal on Matrix Analysis and Applications*, 37(3), 1176–1197.

---

*(C) 2026 Dr. José Manuel Cornejo Álvarez / NEXORD Platform (VISORD) / Sociometric Data Bank BSOC / University of Barcelona.*  
*Published under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).*
