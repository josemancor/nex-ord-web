#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEXORD 2026 - MASTER AUDIO: OCTETO CON IDENTIDADES ACÚSTICAS ("PEDRO Y EL LOBO")
Cada sujeto (1A a 8A) posee un instrumento orquestal físico único:
1A: Contrabajo Imperial (Madera subgrave y pizzicato noble)
2A: Fagot Socarrón (Lengüeta doble nasal y articulación terrenal)
3A: Trompa / Corno Francés (Metal noble y cálido)
4A: Viola Cantabile (Cuerda aterciopelada lírica)
5A: Clarinete Ámbar (Armónicos impares y timbre líquido)
6A: Oboe Incisivo (Caña penetrante y melancólica)
7A: Flauta de Cristal (Viento ágil y gorjeo de pájaro)
8A: Violín Solista / Virtuoso (Cuerda brillante y vibrato luminoso)

Genera el archivo .mp3 y .wav con alta fidelidad estéreo.
"""

import os
import sys
import subprocess
import numpy as np
import scipy.signal as signal
import wave

SAMPLE_RATE = 44100

# 8 Sujetos con sus Identidades Acústicas Singulares
CHARACTERS = [
    {
        "id": 1, "code": "1A", "name": "El Contrabajo Imperial",
        "fMin": 130.81, "fBase": 164.81, "fMax": 196.00, "pan": -0.75,
        "role": "El Patriarca / Voz Subgrave de Madera"
    },
    {
        "id": 2, "code": "2A", "name": "El Fagot Socarrón",
        "fMin": 164.81, "fBase": 196.00, "fMax": 246.94, "pan": -0.55,
        "role": "El Abuelo Reflexivo / Lengüeta Doble"
    },
    {
        "id": 3, "code": "3A", "name": "La Trompa Noble",
        "fMin": 196.00, "fBase": 261.63, "fMax": 293.66, "pan": -0.35,
        "role": "El Guardián Solemne / Metal Cálido"
    },
    {
        "id": 4, "code": "4A", "name": "La Viola Cantabile",
        "fMin": 220.00, "fBase": 293.66, "fMax": 329.63, "pan": -0.15,
        "role": "El Pensador Íntimo / Cuerda Aterciopelada"
    },
    {
        "id": 5, "code": "5A", "name": "El Clarinete Ámbar",
        "fMin": 246.94, "fBase": 329.63, "fMax": 369.99, "pan":  0.15,
        "role": "El Mediador Ágil / Madera Cilíndrica"
    },
    {
        "id": 6, "code": "6A", "name": "El Oboe Incisivo",
        "fMin": 293.66, "fBase": 392.00, "fMax": 440.00, "pan":  0.35,
        "role": "La Voz Inquieta / Caña Penetrante"
    },
    {
        "id": 7, "code": "7A", "name": "La Flauta de Cristal",
        "fMin": 349.23, "fBase": 440.00, "fMax": 523.25, "pan":  0.55,
        "role": "El Pajarillo Alado / Viento Sibilante"
    },
    {
        "id": 8, "code": "8A", "name": "El Violín Virtuoso",
        "fMin": 440.00, "fBase": 523.25, "fMax": 659.25, "pan":  0.75,
        "role": "El Héroe Luminoso / Canto Soprano"
    }
]

# -------------------------------------------------------------
# SÍNTESIS FÍSICA INDIVIDUAL DE CADA UNO DE LOS 8 INSTRUMENTOS
# -------------------------------------------------------------

def synth_contrabass(freq, dur, is_rejection=False):
    """1A: Contrabajo Imperial (madera grave, subarmónicos y resonancia profunda)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    if is_rejection:
        freq_curve = freq * (1.0 - 0.09 * (t / dur)**0.7)
    else:
        freq_curve = freq * np.ones(n)
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    # Fundamental potente + armónicos de cuerda gruesa de tripa
    sig = (
        1.10 * np.sin(phase) +
        0.80 * signal.sawtooth(phase) +
        0.40 * np.sin(2 * phase) +
        0.20 * np.sin(3 * phase)
    )
    # Ataque de frote profundo
    att = int(min(0.06, dur * 0.2) * SAMPLE_RATE)
    dec = int(min(0.15, dur * 0.3) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**2, np.linspace(1.0, 0.85, sus), np.linspace(0.85, 0, dec)**2])
    sig = sig[:n] * env[:n]
    # Filtro paso-bajo resonante de caja de contrabajo
    try:
        b, a = signal.butter(2, min(420.0, freq * 2.8) / (SAMPLE_RATE / 2), btype='lowpass')
        sig = signal.lfilter(b, a, sig)
    except Exception:
        pass
    return sig * 0.32

