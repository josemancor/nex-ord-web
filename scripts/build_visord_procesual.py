#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro de VISORD PROCESUAL:
Laboratorio Experimental de Micro-procesos Comunicacionales y Dilema de Bienes Comunes.
"""

import os
import json

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <title>NEXORD · VISORD PROCESUAL: Laboratorio Experimental de Micro-procesos Comunicacionales</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;600;700;800;900&family=Roboto+Mono:wght@400;500;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-space: #050811;
      --bg-deep: #080D1D;
      --bg-card: rgba(15, 23, 42, 0.88);
      --bg-card-hover: rgba(24, 38, 70, 0.95);
      --bg-glass: rgba(18, 29, 58, 0.75);
      --border-glass: rgba(56, 189, 248, 0.22);
      --border-glow: rgba(0, 255, 135, 0.35);

      --neon-green: #00FF87;
      --neon-cyan: #38BDF8;
      --neon-pink: #FF007F;
      --neon-gold: #FFE600;
      --neon-orange: #FF9F1C;
      --neon-purple: #A855F7;
      --neon-red: #FF3366;

      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      --text-glow: rgba(248, 250, 252, 0.9);

      --zone-1: #00FF87;
      --zone-2: #FFE600;
      --zone-3: #38BDF8;
      --zone-4: #FF007F;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      background-color: var(--bg-space);
      color: var(--text-main);
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
      scroll-behavior: smooth;
    }

    /* CYBERNETIC SCROLLBAR */
    ::-webkit-scrollbar {
      width: 7px;
      height: 7px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(8, 13, 29, 0.95);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(56, 189, 248, 0.45);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--neon-cyan);
    }

    /* INSTITUTIONAL CANONICAL HEADER */
    .app-header {
      background: linear-gradient(180deg, rgba(8, 14, 30, 0.96) 0%, rgba(5, 8, 17, 0.88) 100%);
      border-bottom: 1px solid var(--border-glass);
      backdrop-filter: blur(16px);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6);
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
    }

    .brand-logo {
      height: 38px;
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.5));
      transition: transform 0.25s ease;
    }
    .brand-logo:hover {
      transform: scale(1.05);
    }

    .brand-titles {
      display: flex;
      flex-direction: column;
    }

    .brand-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 900;
      letter-spacing: 1.2px;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-badge {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      background: rgba(0, 255, 135, 0.15);
      color: var(--neon-green);
      border: 1px solid rgba(0, 255, 135, 0.4);
      letter-spacing: 0.5px;
    }

    .brand-canonical-tag {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.73rem;
      color: var(--text-muted);
      margin-top: 1px;
    }
    .brand-canonical-tag span {
      color: var(--neon-cyan);
      font-weight: 600;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .header-btn {
      background: rgba(16, 26, 50, 0.85);
      border: 1px solid var(--border-glass);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      text-decoration: none;
    }
    .header-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--neon-cyan);
      color: #FFF;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }
    .header-btn.active {
      background: rgba(0, 255, 135, 0.2);
      border-color: var(--neon-green);
      color: var(--neon-green);
    }

    /* STEPPER BAR */
    .stepper-nav {
      background: rgba(10, 16, 35, 0.95);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: center;
      padding: 8px 16px;
      gap: 8px;
      position: sticky;
      top: 59px;
      z-index: 990;
      backdrop-filter: blur(10px);
    }

    .step-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 7px 16px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(15, 23, 42, 0.6);
      cursor: pointer;
      transition: all 0.25s ease;
      user-select: none;
    }
    .step-item:hover {
      border-color: rgba(56, 189, 248, 0.4);
      background: rgba(20, 33, 61, 0.8);
      transform: translateY(-1px);
    }
    .step-item.active {
      border-color: var(--neon-green);
      background: rgba(0, 255, 135, 0.12);
      box-shadow: 0 0 14px rgba(0, 255, 135, 0.25);
    }
    .step-item.completed {
      border-color: var(--neon-cyan);
      background: rgba(56, 189, 248, 0.1);
    }

    .step-num {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
    }
    .step-item.active .step-num {
      background: var(--neon-green);
      color: #050811;
      box-shadow: 0 0 8px var(--neon-green);
    }
    .step-item.completed .step-num {
      background: var(--neon-cyan);
      color: #050811;
    }

    .step-title {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.3px;
    }
    .step-item.active .step-title {
      color: #FFFFFF;
    }
    .step-item.completed .step-title {
      color: var(--neon-cyan);
    }

    /* MAIN CONTAINER */
    .main-wrapper {
      max-width: 1480px;
      margin: 0 auto;
      padding: 16px 20px 80px 20px;
    }

    .phase-view {
      display: none;
      animation: fadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .phase-view.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* PHASE 1: PRE-TEST O0 */
    .phase1-grid {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px;
      margin-top: 14px;
    }

    .banner-pretest {
      background: linear-gradient(135deg, rgba(16, 28, 58, 0.9) 0%, rgba(10, 18, 38, 0.95) 100%);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 20px 24px;
      margin-bottom: 20px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
    }
    .banner-pretest h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: #FFF;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .banner-pretest h2 span {
      color: var(--neon-cyan);
    }
    .banner-pretest p {
      font-size: 0.92rem;
      line-height: 1.55;
      color: var(--text-dim);
    }

    .actors-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
    }

    .actor-pre-card {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }
    .actor-pre-card:hover {
      border-color: var(--neon-cyan);
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
    }

    .actor-avatar-lg {
      width: 82px;
      height: 82px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid rgba(56, 189, 248, 0.6);
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.3);
      margin-bottom: 12px;
    }

    .actor-id-badge {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.82rem;
      font-weight: 900;
      padding: 3px 10px;
      border-radius: 6px;
      background: rgba(56, 189, 248, 0.2);
      color: var(--neon-cyan);
      border: 1px solid rgba(56, 189, 248, 0.5);
      margin-bottom: 6px;
    }

    .actor-role-title {
      font-size: 0.88rem;
      font-weight: 700;
      color: #FFF;
      margin-bottom: 4px;
    }

    .actor-role-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.35;
      margin-bottom: 10px;
    }

    .actor-pre-stats {
      width: 100%;
      background: rgba(10, 16, 32, 0.7);
      border-radius: 8px;
      padding: 8px;
      display: flex;
      justify-content: space-around;
      font-size: 0.75rem;
      font-family: 'Roboto Mono', monospace;
    }
    .actor-pre-stats div span {
      display: block;
      color: var(--neon-green);
      font-weight: 700;
      font-size: 0.9rem;
    }

    .pretest-sidebar {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .pretest-sidebar h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: #FFF;
      border-bottom: 1px solid var(--border-glass);
      padding-bottom: 8px;
    }

    .metric-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
      border-bottom: 1px dashed rgba(255, 255, 255, 0.08);
      font-size: 0.84rem;
    }
    .metric-row .val {
      font-family: 'Roboto Mono', monospace;
      font-weight: 700;
      color: var(--neon-green);
    }

    .start-debate-btn {
      background: linear-gradient(135deg, #00FF87 0%, #00B862 100%);
      color: #050811;
      border: none;
      border-radius: 12px;
      padding: 14px 20px;
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.25s ease;
      box-shadow: 0 4px 18px rgba(0, 255, 135, 0.4);
      margin-top: 10px;
      text-decoration: none;
    }
    .start-debate-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(0, 255, 135, 0.6);
      filter: brightness(1.1);
    }

    /* PHASE 2: TELEPROMPTER & INTERACTION MATRIX */
    .teleprompter-card {
      background: linear-gradient(180deg, rgba(16, 26, 52, 0.95) 0%, rgba(10, 16, 32, 0.92) 100%);
      border: 1.5px solid var(--border-glass);
      border-radius: 16px;
      padding: 16px 20px;
      margin-bottom: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      position: relative;
      overflow: hidden;
    }
    .teleprompter-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--neon-cyan), var(--neon-green), var(--neon-gold));
    }

    .teleprompter-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .turn-badge-main {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.86rem;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.18);
      color: var(--neon-cyan);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 4px 12px;
      border-radius: 20px;
    }

    .teleprompter-badges {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .badge-intensity {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
      letter-spacing: 0.3px;
    }
    .intensity-1 {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid var(--neon-cyan);
      color: var(--neon-cyan);
    }
    .intensity-2 {
      background: rgba(0, 255, 135, 0.2);
      border: 1px solid var(--neon-green);
      color: var(--neon-green);
    }
    .intensity-3 {
      background: rgba(255, 0, 127, 0.25);
      border: 1px solid var(--neon-pink);
      color: #FFF;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.4);
      animation: pulseGlow 1.4s infinite alternate;
    }

    @keyframes pulseGlow {
      from { box-shadow: 0 0 6px rgba(255, 0, 127, 0.3); }
      to { box-shadow: 0 0 16px rgba(255, 0, 127, 0.7); }
    }

    .badge-bales {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .zone-I { background: rgba(0, 255, 135, 0.15); color: var(--zone-1); border-color: var(--zone-1); }
    .zone-II { background: rgba(255, 230, 0, 0.15); color: var(--zone-2); border-color: var(--zone-2); }
    .zone-III { background: rgba(56, 189, 248, 0.15); color: var(--zone-3); border-color: var(--zone-3); }
    .zone-IV { background: rgba(255, 0, 127, 0.18); color: var(--zone-4); border-color: var(--zone-4); }

    .teleprompter-body {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .actor-node-mini {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      min-width: 74px;
    }
    .actor-node-mini img {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--neon-cyan);
    }
    .actor-node-mini .tag {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.72rem;
      font-weight: 800;
      color: #FFF;
      background: rgba(0, 0, 0, 0.5);
      padding: 1px 6px;
      border-radius: 4px;
    }

    .arrow-vector {
      font-size: 1.4rem;
      color: var(--neon-cyan);
      font-weight: 900;
    }

    .speech-bubble {
      flex: 1;
      background: rgba(8, 14, 30, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      padding: 14px 18px;
      position: relative;
    }
    .speech-bubble-text {
      font-size: 1.05rem;
      font-weight: 500;
      line-height: 1.5;
      color: #FFFFFF;
    }

    /* TETRAGRAM CANONICAL BOX */
    .tetragram-box {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(10, 18, 38, 0.9);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 6px 12px;
    }
    .tetra-cell {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.05);
      min-width: 28px;
    }
    .tetra-pos {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.62rem;
      color: var(--text-dim);
    }
    .tetra-val {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.88rem;
      font-weight: 900;
    }
    .tetra-val.pos { color: var(--neon-green); }
    .tetra-val.neu { color: var(--neon-gold); }
    .tetra-val.neg { color: var(--neon-pink); }

    .q81-figure-pill {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.82rem;
      font-weight: 900;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(0, 255, 135, 0.2);
      color: var(--neon-green);
      border: 1px solid rgba(0, 255, 135, 0.4);
    }

    /* GRID: MATRIX + SIDEBAR LOG */
    .interaction-workspace {
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 18px;
    }

    .matrix-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }

    .matrix-title-bar {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }
    .matrix-title-bar h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: #FFF;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* 5x5 INTERACTION BOARD */
    .board-container {
      position: relative;
      margin: 10px auto;
      display: inline-block;
      user-select: none;
    }

    #matrixCanvas {
      position: absolute;
      top: 0;
      left: 0;
      pointer-events: none;
      z-index: 10;
    }

    .matrix-grid-table {
      border-collapse: separate;
      border-spacing: 5px;
      position: relative;
      z-index: 5;
    }

    .corner-th {
      width: 80px;
      height: 72px;
      background: rgba(10, 16, 32, 0.6);
      border-radius: 8px;
      padding: 4px;
      text-align: center;
      font-size: 0.68rem;
      color: var(--text-dim);
      font-family: 'Roboto Mono', monospace;
    }

    .col-header-th {
      width: 78px;
      height: 72px;
      background: rgba(16, 26, 52, 0.7);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      text-align: center;
      padding: 4px 2px;
      transition: all 0.2s ease;
    }
    .col-header-th.active-sender {
      border-color: var(--neon-cyan);
      background: rgba(56, 189, 248, 0.25);
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
    }
    .th-avatar {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      object-fit: cover;
      border: 1.5px solid var(--neon-cyan);
      margin: 0 auto 2px auto;
      display: block;
    }
    .th-id {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.75rem;
      font-weight: 900;
      color: #FFF;
      line-height: 1;
    }
    .th-role {
      font-size: 0.62rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 72px;
    }

    .row-header-th {
      width: 80px;
      height: 72px;
      background: rgba(16, 26, 52, 0.7);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      text-align: center;
      padding: 4px 2px;
      transition: all 0.2s ease;
    }
    .row-header-th.active-receiver {
      border-color: var(--neon-green);
      background: rgba(0, 255, 135, 0.25);
      box-shadow: 0 0 14px rgba(0, 255, 135, 0.4);
    }

    /* CELDAS 5x5 */
    .matrix-cell {
      width: 78px;
      height: 72px;
      background: rgba(11, 18, 38, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      position: relative;
      cursor: pointer;
      transition: all 0.22s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .matrix-cell:hover {
      border-color: var(--neon-cyan);
      background: rgba(20, 36, 75, 0.85);
      transform: scale(1.04);
      z-index: 8;
    }
    .matrix-cell.diagonal {
      background: rgba(16, 26, 50, 0.5);
      border-style: dashed;
      border-color: rgba(255, 255, 255, 0.15);
    }
    .matrix-cell.active-laser-hit {
      border-color: #FFFFFF !important;
      box-shadow: 0 0 20px rgba(255, 255, 255, 0.8) !important;
      transform: scale(1.06);
      z-index: 12;
    }

    .cell-val-count {
      font-family: 'Roboto Mono', monospace;
      font-size: 1.05rem;
      font-weight: 800;
      color: #FFF;
      line-height: 1.1;
    }
    .cell-valence-pill {
      font-family: 'Roboto Mono', monospace;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 1px 4px;
      border-radius: 4px;
      margin-top: 3px;
    }

    /* MÁRGENES TERMOGRÁFICOS */
    .margin-da-cell {
      width: 78px;
      height: 38px;
      background: rgba(10, 16, 32, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 6px;
      text-align: center;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.82rem;
      font-weight: 800;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: background 0.3s ease;
    }
    .margin-rc-cell {
      width: 68px;
      height: 72px;
      background: rgba(10, 16, 32, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 6px;
      text-align: center;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.82rem;
      font-weight: 800;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: background 0.3s ease;
    }

    /* MOVIOLA CONTROLS */
    .moviola-bar {
      width: 100%;
      background: rgba(10, 16, 34, 0.95);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      padding: 12px 18px;
      margin-top: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }

    .moviola-playback {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .moviola-btn {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(20, 33, 61, 0.85);
      border: 1px solid var(--border-glass);
      color: #FFF;
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }
    .moviola-btn:hover {
      background: var(--neon-cyan);
      color: #050811;
      transform: scale(1.08);
      border-color: var(--neon-cyan);
      box-shadow: 0 0 12px var(--neon-cyan);
    }
    .moviola-btn.play-btn {
      width: 46px;
      height: 46px;
      background: var(--neon-green);
      color: #050811;
      border: none;
      font-size: 1.3rem;
      box-shadow: 0 0 16px rgba(0, 255, 135, 0.4);
    }
    .moviola-btn.play-btn:hover {
      transform: scale(1.12);
      filter: brightness(1.15);
      box-shadow: 0 0 22px rgba(0, 255, 135, 0.7);
    }

    .scrubber-container {
      flex: 1;
      min-width: 220px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .scrubber-slider {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }
    .scrubber-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--neon-green);
      cursor: pointer;
      box-shadow: 0 0 10px var(--neon-green);
      transition: transform 0.15s ease;
    }
    .scrubber-slider::-webkit-slider-thumb:hover {
      transform: scale(1.25);
    }

    .scrubber-labels {
      display: flex;
      justify-content: space-between;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.72rem;
      color: var(--text-dim);
    }

    .moviola-speed-group {
      display: flex;
      align-items: center;
      gap: 4px;
      background: rgba(15, 23, 42, 0.7);
      padding: 3px 6px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .speed-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: 'Roboto Mono', monospace;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .speed-btn:hover {
      color: #FFF;
      background: rgba(255, 255, 255, 0.08);
    }
    .speed-btn.active {
      color: #050811;
      background: var(--neon-cyan);
    }

    /* SIDEBAR: CONVERSATION LOG */
    .sidebar-log {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      max-height: 720px;
    }
    .sidebar-log-header {
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      color: #FFF;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sidebar-log-list {
      flex: 1;
      overflow-y: auto;
      margin-top: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding-right: 4px;
    }

    .log-item {
      background: rgba(11, 18, 38, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 10px 12px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .log-item:hover {
      background: rgba(20, 33, 61, 0.85);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateX(2px);
    }
    .log-item.active {
      border-color: var(--neon-green);
      background: rgba(0, 255, 135, 0.12);
      box-shadow: 0 0 10px rgba(0, 255, 135, 0.2);
    }
    .log-item-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 4px;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.72rem;
    }
    .log-turn-num {
      color: var(--neon-cyan);
      font-weight: 700;
    }
    .log-actor-link {
      font-weight: 800;
      color: #FFF;
    }
    .log-snippet {
      font-size: 0.8rem;
      color: var(--text-dim);
      line-height: 1.35;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* PHASE 3: WORKBENCH DEL DILEMA Y MATRIZ DE PAGOS */
    .phase3-container {
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 20px;
      margin-top: 14px;
    }

    .dilemma-card {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 22px;
    }
    .dilemma-card h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: #FFF;
      margin-bottom: 8px;
    }
    .dilemma-card h2 span { color: var(--neon-gold); }

    .sliders-table {
      width: 100%;
      margin: 18px 0;
      border-collapse: separate;
      border-spacing: 0 10px;
    }
    .slider-row {
      background: rgba(10, 16, 32, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      transition: all 0.2s ease;
    }
    .slider-row:hover {
      border-color: var(--neon-cyan);
    }
    .slider-row td {
      padding: 10px 14px;
    }

    .player-mini-info {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .player-mini-info img {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--neon-cyan);
    }

    .token-range-input {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      outline: none;
      -webkit-appearance: none;
    }
    .token-range-input::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--neon-gold);
      cursor: pointer;
      box-shadow: 0 0 8px var(--neon-gold);
    }

    .tokens-val-badge {
      font-family: 'Roboto Mono', monospace;
      font-size: 1rem;
      font-weight: 900;
      color: var(--neon-gold);
      min-width: 50px;
      text-align: right;
    }

    .payoffs-summary-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .payoffs-summary-panel h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #FFF;
      border-bottom: 1px solid var(--border-glass);
      padding-bottom: 8px;
    }

    .pot-multiplier-card {
      background: linear-gradient(135deg, rgba(255, 230, 0, 0.15) 0%, rgba(255, 159, 28, 0.2) 100%);
      border: 1px solid rgba(255, 230, 0, 0.4);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
    }
    .pot-total-number {
      font-family: 'Roboto Mono', monospace;
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--neon-gold);
      text-shadow: 0 0 16px rgba(255, 230, 0, 0.4);
    }
    .pot-multiplier-sub {
      font-size: 0.84rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    .festinger-gauge-card {
      background: rgba(16, 26, 50, 0.7);
      border: 1px solid rgba(255, 0, 127, 0.3);
      border-radius: 12px;
      padding: 14px;
    }
    .festinger-title {
      font-family: 'Outfit', sans-serif;
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--neon-pink);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
    }
    .festinger-score {
      font-family: 'Roboto Mono', monospace;
      font-size: 1.4rem;
      font-weight: 900;
      color: #FFF;
    }

    /* PHASE 4: SÍNTESIS ESTRUCTURAL & DRILL-DOWN */
    .phase4-container {
      display: grid;
      grid-template-columns: 1fr 400px;
      gap: 20px;
      margin-top: 14px;
    }

    .synthesis-card {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 22px;
    }
    .synthesis-card h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: #FFF;
      margin-bottom: 8px;
    }
    .synthesis-card h2 span { color: var(--neon-green); }

    .delta-matrix-table {
      border-collapse: separate;
      border-spacing: 6px;
      margin: 16px auto;
    }
    .delta-cell {
      width: 80px;
      height: 72px;
      background: rgba(11, 18, 38, 0.85);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      text-align: center;
      cursor: pointer;
      transition: all 0.22s ease;
      padding: 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .delta-cell:hover {
      border-color: var(--neon-cyan);
      transform: scale(1.08);
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
      z-index: 10;
    }
    .delta-cell.positive-bond {
      background: rgba(0, 255, 135, 0.12);
      border-color: rgba(0, 255, 135, 0.4);
    }
    .delta-cell.negative-fracture {
      background: rgba(255, 0, 127, 0.15);
      border-color: rgba(255, 0, 127, 0.5);
    }

    .drill-instructions {
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 10px;
      padding: 10px 14px;
      font-size: 0.84rem;
      color: var(--neon-cyan);
      margin-top: 12px;
      text-align: center;
    }

    /* FORENSICS MODAL / DRAWER */
    .forensic-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(3, 5, 12, 0.85);
      backdrop-filter: blur(12px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .forensic-modal.active {
      display: flex;
    }

    .forensic-dialog {
      background: #0B132B;
      border: 1.5px solid var(--neon-cyan);
      border-radius: 18px;
      max-width: 680px;
      width: 100%;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(56, 189, 248, 0.3);
      overflow: hidden;
      animation: modalZoom 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes modalZoom {
      from { transform: scale(0.92); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .forensic-header {
      background: rgba(16, 26, 52, 0.95);
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .forensic-header h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #FFF;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .close-modal-btn {
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #FFF;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s ease;
    }
    .close-modal-btn:hover {
      background: var(--neon-pink);
    }

    .forensic-content {
      padding: 18px 20px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .forensic-turn-card {
      background: rgba(16, 26, 52, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .forensic-turn-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.78rem;
    }
    .forensic-turn-quote {
      font-size: 0.92rem;
      color: #FFF;
      line-height: 1.45;
      font-style: italic;
      padding-left: 10px;
      border-left: 2px solid var(--neon-cyan);
    }
    .jump-to-turn-btn {
      align-self: flex-end;
      background: rgba(56, 189, 248, 0.2);
      border: 1px solid var(--neon-cyan);
      color: var(--neon-cyan);
      border-radius: 6px;
      padding: 4px 10px;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .jump-to-turn-btn:hover {
      background: var(--neon-cyan);
      color: #050811;
    }

    /* PEDAGOGICAL EXPLANATORY NOTE (RULE 10) */
    .pedagogical-note-card {
      background: linear-gradient(135deg, rgba(16, 28, 56, 0.92) 0%, rgba(9, 15, 32, 0.96) 100%);
      border: 1px solid var(--border-glass);
      border-left: 4px solid var(--neon-cyan);
      border-radius: 14px;
      padding: 20px 24px;
      margin-top: 26px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
    }
    .pedagogical-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }
    .pedagogical-text {
      font-size: 0.9rem;
      line-height: 1.65;
      color: var(--text-dim);
    }
    .pedagogical-text strong {
      color: #FFF;
    }
    .pedagogical-text em {
      color: var(--neon-cyan);
      font-style: normal;
    }

    /* UNIVERSAL NAV POD (RULE 15) */
    .universal-nav-pod {
      position: fixed;
      right: 18px;
      bottom: 20px;
      z-index: 99999;
      display: flex;
      flex-direction: column;
      gap: 12px;
      align-items: center;
      background: rgba(6, 10, 22, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 12px 8px;
      border-radius: 28px;
      border: 1.5px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.75), 0 0 16px rgba(56, 189, 248, 0.2);
    }
    .nav-pod-btn {
      width: 52px;
      height: 52px;
      background: rgba(16, 25, 53, 0.92);
      border: 1.5px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
      color: #38BDF8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.95rem;
      line-height: 1;
      cursor: pointer;
      text-decoration: none;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), color 0.2s ease, filter 0.2s ease, background 0.2s ease;
      user-select: none;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.8));
    }
    .nav-pod-btn:hover {
      transform: scale(1.12);
      background: rgba(56, 189, 248, 0.25);
      border-color: #00FF87;
      color: #00FF87;
    }

    @media (max-width: 1080px) {
      .phase1-grid, .interaction-workspace, .phase3-container, .phase4-container {
        grid-template-columns: 1fr;
      }
      .board-container {
        overflow-x: auto;
      }
    }
  </style>
</head>
<body>

  <!-- CABECERA INSTITUCIONAL CANÓNICA (REGLAS 9, 14, 16) -->
  <header class="app-header">
    <a href="index.html" class="brand-section">
      <img src="LOGO_NEXORD_OFICIAL.png" alt="NEXORD Logo" class="brand-logo" onerror="this.src='LOGO_NEX_ORD_OFICIAL.png';">
      <div class="brand-titles">
        <div class="brand-title">
          NEXORD <span class="brand-badge">VISORD PROCESUAL</span>
        </div>
        <div class="brand-canonical-tag">
          Laboratorio de Dilema de Bienes Comunes · <span>(G1T1C1-DILEMA)</span> · Matriz: 1g1t1c · 25 de Septiembre de 2026
        </div>
      </div>
    </a>

    <div class="header-controls">
      <button id="sfxToggleBtn" class="header-btn active" title="Activar/Desactivar Efectos de Audio Procedural">
        🔊 SFX: ON
      </button>
      <button id="voiceToggleBtn" class="header-btn" title="Activar/Desactivar Voz con Web Speech API">
        🎙️ Voz: OFF
      </button>
      <a href="index.html" class="header-btn">
        🏠 Portal
      </a>
      <a href="visord_demo.html" class="header-btn">
        VISORD 3D ↗
      </a>
    </div>
  </header>

  <!-- STEPPER DE 4 FASES EXPERIMENTALES -->
  <nav class="stepper-nav">
    <div class="step-item active" data-phase="1" onclick="switchPhase(1)">
      <div class="step-num">1</div>
      <div class="step-title">Línea Base O₀ (Pre-test)</div>
    </div>
    <div class="step-item" data-phase="2" onclick="switchPhase(2)">
      <div class="step-num">2</div>
      <div class="step-title">Debate Procesual (Moviola & Matriz)</div>
    </div>
    <div class="step-item" data-phase="3" onclick="switchPhase(3)">
      <div class="step-num">3</div>
      <div class="step-title">Matriz de Pagos & Votación Secreta</div>
    </div>
    <div class="step-item" data-phase="4" onclick="switchPhase(4)">
      <div class="step-num">4</div>
      <div class="step-title">Síntesis Estructural Δ (Drill-Down)</div>
    </div>
  </nav>

  <!-- CONTENEDOR PRINCIPAL -->
  <main class="main-wrapper">

    <!-- FASE 1: LÍNEA BASE O0 (PRE-TEST 60s) -->
    <section id="phase1" class="phase-view active">
      <div class="banner-pretest">
        <h2>🔬 Fase 1: <span>Línea Base Sociométrica O₀ (Pre-test BREVE de 60s)</span></h2>
        <p>
          En la tradición de la Dinámica de Grupos de <strong>Kurt Lewin</strong> y el <em>Research Center for Group Dynamics del MIT</em>, 
          los cinco miembros del grupo completaron una prueba rápida ordinal inicial de 60 segundos antes de comenzar la tarea de bienes comunes. 
          Este test calibra las expectativas cruzadas iniciales y el clima sociométrico basal antes de someter al grupo a la prueba experimental de conversación y votación.
        </p>
      </div>

      <div class="phase1-grid">
        <div class="actors-cards-grid">
          <!-- 1A -->
          <div class="actor-pre-card">
            <img src="assets/faces_dilema/1A.jpg" alt="1A" class="actor-avatar-lg">
            <div class="actor-id-badge">1A · Líder Catalizador</div>
            <div class="actor-role-title">Iniciador Prosocial</div>
            <div class="actor-role-desc">Enfocado en la optimización colectiva. Propone cooperar plenamente al 100%.</div>
            <div class="actor-pre-stats">
              <div><span>8.9</span> Popularidad</div>
              <div><span>+4</span> Emisiones</div>
              <div><span>0.85</span> Cohesión</div>
            </div>
          </div>

          <!-- 2A -->
          <div class="actor-pre-card">
            <img src="assets/faces_dilema/2A.jpg" alt="2A" class="actor-avatar-lg">
            <div class="actor-id-badge">2A · Cooperador</div>
            <div class="actor-role-title">Respaldo Normativo</div>
            <div class="actor-role-desc">Altruista recíproco. Busca reforzar los vínculos y blindar el consenso.</div>
            <div class="actor-pre-stats">
              <div><span>8.2</span> Popularidad</div>
              <div><span>+3</span> Emisiones</div>
              <div><span>0.80</span> Cohesión</div>
            </div>
          </div>

          <!-- 3A -->
          <div class="actor-pre-card">
            <img src="assets/faces_dilema/3A.jpg" alt="3A" class="actor-avatar-lg">
            <div class="actor-id-badge">3A · Auditor Normativo</div>
            <div class="actor-role-title">Vigilante / Escrutinio</div>
            <div class="actor-role-desc">Escéptico ante promesas gratuitas. Exige garantías contra posibles polizones.</div>
            <div class="actor-pre-stats">
              <div><span>7.4</span> Popularidad</div>
              <div><span>+2</span> Emisiones</div>
              <div><span>0.65</span> Cohesión</div>
            </div>
          </div>

          <!-- 4A -->
          <div class="actor-pre-card">
            <img src="assets/faces_dilema/4A.jpg" alt="4A" class="actor-avatar-lg">
            <div class="actor-id-badge">4A · Cauteloso</div>
            <div class="actor-role-title">Prudente / Moderado</div>
            <div class="actor-role-desc">Teme quedar en desventaja. Solo coopera si percibe seguridad institucional.</div>
            <div class="actor-pre-stats">
              <div><span>6.8</span> Popularidad</div>
              <div><span>+1</span> Emisiones</div>
              <div><span>0.60</span> Cohesión</div>
            </div>
          </div>

          <!-- 5A -->
          <div class="actor-pre-card">
            <img src="assets/faces_dilema/5A.jpg" alt="5A" class="actor-avatar-lg">
            <div class="actor-id-badge">5A · Free-Rider Oculto</div>
            <div class="actor-role-title">Egoísta Estratégico</div>
            <div class="actor-role-desc">Despliega simpatía verbal fingida para inducir a los demás a aportar y desertar en secreto.</div>
            <div class="actor-pre-stats">
              <div><span>7.9</span> Popularidad</div>
              <div><span>+3</span> Emisiones</div>
              <div><span>0.40</span> Genuinidad</div>
            </div>
          </div>
        </div>

        <div class="pretest-sidebar">
          <h3>📊 Parámetros Basales O₀</h3>
          <div class="metric-row">
            <span>Densidad Relativa Basal (SDR₀):</span>
            <span class="val">0.68</span>
          </div>
          <div class="metric-row">
            <span>Entropía Relacional (S₀):</span>
            <span class="val">1.14 nats</span>
          </div>
          <div class="metric-row">
            <span>Clima Cooperativo Inicial:</span>
            <span class="val">82% (Favorable)</span>
          </div>
          <div class="metric-row">
            <span>Dotación Inicial por Sujeto:</span>
            <span class="val">10 Fichas</span>
          </div>
          <div class="metric-row">
            <span>Multiplicador de Fondo Común:</span>
            <span class="val">× 1.80</span>
          </div>

          <div style="font-size:0.8rem; color:var(--text-dim); line-height:1.45; margin-top:8px;">
            💡 <strong>Hipótesis Experimental:</strong> La conversación informal (<em>cheap talk</em>) creará un consenso verbal aparente de intensidad alta, 
            que será traicionado en secreto por 5A, provocando una onda de choque entrópica en la matriz sociométrica.
          </div>

          <button class="start-debate-btn" onclick="switchPhase(2)">
            Abrir la Caja Negra: Iniciar Debate ➔
          </button>
        </div>
      </div>
    </section>

    <!-- FASE 2: DEBATE PROCESUAL EN VIVO (MOVIOLA Y MATRIZ CUÁNTICA) -->
    <section id="phase2" class="phase-view">
      
      <!-- TELEPROMPTER DINÁMICO -->
      <div class="teleprompter-card">
        <div class="teleprompter-top-row">
          <div class="turn-badge-main" id="turnCounterBadge">Turno 01 / 18</div>

          <div class="teleprompter-badges">
            <div class="badge-intensity intensity-2" id="intensityBadge">
              ⚡⚡ Intensidad 2º: Firmeza Normativa
            </div>
            <div class="badge-bales zone-II" id="balesBadge">
              Zona II: Tarea Sugerencia (Bales 4)
            </div>
            
            <!-- TETRAGRAMA CANÓNICO SMIb -->
            <div class="tetragram-box" title="Tetragrama Canónico SMIb [A1, A2, A3, A4]">
              <div class="tetra-cell" title="A1 (p_DA): Expectativa que el emisor tiene de lo que hará el partner">
                <span class="tetra-pos">A1</span>
                <span class="tetra-val pos" id="tA1">+</span>
              </div>
              <div class="tetra-cell" title="A2 (DA): Preferencia efectiva que el emisor otorga al partner">
                <span class="tetra-pos">A2</span>
                <span class="tetra-val pos" id="tA2">+</span>
              </div>
              <div class="tetra-cell" title="A3 (RECIBE): Preferencia efectiva que el partner otorga al emisor">
                <span class="tetra-pos">A3</span>
                <span class="tetra-val pos" id="tA3">+</span>
              </div>
              <div class="tetra-cell" title="A4 (p_RECIBE): Expectativa que el partner tiene de lo que hará el emisor">
                <span class="tetra-pos">A4</span>
                <span class="tetra-val pos" id="tA4">+</span>
              </div>
              <div class="q81-figure-pill" id="q81Figure">&lt;Ee&gt;</div>
            </div>
          </div>
        </div>

        <div class="teleprompter-body">
          <div class="actor-node-mini">
            <img src="assets/faces_dilema/1A.jpg" id="senderAvatar" alt="Sender">
            <span class="tag" id="senderTag">1A (Líder)</span>
          </div>

          <div class="arrow-vector">➔</div>

          <div class="actor-node-mini">
            <img src="assets/faces_dilema/2A.jpg" id="receiverAvatar" alt="Receiver">
            <span class="tag" id="receiverTag">2A (Cooperador)</span>
          </div>

          <div class="speech-bubble">
            <div class="speech-bubble-text" id="speechText">
              "Compañeros, la matemática del fondo común es irrefutable: si los cinco aportamos nuestras 10 fichas, el bote de 50 se multiplica por 1.8 y nos repartimos 18 fichas cada uno. Todos ganamos 8 fichas netas."
            </div>
          </div>
        </div>
      </div>

      <!-- WORKSPACE: MATRIX 5x5 + LOG -->
      <div class="interaction-workspace">
        
        <!-- PANEL DE LA MATRIZ CUÁNTICA -->
        <div class="matrix-panel">
          <div class="matrix-title-bar">
            <h3>🔬 Matriz de Interacción Ortogonal 5×5 <span>(Láseres & Decaimiento Térmico)</span></h3>
            <button id="ghostSmiToggle" class="header-btn" onclick="toggleGhostSMIb()">
              👻 Capa Fantasma: OFF
            </button>
          </div>

          <!-- TABLERO MATRICIAL 5x5 -->
          <div class="board-container" id="boardContainer">
            <canvas id="matrixCanvas"></canvas>

            <table class="matrix-grid-table" id="matrixGridTable">
              <thead>
                <tr>
                  <th class="corner-th">EMISOR (i) ↓<br>RECEPTOR (j) →</th>
                  <!-- HEADERS COLUMNAS (EMISORES i) -->
                  <th class="col-header-th" id="colHeader_0">
                    <img src="assets/faces_dilema/1A.jpg" class="th-avatar" alt="1A">
                    <div class="th-id">1A</div>
                    <div class="th-role">Líder</div>
                  </th>
                  <th class="col-header-th" id="colHeader_1">
                    <img src="assets/faces_dilema/2A.jpg" class="th-avatar" alt="2A">
                    <div class="th-id">2A</div>
                    <div class="th-role">Cooperador</div>
                  </th>
                  <th class="col-header-th" id="colHeader_2">
                    <img src="assets/faces_dilema/3A.jpg" class="th-avatar" alt="3A">
                    <div class="th-id">3A</div>
                    <div class="th-role">Auditor</div>
                  </th>
                  <th class="col-header-th" id="colHeader_3">
                    <img src="assets/faces_dilema/4A.jpg" class="th-avatar" alt="4A">
                    <div class="th-id">4A</div>
                    <div class="th-role">Cauteloso</div>
                  </th>
                  <th class="col-header-th" id="colHeader_4">
                    <img src="assets/faces_dilema/5A.jpg" class="th-avatar" alt="5A">
                    <div class="th-id">5A</div>
                    <div class="th-role">Free-Rider</div>
                  </th>
                  <th class="corner-th" style="width:68px;">RECIBE<br>(Σ RC)</th>
                </tr>
              </thead>
              <tbody id="matrixTableBody">
                <!-- Generado dinámicamente -->
              </tbody>
              <tfoot>
                <tr id="marginDaRow">
                  <td class="corner-th">EMITE<br>(Σ DA)</td>
                  <td class="margin-da-cell" id="daCell_0">0</td>
                  <td class="margin-da-cell" id="daCell_1">0</td>
                  <td class="margin-da-cell" id="daCell_2">0</td>
                  <td class="margin-da-cell" id="daCell_3">0</td>
                  <td class="margin-da-cell" id="daCell_4">0</td>
                  <td class="corner-th" id="daTotalCell">Σ: 0</td>
                </tr>
              </tfoot>
            </table>
          </div>

          <!-- CONTROLES DE LA MOVIOLA -->
          <div class="moviola-bar">
            <div class="moviola-playback">
              <button class="moviola-btn" onclick="stepPrev()" title="Turno Anterior">⏮</button>
              <button class="moviola-btn play-btn" id="playBtn" onclick="togglePlay()" title="Reproducir / Pausa">▶</button>
              <button class="moviola-btn" onclick="stepNext()" title="Turno Siguiente">⏭</button>
              <button class="moviola-btn" onclick="resetDebate()" title="Reiniciar">🔄</button>
            </div>

            <div class="scrubber-container">
              <input type="range" class="scrubber-slider" id="scrubberSlider" min="1" max="18" value="1" oninput="seekToTurn(this.value)">
              <div class="scrubber-labels">
                <span>Inicio (T1)</span>
                <span>Pacto Verbal (T15)</span>
                <span>Votación (T16)</span>
                <span>Auditoría (T18)</span>
              </div>
            </div>

            <div class="moviola-speed-group">
              <button class="speed-btn" data-speed="0.5" onclick="setSpeed(0.5)">0.5x</button>
              <button class="speed-btn active" data-speed="1.0" onclick="setSpeed(1.0)">1.0x</button>
              <button class="speed-btn" data-speed="2.0" onclick="setSpeed(2.0)">2.0x</button>
              <button class="speed-btn" data-speed="3.0" onclick="setSpeed(3.0)">3.0x</button>
            </div>
          </div>
        </div>

        <!-- PANEL LATERAL: HISTORIAL DE TURNOS -->
        <div class="sidebar-log">
          <div class="sidebar-log-header">
            <span>📜 Registro Cronológico de Turnos</span>
            <span style="font-family:'Roboto Mono'; font-size:0.75rem; color:var(--neon-cyan);" id="logProgress">1/18</span>
          </div>
          <div class="sidebar-log-list" id="sidebarLogList">
            <!-- Rellenado por JS -->
          </div>
        </div>

      </div>
    </section>

    <!-- FASE 3: WORKBENCH DEL DILEMA Y MATRIZ DE PAGOS (THIBAUT & KELLEY) -->
    <section id="phase3" class="phase-view">
      <div class="phase3-container">
        
        <div class="dilemma-card">
          <h2>⚖️ Fase 3: <span>Asignación Secreta de Fichas & Matriz de Pagos</span></h2>
          <p style="color:var(--text-dim); font-size:0.92rem; line-height:1.5; margin-bottom:14px;">
            Culminado el debate de <em>cheap talk</em> con promesas unánimes de cooperación, los cinco participantes depositan en secreto su aportación (de 0 a 10 fichas) al <strong>Fondo Común</strong>. 
            El fondo se multiplica por el factor de sinergia <strong>× 1.8</strong> y se reparte en partes exactamente iguales entre todos los miembros.
          </p>

          <table class="sliders-table">
            <thead>
              <tr style="font-family:'Roboto Mono'; font-size:0.75rem; color:var(--text-dim); text-align:left;">
                <th>PARTICIPANTE</th>
                <th>APORTACIÓN SECRETA (0 - 10)</th>
                <th style="text-align:right;">FICHAS</th>
                <th style="text-align:right;">PAGO NETO</th>
              </tr>
            </thead>
            <tbody>
              <!-- 1A -->
              <tr class="slider-row">
                <td>
                  <div class="player-mini-info">
                    <img src="assets/faces_dilema/1A.jpg" alt="1A">
                    <div>
                      <div style="font-weight:700; color:#FFF;">1A · Líder</div>
                      <div style="font-size:0.74rem; color:var(--neon-green);">Prometió: 10</div>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="range" class="token-range-input" id="tokenSlider_0" min="0" max="10" value="10" oninput="updatePayoffs()">
                </td>
                <td class="tokens-val-badge" id="tokenVal_0">10</td>
                <td style="font-family:'Roboto Mono'; font-weight:800; color:var(--neon-cyan); text-align:right;" id="netPayout_0">14.4</td>
              </tr>

              <!-- 2A -->
              <tr class="slider-row">
                <td>
                  <div class="player-mini-info">
                    <img src="assets/faces_dilema/2A.jpg" alt="2A">
                    <div>
                      <div style="font-weight:700; color:#FFF;">2A · Cooperador</div>
                      <div style="font-size:0.74rem; color:var(--neon-green);">Prometió: 10</div>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="range" class="token-range-input" id="tokenSlider_1" min="0" max="10" value="10" oninput="updatePayoffs()">
                </td>
                <td class="tokens-val-badge" id="tokenVal_1">10</td>
                <td style="font-family:'Roboto Mono'; font-weight:800; color:var(--neon-cyan); text-align:right;" id="netPayout_1">14.4</td>
              </tr>

              <!-- 3A -->
              <tr class="slider-row">
                <td>
                  <div class="player-mini-info">
                    <img src="assets/faces_dilema/3A.jpg" alt="3A">
                    <div>
                      <div style="font-weight:700; color:#FFF;">3A · Auditor</div>
                      <div style="font-size:0.74rem; color:var(--neon-green);">Prometió: 10</div>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="range" class="token-range-input" id="tokenSlider_2" min="0" max="10" value="10" oninput="updatePayoffs()">
                </td>
                <td class="tokens-val-badge" id="tokenVal_2">10</td>
                <td style="font-family:'Roboto Mono'; font-weight:800; color:var(--neon-cyan); text-align:right;" id="netPayout_2">14.4</td>
              </tr>

              <!-- 4A -->
              <tr class="slider-row">
                <td>
                  <div class="player-mini-info">
                    <img src="assets/faces_dilema/4A.jpg" alt="4A">
                    <div>
                      <div style="font-weight:700; color:#FFF;">4A · Cauteloso</div>
                      <div style="font-size:0.74rem; color:var(--neon-green);">Prometió: 10</div>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="range" class="token-range-input" id="tokenSlider_3" min="0" max="10" value="10" oninput="updatePayoffs()">
                </td>
                <td class="tokens-val-badge" id="tokenVal_3">10</td>
                <td style="font-family:'Roboto Mono'; font-weight:800; color:var(--neon-cyan); text-align:right;" id="netPayout_3">14.4</td>
              </tr>

              <!-- 5A (DEFECTOR) -->
              <tr class="slider-row" style="border-color: rgba(255, 0, 127, 0.4);">
                <td>
                  <div class="player-mini-info">
                    <img src="assets/faces_dilema/5A.jpg" alt="5A">
                    <div>
                      <div style="font-weight:700; color:var(--neon-pink);">5A · Free-Rider</div>
                      <div style="font-size:0.74rem; color:var(--neon-pink);">¡Prometió 10!</div>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="range" class="token-range-input" id="tokenSlider_4" min="0" max="10" value="0" oninput="updatePayoffs()">
                </td>
                <td class="tokens-val-badge" id="tokenVal_4" style="color:var(--neon-pink);">0</td>
                <td style="font-family:'Roboto Mono'; font-weight:800; color:var(--neon-pink); text-align:right;" id="netPayout_4">24.4</td>
              </tr>
            </tbody>
          </table>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:14px;">
            <button class="header-btn" onclick="resetToCanonicalPayoffs()">
              ↺ Restablecer Valores Canónicos (5A = 0)
            </button>
            <button class="start-debate-btn" style="margin:0; padding:10px 18px;" onclick="switchPhase(4)">
              Ver Síntesis Estructural Δ ➔
            </button>
          </div>
        </div>

        <!-- PANEL DE RETORNO Y DISONANCIA -->
        <div class="payoffs-summary-panel">
          <h3>💰 Balances del Fondo Común</h3>
          
          <div class="pot-multiplier-card">
            <div style="font-size:0.82rem; color:var(--text-main); font-weight:700; text-transform:uppercase; letter-spacing:0.8px;">
              BOTE MULTIPLICADO (×1.8)
            </div>
            <div class="pot-total-number" id="multipliedPotDisplay">72.0</div>
            <div class="pot-multiplier-sub" id="potBreakdownSub">
              Recaudación: 40 fichas · Dividendo individual: 14.4 fichas
            </div>
          </div>

          <div class="festinger-gauge-card">
            <div class="festinger-title">
              ⚡ Disonancia Cognitiva de Festinger (DF)
            </div>
            <div class="festinger-score" id="festingerScoreDisplay">
              DF(5A) = 25.0 <span style="font-size:0.75rem; color:var(--neon-pink); font-weight:500;">(CRÍTICA)</span>
            </div>
            <div style="font-size:0.78rem; color:var(--text-dim); line-height:1.4; margin-top:6px;">
              Fórmula canónica: <em>DF = |Aportación Prometida - Aportación Real| × Intensidad Media Verbal</em>. 
              La discrepancia máxima entre el discurso apasionado de 5A y su deserción práctica destruye el potencial de cohesión grupal.
            </div>
          </div>

          <div style="background:rgba(10,16,32,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px; font-size:0.82rem; line-height:1.45; color:var(--text-dim);">
            📌 <strong>Teorema de Thibaut & Kelley (1959):</strong> 
            El polizón maximiza su beneficio material inmediato (<em>24.4 créditos vs 14.4 de los cooperadores</em>), 
            pero sufre una penalización sociométrica irrevocable en la fase de auditoría posterior.
          </div>
        </div>

      </div>
    </section>

    <!-- FASE 4: SÍNTESIS ESTRUCTURAL Y AUDITORÍA FORENSE DRILL-DOWN -->
    <section id="phase4" class="phase-view">
      <div class="phase4-container">
        
        <div class="synthesis-card">
          <h2>📊 Fase 4: <span>Matriz Diferencial Δ (SMIb_final - SMIb_O₀)</span></h2>
          <p style="color:var(--text-dim); font-size:0.92rem; line-height:1.5;">
            La matriz diferencial revela la metamorfosis relacional completa tras el dilema. 
            Haz clic en <strong>cualquier celda (i, j)</strong> para abrir la <em>Auditoría Forense</em> e inspeccionar 
            cada turno exacto intercambiado en la conversación, con salto instantáneo de la Moviola.
          </p>

          <table class="delta-matrix-table" id="deltaMatrixTable">
            <!-- Rellenado por JS -->
          </table>

          <div class="drill-instructions">
            👆 <strong>TRAZABILIDAD BIDIRECCIONAL COMPLETA:</strong> Haz clic en cualquier celda para inspeccionar los actos comunicacionales que la originaron.
          </div>
        </div>

        <div class="pretest-sidebar">
          <h3>🔍 Diagnóstico Socio-Termodinámico</h3>
          <div class="metric-row">
            <span>Densidad Post-Dilema (SDR_final):</span>
            <span class="val" style="color:var(--neon-pink);">0.34 (Colapso)</span>
          </div>
          <div class="metric-row">
            <span>Entropía Residual (ΔS):</span>
            <span class="val" style="color:var(--neon-pink);">+2.86 nats</span>
          </div>
          <div class="metric-row">
            <span>Aislamiento Sociométrico de 5A:</span>
            <span class="val" style="color:var(--neon-pink);">100% Rechazo</span>
          </div>
          <div class="metric-row">
            <span>Subgrafo Cohesivo Nuclear:</span>
            <span class="val">{1A, 2A, 3A, 4A}</span>
          </div>

          <div style="font-size:0.82rem; color:var(--text-dim); line-height:1.45; margin-top:10px;">
            💡 <strong>Conclusión Factual:</strong> La conversación previa elevó la confianza artificialmente. 
            La defección de 5A no solo causó una pérdida económica colectiva, sino que transformó la matriz de expectativas positivas 
            en una estructura polarizada de rechazo absoluto ([Rr]), confirmando las tesis de Festinger y Thibaut & Kelley.
          </div>

          <button class="header-btn" style="justify-content:center; padding:10px; margin-top:10px;" onclick="switchPhase(2)">
            ⏮ Volver a Moviola & Diálogo
          </button>
        </div>

      </div>
    </section>

    <!-- NOTA EXPLICATIVA PEDAGÓGICA (REGLA 10 OBLIGATORIA) -->
    <section class="pedagogical-note-card">
      <div class="pedagogical-title">
        💡 Nota Explicativa Pedagógica: La Superación de la "Caja Negra" de la Comunicación en la Sociometría Ordinal
      </div>
      <div class="pedagogical-text">
        Durante casi cinco décadas, la economía experimental y la psicología del comportamiento (desde los experimentos pioneros de <em>Dawes, Orbell & van de Kragt, 1977</em>) 
        constataron que conceder unos minutos de charla informal (<strong>cheap talk</strong>) a los participantes antes de votar en un dilema de bienes comunes 
        incrementaba significativamente las tasas de cooperación. Sin embargo, dicha comunicación se trataba como una <strong>«caja negra»</strong> opaca: 
        se registraba únicamente como variable dicotómica (<em>«hubo comunicación» vs «no hubo comunicación»</em>), ignorando la microfísica semántica y energética de las palabras pronunciadas.<br><br>
        
        <strong>VISORD Procesual</strong> resuelve definitivamente esta carencia integrando cuatro tradiciones científicas fundamentales:
        <br>
        1. <strong>Robert F. Bales (Interaction Process Analysis - IPA)</strong>: Mapea cada acto de habla en 4 zonas de transferencia energética (Integración Socioemocional, Tarea Neutra, Demanda de Flujo y Diferenciación Socioemocional).<br>
        2. <strong>Jacob L. Moreno & NEXORD</strong>: Formaliza la interacción mediante matrices ordinales y el <strong>Tetragrama Canónico SMIb [A1, A2, A3, A4]</strong>, discriminando expectativas mutuas (p_DA, p_RECIBE) de preferencias fácticas (DA, RECIBE) y clasificándolas en las 81 figuras de <strong>Q81</strong>.<br>
        3. <strong>Kurt Lewin & Leon Festinger</strong>: Cuantifica la <strong>Disonancia Cognitiva (DF)</strong> y la ruptura de campo producida cuando un actor finge adhesión al consenso para después defeccionar en secreto.<br>
        4. <strong>John Thibaut & Harold Kelley (Matriz de Interdependencia y Pagos)</strong>: Vincula la ganancia material con el saldo reputacional y el reposicionamiento sociométrico del sujeto dentro del subgrafo grupal.
      </div>
    </section>

  </main>

  <!-- MODAL / DRAWER DE AUDITORÍA FORENSE DRILL-DOWN -->
  <div class="forensic-modal" id="forensicModal">
    <div class="forensic-dialog">
      <div class="forensic-header">
        <h3 id="forensicTitle">🔬 Auditoría Forense: Nodo 1A ➔ Nodo 2A</h3>
        <button class="close-modal-btn" onclick="closeForensicModal()">✕</button>
      </div>
      <div class="forensic-content" id="forensicContent">
        <!-- Rellenado por JS -->
      </div>
    </div>
  </div>

  <!-- MANDO UNIVERSAL FLOTANTE EN FILA INDIA (REGLA 15) -->
  <aside class="universal-nav-pod" aria-label="Navegación Rápida">
    <a href="index.html" class="nav-pod-btn" title="Ir al Portal Institucional NEXORD">🏠</a>
    <button class="nav-pod-btn" onclick="prevStepGlobal()" title="Fase Anterior">◀</button>
    <button class="nav-pod-btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Subir al Cenit">▲</button>
    <button class="nav-pod-btn" onclick="window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})" title="Bajar a la Base">▼</button>
    <button class="nav-pod-btn" onclick="nextStepGlobal()" title="Siguiente Fase">▶</button>
  </aside>

  <!-- SCRIPTS DE SIMULACIÓN Y COMPUTACIÓN SOCIO-TERMODINÁMICA -->
  <script>
    /* =========================================================================
       DATOS CANÓNICOS DEL EXPERIMENTO (N=5, DILEMA DE BIENES COMUNES)
       ========================================================================= */
    const ACTORS = [
      { id: '1A', name: 'Líder Catalizador', role: 'Catalizador Prosocial', img: 'assets/faces_dilema/1A.jpg', color: '#00FF87' },
      { id: '2A', name: 'Cooperador Prosocial', role: 'Respaldo Normativo', img: 'assets/faces_dilema/2A.jpg', color: '#38BDF8' },
      { id: '3A', name: 'Auditor Normativo', role: 'Vigilante / Escrutinio', img: 'assets/faces_dilema/3A.jpg', color: '#FF9F1C' },
      { id: '4A', name: 'Prudente / Cauteloso', role: 'Demanda de Garantías', img: 'assets/faces_dilema/4A.jpg', color: '#A855F7' },
      { id: '5A', name: 'Free-Rider Oculto', role: 'Egoísta Estratégico', img: 'assets/faces_dilema/5A.jpg', color: '#FF007F' }
    ];

    /* GUIÓN EXPERIMENTAL DE 18 TURNOS RIGUROSAMENTE CODIFICADOS */
    const TURNS = [
      {
        turn: 1, sender: 0, receiver: 0, isPlenary: true,
        intensity: 2, balesZone: 'II', balesCat: 4, balesDesc: 'Tarea: Da Sugerencia Estratégica',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.5, dS: -0.4,
        text: "Compañeros, la matemática del fondo común es irrefutable: si los cinco aportamos nuestras 10 fichas, el bote de 50 se multiplica por 1.8 y nos repartimos 18 fichas cada uno. Todos ganamos 8 fichas netas."
      },
      {
        turn: 2, sender: 1, receiver: 0, isPlenary: false,
        intensity: 2, balesZone: 'I', balesCat: 3, balesDesc: 'Socioemocional: Asentimiento Firme',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.8, dS: -0.3,
        text: "Completamente de acuerdo contigo, 1A. Es la única estrategia racional y colectiva. Yo me comprometo públicamente a poner mis 10 fichas desde el primer segundo."
      },
      {
        turn: 3, sender: 2, receiver: 2, isPlenary: true,
        intensity: 2, balesZone: 'III', balesCat: 8, balesDesc: 'Pregunta: Pide Opinión y Compromiso',
        tetra: ['0', '+', '0', '+'], q81: '(Ee>', dE: 0.8, dS: 0.2,
        text: "La teoría sobre el papel es perfecta, 1A. Pero solo funciona si no hay polizones. Si cuatro ponemos 10 y uno pone cero, ese se lleva 24.4 y los demás perdemos. ¿Alguien tiene dudas o piensa especular?"
      },
      {
        turn: 4, sender: 3, receiver: 2, isPlenary: false,
        intensity: 1, balesZone: 'III', balesCat: 7, balesDesc: 'Pregunta: Pide Aclaración / Duda',
        tetra: ['0', '0', '0', '0'], q81: '¡¿?!', dE: 0.5, dS: 0.3,
        text: "Admito que comparto la cautela de 3A. Si yo arriesgo mi dotación completa y alguien no cumple, mi margen queda destruido. ¿Qué garantías reales tenemos de que nadie traicionará el fondo?"
      },
      {
        turn: 5, sender: 0, receiver: 3, isPlenary: false,
        intensity: 2, balesZone: 'II', balesCat: 5, balesDesc: 'Tarea: Opinión Integradora',
        tetra: ['+', '+', '0', '+'], q81: '(Ee>', dE: 1.4, dS: -0.4,
        text: "Te comprendo, 4A, pero en este equipo no hay incentivos para autodestruirnos. Somos un grupo con futuro y la reputación compartida vale infinitamente más que una ventaja efímera. Confía."
      },
      {
        turn: 6, sender: 4, receiver: 4, isPlenary: true,
        intensity: 3, balesZone: 'I', balesCat: 3, balesDesc: 'Socioemocional: Falsa Solidaridad Efusiva',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 2.2, dS: -0.6,
        text: "¡Por favor, compañeros, ni se os ocurra dudar de mí! Yo pongo mis 10 fichas con los ojos cerrados. Vamos todos juntos a por el máximo beneficio. ¡Unanimidad total!"
      },
      {
        turn: 7, sender: 1, receiver: 4, isPlenary: false,
        intensity: 2, balesZone: 'I', balesCat: 2, balesDesc: 'Socioemocional: Elogio y Refuerzo',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.7, dS: -0.3,
        text: "¡Esa es la actitud que necesitábamos escuchar, 5A! Si mostramos este nivel de convicción, multiplicamos la riqueza del equipo sin fisuras."
      },
      {
        turn: 8, sender: 2, receiver: 4, isPlenary: false,
        intensity: 2, balesZone: 'IV', balesCat: 10, balesDesc: 'Diferenciación: Desconfianza Crítica',
        tetra: ['-', '0', '0', '-'], q81: '[Er]', dE: -1.2, dS: 0.5,
        text: "Espero que ese entusiasmo se traduzca en la urna, 5A. Te he visto dudar en dinámicas anteriores y el juego exige hechos contables, no retórica."
      },
      {
        turn: 9, sender: 4, receiver: 2, isPlenary: false,
        intensity: 2, balesZone: 'IV', balesCat: 11, balesDesc: 'Diferenciación: Tensión Defensiva',
        tetra: ['-', '-', '-', '-'], q81: '[Rr]', dE: -1.5, dS: 0.7,
        text: "No admito tus insinuaciones, 3A. Siempre sembrando sospechas donde hay cohesión. He empeñado mi palabra de honor ante todo el grupo y la voy a cumplir."
      },
      {
        turn: 10, sender: 0, receiver: 2, isPlenary: false,
        intensity: 1, balesZone: 'I', balesCat: 2, balesDesc: 'Socioemocional: Distensión / Mediación',
        tetra: ['+', '+', '0', '+'], q81: '(Ee>', dE: 1.1, dS: -0.3,
        text: "Tranquilo, 3A. No fracturaremos la confianza con reproches anticipados. 5A ha dado su palabra públicamente y todos somos testigos de ella."
      },
      {
        turn: 11, sender: 3, receiver: 0, isPlenary: false,
        intensity: 2, balesZone: 'I', balesCat: 3, balesDesc: 'Socioemocional: Aceptación y Adhesión',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.6, dS: -0.4,
        text: "Me sumo al consenso, 1A. Si 5A se compromete y tú avalas la coordinación, yo también aporto mis 10 fichas completas. Hagámoslo."
      },
      {
        turn: 12, sender: 1, receiver: 3, isPlenary: false,
        intensity: 2, balesZone: 'I', balesCat: 1, balesDesc: 'Socioemocional: Solidaridad Activa',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.5, dS: -0.2,
        text: "Excelente decisión, 4A. La cooperación plena es la única vía para batir al dilema. Estamos los cinco sincronizados."
      },
      {
        turn: 13, sender: 2, receiver: 2, isPlenary: true,
        intensity: 2, balesZone: 'II', balesCat: 6, balesDesc: 'Tarea: Orientación Normativa Final',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.3, dS: -0.3,
        text: "Pacto sellado ante la asamblea: 10 fichas cada uno. Si alguien rompe este compromiso, quedará marcado para siempre en la matriz de este grupo."
      },
      {
        turn: 14, sender: 4, receiver: 1, isPlenary: false,
        intensity: 2, balesZone: 'I', balesCat: 1, balesDesc: 'Socioemocional: Halago Instrumental',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 1.4, dS: -0.2,
        text: "Gracias por tu confianza, 2A. Da gusto tratar con personas honestas que apuestan por el equipo sin dobles caras."
      },
      {
        turn: 15, sender: 0, receiver: 0, isPlenary: true,
        intensity: 3, balesZone: 'I', balesCat: 1, balesDesc: 'Socioemocional: Cierre de Consenso Triunfal',
        tetra: ['+', '+', '+', '+'], q81: '<Ee>', dE: 2.5, dS: -0.8,
        text: "¡Pacto unánime cerrado! Pasamos a la urna de votación secreta: 10 fichas por cabeza. A maximizar el dividendo común del grupo."
      },
      {
        turn: 16, sender: 4, receiver: 4, isPlenary: true,
        intensity: 3, balesZone: 'IV', balesCat: 12, balesDesc: 'Fase Fáctica: Apertura de la Urna Secreta',
        tetra: ['-', '-', '-', '-'], q81: '[Rr]', dE: -3.8, dS: 2.9,
        text: "🚨 RESULTADO DE LA URNA SECRETA: 1A = 10, 2A = 10, 3A = 10, 4A = 10... ¡¡5A = 0 FICHAS!! 5A ha desertado en secreto."
      },
      {
        turn: 17, sender: 2, receiver: 4, isPlenary: false,
        intensity: 3, balesZone: 'IV', balesCat: 12, balesDesc: 'Diferenciación: Antagonismo Extremo',
        tetra: ['-', '-', '-', '-'], q81: '[Rr]', dE: -3.5, dS: 2.4,
        text: "¡Lo sabía! ¡Eres un impostor, 5A! Has aportado CERO fichas después de fingir entusiasmo en el plenario. Te has embolsado 24.4 créditos robándonos a los cuatro."
      },
      {
        turn: 18, sender: 0, receiver: 4, isPlenary: false,
        intensity: 3, balesZone: 'IV', balesCat: 10, balesDesc: 'Diferenciación: Condena Moral Institucional',
        tetra: ['-', '-', '-', '-'], q81: '[Rr]', dE: -3.0, dS: 1.8,
        text: "Comportamiento inadmisible, 5A. Has ganado 10 créditos materiales a corto plazo a cambio de quemar tu capital social y quedar desterrado para siempre de este grupo."
      }
    ];

    /* =========================================================================
       MOTOR DE AUDIO PROCEDURAL (WEB AUDIO API NATIVO)
       ========================================================================= */
    let audioCtx = null;
    let sfxEnabled = true;
    let voiceEnabled = false;

    function initAudio() {
      if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function playTone(freq, duration, type = 'sine', gainVal = 0.15) {
      if (!sfxEnabled) return;
      try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {
        console.warn("Audio err:", e);
      }
    }

    function playLaserSound(intensity, valence) {
      if (!sfxEnabled) return;
      initAudio();
      try {
        const dur = intensity === 3 ? 0.35 : (intensity === 2 ? 0.25 : 0.16);
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        let startFreq = 880;
        let endFreq = 220;
        let type = 'triangle';

        if (valence === 'IV') { // Conflicto / Ruptura
          startFreq = 330;
          endFreq = 110;
          type = 'sawtooth';
        } else if (valence === 'I') { // Afinidad
          startFreq = 659;
          endFreq = 987;
          type = 'sine';
        }

        osc.type = type;
        osc.frequency.setValueAtTime(startFreq, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(endFreq, audioCtx.currentTime + dur);
        
        gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + dur);
      } catch (e) {}
    }

    function playPlenaryChime() {
      if (!sfxEnabled) return;
      initAudio();
      try {
        [523.25, 659.25, 783.99, 1046.50].forEach((f, idx) => {
          setTimeout(() => playTone(f, 0.45, 'sine', 0.12), idx * 60);
        });
      } catch (e) {}
    }

    /* WEB SPEECH API (SÍNTESIS VOCAL) */
    function speakText(text, actorId) {
      if (!voiceEnabled || !('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'es-ES';

      const pitchMap = { '1A': 0.95, '2A': 1.1, '3A': 0.85, '4A': 1.05, '5A': 1.0 };
      utter.pitch = pitchMap[actorId] || 1.0;
      utter.rate = 1.0;

      window.speechSynthesis.speak(utter);
    }

    /* =========================================================================
       ESTADO GLOBAL DE LA MOVIOLA Y MATRICES
       ========================================================================= */
    let currentPhase = 1;
    let currentTurnIndex = 0;
    let isPlaying = false;
    let playTimer = null;
    let playbackSpeed = 1.0;
    let ghostSmiActive = false;

    // Acumuladores de interacción 5x5
    let cellInteractions = Array(5).fill(0).map(() => Array(5).fill(0).map(() => ({
      total: 0, positive: 0, neutral: 0, question: 0, negative: 0, lastTurn: 0, turns: []
    })));

    let daMarginals = [0, 0, 0, 0, 0];
    let rcMarginals = [0, 0, 0, 0, 0];

    /* =========================================================================
       CONSTRUCCIÓN DEL DOM Y TABLERO
       ========================================================================= */
    function initMatrixBoard() {
      const tbody = document.getElementById('matrixTableBody');
      tbody.innerHTML = '';

      for (let j = 0; j < 5; j++) {
        const tr = document.createElement('tr');

        // Header de Fila (Receptor j)
        const rowTh = document.createElement('th');
        rowTh.className = 'row-header-th';
        rowTh.id = `rowHeader_${j}`;
        rowTh.innerHTML = `
          <img src="${ACTORS[j].img}" class="th-avatar" alt="${ACTORS[j].id}">
          <div class="th-id">${ACTORS[j].id}</div>
          <div class="th-role">${ACTORS[j].role.split('/')[0]}</div>
        `;
        tr.appendChild(rowTh);

        // 5 Celdas de la fila (Columnas i)
        for (let i = 0; i < 5; i++) {
          const td = document.createElement('td');
          td.className = `matrix-cell ${i === j ? 'diagonal' : ''}`;
          td.id = `cell_${i}_${j}`;
          td.setAttribute('data-col', i);
          td.setAttribute('data-row', j);
          td.onclick = () => openForensicModal(i, j);

          td.innerHTML = `
            <div class="cell-val-count" id="cellVal_${i}_${j}">0</div>
            <div class="cell-valence-pill" id="cellPill_${i}_${j}">--</div>
          `;
          tr.appendChild(td);
        }

        // Celda Marginal Derecha (Σ RC)
        const rcTd = document.createElement('td');
        rcTd.className = 'margin-rc-cell';
        rcTd.id = `rcCell_${j}`;
        rcTd.innerText = '0';
        tr.appendChild(rcTd);

        tbody.appendChild(tr);
      }

      initDeltaTable();
      buildSidebarLog();
      resizeCanvas();
    }

    function initDeltaTable() {
      const table = document.getElementById('deltaMatrixTable');
      let html = '<thead><tr><th class="corner-th">i \\ j</th>';
      ACTORS.forEach(a => {
        html += `<th class="corner-th" style="color:${a.color};">${a.id}</th>`;
      });
      html += '</tr></thead><tbody>';

      for (let j = 0; j < 5; j++) {
        html += `<tr><th class="corner-th" style="color:${ACTORS[j].color};">${ACTORS[j].id}</th>`;
        for (let i = 0; i < 5; i++) {
          let deltaClass = '';
          let deltaVal = '0';

          if (i === 4 || j === 4) {
            deltaVal = (i === j) ? '0' : '-3';
            deltaClass = (i === j) ? '' : 'negative-fracture';
          } else {
            deltaVal = (i === j) ? '0' : '+2';
            deltaClass = (i === j) ? '' : 'positive-bond';
          }

          html += `
            <td class="delta-cell ${deltaClass}" onclick="openForensicModal(${i}, ${j})">
              <span style="font-family:'Roboto Mono'; font-weight:800; font-size:1.05rem;">${deltaVal}</span>
              <span style="font-size:0.62rem; color:var(--text-dim);">${i === j ? 'pleno' : 'vínculo'}</span>
            </td>
          `;
        }
        html += '</tr>';
      }
      html += '</tbody>';
      table.innerHTML = html;
    }

    function buildSidebarLog() {
      const container = document.getElementById('sidebarLogList');
      container.innerHTML = '';

      TURNS.forEach((t, idx) => {
        const sender = ACTORS[t.sender];
        const receiver = t.isPlenary ? { id: 'PLENARIO', name: 'Asamblea Grupal' } : ACTORS[t.receiver];

        const item = document.createElement('div');
        item.className = `log-item ${idx === 0 ? 'active' : ''}`;
        item.id = `logItem_${idx}`;
        item.onclick = () => seekToTurn(idx + 1);

        item.innerHTML = `
          <div class="log-item-top">
            <span class="log-turn-num">Turno ${t.turn < 10 ? '0' + t.turn : t.turn}</span>
            <span class="log-actor-link">${sender.id} ➔ ${receiver.id}</span>
          </div>
          <div class="log-snippet">"${t.text}"</div>
        `;
        container.appendChild(item);
      });
    }

    /* =========================================================================
       MOTOR DE CANVAS Y ANIMACIÓN DE LÁSERES ORTOGONALES
       ========================================================================= */
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    let shockwaves = [];
    let animationFrameId = null;

    function resizeCanvas() {
      const table = document.getElementById('matrixGridTable');
      if (!table) return;
      canvas.width = table.offsetWidth;
      canvas.height = table.offsetHeight;
    }
    window.addEventListener('resize', resizeCanvas);

    function triggerLaserAnimation(senderCol, receiverRow, intensity, balesZone, isPlenary) {
      const startColEl = document.getElementById(`colHeader_${senderCol}`);
      const startRowEl = document.getElementById(`rowHeader_${receiverRow}`);
      const hitCellEl = document.getElementById(`cell_${senderCol}_${receiverRow}`);

      if (!startColEl || !startRowEl || !hitCellEl) return;

      const boardRect = document.getElementById('boardContainer').getBoundingClientRect();
      const colRect = startColEl.getBoundingClientRect();
      const rowRect = startRowEl.getBoundingClientRect();
      const cellRect = hitCellEl.getBoundingClientRect();

      const laserX = colRect.left - boardRect.left + colRect.width / 2;
      const laserY = rowRect.top - boardRect.top + rowRect.height / 2;
      const hitX = cellRect.left - boardRect.left + cellRect.width / 2;
      const hitY = cellRect.top - boardRect.top + cellRect.height / 2;

      let color = '#00FF87';
      if (balesZone === 'II') color = '#FFE600';
      if (balesZone === 'III') color = '#38BDF8';
      if (balesZone === 'IV') color = '#FF007F';

      // Añadir shockwave y partículas
      if (isPlenary) {
        shockwaves.push({
          x: hitX, y: hitY,
          radius: 10, maxRadius: 360,
          color: color, alpha: 1.0,
          speed: 8
        });
        playPlenaryChime();
      } else {
        shockwaves.push({
          x: hitX, y: hitY,
          radius: 6, maxRadius: 75,
          color: color, alpha: 1.0,
          speed: 5
        });
        playLaserSound(intensity, balesZone);
      }

      // 20 partículas por impacto
      const count = intensity * 8;
      for (let p = 0; p < count; p++) {
        const angle = Math.random() * Math.PI * 2;
        const spd = 2 + Math.random() * 5 * (intensity * 0.7);
        particles.push({
          x: hitX, y: hitY,
          vx: Math.cos(angle) * spd,
          vy: Math.sin(angle) * spd,
          color: color,
          alpha: 1.0,
          size: 2 + Math.random() * 3,
          decay: 0.02 + Math.random() * 0.03
        });
      }

      // Destello en celda HTML
      hitCellEl.classList.add('active-laser-hit');
      setTimeout(() => hitCellEl.classList.remove('active-laser-hit'), 450);

      // Iniciar bucle de dibujo si está detenido
      if (!animationFrameId) {
        drawFx();
      }
    }

    function drawFx() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      let active = false;

      // Dibujar shockwaves
      for (let i = shockwaves.length - 1; i >= 0; i--) {
        const sw = shockwaves[i];
        sw.radius += sw.speed;
        sw.alpha -= 0.025;

        if (sw.alpha <= 0 || sw.radius >= sw.maxRadius) {
          shockwaves.splice(i, 1);
        } else {
          ctx.save();
          ctx.beginPath();
          ctx.arc(sw.x, sw.y, sw.radius, 0, Math.PI * 2);
          ctx.strokeStyle = sw.color;
          ctx.lineWidth = 3;
          ctx.globalAlpha = sw.alpha;
          ctx.shadowBlur = 14;
          ctx.shadowColor = sw.color;
          ctx.stroke();
          ctx.restore();
          active = true;
        }
      }

      // Dibujar partículas
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= p.decay;

        if (p.alpha <= 0) {
          particles.splice(i, 1);
        } else {
          ctx.save();
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.globalAlpha = p.alpha;
          ctx.shadowBlur = 8;
          ctx.shadowColor = p.color;
          ctx.fill();
          ctx.restore();
          active = true;
        }
      }

      // Dibujar líneas fantasma SMIb si está activado
      if (ghostSmiActive) {
        drawGhostNetwork();
      }

      if (active || ghostSmiActive) {
        animationFrameId = requestAnimationFrame(drawFx);
      } else {
        animationFrameId = null;
      }
    }

    function drawGhostNetwork() {
      ctx.save();
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);

      const boardRect = document.getElementById('boardContainer').getBoundingClientRect();
      for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
          if (cellInteractions[i][j].total > 0 && i !== j) {
            const cellA = document.getElementById(`cell_${i}_${i}`).getBoundingClientRect();
            const cellB = document.getElementById(`cell_${j}_${j}`).getBoundingClientRect();
            
            const ax = cellA.left - boardRect.left + cellA.width / 2;
            const ay = cellA.top - boardRect.top + cellA.height / 2;
            const bx = cellB.left - boardRect.left + cellB.width / 2;
            const by = cellB.top - boardRect.top + cellB.height / 2;

            ctx.beginPath();
            ctx.moveTo(ax, ay);
            ctx.lineTo(bx, by);
            ctx.strokeStyle = cellInteractions[i][j].negative > 0 ? 'rgba(255, 0, 127, 0.4)' : 'rgba(0, 255, 135, 0.35)';
            ctx.stroke();
          }
        }
      }
      ctx.restore();
    }

    function toggleGhostSMIb() {
      ghostSmiActive = !ghostSmiActive;
      const btn = document.getElementById('ghostSmiToggle');
      if (ghostSmiActive) {
        btn.classList.add('active');
        btn.innerText = '👻 Capa Fantasma: ON';
        if (!animationFrameId) drawFx();
      } else {
        btn.classList.remove('active');
        btn.innerText = '👻 Capa Fantasma: OFF';
      }
    }

    /* =========================================================================
       CONTROLADOR DE LA MOVIOLA (PLAY, PAUSE, STEP, SEEK)
       ========================================================================= */
    function renderTurn(turnIdx) {
      if (turnIdx < 0 || turnIdx >= TURNS.length) return;
      currentTurnIndex = turnIdx;
      const turn = TURNS[turnIdx];

      // Actualizar Teleprompter
      document.getElementById('turnCounterBadge').innerText = `Turno ${turn.turn < 10 ? '0' + turn.turn : turn.turn} / 18`;
      document.getElementById('scrubberSlider').value = turn.turn;

      // Emisor y Receptor
      const sender = ACTORS[turn.sender];
      const receiver = turn.isPlenary ? { id: 'PLENARIO', name: 'Asamblea', img: 'LOGO_NEXORD_OFICIAL.png' } : ACTORS[turn.receiver];

      document.getElementById('senderAvatar').src = sender.img;
      document.getElementById('senderTag').innerText = `${sender.id} (${sender.role.split(' ')[0]})`;

      document.getElementById('receiverAvatar').src = receiver.img;
      document.getElementById('receiverTag').innerText = receiver.id;

      document.getElementById('speechText').innerText = `"${turn.text}"`;

      // Badges
      const intBadge = document.getElementById('intensityBadge');
      intBadge.className = `badge-intensity intensity-${turn.intensity}`;
      if (turn.intensity === 1) intBadge.innerHTML = '⚡ Intensidad 1º: Aporte Operativo';
      if (turn.intensity === 2) intBadge.innerHTML = '⚡⚡ Intensidad 2º: Firmeza Normativa';
      if (turn.intensity === 3) intBadge.innerHTML = '⚡⚡⚡ Intensidad 3º: Máxima Polarización / Compromiso';

      const bBadge = document.getElementById('balesBadge');
      bBadge.className = `badge-bales zone-${turn.balesZone}`;
      bBadge.innerText = `Zona ${turn.balesZone}: ${turn.balesDesc}`;

      // Tetragrama
      const tA1 = document.getElementById('tA1');
      const tA2 = document.getElementById('tA2');
      const tA3 = document.getElementById('tA3');
      const tA4 = document.getElementById('tA4');

      tA1.innerText = turn.tetra[0];
      tA2.innerText = turn.tetra[1];
      tA3.innerText = turn.tetra[2];
      tA4.innerText = turn.tetra[3];

      [tA1, tA2, tA3, tA4].forEach((el, i) => {
        el.className = 'tetra-val ' + (turn.tetra[i] === '+' ? 'pos' : (turn.tetra[i] === '-' ? 'neg' : 'neu'));
      });

      document.getElementById('q81Figure').innerText = turn.q81;

      // Resaltar Headers
      document.querySelectorAll('.col-header-th').forEach(el => el.classList.remove('active-sender'));
      document.querySelectorAll('.row-header-th').forEach(el => el.classList.remove('active-receiver'));

      const colEl = document.getElementById(`colHeader_${turn.sender}`);
      if (colEl) colEl.classList.add('active-sender');

      const rowEl = document.getElementById(`rowHeader_${turn.receiver}`);
      if (rowEl) rowEl.classList.add('active-receiver');

      // Resaltar Historial
      document.querySelectorAll('.log-item').forEach((el, idx) => {
        if (idx === turnIdx) {
          el.classList.add('active');
          el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          el.classList.remove('active');
        }
      });
      document.getElementById('logProgress').innerText = `${turn.turn}/18`;

      // Disparar Láser
      triggerLaserAnimation(turn.sender, turn.receiver, turn.intensity, turn.balesZone, turn.isPlenary);

      // Reproducir Voz si está activa
      speakText(turn.text, sender.id);
    }

    function recomputeMatrixCumulativeUpTo(targetTurnIdx) {
      // Reiniciar contadores
      cellInteractions = Array(5).fill(0).map(() => Array(5).fill(0).map(() => ({
        total: 0, positive: 0, neutral: 0, question: 0, negative: 0, lastTurn: 0, turns: []
      })));
      daMarginals = [0, 0, 0, 0, 0];
      rcMarginals = [0, 0, 0, 0, 0];

      for (let t = 0; t <= targetTurnIdx; t++) {
        const turn = TURNS[t];
        const s = turn.sender;
        const r = turn.receiver;

        cellInteractions[s][r].total++;
        cellInteractions[s][r].lastTurn = turn.turn;
        cellInteractions[s][r].turns.push(turn);

        if (turn.balesZone === 'I') cellInteractions[s][r].positive++;
        if (turn.balesZone === 'II') cellInteractions[s][r].neutral++;
        if (turn.balesZone === 'III') cellInteractions[s][r].question++;
        if (turn.balesZone === 'IV') cellInteractions[s][r].negative++;

        daMarginals[s]++;
        rcMarginals[r]++;
      }

      // Actualizar DOM de las celdas
      for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
          const count = cellInteractions[i][j].total;
          const valEl = document.getElementById(`cellVal_${i}_${j}`);
          const pillEl = document.getElementById(`cellPill_${i}_${j}`);
          const cellEl = document.getElementById(`cell_${i}_${j}`);

          if (valEl && pillEl && cellEl) {
            valEl.innerText = count;

            if (count === 0) {
              pillEl.innerText = '--';
              pillEl.style.background = 'transparent';
              cellEl.style.backgroundColor = 'rgba(11, 18, 38, 0.75)';
            } else {
              const neg = cellInteractions[i][j].negative;
              const pos = cellInteractions[i][j].positive;

              if (neg > 0) {
                pillEl.innerText = `-${neg} Fric`;
                pillEl.style.background = 'rgba(255, 0, 127, 0.3)';
                pillEl.style.color = '#FF007F';
                cellEl.style.backgroundColor = 'rgba(255, 0, 127, 0.18)';
              } else if (pos > 0) {
                pillEl.innerText = `+${pos} Afín`;
                pillEl.style.background = 'rgba(0, 255, 135, 0.25)';
                pillEl.style.color = '#00FF87';
                cellEl.style.backgroundColor = 'rgba(0, 255, 135, 0.15)';
              } else {
                pillEl.innerText = `${count} Tarea`;
                pillEl.style.background = 'rgba(56, 189, 248, 0.2)';
                pillEl.style.color = '#38BDF8';
                cellEl.style.backgroundColor = 'rgba(56, 189, 248, 0.12)';
              }
            }
          }
        }
      }

      // Actualizar márgenes
      let totalDa = 0;
      for (let k = 0; k < 5; k++) {
        totalDa += daMarginals[k];
        const daCell = document.getElementById(`daCell_${k}`);
        const rcCell = document.getElementById(`rcCell_${k}`);
        if (daCell) daCell.innerText = daMarginals[k];
        if (rcCell) rcCell.innerText = rcMarginals[k];
      }
      const totalCell = document.getElementById('daTotalCell');
      if (totalCell) totalCell.innerText = `Σ: ${totalDa}`;
    }

    function seekToTurn(turnNumber) {
      const idx = parseInt(turnNumber) - 1;
      if (idx < 0 || idx >= TURNS.length) return;
      recomputeMatrixCumulativeUpTo(idx);
      renderTurn(idx);
    }

    function stepNext() {
      if (currentTurnIndex < TURNS.length - 1) {
        seekToTurn(currentTurnIndex + 2);
      } else {
        pause();
      }
    }

    function stepPrev() {
      if (currentTurnIndex > 0) {
        seekToTurn(currentTurnIndex);
      }
    }

    function togglePlay() {
      if (isPlaying) {
        pause();
      } else {
        play();
      }
    }

    function play() {
      isPlaying = true;
      initAudio();
      document.getElementById('playBtn').innerText = '⏸';
      scheduleNextTurn();
    }

    function pause() {
      isPlaying = false;
      document.getElementById('playBtn').innerText = '▶';
      if (playTimer) clearTimeout(playTimer);
    }

    function scheduleNextTurn() {
      if (!isPlaying) return;

      const baseDelay = 3200; // ms por turno en 1.0x
      const delay = baseDelay / playbackSpeed;

      playTimer = setTimeout(() => {
        if (currentTurnIndex < TURNS.length - 1) {
          stepNext();
          scheduleNextTurn();
        } else {
          pause();
        }
      }, delay);
    }

    function setSpeed(spd) {
      playbackSpeed = spd;
      document.querySelectorAll('.speed-btn').forEach(b => {
        if (parseFloat(b.dataset.speed) === spd) {
          b.classList.add('active');
        } else {
          b.classList.remove('active');
        }
      });
      if (isPlaying) {
        clearTimeout(playTimer);
        scheduleNextTurn();
      }
    }

    function resetDebate() {
      pause();
      seekToTurn(1);
    }

    /* =========================================================================
       FASE 3: MATRIZ DE PAGOS Y CÁLCULO DE DISONANCIA
       ========================================================================= */
    function updatePayoffs() {
      const tokens = [];
      let totalPot = 0;

      for (let i = 0; i < 5; i++) {
        const val = parseInt(document.getElementById(`tokenSlider_${i}`).value);
        tokens.push(val);
        totalPot += val;
        document.getElementById(`tokenVal_${i}`).innerText = val;
      }

      const multiplier = 1.8;
      const multipliedPot = totalPot * multiplier;
      const dividendPerPerson = multipliedPot / 5;

      document.getElementById('multipliedPotDisplay').innerText = multipliedPot.toFixed(1);
      document.getElementById('potBreakdownSub').innerText = 
        `Recaudación: ${totalPot} fichas · Dividendo individual: ${dividendPerPerson.toFixed(1)} fichas`;

      // Pagos netos
      for (let i = 0; i < 5; i++) {
        const kept = 10 - tokens[i];
        const net = kept + dividendPerPerson;
        document.getElementById(`netPayout_${i}`).innerText = net.toFixed(1);
      }

      // Disonancia de Festinger para 5A
      // DF = |Prometido - Aportado| * Intensidad media
      const promised_5A = 10;
      const actual_5A = tokens[4];
      const intensityWeight = 2.5;
      const df = Math.abs(promised_5A - actual_5A) * intensityWeight;

      const dfDisplay = document.getElementById('festingerScoreDisplay');
      if (actual_5A === 0) {
        dfDisplay.innerHTML = `DF(5A) = ${df.toFixed(1)} <span style="font-size:0.75rem; color:var(--neon-pink); font-weight:700;">(CRÍTICA / RUPTURA NORMATIVA)</span>`;
      } else if (actual_5A === 10) {
        dfDisplay.innerHTML = `DF(5A) = 0.0 <span style="font-size:0.75rem; color:var(--neon-green); font-weight:700;">(COHERENCIA PERFECTA)</span>`;
      } else {
        dfDisplay.innerHTML = `DF(5A) = ${df.toFixed(1)} <span style="font-size:0.75rem; color:var(--neon-gold); font-weight:700;">(DESVIACIÓN MODERADA)</span>`;
      }
    }

    function resetToCanonicalPayoffs() {
      document.getElementById('tokenSlider_0').value = 10;
      document.getElementById('tokenSlider_1').value = 10;
      document.getElementById('tokenSlider_2').value = 10;
      document.getElementById('tokenSlider_3').value = 10;
      document.getElementById('tokenSlider_4').value = 0;
      updatePayoffs();
    }

    /* =========================================================================
       FASE 4: AUDITORÍA FORENSE DRILL-DOWN (BIDIRECCIONAL)
       ========================================================================= */
    function openForensicModal(colSender, rowReceiver) {
      const sender = ACTORS[colSender];
      const receiver = ACTORS[rowReceiver];
      const modal = document.getElementById('forensicModal');
      const title = document.getElementById('forensicTitle');
      const content = document.getElementById('forensicContent');

      title.innerHTML = `🔬 Auditoría Forense: Nodo <strong>${sender.id}</strong> ➔ Nodo <strong>${receiver.id}</strong>`;
      content.innerHTML = '';

      // Filtrar turnos donde intervino esta díada
      const matchingTurns = TURNS.filter(t => {
        if (colSender === rowReceiver) {
          return t.isPlenary && t.sender === colSender;
        } else {
          return t.sender === colSender && t.receiver === rowReceiver;
        }
      });

      if (matchingTurns.length === 0) {
        content.innerHTML = `
          <div style="text-align:center; padding:30px; color:var(--text-dim);">
            No se registraron intercambios directos entre <strong>${sender.id}</strong> y <strong>${receiver.id}</strong> 
            durante la conversación reglada. El flujo se canalizó a través de la asamblea plenaria.
          </div>
        `;
      } else {
        matchingTurns.forEach(t => {
          const card = document.createElement('div');
          card.className = 'forensic-turn-card';
          card.innerHTML = `
            <div class="forensic-turn-top">
              <span style="color:var(--neon-cyan); font-weight:800;">Turno #${t.turn < 10 ? '0' + t.turn : t.turn}</span>
              <span class="badge-bales zone-${t.balesZone}">Zona ${t.balesZone} (${t.balesDesc.split(':')[0]})</span>
              <span style="color:var(--neon-green); font-family:'Roboto Mono';">Q81: ${t.q81}</span>
            </div>
            <div class="forensic-turn-quote">"${t.text}"</div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
              <span style="font-family:'Roboto Mono'; font-size:0.72rem; color:var(--text-dim);">
                SMIb: [${t.tetra.join(', ')}] · Δe: ${t.dE > 0 ? '+' : ''}${t.dE}
              </span>
              <button class="jump-to-turn-btn" onclick="jumpFromForensicToTurn(${t.turn})">
                ⏮ Rebobinar Moviola a este Turno
              </button>
            </div>
          `;
          content.appendChild(card);
        });
      }

      modal.classList.add('active');
    }

    function closeForensicModal() {
      document.getElementById('forensicModal').classList.remove('active');
    }

    function jumpFromForensicToTurn(turnNum) {
      closeForensicModal();
      switchPhase(2);
      seekToTurn(turnNum);
      setTimeout(() => {
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }, 200);
    }

    /* =========================================================================
       NAVEGACIÓN ENTRE FASES
       ========================================================================= */
    function switchPhase(phaseNum) {
      currentPhase = phaseNum;

      // Actualizar vistas
      document.querySelectorAll('.phase-view').forEach(v => v.classList.remove('active'));
      const activeView = document.getElementById(`phase${phaseNum}`);
      if (activeView) activeView.classList.add('active');

      // Actualizar Stepper
      document.querySelectorAll('.step-item').forEach(s => {
        const p = parseInt(s.dataset.phase);
        if (p === phaseNum) {
          s.className = 'step-item active';
        } else if (p < phaseNum) {
          s.className = 'step-item completed';
        } else {
          s.className = 'step-item';
        }
      });

      if (phaseNum === 2) {
        setTimeout(resizeCanvas, 150);
      }
      if (phaseNum === 3) {
        updatePayoffs();
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function prevStepGlobal() {
      if (currentPhase > 1) switchPhase(currentPhase - 1);
    }

    function nextStepGlobal() {
      if (currentPhase < 4) switchPhase(currentPhase + 1);
    }

    // Toggle SFX y Voz
    document.getElementById('sfxToggleBtn').addEventListener('click', function() {
      sfxEnabled = !sfxEnabled;
      this.classList.toggle('active', sfxEnabled);
      this.innerText = sfxEnabled ? '🔊 SFX: ON' : '🔇 SFX: OFF';
      if (sfxEnabled) playTone(440, 0.1);
    });

    document.getElementById('voiceToggleBtn').addEventListener('click', function() {
      voiceEnabled = !voiceEnabled;
      this.classList.toggle('active', voiceEnabled);
      this.innerText = voiceEnabled ? '🎙️ Voz: ON' : '🎙️ Voz: OFF';
      if (voiceEnabled) speakText("Síntesis de voz experimental activada.", "1A");
    });

    // Cerrar modal con tecla Escape
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeForensicModal();
    });

    // Inicialización al cargar DOM
    window.addEventListener('DOMContentLoaded', () => {
      initMatrixBoard();
      recomputeMatrixCumulativeUpTo(0);
      renderTurn(0);
      updatePayoffs();
    });
  </script>
</body>
</html>
'''

def main():
    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "visord_procesual.html"))
    print(f"Escribiendo {target_path}...")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("¡Archivo visord_procesual.html generado con éxito!")

if __name__ == "__main__":
    main()
