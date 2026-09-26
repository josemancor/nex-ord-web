#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_visord_procesual.py
Generador Maestro del VISORD PROCESUAL: Observador Universal de Textos y Diálogos
Ecosistema VISORD / NEXORD.
"""
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>VISORD PROCESUAL · Observador Universal de Textos y Diálogos · NEXORD</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700;800&family=Roboto+Mono:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-dark: #070B18;
      --bg-navy: #0B132B;
      --bg-card: rgba(14, 25, 52, 0.78);
      --border-blue: rgba(56, 189, 248, 0.35);
      --border-gold: rgba(233, 185, 19, 0.45);
      --neon-cyan: #38BDF8;
      --neon-green: #00FF87;
      --neon-gold: #FFE600;
      --neon-orange: #FF9F1C;
      --neon-magenta: #FF007F;
      --neon-red: #FF3366;
      --font-cinzel: 'Cinzel', serif;
      --font-outfit: 'Outfit', sans-serif;
      --font-mono: 'Roboto Mono', 'JetBrains Mono', monospace;
      --font-sans: 'Inter', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: #050814;
      color: #E2E8F0;
      font-family: var(--font-sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 18% 18%, rgba(56, 189, 248, 0.07) 0%, transparent 45%),
        radial-gradient(circle at 82% 78%, rgba(0, 255, 135, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(11, 19, 43, 0.4) 0%, transparent 70%);
      background-attachment: fixed;
    }

    /* CABECERA INSTITUCIONAL */
    .app-header {
      background: rgba(7, 12, 28, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1.5px solid var(--border-blue);
      padding: 5px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 1000;
      gap: 12px;
      flex-wrap: wrap;
    }
    .brand-section {
      display: flex;
      align-items: center;
      gap: 9px;
      text-decoration: none;
    }
    .brand-logo {
      height: 28px;
      width: auto;
      filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.5));
    }
    .brand-title {
      font-family: var(--font-cinzel);
      font-size: 13.5px;
      font-weight: 800;
      letter-spacing: 1.2px;
      color: #FFF;
      display: flex;
      align-items: center;
      gap: 7px;
    }
    .brand-badge {
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      background: rgba(0, 255, 135, 0.15);
      border: 1px solid var(--neon-green);
      color: var(--neon-green);
      padding: 1.5px 6px;
      border-radius: 4px;
      letter-spacing: 0.8px;
      box-shadow: 0 0 8px rgba(0, 255, 135, 0.25);
    }
    .brand-sub {
      font-family: var(--font-sans);
      font-size: 10px;
      color: #94A3B8;
      font-weight: 400;
    }

    /* SELECTOR DE ESCENARIO / CORPUS TEXTUAL */
    .corpus-selector-group {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(14, 25, 52, 0.85);
      border: 1.5px solid rgba(56, 189, 248, 0.45);
      border-radius: 6px;
      padding: 2.5px 8px;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.15);
    }
    .corpus-lbl {
      font-family: var(--font-mono);
      font-size: 8px;
      font-weight: 900;
      color: var(--neon-cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .corpus-select {
      background: rgba(6, 11, 26, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #F8FAFC;
      font-family: var(--font-sans);
      font-size: 10px;
      font-weight: 700;
      padding: 3px 6px;
      border-radius: 4px;
      outline: none;
      cursor: pointer;
      max-width: 250px;
      transition: all 0.2s ease;
    }
    .corpus-select:focus, .corpus-select:hover {
      border-color: var(--neon-green);
      box-shadow: 0 0 8px rgba(0, 255, 135, 0.3);
    }
    .corpus-select option {
      background: #081126;
      color: #F8FAFC;
      font-family: var(--font-sans);
      font-size: 10px;
      padding: 4px;
    }
    .corpus-ingest-btn {
      background: rgba(0, 255, 135, 0.18);
      border: 1.2px solid var(--neon-green);
      color: var(--neon-green);
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      padding: 3.5px 8px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      letter-spacing: 0.5px;
      transition: all 0.2s ease;
    }
    .corpus-ingest-btn:hover {
      background: rgba(0, 255, 135, 0.35);
      box-shadow: 0 0 12px rgba(0, 255, 135, 0.5);
      color: #FFF;
      transform: translateY(-1px);
    }

    .header-center-ctrl {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* MODOS DE DISPOSICIÓN */
    .mode-toggle-group {
      display: inline-flex;
      background: rgba(14, 25, 52, 0.85);
      border: 1px solid var(--border-blue);
      border-radius: 6px;
      padding: 2px;
      gap: 2px;
    }
    .mode-btn {
      background: transparent;
      border: none;
      color: #94A3B8;
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      padding: 3.5px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 4px;
      letter-spacing: 0.4px;
    }
    .mode-btn:hover {
      color: #FFF;
      background: rgba(255, 255, 255, 0.08);
    }
    .mode-btn.active {
      background: rgba(0, 255, 135, 0.25);
      color: var(--neon-green);
      border: 1px solid rgba(0, 255, 135, 0.6);
      box-shadow: 0 0 8px rgba(0, 255, 135, 0.35);
    }

    /* BOTÓN PARA ABRIR CONTABILIDAD EN SEGUNDO PLANO */
    .btn-toggle-bg-tables {
      background: rgba(56, 189, 248, 0.18);
      border: 1.2px solid rgba(56, 189, 248, 0.6);
      color: var(--neon-cyan);
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      padding: 3.5px 9px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
    }
    .btn-toggle-bg-tables:hover {
      background: rgba(56, 189, 248, 0.35);
      color: #FFF;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }
    .btn-toggle-bg-tables.active {
      background: rgba(0, 255, 135, 0.25);
      border-color: var(--neon-green);
      color: var(--neon-green);
    }

    /* SELECTOR N RÁPIDO */
    .n-selector-group {
      display: inline-flex;
      background: rgba(14, 25, 52, 0.85);
      border: 1px solid var(--border-blue);
      border-radius: 6px;
      padding: 2px;
      gap: 2px;
    }
    .n-btn {
      background: transparent;
      border: none;
      color: #94A3B8;
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      padding: 3px 7px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .n-btn:hover {
      color: #FFF;
      background: rgba(255, 255, 255, 0.08);
    }
    .n-btn.active {
      background: rgba(0, 255, 135, 0.22);
      color: var(--neon-green);
      border: 1px solid rgba(0, 255, 135, 0.5);
    }

    .header-autoplay-pill {
      background: rgba(15, 23, 42, 0.95);
      border: 1.2px solid rgba(0, 255, 135, 0.4);
      color: var(--neon-green);
      font-family: var(--font-mono);
      font-size: 8.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .header-autoplay-pill:hover {
      border-color: var(--neon-green);
      box-shadow: 0 0 10px rgba(0, 255, 135, 0.4);
    }
    .auto-pulse-indicator {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--neon-green);
      box-shadow: 0 0 7px var(--neon-green);
      animation: pulseGreen 1.4s infinite ease-in-out;
    }
    @keyframes pulseGreen {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.4); opacity: 0.5; }
    }

    .header-nav {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .hdr-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #CBD5E1;
      font-size: 9.5px;
      font-weight: 600;
      padding: 3.5px 9px;
      border-radius: 4px;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .hdr-btn:hover {
      background: rgba(56, 189, 248, 0.25);
      border-color: var(--neon-cyan);
      color: #FFF;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.4);
    }

    /* LÍNEA SUPERIOR DE TELEPROMPTER */
    .teleprompter-line {
      background: rgba(5, 9, 22, 0.95);
      border-bottom: 1px solid rgba(56, 189, 248, 0.25);
      padding: 4px 14px;
      font-family: var(--font-mono);
      font-size: 9px;
      display: flex;
      align-items: center;
      gap: 10px;
      overflow-x: auto;
      white-space: nowrap;
      position: sticky;
      top: 42px;
      z-index: 990;
    }
    .tele-inner {
      display: flex;
      align-items: center;
      gap: 7px;
      width: 100%;
    }
    .tele-ctrl-group {
      display: flex;
      align-items: center;
      gap: 3px;
    }
    .tele-btn-action {
      background: rgba(0, 255, 135, 0.2);
      border: 1px solid var(--neon-green);
      color: #FFF;
      font-family: var(--font-mono);
      font-size: 8px;
      font-weight: 800;
      padding: 2.5px 7px;
      border-radius: 3px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
    }
    .tele-btn-action:hover {
      background: rgba(0, 255, 135, 0.35);
      box-shadow: 0 0 8px rgba(0, 255, 135, 0.5);
    }
    .tele-btn-sub {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #E2E8F0;
      font-family: var(--font-mono);
      font-size: 8px;
      padding: 2.5px 6px;
      border-radius: 3px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .tele-btn-sub:hover {
      background: rgba(56, 189, 248, 0.25);
      border-color: var(--neon-cyan);
    }
    .tele-btn-sub.active {
      background: rgba(0, 255, 135, 0.25);
      border-color: var(--neon-green);
      color: var(--neon-green);
    }
    .tele-turn {
      font-weight: 800;
      color: var(--neon-cyan);
    }
    .tele-actor {
      font-weight: 800;
      padding: 1px 5px;
      border-radius: 3px;
    }
    .tele-actor.emit {
      background: rgba(0, 255, 135, 0.2);
      color: var(--neon-green);
      border: 1px solid var(--neon-green);
    }
    .tele-actor.rec {
      background: rgba(56, 189, 248, 0.2);
      color: var(--neon-cyan);
      border: 1px solid var(--neon-cyan);
    }
    
    /* BADGES DINÁMICOS DE ROL EN TELEPROMPTER */
    .tele-role-badge {
      font-size: 7.5px;
      font-weight: 800;
      padding: 1.5px 5px;
      border-radius: 3px;
      letter-spacing: 0.3px;
      text-transform: uppercase;
      transition: all 0.2s ease;
      white-space: nowrap;
      display: inline-block;
    }
    .tele-role-badge.inic {
      background: rgba(0, 255, 135, 0.15);
      color: #00FF87;
      border: 1px solid rgba(0, 255, 135, 0.4);
    }
    .tele-role-badge.resp {
      background: rgba(56, 189, 248, 0.15);
      color: #38BDF8;
      border: 1px solid rgba(56, 189, 248, 0.4);
    }
    .tele-role-badge.prov {
      background: rgba(255, 159, 28, 0.15);
      color: #FF9F1C;
      border: 1px solid rgba(255, 159, 28, 0.4);
    }
    .tele-role-badge.repl {
      background: rgba(168, 85, 247, 0.15);
      color: #A855F7;
      border: 1px solid rgba(168, 85, 247, 0.4);
    }
    .tele-role-badge.pause {
      background: rgba(255, 230, 0, 0.15);
      color: #FFE600;
      border: 1px solid rgba(255, 230, 0, 0.4);
    }

    .tele-actor.center-hub {
      background: rgba(245, 205, 83, 0.2);
      color: #FCD34D;
      border: 1px solid #FCD34D;
    }
    .tele-q81 {
      font-weight: 900;
      padding: 1px 5px;
      border-radius: 3px;
    }
    .tele-text {
      color: #F1F5F9;
      font-family: var(--font-sans);
      font-size: 10px;
      font-style: italic;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 600px;
    }
    .tele-dot {
      color: #475569;
    }

    /* CONTENEDOR PRINCIPAL */
    .stage-container {
      flex: 1;
      padding: 8px 14px 40px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-width: 1920px;
      margin: 0 auto;
      width: 100%;
    }

    /* GRID DEL ESCENARIO */
    .stage-grid {
      display: grid;
      gap: 8px;
      transition: all 0.3s ease;
      min-height: 600px;
      flex: 1;
    }

    /* MODO FOCO RUEDO (TABLAS EN 2º PLANO): EL RUEDO A LO GRANDE */
    .stage-grid.mode-ruedo-focus {
      grid-template-columns: 1fr;
    }
    .stage-grid.mode-ruedo-focus .stage-wing-left,
    .stage-grid.mode-ruedo-focus .stage-wing-right,
    .stage-grid.mode-ruedo-focus .stage-live-table-panel {
      display: none;
    }
    .stage-grid.mode-ruedo-focus .stage-center-arena {
      min-height: 680px;
      height: calc(100vh - 160px);
    }

    /* MODO SPLIT: Ruedo a un lado + Gran Tabla al otro */
    .stage-grid.mode-split {
      grid-template-columns: 1fr 1fr;
    }
    .stage-grid.mode-split .stage-wing-left,
    .stage-grid.mode-split .stage-wing-right {
      display: none;
    }
    .stage-grid.mode-split .stage-center-arena {
      min-height: 580px;
    }

    /* MODO TABLAS EN 1º PLANO */
    .stage-grid.mode-tables-focus {
      grid-template-columns: 1fr;
    }
    .stage-grid.mode-tables-focus .stage-center-arena,
    .stage-grid.mode-tables-focus .stage-wing-left,
    .stage-grid.mode-tables-focus .stage-wing-right {
      display: none;
    }

    /* MODO RUEDO CON BURLADEROS */
    .stage-grid.mode-ruedo {
      grid-template-columns: 480px 1fr 480px;
    }
    .stage-grid.mode-ruedo .stage-live-table-panel {
      display: none;
    }

    /* MODO MATRICIAL 3X3 */
    .stage-grid.mode-matrix {
      grid-template-columns: 320px 1fr 320px;
    }
    .stage-grid.mode-matrix .stage-live-table-panel {
      display: none;
    }

    /* ESCENARIO CENTRAL: EL RUEDO RELACIONAL (ARENA DE ANFITEATRO) */
    .stage-center-arena {
      background: radial-gradient(circle at 50% 50%, #0C1530 0%, #070C1E 70%, #040816 100%);
      border: 1.5px solid var(--border-blue);
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.9), 0 0 25px rgba(56, 189, 248, 0.12);
    }
    .cuad-vector-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 10;
    }
    .center-matrix-grid {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: grid;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }
    .stage-grid.mode-matrix .center-matrix-grid {
      opacity: 1;
      pointer-events: auto;
    }
    .cell-diagonal-subject {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .presence-point {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      box-shadow: 0 0 8px currentColor;
      transition: transform 0.2s ease;
    }
    .presence-point.active-actor {
      transform: scale(2.2);
      box-shadow: 0 0 18px currentColor;
    }
    .cell-center-interaction {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    /* =========================================================================
       CAJÓN DESPLEGABLE DE CONTABILIDAD EN SEGUNDO PLANO (TELEMETRY DRAWER)
       ========================================================================= */
    .telemetry-drawer {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100vw;
      background: rgba(6, 12, 28, 0.96);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-top: 1.5px solid var(--neon-cyan);
      box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.85);
      z-index: 99990;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      transform: translateY(calc(100% - 32px));
      display: flex;
      flex-direction: column;
      max-height: 80vh;
    }
    .telemetry-drawer.open {
      transform: translateY(0);
    }
    .drawer-tab-handle {
      height: 32px;
      background: rgba(14, 25, 52, 0.98);
      border-bottom: 1px solid rgba(56, 189, 248, 0.25);
      padding: 0 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
      font-family: var(--font-mono);
      font-size: 8.5px;
      transition: background 0.2s ease;
    }
    .drawer-tab-handle:hover {
      background: rgba(20, 35, 75, 0.98);
    }
    .drawer-tab-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .drawer-pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--neon-green);
      box-shadow: 0 0 8px var(--neon-green);
      animation: pulseGreen 1.5s infinite ease-in-out;
    }
    .drawer-title {
      font-weight: 900;
      color: var(--neon-cyan);
      letter-spacing: 0.5px;
    }
    .drawer-stat {
      color: #94A3B8;
      font-size: 8px;
    }
    .drawer-stat b {
      color: #FFF;
      font-family: var(--font-outfit);
      font-size: 10px;
    }
    .drawer-toggle-arrow {
      font-weight: 800;
      color: var(--neon-green);
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 12px 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    /* GRAN TABLA SIMULTÁNEA DE RESULTADOS EN DIRECTO */
    .stage-live-table-panel {
      background: rgba(9, 16, 38, 0.92);
      border: 1.5px solid var(--border-blue);
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding: 8px 10px;
      overflow: hidden;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
      min-height: 480px;
    }
    .live-macro-telemetry {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      flex: 0 0 auto;
    }
    .macro-card {
      background: rgba(14, 25, 52, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 5px;
      padding: 5px 8px;
      display: flex;
      flex-direction: column;
      gap: 1.5px;
      font-family: var(--font-mono);
    }
    .macro-lbl {
      font-size: 7px;
      font-weight: 800;
      color: #94A3B8;
      letter-spacing: 0.4px;
      text-transform: uppercase;
    }
    .macro-val {
      font-family: var(--font-outfit);
      font-size: 13.5px;
      font-weight: 900;
      color: #FFF;
    }
    .macro-sub {
      font-size: 6.5px;
      color: #64748B;
      font-weight: 600;
    }
    .live-split-view {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 6px;
      overflow-y: auto;
      padding-right: 2px;
    }
    .mini-matrix-box {
      background: rgba(7, 13, 30, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 5px;
      padding: 5px 8px;
      flex: 0 0 auto;
    }
    .mini-box-hdr {
      font-family: var(--font-mono);
      font-size: 7.5px;
      font-weight: 900;
      color: var(--neon-cyan);
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .live-matrix-container {
      display: grid;
      gap: 2px;
    }
    .live-mat-cell {
      background: rgba(14, 25, 52, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 2px;
      height: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 7.5px;
      font-weight: 800;
      color: #94A3B8;
      transition: all 0.2s ease;
    }
    .live-mat-cell.hdr {
      background: rgba(56, 189, 248, 0.15);
      color: #38BDF8;
      border-color: rgba(56, 189, 248, 0.3);
    }
    .live-mat-cell.diag {
      background: rgba(255, 255, 255, 0.04);
      color: #475569;
    }
    .live-mat-cell.active-pulse {
      background: rgba(0, 255, 135, 0.35) !important;
      border-color: #00FF87 !important;
      color: #FFF !important;
      box-shadow: 0 0 8px rgba(0, 255, 135, 0.6);
      transform: scale(1.05);
    }
    .live-table-container {
      flex: 1;
      background: rgba(7, 13, 30, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 5px;
      overflow-x: auto;
      padding: 4px;
    }
    .live-data-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0 2px;
      font-family: var(--font-mono);
      font-size: 8px;
    }
    .live-data-table thead th {
      background: rgba(16, 28, 58, 0.95);
      color: #94A3B8;
      font-size: 6.5px;
      font-weight: 800;
      letter-spacing: 0.3px;
      padding: 3px 5px;
      text-align: center;
      border-bottom: 1px solid rgba(56, 189, 248, 0.3);
      white-space: nowrap;
    }
    .live-data-table tr.super-th-row th {
      font-size: 7px;
      font-weight: 900;
      letter-spacing: 0.4px;
      text-transform: uppercase;
      padding: 3px 4px;
      border-bottom: 1.5px solid rgba(255, 255, 255, 0.15);
    }
    .th-group-subj {
      background: rgba(16, 28, 58, 0.95) !important;
      color: #CBD5E1 !important;
    }
    .th-group-dador {
      background: rgba(245, 205, 83, 0.22) !important;
      color: #FCD34D !important;
      border-left: 1px solid rgba(245, 205, 83, 0.4);
      border-right: 1px solid rgba(245, 205, 83, 0.4);
    }
    .th-group-rec {
      background: rgba(56, 189, 248, 0.20) !important;
      color: #38BDF8 !important;
      border-right: 1px solid rgba(56, 189, 248, 0.4);
    }
    .th-group-bal {
      background: rgba(0, 255, 135, 0.15) !important;
      color: #00FF87 !important;
    }
    .live-data-table th.col-dador, .live-data-table td.col-dador {
      background: rgba(245, 205, 83, 0.05);
    }
    .live-data-table th.col-rec, .live-data-table td.col-rec {
      background: rgba(56, 189, 248, 0.05);
    }
    .live-data-table th.col-bal, .live-data-table td.col-bal {
      background: rgba(0, 255, 135, 0.04);
    }
    .live-data-table td {
      background: rgba(11, 20, 44, 0.75);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding: 3px 5px;
      text-align: center;
      color: #E2E8F0;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .live-data-table tr.active-row-emit td {
      border-color: #00FF87 !important;
      background: rgba(0, 255, 135, 0.14) !important;
    }
    .live-data-table tr.active-row-rec td {
      border-color: #38BDF8 !important;
      background: rgba(56, 189, 248, 0.14) !important;
    }
    .live-data-table tr.defector-row td {
      border-color: #FF007F !important;
      background: rgba(255, 0, 127, 0.16) !important;
      color: #FFF !important;
    }
    .badge-bando-a {
      background: rgba(0, 255, 135, 0.15);
      border: 1px solid rgba(0, 255, 135, 0.4);
      color: #00FF87;
      font-size: 7px;
      font-weight: 800;
      padding: 1px 4px;
      border-radius: 3px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }
    .badge-bando-b {
      background: rgba(245, 205, 83, 0.18);
      border: 1px solid rgba(245, 205, 83, 0.45);
      color: #FCD34D;
      font-size: 7px;
      font-weight: 800;
      padding: 1px 4px;
      border-radius: 3px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }
    .live-thermo-bar {
      flex: 0 0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 5px;
      background: rgba(7, 13, 30, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 6px;
      padding: 4px 6px;
    }
    .thermo-item {
      display: flex;
      flex-direction: column;
      gap: 1px;
      font-family: var(--font-mono);
      font-size: 7.5px;
    }
    .thermo-lbl {
      font-size: 6.5px;
      color: #94A3B8;
      font-weight: 700;
    }
    .thermo-val {
      font-family: var(--font-outfit);
      font-size: 10px;
      font-weight: 900;
      color: #FFFFFF;
    }

    /* BURLADEROS PARA MODOS CLÁSICOS */
    .stage-wing-left, .stage-wing-right {
      background: rgba(233, 185, 19, 0.04);
      border: 1.5px solid rgba(233, 185, 19, 0.45);
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      padding: 5px 6px;
      box-sizing: border-box;
      box-shadow: 0 0 14px rgba(233, 185, 19, 0.1);
    }
    .wing-title-bar {
      background: rgba(233, 185, 19, 0.16);
      border: 1px solid rgba(233, 185, 19, 0.4);
      border-radius: 3px;
      padding: 3px 6px;
      font-family: var(--font-mono);
      font-size: 7.5px;
      font-weight: 900;
      color: #FFE600;
      display: flex;
      align-items: center;
      justify-content: space-between;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .wing-header-row {
      display: grid;
      grid-template-columns: 80px 32px 34px 34px 34px 34px 44px 50px 52px 64px;
      gap: 2px;
      padding: 2px 2px;
      background: rgba(14, 25, 52, 0.7);
      border-radius: 3px;
      font-family: var(--font-mono);
      font-size: 6.5px;
      font-weight: 800;
      color: #94A3B8;
      text-align: center;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }
    .wing-body {
      flex: 1;
      display: grid;
      gap: 4px;
    }
    .wing-row-left, .wing-row-right {
      background: rgba(14, 25, 52, 0.85);
      border: 1px solid rgba(233, 185, 19, 0.3);
      border-radius: 4px;
      display: grid;
      grid-template-columns: 80px 32px 34px 34px 34px 34px 44px 50px 52px 64px;
      gap: 2px;
      align-items: center;
      padding: 2px 3px;
      transition: all 0.2s ease;
      font-family: var(--font-mono);
      font-size: 8.5px;
    }
    .wing-row-left.active-dan, .wing-row-right.active-dan {
      background: rgba(0, 255, 135, 0.16) !important;
      border-color: #00FF87 !important;
      box-shadow: 0 0 10px rgba(0, 255, 135, 0.4);
    }
    .wing-row-left.active-rec, .wing-row-right.active-rec {
      background: rgba(56, 189, 248, 0.16) !important;
      border-color: #38BDF8 !important;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }
    .wing-cell {
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .wcell-id {
      justify-content: flex-start;
      gap: 4px;
      font-weight: 800;
    }
    .subj-circle-badge {
      width: 17px;
      height: 17px;
      border-radius: 50%;
      border: 1.5px solid #38BDF8;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 8px;
    }
    .subj-name-tag {
      font-size: 8.5px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .wcell-rt {
      color: #FCD34D;
      font-weight: 700;
      font-size: 7.5px;
    }
    .wcell-saldo {
      font-weight: 800;
      color: #94A3B8;
      font-size: 8px;
    }
    .wcell-fichas {
      color: #00FF87;
      font-weight: 800;
      font-size: 8px;
    }
    .badge-status {
      font-size: 6.5px;
      font-weight: 800;
      padding: 1.5px 3.5px;
      border-radius: 3px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }
    .status-coop { background: rgba(0, 255, 135, 0.18); border: 1px solid #00FF87; color: #00FF87; }
    .status-defector { background: rgba(255, 0, 127, 0.22); border: 1px solid #FF007F; color: #FF007F; }
    .status-warning { background: rgba(245, 205, 83, 0.2); border: 1px solid #FCD34D; color: #FCD34D; }
    .status-leader { background: rgba(56, 189, 248, 0.2); border: 1px solid #38BDF8; color: #38BDF8; }
    .status-eq { background: rgba(148, 163, 184, 0.18); border: 1px solid #94A3B8; color: #CBD5E1; }

    /* NOTA EXPLICATIVA PEDAGÓGICA (REGLA 10) */
    .visord-pedagogical-note {
      background: rgba(11, 19, 43, 0.88);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-left: 4px solid var(--neon-cyan);
      border-radius: 6px;
      padding: 10px 14px;
      margin-top: 6px;
      font-size: 9.5px;
      line-height: 1.55;
      color: #CBD5E1;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
    }
    .note-title {
      font-family: var(--font-mono);
      font-weight: 900;
      font-size: 10.5px;
      color: var(--neon-cyan);
      margin-bottom: 5px;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .note-body strong {
      color: #FFF;
    }
    .note-body code {
      font-family: var(--font-mono);
      color: var(--neon-green);
      background: rgba(0, 255, 135, 0.12);
      padding: 1px 4px;
      border-radius: 3px;
    }

    /* MANDO UNIVERSAL FLOTANTE (REGLA 15) */
    .universal-nav-pod {
      position: fixed;
      right: 18px;
      bottom: 42px;
      z-index: 99998;
      display: flex;
      flex-direction: column;
      gap: 7px;
      align-items: center;
      background: rgba(6, 10, 22, 0.75);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      padding: 8px 5px;
      border-radius: 18px;
      border: 1px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
    }
    .nav-pod-btn {
      width: 34px;
      height: 34px;
      background: rgba(16, 25, 53, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      color: #38BDF8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .nav-pod-btn:hover {
      background: rgba(56, 189, 248, 0.35);
      border-color: #38BDF8;
      color: #FFF;
      transform: scale(1.08);
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
    }

    /* MODAL DE INGESTIÓN */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(3, 7, 18, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 100000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .modal-backdrop.open {
      display: flex;
      animation: fadeInModal 0.25s ease-out;
    }
    @keyframes fadeInModal {
      from { opacity: 0; transform: scale(0.97); }
      to { opacity: 1; transform: scale(1); }
    }
    .modal-window {
      background: #080F24;
      border: 1.5px solid rgba(0, 255, 135, 0.55);
      border-radius: 10px;
      width: 960px;
      max-width: 96vw;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 0 40px rgba(0, 255, 135, 0.25), 0 20px 50px rgba(0, 0, 0, 0.85);
      overflow: hidden;
    }
    .modal-header {
      background: rgba(14, 25, 52, 0.95);
      border-bottom: 1.5px solid rgba(56, 189, 248, 0.35);
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-title-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .modal-title {
      font-family: var(--font-cinzel);
      font-size: 14px;
      font-weight: 800;
      color: #FFF;
      letter-spacing: 0.8px;
    }
    .modal-badge {
      background: rgba(0, 255, 135, 0.15);
      border: 1px solid var(--neon-green);
      color: var(--neon-green);
      font-family: var(--font-mono);
      font-size: 8px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .modal-close-btn {
      background: transparent;
      border: none;
      color: #94A3B8;
      font-size: 18px;
      cursor: pointer;
      line-height: 1;
      padding: 2px 6px;
      border-radius: 4px;
      transition: all 0.15s ease;
    }
    .modal-close-btn:hover {
      color: #FFF;
      background: rgba(255, 0, 127, 0.3);
    }
    .modal-tabs {
      background: rgba(8, 14, 32, 0.9);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      gap: 4px;
      padding: 6px 16px 0;
    }
    .modal-tab-btn {
      background: transparent;
      border: 1px solid transparent;
      border-bottom: none;
      color: #94A3B8;
      font-family: var(--font-mono);
      font-size: 9px;
      font-weight: 800;
      padding: 6px 12px;
      border-radius: 6px 6px 0 0;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 5px;
      letter-spacing: 0.4px;
    }
    .modal-tab-btn:hover {
      color: #FFF;
      background: rgba(255, 255, 255, 0.05);
    }
    .modal-tab-btn.active {
      background: #080F24;
      border-color: rgba(56, 189, 248, 0.4);
      color: var(--neon-cyan);
      border-bottom: 2px solid var(--neon-cyan);
    }
    .modal-body {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .tab-content {
      display: none;
      flex-direction: column;
      gap: 12px;
    }
    .tab-content.active {
      display: flex;
    }

    .card-corpus-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .corpus-card {
      background: rgba(14, 25, 52, 0.65);
      border: 1.5px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .corpus-card:hover {
      background: rgba(14, 25, 52, 0.95);
      border-color: var(--neon-green);
      box-shadow: 0 0 16px rgba(0, 255, 135, 0.25);
      transform: translateY(-2px);
    }
    .corpus-card-hdr {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .corpus-card-title {
      font-family: var(--font-cinzel);
      font-size: 12px;
      font-weight: 800;
      color: #FFF;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .corpus-card-badge {
      font-family: var(--font-mono);
      font-size: 7.5px;
      font-weight: 800;
      padding: 1.5px 5px;
      border-radius: 3px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38BDF8;
    }
    .corpus-card-sub {
      font-size: 9px;
      color: #94A3B8;
      line-height: 1.4;
    }
    .corpus-card-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 4px;
      font-family: var(--font-mono);
      font-size: 7.5px;
      color: #64748B;
    }
    .corpus-card-meta span {
      color: var(--neon-green);
      font-weight: 700;
    }

    .syntax-guide {
      background: rgba(7, 13, 30, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 8.5px;
      line-height: 1.5;
      color: #94A3B8;
    }
    .syntax-guide code {
      font-family: var(--font-mono);
      color: var(--neon-green);
      background: rgba(0, 255, 135, 0.1);
      padding: 1px 4px;
      border-radius: 3px;
    }
    .editor-textarea {
      width: 100%;
      height: 240px;
      background: #050A1A;
      border: 1.5px solid rgba(56, 189, 248, 0.35);
      border-radius: 6px;
      padding: 10px 12px;
      font-family: var(--font-mono);
      font-size: 9.5px;
      color: #F8FAFC;
      line-height: 1.5;
      resize: vertical;
      outline: none;
      transition: all 0.2s ease;
      white-space: pre;
    }
    .editor-textarea:focus {
      border-color: var(--neon-green);
      box-shadow: 0 0 14px rgba(0, 255, 135, 0.25);
    }
    .sample-btns-row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .sample-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #CBD5E1;
      font-family: var(--font-mono);
      font-size: 8px;
      padding: 3px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .sample-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--neon-cyan);
      color: #FFF;
    }
    .modal-footer {
      background: rgba(14, 25, 52, 0.95);
      border-top: 1.5px solid rgba(56, 189, 248, 0.35);
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .modal-action-btn {
      background: rgba(0, 255, 135, 0.2);
      border: 1.5px solid var(--neon-green);
      color: #FFF;
      font-family: var(--font-mono);
      font-size: 9.5px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.5px;
      transition: all 0.2s ease;
    }
    .modal-action-btn:hover {
      background: rgba(0, 255, 135, 0.4);
      box-shadow: 0 0 14px rgba(0, 255, 135, 0.6);
      transform: translateY(-1px);
    }
  </style>
</head>
<body>

  <!-- CABECERA INSTITUCIONAL MINIMALISTA -->
  <header class="app-header">
    <a href="index.html" class="brand-section">
      <img src="LOGO_NEXORD_OFICIAL.png" alt="NEXORD Logo" class="brand-logo" onerror="this.src='LOGO_NEX_ORD_OFICIAL.png';">
      <div class="brand-title">
        NEXORD <span class="brand-badge">VISORD PROCESUAL</span>
        <span class="brand-sub" id="hdrCorpusCode">· CULTURAL-AA-G2-T1-C1-V10-A16-ES-5 · 25 de Septiembre de 2026</span>
      </div>
    </a>

    <!-- SELECTOR DE ESCENARIO / CORPUS TEXTUAL UNIVERSAL -->
    <div class="corpus-selector-group">
      <span class="corpus-lbl">📖 GUION:</span>
      <select id="selCorpusPreset" class="corpus-select" onchange="onSelectCorpusPreset(this.value)">
        <option value="dawes_orbell_5">🪙 Dilema Bien Común (Dawes & Orbell, N=5)</option>
        <option value="12_angry_men_8">⚖️ Jurado Deliberante / 12 Hombres en Pugna (N=8)</option>
        <option value="labor_mediation_6">🤝 Mediación Laboral / Negociación Bipartita (N=6)</option>
        <option value="socrates_trial_5">🏛️ Juicio a Sócrates / Litigio Clásico (N=5)</option>
      </select>
      <button class="corpus-ingest-btn" onclick="openScriptIngestorModal()" title="Cargar, pegar o editar cualquier texto o guion procesual">
        📂 CARGAR GUION PROCESUAL
      </button>
    </div>

    <!-- SELECTOR DE VISTA Y CONTABILIDAD EN SEGUNDO PLANO -->
    <div class="header-center-ctrl">
      <div class="mode-toggle-group">
        <button class="mode-btn active" id="btnModeRuedoFocus" onclick="setLayoutMode('ruedo-focus')" title="El Ruedo a pantalla completa majestuoso · Tablas en segundo plano">
          🎯 FOCO RUEDO
        </button>
        <button class="mode-btn" id="btnModeSplit" onclick="setLayoutMode('split')" title="Ruedo a un lado + Tabla simultánea de resultados en directo al otro">
          ⚖️ SPLIT
        </button>
        <button class="mode-btn" id="btnModeTablesFocus" onclick="setLayoutMode('tables-focus')" title="Tablas de contabilidad a pantalla completa">
          📊 TABLAS
        </button>
        <button class="mode-btn" id="btnModeRuedoWings" onclick="setLayoutMode('ruedo')" title="Ruedo con sus burladeros laterales">
          📡 BURLADEROS
        </button>
      </div>

      <!-- BOTÓN RÁPIDO PARA VER CONTABILIDAD EN SEGUNDO PLANO -->
      <button class="btn-toggle-bg-tables" id="btnToggleBgTables" onclick="toggleTelemetryDrawer()" title="Desplegar las tablas de contabilidad de segundo plano (Tecla T)">
        <span>📊</span> <span>CONTABILIDAD (T)</span>
      </button>

      <!-- SELECTOR N RÁPIDO -->
      <div class="n-selector-group">
        <button class="n-btn active" id="hdrBtnN5" onclick="changeN(5)">N=5</button>
        <button class="n-btn" id="hdrBtnN8" onclick="changeN(8)">N=8</button>
        <button class="n-btn" id="hdrBtnN12" onclick="changeN(12)">N=12</button>
        <button class="n-btn" id="hdrBtnNQ81" onclick="changeN(9)">Q81</button>
      </div>

      <div class="header-autoplay-pill" id="hdrAutoPlayPill" onclick="togglePlay()" title="Control Maestro de Inicio / Pausa">
        <span class="auto-pulse-indicator" id="autoPulseIndicator"></span>
        <span id="hdrPlayText">RADAR ACTIVO</span>
      </div>
    </div>

    <div class="header-nav">
      <a href="radiografias_relacionales.html" class="hdr-btn" title="◀ VISORD Anterior: Radiografías Relacionales">
        ◀ Radiografías
      </a>
      <a href="recursos.html" class="hdr-btn" title="VISORD Siguiente: Recursos ▶">
        Recursos ▶
      </a>
      <a href="index.html" class="hdr-btn" title="Ir al Portal Institucional NEXORD">
        🏠 Portal
      </a>
    </div>
  </header>

  <!-- LÍNEA SUPERIOR DE TELEPROMPTER -->
  <div class="teleprompter-line" id="teleprompterLine">
    <div class="tele-inner">
      <div class="tele-ctrl-group">
        <button class="tele-btn-action" id="btnTeleStart" onclick="togglePlay()" title="Iniciar / Pausar">
          <span id="telePlayIcon">⏸</span> <span id="telePlayLabel">PAUSAR</span>
        </button>
        <button class="tele-btn-sub" onclick="stepPrev()" title="Turno Anterior">⏮</button>
        <button class="tele-btn-sub" onclick="stepNext()" title="Turno Siguiente">⏭</button>
        <button class="tele-btn-sub" onclick="resetDebate()" title="Reiniciar">🔄</button>
      </div>

      <span class="tele-dot">|</span>
      <span class="tele-turn" id="teleTurn">TURNO 01 / 18</span>
      <span class="tele-dot">·</span>
      <span class="tele-actor emit" id="teleSender">1</span>
      <span class="tele-role-badge inic" id="teleSenderRole" title="El sujeto toma la iniciativa de hablar por sí mismo">⚡ DA INICIATIVA</span>
      <span class="tele-dot">➔</span>
      <span class="tele-actor rec" id="teleReceiver">GRUPO (CENTRO)</span>
      <span class="tele-role-badge prov" id="teleReceiverRole" title="El receptor recibe una interpelación o reto directo">🛡️ RC INTERPEL</span>
      <span class="tele-dot">·</span>
      <span class="tele-q81" id="teleQ81" style="color:#00FF87; background:rgba(0,255,135,0.15);">&lt;Ee&gt;</span>
      <span class="tele-dot">·</span>
      <span class="tele-text" id="teleText">"Compañeros, la matemática del fondo común es irrefutable: si los cinco aportamos nuestras 10 fichas, el bote de 50 se multiplica por 1.8 y nos repartimos 18 fichas cada uno."</span>

      <div style="margin-left:auto; display:flex; align-items:center; gap:6px; flex-shrink:0;">
        <input type="range" id="scrubberSlider" min="1" max="18" value="1" style="width:65px; accent-color:#00FF87; height:3px; cursor:pointer;" oninput="seekToTurn(this.value)">
        <span id="scrubberLabel" style="font-size:7.5px; color:#00FF87; font-family:var(--font-mono); font-weight:700;">01/18</span>
        <button class="tele-btn-sub" id="btnSpeedTele" onclick="toggleSpeed(this)">1.0x</button>
        <button class="tele-btn-sub active" id="btnSfxTele" onclick="toggleSFX()">🔊 SFX</button>
        <button class="tele-btn-sub" id="btnVoiceTele" onclick="toggleVoice()">🎙️ VOZ</button>
      </div>
    </div>
  </div>

  <!-- CONTENEDOR PRINCIPAL DEL ESCENARIO -->
  <main class="stage-container" id="mainContainer">

    <!-- 1. BARRA SUPERIOR AZUL (DAN) -->
    <div class="stage-bar-blue" id="stageBarBlue"></div>

    <!-- 2. GRID PRINCIPAL: MODO FOCO RUEDO POR DEFECTO -->
    <div class="stage-grid mode-ruedo-focus" id="stageGrid">

      <!-- FLANCO IZQUIERDO: BURLADERO BANDO A -->
      <div class="stage-wing-left" id="stageWingLeft">
        <div class="wing-title-bar">
          <span>🏛️ BURLADERO FLANCO IZQUIERDO · BANDO A</span>
          <span style="color:#00FF87;" id="wingLeftSub">(SUJETOS 1..3 · DOBLE CONTABILIDAD)</span>
        </div>
        <div class="wing-header-row">
          <div>SUJETO</div>
          <div>⚡</div>
          <div title="Dador: Iniciativa propia">DA INIC</div>
          <div title="Dador: Respuesta a provocación">DA RESP</div>
          <div title="Receptor: Interpelación / Reto recibido">RC PROV</div>
          <div title="Receptor: Respuesta / Feedback recibido">RC RESP</div>
          <div>SALDO</div>
          <div id="wingHdrAporteL">APORTE</div>
          <div id="wingHdrCarteraL">CARTERA</div>
          <div>ESTATUS</div>
        </div>
        <div class="wing-body" id="wingLeftBody"></div>
      </div>

      <!-- ESCENARIO CENTRAL: EL RUEDO RELACIONAL (ANFITEATRO CIRCULAR MAJESTUOSO) -->
      <div class="stage-center-arena" id="stageCenterArena">
        <canvas class="cuad-vector-canvas" id="cuadVectorCanvas"></canvas>
        <div class="center-matrix-grid" id="centerMatrixGrid"></div>
      </div>

      <!-- FLANCO DERECHO: BURLADERO BANDO B -->
      <div class="stage-wing-right" id="stageWingRight">
        <div class="wing-title-bar">
          <span style="color:#FCD34D;" id="wingRightSub">(SUJETOS 4..5 · DOBLE CONTABILIDAD)</span>
          <span>BANDO B · BURLADERO FLANCO DERECHO 🏛️</span>
        </div>
        <div class="wing-header-row">
          <div>SUJETO</div>
          <div>⚡</div>
          <div title="Dador: Iniciativa propia">DA INIC</div>
          <div title="Dador: Respuesta a provocación">DA RESP</div>
          <div title="Receptor: Interpelación / Reto recibido">RC PROV</div>
          <div title="Receptor: Respuesta / Feedback recibido">RC RESP</div>
          <div>SALDO</div>
          <div id="wingHdrAporteR">APORTE</div>
          <div id="wingHdrCarteraR">CARTERA</div>
          <div>ESTATUS</div>
        </div>
        <div class="wing-body" id="wingRightBody"></div>
      </div>

      <!-- GRAN TABLA SIMULTÁNEA DE RESULTADOS EN DIRECTO (PANEL PRIMARIO EN MODO SPLIT/TABLES) -->
      <div class="stage-live-table-panel" id="stageLiveTablePanel">
        <!-- MACRO TELEMETRÍA EN VIVO -->
        <div class="live-macro-telemetry">
          <div class="macro-card">
            <span class="macro-lbl" id="liveBoteLbl">🪙 FONDO / BOTE</span>
            <span class="macro-val" id="liveBoteVal" style="color:#00FF87;">🪙 50.0 F</span>
            <span class="macro-sub" id="liveBoteSub">FONDO COLECTIVO</span>
          </div>
          <div class="macro-card">
            <span class="macro-lbl">TERMODINÁMICA</span>
            <span class="macro-val" id="liveClimaVal" style="color:#00FF87;">&lt;Ee&gt; COHESIÓN</span>
            <span class="macro-sub" id="liveClimaSub">ESTADO GRUPAL</span>
          </div>
          <div class="macro-card">
            <span class="macro-lbl">TURNO PROCESUAL</span>
            <span class="macro-val" id="liveTurnVal" style="color:#38BDF8;">01 / 18</span>
            <span class="macro-sub" id="liveTurnSub">SECUENCIA ACTIVA</span>
          </div>
          <div class="macro-card">
            <span class="macro-lbl">DIAGNÓSTICO</span>
            <span class="macro-val" id="liveStatusNote" style="font-size:10.5px; color:#00FF87;">ÓPTIMO PARETO</span>
            <span class="macro-sub">DIALÉCTICA EN DIRECTO</span>
          </div>
        </div>

        <!-- VISTA DIVIDIDA: MINI SOCIOMATRIZ SMIb + GRAN TABLA CUANTITATIVA -->
        <div class="live-split-view">
          <!-- MINI SOCIOMATRIZ SMIb -->
          <div class="mini-matrix-box">
            <div class="mini-box-hdr">
              <span>SOCIOMATRIZ DINÁMICA SMIb (COLUMNAS: DAN | FILAS: RECIBEN)</span>
              <span id="miniMatLegend" style="font-size:7px; color:#94A3B8;">&lt;Ee&gt; +1.0 | [Rr] -1.0 | ¡¿?! 0.0</span>
            </div>
            <div class="live-matrix-container" id="liveMatrixContainer"></div>
          </div>

          <!-- GRAN TABLA CUANTITATIVA EN 4 BLOQUES (12 COLUMNAS) -->
          <div class="live-table-container">
            <table class="live-data-table" id="liveDataTable">
              <thead>
                <tr class="super-th-row">
                  <th colspan="3" class="th-group-subj">PARTICIPANTE</th>
                  <th colspan="3" class="th-group-dador">⚔️ FUNCIÓN DADOR (EMISIÓN)</th>
                  <th colspan="3" class="th-group-rec">🛡️ FUNCIÓN RECEPTOR ALTERNATIVO</th>
                  <th colspan="3" class="th-group-bal">🪙 BALANCE & BIENES COMUNES</th>
                </tr>
                <tr>
                  <th>ID</th>
                  <th>ROL / NOMBRE</th>
                  <th>BANDO</th>
                  <th class="col-dador" title="Iniciativa Propia">INIC.</th>
                  <th class="col-dador" title="Respuesta a Provocación">RESP.</th>
                  <th class="col-dador" id="liveThAporte">APORTE</th>
                  <th class="col-rec" title="Interpelación o Reto recibido">INTERP.</th>
                  <th class="col-rec" title="Respuesta o Réplica recibida">FEEDBK</th>
                  <th class="col-rec" id="liveThRetorno">RETORNO</th>
                  <th class="col-bal">SALDO</th>
                  <th class="col-bal" id="liveThCartera">CARTERA</th>
                  <th class="col-bal">ESTADO SOCIOTÉRMICO</th>
                </tr>
              </thead>
              <tbody id="liveTableBody"></tbody>
            </table>
          </div>
        </div>

        <!-- BARRA TERMODINÁMICA INFERIOR -->
        <div class="live-thermo-bar">
          <div class="thermo-item">
            <span class="thermo-lbl">DENSIDAD RELATIVA (SDR):</span>
            <span class="thermo-val" id="thermoSDR" style="color:#00FF87;">0.840 (ALTA)</span>
          </div>
          <div class="thermo-item">
            <span class="thermo-lbl">VALENCIA POLAR Σ(+)/Σ(-):</span>
            <span class="thermo-val" style="display:flex; gap:6px;">
              <span id="thermoPos" style="color:#00FF87;">Σ(+): 1</span>
              <span id="thermoNeg" style="color:#FF3366;">Σ(-): 0</span>
            </span>
          </div>
          <div class="thermo-item">
            <span class="thermo-lbl">FRUSTRACIÓN DE HEIDER (λ₁):</span>
            <span class="thermo-val" id="thermoHeider" style="color:#00FF87;">0.042 (ESTABLE)</span>
          </div>
          <div class="thermo-item">
            <span class="thermo-lbl">INTEGRACIÓN DE TONONI (Φ):</span>
            <span class="thermo-val" id="thermoTononi" style="color:#00FF87;">1.450 Φ (MÁXIMA)</span>
          </div>
        </div>
      </div>

    </div>

    <!-- 3. BARRA INFERIOR VERDE (BIENES COMUNES) -->
    <div class="stage-bar-green" id="stageBarGreen"></div>

    <!-- NOTA EXPLICATIVA PEDAGÓGICA (REGLA 10 DE AGENTS.MD) -->
    <div class="visord-pedagogical-note">
      <div class="note-title">
        <span>💡 NOTA EXPLICATIVA PEDAGÓGICA · VISORD PROCESUAL: MOTOR UNIVERSAL DE OBSERVACIÓN DE TEXTOS</span>
      </div>
      <div class="note-body">
        El <strong>VISORD PROCESUAL</strong> es la arquitectura canónica de observación secuencial, dialéctica y socio-termodinámica para cualquier interacción textual o verbal (teatro, litigios judiciales, debates parlamentarios, asambleas de vecinos, mediaciones de conflicto o diálogos filosóficos en la categoría <code>CULTURAL</code>).
        <br><br>
        <strong>1. Geometría Bipolar del Ruedo (Eliminación de la Distorsión Especular)</strong>: En ningún debate real un participante se sienta frente a un espejo de sí mismo. Los sujetos se distribuyen armónicamente en dos gradas semicirculares encaradas (Flanco Izquierdo · Bando A vs. Flanco Derecho · Bando B).
        <br>
        <strong>2. Tablas de Contabilidad en Segundo Plano</strong>: Para preservar la majestad circular del Ruedo y evitar que tablas masivas compriman la arena en pantallas convencionales, la contabilidad completa se calcula en <em>segundo plano</em>. Puede desplegarse instantáneamente mediante el cajón inferior o la tecla <code>T</code>.
        <br>
        <strong>3. El Centro del Ruedo como Espacio Plenario Grupal</strong>: Representa el espacio colectivo (el tribunal, la asamblea, el fondo común o el veredicto). Cuando un participante habla al plenario, <em>el rayo se detiene en el círculo concéntrico de identidad del centro</em>. Cuando el plenario emite una resolución o resultado, <em>el rayo nace en dicho círculo concéntrico hacia la periferia</em>. Si sobreviene una deliberación muda o pausa reflexiva, <em>los silencios no disparan rayos, sino que generan un torbellino centrípeto en el centro</em>.
        <br>
        <strong>4. Doble Contabilidad Relacional y Regla Canónica de Respuesta</strong>: En el flujo conversacional, todo participante cumple dos funciones dialécticas con contabilidad rigurosamente separada:
        <br>
        • <em>Como Dador (Emisor)</em>: Se establece formalmente que un sujeto actúa en <strong>Respuesta</strong> (<code>DA RESP</code>) si y solo si su intervención sucede <em>inmediatamente después de recibir una interacción en el turno \(t-1\)</em> (bien por interpelación directa entre pares o por alocución plenaria dirigida al colectivo). En cualquier otro caso (si no fue el destinatario en \(t-1\), o si inaugura el debate), actúa por <strong>Iniciativa Propia</strong> (<code>DA INIC</code>).
        <br>
        • <em>Como Receptor Alternativo</em>: Recibe <strong>Feedback / Réplica</strong> (<code>RC RESP</code>) si era quien acababa de hablar en el turno \(t-1\); de lo contrario, recibe una <strong>Interpelación o Reto Directo</strong> (<code>RC PROV</code>) sobrevenido.
        <br>
        Esta regla delimita con rigor matemático el liderazgo proactivo frente a la reactividad situacional, calculando el saldo dialéctico neto (\(DA - RC\)) y el balance acumulado en tiempo real.
      </div>
    </div>

  </main>

  <!-- =========================================================================
       CAJÓN DESPLEGABLE DE CONTABILIDAD EN SEGUNDO PLANO (TELEMETRY DRAWER)
       ========================================================================= -->
  <div class="telemetry-drawer" id="telemetryDrawer">
    <!-- PESTAÑA MANIJA DEL CAJÓN -->
    <div class="drawer-tab-handle" onclick="toggleTelemetryDrawer()">
      <div class="drawer-tab-left">
        <span class="drawer-pulse-dot"></span>
        <span class="drawer-title">📊 TABLAS DE CONTABILIDAD EN SEGUNDO PLANO</span>
        <span class="drawer-stat">FONDO: <b id="drawerBoteVal">🪙 50.0 F</b></span>
        <span class="drawer-stat">CLIMA: <b id="drawerClimaVal">&lt;Ee&gt; COHESIÓN</b></span>
        <span class="drawer-stat">SDR: <b id="drawerSdrVal">0.840</b></span>
      </div>
      <div class="drawer-toggle-arrow" id="drawerToggleArrow">
        <span>▲</span> <span>DESPLEGAR TABLAS (T)</span>
      </div>
    </div>

    <!-- CONTENIDO DEL CAJÓN DE SEGUNDO PLANO -->
    <div class="drawer-body" id="drawerBody">
      <!-- Inyectado o clonado dinámicamente -->
      <div id="drawerTableInsert"></div>
    </div>
  </div>

  <!-- MANDO UNIVERSAL FLOTANTE (REGLA 15 DE AGENTS.MD) -->
  <nav class="universal-nav-pod" id="universalNavPod">
    <a href="index.html" class="nav-pod-btn" title="Inicio / Portada Principal">🏠</a>
    <a href="radiografias_relacionales.html" class="nav-pod-btn" title="◀ Estación Anterior: Radiografías Relacionales">◀</a>
    <a href="#teleprompterLine" class="nav-pod-btn" title="Subir al Teleprompter">▲</a>
    <a href="#mainContainer" class="nav-pod-btn" title="Ir al Ruedo">▼</a>
    <a href="recursos.html" class="nav-pod-btn" title="Estación Siguiente: Recursos ▶">▶</a>
  </nav>

  <!-- MODAL: OBSERVADOR UNIVERSAL DE TEXTOS PROCESUALES & SMART INGESTOR -->
  <div class="modal-backdrop" id="modalScriptIngestor">
    <div class="modal-window">
      <!-- HEADER DEL MODAL -->
      <div class="modal-header">
        <div class="modal-title-group">
          <span style="font-size:16px;">🏛️</span>
          <div class="modal-title">OBSERVADOR UNIVERSAL DE TEXTOS PROCESUALES</div>
          <span class="modal-badge">INGESTOR Y BIBLIOTECA</span>
        </div>
        <button class="modal-close-btn" onclick="closeScriptIngestorModal()" title="Cerrar modal">✕</button>
      </div>

      <!-- PESTAÑAS DEL MODAL -->
      <div class="modal-tabs">
        <button class="modal-tab-btn active" id="tabBtnLibrary" onclick="switchIngestorTab('library')">
          <span>📚</span> BIBLIOTECA CANÓNICA
        </button>
        <button class="modal-tab-btn" id="tabBtnText" onclick="switchIngestorTab('text')">
          <span>📝</span> PEGAR GUION DE TEXTO (SMART PARSER)
        </button>
        <button class="modal-tab-btn" id="tabBtnJson" onclick="switchIngestorTab('json')">
          <span>⚙️</span> EDITOR JSON / EXPORTAR
        </button>
      </div>

      <!-- CUERPO DEL MODAL -->
      <div class="modal-body">
        
        <!-- PESTAÑA 1: BIBLIOTECA CANÓNICA -->
        <div class="tab-content active" id="tabContentLibrary">
          <div style="font-size:9.5px; color:#94A3B8;">
            Seleccione uno de los escenarios canónicos preparados para cargar instantáneamente su topología, bandos encarados, doble contabilidad y dinámica procesual:
          </div>
          <div class="card-corpus-grid">
            <div class="corpus-card active-corpus-item" onclick="loadCanonicalCorpus('dawes_orbell_5')">
              <div class="corpus-card-hdr">
                <div class="corpus-card-title">🪙 Dilema del Bien Común</div>
                <span class="corpus-card-badge">N=5 · DAWES & ORBELL</span>
              </div>
              <div class="corpus-card-sub">
                Teoría de juegos y dilema de cooperación colectiva. Unanimidad verbal inicial seguida de la deserción del polizón (Sujeto 5) y colapso de la confianza.
              </div>
              <div class="corpus-card-meta">
                <span>18 Turnos</span> · <span>2 Bandos (3 vs 2)</span> · <span>Fondo de Fichas (🪙)</span>
              </div>
            </div>

            <div class="corpus-card" onclick="loadCanonicalCorpus('12_angry_men_8')">
              <div class="corpus-card-hdr">
                <div class="corpus-card-title">⚖️ Doce Hombres en Pugna</div>
                <span class="corpus-card-badge">N=8 · LITIGIO JUDICIAL</span>
              </div>
              <div class="corpus-card-sub">
                Deliberación de jurado penal. Disidencia solitaria del Jurado 8 (Arquitecto) que quiebra el consenso inicial acusatorio mediante el examen crítico de la prueba.
              </div>
              <div class="corpus-card-meta">
                <span>16 Turnos</span> · <span>2 Bandos (4 vs 4)</span> · <span>Votos de Duda (⚖️)</span>
              </div>
            </div>

            <div class="corpus-card" onclick="loadCanonicalCorpus('labor_mediation_6')">
              <div class="corpus-card-hdr">
                <div class="corpus-card-title">🤝 Mediación Laboral Bipartita</div>
                <span class="corpus-card-badge">N=6 · CONVENIO COLECTIVO</span>
              </div>
              <div class="corpus-card-sub">
                Negociación de convenio colectivo entre el Comité Sindical (Bando A) y la Dirección Empresarial (Bando B), con bloqueo, silencios y pacto final.
              </div>
              <div class="corpus-card-meta">
                <span>14 Turnos</span> · <span>2 Bandos (3 vs 3)</span> · <span>Concesiones (🤝)</span>
              </div>
            </div>

            <div class="corpus-card" onclick="loadCanonicalCorpus('socrates_trial_5')">
              <div class="corpus-card-hdr">
                <div class="corpus-card-title">🏛️ Juicio a Sócrates (Platón)</div>
                <span class="corpus-card-badge">N=5 · FILOSOFÍA CLÁSICA</span>
              </div>
              <div class="corpus-card-sub">
                Diálogo mayéutico ante el tribunal ateniense. El filósofo interroga a Meleto y desafía la rigidez dogmática de sus tres acusadores en la polis.
              </div>
              <div class="corpus-card-meta">
                <span>12 Turnos</span> · <span>2 Bandos (2 vs 3)</span> · <span>Alegatos (🏛️)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- PESTAÑA 2: PEGAR GUION DE TEXTO (SMART PARSER) -->
        <div class="tab-content" id="tabContentText">
          <div class="syntax-guide">
            <strong>Sintaxis Inteligente de Ingestión Textual:</strong><br>
            • Diálogo directo entre pares: <code>1 -> 2: Texto del diálogo...</code> o <code>Ana -> Bruno: Texto...</code><br>
            • Intervención al plenario / asamblea: <code>1: Propongo al grupo...</code> o <code>1 -> Centro: Propongo...</code><br>
            • Resolución o veredicto del centro: <code>Centro -> 1: El tribunal aprueba...</code><br>
            • Pausa deliberativa / silencio: <code>[silencio]: La sala reflexiona...</code> o <code>SILENCIO: Nadie responde...</code><br>
            • Metadatos opcionales: <code># Titulo: Mi Debate</code>, <code># Participantes: 1:Ana, 2:Bruno | 3:Carlos, 4:Diana</code>
          </div>

          <div class="sample-btns-row">
            <span style="font-size:7.5px; font-family:var(--font-mono); color:#94A3B8;">EJEMPLOS RÁPIDOS:</span>
            <button class="sample-btn" onclick="insertSampleScript('deliberacion')">📋 Deliberación de Comité</button>
            <button class="sample-btn" onclick="insertSampleScript('negociacion')">🤝 Negociación Paritaria</button>
            <button class="sample-btn" onclick="insertSampleScript('litigio')">⚖️ Discusión Jurídica</button>
          </div>

          <textarea class="editor-textarea" id="txtCustomScript" placeholder="# Pegue aquí su texto procesual, diálogo teatral, acta o debate..."></textarea>
        </div>

        <!-- PESTAÑA 3: EDITOR JSON / EXPORTAR -->
        <div class="tab-content" id="tabContentJson">
          <div style="font-size:9px; color:#94A3B8;">
            Estructura canónica JSON del corpus actual. Puede editarla directamente, cargar un archivo <code>.json</code> o descargarlo para su archivo científico:
          </div>
          <textarea class="editor-textarea" id="txtJsonCorpus" style="height:260px;"></textarea>
          <div style="display:flex; gap:8px;">
            <button class="sample-btn" onclick="loadCorpusFromJsonInput()">⚡ Cargar JSON Editado</button>
            <button class="sample-btn" onclick="downloadCurrentCorpusJson()">💾 Descargar Guion JSON</button>
            <button class="sample-btn" onclick="copyJsonToClipboard()">📋 Copiar JSON</button>
          </div>
        </div>

      </div>

      <!-- FOOTER DEL MODAL -->
      <div class="modal-footer">
        <span style="font-size:8px; font-family:var(--font-mono); color:#94A3B8;" id="modalStatusMsg">
          VISORD Engine: Listo para procesar cualquier texto procesual.
        </span>
        <div style="display:flex; gap:8px;">
          <button class="hdr-btn" onclick="closeScriptIngestorModal()">Cancelar</button>
          <button class="modal-action-btn" id="btnApplyCustomText" onclick="processCustomPastedText()">
            <span>⚡</span> PROCESAR Y APLICAR AL RUEDO
          </button>
        </div>
      </div>

    </div>
  </div>
  <script>
    /* =========================================================================
       VISORD PROCESUAL: OBSERVADOR UNIVERSAL DE TEXTOS Y DIÁLOGOS
       NÚCLEO SOCIO-TERMODINÁMICO DE OBSERVACIÓN SECUENCIAL Y TOPOLÓGICA
       ========================================================================= */

    /* 1. BIBLIOTECA CANÓNICA DE ESCENARIOS PROCESUALES */
    const CANONICAL_CORPORA = {
      'dawes_orbell_5': {
        id: 'dawes_orbell_5',
        code: 'CULTURAL-AA-G2-T1-C1-V10-A16-ES-5',
        title: 'Dilema de Bienes Comunes (Dawes & Orbell)',
        subtitle: 'Teoría de Juegos · Cooperación Colectiva, Deserción del Polizón y Colapso Termodinámico',
        groupCenterName: 'FONDO COMÚN',
        unitSymbol: '🪙',
        unitName: 'fichas',
        investmentLabel: 'APORTE',
        dividendLabel: 'RETORNO',
        resourceLabel: 'CARTERA',
        actors: [
          { id: '1', name: '1A (Proponente)', role: 'Proponente Líder', bando: 'A', color: '#00FF87' },
          { id: '2', name: '2A (Conciliador)', role: 'Moderador Aliado', bando: 'A', color: '#38BDF8' },
          { id: '3', name: '3A (Escéptico)', role: 'Escéptico Cauto', bando: 'A', color: '#FCD34D' },
          { id: '4', name: '4B (Pragmático)', role: 'Pragmático Dubitativo', bando: 'B', color: '#A855F7' },
          { id: '5', name: '5B (Polizón)', role: 'Polizón Desertor', bando: 'B', color: '#FF007F' }
        ],
        turns: [
          { turn: 1, sender: 0, receiver: 1, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Compañeros, la matemática del fondo común es irrefutable: si los cinco aportamos nuestras 10 fichas, el bote de 50 se multiplica por 1.8 y nos repartimos 18 fichas cada uno." },
          { turn: 2, sender: 1, receiver: 0, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Completamente de acuerdo contigo, 1. Es la única estrategia racional y colectiva. Yo me comprometo públicamente a poner mis 10 fichas desde el primer segundo." },
          { turn: 3, sender: 2, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'respuesta', recType: 'provocacion', tetra: ['0','+','0','+'], q81: '(Ee>', color: '#38BDF8', text: "La teoría sobre el papel es perfecta, 1. Pero solo funciona si no hay polizones. Si cuatro ponemos 10 y uno pone cero, ese se lleva 24.4 y los demás perdemos." },
          { turn: 4, sender: 3, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['0','0','0','0'], q81: '¡¿?!', color: '#FFE600', text: "Comparto la inquietud de 3. No conozco el historial del grupo en votaciones a ciegas. Si cooperamos a tontas y a locas nos exponemos a una sangría." },
          { turn: 5, sender: 4, receiver: 0, flow: 'to_center', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Por favor, 3 y 4, no entremos en paranoias innecesarias antes de empezar. El incentivo conjunto es gigantesco. Doy mi palabra de que aportaré íntegramente mis 10 fichas." },
          { turn: 6, sender: 0, receiver: 4, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Excelente, 5. Con tu respaldo explícito ya tenemos a la mayoría con compromiso verbal sellado. 3, 4: la confianza se construye. ¿Podemos contar con vosotros?" },
          { turn: 7, sender: 2, receiver: 4, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['0','0','-','0'], q81: '¡?r!', color: '#FF9F1C', text: "5, hablas con demasiada soltura. En los dilemas de Dawes y Orbell, quienes más enfáticamente juran cooperar son estadísticamente los que más desertan." },
          { turn: 8, sender: 4, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['-','+','-','+'], q81: '[Er>', color: '#FF9F1C', text: "¿Me estás llamando mentiroso a la cara, 3? Esa desconfianza corrosiva es la que arruina los grupos. Aportaré el 100% y te dejaré en evidencia." },
          { turn: 9, sender: 1, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['+','+','0','+'], q81: '<Ee!', color: '#38BDF8', text: "Haya paz, compañeros. Si 1, 5 y yo aportamos 10, ya hay 30 fichas seguras. 3, tu recelo es legítimo, pero si desertas por miedo, provocarás la ruina." },
          { turn: 10, sender: 3, receiver: 1, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Tienes razón, 2. Agradezco tu tono conciliador. Si 1 y tú os comprometéis de verdad, yo no seré el freno del grupo. Cuenten con mis 10 fichas." },
          { turn: 11, sender: 0, receiver: 2, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Solo faltas tú, 3. Todos nos hemos expuesto por el bien común. Si te unes, aseguramos el óptimo de Pareto perfecto: 18 fichas limpias para cada uno." },
          { turn: 12, sender: 2, receiver: 0, flow: 'to_center', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "De acuerdo. Cedo ante la presión del consenso. Confiaré en la palabra colectiva. Votaré cooperar con mis 10 fichas." },
          { turn: 13, sender: 4, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "¡Brillante! Unanimidad absoluta. Hemos demostrado madurez moral. Nadie traicionará el pacto porque sería una ignominia social imperdonable." },
          { turn: 14, sender: 1, receiver: 4, flow: 'to_center', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Un aplauso para todos. La asamblea deliberativa ha funcionado. Votemos con tranquilidad y cosechemos las 18 fichas cada uno." },
          { turn: 15, sender: 0, receiver: 0, flow: 'silence', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "PACTO CERRADO: Unanimidad verbal del 100% (50 fichas al bote común). Procedemos de inmediato a la urna de votación secreta e individual." },
          { turn: 16, sender: 4, receiver: 0, flow: 'from_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "VOTACIÓN SECRETA EJECUTADA: 1 aporta 10 | 2 aporta 10 | 3 aporta 10 | 4 aporta 10 | 5 APORTA 0 FICHAS (¡DESERCIÓN POLIZÓN!)." },
          { turn: 17, sender: 2, receiver: 4, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "¡LO SABÍA! 5 nos ha estafado a sangre fría. Se queda con sus 10 fichas privadas y además cobra 14.4 fichas del bote común: ¡24.4 fichas frente a nuestras 14.4!" },
          { turn: 18, sender: 0, receiver: 4, flow: 'from_center', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "5, has dinamitado la seguridad psicológica del grupo. Tu ganancia material inmediata aísla tu nodo y fractura la red en el colapso termodinámico más severo." }
        ]
      },

      '12_angry_men_8': {
        id: '12_angry_men_8',
        code: 'CULTURAL-AA-G2-T1-C1-V10-A16-ES-8',
        title: 'Deliberación Judicial · Doce Hombres en Pugna (12 Angry Men)',
        subtitle: 'Litigio Procesual · Disidencia Solitaria Frente a la Acusación Rígida y Giro Dialéctico',
        groupCenterName: 'TRIBUNAL / VEREDICTO',
        unitSymbol: '⚖️',
        unitName: 'votos',
        investmentLabel: 'ALEGATOS',
        dividendLabel: 'IMPACTO',
        resourceLabel: 'CONVICCIÓN',
        actors: [
          { id: '1', name: 'Jurado 8 (Arquitecto)', role: 'Disidente Solitario', bando: 'A', color: '#00FF87' },
          { id: '2', name: 'Jurado 9 (Anciano)', role: 'Observador Perceptivo', bando: 'A', color: '#38BDF8' },
          { id: '3', name: 'Jurado 2 (Prudente)', role: 'Empleado Cauto', bando: 'A', color: '#34D399' },
          { id: '4', name: 'Jurado 5 (Suburbio)', role: 'Testigo Experto', bando: 'A', color: '#00F0FF' },
          { id: '5', name: 'Jurado 3 (Empresario)', role: 'Acusador Colérico', bando: 'B', color: '#FF007F' },
          { id: '6', name: 'Jurado 4 (Corredor)', role: 'Racionalista Formal', bando: 'B', color: '#FB923C' },
          { id: '7', name: 'Jurado 7 (Vendedor)', role: 'Impaciente Cínico', bando: 'B', color: '#FCD34D' },
          { id: '8', name: 'Jurado 10 (Hostil)', role: 'Dogmático Agresivo', bando: 'B', color: '#F43F5E' }
        ],
        turns: [
          { turn: 1, sender: 0, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "No puedo levantar la mano y enviar a morir a un chico de 18 años sin hablar de ello al menos una hora." },
          { turn: 2, sender: 4, receiver: 0, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "¿Qué hay que hablar? ¡Once creemos que es culpable! ¡Los hechos del juicio son aplastantes y evidentes!" },
          { turn: 3, sender: 5, receiver: 0, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','+','-','+'], q81: '[Er>', color: '#FB923C', text: "La navaja automática es una pieza única. El comerciante declaró que no existía otra igual en toda la ciudad." },
          { turn: 4, sender: 0, receiver: 5, flow: 'to_center', isPlenary: true, actType: 'respuesta', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Compré esta navaja idéntica anoche a tres manzanas de la vivienda por dos dólares. No era única." },
          { turn: 5, sender: 0, receiver: 0, flow: 'silence', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['0','0','0','0'], q81: '¡¿?!', color: '#FFE600', text: "Silencio absoluto en la sala. Los jurados observan con estupor las dos navajas gemelas clavadas en la mesa." },
          { turn: 6, sender: 6, receiver: 0, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['0','0','-','0'], q81: '¡?r!', color: '#FCD34D', text: "De acuerdo, una coincidencia. Pero el anciano de abajo escuchó el golpe del cuerpo y los gritos en el piso." },
          { turn: 7, sender: 1, receiver: 6, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','0','+'], q81: '<Ee!', color: '#38BDF8', text: "Ese anciano arrastra una pierna por un ictus. Tardó 41 segundos en recorrer el pasillo, no 15 como juró." },
          { turn: 8, sender: 4, receiver: 1, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "¡Qué sabrás tú! ¡Te estás inventando fantasías seniles para justificar que un criminal quede impune!" },
          { turn: 9, sender: 0, receiver: 4, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['+','+','-','+'], q81: '<Er>', color: '#00FF87', text: "No le grite, 3. El tren elevado pasaba rugiendo frente a la ventana abierta. Nadie podía oír ese grito." },
          { turn: 10, sender: 3, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00F0FF', text: "En las peleas callejeras nadie apuñala hacia abajo con navaja de resorte; se empuña siempre de abajo a arriba." },
          { turn: 11, sender: 2, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#34D399', text: "Las dudas ya no son teóricas, son materiales y físicas. Cambio mi postura oficial: voto No Culpable." },
          { turn: 12, sender: 7, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#F43F5E', text: "¡Esa gentuza miente por instinto! ¡Si les dejamos libres en la calle nos devorarán a todos vivos!" },
          { turn: 13, sender: 7, receiver: 7, flow: 'silence', isPlenary: true, actType: 'respuesta', recType: 'feedback', tetra: ['0','0','0','0'], q81: '¡¿?!', color: '#FFE600', text: "Todos los jurados se levantan de espaldas a la mesa en desprecio unánime ante la hostilidad de 10." },
          { turn: 14, sender: 5, receiver: 0, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#FB923C', text: "La marca de las gafas en la nariz de la testigo prueba que no las llevaba en la cama. Duda razonable." },
          { turn: 15, sender: 4, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'respuesta', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "¡No podéis abandonarme! ¡Ese chico merece la pena capital! ¡No daré mi brazo a torcer jamás!" },
          { turn: 16, sender: 0, receiver: 0, flow: 'from_center', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "No culpable. El veredicto de la asamblea es unánime en el respeto a la vida y la duda razonable." }
        ]
      },

      'labor_mediation_6': {
        id: 'labor_mediation_6',
        code: 'CULTURAL-AA-G2-T1-C1-V10-A16-ES-6',
        title: 'Mediación Laboral · Conflicto de Convenio Colectivo',
        subtitle: 'Negociación Bipartita · Reivindicaciones, Tensión Presupuestaria y Pacto Social',
        groupCenterName: 'MESA DE NEGOCIACIÓN',
        unitSymbol: '🤝',
        unitName: 'puntos',
        investmentLabel: 'OFERTAS',
        dividendLabel: 'CONCESIONES',
        resourceLabel: 'CAPITAL',
        actors: [
          { id: '1', name: 'T1 (Portavoz Sindical)', role: 'Portavoz Social', bando: 'A', color: '#00FF87' },
          { id: '2', name: 'T2 (Salud y Turnos)', role: 'Delegada Prevención', bando: 'A', color: '#38BDF8' },
          { id: '3', name: 'T3 (Base Operativa)', role: 'Representante Turnos', bando: 'A', color: '#34D399' },
          { id: '4', name: 'E1 (Director General)', role: 'Director General', bando: 'B', color: '#FF9F1C' },
          { id: '5', name: 'E2 (Directora RRHH)', role: 'Directora Personas', bando: 'B', color: '#FCD34D' },
          { id: '6', name: 'E3 (Asesor Legal)', role: 'Asesor Financiero', bando: 'B', color: '#FF5E85' }
        ],
        turns: [
          { turn: 1, sender: 0, receiver: 3, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','-','+'], q81: '<Er>', color: '#00FF87', text: "Dirección, ponemos sobre la mesa la subida salarial vinculada al IPC real más la regulación del turno nocturno." },
          { turn: 2, sender: 3, receiver: 0, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['-','+','-','+'], q81: '[Er>', color: '#FF9F1C', text: "La inflación actual hace inasumible una indexación automática directa; pondría en riesgo la viabilidad de la planta." },
          { turn: 3, sender: 1, receiver: 4, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['0','0','-','0'], q81: '¡?r!', color: '#38BDF8', text: "Los accidentes en el tercer turno han aumentado un 18%. No es solo dinero, es salud física no negociable." },
          { turn: 4, sender: 4, receiver: 1, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','0','+'], q81: '<Ee!', color: '#FCD34D', text: "En ergonomía y rotaciones de descanso podemos acordar un plan de choque inmediato financiado al 100%." },
          { turn: 5, sender: 2, receiver: 5, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF3366', text: "Si el viernes no hay preacuerdo con fecha de pago, la asamblea de fábrica ya ha votado ir a la huelga indefinida." },
          { turn: 6, sender: 5, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF5E85', text: "Una huelga rompería los contratos internacionales de suministro. Sería un suicidio para el empleo de todos." },
          { turn: 7, sender: 0, receiver: 0, flow: 'silence', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['0','0','0','0'], q81: '¡¿?!', color: '#FFE600', text: "Receso de 15 minutos en la sala. Los mediadores consultan balances y cuadros de márgenes en silencio." },
          { turn: 8, sender: 3, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#FF9F1C', text: "Reanudamos. Proponemos un plus de productividad consolidable más una cláusula de revisión a los dos años." },
          { turn: 9, sender: 0, receiver: 3, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Si ese plus garantiza el poder adquisitivo en el 90% del tramo y blindamos los descansos, lo llevaremos a votación." },
          { turn: 10, sender: 4, receiver: 1, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#FCD34D', text: "Aceptamos la comisión paritaria de turnos con veto sindical en prevención de riesgos desde este lunes." },
          { turn: 11, sender: 1, receiver: 4, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#38BDF8', text: "Ese punto era irrenunciable para la plantilla. Valoramos el avance de la representación empresarial." },
          { turn: 12, sender: 2, receiver: 3, flow: 'to_center', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#34D399', text: "La asamblea desconvocará el preaviso de paro una vez redactado el articulado definitivo del texto." },
          { turn: 13, sender: 5, receiver: 0, flow: 'to_center', isPlenary: false, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#FF5E85', text: "El borrador jurídico está listo para firma de los seis interlocutores en la mesa principal." },
          { turn: 14, sender: 0, receiver: 0, flow: 'from_center', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "PACTO COLECTIVO RATIFICADO: Consenso social cerrado. Estabilidad laboral y operativa asegurada para los tres años." }
        ]
      },

      'socrates_trial_5': {
        id: 'socrates_trial_5',
        code: 'CULTURAL-AA-G2-T1-C1-V10-A16-ES-5',
        title: 'Apología y Juicio a Sócrates (Platón / Litigio Clásico)',
        subtitle: 'Filosofía Dialéctica Clásica · El Examen Mayéutico Frente a la Acusación de la Polis',
        groupCenterName: 'TRIBUNAL DE ATENAS',
        unitSymbol: '🏛️',
        unitName: 'votos',
        investmentLabel: 'ALEGATOS',
        dividendLabel: 'RÉPLICAS',
        resourceLabel: 'INFLUENCIA',
        actors: [
          { id: '1', name: 'Sócrates (Filósofo)', role: 'Acusado / Defensa', bando: 'A', color: '#00FF87' },
          { id: '2', name: 'Critón (Garante)', role: 'Discípulo Defensor', bando: 'A', color: '#38BDF8' },
          { id: '3', name: 'Meleto (Poeta)', role: 'Acusador Principal', bando: 'B', color: '#FF007F' },
          { id: '4', name: 'Anito (Político)', role: 'Tradicionalista', bando: 'B', color: '#FB923C' },
          { id: '5', name: 'Licón (Orador)', role: 'Retórico Acusador', bando: 'B', color: '#FCD34D' }
        ],
        turns: [
          { turn: 1, sender: 0, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Atenienses: no sé qué impresión habrán dejado en vosotros mis acusadores; mas yo casi me desconocí por su elocuencia." },
          { turn: 2, sender: 2, receiver: 0, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "Sócrates, te acusamos formalmente de corromper a los jóvenes y de no creer en los dioses que la ciudad reconoce." },
          { turn: 3, sender: 0, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['+','+','-','+'], q81: '<Er>', color: '#00FF87', text: "Acércate, Meleto, y respóndeme ante el jurado: ¿dices que corrompo a la juventud de modo voluntario o involuntario?" },
          { turn: 4, sender: 2, receiver: 0, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['-','+','-','+'], q81: '[Er>', color: '#FF007F', text: "¡Afirmo categóricamente que lo haces con plena voluntad y malicia para socavar las costumbres de Atenas!" },
          { turn: 5, sender: 0, receiver: 2, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Nadie daña voluntariamente a quienes le rodean, pues recibiría daño a cambio. Si yerro, la ley exige educar, no castigar." },
          { turn: 6, sender: 3, receiver: 0, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FB923C', text: "Tus sutilezas verbales no te salvarán, Sócrates. Tus discípulos cuestionan las jerarquías de nuestros antepasados." },
          { turn: 7, sender: 1, receiver: 3, flow: 'peer', isPlenary: false, actType: 'iniciativa', recType: 'feedback', tetra: ['+','+','0','+'], q81: '<Ee!', color: '#38BDF8', text: "Anito, jamás cobró una moneda ni fundó escuela privada alguna. Su pobreza voluntaria es testimonio público visible." },
          { turn: 8, sender: 4, receiver: 1, flow: 'peer', isPlenary: false, actType: 'respuesta', recType: 'provocacion', tetra: ['0','0','-','0'], q81: '¡?r!', color: '#FCD34D', text: "La pobreza no exime de la ley. La asamblea soberana juzgará la lealtad a los dioses patrios de la polis." },
          { turn: 9, sender: 0, receiver: 0, flow: 'silence', isPlenary: true, actType: 'iniciativa', recType: 'feedback', tetra: ['0','0','0','0'], q81: '¡¿?!', color: '#FFE600', text: "Murmullos en el tribunal de los quinientos. Los heliastas deliberan en sus bancadas mientras caen los granos de la clepsidra." },
          { turn: 10, sender: 0, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'iniciativa', recType: 'provocacion', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Una vida sin examen no merece ser vivida. Soy el tábano que el dios ha colocado sobre el noble caballo de la ciudad." },
          { turn: 11, sender: 2, receiver: 0, flow: 'to_center', isPlenary: true, actType: 'respuesta', recType: 'provocacion', tetra: ['-','-','-','-'], q81: '[Rr]', color: '#FF007F', text: "¡El tribunal exige que propongas tu propia pena alternativa si no aceptas el destierro perpetuo!" },
          { turn: 12, sender: 0, receiver: 0, flow: 'from_center', isPlenary: true, actType: 'respuesta', recType: 'feedback', tetra: ['+','+','+','+'], q81: '<Ee>', color: '#00FF87', text: "Si propongo lo que en justicia merezco por consagrar mi vida a Atenas, pido ser alimentado en el Pritaneo." }
        ]
      }
    };

    /* ESTADO DEL SISTEMA */
    let activeCorpus = CANONICAL_CORPORA['dawes_orbell_5'];
    let currentN = activeCorpus.actors.length;
    let actors = activeCorpus.actors;
    let TURNS = activeCorpus.turns;
    let currentTurnIndex = 0;
    let isPlaying = false;
    let playInterval = null;
    let playbackSpeed = 1.0;
    let sfxEnabled = true;
    let voiceEnabled = false;

    // Disposición y UI
    let layoutMode = 'split'; 
    let isRuedoOnRight = true;
    let sweepAngle = 0;
    let vortexAngle = 0;
    let radarAnimFrame = null;
    let audioCtx = null;

    // Contadores dinámicos universales
    let emitInic = [];
    let emitResp = [];
    let emitCounts = [];
    let emitPos = [];
    let emitNeg = [];
    let recProv = [];
    let recResp = [];
    let recCounts = [];
    let recPos = [];
    let recNeg = [];
    let cellInteractions = [];

    // Balances de recursos universales
    let userAportes = [];
    let userRetornos = [];
    let userCarteras = [];

    /* =========================================================================
       MODAL INGESTOR Y CARGA UNIVERSAL DE CORPORA
       ========================================================================= */
    function openScriptIngestorModal() {
      const modal = document.getElementById('modalScriptIngestor');
      if (modal) {
        modal.classList.add('open');
        // Sincronizar pestaña JSON con el corpus activo
        const txtJson = document.getElementById('txtJsonCorpus');
        if (txtJson) txtJson.value = JSON.stringify(activeCorpus, null, 2);
      }
    }

    function closeScriptIngestorModal() {
      const modal = document.getElementById('modalScriptIngestor');
      if (modal) modal.classList.remove('open');
    }

    function switchIngestorTab(tabName) {
      document.querySelectorAll('.modal-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

      if (tabName === 'library') {
        document.getElementById('tabBtnLibrary')?.classList.add('active');
        document.getElementById('tabContentLibrary')?.classList.add('active');
      } else if (tabName === 'text') {
        document.getElementById('tabBtnText')?.classList.add('active');
        document.getElementById('tabContentText')?.classList.add('active');
      } else if (tabName === 'json') {
        document.getElementById('tabBtnJson')?.classList.add('active');
        document.getElementById('tabContentJson')?.classList.add('active');
        const txtJson = document.getElementById('txtJsonCorpus');
        if (txtJson) txtJson.value = JSON.stringify(activeCorpus, null, 2);
      }
    }

    function onSelectCorpusPreset(key) {
      if (CANONICAL_CORPORA[key]) {
        loadCorpus(CANONICAL_CORPORA[key]);
      }
    }

    function loadCanonicalCorpus(key) {
      if (CANONICAL_CORPORA[key]) {
        const sel = document.getElementById('selCorpusPreset');
        if (sel) sel.value = key;
        loadCorpus(CANONICAL_CORPORA[key]);
        closeScriptIngestorModal();
      }
    }

    function loadCorpus(corpusObj) {
      pause();
      activeCorpus = corpusObj;
      currentN = corpusObj.actors.length;
      actors = corpusObj.actors;
      TURNS = corpusObj.turns;
      currentTurnIndex = 0;

      // Actualizar cabecera institucional
      const hdrCode = document.getElementById('hdrCorpusCode');
      if (hdrCode) {
        hdrCode.innerText = `· ${corpusObj.code || 'CULTURAL-AA-G2-T1-C1-V10-A16-ES-' + currentN} · 25 de Septiembre de 2026`;
      }

      // Actualizar select si coincide
      const sel = document.getElementById('selCorpusPreset');
      if (sel && CANONICAL_CORPORA[corpusObj.id]) {
        sel.value = corpusObj.id;
      }

      // Actualizar etiquetas en la macro telemetría y tablas
      const bLbl = document.getElementById('liveBoteLbl');
      if (bLbl) bLbl.innerText = `${corpusObj.unitSymbol || '🪙'} ${corpusObj.groupCenterName || 'FONDO'}`;
      
      const bSub = document.getElementById('liveBoteSub');
      if (bSub) bSub.innerText = corpusObj.groupCenterName || 'FONDO COLECTIVO';

      const thAporte = document.getElementById('liveThAporte');
      if (thAporte) thAporte.innerText = corpusObj.investmentLabel || 'APORTE';

      const thRetorno = document.getElementById('liveThRetorno');
      if (thRetorno) thRetorno.innerText = corpusObj.dividendLabel || 'RETORNO';

      const thCartera = document.getElementById('liveThCartera');
      if (thCartera) thCartera.innerText = corpusObj.resourceLabel || 'CARTERA';

      const wAporteL = document.getElementById('wingHdrAporteL');
      if (wAporteL) wAporteL.innerText = corpusObj.investmentLabel || 'APORTE';
      const wCarteraL = document.getElementById('wingHdrCarteraL');
      if (wCarteraL) wCarteraL.innerText = corpusObj.resourceLabel || 'CARTERA';

      const wAporteR = document.getElementById('wingHdrAporteR');
      if (wAporteR) wAporteR.innerText = corpusObj.investmentLabel || 'APORTE';
      const wCarteraR = document.getElementById('wingHdrCarteraR');
      if (wCarteraR) wCarteraR.innerText = corpusObj.resourceLabel || 'CARTERA';

      // Scrubber límites
      const sl = document.getElementById('scrubberSlider');
      if (sl) {
        sl.min = 1;
        sl.max = TURNS.length;
        sl.value = 1;
      }

      // Sincronizar botones N rápidos si aplican
      document.querySelectorAll('.n-btn').forEach(b => b.classList.remove('active'));
      if (currentN === 5) document.getElementById('hdrBtnN5')?.classList.add('active');
      else if (currentN === 8) document.getElementById('hdrBtnN8')?.classList.add('active');
      else if (currentN === 12) document.getElementById('hdrBtnN12')?.classList.add('active');

      buildGrid(currentN);
      renderTurn(0);
      drawVectors(TURNS[0]);

      // Mensaje de éxito
      const msg = document.getElementById('modalStatusMsg');
      if (msg) msg.innerText = `Corpus "${corpusObj.title}" cargado con éxito (${TURNS.length} turnos, N=${currentN}).`;
    }

    /* =========================================================================
       SMART SCRIPT PARSER: PROCESADOR INTELIGENTE DE TEXTO LIBRE
       ========================================================================= */
    function parseCustomTextScript(rawText) {
      const lines = rawText.split('\n').map(l => l.trim()).filter(l => l.length > 0);
      let title = "Observación Procesual de Texto";
      let subtitle = "Corpus de Diálogo Dinámico";
      let groupCenterName = "ESPACIO PLENARIO / CENTRO";
      let declaredActors = [];
      let parsedTurns = [];

      // Diccionario de polaridad léxica para inferir SMIb y Q81
      const posWords = ['acuerdo','apoyo','cooperar','cohesión','pacto','sí','bien','solución','verdad','madurez','consenso','paz','compromiso','legítimo','excelente','correcto','confianza','óbice','viable','salud','respeto'];
      const negWords = ['no','mentira','trampa','fraude','polizón','deserción','rechazo','ruina','sangría','estafa','asesino','criminal','malo','odio','daño','violencia','furia','prejuicio','culpable','huelga','ruptura','amenaza'];

      // 1. Lectura de metadatos o cabecera
      const dialogLines = [];
      for (const line of lines) {
        if (line.startsWith('#')) {
          const lower = line.toLowerCase();
          if (lower.startsWith('# titulo:') || lower.startsWith('# título:')) {
            title = line.split(':')[1].trim();
          } else if (lower.startsWith('# subtitulo:') || lower.startsWith('# subtítulo:')) {
            subtitle = line.split(':')[1].trim();
          } else if (lower.startsWith('# centro:')) {
            groupCenterName = line.split(':')[1].trim().toUpperCase();
          } else if (lower.startsWith('# participantes:') || lower.startsWith('# sujetos:')) {
            const rawAct = line.split(':')[1].trim();
            // Formato: 1:Ana, 2:Bruno | 3:Carlos, 4:Diana
            const parts = rawAct.replace(/\|/g, ',').split(',');
            parts.forEach((p, idx) => {
              const segs = p.trim().split(':');
              if (segs.length >= 2) {
                declaredActors.push({ id: segs[0].trim(), name: segs[1].trim() });
              } else if (segs[0].trim().length > 0) {
                declaredActors.push({ id: String(idx + 1), name: segs[0].trim() });
              }
            });
          }
        } else {
          dialogLines.push(line);
        }
      }

      // 2. Extraer oradores dinámicamente si no fueron declarados
      const speakerSet = new Map();
      if (declaredActors.length > 0) {
        declaredActors.forEach(a => speakerSet.set(a.name.toLowerCase(), a));
      }

      const standardRegex = /^([^:->\[\]]+?)(?:\s*(?:->|a)\s*([^:]+?))?:\s*(.+)$/i;
      const silenceRegex = /^\[silencio\]:?\s*(.+)$/i;
      const silenceRegex2 = /^silencio:?\s*(.+)$/i;

      // Primer barrido para registrar nombres
      for (const dl of dialogLines) {
        if (silenceRegex.test(dl) || silenceRegex2.test(dl)) continue;
        const m = dl.match(standardRegex);
        if (m) {
          const sRaw = m[1].trim();
          const rRaw = m[2] ? m[2].trim() : null;
          if (sRaw.toLowerCase() !== 'centro' && !speakerSet.has(sRaw.toLowerCase())) {
            speakerSet.set(sRaw.toLowerCase(), { id: String(speakerSet.size + 1), name: sRaw });
          }
          if (rRaw && rRaw.toLowerCase() !== 'centro' && !speakerSet.has(rRaw.toLowerCase())) {
            speakerSet.set(rRaw.toLowerCase(), { id: String(speakerSet.size + 1), name: rRaw });
          }
        }
      }

      // Si no se detectaron oradores, crear 4 por defecto
      if (speakerSet.size === 0) {
        speakerSet.set('1', { id: '1', name: '1A (Interlocutor 1)' });
        speakerSet.set('2', { id: '2', name: '2A (Interlocutor 2)' });
        speakerSet.set('3', { id: '3', name: '3B (Interlocutor 3)' });
        speakerSet.set('4', { id: '4', name: '4B (Interlocutor 4)' });
      }

      const actorList = Array.from(speakerSet.values());
      const nTotal = actorList.length;
      const nLeft = Math.ceil(nTotal / 2);

      const colorPalette = ['#00FF87', '#38BDF8', '#34D399', '#00F0FF', '#FF007F', '#FB923C', '#FCD34D', '#F43F5E', '#A855F7', '#818CF8', '#E879F9', '#38BDF8'];

      actorList.forEach((act, idx) => {
        act.bando = (idx < nLeft) ? 'A' : 'B';
        act.color = colorPalette[idx % colorPalette.length];
        act.role = (idx === 0) ? 'Iniciador Principal' : (idx < nLeft ? 'Bando A' : 'Bando B');
      });

      const getActorIndex = (str) => {
        if (!str) return 0;
        const clean = str.trim().toLowerCase();
        for (let i = 0; i < actorList.length; i++) {
          if (actorList[i].name.toLowerCase() === clean || actorList[i].id.toLowerCase() === clean) {
            return i;
          }
        }
        return 0;
      };

      // 3. Procesar turnos con inferencia de funciones Dador / Receptor
      let lastSender = -1;
      let lastReceiver = -1;
      let lastTurnObj = null;

      for (let i = 0; i < dialogLines.length; i++) {
        const line = dialogLines[i];
        let turnObj = null;

        // Silencio
        const mSil1 = line.match(silenceRegex);
        const mSil2 = line.match(silenceRegex2);
        if (mSil1 || mSil2) {
          const txt = (mSil1 ? mSil1[1] : mSil2[1]).trim();
          turnObj = {
            turn: i + 1,
            sender: lastSender >= 0 ? lastSender : 0,
            receiver: lastReceiver >= 0 ? lastReceiver : 0,
            flow: 'silence',
            isPlenary: true,
            actType: 'respuesta',
            recType: 'feedback',
            tetra: ['0','0','0','0'],
            q81: '¡¿?!',
            color: '#FFE600',
            text: txt
          };
          parsedTurns.push(turnObj);
          continue;
        }

        // Diálogo estándar
        const m = line.match(standardRegex);
        if (m) {
          const sRaw = m[1].trim();
          const rRaw = m[2] ? m[2].trim() : null;
          const txt = m[3].trim();

          const isCenterSender = (sRaw.toLowerCase() === 'centro');
          const isCenterRec = (!rRaw || rRaw.toLowerCase() === 'centro' || rRaw.toLowerCase() === 'todos' || rRaw.toLowerCase() === 'grupo');

          const sIdx = isCenterSender ? 0 : getActorIndex(sRaw);
          const rIdx = isCenterRec ? 0 : getActorIndex(rRaw);

          let flow = 'peer';
          if (isCenterSender) flow = 'from_center';
          else if (isCenterRec) flow = 'to_center';

          // Inferencia Canónica Dador: ¿Iniciativa o Respuesta?
          // Regla Operacional: Un sujeto actúa en Respuesta si y solo si su intervención sucede
          // inmediatamente después de recibir una interacción en el turno inmediatamente anterior t-1.
          let actType = 'iniciativa';
          if (i > 0 && lastTurnObj && lastTurnObj.flow !== 'silence') {
            if (lastTurnObj.isPlenary || lastTurnObj.flow === 'to_center') {
              if (lastSender !== sIdx) {
                actType = 'respuesta';
              }
            } else if (lastReceiver === sIdx && lastSender !== sIdx) {
              actType = 'respuesta';
            }
          }

          // Inferencia Canónica Receptor: ¿Provocación/Interpelación o Feedback/Réplica?
          let recType = (i > 0 && lastTurnObj && lastTurnObj.flow !== 'silence' && lastSender === rIdx && lastSender !== sIdx) ? 'feedback' : 'provocacion';

          // Inferencia de tono y Q81
          const lowerTxt = txt.toLowerCase();
          let pCount = 0;
          let nCount = 0;
          posWords.forEach(w => { if (lowerTxt.includes(w)) pCount++; });
          negWords.forEach(w => { if (lowerTxt.includes(w)) nCount++; });

          let tetra = ['0','0','0','0'];
          let q81 = '¡¿?!';
          let color = '#FFE600';

          if (pCount > nCount) {
            tetra = ['+','+','+','+'];
            q81 = (pCount >= 2) ? '<Ee>' : '(Ee>';
            color = (pCount >= 2) ? '#00FF87' : '#38BDF8';
          } else if (nCount > pCount) {
            tetra = ['-','-','-','-'];
            q81 = (nCount >= 2) ? '[Rr]' : '[Er>';
            color = (nCount >= 2) ? '#FF007F' : '#FF9F1C';
          } else {
            tetra = ['0','+','0','+'];
            q81 = '<Ee!';
            color = '#38BDF8';
          }

          turnObj = {
            turn: i + 1,
            sender: sIdx,
            receiver: rIdx,
            flow: flow,
            isPlenary: isCenterRec || isCenterSender,
            actType: actType,
            recType: recType,
            tetra: tetra,
            q81: q81,
            color: color,
            text: txt
          };

          lastSender = sIdx;
          lastReceiver = rIdx;
          lastTurnObj = turnObj;
          parsedTurns.push(turnObj);
        }
      }

      if (parsedTurns.length === 0) {
        parsedTurns = CANONICAL_CORPORA['dawes_orbell_5'].turns;
      }

      return {
        id: 'custom_' + Date.now(),
        code: `CULTURAL-AA-G2-T1-C1-V10-A16-ES-${actorList.length}`,
        title: title,
        subtitle: subtitle,
        groupCenterName: groupCenterName,
        unitSymbol: '🪙',
        unitName: 'puntos',
        investmentLabel: 'APORTE',
        dividendLabel: 'RETORNO',
        resourceLabel: 'CARTERA',
        actors: actorList,
        turns: parsedTurns
      };
    }

    function processCustomPastedText() {
      const txt = document.getElementById('txtCustomScript').value;
      if (!txt || txt.trim().length === 0) {
        alert("Por favor, pegue un guion o texto procesual en el área de texto.");
        return;
      }
      try {
        const parsedCorpus = parseCustomTextScript(txt);
        loadCorpus(parsedCorpus);
        closeScriptIngestorModal();
      } catch (e) {
        alert("Error al procesar el texto: " + e.message);
      }
    }

    function loadCorpusFromJsonInput() {
      const jsonStr = document.getElementById('txtJsonCorpus').value;
      try {
        const obj = JSON.parse(jsonStr);
        if (!obj.actors || !obj.turns) {
          alert("El JSON debe contener las propiedades 'actors' y 'turns'.");
          return;
        }
        loadCorpus(obj);
        closeScriptIngestorModal();
      } catch (e) {
        alert("Error de sintaxis JSON: " + e.message);
      }
    }

    function downloadCurrentCorpusJson() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(activeCorpus, null, 2));
      const dlAnchor = document.createElement('a');
      dlAnchor.setAttribute("href", dataStr);
      dlAnchor.setAttribute("download", `${activeCorpus.id || 'corpus_visord'}.json`);
      document.body.appendChild(dlAnchor);
      dlAnchor.click();
      dlAnchor.remove();
    }

    function copyJsonToClipboard() {
      const txt = document.getElementById('txtJsonCorpus');
      if (txt) {
        txt.select();
        navigator.clipboard.writeText(txt.value).then(() => {
          const msg = document.getElementById('modalStatusMsg');
          if (msg) msg.innerText = "¡JSON copiado al portapapeles con éxito!";
        });
      }
    }

    function insertSampleScript(type) {
      const area = document.getElementById('txtCustomScript');
      if (!area) return;

      if (type === 'deliberacion') {
        area.value = `# Titulo: Deliberación del Comité de Dirección
# Subtitulo: Plan de Expansión Estratégica
# Centro: CONSEJO DE ADMINISTRACIÓN
# Participantes: 1:CEO (Elena), 2:CFO (Marcos) | 3:CTO (Lucía), 4:COO (David)

1: Señores, propongo adelantar el lanzamiento de la nueva plataforma a noviembre.
2 -> 1: La tesorería está tensionada por los costes del servidor cloud; requeriría póliza de crédito.
3 -> 2: Si recortamos el alcance del módulo de analítica predictiva, los costes de cómputo caen un 40%.
[silencio]: El consejo examina los gráficos de flujo de caja y balances proyectados.
4 -> 3: De acuerdo, Lucía. Operaciones asume el despliegue con esa versión acotada.
1: Excelente. Hay consenso operativo. Cerramos el acuerdo por unanimidad.`;
      } else if (type === 'negociacion') {
        area.value = `# Titulo: Mediación de Conflicto Vecinal
# Subtitulo: Uso de Espacios Comunes
# Centro: ASAMBLEA GENERAL
# Participantes: 1:Portavoz A (Rosa), 2:Vecino 2 (Juan) | 3:Portavoz B (Pedro), 4:Vecina 4 (Carmen)

1 -> 3: Pedro, los ruidos en la terraza común hasta las dos de la madrugada son intolerables.
3 -> 1: Rosa, la terraza es comunitaria y en verano los jóvenes tienen derecho a reunirse.
2 -> 3: El derecho al descanso entre semana está recogido en los estatutos de la finca.
[silencio]: Pausa de reflexión y consulta de los estatutos de la comunidad.
4 -> 1: Propongo horario límite a las 23:00 de domingo a jueves y a la 01:00 los fines de semana.
1 -> 4: Aceptamos esa propuesta de consenso y retiramos la queja formal.`;
      } else if (type === 'litigio') {
        area.value = `# Titulo: Sesión de Prueba Pericial
# Subtitulo: Litigio por Patente Industrial
# Centro: TRIBUNAL MERCANTIL
# Participantes: 1:Letrado Actor (Gómez), 2:Perito Actor (Dr. Sanz) | 3:Letrado Demandado (López), 4:Perito Demandado (Ing. Vega)

1 -> Centro: Ilustrísima, acreditamos que el diseño del motor reproduce nuestra patente registrada.
3 -> 1: Su patente reivindica un rotor cilíndrico, mientras que el nuestro es helicoidal asimétrico.
2 -> 3: La función técnica termodinámica es idéntica con independencia de la curvatura.
[silencio]: El magistrado y los asesores examinan los planos en la mesa judicial.
4 -> 2: El rendimiento volumétrico y el flujo de admisión demuestran una solución inventiva distinta.
Centro -> 1: El tribunal admite las dos periciales y suspende la vista para deliberación.`;
      }
    }

    /* =========================================================================
       DISPOSICIÓN, MODOS Y CAJÓN DE CONTABILIDAD EN SEGUNDO PLANO
       ========================================================================= */
    let isDrawerOpen = false;

    function setLayoutMode(mode) {
      layoutMode = mode;
      const grid = document.getElementById('stageGrid');
      const btnRF = document.getElementById('btnModeRuedoFocus');
      const btnS = document.getElementById('btnModeSplit');
      const btnTF = document.getElementById('btnModeTablesFocus');
      const btnRW = document.getElementById('btnModeRuedoWings');

      if (grid) {
        grid.classList.remove('mode-ruedo-focus', 'mode-split', 'mode-tables-focus', 'mode-ruedo', 'mode-matrix');
        if (mode === 'ruedo-focus') grid.classList.add('mode-ruedo-focus');
        else if (mode === 'split') grid.classList.add('mode-split');
        else if (mode === 'tables-focus') grid.classList.add('mode-tables-focus');
        else if (mode === 'ruedo') grid.classList.add('mode-ruedo');
        else if (mode === 'matrix') grid.classList.add('mode-matrix');
      }

      if (btnRF) btnRF.classList.toggle('active', mode === 'ruedo-focus');
      if (btnS) btnS.classList.toggle('active', mode === 'split');
      if (btnTF) btnTF.classList.toggle('active', mode === 'tables-focus');
      if (btnRW) btnRW.classList.toggle('active', mode === 'ruedo');

      // Si se pasa a modo tablas o split, cerrar drawer y devolver panel a stageGrid
      if (mode === 'split' || mode === 'tables-focus') {
        closeTelemetryDrawer();
        const stageGrid = document.getElementById('stageGrid');
        const tablePanel = document.getElementById('stageLiveTablePanel');
        if (stageGrid && tablePanel && !stageGrid.contains(tablePanel)) {
          stageGrid.appendChild(tablePanel);
        }
        if (tablePanel) tablePanel.style.display = 'flex';
      }

      drawVectors(TURNS[currentTurnIndex]);
    }

    function toggleTelemetryDrawer() {
      if (isDrawerOpen) closeTelemetryDrawer();
      else openTelemetryDrawer();
    }

    function openTelemetryDrawer() {
      isDrawerOpen = true;
      const drawer = document.getElementById('telemetryDrawer');
      const btn = document.getElementById('btnToggleBgTables');
      const arrow = document.getElementById('drawerToggleArrow');
      if (drawer) drawer.classList.add('open');
      if (btn) btn.classList.add('active');
      if (arrow) arrow.innerHTML = '<span>▼</span> <span>PLEGAR A SEGUNDO PLANO (T)</span>';

      // Asegurar que el contenido de la tabla esté insertado en el drawer si estamos en modo foco ruedo
      const insertContainer = document.getElementById('drawerTableInsert');
      const tablePanel = document.getElementById('stageLiveTablePanel');
      if (insertContainer && tablePanel && layoutMode === 'ruedo-focus') {
        if (!insertContainer.contains(tablePanel)) {
          insertContainer.appendChild(tablePanel);
          tablePanel.style.display = 'flex';
        }
      }
    }

    function closeTelemetryDrawer() {
      isDrawerOpen = false;
      const drawer = document.getElementById('telemetryDrawer');
      const btn = document.getElementById('btnToggleBgTables');
      const arrow = document.getElementById('drawerToggleArrow');
      if (drawer) drawer.classList.remove('open');
      if (btn) btn.classList.remove('active');
      if (arrow) arrow.innerHTML = '<span>▲</span> <span>DESPLEGAR TABLAS (T)</span>';

      // Si salimos del drawer y estamos en modo split/tables, devolver panel a stageGrid
      const stageGrid = document.getElementById('stageGrid');
      const tablePanel = document.getElementById('stageLiveTablePanel');
      if (stageGrid && tablePanel && (layoutMode === 'split' || layoutMode === 'tables-focus')) {
        if (!stageGrid.contains(tablePanel)) {
          stageGrid.appendChild(tablePanel);
        }
        tablePanel.style.display = 'flex';
      }
    }

    /* =========================================================================
       SISTEMA DE AUDIO SINTETIZADO Y VOZ
       ========================================================================= */
    function initAudio() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function playZapTone(q81) {
      if (!sfxEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        const t = audioCtx.currentTime;
        osc.type = (q81 === '[Rr]') ? 'sawtooth' : 'sine';
        const startFreq = (q81 === '[Rr]') ? 380 : 880;
        osc.frequency.setValueAtTime(startFreq, t);
        osc.frequency.exponentialRampToValueAtTime(140, t + 0.08);
        gain.gain.setValueAtTime(0.12, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.08);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(t);
        osc.stop(t + 0.09);
      } catch (e) {}
    }

    function playAbsorptionTone() {
      if (!sfxEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        const t = audioCtx.currentTime;
        osc.type = 'sine';
        osc.frequency.setValueAtTime(329.63, t);
        osc.frequency.exponentialRampToValueAtTime(523.25, t + 0.15);
        gain.gain.setValueAtTime(0.14, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.22);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(t);
        osc.stop(t + 0.23);
      } catch (e) {}
    }

    function playDischargeTone() {
      if (!sfxEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        const t = audioCtx.currentTime;
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(659.25, t);
        osc.frequency.exponentialRampToValueAtTime(110.0, t + 0.18);
        gain.gain.setValueAtTime(0.16, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.20);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(t);
        osc.stop(t + 0.21);
      } catch (e) {}
    }

    function playVortexTone() {
      if (!sfxEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        const t = audioCtx.currentTime;
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(160, t);
        osc.frequency.linearRampToValueAtTime(80, t + 0.35);
        gain.gain.setValueAtTime(0.08, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.38);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(t);
        osc.stop(t + 0.40);
      } catch (e) {}
    }

    function playAppropriateTone(turn) {
      if (turn.flow === 'silence') playVortexTone();
      else if (turn.flow === 'to_center') playAbsorptionTone();
      else if (turn.flow === 'from_center') playDischargeTone();
      else playZapTone(turn.q81);
    }

    function speakText(text) {
      if (!voiceEnabled || !('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'es-ES';
      u.rate = 1.05;
      window.speechSynthesis.speak(u);
    }

    /* =========================================================================
       CONSTRUCCIÓN DINÁMICA DE ELEMENTOS (RADAR, TABLA Y BURLADEROS)
       ========================================================================= */
    function buildGrid(n) {
      currentN = n;
      const nLeft = Math.ceil(n / 2);
      const nRight = n - nLeft;

      // 1. Mini Sociomatriz y Gran Tabla Cuantitativa
      buildLiveTable(n);

      // 2. Barra Superior Azul (DAN)
      const barBlue = document.getElementById('stageBarBlue');
      if (barBlue) {
        barBlue.innerHTML = '';
        barBlue.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
        for (let j = 0; j < n; j++) {
          const a = actors[j] || { id: String(j + 1), color: '#38BDF8', name: `S${j+1}` };
          const bCell = document.createElement('div');
          bCell.className = 'blue-cell';
          bCell.id = `dan_${j}`;
          bCell.innerHTML = `
            <span style="width:6px; height:6px; border-radius:50%; background:${a.color}; box-shadow:0 0 5px ${a.color};"></span>
            <span class="blue-cell-name" style="color:${a.color};">${a.id}</span>
            <span class="blue-cell-tag">DAN</span>
          `;
          barBlue.appendChild(bCell);
        }
      }

      // 3. Barra Inferior Verde (Bienes Comunes / Aportes)
      const barGreen = document.getElementById('stageBarGreen');
      if (barGreen) {
        barGreen.innerHTML = '';
        barGreen.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
        for (let j = 0; j < n; j++) {
          const gCell = document.createElement('div');
          gCell.className = 'green-cell';
          gCell.id = `fichas_dan_${j}`;
          gCell.innerHTML = `
            <span class="green-cell-fichas" id="val_fichas_${j}">${activeCorpus.unitSymbol || '🪙'} 10</span>
            <span class="green-cell-sub">${activeCorpus.investmentLabel || 'APORTE'}</span>
          `;
          barGreen.appendChild(gCell);
        }
      }

      // 4. Subtítulos dinámicos de los burladeros
      const subL = document.getElementById('wingLeftSub');
      if (subL) subL.innerText = `(SUJETOS 1..${nLeft} · DOBLE CONTABILIDAD)`;
      const subR = document.getElementById('wingRightSub');
      if (subR) subR.innerText = `(SUJETOS ${nLeft + 1}..${n} · DOBLE CONTABILIDAD)`;

      // 5. Burladeros Izquierda (Flanco Izquierdo · Bando A)
      const wingLBody = document.getElementById('wingLeftBody');
      if (wingLBody) {
        wingLBody.innerHTML = '';
        wingLBody.style.gridTemplateRows = `repeat(${nLeft}, 1fr)`;
        for (let i = 0; i < nLeft; i++) {
          const a = actors[i] || { id: String(i + 1), color: '#38BDF8', name: `S${i+1}` };
          const rowEl = document.createElement('div');
          rowEl.className = 'wing-row-left';
          rowEl.id = `wing_row_${i}`;
          rowEl.innerHTML = `
            <div class="wing-cell wcell-id" id="id_subj_${i}" style="color:${a.color};">
              <span class="subj-circle-badge" style="color:${a.color}; border-color:${a.color};">${a.id}</span>
              <span class="subj-name-tag">${a.name}</span>
            </div>
            <div class="wing-cell wcell-rt" id="rt_subj_${i}">⚡ 0</div>
            <div class="wing-cell" id="da_inic_${i}" style="color:#00FF87; font-weight:800;" title="Dador por iniciativa propia">0</div>
            <div class="wing-cell" id="da_resp_${i}" style="color:#38BDF8; font-weight:800;" title="Dador por respuesta a provocación">0</div>
            <div class="wing-cell" id="rc_prov_${i}" style="color:#FF9F1C; font-weight:800;" title="Interpelación o reto recibido">0</div>
            <div class="wing-cell" id="rc_resp_${i}" style="color:#A855F7; font-weight:800;" title="Respuesta o réplica recibida">0</div>
            <div class="wing-cell wcell-saldo" id="bal_subj_${i}">BAL: 0</div>
            <div class="wing-cell wcell-fichas" id="aporte_subj_${i}">10</div>
            <div class="wing-cell" id="cartera_subj_${i}" style="font-size:7.5px; font-weight:800; color:#FFE600;">18.0</div>
            <div class="wing-cell" id="status_subj_${i}"><span class="badge-status status-coop">🟢 COOP</span></div>
          `;
          wingLBody.appendChild(rowEl);
        }
      }

      // 6. Burladeros Derecha (Flanco Derecho · Bando B)
      const wingRBody = document.getElementById('wingRightBody');
      if (wingRBody) {
        wingRBody.innerHTML = '';
        wingRBody.style.gridTemplateRows = `repeat(${nRight}, 1fr)`;
        for (let j = 0; j < nRight; j++) {
          const k = nLeft + j;
          const a = actors[k] || { id: String(k + 1), color: '#FCD34D', name: `S${k+1}` };
          const rowEl = document.createElement('div');
          rowEl.className = 'wing-row-right';
          rowEl.id = `wing_row_${k}`;
          rowEl.innerHTML = `
            <div class="wing-cell wcell-id" id="id_subj_${k}" style="color:${a.color};">
              <span class="subj-circle-badge" style="color:${a.color}; border-color:${a.color};">${a.id}</span>
              <span class="subj-name-tag">${a.name}</span>
            </div>
            <div class="wing-cell wcell-rt" id="rt_subj_${k}">⚡ 0</div>
            <div class="wing-cell" id="da_inic_${k}" style="color:#00FF87; font-weight:800;" title="Dador por iniciativa propia">0</div>
            <div class="wing-cell" id="da_resp_${k}" style="color:#38BDF8; font-weight:800;" title="Dador por respuesta a provocación">0</div>
            <div class="wing-cell" id="rc_prov_${k}" style="color:#FF9F1C; font-weight:800;" title="Interpelación o reto recibido">0</div>
            <div class="wing-cell" id="rc_resp_${k}" style="color:#A855F7; font-weight:800;" title="Respuesta o réplica recibida">0</div>
            <div class="wing-cell wcell-saldo" id="bal_subj_${k}">BAL: 0</div>
            <div class="wing-cell wcell-fichas" id="aporte_subj_${k}">10</div>
            <div class="wing-cell" id="cartera_subj_${k}" style="font-size:7.5px; font-weight:800; color:#FFE600;">18.0</div>
            <div class="wing-cell" id="status_subj_${k}"><span class="badge-status status-coop">🟢 COOP</span></div>
          `;
          wingRBody.appendChild(rowEl);
        }
      }

      // 7. Cuadrilátero Matricial 3x3 Clásico (para modo matrix)
      const matrixGrid = document.getElementById('centerMatrixGrid');
      if (matrixGrid) {
        matrixGrid.innerHTML = '';
        matrixGrid.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
        matrixGrid.style.gridTemplateRows = `repeat(${n}, 1fr)`;

        for (let i = 0; i < n; i++) {
          for (let j = 0; j < n; j++) {
            if (i === j) {
              const diag = document.createElement('div');
              diag.className = 'cell-diagonal-subject';
              diag.id = `diag_cell_${i}`;
              const act = actors[i] || { id: String(i + 1), color: '#38BDF8', name: `S${i+1}` };
              diag.innerHTML = `<div class="presence-point" id="diag_pt_${i}" style="background:${act.color}; color:${act.color};" title="Sujeto ${act.id} (${act.name})"></div>`;
              matrixGrid.appendChild(diag);
            } else {
              const cell = document.createElement('div');
              cell.className = 'cell-center-interaction';
              cell.id = `cell_${i}_${j}`;
              matrixGrid.appendChild(cell);
            }
          }
        }
      }

      renderTurn(currentTurnIndex);
      updatePlayControls(isPlaying);
    }

    function buildLiveTable(n) {
      // 1. Mini Sociomatriz SMIb (N x N)
      const mContainer = document.getElementById('liveMatrixContainer');
      if (mContainer) {
        mContainer.innerHTML = '';
        mContainer.style.gridTemplateColumns = `32px repeat(${n}, 1fr)`;
        
        const cornerCell = document.createElement('div');
        cornerCell.className = 'live-mat-cell hdr';
        cornerCell.innerText = 'R \\ D';
        mContainer.appendChild(cornerCell);

        for (let j = 0; j < n; j++) {
          const colHdr = document.createElement('div');
          colHdr.className = 'live-mat-cell hdr';
          const a = actors[j] || { id: String(j + 1) };
          colHdr.innerText = a.id;
          mContainer.appendChild(colHdr);
        }

        for (let i = 0; i < n; i++) {
          const rowHdr = document.createElement('div');
          rowHdr.className = 'live-mat-cell hdr';
          const a = actors[i] || { id: String(i + 1) };
          rowHdr.innerText = a.id;
          mContainer.appendChild(rowHdr);

          for (let j = 0; j < n; j++) {
            const cell = document.createElement('div');
            cell.className = (i === j) ? 'live-mat-cell diag' : 'live-mat-cell';
            cell.id = `live_mat_${i}_${j}`;
            cell.innerText = '·';
            mContainer.appendChild(cell);
          }
        }
      }

      // 2. Gran Tabla Cuantitativa de Participantes (12 Columnas en 4 Bloques)
      const tBody = document.getElementById('liveTableBody');
      if (tBody) {
        tBody.innerHTML = '';
        for (let k = 0; k < n; k++) {
          const a = actors[k] || { id: String(k + 1), name: `S${k+1}`, color: '#38BDF8' };
          const isBandoA = (k < Math.ceil(n / 2));
          const tr = document.createElement('tr');
          tr.id = `live_row_${k}`;
          tr.innerHTML = `
            <td>
              <span class="subj-circle-badge" style="color:${a.color}; border-color:${a.color}; width:18px; height:18px; font-size:9px;">${a.id}</span>
            </td>
            <td style="color:${a.color}; font-weight:700;">${a.name}</td>
            <td><span class="${isBandoA ? 'badge-bando-a' : 'badge-bando-b'}">${isBandoA ? 'BANDO A' : 'BANDO B'}</span></td>
            <td id="live_da_inic_${k}" class="col-dador" style="color:#00FF87; font-weight:800;">0</td>
            <td id="live_da_resp_${k}" class="col-dador" style="color:#38BDF8; font-weight:800;">0</td>
            <td id="live_aporte_${k}" class="col-dador" style="color:#00FF87; font-weight:800;">10</td>
            <td id="live_rc_prov_${k}" class="col-rec" style="color:#FF9F1C; font-weight:800;">0</td>
            <td id="live_rc_resp_${k}" class="col-rec" style="color:#A855F7; font-weight:800;">0</td>
            <td id="live_retorno_${k}" class="col-rec" style="color:#00FF87; font-weight:800;">18.0</td>
            <td id="live_bal_${k}" class="col-bal" style="font-weight:800;">BAL: 0</td>
            <td id="live_cartera_${k}" class="col-bal" style="color:#FFE600; font-weight:800;">18.0</td>
            <td id="live_status_${k}" class="col-bal" style="font-size:7.5px; font-weight:800; color:#00FF87;">🟢 ÓPTIMO</td>
          `;
          tBody.appendChild(tr);
        }
      }
    }

    function changeN(n) {
      if (activeCorpus.actors.length === n) {
        buildGrid(n);
        return;
      }
      if (n === 5) loadCanonicalCorpus('dawes_orbell_5');
      else if (n === 8) loadCanonicalCorpus('12_angry_men_8');
      else if (n === 6) loadCanonicalCorpus('labor_mediation_6');
      else {
        const genActors = [];
        const pal = ['#00FF87','#38BDF8','#34D399','#00F0FF','#FF007F','#FB923C','#FCD34D','#F43F5E','#A855F7','#818CF8','#E879F9','#38BDF8'];
        const nLeft = Math.ceil(n / 2);
        for (let i = 0; i < n; i++) {
          genActors.push({
            id: String(i + 1),
            name: `${i+1}${i < nLeft ? 'A' : 'B'} (Nodo ${i+1})`,
            role: i < nLeft ? 'Bando A' : 'Bando B',
            bando: i < nLeft ? 'A' : 'B',
            color: pal[i % pal.length]
          });
        }
        activeCorpus = {
          id: `generic_n${n}`,
          code: `CULTURAL-AA-G2-T1-C1-V10-A16-ES-${n}`,
          title: `Escenario Multidimensional (N=${n})`,
          subtitle: `Observación Procesual de ${n} Nodos`,
          groupCenterName: 'PLENARIO',
          unitSymbol: '🪙',
          unitName: 'puntos',
          investmentLabel: 'APORTE',
          dividendLabel: 'RETORNO',
          resourceLabel: 'CARTERA',
          actors: genActors,
          turns: activeCorpus.turns
        };
        loadCorpus(activeCorpus);
      }
    }

    /* =========================================================================
       RENDERIZADO DEL TURNO Y ACTUALIZACIÓN EN TIEMPO REAL
       ========================================================================= */
    function renderTurn(tIdx) {
      if (tIdx < 0 || tIdx >= TURNS.length) return;
      currentTurnIndex = tIdx;
      const turn = TURNS[tIdx];

      const sIdx = turn.sender % currentN;
      const rIdx = turn.receiver % currentN;
      const senderObj = actors[sIdx] || { id: String(sIdx + 1), name: `S${sIdx+1}` };
      const recObj = actors[rIdx] || { id: String(rIdx + 1), name: `S${rIdx+1}` };

      // 1. Teleprompter
      document.getElementById('teleTurn').innerText = `TURNO ${String(turn.turn).padStart(2, '0')} / ${String(TURNS.length).padStart(2, '0')}`;
      
      const sElem = document.getElementById('teleSender');
      const rElem = document.getElementById('teleReceiver');

      if (turn.flow === 'silence') {
        sElem.innerText = `SILENCIO [${senderObj.id}]`;
        sElem.className = 'tele-actor center-hub';
        rElem.innerText = `🌪️ TORBELLINO (${activeCorpus.groupCenterName || 'CENTRO'})`;
        rElem.className = 'tele-actor center-hub';
      } else if (turn.flow === 'to_center') {
        sElem.innerText = senderObj.id;
        sElem.className = 'tele-actor emit';
        rElem.innerText = `${activeCorpus.groupCenterName || 'CENTRO'} (PLENARIO)`;
        rElem.className = 'tele-actor center-hub';
      } else if (turn.flow === 'from_center') {
        sElem.innerText = `${activeCorpus.groupCenterName || 'CENTRO'} (PLENARIO)`;
        sElem.className = 'tele-actor center-hub';
        rElem.innerText = recObj.id;
        rElem.className = 'tele-actor rec';
      } else {
        sElem.innerText = senderObj.id;
        sElem.className = 'tele-actor emit';
        rElem.innerText = recObj.id;
        rElem.className = 'tele-actor rec';
      }

      // Actualización de Badges Operacionales de Interacción (Iniciativa / Respuesta)
      const ex = evaluateTurnExchange(tIdx, TURNS, currentN);
      const roleSendEl = document.getElementById('teleSenderRole');
      if (roleSendEl) {
        if (turn.flow === 'silence') {
          roleSendEl.className = 'tele-role-badge pause';
          roleSendEl.innerText = '⏳ PAUSA';
          roleSendEl.title = 'Silencio / Deliberación colectiva';
        } else if (ex.actType === 'respuesta') {
          roleSendEl.className = 'tele-role-badge resp';
          roleSendEl.innerText = '⚡ DA RESPUESTA';
          roleSendEl.title = 'El sujeto interviene inmediatamente tras recibir una interacción en t-1';
        } else {
          roleSendEl.className = 'tele-role-badge inic';
          roleSendEl.innerText = '⚡ DA INICIATIVA';
          roleSendEl.title = 'El sujeto toma la iniciativa de hablar por sí mismo';
        }
      }

      const roleRecEl = document.getElementById('teleReceiverRole');
      if (roleRecEl) {
        if (turn.flow === 'silence') {
          roleRecEl.className = 'tele-role-badge pause';
          roleRecEl.innerText = '⏳ TORBELLINO';
          roleRecEl.title = 'Silencio reflexivo en el centro de gravedad';
        } else if (ex.recType === 'feedback') {
          roleRecEl.className = 'tele-role-badge repl';
          roleRecEl.innerText = '🛡️ RC RÉPLICA';
          roleRecEl.title = 'El receptor recibe respuesta o feedback a su intervención previa';
        } else {
          roleRecEl.className = 'tele-role-badge prov';
          roleRecEl.innerText = '🛡️ RC INTERPEL';
          roleRecEl.title = 'El receptor recibe un reto o interpelación directa sobrevenida';
        }
      }

      const q81El = document.getElementById('teleQ81');
      q81El.innerText = turn.q81;
      q81El.style.color = turn.color;
      q81El.style.background = `${turn.color}22`;

      document.getElementById('teleText').innerText = `"${turn.text}"`;

      // Scrubber
      const sl = document.getElementById('scrubberSlider');
      if (sl) sl.value = tIdx + 1;
      const slb = document.getElementById('scrubberLabel');
      if (slb) slb.innerText = `${String(tIdx + 1).padStart(2, '0')}/${String(TURNS.length).padStart(2, '0')}`;

      // 2. Acumular y contabilizar interacciones
      recalcCounters(tIdx, turn);

      // 3. Resaltar barra azul superior (DAN) y burladeros
      for (let j = 0; j < currentN; j++) {
        const el = document.getElementById(`dan_${j}`);
        if (el) el.classList.toggle('active-dan', j === sIdx);

        const wingRow = document.getElementById(`wing_row_${j}`);
        if (wingRow) {
          wingRow.classList.remove('active-dan', 'active-rec');
          if (j === sIdx) {
            wingRow.classList.add('active-dan');
          } else if (turn.flow === 'to_center' || turn.isPlenary || j === rIdx) {
            wingRow.classList.add('active-rec');
          }
        }
      }

      // 4. Puntos en la diagonal
      for (let k = 0; k < currentN; k++) {
        const pt = document.getElementById(`diag_pt_${k}`);
        if (pt) {
          if (k === sIdx || (!turn.isPlenary && k === rIdx) || (turn.isPlenary && k !== sIdx)) {
            pt.classList.add('active-actor');
          } else {
            pt.classList.remove('active-actor');
          }
        }
      }

      // 5. Actualizar Gran Tabla Simultánea en Directo y Drawer
      updateLiveTableData(tIdx, turn);

      // Audio & Síntesis de voz
      playAppropriateTone(turn);
      speakText(turn.text);

      // Dibujar vectores / radar
      drawVectors(turn);
    }

    /* =========================================================================
       ACTUALIZACIÓN UNIVERSAL DE LA GRAN TABLA, DRAWER Y BURLADEROS
       ========================================================================= */
    function updateLiveTableData(tIdx, turn) {
      const sym = activeCorpus.unitSymbol || '🪙';

      // A) Macro Telemetría
      let boteTxt = `${sym} ACTIVO`;
      let boteClr = '#00FF87';
      if (activeCorpus.id === 'dawes_orbell_5') {
        boteTxt = (tIdx < 15) ? '🪙 50.0 F' : '🪙 40.0 F (-10 POLIZÓN)';
        boteClr = (tIdx < 15) ? '#00FF87' : '#FF3366';
      } else if (activeCorpus.id === '12_angry_men_8') {
        boteTxt = (tIdx < 10) ? '⚖️ 7-1 (CULPABLE)' : (tIdx < 15 ? '⚖️ 3-5 (EN DUDA)' : '⚖️ 0-8 (NO CULPABLE)');
        boteClr = (tIdx < 10) ? '#FF9F1C' : '#00FF87';
      } else if (activeCorpus.id === 'labor_mediation_6') {
        boteTxt = (tIdx < 7) ? '🤝 EN DISPUTA' : (tIdx < 13 ? '🤝 PREACUERDO' : '🤝 PACTO CERRADO');
        boteClr = (tIdx < 7) ? '#FF9F1C' : '#00FF87';
      }

      const bVal = document.getElementById('liveBoteVal');
      if (bVal) { bVal.innerText = boteTxt; bVal.style.color = boteClr; }
      const drwBVal = document.getElementById('drawerBoteVal');
      if (drwBVal) { drwBVal.innerText = boteTxt; drwBVal.style.color = boteClr; }

      const climaTxt = `${turn.q81} ${turn.tetra.filter(x => x === '+').length >= 2 ? 'COHESIÓN' : (turn.tetra.filter(x => x === '-').length >= 2 ? 'TENSIÓN' : 'EQUILIBRIO')}`;
      const cVal = document.getElementById('liveClimaVal');
      if (cVal) { cVal.innerText = climaTxt; cVal.style.color = turn.color; }
      const drwClima = document.getElementById('drawerClimaVal');
      if (drwClima) { drwClima.innerText = climaTxt; drwClima.style.color = turn.color; }

      const turnTxt = `${String(tIdx + 1).padStart(2, '0')} / ${String(TURNS.length).padStart(2, '0')}`;
      const tVal = document.getElementById('liveTurnVal');
      if (tVal) tVal.innerText = turnTxt;

      const note = document.getElementById('liveStatusNote');
      if (note) {
        if (activeCorpus.id === 'dawes_orbell_5') {
          note.innerText = (tIdx < 15) ? 'UNANIMIDAD COOPERATIVA 100% · ÓPTIMO PARETO' : 'FRACTURA TERMODINÁMICA: POLIZÓN EJECUTADO';
          note.style.color = (tIdx < 15) ? '#00FF87' : '#FF007F';
        } else if (activeCorpus.id === '12_angry_men_8') {
          note.innerText = (tIdx < 4) ? 'DISIDENCIA SOLITARIA: DUDA INICIAL' : (tIdx < 12 ? 'EXAMEN CRÍTICO: GIRO DIALÉCTICO' : 'CONSENSO EN LA DUDA RAZONABLE');
          note.style.color = (tIdx < 12) ? '#38BDF8' : '#00FF87';
        } else {
          note.innerText = `OBSERVACIÓN ACTIVA (${turn.actType.toUpperCase()} / ${turn.recType.toUpperCase()})`;
          note.style.color = '#38BDF8';
        }
      }

      // B) Mini Sociomatriz SMIb
      const sIdx = turn.sender % currentN;
      const rIdx = turn.receiver % currentN;

      for (let i = 0; i < currentN; i++) {
        for (let j = 0; j < currentN; j++) {
          const cell = document.getElementById(`live_mat_${i}_${j}`);
          if (cell) {
            cell.classList.remove('active-pulse');
            if (cellInteractions[i] && cellInteractions[i][j]) {
              cell.innerText = cellInteractions[i][j].q81;
              cell.style.color = cellInteractions[i][j].color;
            }
          }
        }
      }

      if (turn.flow !== 'silence') {
        if (turn.flow === 'to_center' || turn.isPlenary) {
          for (let r = 0; r < currentN; r++) {
            if (r !== sIdx) {
              const activeCell = document.getElementById(`live_mat_${r}_${sIdx}`);
              if (activeCell) activeCell.classList.add('active-pulse');
            }
          }
        } else {
          const activeCell = document.getElementById(`live_mat_${rIdx}_${sIdx}`);
          if (activeCell) activeCell.classList.add('active-pulse');
        }
      }

      // C) Filas de la Gran Tabla Cuantitativa
      for (let k = 0; k < currentN; k++) {
        const tr = document.getElementById(`live_row_${k}`);
        if (tr) {
          tr.classList.remove('active-row-emit', 'active-row-rec', 'defector-row');
          if (k === sIdx) tr.classList.add('active-row-emit');
          if (k === rIdx && turn.flow !== 'to_center') tr.classList.add('active-row-rec');
          if (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) tr.classList.add('defector-row');
        }

        const daInicEl = document.getElementById(`live_da_inic_${k}`);
        if (daInicEl) daInicEl.innerText = emitInic[k];

        const daRespEl = document.getElementById(`live_da_resp_${k}`);
        if (daRespEl) daRespEl.innerText = emitResp[k];

        const rcProvEl = document.getElementById(`live_rc_prov_${k}`);
        if (rcProvEl) rcProvEl.innerText = recProv[k];

        const rcRespEl = document.getElementById(`live_rc_resp_${k}`);
        if (rcRespEl) rcRespEl.innerText = recResp[k];

        const balEl = document.getElementById(`live_bal_${k}`);
        if (balEl) {
          const net = emitCounts[k] - recCounts[k];
          balEl.innerText = `${net >= 0 ? '+' : ''}${net}`;
          balEl.style.color = (net > 0) ? '#00FF87' : (net < 0 ? '#FF5E85' : '#94A3B8');
        }

        const apEl = document.getElementById(`live_aporte_${k}`);
        if (apEl) {
          apEl.innerText = `${sym} ${userAportes[k]}`;
          apEl.style.color = (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) ? '#FF3366' : '#00FF87';
        }

        const retEl = document.getElementById(`live_retorno_${k}`);
        if (retEl) {
          retEl.innerText = `${sym} ${userRetornos[k]}`;
          retEl.style.color = (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) ? '#FF007F' : '#00FF87';
        }

        const cartEl = document.getElementById(`live_cartera_${k}`);
        if (cartEl) {
          cartEl.innerText = `${sym} ${userCarteras[k]}`;
          cartEl.style.color = (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) ? '#00FF87' : '#FFE600';
        }

        const stEl = document.getElementById(`live_status_${k}`);
        if (stEl) {
          stEl.innerHTML = computeDynamicStatusBadge(k, tIdx);
        }
      }

      // D) Métricas termodinámicas universales
      let sdrTxt = '0.840 (ALTA)';
      if (activeCorpus.id === 'dawes_orbell_5') {
        sdrTxt = (tIdx < 15) ? '0.840 (ALTA)' : '0.412 (COLAPSO)';
      } else {
        const ratio = (emitCounts.reduce((a,b)=>a+b, 0) + 1) / (currentN * (currentN - 1) + 1);
        sdrTxt = `${ratio.toFixed(3)} (${ratio > 0.5 ? 'ALTA' : 'ESTABLE'})`;
      }
      const sdrEl = document.getElementById('thermoSDR');
      if (sdrEl) sdrEl.innerText = sdrTxt;
      const drwSdr = document.getElementById('drawerSdrVal');
      if (drwSdr) drwSdr.innerText = sdrTxt.split(' ')[0];

      const posTot = emitPos.reduce((a, b) => a + b, 0);
      const negTot = emitNeg.reduce((a, b) => a + b, 0);

      const tPosEl = document.getElementById('thermoPos');
      if (tPosEl) tPosEl.innerText = `Σ(+): ${posTot}`;
      const tNegEl = document.getElementById('thermoNeg');
      if (tNegEl) tNegEl.innerText = `Σ(-): ${negTot}`;

      const hEl = document.getElementById('thermoHeider');
      if (hEl) {
        const frust = (negTot / (posTot + negTot + 0.01)).toFixed(3);
        hEl.innerText = `${frust} (${frust < 0.3 ? 'ESTABLE' : (frust < 0.7 ? 'TENSA' : 'CRÍTICA')})`;
        hEl.style.color = (frust < 0.3) ? '#00FF87' : (frust < 0.7 ? '#FCD34D' : '#FF007F');
      }

      const tonEl = document.getElementById('thermoTononi');
      if (tonEl) {
        const phi = (1.200 - (negTot * 0.12) + (posTot * 0.08)).toFixed(3);
        tonEl.innerText = `${Math.max(0.1, phi)} Φ (INTEGRACIÓN)`;
        tonEl.style.color = (phi > 0.8) ? '#00FF87' : '#FF5E85';
      }
    }

    /* =========================================================================
       CÁLCULO EXACTO DE CONTADORES Y BALANCES UNIVERSALES
       ========================================================================= */
        /* =========================================================================
       INFERENCIA CANÓNICA DE INTERACCIÓN PROCESUAL
       Regla Operacional Inviolable:
       - Un sujeto actúa en RESPUESTA (DA RESP) si su intervención sucede
         inmediatamente después de recibir una interacción en el turno t-1.
       - En cualquier otro caso, actúa por INICIATIVA propia (DA INIC).
       - Como RECEPTOR: recibe RÉPLICA (RC RESP) si era quien acababa de hablar
         en el turno t-1; de lo contrario recibe INTERPELACIÓN/RETO (RC PROV).
       ========================================================================= */
    function evaluateTurnExchange(i, turns, n) {
      if (!turns || turns.length === 0 || i < 0 || i >= turns.length) {
        return { actType: 'iniciativa', recType: 'provocacion', isResponse: false };
      }
      const curr = turns[i];
      if (curr.flow === 'silence') {
        return { actType: 'iniciativa', recType: 'feedback', isResponse: false, isSilence: true };
      }

      const sCurr = curr.sender % n;
      const rCurr = curr.receiver % n;

      if (i === 0) {
        return {
          actType: 'iniciativa',
          recType: (curr.isPlenary || curr.flow === 'to_center') ? 'provocacion' : 'provocacion',
          isResponse: false
        };
      }

      const prev = turns[i - 1];
      const sPrev = prev.sender % n;
      const rPrev = prev.receiver % n;

      // Criterio Canónico: Un sujeto responde si su intervención sucede inmediatamente
      // después de recibir una interacción en t - 1.
      let receivedImmediate = false;
      if (prev.flow !== 'silence') {
        if (prev.isPlenary || prev.flow === 'to_center') {
          // El turno previo fue un llamamiento a todo el plenario/centro.
          // Todo sujeto en el grupo distinto al emisor previo recibió esa interacción.
          if (sPrev !== sCurr) {
            receivedImmediate = true;
          }
        } else if (prev.flow === 'peer' || prev.flow === 'from_center') {
          // El turno previo fue dirigido específicamente al sujeto actual.
          if (rPrev === sCurr && sPrev !== sCurr) {
            receivedImmediate = true;
          }
        }
      }

      const actType = receivedImmediate ? 'respuesta' : 'iniciativa';

      // Criterio Canónico de Recepción:
      // Si el receptor rCurr fue el emisor en t - 1 (sPrev === rCurr), está recibiendo una RÉPLICA / FEEDBACK.
      // Si rCurr no habló en t - 1, está recibiendo una INTERPELACIÓN / RETO directo sobrevenido.
      let recType = 'provocacion';
      if (prev.flow !== 'silence' && sPrev === rCurr && sPrev !== sCurr) {
        recType = 'feedback';
      }

      return {
        actType: actType,
        recType: recType,
        isResponse: receivedImmediate
      };
    }

    function recalcCounters(tIdx, activeTurn) {
      emitInic = Array(currentN).fill(0);
      emitResp = Array(currentN).fill(0);
      emitCounts = Array(currentN).fill(0);
      emitPos = Array(currentN).fill(0);
      emitNeg = Array(currentN).fill(0);

      recProv = Array(currentN).fill(0);
      recResp = Array(currentN).fill(0);
      recCounts = Array(currentN).fill(0);
      recPos = Array(currentN).fill(0);
      recNeg = Array(currentN).fill(0);

      cellInteractions = Array(currentN).fill(null).map(() => Array(currentN).fill(null));

      for (let i = 0; i <= tIdx; i++) {
        const t = TURNS[i];
        if (t.flow === 'silence') continue; // Pausa reflexiva / deliberación colectiva sin interacción dirigida

        const s = t.sender % currentN;
        const isPos = t.tetra.filter(x => x === '+').length >= 2;
        const isNeg = t.tetra.filter(x => x === '-').length >= 2;
        const ex = evaluateTurnExchange(i, TURNS, currentN);

        emitCounts[s]++;
        if (ex.actType === 'iniciativa') emitInic[s]++;
        else emitResp[s]++;

        if (isPos) emitPos[s]++;
        else if (isNeg) emitNeg[s]++;

        if (t.isPlenary || t.flow === 'to_center') {
          for (let r = 0; r < currentN; r++) {
            if (r !== s) {
              recCounts[r]++;
              // En plenario: si r era el hablante anterior (t-1), recibe réplica; si no, provocación/reto
              const isPrevSpeaker = (i > 0 && TURNS[i - 1].flow !== 'silence' && (TURNS[i - 1].sender % currentN) === r);
              if (isPrevSpeaker) recResp[r]++;
              else recProv[r]++;

              if (isPos) recPos[r]++;
              else if (isNeg) recNeg[r]++;
              cellInteractions[r][s] = t;
            }
          }
        } else {
          const r = t.receiver % currentN;
          recCounts[r]++;
          if (ex.recType === 'provocacion') recProv[r]++;
          else recResp[r]++;

          if (isPos) recPos[r]++;
          else if (isNeg) recNeg[r]++;
          cellInteractions[r][s] = t;
        }
      }

      userAportes = Array(currentN).fill(10);
      userRetornos = Array(currentN).fill(18.0);
      userCarteras = Array(currentN).fill(18.0);

      if (activeCorpus.id === 'dawes_orbell_5') {
        if (tIdx >= 15) {
          userAportes = [10, 10, 10, 10, 0];
          userRetornos = [14.4, 14.4, 14.4, 14.4, 24.4];
          userCarteras = [14.4, 14.4, 14.4, 14.4, 24.4];
        }
      } else {
        for (let k = 0; k < currentN; k++) {
          userAportes[k] = emitCounts[k];
          userRetornos[k] = (recCounts[k] * 1.5).toFixed(1);
          userCarteras[k] = (10 + (emitCounts[k] * 2) - (recNeg[k] * 3)).toFixed(1);
        }
      }

      const sym = activeCorpus.unitSymbol || '🪙';
      for (let k = 0; k < currentN; k++) {
        const daInicEl = document.getElementById(`da_inic_${k}`);
        if (daInicEl) daInicEl.innerText = emitInic[k];

        const daRespEl = document.getElementById(`da_resp_${k}`);
        if (daRespEl) daRespEl.innerText = emitResp[k];

        const rcProvEl = document.getElementById(`rc_prov_${k}`);
        if (rcProvEl) rcProvEl.innerText = recProv[k];

        const rcRespEl = document.getElementById(`rc_resp_${k}`);
        if (rcRespEl) rcRespEl.innerText = recResp[k];

        const rtBadge = document.getElementById(`rt_subj_${k}`);
        if (rtBadge) rtBadge.innerText = `⚡ ${emitCounts[k] + recCounts[k]}`;

        const balEl = document.getElementById(`bal_subj_${k}`);
        if (balEl) {
          const bal = emitCounts[k] - recCounts[k];
          balEl.innerText = `BAL: ${bal >= 0 ? '+' : ''}${bal}`;
          balEl.style.color = bal > 0 ? '#00FF87' : (bal < 0 ? '#FF5E85' : '#94A3B8');
        }

        const apEl = document.getElementById(`aporte_subj_${k}`);
        if (apEl) {
          apEl.innerText = `${sym} ${userAportes[k]}`;
          apEl.style.color = (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) ? '#FF3366' : '#FFE600';
        }

        const fEl = document.getElementById(`cartera_subj_${k}`);
        if (fEl) {
          fEl.innerText = `${sym} ${userCarteras[k]}`;
          fEl.style.color = (activeCorpus.id === 'dawes_orbell_5' && tIdx >= 15 && k === 4) ? '#00FF87' : '#FFE600';
        }

        const statusEl = document.getElementById(`status_subj_${k}`);
        if (statusEl) {
          statusEl.innerHTML = computeDynamicStatusBadge(k, tIdx);
        }

        const fichasEl = document.getElementById(`val_fichas_${k}`);
        if (fichasEl) {
          fichasEl.innerText = `${sym} ${userAportes[k]}`;
        }
      }
    }

    function computeDynamicStatusBadge(k, tIdx) {
      if (activeCorpus.id === 'dawes_orbell_5') {
        if (tIdx >= 15 && k === 4) return '<span class="badge-status status-defector">🚨 POLIZÓN</span>';
        if (tIdx >= 15) return '<span class="badge-status status-warning">⚠️ MERMA</span>';
        if (emitInic[k] >= 2) return '<span class="badge-status status-leader">⭐ LÍDER</span>';
        return '<span class="badge-status status-coop">🟢 COOP</span>';
      }

      if (activeCorpus.id === '12_angry_men_8') {
        if (k === 0) return '<span class="badge-status status-leader">⭐ DISIDENTE</span>';
        if (k === 4 && tIdx >= 14) return '<span class="badge-status status-defector">🚨 AISLADO</span>';
        if (emitCounts[k] >= 3) return '<span class="badge-status status-warning">🔥 ACTIVO</span>';
        if (k >= 4) return '<span class="badge-status status-eq">⚖️ ACUSACIÓN</span>';
        return '<span class="badge-status status-coop">🟢 DUDA</span>';
      }

      if (emitNeg[k] >= 2) return '<span class="badge-status status-defector">🚨 OPOSITOR</span>';
      if (emitInic[k] >= 2 && emitPos[k] >= 1) return '<span class="badge-status status-leader">⭐ LÍDER</span>';
      if (recProv[k] >= 2) return '<span class="badge-status status-warning">🎯 INTERPEL</span>';
      if (emitPos[k] >= 2) return '<span class="badge-status status-coop">🟢 COOP</span>';
      if (emitCounts[k] + recCounts[k] === 0) return '<span class="badge-status status-eq">⏳ SILENTE</span>';
      return '<span class="badge-status status-eq">⚖️ EQUIL</span>';
    }

    /* =========================================================================
       CANVAS Y TRIGONOMETRÍA DEL RUEDO: ANFITEATRO CIRCULAR MAJESTUOSO
       ========================================================================= */
    function getRadarGeometry(W, H, N) {
      const cx = W / 2;
      const cy = H / 2;
      // El radio ocupa el espacio óptimo dejando margen para las etiquetas exteriores
      const R = Math.min(cx - 75, cy - 45);
      const nLeft = Math.ceil(N / 2);
      const nRight = N - nLeft;
      const spanRad = 135 * (Math.PI / 180); // 135 grados de apertura para cada grada

      return { cx, cy, R, nLeft, nRight, spanRad };
    }

    function getRadarCoords(k, W, H, N) {
      const { cx, cy, R, nLeft, nRight, spanRad } = getRadarGeometry(W, H, N);

      if (k < nLeft) {
        // FLANCO IZQUIERDO (BANDO A): Distribuido ordenadamente de arriba a abajo
        const alpha = spanRad * (0.5 - (k + 0.5) / nLeft);
        const x = cx - R * Math.cos(alpha);
        const y = cy - R * Math.sin(alpha);
        return { x, y, side: 'left', localIdx: k, angle: Math.PI - alpha };
      } else {
        // FLANCO DERECHO (BANDO B): Distribuido ordenadamente de arriba a abajo
        const m = k - nLeft;
        const beta = spanRad * (0.5 - (m + 0.5) / nRight);
        const x = cx + R * Math.cos(beta);
        const y = cy - R * Math.sin(beta);
        return { x, y, side: 'right', localIdx: m, angle: beta };
      }
    }

    /* TRANSPONDEDOR RADAR BLIP CON ETIQUETAS SATÉLITE EN EL RUEDO */
    function drawRadarBlipWithSatellite(ctx, x, y, act, isSender, isRec, side, k) {
      ctx.save();
      const radius = currentN > 8 ? 12 : 15;
      const isActive = isSender || isRec;
      const actColor = act ? act.color : '#38BDF8';

      // 1. Halo de activación del nodo
      if (isActive) {
        ctx.beginPath();
        ctx.arc(x, y, radius + 7, 0, Math.PI * 2);
        ctx.strokeStyle = isSender ? '#00FF87' : '#38BDF8';
        ctx.lineWidth = 2.2;
        ctx.shadowColor = isSender ? '#00FF87' : '#38BDF8';
        ctx.shadowBlur = 18;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(x, y, radius + 14, 0, Math.PI * 2);
        ctx.strokeStyle = (isSender ? '#00FF87' : '#38BDF8') + '44';
        ctx.lineWidth = 1.0;
        ctx.setLineDash([3, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // 2. Transpondedor Blip
      ctx.beginPath();
      ctx.arc(x, y, radius, 0, Math.PI * 2);
      ctx.fillStyle = isActive ? 'rgba(15, 23, 42, 0.98)' : 'rgba(8, 14, 34, 0.94)';
      ctx.fill();
      ctx.strokeStyle = isActive ? (isSender ? '#00FF87' : '#FFFFFF') : actColor;
      ctx.lineWidth = isActive ? 2.5 : 1.4;
      ctx.shadowColor = actColor;
      ctx.shadowBlur = isActive ? 14 : 6;
      ctx.stroke();

      // Número / ID del Sujeto
      ctx.font = `900 ${radius > 13 ? '12px' : '10px'} "Roboto Mono", monospace`;
      ctx.fillStyle = isActive ? '#FFFFFF' : actColor;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(act.id, x, y);

      // 3. ETIQUETA SATÉLITE COMPACTA EN EL RUEDO (DATOS EN PRIMER PLANO)
      const isLeft = (side === 'left');
      const tagOffsetX = isLeft ? -22 : 22;
      const tagX = x + tagOffsetX;
      const tagY = y;

      const net = (emitCounts[k] || 0) - (recCounts[k] || 0);
      const netStr = `${net >= 0 ? '+' : ''}${net}`;
      const rtTotal = (emitCounts[k] || 0) + (recCounts[k] || 0);

      ctx.save();
      ctx.textAlign = isLeft ? 'right' : 'left';
      
      // Nombre y Rol
      ctx.font = '800 8.5px "Outfit", sans-serif';
      ctx.fillStyle = '#FFFFFF';
      ctx.shadowColor = 'rgba(0,0,0,0.9)';
      ctx.shadowBlur = 6;
      ctx.fillText(act.name, tagX, tagY - 7);

      // Mini Contadores de Contabilidad en Vivo
      ctx.font = '800 7px "Roboto Mono", monospace';
      ctx.fillStyle = '#94A3B8';
      const statLine = `⚡ ${rtTotal} | BAL: ${netStr} | ${activeCorpus.unitSymbol || '🪙'}${userCarteras[k] || 18}`;
      ctx.fillText(statLine, tagX, tagY + 5);

      // Micro Badge de Bando
      ctx.font = '700 6px "Roboto Mono", monospace';
      ctx.fillStyle = isLeft ? '#00FF87' : '#FCD34D';
      ctx.fillText(isLeft ? '◄ BANDO A' : 'BANDO B ►', tagX, tagY + 14);

      ctx.restore();
      ctx.restore();
    }

    /* NÚCLEO GRUPAL CENTRAL: EL ESPACIO DEL GRUPO GLOBALMENTE CONSIDERADO */
    function drawGroupCenterHub(ctx, cx, cy, statusText, statusColor, isAbsorbing, isEmitting, isVortex, centerRadius = 48) {
      ctx.save();
      const ringR = centerRadius;
      const coreR = Math.round(ringR * 0.54);

      // 1. Área radial de identidad grupal
      const grad = ctx.createRadialGradient(cx, cy, coreR * 0.3, cx, cy, ringR);
      if (isAbsorbing || isEmitting) {
        grad.addColorStop(0, statusColor + '35');
        grad.addColorStop(0.7, statusColor + '16');
        grad.addColorStop(1, 'rgba(8, 16, 36, 0.05)');
      } else if (isVortex) {
        grad.addColorStop(0, 'rgba(255, 230, 0, 0.28)');
        grad.addColorStop(0.7, 'rgba(255, 159, 28, 0.12)');
        grad.addColorStop(1, 'rgba(8, 16, 36, 0.05)');
      } else {
        grad.addColorStop(0, 'rgba(56, 189, 248, 0.20)');
        grad.addColorStop(0.7, 'rgba(15, 28, 62, 0.09)');
        grad.addColorStop(1, 'rgba(8, 16, 36, 0.02)');
      }
      ctx.beginPath();
      ctx.arc(cx, cy, ringR, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();

      // 2. Ondas concéntricas de pulso
      if (isAbsorbing || isEmitting) {
        ctx.beginPath();
        ctx.arc(cx, cy, ringR + 9, 0, Math.PI * 2);
        ctx.strokeStyle = statusColor;
        ctx.lineWidth = 2.4;
        ctx.shadowColor = statusColor;
        ctx.shadowBlur = 20;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(cx, cy, ringR + 20, 0, Math.PI * 2);
        ctx.strokeStyle = statusColor + '66';
        ctx.lineWidth = 1.4;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // 3. Propio Círculo Concéntrico de Identidad
      ctx.beginPath();
      ctx.arc(cx, cy, ringR, 0, Math.PI * 2);
      ctx.strokeStyle = (isAbsorbing || isEmitting) ? statusColor : (isVortex ? '#FFE600' : 'rgba(56, 189, 248, 0.70)');
      ctx.lineWidth = (isAbsorbing || isEmitting) ? 2.4 : (isVortex ? 2.0 : 1.5);
      ctx.shadowColor = (isAbsorbing || isEmitting) ? statusColor : (isVortex ? '#FFE600' : 'rgba(56, 189, 248, 0.5)');
      ctx.shadowBlur = (isAbsorbing || isEmitting) ? 18 : 10;
      ctx.stroke();

      // Pista interior técnica
      ctx.beginPath();
      ctx.arc(cx, cy, ringR - 3.5, 0, Math.PI * 2);
      ctx.strokeStyle = (isAbsorbing || isEmitting) ? statusColor + '66' : (isVortex ? 'rgba(255, 230, 0, 0.4)' : 'rgba(56, 189, 248, 0.3)');
      ctx.lineWidth = 0.9;
      ctx.setLineDash([3, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      // 4. Muescas cardinales de identidad (N, S, E, W)
      const tickLen = 5.0;
      ctx.strokeStyle = (isAbsorbing || isEmitting) ? statusColor : (isVortex ? '#FFE600' : 'rgba(56, 189, 248, 0.8)');
      ctx.lineWidth = 1.4;
      [0, Math.PI * 0.5, Math.PI, Math.PI * 1.5].forEach(ang => {
        ctx.beginPath();
        ctx.moveTo(cx + (ringR - tickLen) * Math.cos(ang), cy + (ringR - tickLen) * Math.sin(ang));
        ctx.lineTo(cx + (ringR + tickLen) * Math.cos(ang), cy + (ringR + tickLen) * Math.sin(ang));
        ctx.stroke();
      });

      // 5. Etiqueta del círculo concéntrico
      ctx.font = '800 7px "Roboto Mono", monospace';
      ctx.fillStyle = (isAbsorbing || isEmitting) ? statusColor : (isVortex ? '#FFE600' : 'rgba(56, 189, 248, 0.85)');
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText(activeCorpus.groupCenterName || 'ESPACIO GRUPAL', cx, cy - ringR - 4);

      if (isVortex) {
        ctx.restore();
        return;
      }

      // 6. Disco Núcleo Interior
      ctx.beginPath();
      ctx.arc(cx, cy, coreR, 0, Math.PI * 2);
      ctx.fillStyle = (isAbsorbing || isEmitting) ? 'rgba(12, 24, 52, 0.98)' : 'rgba(8, 16, 36, 0.94)';
      ctx.fill();
      ctx.strokeStyle = (isAbsorbing || isEmitting) ? statusColor : 'rgba(56, 189, 248, 0.5)';
      ctx.lineWidth = (isAbsorbing || isEmitting) ? 2.2 : 1.3;
      ctx.shadowColor = statusColor;
      ctx.shadowBlur = (isAbsorbing || isEmitting) ? 16 : 8;
      ctx.stroke();

      ctx.font = '900 9px "Roboto Mono", monospace';
      ctx.fillStyle = (isAbsorbing || isEmitting) ? '#FFFFFF' : '#38BDF8';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('GRUPO', cx, cy - 5);

      ctx.font = '700 7px "Outfit", sans-serif';
      ctx.fillStyle = statusColor;
      ctx.fillText(statusText, cx, cy + 6);

      ctx.restore();
    }

    /* TORBELLINO DEL SILENCIO COLECTIVO: LOS SILENCIOS NO DISPARAN RAYOS */
    function drawTorbellino(ctx, cx, cy, angleOffset, centerRadius = 48) {
      ctx.save();
      drawGroupCenterHub(ctx, cx, cy, 'TORBELLINO', '#FFE600', false, false, true, centerRadius);

      const numArms = 4;
      const maxR = Math.round(centerRadius * 1.35);
      for (let a = 0; a < numArms; a++) {
        const baseAngle = (a * Math.PI * 2) / numArms + angleOffset;
        ctx.beginPath();
        for (let step = 0; step < 24; step++) {
          const t = step / 23;
          const r = 5 + t * maxR;
          const theta = baseAngle + t * 2.8;
          const x = cx + r * Math.cos(theta);
          const y = cy + r * Math.sin(theta);
          if (step === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        const armAlpha = 0.25 + 0.35 * Math.sin(angleOffset * 2 + a);
        ctx.strokeStyle = `rgba(255, 230, 0, ${armAlpha})`;
        ctx.lineWidth = 1.8;
        ctx.shadowColor = '#FFE600';
        ctx.shadowBlur = 12;
        ctx.stroke();
      }

      const particleCount = 28;
      for (let i = 0; i < particleCount; i++) {
        const pFrac = i / particleCount;
        const r = 8 + pFrac * maxR;
        const speed = 0.05 / (0.35 + pFrac);
        const pAngle = (i * 0.45 + angleOffset * speed * 25) % (Math.PI * 2);
        const pX = cx + r * Math.cos(pAngle);
        const pY = cy + r * Math.sin(pAngle);
        const pSize = 1.5 + (1 - pFrac) * 2.0;

        ctx.beginPath();
        ctx.arc(pX, pY, pSize, 0, Math.PI * 2);
        ctx.fillStyle = (i % 3 === 0) ? '#00FF87' : ((i % 3 === 1) ? '#FFE600' : '#FF9F1C');
        ctx.shadowColor = '#FFE600';
        ctx.shadowBlur = 8;
        ctx.fill();
      }

      ctx.beginPath();
      ctx.arc(cx, cy, 15, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(5, 9, 20, 0.95)';
      ctx.fill();
      ctx.strokeStyle = '#FFE600';
      ctx.lineWidth = 2.0;
      ctx.shadowColor = '#FFE600';
      ctx.shadowBlur = 16;
      ctx.stroke();

      ctx.font = '900 7.5px "Roboto Mono", monospace';
      ctx.fillStyle = '#FFE600';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('SILENCIO', cx, cy - 2.5);
      ctx.font = '700 6px "Outfit", sans-serif';
      ctx.fillStyle = '#FFFFFF';
      ctx.fillText('TORBELLINO', cx, cy + 5);

      ctx.restore();
    }

    /* MOTOR MAESTRO: RADAR RELACIONAL, NÚCLEO GRUPAL Y RAYOS TÁCTICOS */
    function drawVectors(turn) {
      const cvs = document.getElementById('cuadVectorCanvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      const arena = document.getElementById('stageCenterArena');
      if (!arena) return;

      const rect = arena.getBoundingClientRect();
      if (cvs.width !== rect.width || cvs.height !== rect.height) {
        cvs.width = rect.width;
        cvs.height = rect.height;
      }
      ctx.clearRect(0, 0, cvs.width, cvs.height);

      const W = cvs.width;
      const H = cvs.height;
      const N = currentN;
      const { cx, cy, R } = getRadarGeometry(W, H, N);
      const centerRadius = Math.round(Math.min(52, Math.max(40, R * 0.22)));

      const sIdx = turn ? (turn.sender % N) : 0;
      const rIdx = turn ? (turn.receiver % N) : 0;
      const turnColor = turn ? (turn.color || '#00FF87') : '#00FF87';
      const flow = turn ? (turn.flow || 'peer') : 'peer';

      // =========================================================================
      // DIBUJO DEL RUEDO: ANFITEATRO CIRCULAR MAJESTUOSO
      // =========================================================================
      if (layoutMode !== 'matrix') {
        // 1. Albero / Superficie de la Arena (Fondo Radial Suave)
        ctx.save();
        const alberoGrad = ctx.createRadialGradient(cx, cy, centerRadius, cx, cy, R + 35);
        alberoGrad.addColorStop(0, 'rgba(12, 22, 50, 0.4)');
        alberoGrad.addColorStop(0.7, 'rgba(8, 15, 36, 0.6)');
        alberoGrad.addColorStop(1, 'rgba(4, 8, 20, 0.85)');
        ctx.beginPath();
        ctx.arc(cx, cy, R + 35, 0, Math.PI * 2);
        ctx.fillStyle = alberoGrad;
        ctx.fill();

        // 2. Anillos Concéntricos Técnicos de la Arena (25%, 50%, 75%, 100%)
        [0.25, 0.50, 0.75, 1.0].forEach((pct, idx) => {
          ctx.beginPath();
          ctx.arc(cx, cy, R * pct, 0, Math.PI * 2);
          ctx.strokeStyle = idx === 3 ? 'rgba(56, 189, 248, 0.35)' : 'rgba(56, 189, 248, 0.12)';
          ctx.lineWidth = idx === 3 ? 1.5 : 0.8;
          ctx.setLineDash(idx === 3 ? [] : [3, 5]);
          ctx.stroke();

          ctx.font = '7px "Roboto Mono", monospace';
          ctx.fillStyle = 'rgba(56, 189, 248, 0.35)';
          ctx.textAlign = 'left';
          ctx.textBaseline = 'bottom';
          ctx.fillText(`${Math.round(pct * 100)}%`, cx + 4, cy - R * pct + 9);
        });
        ctx.setLineDash([]);
        ctx.restore();

        // 3. Ejes Cardinales y Marcas Perimetrales
        ctx.save();
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.14)';
        ctx.lineWidth = 0.8;

        ctx.beginPath();
        ctx.moveTo(cx - R, cy);
        ctx.lineTo(cx + R, cy);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(cx, cy - R);
        ctx.lineTo(cx, cy + R);
        ctx.stroke();

        for (let d = 0; d < 360; d += 30) {
          const rad = d * Math.PI / 180;
          const x1 = cx + R * Math.cos(rad);
          const y1 = cy + R * Math.sin(rad);
          const x2 = cx + (R - 6) * Math.cos(rad);
          const y2 = cy + (R - 6) * Math.sin(rad);
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
          ctx.stroke();
        }
        ctx.restore();

        // 4. Haz de Barrido Radar en Tiempo Real
        ctx.save();
        const sweepGradient = ctx.createRadialGradient(cx, cy, 0, cx, cy, R);
        sweepGradient.addColorStop(0, 'rgba(0, 255, 135, 0.0)');
        sweepGradient.addColorStop(1, 'rgba(0, 255, 135, 0.08)');

        const wedgeAngle = 0.35;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.arc(cx, cy, R, sweepAngle - wedgeAngle, sweepAngle, false);
        ctx.closePath();
        ctx.fillStyle = sweepGradient;
        ctx.fill();

        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(cx + R * Math.cos(sweepAngle), cy + R * Math.sin(sweepAngle));
        ctx.strokeStyle = 'rgba(0, 255, 135, 0.40)';
        ctx.lineWidth = 1.2;
        ctx.stroke();
        ctx.restore();

        // 5. GRADAS DEL ANFITEATRO: BANDO A (IZQUIERDA) Y BANDO B (DERECHA)
        const spanRad = 135 * (Math.PI / 180);
        const halfSpan = spanRad / 2;
        const margin = 0.12;

        // A) GRADA IZQUIERDA (FLANCO IZQUIERDO · BANDO A)
        ctx.save();
        const leftStart = Math.PI - halfSpan - margin;
        const leftEnd = Math.PI + halfSpan + margin;

        // Pista exterior curvada del anfiteatro
        ctx.beginPath();
        ctx.arc(cx, cy, R + 18, leftStart, leftEnd, false);
        ctx.strokeStyle = 'rgba(0, 255, 135, 0.55)';
        ctx.lineWidth = 2.0;
        ctx.shadowColor = '#00FF87';
        ctx.shadowBlur = 12;
        ctx.stroke();

        // Pista interior punteada
        ctx.beginPath();
        ctx.arc(cx, cy, R - 18, leftStart, leftEnd, false);
        ctx.strokeStyle = 'rgba(0, 255, 135, 0.22)';
        ctx.lineWidth = 1.0;
        ctx.setLineDash([3, 4]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Relleno suave de la grada
        ctx.beginPath();
        ctx.arc(cx, cy, R + 18, leftStart, leftEnd, false);
        ctx.arc(cx, cy, R - 18, leftEnd, leftStart, true);
        ctx.closePath();
        ctx.fillStyle = 'rgba(0, 255, 135, 0.05)';
        ctx.fill();

        // Banner en el arco
        ctx.font = '900 8px "Roboto Mono", monospace';
        ctx.fillStyle = '#00FF87';
        ctx.textAlign = 'right';
        ctx.fillText('🏛️ FLANCO IZQUIERDO · BANDO A', cx - R - 24, cy - 2);

        // B) GRADA DERECHA (FLANCO DERECHO · BANDO B)
        const rightStart = -halfSpan - margin;
        const rightEnd = halfSpan + margin;

        ctx.beginPath();
        ctx.arc(cx, cy, R + 18, rightStart, rightEnd, false);
        ctx.strokeStyle = 'rgba(245, 205, 83, 0.55)';
        ctx.lineWidth = 2.0;
        ctx.shadowColor = '#FCD34D';
        ctx.shadowBlur = 12;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(cx, cy, R - 18, rightStart, rightEnd, false);
        ctx.strokeStyle = 'rgba(245, 205, 83, 0.22)';
        ctx.lineWidth = 1.0;
        ctx.setLineDash([3, 4]);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.beginPath();
        ctx.arc(cx, cy, R + 18, rightStart, rightEnd, false);
        ctx.arc(cx, cy, R - 18, rightEnd, rightStart, true);
        ctx.closePath();
        ctx.fillStyle = 'rgba(245, 205, 83, 0.05)';
        ctx.fill();

        ctx.font = '900 8px "Roboto Mono", monospace';
        ctx.fillStyle = '#FCD34D';
        ctx.textAlign = 'left';
        ctx.fillText('BANDO B · FLANCO DERECHO 🏛️', cx + R + 24, cy - 2);

        // C) PUERTAS NORTE Y SUR (PUERTA GRANDE DE LA ARENA)
        ctx.font = '800 7px "Roboto Mono", monospace';
        ctx.fillStyle = 'rgba(56, 189, 248, 0.5)';
        ctx.textAlign = 'center';
        ctx.fillText('▲ PUERTA NORTE ▲', cx, cy - R - 24);
        ctx.fillText('▼ PUERTA SUR ▼', cx, cy + R + 32);

        ctx.restore();

        // 6. DIBUJO DE TRANSPONDEDORES BLIP SOBRE LA CIRCUNFERENCIA PERFECTA
        for (let k = 0; k < N; k++) {
          const pt = getRadarCoords(k, W, H, N);
          const act = actors[k % actors.length] || { id: String(k + 1), color: '#38BDF8', name: `S${k+1}` };
          const isSender = (k === sIdx);
          const isRec = (flow === 'from_center' ? (k === rIdx) : (k === rIdx && flow !== 'to_center'));

          drawRadarBlipWithSatellite(ctx, pt.x, pt.y, act, isSender, isRec, pt.side, k);
        }

        // 7. ESPACIO GRUPAL CENTRAL Y RAYOS TÁCTICOS
        const potStatus = `${activeCorpus.unitSymbol || '🪙'} ${activeCorpus.groupCenterName || 'CENTRO'}`;
        if (!turn) {
          drawGroupCenterHub(ctx, cx, cy, potStatus, '#38BDF8', false, false, false, centerRadius);
          return;
        }

        if (flow === 'silence') {
          drawTorbellino(ctx, cx, cy, vortexAngle, centerRadius);
          return;
        }

        if (flow === 'to_center') {
          // El rayo se detiene en el círculo concéntrico de identidad del centro
          const startPt = getRadarCoords(sIdx, W, H, N);
          const dx = cx - startPt.x;
          const dy = cy - startPt.y;
          const dist = Math.hypot(dx, dy);
          const angle = Math.atan2(dy, dx);

          const stopDist = Math.max(0, dist - centerRadius);
          const stopX = startPt.x + (dx / dist) * stopDist;
          const stopY = startPt.y + (dy / dist) * stopDist;

          ctx.save();
          ctx.beginPath();
          ctx.moveTo(startPt.x, startPt.y);
          ctx.lineTo(stopX, stopY);
          ctx.strokeStyle = turnColor;
          ctx.lineWidth = 3.2;
          ctx.shadowColor = turnColor;
          ctx.shadowBlur = 18;
          ctx.stroke();

          ctx.beginPath();
          ctx.moveTo(startPt.x, startPt.y);
          ctx.lineTo(stopX, stopY);
          ctx.strokeStyle = '#FFFFFF';
          ctx.lineWidth = 1.0;
          ctx.stroke();

          const arrowLen = 13;
          const arrowSpread = Math.PI / 6;
          ctx.beginPath();
          ctx.moveTo(stopX, stopY);
          ctx.lineTo(stopX - arrowLen * Math.cos(angle - arrowSpread), stopY - arrowLen * Math.sin(angle - arrowSpread));
          ctx.lineTo(stopX - arrowLen * 0.5 * Math.cos(angle), stopY - arrowLen * 0.5 * Math.sin(angle));
          ctx.lineTo(stopX - arrowLen * Math.cos(angle + arrowSpread), stopY - arrowLen * Math.sin(angle + arrowSpread));
          ctx.closePath();
          ctx.fillStyle = '#FFFFFF';
          ctx.shadowColor = turnColor;
          ctx.shadowBlur = 12;
          ctx.fill();
          ctx.restore();

          drawGroupCenterHub(ctx, cx, cy, activeCorpus.groupCenterName || 'CENTRO', turnColor, true, false, false, centerRadius);
          return;
        }

        if (flow === 'from_center') {
          // El rayo nace en el círculo concéntrico de identidad hacia la periferia
          const targetPt = getRadarCoords(rIdx, W, H, N);
          const dx = targetPt.x - cx;
          const dy = targetPt.y - cy;
          const dist = Math.hypot(dx, dy);
          const angle = Math.atan2(dy, dx);

          const startX = cx + (dx / dist) * centerRadius;
          const startY = cy + (dy / dist) * centerRadius;

          ctx.save();
          ctx.beginPath();
          ctx.moveTo(startX, startY);
          ctx.lineTo(targetPt.x, targetPt.y);
          ctx.strokeStyle = turnColor;
          ctx.lineWidth = 3.2;
          ctx.shadowColor = turnColor;
          ctx.shadowBlur = 18;
          ctx.stroke();

          ctx.beginPath();
          ctx.moveTo(startX, startY);
          ctx.lineTo(targetPt.x, targetPt.y);
          ctx.strokeStyle = '#FFFFFF';
          ctx.lineWidth = 1.0;
          ctx.stroke();

          const arrowLen = 13;
          const arrowSpread = Math.PI / 6;
          const aX = startX + dx * 0.65;
          const aY = startY + dy * 0.65;
          ctx.beginPath();
          ctx.moveTo(aX, aY);
          ctx.lineTo(aX - arrowLen * Math.cos(angle - arrowSpread), aY - arrowLen * Math.sin(angle - arrowSpread));
          ctx.lineTo(aX - arrowLen * 0.5 * Math.cos(angle), aY - arrowLen * 0.5 * Math.sin(angle));
          ctx.lineTo(aX - arrowLen * Math.cos(angle + arrowSpread), aY - arrowLen * Math.sin(angle + arrowSpread));
          ctx.closePath();
          ctx.fillStyle = '#FFFFFF';
          ctx.shadowColor = turnColor;
          ctx.shadowBlur = 10;
          ctx.fill();

          ctx.beginPath();
          ctx.arc(targetPt.x, targetPt.y, 18, 0, Math.PI * 2);
          ctx.strokeStyle = turnColor;
          ctx.lineWidth = 2.0;
          ctx.shadowColor = turnColor;
          ctx.shadowBlur = 16;
          ctx.stroke();
          ctx.restore();

          drawGroupCenterHub(ctx, cx, cy, 'VEREDICTO', turnColor, false, true, false, centerRadius);
          return;
        }

        // Interacción directa diádica entre dos nodos (A -> B)
        const startPt = getRadarCoords(sIdx, W, H, N);
        const endPt = getRadarCoords(rIdx, W, H, N);

        const dx = endPt.x - startPt.x;
        const dy = endPt.y - startPt.y;
        const angle = Math.atan2(dy, dx);

        ctx.save();
        ctx.beginPath();
        ctx.moveTo(startPt.x, startPt.y);
        ctx.lineTo(endPt.x, endPt.y);
        ctx.strokeStyle = turnColor;
        ctx.lineWidth = 3.0;
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 16;
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(startPt.x, startPt.y);
        ctx.lineTo(endPt.x, endPt.y);
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 1.0;
        ctx.stroke();

        const arrowLen = 13;
        const arrowSpread = Math.PI / 6;
        const aX = startPt.x + dx * 0.65;
        const aY = startPt.y + dy * 0.65;
        ctx.beginPath();
        ctx.moveTo(aX, aY);
        ctx.lineTo(aX - arrowLen * Math.cos(angle - arrowSpread), aY - arrowLen * Math.sin(angle - arrowSpread));
        ctx.lineTo(aX - arrowLen * 0.5 * Math.cos(angle), aY - arrowLen * 0.5 * Math.sin(angle));
        ctx.lineTo(aX - arrowLen * Math.cos(angle + arrowSpread), aY - arrowLen * Math.sin(angle + arrowSpread));
        ctx.closePath();
        ctx.fillStyle = '#FFFFFF';
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 10;
        ctx.fill();

        ctx.beginPath();
        ctx.arc(endPt.x, endPt.y, 17, 0, Math.PI * 2);
        ctx.strokeStyle = turnColor;
        ctx.lineWidth = 2.0;
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 14;
        ctx.stroke();
        ctx.restore();

        drawGroupCenterHub(ctx, cx, cy, potStatus, '#38BDF8', false, false, false, centerRadius);
        return;
      }

      // =========================================================================
      // MODO CUADRILÁTERO MATRICIAL 3×3 (DIAGONAL Y ÁNGULO RECTO)
      // =========================================================================
      function getX(k) { return (k + 0.5) * (W / N); }
      function getY(k) { return (k + 0.5) * (H / N); }

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(W, H);
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.20)';
      ctx.lineWidth = 1.2;
      ctx.setLineDash([4, 6]);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.restore();

      for (let k = 0; k < N; k++) {
        const dx = getX(k);
        const dy = getY(k);
        const act = actors[k % actors.length] || { id: String(k + 1), color: '#38BDF8' };
        const isActorActive = (k === turn.sender % N) || (k === turn.receiver % N);

        ctx.save();
        ctx.beginPath();
        ctx.arc(dx, dy, isActorActive ? 4.5 : 2.5, 0, Math.PI * 2);
        ctx.fillStyle = act ? act.color : '#38BDF8';
        if (isActorActive) {
          ctx.shadowColor = act ? act.color : '#38BDF8';
          ctx.shadowBlur = 10;
        }
        ctx.fill();
        ctx.restore();
      }

      function drawDirectedLBeam(targetIdx) {
        if (sIdx === targetIdx) return;
        const xs = getX(sIdx);
        const yr = getY(targetIdx);
        const isResponse = (currentTurnIndex > 0 && turn.sender === TURNS[currentTurnIndex - 1].receiver) || (sIdx > targetIdx);
        const yStart = isResponse ? H : 0;
        const yEnd = yr;
        const xTarget = 0.5 * (W / N);

        ctx.save();
        ctx.beginPath();
        ctx.moveTo(xs, yStart);
        ctx.lineTo(xs, yEnd);
        ctx.strokeStyle = turnColor;
        ctx.lineWidth = 2.2;
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 10;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(xs, yr, 4.5, 0, Math.PI * 2);
        ctx.fillStyle = '#FFFFFF';
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 14;
        ctx.fill();

        ctx.beginPath();
        ctx.moveTo(xs, yr);
        ctx.lineTo(xTarget, yr);
        ctx.strokeStyle = turnColor;
        ctx.lineWidth = 2.2;
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 10;
        ctx.stroke();

        const midX = (xs + xTarget) / 2;
        ctx.beginPath();
        ctx.moveTo(midX - 7, yr);
        ctx.lineTo(midX + 2, yr - 4);
        ctx.lineTo(midX + 2, yr + 4);
        ctx.closePath();
        ctx.fillStyle = '#FFFFFF';
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 8;
        ctx.fill();

        ctx.beginPath();
        ctx.arc(xTarget, yr, 12, 0, Math.PI * 2);
        ctx.strokeStyle = turnColor;
        ctx.lineWidth = 1.8;
        ctx.shadowColor = turnColor;
        ctx.shadowBlur = 14;
        ctx.stroke();
        ctx.restore();
      }

      if (flow !== 'silence') {
        drawDirectedLBeam(rIdx);
      }
    }

    /* =========================================================================
       ANIMACIÓN CONTINUA DEL RADAR Y REPRODUCCIÓN
       ========================================================================= */
    function startRadarAnimation() {
      if (radarAnimFrame) cancelAnimationFrame(radarAnimFrame);

      function radarTick() {
        if (layoutMode !== 'matrix') {
          sweepAngle = (sweepAngle + 0.012) % (Math.PI * 2);
          vortexAngle = (vortexAngle + 0.04) % (Math.PI * 2);
          drawVectors(TURNS[currentTurnIndex]);
        }
        radarAnimFrame = requestAnimationFrame(radarTick);
      }

      radarAnimFrame = requestAnimationFrame(radarTick);
    }

    window.addEventListener('resize', () => {
      drawVectors(TURNS[currentTurnIndex]);
    });

    function updatePlayControls(playing) {
      isPlaying = playing;

      const tIcon = document.getElementById('telePlayIcon');
      const tLabel = document.getElementById('telePlayLabel');
      const tBtn = document.getElementById('btnTeleStart');
      if (tIcon && tLabel && tBtn) {
        if (playing) {
          tIcon.innerText = '⏸';
          tLabel.innerText = 'PAUSAR';
          tBtn.style.color = '#00FF87';
          tBtn.style.borderColor = 'rgba(0, 255, 135, 0.4)';
        } else {
          tIcon.innerText = '▶';
          tLabel.innerText = 'INICIAR';
          tBtn.style.color = '#FFE600';
          tBtn.style.borderColor = 'rgba(255, 230, 0, 0.5)';
        }
      }

      const hText = document.getElementById('hdrPlayText');
      const hDot = document.getElementById('autoPulseIndicator');
      const hPill = document.getElementById('hdrAutoPlayPill');
      if (hText && hDot && hPill) {
        if (playing) {
          hText.innerText = 'RADAR ACTIVO';
          hDot.style.background = '#00FF87';
          hDot.style.boxShadow = '0 0 8px #00FF87';
          hPill.style.color = '#00FF87';
        } else {
          hText.innerText = '▶ INICIAR RADAR';
          hDot.style.background = '#FFE600';
          hDot.style.boxShadow = '0 0 8px #FFE600';
          hPill.style.color = '#FFE600';
        }
      }
    }

    function togglePlay() {
      initAudio();
      if (isPlaying) pause();
      else play();
    }

    function play() {
      if (playInterval) clearInterval(playInterval);
      updatePlayControls(true);
      playInterval = setInterval(() => {
        if (currentTurnIndex < TURNS.length - 1) {
          stepNext();
        } else {
          if (playInterval) clearInterval(playInterval);
          setTimeout(() => {
            if (isPlaying) {
              renderTurn(0);
              play();
            }
          }, 3500);
        }
      }, 2600 / playbackSpeed);
    }

    function pause() {
      if (playInterval) {
        clearInterval(playInterval);
        playInterval = null;
      }
      updatePlayControls(false);
    }

    function stepNext() {
      if (currentTurnIndex < TURNS.length - 1) {
        renderTurn(currentTurnIndex + 1);
      }
    }

    function stepPrev() {
      if (currentTurnIndex > 0) {
        renderTurn(currentTurnIndex - 1);
      }
    }

    function resetDebate() {
      pause();
      renderTurn(0);
    }

    function seekToTurn(val) {
      const idx = parseInt(val, 10) - 1;
      if (idx >= 0 && idx < TURNS.length) {
        renderTurn(idx);
      }
    }

    function toggleSpeed(btn) {
      if (playbackSpeed === 1.0) playbackSpeed = 2.0;
      else if (playbackSpeed === 2.0) playbackSpeed = 0.5;
      else playbackSpeed = 1.0;
      const label = `${playbackSpeed}x`;
      if (btn) btn.innerText = label;
      const teleSpd = document.getElementById('btnSpeedTele');
      if (teleSpd) teleSpd.innerText = label;
      if (isPlaying) { pause(); play(); }
    }

    function toggleSFX() {
      initAudio();
      sfxEnabled = !sfxEnabled;
      const label = sfxEnabled ? '🔊 SFX' : '🔇 OFF';
      const teleSfx = document.getElementById('btnSfxTele');
      if (teleSfx) {
        teleSfx.classList.toggle('active', sfxEnabled);
        teleSfx.innerText = label;
      }
      if (sfxEnabled) playZapTone('<Ee>');
    }

    function toggleVoice() {
      initAudio();
      voiceEnabled = !voiceEnabled;
      const label = voiceEnabled ? '🎙️ VOZ' : '🎙️ OFF';
      const teleVoice = document.getElementById('btnVoiceTele');
      if (teleVoice) {
        teleVoice.classList.toggle('active', voiceEnabled);
        teleVoice.innerText = label;
      }
      if (voiceEnabled) speakText("Observador universal activado.");
    }

    // Teclado: Espacio = Play/Pausa, Flechas = Turnos, Tecla T = Contabilidad en 2º plano
    window.addEventListener('keydown', (e) => {
      if (e.target && (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT')) return;
      if (e.code === 'Space') {
        e.preventDefault();
        togglePlay();
      } else if (e.code === 'ArrowRight') {
        stepNext();
      } else if (e.code === 'ArrowLeft') {
        stepPrev();
      } else if (e.key === 't' || e.key === 'T') {
        e.preventDefault();
        toggleTelemetryDrawer();
      }
    });

    window.addEventListener('click', () => {
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }, { once: false });

    // INICIALIZACIÓN: MODO FOCO RUEDO (TABLAS EN SEGUNDO PLANO) POR DEFECTO
    window.addEventListener('DOMContentLoaded', () => {
      setLayoutMode('ruedo-focus');
      loadCorpus(CANONICAL_CORPORA['dawes_orbell_5']);
      startRadarAnimation();
      setTimeout(() => {
        play();
      }, 500);
    });
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(__file__)
    target_path = os.path.abspath(os.path.join(base_dir, "..", "visord_procesual.html"))
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Updated target script: {target_path}")

    target_path_v = os.path.abspath(os.path.join(base_dir, "..", "VERSION_IMPACTO_VISUAL", "visord_procesual.html"))
    if os.path.exists(os.path.dirname(target_path_v)):
        with open(target_path_v, "w", encoding="utf-8") as f:
            f.write(HTML_CONTENT)
        print(f"Updated target version: {target_path_v}")
    print("Compilación del VISORD PROCESUAL (Observador Universal de Textos) completada con éxito.")

if __name__ == "__main__":
    main()