def synth_bassoon(freq, dur, is_rejection=False):
    """2A: Fagot Socarrón (lengüeta doble, pulso estrecho, formantes nasales)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    if is_rejection:
        freq_curve = freq * (1.0 - 0.08 * (t / dur)**0.8)
    else:
        freq_curve = freq * np.ones(n)
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    # Onda de pulso estrecho (30% duty) rica en armónicos nasales
    duty = 0.30
    sig = signal.square(phase, duty=duty) * 0.7 + 0.3 * np.sin(phase)
    
    att = int(min(0.04, dur * 0.15) * SAMPLE_RATE)
    dec = int(min(0.08, dur * 0.25) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**1.5, np.linspace(1.0, 0.8, sus), np.linspace(0.8, 0, dec)**1.5])
    sig = sig[:n] * env[:n]
    # Formantes típicos de fagot (480 Hz y 1150 Hz)
    try:
        b1, a1 = signal.butter(1, [380 / (SAMPLE_RATE/2), 620 / (SAMPLE_RATE/2)], btype='bandpass')
        f1 = signal.lfilter(b1, a1, sig)
        b2, a2 = signal.butter(1, [950 / (SAMPLE_RATE/2), 1400 / (SAMPLE_RATE/2)], btype='bandpass')
        f2 = signal.lfilter(b2, a2, sig)
        sig = 0.4 * sig + 0.4 * f1 + 0.2 * f2
    except Exception:
        pass
    return sig * 0.26

def synth_french_horn(freq, dur, is_rejection=False):
    """3A: Trompa Noble (metal cálido y redondo, campana de bronce)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    if is_rejection:
        freq_curve = freq * (1.0 - 0.07 * (t / dur))
    else:
        freq_curve = freq * np.ones(n)
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    sig = 0.65 * signal.sawtooth(phase, width=0.5) + 0.45 * np.sin(phase) + 0.25 * np.sin(2 * phase)
    att = int(min(0.07, dur * 0.25) * SAMPLE_RATE)
    dec = int(min(0.12, dur * 0.3) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**1.8, np.linspace(1.0, 0.9, sus), np.linspace(0.9, 0, dec)**2])
    sig = sig[:n] * env[:n]
    try:
        b, a = signal.butter(2, min(750.0, freq * 3.0) / (SAMPLE_RATE / 2), btype='lowpass')
        sig = signal.lfilter(b, a, sig)
    except Exception:
        pass
    return sig * 0.28

