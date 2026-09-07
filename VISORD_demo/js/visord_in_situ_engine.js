/**
 * NEX_ORD - VISORD IN SITU COMPUTATION ENGINE
 * Motor socio-termodinámico y analítico in situ (Client-Side Pure JavaScript)
 * 
 * Capacidades:
 * 1. Inter-proximidad DA/RC, Tensión Individual y Gráfica de Dispersión Cuadrantal.
 * 2. Análisis Espectral Laplaciano, Conectividad de Fiedler (lambda_2), Radio Espectral y Frustración de Heider.
 * 3. Transformada Rápida de Fourier (FFT / DFT) y Espectro Armónico de Potencia sobre densidades SDR/BDR.
 * 4. Cadenas de Markov, Matriz de Transición Estocástica y Masa Gravitatoria (PageRank Sociométrico).
 * 5. Variedad de Grassmann Gr(3, 12), Ángulos Principales y Distancias Geodésicas inter-oleadas.
 */

(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.VisordInSituEngine = factory();
    }
}(typeof self !== 'undefined' ? self : this, function() {

    const JURORS = [
        { id: 1, code: '1A1a', name: 'Sujeto 1 (1A1a)', actor: '1A1a', role: 'Nodo Coordinador / Moderador', color: '#38BDF8' },
        { id: 2, code: '2A1a', name: 'Sujeto 2 (2A1a)', actor: '2A1a', role: 'Nodo Consonante', color: '#818CF8' },
        { id: 3, code: '3A1a', name: 'Sujeto 3 (3A1a)', actor: '3A1a', role: 'Polo de Oposición / Fricción', color: '#FF007F' },
        { id: 4, code: '4A1a', name: 'Sujeto 4 (4A1a)', actor: '4A1a', role: 'Nodo Analítico', color: '#38BDF8' },
        { id: 5, code: '5A1a', name: 'Sujeto 5 (5A1a)', actor: '5A1a', role: 'Nodo Periférico', color: '#FBBF24' },
        { id: 6, code: '6A1a', name: 'Sujeto 6 (6A1a)', actor: '6A1a', role: 'Nodo Protector', color: '#34D399' },
        { id: 7, code: '7A1a', name: 'Sujeto 7 (7A1a)', actor: '7A1a', role: 'Nodo Volátil', color: '#F87171' },
        { id: 8, code: '8A1a', name: 'Sujeto 8 (8A1a)', actor: '8A1a', role: 'Disidente Racional / Polarizador', color: '#00FF87' },
        { id: 9, code: '9A1a', name: 'Sujeto 9 (9A1a)', actor: '9A1a', role: 'Ancla Cohesiva', color: '#A78BFA' },
        { id: 10, code: '10A1a', name: 'Sujeto 10 (10A1a)', actor: '10A1a', role: 'Polo Tradicional', color: '#F43F5E' },
        { id: 11, code: '11A1a', name: 'Sujeto 11 (11A1a)', actor: '11A1a', role: 'Integrador Cívico', color: '#67E8F9' },
        { id: 12, code: '12A1a', name: 'Sujeto 12 (12A1a)', actor: '12A1a', role: 'Nodo Adaptativo', color: '#CBD5E1' }
    ];

    const WAVES_INFO = [
        { id: 1, key: '1g1t1c', keyCrit2: '1g1t2c', label: 'T1: Estado Inicial', sublabel: 'Configuración asimétrica de bloque inicial', voteCount: '11-1' },
        { id: 2, key: '1g2t1c', keyCrit2: '1g2t2c', label: 'T2: Emergencia de Díada', sublabel: 'Formación del primer núcleo alternativo resonante', voteCount: '10-2' },
        { id: 3, key: '1g3t1c', keyCrit2: '1g3t2c', label: 'T3: Bifurcación Relacional', sublabel: 'Empate técnico y fractura dipolar simétrica', voteCount: '6-6' },
        { id: 4, key: '1g4t1c', keyCrit2: '1g4t2c', label: 'T4: Transición de Fase', sublabel: 'Reconfiguración masiva hacia el atractor central', voteCount: '1-11' },
        { id: 5, key: '1g5t1c', keyCrit2: '1g5t2c', label: 'T5: Atractor Consonante', sublabel: 'Consenso pleno y minimización entrópica', voteCount: '0-12' }
    ];

    const DATASET = {
  "1g1t1c": {
    "coords": [
      [
        1.5,
        1.0,
        -1.2
      ],
      [
        2.0,
        0.2,
        -1.8
      ],
      [
        3.8,
        -2.2,
        2.0
      ],
      [
        2.6,
        2.2,
        0.6
      ],
      [
        2.2,
        -0.8,
        -0.5
      ],
      [
        1.8,
        0.6,
        -1.0
      ],
      [
        3.2,
        -1.5,
        -1.4
      ],
      [
        -4.2,
        1.8,
        2.2
      ],
      [
        1.2,
        0.8,
        0.5
      ],
      [
        4.0,
        -3.0,
        1.2
      ],
      [
        1.9,
        1.2,
        -0.2
      ],
      [
        2.8,
        -0.2,
        -1.6
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 0,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 3,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 9,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 6,
        "type": "E",
        "weight": 1,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 1,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 5,
        "tgt": 3,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 2,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 3,
        "type": "E",
        "weight": 1,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 9,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 11,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 0,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 9,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 3,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 11,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "BBBB",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "C0CC",
        "0000",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "0000",
        "0000",
        "CC0C",
        "C0CC",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "C0CC",
        "AAAA",
        "0000",
        "0000",
        "C0CC",
        "CCCC",
        "0000",
        "0000",
        "0000",
        "C0CC",
        "0000"
      ],
      [
        "0000",
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "BBBB",
        "CCCC",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "BBBB"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "3.80",
    "sdr": "+0.58",
    "f1": "98.2%",
    "grassmann": "d_G = 0.320 rad",
    "regime": "Monopolio de Culpabilidad",
    "synopsis_tc": "1\u00aa Votaci\u00f3n a mano alzada (11 Culpables vs 1 No Culpable). Davis (Jurado 8) vota en solitario invocando la duda razonable frente a la inercia punitiva masiva.",
    "t": 1,
    "c": 1
  },
  "1g1t2c": {
    "coords": [
      [
        1.5,
        1.0,
        -1.2
      ],
      [
        2.0,
        0.2,
        -1.8
      ],
      [
        3.8,
        -2.2,
        2.0
      ],
      [
        2.6,
        2.2,
        0.6
      ],
      [
        2.2,
        -0.8,
        -0.5
      ],
      [
        1.8,
        0.6,
        -1.0
      ],
      [
        3.2,
        -1.5,
        -1.4
      ],
      [
        -4.2,
        1.8,
        2.2
      ],
      [
        1.2,
        0.8,
        0.5
      ],
      [
        4.0,
        -3.0,
        1.2
      ],
      [
        1.9,
        1.2,
        -0.2
      ],
      [
        2.8,
        -0.2,
        -1.6
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 7,
        "type": "R",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 1,
        "tgt": 7,
        "type": "R",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 4,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 9,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 7,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 0,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 9,
        "tgt": 2,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 4,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 9,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 11,
        "tgt": 7,
        "type": "R",
        "weight": 2,
        "mutual": false
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "b0bb",
        "cc0c",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "cc0c",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "BBBB",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "c0cc",
        "c0cc",
        "a0aa",
        "b0bb",
        "0000",
        "0000",
        "a0aa",
        "0000",
        "0000",
        "a0aa",
        "0000",
        "b0bb"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "BBBB",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "3.80",
    "sdr": "-0.45",
    "f1": "98.2%",
    "grassmann": "d_G = 0.320 rad",
    "regime": "Coerci\u00f3n Punitiva Masiva",
    "synopsis_tc": "Furia inmediata del Jurado 3 y del Jurado 10 contra Davis. La prisa por clausurar el caso choca con la exigencia \u00e9tica de deliberar.",
    "t": 1,
    "c": 2
  },
  "1g2t1c": {
    "coords": [
      [
        1.2,
        0.8,
        -1.0
      ],
      [
        1.6,
        0.0,
        -1.5
      ],
      [
        3.6,
        -2.5,
        2.2
      ],
      [
        2.2,
        2.0,
        0.8
      ],
      [
        1.5,
        -0.5,
        -0.6
      ],
      [
        1.4,
        0.4,
        -0.8
      ],
      [
        3.0,
        -1.6,
        -1.2
      ],
      [
        -3.8,
        2.0,
        2.0
      ],
      [
        -3.0,
        1.2,
        1.4
      ],
      [
        3.8,
        -3.2,
        1.0
      ],
      [
        1.5,
        1.0,
        0.0
      ],
      [
        2.5,
        -0.2,
        -1.4
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 9,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 7,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 5,
        "tgt": 7,
        "type": "E",
        "weight": 1,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 2,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 11,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 10,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 8,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 11,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "CC0C",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "C0CC",
        "C0CC",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "BBBB",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "3.95",
    "sdr": "+0.42",
    "f1": "96.8%",
    "grassmann": "d_G = 0.410 rad",
    "regime": "Emergencia de D\u00edada Cr\u00edtica",
    "synopsis_tc": "2\u00aa Votaci\u00f3n secreta (10 a 2). McArdle (Jurado 9) apoya a Davis respetando su coraje moral. Se consolida la primera d\u00edada de duda razonable.",
    "t": 2,
    "c": 1
  },
  "1g2t2c": {
    "coords": [
      [
        1.2,
        0.8,
        -1.0
      ],
      [
        1.6,
        0.0,
        -1.5
      ],
      [
        3.6,
        -2.5,
        2.2
      ],
      [
        2.2,
        2.0,
        0.8
      ],
      [
        1.5,
        -0.5,
        -0.6
      ],
      [
        1.4,
        0.4,
        -0.8
      ],
      [
        3.0,
        -1.6,
        -1.2
      ],
      [
        -3.8,
        2.0,
        2.0
      ],
      [
        -3.0,
        1.2,
        1.4
      ],
      [
        3.8,
        -3.2,
        1.0
      ],
      [
        1.5,
        1.0,
        0.0
      ],
      [
        2.5,
        -0.2,
        -1.4
      ]
    ],
    "edges": [
      {
        "src": 2,
        "tgt": 4,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 8,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 2,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 2,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 7,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 2,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 4,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 9,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "aabb",
        "b0bb",
        "0000",
        "aa0a",
        "bbbb",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "bbaa",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "a0aa",
        "0000",
        "0000",
        "0000",
        "b0bb",
        "0000",
        "AAAA",
        "a0aa",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "bbbb",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "3.95",
    "sdr": "-0.52",
    "f1": "96.8%",
    "grassmann": "d_G = 0.410 rad",
    "regime": "Paranoia y Sospecha Fraterna",
    "synopsis_tc": "El Jurado 3 estalla en ira y acusa con violencia al Jurado 5 de haber cambiado el voto, evidenciando su rencor latente.",
    "t": 2,
    "c": 2
  },
  "1g3t1c": {
    "coords": [
      [
        0.8,
        0.5,
        -1.2
      ],
      [
        -2.0,
        0.2,
        -1.0
      ],
      [
        3.9,
        -2.8,
        2.4
      ],
      [
        2.0,
        2.2,
        0.6
      ],
      [
        -2.5,
        -0.8,
        0.8
      ],
      [
        -1.8,
        0.6,
        -0.6
      ],
      [
        2.8,
        -1.8,
        -1.0
      ],
      [
        -3.6,
        2.2,
        1.8
      ],
      [
        -2.8,
        1.4,
        1.2
      ],
      [
        3.6,
        -3.5,
        0.8
      ],
      [
        -2.2,
        1.2,
        0.5
      ],
      [
        2.2,
        -0.4,
        -1.2
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 8,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 6,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 9,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 4,
        "tgt": 5,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 4,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 11,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 4,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 5,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 10,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 10,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 8,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 11,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "BBBB",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "BB0B",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "B0BB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB"
      ],
      [
        "0000",
        "BBBB",
        "0000",
        "0000",
        "AAAA",
        "BBBB",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "AAAA",
        "0000"
      ],
      [
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "BBBB",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "BBBB",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.25",
    "sdr": "+0.08",
    "f1": "94.5%",
    "grassmann": "d_G = 0.590 rad",
    "regime": "Bipolaridad Equitativa (Cisma)",
    "synopsis_tc": "3\u00aa Votaci\u00f3n (6 a 6). El jurado se parte exactamente a la mitad tras la demostraci\u00f3n de la navaja autom\u00e1tica y el paso del tren.",
    "t": 3,
    "c": 1
  },
  "1g3t2c": {
    "coords": [
      [
        0.8,
        0.5,
        -1.2
      ],
      [
        -2.0,
        0.2,
        -1.0
      ],
      [
        3.9,
        -2.8,
        2.4
      ],
      [
        2.0,
        2.2,
        0.6
      ],
      [
        -2.5,
        -0.8,
        0.8
      ],
      [
        -1.8,
        0.6,
        -0.6
      ],
      [
        2.8,
        -1.8,
        -1.0
      ],
      [
        -3.6,
        2.2,
        1.8
      ],
      [
        -2.8,
        1.4,
        1.2
      ],
      [
        3.6,
        -3.5,
        0.8
      ],
      [
        -2.2,
        1.2,
        0.5
      ],
      [
        2.2,
        -0.4,
        -1.2
      ]
    ],
    "edges": [
      {
        "src": 1,
        "tgt": 6,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 4,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 5,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 8,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 9,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 2,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 1,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 7,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 7,
        "tgt": 2,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 2,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 4,
        "type": "R",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 9,
        "tgt": 10,
        "type": "R",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 9,
        "type": "R",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bbbb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "aaaa",
        "0000",
        "aaaa",
        "bbbb",
        "AAAA",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aaaa",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "aaaa",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "bbbb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bb0b",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "aaaa",
        "0000",
        "0000",
        "0000",
        "b0bb",
        "0000",
        "AAAA",
        "a0aa",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "bbbb",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "0000",
        "aaaa",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000",
        "bbbb",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "bbbb",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.25",
    "sdr": "-0.68",
    "f1": "94.5%",
    "grassmann": "d_G = 0.590 rad",
    "regime": "M\u00e1xima Fricci\u00f3n Geod\u00e9sica",
    "synopsis_tc": "Tensi\u00f3n l\u00edmite: el Jurado 3 pierde el control y grita a Davis '\u00a1Voy a matarlo!', demostrando que sus palabras no son literales.",
    "t": 3,
    "c": 2
  },
  "1g4t1c": {
    "coords": [
      [
        -1.5,
        0.6,
        -0.8
      ],
      [
        -2.4,
        0.5,
        -0.6
      ],
      [
        4.5,
        -3.2,
        2.0
      ],
      [
        -1.8,
        2.0,
        0.8
      ],
      [
        -2.8,
        -0.4,
        0.6
      ],
      [
        -2.2,
        0.8,
        -0.4
      ],
      [
        -1.0,
        -1.2,
        -1.0
      ],
      [
        -3.5,
        2.0,
        1.8
      ],
      [
        -3.0,
        1.5,
        1.0
      ],
      [
        0.5,
        -4.0,
        0.5
      ],
      [
        -2.6,
        1.4,
        0.6
      ],
      [
        -1.2,
        -0.2,
        -0.8
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 0,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 4,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 8,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 4,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 5,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 10,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 11,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 11,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "AAAA",
        "BBBB",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "BBBB",
        "0000",
        "AAAA",
        "AAAA",
        "BBBB",
        "BBBB",
        "0000",
        "AAAA",
        "0000",
        "AAAA",
        "BBBB"
      ],
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.40",
    "sdr": "+0.68",
    "f1": "97.1%",
    "grassmann": "d_G = 0.680 rad",
    "regime": "Hegemon\u00eda de la Raz\u00f3n C\u00edvica",
    "synopsis_tc": "4\u00aa Votaci\u00f3n (1 Culpable vs 11 No Culpables). El an\u00e1lisis de las marcas de gafas convence al racional Jurado 4. Todos se vuelven de espaldas al racismo del Jurado 10.",
    "t": 4,
    "c": 1
  },
  "1g4t2c": {
    "coords": [
      [
        -1.5,
        0.6,
        -0.8
      ],
      [
        -2.4,
        0.5,
        -0.6
      ],
      [
        4.5,
        -3.2,
        2.0
      ],
      [
        -1.8,
        2.0,
        0.8
      ],
      [
        -2.8,
        -0.4,
        0.6
      ],
      [
        -2.2,
        0.8,
        -0.4
      ],
      [
        -1.0,
        -1.2,
        -1.0
      ],
      [
        -3.5,
        2.0,
        1.8
      ],
      [
        -3.0,
        1.5,
        1.0
      ],
      [
        0.5,
        -4.0,
        0.5
      ],
      [
        -2.6,
        1.4,
        0.6
      ],
      [
        -1.2,
        -0.2,
        -0.8
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 1,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 3,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 4,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 7,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 8,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 2,
        "tgt": 10,
        "type": "R",
        "weight": 2,
        "mutual": false
      },
      {
        "src": 3,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 4,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 5,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 6,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 7,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 8,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 10,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      },
      {
        "src": 11,
        "tgt": 9,
        "type": "R",
        "weight": 3,
        "mutual": false
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "aa0a",
        "bb0b",
        "0000",
        "0000",
        "aa0a",
        "bb0b",
        "0000",
        "bb0b",
        "0000"
      ],
      [
        "0000",
        "0000",
        "a0aa",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "a0aa",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "a0aa",
        "a0aa",
        "0000",
        "a0aa",
        "a0aa",
        "a0aa",
        "a0aa",
        "a0aa",
        "a0aa",
        "0000",
        "a0aa",
        "a0aa"
      ],
      [
        "0000",
        "0000",
        "b0bb",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "aa0a",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.40",
    "sdr": "-0.32",
    "f1": "97.1%",
    "grassmann": "d_G = 0.680 rad",
    "regime": "Ostracismo del Prejuicio",
    "synopsis_tc": "El Jurado 3 queda acorralado como atractor residual \u00fanico, resisti\u00e9ndose desesperadamente a admitir el fracaso de su venganza personal.",
    "t": 4,
    "c": 2
  },
  "1g5t1c": {
    "coords": [
      [
        -0.5,
        1.2,
        -0.5
      ],
      [
        -1.2,
        0.8,
        -0.8
      ],
      [
        -0.2,
        -0.5,
        1.2
      ],
      [
        -1.5,
        1.8,
        0.5
      ],
      [
        -1.8,
        -0.2,
        0.4
      ],
      [
        -1.4,
        0.6,
        -0.2
      ],
      [
        -0.8,
        -0.8,
        -0.6
      ],
      [
        -2.2,
        1.8,
        1.2
      ],
      [
        -2.0,
        1.2,
        0.8
      ],
      [
        -0.5,
        -2.0,
        0.0
      ],
      [
        -1.8,
        1.4,
        0.2
      ],
      [
        -0.9,
        -0.2,
        -0.5
      ]
    ],
    "edges": [
      {
        "src": 0,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 0,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 0,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 1,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 3,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 4,
        "type": "E",
        "weight": 1,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 2,
        "tgt": 8,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 2,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 3,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 2,
        "type": "E",
        "weight": 1,
        "mutual": true
      },
      {
        "src": 4,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 5,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 6,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 0,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 1,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 3,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 4,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 5,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 6,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 9,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 10,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 11,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 2,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 9,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      },
      {
        "src": 10,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 11,
        "tgt": 7,
        "type": "E",
        "weight": 2,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "BBBB",
        "CCCC",
        "0000",
        "0000",
        "AAAA",
        "BBBB",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "CCCC",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "AAAA",
        "BBBB",
        "AAAA",
        "AAAA",
        "AAAA",
        "BBBB",
        "BBBB",
        "0000",
        "AAAA",
        "BBBB",
        "AAAA",
        "BBBB"
      ],
      [
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "BBBB",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.55",
    "sdr": "+0.92",
    "f1": "99.4%",
    "grassmann": "d_G = 0.745 rad",
    "regime": "Consenso Estacionario Total",
    "synopsis_tc": "Consenso Un\u00e1nime (12 No Culpables). El Jurado 3 rompe la foto de su hijo, llora y musita 'No culpable'. Davis le alcanza el abrigo con respeto humano.",
    "t": 5,
    "c": 1
  },
  "1g5t2c": {
    "coords": [
      [
        -0.5,
        1.2,
        -0.5
      ],
      [
        -1.2,
        0.8,
        -0.8
      ],
      [
        -0.2,
        -0.5,
        1.2
      ],
      [
        -1.5,
        1.8,
        0.5
      ],
      [
        -1.8,
        -0.2,
        0.4
      ],
      [
        -1.4,
        0.6,
        -0.2
      ],
      [
        -0.8,
        -0.8,
        -0.6
      ],
      [
        -2.2,
        1.8,
        1.2
      ],
      [
        -2.0,
        1.2,
        0.8
      ],
      [
        -0.5,
        -2.0,
        0.0
      ],
      [
        -1.8,
        1.4,
        0.2
      ],
      [
        -0.9,
        -0.2,
        -0.5
      ]
    ],
    "edges": [
      {
        "src": 2,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 2,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 7,
        "tgt": 8,
        "type": "E",
        "weight": 3,
        "mutual": true
      },
      {
        "src": 8,
        "tgt": 7,
        "type": "E",
        "weight": 3,
        "mutual": true
      }
    ],
    "smib_matrix": [
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "AAAA",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ],
      [
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000"
      ]
    ],
    "bdr": "4.55",
    "sdr": "0.00",
    "f1": "99.4%",
    "grassmann": "d_G = 0.745 rad",
    "regime": "Entrop\u00eda Cero / Paz Relacional",
    "synopsis_tc": "Disipaci\u00f3n de la hostilidad. El campo grupal alcanza el estado estacionario arm\u00f3nico y los jurados abandonan la sala bajo la lluvia reconciliadora.",
    "t": 5,
    "c": 2
  }
};

    class Engine {
        constructor() {
            this.jurors = JURORS;
            this.waves = WAVES_INFO;
            this.dataset = DATASET;
        }

        getJurors() {
            return this.jurors;
        }

        getWaves() {
            return this.waves;
        }

        getWaveData(waveKey) {
            return this.dataset[waveKey] || null;
        }

        // =========================================================================
        // 1. INTER-PROXIMIDAD DA/RC Y DISPERSIÓN CUADRANTAL
        // =========================================================================
        computeInterProximity(waveKey = '1g1t1c') {
            const waveData = this.dataset[waveKey];
            if (!waveData || !waveData.smib_matrix) {
                return null;
            }

            const smib = waveData.smib_matrix;
            const N = this.jurors.length;
            const da = new Array(N).fill(0);
            const rc = new Array(N).fill(0);
            let mutualCount = 0;

            for (let i = 0; i < N; i++) {
                for (let j = 0; j < N; j++) {
                    const cell = smib[i][j];
                    if (cell && cell.length >= 3) {
                        const a2 = cell[1]; // DA: emisor i otorga a partner j
                        const a3 = cell[2]; // RECIBE: partner j otorga a emisor i
                        if (a2 >= 'A' && a2 <= 'Z') {
                            da[i]++;
                        }
                        if (a3 >= 'A' && a3 <= 'Z') {
                            rc[i]++;
                        }
                        if (i < j && (a2 >= 'A' && a2 <= 'Z') && (a3 >= 'A' && a3 <= 'Z')) {
                            mutualCount++;
                        }
                    }
                }
            }

            const sumDA = da.reduce((a, b) => a + b, 0);
            const sumRC = rc.reduce((a, b) => a + b, 0);
            const meanDA = sumDA / N;
            const meanRC = sumRC / N;

            // Varianza y covarianza para Pearson r
            let cov = 0, varDA = 0, varRC = 0;
            for (let i = 0; i < N; i++) {
                const diffDA = da[i] - meanDA;
                const diffRC = rc[i] - meanRC;
                cov += diffDA * diffRC;
                varDA += diffDA * diffDA;
                varRC += diffRC * diffRC;
            }
            const denom = Math.sqrt(varDA * varRC);
            const pearsonR = denom > 1e-9 ? cov / denom : 0;

            let totalTension = 0;
            const jurorStats = this.jurors.map((juror, idx) => {
                const dVal = da[idx];
                const rVal = rc[idx];
                const delta = Math.abs(rVal - dVal);
                const netStatus = rVal - dVal;
                totalTension += delta;

                // Diagnóstico cuadrantal respecto a la media o bisectriz
                let quadrant = 'Q3';
                let quadrantLabel = 'Periférico / Retraído';
                let quadrantColor = '#94A3B8';

                if (dVal >= meanDA && rVal >= meanRC) {
                    quadrant = 'Q1';
                    quadrantLabel = 'Atractor / Líder Integrador';
                    quadrantColor = '#00FF87';
                } else if (dVal < meanDA && rVal >= meanRC) {
                    quadrant = 'Q2';
                    quadrantLabel = 'Prestigio / Pasivo';
                    quadrantColor = '#38BDF8';
                } else if (dVal >= meanDA && rVal < meanRC) {
                    quadrant = 'Q4';
                    quadrantLabel = 'Emisor Frustrado';
                    quadrantColor = '#F59E0B';
                }

                return {
                    id: juror.id,
                    code: juror.code,
                    name: juror.name,
                    actor: juror.actor,
                    role: juror.role,
                    color: juror.color,
                    da: dVal,
                    rc: rVal,
                    delta: delta,
                    netStatus: netStatus,
                    quadrant: quadrant,
                    quadrantLabel: quadrantLabel,
                    quadrantColor: quadrantColor
                };
            });

            const reciprocityRatio = (sumDA + sumRC) > 0 ? (2 * mutualCount) / (sumDA + sumRC) : 0;

            return {
                waveKey: waveKey,
                meanDA: parseFloat(meanDA.toFixed(2)),
                meanRC: parseFloat(meanRC.toFixed(2)),
                pearsonR: parseFloat(pearsonR.toFixed(3)),
                totalTension: totalTension,
                reciprocityRatio: parseFloat(reciprocityRatio.toFixed(3)),
                mutualCount: mutualCount,
                jurors: jurorStats
            };
        }

        // =========================================================================
        // 2. ANÁLISIS ESPECTRAL LAPLACIANO, FIEDLER (λ2) Y FRUSTRACIÓN DE HEIDER
        // =========================================================================
        computeSpectral(waveKey = '1g1t1c') {
            const waveData = this.dataset[waveKey];
            if (!waveData || !waveData.smib_matrix) return null;

            const smib = waveData.smib_matrix;
            const N = this.jurors.length;
            const A = Array.from({ length: N }, () => new Array(N).fill(0));
            const Asigned = Array.from({ length: N }, () => new Array(N).fill(0));

            for (let i = 0; i < N; i++) {
                for (let j = 0; j < N; j++) {
                    const cell = smib[i][j];
                    if (cell && cell.length >= 2) {
                        const a2 = cell[1];
                        if (a2 >= 'A' && a2 <= 'Z') {
                            A[i][j] = 1.0;
                            Asigned[i][j] = 1.0;
                        } else if (a2 >= 'a' && a2 <= 'z') {
                            Asigned[i][j] = -1.0;
                        }
                    }
                }
            }

            // Laplaciano Estándar Simetrizado: L = D - A_sym
            const L = Array.from({ length: N }, () => new Array(N).fill(0));
            const deg = new Array(N).fill(0);
            for (let i = 0; i < N; i++) {
                for (let j = 0; j < N; j++) {
                    const w = 0.5 * (A[i][j] + A[j][i]);
                    L[i][j] = -w;
                    deg[i] += w;
                }
                L[i][i] = deg[i];
            }

            // Jacobi Solver para autovalores del Laplaciano
            const laplacianEigen = this.jacobiEigenvalues(L);
            const eigenvalues = laplacianEigen.values.map(v => Math.max(0, parseFloat(v.toFixed(4))));
            eigenvalues.sort((a, b) => a - b);

            const fiedlerLambda2 = eigenvalues.length > 1 ? eigenvalues[1] : 0;
            const maxEigenvalue = eigenvalues[eigenvalues.length - 1];

            // Radio Espectral de Adyacencia mediante Power Iteration
            const Asym = Array.from({ length: N }, (row, i) =>
                Array.from({ length: N }, (col, j) => 0.5 * (A[i][j] + A[j][i]))
            );
            const spectralRadius = this.powerIterationRadius(Asym);

            // Laplaciano Signado de Heider: L_s = D_bar - A_signed_sym
            const Ls = Array.from({ length: N }, () => new Array(N).fill(0));
            const degSign = new Array(N).fill(0);
            for (let i = 0; i < N; i++) {
                for (let j = 0; j < N; j++) {
                    const w = 0.5 * (Asigned[i][j] + Asigned[j][i]);
                    Ls[i][j] = -w;
                    degSign[i] += Math.abs(w);
                }
                Ls[i][i] = degSign[i];
            }
            const heiderEigen = this.jacobiEigenvalues(Ls);
            const sortedHeider = heiderEigen.values.slice().sort((a, b) => a - b);
            const heiderLambda1 = Math.max(0, parseFloat(sortedHeider[0].toFixed(4)));

            return {
                waveKey: waveKey,
                eigenvalues: eigenvalues,
                fiedlerLambda2: parseFloat(fiedlerLambda2.toFixed(4)),
                spectralRadius: parseFloat(spectralRadius.toFixed(3)),
                heiderFrustration: parseFloat(heiderLambda1.toFixed(4)),
                maxEigenvalue: parseFloat(maxEigenvalue.toFixed(4)),
                isBalanced: heiderLambda1 < 0.001
            };
        }

        // =========================================================================
        // 3. TRANSFORMADA RÁPIDA DE FOURIER (FFT / DFT) Y ESPECTRO ARMÓNICO
        // =========================================================================
        computeFFT() {
            // Serie longitudinal de Densidad Relativa (SDR) y Absoluta (BDR) en T1..T5
            const sdrSeries = [0.58, 0.42, 0.08, 0.68, 0.92];
            const bdrSeries = [3.80, 3.95, 4.25, 4.40, 4.55];

            // Interpolación periódica a M=16 muestras para análisis armónico nítido
            const M = 16;
            const interpolatedSDR = new Array(M);
            for (let k = 0; k < M; k++) {
                const pos = (k / (M - 1)) * (sdrSeries.length - 1);
                const idx = Math.floor(pos);
                const frac = pos - idx;
                if (idx >= sdrSeries.length - 1) {
                    interpolatedSDR[k] = sdrSeries[sdrSeries.length - 1];
                } else {
                    interpolatedSDR[k] = sdrSeries[idx] * (1 - frac) + sdrSeries[idx + 1] * frac;
                }
            }

            // Cálculo DFT (Discrete Fourier Transform)
            const numFreqs = Math.floor(M / 2) + 1;
            const freqs = [];
            const amplitudes = [];
            const powerSpectrum = [];

            let totalPower = 0;
            let maxPowerIdx = 1;
            let maxPower = 0;

            for (let k = 0; k < numFreqs; k++) {
                let re = 0;
                let im = 0;
                for (let n = 0; n < M; n++) {
                    const phi = (2 * Math.PI * k * n) / M;
                    re += interpolatedSDR[n] * Math.cos(phi);
                    im -= interpolatedSDR[n] * Math.sin(phi);
                }
                const amp = Math.sqrt(re * re + im * im) / M;
                const pwr = (amp * amp);

                freqs.push(parseFloat((k / M).toFixed(4)));
                amplitudes.push(parseFloat(amp.toFixed(4)));
                powerSpectrum.push(parseFloat(pwr.toFixed(5)));

                if (k > 0) {
                    totalPower += pwr;
                    if (pwr > maxPower) {
                        maxPower = pwr;
                        maxPowerIdx = k;
                    }
                }
            }

            const dominantFreq = freqs[maxPowerIdx];
            const dominantPeriod = dominantFreq > 0 ? parseFloat((1 / dominantFreq).toFixed(2)) : 0;
            const harmonicPurity = totalPower > 0 ? parseFloat(((maxPower / totalPower) * 100).toFixed(1)) : 0;

            return {
                frequencies: freqs,
                amplitudes: amplitudes,
                powerSpectrum: powerSpectrum,
                dominantFreq: dominantFreq,
                dominantPeriod: dominantPeriod,
                harmonicPurity: harmonicPurity,
                sdrSeries: sdrSeries,
                bdrSeries: bdrSeries,
                timeLabels: ['T1 (11-1)', 'T2 (10-2)', 'T3 (6-6)', 'T4 (1-11)', 'T5 (0-12)']
            };
        }

        // =========================================================================
        // 4. CADENAS DE MARKOV Y MASA GRAVITATORIA (PAGERANK SOCIOMÉTRICO)
        // =========================================================================
        computeMarkov(waveKey = '1g1t1c') {
            const waveData = this.dataset[waveKey];
            if (!waveData || !waveData.smib_matrix) return null;

            const smib = waveData.smib_matrix;
            const N = this.jurors.length;
            const A = Array.from({ length: N }, () => new Array(N).fill(0));

            for (let i = 0; i < N; i++) {
                for (let j = 0; j < N; j++) {
                    const cell = smib[i][j];
                    if (cell && cell.length >= 2 && cell[1] >= 'A' && cell[1] <= 'Z') {
                        A[i][j] = 1.0;
                    }
                }
            }

            // Matriz estocástica con regularización ergódica (Damping factor alpha = 0.85)
            const alpha = 0.85;
            const P = Array.from({ length: N }, () => new Array(N).fill(0));

            for (let i = 0; i < N; i++) {
                const rowSum = A[i].reduce((a, b) => a + b, 0);
                for (let j = 0; j < N; j++) {
                    if (rowSum > 0) {
                        P[i][j] = alpha * (A[i][j] / rowSum) + (1.0 - alpha) / N;
                    } else {
                        P[i][j] = 1.0 / N;
                    }
                }
            }

            // Power Iteration para encontrar la distribución estacionaria pi (pi * P = pi)
            let pi = new Array(N).fill(1.0 / N);
            for (let iter = 0; iter < 120; iter++) {
                const nextPi = new Array(N).fill(0);
                for (let j = 0; j < N; j++) {
                    let sum = 0;
                    for (let i = 0; i < N; i++) {
                        sum += pi[i] * P[i][j];
                    }
                    nextPi[j] = sum;
                }
                const norm = nextPi.reduce((a, b) => a + b, 0);
                pi = nextPi.map(v => v / norm);
            }

            const equiprobability = 1.0 / N;
            const rankedJurors = this.jurors.map((juror, idx) => {
                const prob = pi[idx];
                const ratio = prob / equiprobability;
                return {
                    id: juror.id,
                    code: juror.code,
                    name: juror.name,
                    actor: juror.actor,
                    role: juror.role,
                    color: juror.color,
                    pi: parseFloat(prob.toFixed(4)),
                    piPct: parseFloat((prob * 100).toFixed(2)),
                    ratioOverMean: parseFloat(ratio.toFixed(2)),
                    isAboveMean: prob >= equiprobability
                };
            }).sort((a, b) => b.pi - a.pi);

            // Índice de concentración Herfindahl-Hirschman (HHI)
            const hhi = pi.reduce((sum, p) => sum + p * p, 0);

            return {
                waveKey: waveKey,
                equiprobabilityPct: parseFloat((equiprobability * 100).toFixed(2)),
                hhi: parseFloat(hhi.toFixed(4)),
                topAttractor: rankedJurors[0],
                jurors: rankedJurors
            };
        }

        // =========================================================================
        // 5. GEOMETRÍA DE GRASSMANN Gr(3, 12) Y DISTANCIAS GEODÉSICAS
        // =========================================================================
        computeGrassmann() {
            const waveKeys = ['1g1t1c', '1g2t1c', '1g3t1c', '1g4t1c', '1g5t1c'];
            const K = waveKeys.length;
            const N = 12;
            const D = 3;

            // Bases ortonormales Q_k (12 x 3) mediante Gram-Schmidt
            const bases = [];
            for (let wIdx = 0; wIdx < K; wIdx++) {
                const tc = this.dataset[waveKeys[wIdx]];
                const coords = tc.coords; // 12 x 3
                const Q = this.gramSchmidtOrtho(coords, N, D);
                bases.push(Q);
            }

            const distMatrix = Array.from({ length: K }, () => new Array(K).fill(0));
            const chordalMatrix = Array.from({ length: K }, () => new Array(K).fill(0));
            const principalAnglesAll = [];

            for (let i = 0; i < K; i++) {
                for (let j = 0; j < K; j++) {
                    if (i === j) {
                        distMatrix[i][j] = 0;
                        chordalMatrix[i][j] = 0;
                        continue;
                    }
                    // M = Q_i^T * Q_j (3 x 3)
                    const M = Array.from({ length: D }, () => new Array(D).fill(0));
                    for (let r = 0; r < D; r++) {
                        for (let c = 0; c < D; c++) {
                            let dot = 0;
                            for (let n = 0; n < N; n++) {
                                dot += bases[i][n][r] * bases[j][n][c];
                            }
                            M[r][c] = dot;
                        }
                    }

                    // SVD de M (3x3)
                    const singVals = this.svd3x3(M);
                    let sumThetaSq = 0;
                    let sumSinThetaSq = 0;
                    const angles = [];

                    for (let m = 0; m < D; m++) {
                        const s = Math.max(0, Math.min(1.0, singVals[m]));
                        const theta = Math.acos(s);
                        angles.push(theta);
                        sumThetaSq += theta * theta;
                        sumSinThetaSq += Math.sin(theta) * Math.sin(theta);
                    }

                    const dG = Math.sqrt(sumThetaSq);
                    const dC = Math.sqrt(sumSinThetaSq);
                    distMatrix[i][j] = parseFloat(dG.toFixed(4));
                    chordalMatrix[i][j] = parseFloat(dC.toFixed(4));

                    if (j === i + 1) {
                        principalAnglesAll.push({
                            step: ,
                            from: WAVES_INFO[i].label,
                            to: WAVES_INFO[j].label,
                            anglesRad: angles.map(a => parseFloat(a.toFixed(4))),
                            anglesDeg: angles.map(a => parseFloat((a * 180 / Math.PI).toFixed(2))),
                            dG: parseFloat(dG.toFixed(4)),
                            dC: parseFloat(dC.toFixed(4))
                        });
                    }
                }
            }

            // Deformación acumulada desde T1
            const cumulativeDistances = [0];
            for (let k = 1; k < K; k++) {
                cumulativeDistances.push(distMatrix[0][k]);
            }

            return {
                waveLabels: ['T1 (11-1)', 'T2 (10-2)', 'T3 (6-6)', 'T4 (1-11)', 'T5 (0-12)'],
                distMatrix: distMatrix,
                chordalMatrix: chordalMatrix,
                stepProgression: principalAnglesAll,
                cumulativeDistances: cumulativeDistances,
                totalDistanceT1T5: distMatrix[0][K - 1]
            };
        }

        // =========================================================================
        // MÉTODOS MATEMÁTICOS DE APOYO (ALGEBRA LINEAL PURA)
        // =========================================================================
        jacobiEigenvalues(A_in, maxIter = 100, eps = 1e-10) {
            const n = A_in.length;
            const A = A_in.map(row => row.slice());
            const V = Array.from({ length: n }, (_, i) =>
                Array.from({ length: n }, (_, j) => (i === j ? 1.0 : 0.0))
            );

            for (let iter = 0; iter < maxIter; iter++) {
                let maxVal = 0;
                let p = 0, q = 1;

                for (let i = 0; i < n; i++) {
                    for (let j = i + 1; j < n; j++) {
                        const absVal = Math.abs(A[i][j]);
                        if (absVal > maxVal) {
                            maxVal = absVal;
                            p = i;
                            q = j;
                        }
                    }
                }

                if (maxVal < eps) break;

                const app = A[p][p];
                const aqq = A[q][q];
                const apq = A[p][q];

                const theta = 0.5 * Math.atan2(2 * apq, aqq - app);
                const c = Math.cos(theta);
                const s = Math.sin(theta);

                for (let i = 0; i < n; i++) {
                    if (i !== p && i !== q) {
                        const aip = A[i][p];
                        const aiq = A[i][q];
                        A[i][p] = c * aip - s * aiq;
                        A[p][i] = A[i][p];
                        A[i][q] = s * aip + c * aiq;
                        A[q][i] = A[i][q];
                    }
                    const vip = V[i][p];
                    const viq = V[i][q];
                    V[i][p] = c * vip - s * viq;
                    V[i][q] = s * vip + c * viq;
                }

                A[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq;
                A[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq;
                A[p][q] = 0;
                A[q][p] = 0;
            }

            const values = [];
            for (let i = 0; i < n; i++) values.push(A[i][i]);
            return { values, vectors: V };
        }

        powerIterationRadius(A, maxIter = 50) {
            const n = A.length;
            let v = new Array(n).fill(1.0 / Math.sqrt(n));

            for (let iter = 0; iter < maxIter; iter++) {
                const nextV = new Array(n).fill(0);
                for (let i = 0; i < n; i++) {
                    for (let j = 0; j < n; j++) {
                        nextV[i] += A[i][j] * v[j];
                    }
                }
                const norm = Math.sqrt(nextV.reduce((acc, val) => acc + val * val, 0));
                if (norm < 1e-12) return 0;
                v = nextV.map(x => x / norm);
            }

            let rayleigh = 0;
            for (let i = 0; i < n; i++) {
                let rowSum = 0;
                for (let j = 0; j < n; j++) rowSum += A[i][j] * v[j];
                rayleigh += v[i] * rowSum;
            }
            return Math.abs(rayleigh);
        }

        gramSchmidtOrtho(matrix, rows, cols) {
            const Q = Array.from({ length: rows }, () => new Array(cols).fill(0));
            for (let j = 0; j < cols; j++) {
                const v = new Array(rows);
                for (let i = 0; i < rows; i++) v[i] = matrix[i][j];

                for (let k = 0; k < j; k++) {
                    let dot = 0;
                    for (let i = 0; i < rows; i++) dot += matrix[i][j] * Q[i][k];
                    for (let i = 0; i < rows; i++) v[i] -= dot * Q[i][k];
                }

                let norm = 0;
                for (let i = 0; i < rows; i++) norm += v[i] * v[i];
                norm = Math.sqrt(norm);

                for (let i = 0; i < rows; i++) {
                    Q[i][j] = norm > 1e-9 ? v[i] / norm : 0;
                }
            }
            return Q;
        }

        svd3x3(M) {
            // M^T * M es una matriz simétrica 3x3
            const MTM = Array.from({ length: 3 }, () => new Array(3).fill(0));
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    let sum = 0;
                    for (let k = 0; k < 3; k++) sum += M[k][i] * M[k][j];
                    MTM[i][j] = sum;
                }
            }
            const eigen = this.jacobiEigenvalues(MTM);
            const singularValues = eigen.values.map(val => Math.sqrt(Math.max(0, val)));
            singularValues.sort((a, b) => b - a);
            return singularValues;
        }
    }

    return Engine;
}));