def synth_viola(freq, dur, is_rejection=False):
    """4A: Viola Cantabile (cuerda frotada media aterciopelada con vibrato lento)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    vib = 4.0 * np.sin(2 * np.pi * 4.8 * t) # Vibrato lírico de viola a 4.8 Hz
    if is_rejection:
        freq_curve = (freq + vib) * (1.0 - 0.08 * (t / dur))
    else:
        freq_curve = freq + vib
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    sig = (
        1.00 * np.sin(phase) +
        0.60 * signal.sawtooth(phase) +
        0.35 * np.sin(2 * phase) +
        0.20 * np.sin(3 * phase)
    )
    att = int(min(0.05, dur * 0.2) * SAMPLE_RATE)
    dec = int(min(0.10, dur * 0.25) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.sin(np.linspace(0, np.pi/2, att)), np.linspace(1.0, 0.88, sus), np.sin(np.linspace(np.pi/2, 0, dec))])
    sig = sig[:n] * env[:n]
    try:
        b, a = signal.butter(2, [min(1100, freq*2)/(SAMPLE_RATE/2), min(2200, freq*6)/(SAMPLE_RATE/2)], btype='bandpass')
        f_sig = signal.lfilter(b, a, sig)
        sig = 0.55 * sig + 0.45 * f_sig
    except Exception:
        pass
    return sig * 0.24

def synth_clarinet(freq, dur, is_rejection=False):
    """5A: Clarinete Ámbar (predominio de armónicos impares, timbre líquido)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    if is_rejection:
        freq_curve = freq * (1.0 - 0.06 * (t / dur))
    else:
        freq_curve = freq * np.ones(n)
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    # Tubo cilíndrico cerrado: armónicos 1, 3, 5, 7 predominantes
    sig = (
        1.00 * np.sin(phase) +
        0.10 * np.sin(2 * phase) + # Par mínimo
        0.60 * np.sin(3 * phase) + # Impar fuerte
        0.05 * np.sin(4 * phase) +
        0.35 * np.sin(5 * phase) + # Impar
        0.18 * np.sin(7 * phase)
    )
    att = int(min(0.04, dur * 0.18) * SAMPLE_RATE)
    dec = int(min(0.09, dur * 0.25) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**2, np.linspace(1.0, 0.92, sus), np.linspace(0.92, 0, dec)**1.8])
    sig = sig[:n] * env[:n]
    try:
        b, a = signal.butter(2, min(1600.0, freq * 4.2) / (SAMPLE_RATE / 2), btype='lowpass')
        sig = signal.lfilter(b, a, sig)
    except Exception:
        pass
    return sig * 0.25

def synth_oboe(freq, dur, is_rejection=False):
    """6A: Oboe Incisivo (lengüeta doble penetrante, mordiente picado, formante 2200 Hz)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    vib = 3.5 * np.sin(2 * np.pi * 5.8 * t) # Vibrato incisivo a 5.8 Hz
    if is_rejection:
        freq_curve = (freq + vib) * (1.0 - 0.09 * (t / dur))
    else:
        freq_curve = freq + vib
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    sig = 0.70 * signal.sawtooth(phase) + 0.35 * np.sin(phase) + 0.30 * signal.sawtooth(2 * phase)
    att = int(min(0.025, dur * 0.12) * SAMPLE_RATE)
    dec = int(min(0.07, dur * 0.22) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**1.2, np.linspace(1.0, 0.85, sus), np.linspace(0.85, 0, dec)**1.5])
    sig = sig[:n] * env[:n]
    # Formante penetrante de oboe
    try:
        b, a = signal.butter(2, [1800 / (SAMPLE_RATE/2), 2600 / (SAMPLE_RATE/2)], btype='bandpass')
        f_sig = signal.lfilter(b, a, sig)
        sig = 0.5 * sig + 0.5 * f_sig
    except Exception:
        pass
    return sig * 0.23

def synth_flute_crystal(freq, dur, is_rejection=False):
    """7A: Flauta de Cristal (viento ágil, aire sibilante, pureza aguda)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    # Ligera inflexión gorjeante ascendente
    if is_rejection:
        freq_curve = freq * (1.0 - 0.06 * (t / dur))
    else:
        freq_curve = freq * (1.0 + 0.025 * np.sin(2 * np.pi * 6.0 * t))
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    breath = np.random.normal(0, 0.025, n)
    
    sig = np.sin(phase) + 0.22 * np.sin(2 * phase) + 0.08 * np.sin(3 * phase) + breath
    att = int(min(0.05, dur * 0.2) * SAMPLE_RATE)
    dec = int(min(0.08, dur * 0.25) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**2, np.linspace(1.0, 0.9, sus), np.linspace(0.9, 0, dec)**2])
    return sig[:n] * env[:n] * 0.22

def synth_solo_violin(freq, dur, is_rejection=False):
    """8A: Violín Virtuoso (canto soprano luminoso, armónicos altos de madera y vibrato 5.5 Hz)"""
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    vib = 5.2 * np.sin(2 * np.pi * 5.5 * t)
    if is_rejection:
        freq_curve = (freq + vib) * (1.0 - 0.08 * (t / dur))
    else:
        freq_curve = freq + vib
    phase = 2 * np.pi * np.cumsum(freq_curve) / SAMPLE_RATE
    
    sig = (
        1.00 * np.sin(phase) +
        0.58 * np.sin(2 * phase) +
        0.38 * np.sin(3 * phase) +
        0.24 * np.sin(4 * phase) +
        0.15 * np.sin(5 * phase) +
        0.10 * np.sin(6 * phase)
    )
    att = int(min(0.045, dur * 0.18) * SAMPLE_RATE)
    dec = int(min(0.08, dur * 0.22) * SAMPLE_RATE)
    sus = n - att - dec
    env = np.concatenate([np.sin(np.linspace(0, np.pi/2, att))**1.5, np.linspace(1.0, 0.9, sus), np.sin(np.linspace(np.pi/2, 0, dec))**1.8])
    sig = sig[:n] * env[:n]
    try:
        b, a = signal.butter(2, [min(2200, freq*2)/(SAMPLE_RATE/2), min(4200, freq*6)/(SAMPLE_RATE/2)], btype='bandpass')
        f_sig = signal.lfilter(b, a, sig)
        sig = 0.55 * sig + 0.45 * f_sig
    except Exception:
        pass
    return sig * 0.24

# Despachador de síntesis según el sujeto
SYNTH_MAP = [
    synth_contrabass,   # 1A
    synth_bassoon,      # 2A
    synth_french_horn,  # 3A
    synth_viola,        # 4A
    synth_clarinet,     # 5A
    synth_oboe,         # 6A
    synth_flute_crystal,# 7A
    synth_solo_violin   # 8A
]

def play_subject_instrument(s_idx, freq, dur, is_rejection=False):
    func = SYNTH_MAP[s_idx % len(SYNTH_MAP)]
    return func(freq, dur, is_rejection=is_rejection)

def get_band_freq(s_idx, rank_char, polarity):
    b = CHARACTERS[s_idx]
    if polarity > 0: # Elección: Cúspide y orden descendente
        if rank_char == 'A':
            return b['fMax']
        elif rank_char == 'B':
            return b['fBase'] * 1.18
        else: # 'C'
            return b['fBase'] * 1.08
    elif polarity < 0: # Rechazo: Descenso hacia el suelo
        if rank_char == 'c':
            return b['fBase'] * 0.92
        elif rank_char == 'b':
            return b['fBase'] * 0.82
        else: # 'a'
            return b['fMin']
    else: # Neutro '0'
        return b['fBase']

def synth_zen_bowl(freq, dur):
    n = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n, False)
    decay = np.exp(-t * 2.5)
    sig = (np.sin(2 * np.pi * freq * t) + 0.18 * np.sin(2 * np.pi * freq * 2.0 * t)) * decay
    return sig * 0.20

def add_note(buffer, sig, start_time, pan=0.0):
    start_idx = int(start_time * SAMPLE_RATE)
    n = len(sig)
    end_idx = min(start_idx + n, len(buffer))
    l = end_idx - start_idx
    if l <= 0: return
    angle = (pan + 1.0) * (np.pi / 4.0)
    buffer[start_idx:end_idx, 0] += sig[:l] * np.cos(angle)
    buffer[start_idx:end_idx, 1] += sig[:l] * np.sin(angle)

def apply_reverb(buffer):
    imp_len = int(SAMPLE_RATE * 1.8)
    t = np.linspace(0, 1.8, imp_len, False)
    hl = np.random.normal(0, 1, imp_len) * np.exp(-t * 4.2)
    hr = np.random.normal(0, 1, imp_len) * np.exp(-t * 4.2)
    b, a = signal.butter(1, 0.14)
    hl = signal.lfilter(b, a, hl); hl /= (np.max(np.abs(hl)) + 1e-6)
    hr = signal.lfilter(b, a, hr); hr /= (np.max(np.abs(hr)) + 1e-6)
    rl = signal.fftconvolve(buffer[:, 0], hl)[:len(buffer)] * 0.22
    rr = signal.fftconvolve(buffer[:, 1], hr)[:len(buffer)] * 0.22
    out = np.zeros_like(buffer)
    out[:, 0] = buffer[:, 0] * 0.84 + rl
    out[:, 1] = buffer[:, 1] * 0.84 + rr
    return out

def build_identified_master_recording():
    total_dur = 64.0 # 64 segundos de desfile orquestal serial
    total_samples = int(total_dur * SAMPLE_RATE)
    buf = np.zeros((total_samples, 2), dtype=np.float32)
    
    print("🎭 PARTE 1: DESFILE DE IDENTIDADES ACÚSTICAS ('Pedro y el Lobo') (0s - 14s)...")
    # Cada uno de los 8 personajes se presenta tocando su motivo identitario personal
    t = 0.2
    for i, c in enumerate(CHARACTERS):
        pan = c['pan']
        print(f"   -> Presentación Sujeto {c['code']}: {c['name']} ({c['role']})")
        # Motivo de llamada del instrumento: nota base -> nota cúspide -> nota base
        note1 = play_subject_instrument(i, c['fBase'], 0.40)
        note2 = play_subject_instrument(i, c['fMax'], 0.55)
        note3 = play_subject_instrument(i, c['fBase'] * 1.12, 0.45)
        add_note(buf, note1, t, pan)
        add_note(buf, note2, t + 0.35, pan)
        add_note(buf, note3, t + 0.80, pan)
        t += 1.55
        
    print("🎻 PARTE 2: DIÁLOGOS DE PERSONAJES Y RECIPROCIDADES (14s - 30s)...")
    # Diálogo 1: 1A (Contrabajo) y 8A (Violín Virtuoso) -> Elección mutua <Ee>
    t = 13.5
    add_note(buf, play_subject_instrument(0, CHARACTERS[0]['fMax'], 0.55), t, CHARACTERS[0]['pan'])
    add_note(buf, play_subject_instrument(7, CHARACTERS[7]['fMax'], 0.55), t + 0.45, CHARACTERS[7]['pan'])
    # Dúo armónico de Contrabajo y Violín entrelazados
    add_note(buf, play_subject_instrument(0, CHARACTERS[0]['fBase'], 1.6), t + 0.95, CHARACTERS[0]['pan'])
    add_note(buf, play_subject_instrument(7, CHARACTERS[7]['fMax'], 1.6), t + 0.95, CHARACTERS[7]['pan'])
    
    # Diálogo 2: 2A (Fagot) y 6A (Oboe) -> Choque de lengüetas dobles y fricción [Rr]
    t = 17.5
    add_note(buf, play_subject_instrument(1, CHARACTERS[1]['fMin'], 0.45, is_rejection=True), t, CHARACTERS[1]['pan'])
    add_note(buf, play_subject_instrument(5, CHARACTERS[5]['fMin'], 0.48, is_rejection=True), t + 0.42, CHARACTERS[5]['pan'])
    # Fricción disonante
    add_note(buf, play_subject_instrument(1, CHARACTERS[1]['fMin'], 1.5, is_rejection=True) * 0.8, t + 0.90, CHARACTERS[1]['pan'])
    add_note(buf, play_subject_instrument(5, CHARACTERS[5]['fMin'] * 1.05, 1.5, is_rejection=True) * 0.8, t + 0.90, CHARACTERS[5]['pan'])
    
    # Diálogo 3: 3A (Trompa) y 7A (Flauta) -> Contrapunto aire y metal
    t = 21.5
    add_note(buf, play_subject_instrument(2, CHARACTERS[2]['fMax'], 0.65), t, CHARACTERS[2]['pan'])
    add_note(buf, play_subject_instrument(6, CHARACTERS[6]['fMax'], 0.65), t + 0.35, CHARACTERS[6]['pan'])
    
    # Diálogo 4: 4A (Viola) y 5A (Clarinete) -> Dúo de cámara íntimo
    t = 25.5
    add_note(buf, play_subject_instrument(3, CHARACTERS[3]['fMax'], 0.80), t, CHARACTERS[3]['pan'])
    add_note(buf, play_subject_instrument(4, CHARACTERS[4]['fMax'], 0.80), t + 0.25, CHARACTERS[4]['pan'])
    
    print("🎹 PARTE 3: GRAN SECUENCIA SERIAL POLIFÓNICA (30s - 54s)...")
    # Los 8 personajes cantan sus elecciones y rechazos en orden descendente
    t_curr = 29.5
    ranks = ['A', 'B', 'C', '0', 'c', 'b', 'a']
    
    for s_idx in range(8):
        c = CHARACTERS[s_idx]
        pan = c['pan']
        
        for r_char in ranks:
            pol = 1 if r_char in ['A', 'B', 'C'] else (-1 if r_char in ['c', 'b', 'a'] else 0)
            f = get_band_freq(s_idx, r_char, pol)
            dur_note = 0.22 if pol != 0 else 0.32
            
            if pol > 0:
                # El instrumento canta su preferencia en orden descendente
                sig = play_subject_instrument(s_idx, f, dur_note)
            elif pol < 0:
                # El instrumento cae con aspereza o glissando hacia su suelo
                sig = play_subject_instrument(s_idx, f, dur_note * 1.25, is_rejection=True)
            else:
                sig = synth_zen_bowl(f, dur_note * 1.5)
                
            add_note(buf, sig, t_curr, pan)
            t_curr += dur_note * 0.78
            
        t_curr += 0.30
        
    print("🕊️ PARTE 4: CODA POLIFÓNICA Y RESONANCIA FINAL (54s - 64s)...")
    t_coda = 54.0
    for s_idx in range(8):
        c = CHARACTERS[s_idx]
        sig_voice = play_subject_instrument(s_idx, c['fBase'], 8.0) * 0.35
        sig_zen = synth_zen_bowl(c['fBase'], 8.5) * 0.30
        add_note(buf, sig_voice, t_coda + s_idx * 0.18, c['pan'])
        add_note(buf, sig_zen, t_coda + s_idx * 0.18, c['pan'])
        
    print("🌌 Aplicando reverberación estéreo de sala de conciertos...")
    stereo_out = apply_reverb(buf)
    
    # Normalizar a -1.0 dB
    peak = np.max(np.abs(stereo_out))
    if peak > 0:
        stereo_out = stereo_out * ((10 ** (-1.0 / 20.0)) / peak)
        
    int16_out = np.int16(np.clip(stereo_out * 32767.0, -32768, 32767))
    
    # Rutas de guardado
    wav_promo = "05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.wav"
    mp3_promo = "05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.mp3"
    
    wav_root = "/Users/jmcor/Desktop/SOC_ORD_Project/GRABACION_OCTETO_N8_IDENTIDAD_ACUSTICA_NEXORD.wav"
    mp3_root = "/Users/jmcor/Desktop/SOC_ORD_Project/GRABACION_OCTETO_N8_IDENTIDAD_ACUSTICA_NEXORD.mp3"
    
    print(f"💾 Guardando archivo WAV en {wav_promo}...")
    with wave.open(wav_promo, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(int16_out.tobytes())
        
    print(f"🔄 Convirtiendo a MP3 mediante ffmpeg (256 kbps, estéreo)...")
    subprocess.run([
        '/usr/local/bin/ffmpeg', '-y', '-i', wav_promo,
        '-b:a', '256k',
        '-metadata', 'title=NEXORD Sinfonía del Octeto N=8 (Identidades Acústicas)',
        '-metadata', 'artist=VISORD & NEXORD Engine',
        '-metadata', 'album=Sociometría Serial Pedro y el Lobo',
        '-metadata', 'year=2026',
        mp3_promo
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Copiar a la raíz del proyecto para acceso directo del usuario
    import shutil
    shutil.copyfile(wav_promo, wav_root)
    shutil.copyfile(mp3_promo, mp3_root)
    print(f"✅ Archivos MP3 y WAV copiados a la raíz del proyecto:")
    print(f"   -> {mp3_root}")
    print(f"   -> {wav_root}")

if __name__ == "__main__":
    build_identified_master_recording()
