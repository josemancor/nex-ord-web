#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEXORD 2026 - MASTER AUDIO SYNTHESIZER: OCTETO SINFÓNICO (N=8)
Serialismo Integral Cuadridimensional:
Sujeto - Orden - Posición - Preferencia ... [Reciprocidad]
Genera:
- 05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.wav
- 05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.mp3
"""

import os
import sys
import subprocess
import numpy as np
import scipy.signal as signal
import wave

SAMPLE_RATE = 44100

# 8 Bandas de Oscilación Determinadas del Octeto (de Bajo a Soprano)
SUBJECT_BANDS = [
    {"id": 1, "code": "1A", "fMin": 130.81, "fBase": 164.81, "fMax": 196.00, "pan": -0.75, "instrument": "Contrabajo / Bajo profundo"},
    {"id": 2, "code": "2A", "fMin": 164.81, "fBase": 196.00, "fMax": 246.94, "pan": -0.55, "instrument": "Violonchelo / Barítono"},
    {"id": 3, "code": "3A", "fMin": 196.00, "fBase": 261.63, "fMax": 293.66, "pan": -0.35, "instrument": "Fagot / Tenor bajo"},
    {"id": 4, "code": "4A", "fMin": 220.00, "fBase": 293.66, "fMax": 329.63, "pan": -0.15, "instrument": "Viola / Tenor alto"},
    {"id": 5, "code": "5A", "fMin": 246.94, "fBase": 329.63, "fMax": 369.99, "pan":  0.15, "instrument": "Corno Francés / Contralto"},
    {"id": 6, "code": "6A", "fMin": 293.66, "fBase": 392.00, "fMax": 440.00, "pan":  0.35, "instrument": "Clarinete / Mezzosoprano"},
    {"id": 7, "code": "7A", "fMin": 349.23, "fBase": 440.00, "fMax": 523.25, "pan":  0.55, "instrument": "Violín II / Soprano dramática"},
    {"id": 8, "code": "8A", "fMin": 440.00, "fBase": 523.25, "fMax": 659.25, "pan":  0.75, "instrument": "Violín I / Soprano lírica"},
]

def get_band_freq(s_idx, rank_char, polarity):
    b = SUBJECT_BANDS[s_idx]
    if polarity > 0: # Elección (A, B, C)
        if rank_char == 'A':
            return b['fMax']
        elif rank_char == 'B':
            return b['fBase'] * 1.18
        else: # 'C'
            return b['fBase'] * 1.08
    elif polarity < 0: # Rechazo (c, b, a)
        if rank_char == 'c':
            return b['fBase'] * 0.92
        elif rank_char == 'b':
            return b['fBase'] * 0.82
        else: # 'a'
            return b['fMin']
    else: # Neutro '0'
        return b['fBase']

def synth_violin(freq, dur, s_idx=0, vibrato_rate=5.3, vibrato_depth=5.0):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    
    vib = vibrato_depth * np.sin(2 * np.pi * vibrato_rate * t)
    inst_freq = freq + vib
    phase = 2 * np.pi * np.cumsum(inst_freq) / SAMPLE_RATE
    
    wave_sig = (
        1.00 * np.sin(phase) +
        0.55 * np.sin(2 * phase) +
        0.35 * np.sin(3 * phase) +
        0.20 * np.sin(4 * phase) +
        0.12 * np.sin(5 * phase) +
        0.08 * np.sin(6 * phase)
    )
    
    attack_time = min(0.06, dur * 0.2)
    decay_time = min(0.08, dur * 0.25)
    n_att = int(attack_time * SAMPLE_RATE)
    n_dec = int(decay_time * SAMPLE_RATE)
    n_sus = n_samples - n_att - n_dec
    
    env_att = np.sin(np.linspace(0, np.pi/2, n_att)) ** 2
    env_sus = np.linspace(1.0, 0.9, n_sus)
    env_dec = np.sin(np.linspace(np.pi/2, 0, n_dec)) ** 2
    env = np.concatenate([env_att, env_sus, env_dec])
    if len(env) < n_samples:
        env = np.pad(env, (0, n_samples - len(env)), 'constant')
    else:
        env = env[:n_samples]
        
    sig = wave_sig * env
    
    try:
        f_low = max(100.0, min(1800.0, freq * 1.2)) / (SAMPLE_RATE / 2)
        f_high = min(SAMPLE_RATE / 2 - 100, max(f_low * (SAMPLE_RATE/2) + 200, min(3200.0, freq * 6.0))) / (SAMPLE_RATE / 2)
        if f_low < f_high:
            b, a = signal.butter(2, [f_low, f_high], btype='bandpass')
            sig_filtered = signal.lfilter(b, a, sig)
            sig = 0.6 * sig + 0.4 * sig_filtered
    except Exception:
        pass
        
    return sig * 0.22

def synth_trombone(freq, dur, s_idx=0):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    
    gliss_curve = 1.0 - 0.08 * (t / dur) ** 0.8
    inst_freq = freq * gliss_curve
    phase = 2 * np.pi * np.cumsum(inst_freq) / SAMPLE_RATE
    
    wave_sig = (
        0.85 * signal.sawtooth(phase) +
        0.45 * np.sin(phase) +
        0.30 * signal.sawtooth(2 * phase + 0.2)
    )
    
    attack_time = min(0.03, dur * 0.12)
    decay_time = min(0.12, dur * 0.3)
    n_att = int(attack_time * SAMPLE_RATE)
    n_dec = int(decay_time * SAMPLE_RATE)
    n_sus = n_samples - n_att - n_dec
    
    env_att = np.linspace(0.1, 1.0, n_att)
    env_sus = np.linspace(1.0, 0.75, n_sus)
    env_dec = np.linspace(0.75, 0.001, n_dec) ** 1.5
    env = np.concatenate([env_att, env_sus, env_dec])
    if len(env) < n_samples:
        env = np.pad(env, (0, n_samples - len(env)), 'constant')
    else:
        env = env[:n_samples]
        
    sig = wave_sig * env
    
    try:
        cutoff = min(freq * 3.2, 950.0) / (SAMPLE_RATE / 2)
        b, a = signal.butter(2, cutoff, btype='lowpass')
        sig = signal.lfilter(b, a, sig)
    except Exception:
        pass
        
    return sig * 0.25

def synth_flute(freq, dur):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    inst_freq = freq * (1.0 + 0.03 * (t / dur))
    phase = 2 * np.pi * np.cumsum(inst_freq) / SAMPLE_RATE
    breath = np.random.normal(0, 0.02, n_samples)
    wave_sig = np.sin(phase) + 0.25 * np.sin(2 * phase) + 0.1 * np.sin(3 * phase) + breath
    
    att = int(min(0.08, dur * 0.25) * SAMPLE_RATE)
    dec = int(min(0.12, dur * 0.35) * SAMPLE_RATE)
    sus = n_samples - att - dec
    env = np.concatenate([np.linspace(0, 1.0, att)**2, np.ones(sus), np.linspace(1.0, 0, dec)**2])
    return wave_sig[:n_samples] * env[:n_samples] * 0.18

def synth_pluck(freq, dur):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    phase = 2 * np.pi * freq * t
    decay = np.exp(-t * 9.0)
    wave_sig = (np.sin(phase) + 0.4 * np.sin(2 * phase) + 0.2 * np.sin(3 * phase)) * decay
    return wave_sig * 0.28

def synth_harp(freq, dur):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    decay = np.exp(-t * 4.5)
    wave_sig = (
        np.sin(2 * np.pi * freq * t) +
        0.5 * np.sin(2 * np.pi * freq * 2.005 * t) +
        0.3 * np.sin(2 * np.pi * freq * 3.01 * t) +
        0.15 * np.sin(2 * np.pi * freq * 4.02 * t)
    ) * decay
    return wave_sig * 0.20

def synth_zen_bowl(freq, dur):
    n_samples = int(SAMPLE_RATE * dur)
    t = np.linspace(0, dur, n_samples, False)
    decay = np.exp(-t * 2.8)
    wave_sig = (
        np.sin(2 * np.pi * freq * t) +
        0.18 * np.sin(2 * np.pi * freq * 2.0 * t) +
        0.05 * np.sin(2 * np.pi * freq * 3.0 * t)
    ) * decay
    return wave_sig * 0.22

def apply_reverb_and_pan(stereo_buf, impulse_decay=1.6):
    n_rev = int(SAMPLE_RATE * impulse_decay)
    t_rev = np.linspace(0, impulse_decay, n_rev, False)
    h_l = np.random.normal(0, 1, n_rev) * np.exp(-t_rev * 4.0)
    h_r = np.random.normal(0, 1, n_rev) * np.exp(-t_rev * 4.0)
    b_ir, a_ir = signal.butter(1, 0.15)
    h_l = signal.lfilter(b_ir, a_ir, h_l)
    h_r = signal.lfilter(b_ir, a_ir, h_r)
    h_l /= (np.max(np.abs(h_l)) + 1e-6)
    h_r /= (np.max(np.abs(h_r)) + 1e-6)
    
    rev_l = signal.fftconvolve(stereo_buf[:, 0], h_l)[:len(stereo_buf)] * 0.20
    rev_r = signal.fftconvolve(stereo_buf[:, 1], h_r)[:len(stereo_buf)] * 0.20
    
    out = np.zeros_like(stereo_buf)
    out[:, 0] = stereo_buf[:, 0] * 0.85 + rev_l
    out[:, 1] = stereo_buf[:, 1] * 0.85 + rev_r
    return out

def add_note_to_buffer(buffer, mono_sig, start_time, pan=0.0):
    start_idx = int(start_time * SAMPLE_RATE)
    n_samples = len(mono_sig)
    end_idx = min(start_idx + n_samples, len(buffer))
    actual_len = end_idx - start_idx
    if actual_len <= 0:
        return
    angle = (pan + 1.0) * (np.pi / 4.0)
    gain_l = np.cos(angle)
    gain_r = np.sin(angle)
    buffer[start_idx:end_idx, 0] += mono_sig[:actual_len] * gain_l
    buffer[start_idx:end_idx, 1] += mono_sig[:actual_len] * gain_r

def generate_octet_master_recording():
    total_duration = 56.0 # 56 segundos de sinfonía
    total_samples = int(total_duration * SAMPLE_RATE)
    buffer = np.zeros((total_samples, 2), dtype=np.float32)
    
    print("🎼 Movimiento 1: Afinación y Entrada Polifónica del Octeto N=8 (0s - 8s)...")
    entry_times = [0.0, 0.65, 1.30, 1.95, 2.60, 3.25, 3.90, 4.55]
    for s_idx, t_start in enumerate(entry_times):
        b = SUBJECT_BANDS[s_idx]
        dur = 4.8 - (s_idx * 0.2)
        note = synth_zen_bowl(b['fBase'], dur)
        add_note_to_buffer(buffer, note, t_start, b['pan'])
        v_note = synth_violin(b['fBase'], dur * 0.85, s_idx=s_idx, vibrato_depth=2.8) * 0.4
        add_note_to_buffer(buffer, v_note, t_start + 0.12, b['pan'])
        
    print("🎻 Movimiento 2: Diálogos Diádicos y Reciprocidades Fácticas (8s - 22s)...")
    t = 7.2
    # Diálogo 1: 1A y 8A (<Ee> elección mutua)
    add_note_to_buffer(buffer, synth_flute(SUBJECT_BANDS[0]['fBase'], 0.42), t, SUBJECT_BANDS[0]['pan'])
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[0]['fMax'], 0.28, s_idx=0), t + 0.42, SUBJECT_BANDS[0]['pan'])
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[7]['fMax'], 0.28, s_idx=7), t + 0.75, SUBJECT_BANDS[7]['pan'])
    add_note_to_buffer(buffer, synth_harp(SUBJECT_BANDS[7]['fBase'], 0.50), t + 1.05, SUBJECT_BANDS[7]['pan'])
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[0]['fMax'], 1.2, s_idx=0) * 0.65, t + 1.45, SUBJECT_BANDS[0]['pan'])
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[7]['fMax'], 1.2, s_idx=7) * 0.65, t + 1.45, SUBJECT_BANDS[7]['pan'])
    
    # Diálogo 2: 2A y 5A ([Rr] fricción pesada de trombones)
    t = 10.6
    add_note_to_buffer(buffer, synth_flute(SUBJECT_BANDS[1]['fBase'], 0.40), t, SUBJECT_BANDS[1]['pan'])
    add_note_to_buffer(buffer, synth_trombone(SUBJECT_BANDS[1]['fMin'], 0.35, s_idx=1), t + 0.40, SUBJECT_BANDS[1]['pan'])
    add_note_to_buffer(buffer, synth_trombone(SUBJECT_BANDS[4]['fMin'], 0.38, s_idx=4), t + 0.78, SUBJECT_BANDS[4]['pan'])
    add_note_to_buffer(buffer, synth_trombone(SUBJECT_BANDS[1]['fMin'], 1.4, s_idx=1) * 0.75, t + 1.20, SUBJECT_BANDS[1]['pan'])
    add_note_to_buffer(buffer, synth_trombone(SUBJECT_BANDS[4]['fMin'], 1.4, s_idx=4) * 0.75, t + 1.20, SUBJECT_BANDS[4]['pan'])
    
    # Diálogo 3: 3A y 6A (<Er] contrapunto violín/trombón)
    t = 14.0
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[2]['fMax'], 0.35, s_idx=2), t, SUBJECT_BANDS[2]['pan'])
    add_note_to_buffer(buffer, synth_trombone(SUBJECT_BANDS[5]['fMin'], 0.38, s_idx=5), t + 0.38, SUBJECT_BANDS[5]['pan'])
    add_note_to_buffer(buffer, synth_harp(SUBJECT_BANDS[5]['fBase'], 0.45), t + 0.78, SUBJECT_BANDS[5]['pan'])
    
    # Diálogo 4: 4A y 7A (<Ee> dúo armónico)
    t = 17.2
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[3]['fMax'], 0.48, s_idx=3), t, SUBJECT_BANDS[3]['pan'])
    add_note_to_buffer(buffer, synth_violin(SUBJECT_BANDS[6]['fMax'], 0.48, s_idx=6), t + 0.28, SUBJECT_BANDS[6]['pan'])
    add_note_to_buffer(buffer, synth_harp(SUBJECT_BANDS[6]['fBase'] * 1.5, 0.70), t + 0.70, SUBJECT_BANDS[6]['pan'])
    
    print("🎹 Movimiento 3: Secuencia Serial Integral del Octeto N=8 (21s - 47s)...")
    t_curr = 21.0
    ranks_sequence = ['A', 'B', 'C', '0', 'c', 'b', 'a']
    
    for s_idx in range(8):
        b = SUBJECT_BANDS[s_idx]
        pan = b['pan']
        
        dur_a1 = 0.42 + (s_idx % 3) * 0.02
        add_note_to_buffer(buffer, synth_flute(b['fBase'], dur_a1), t_curr, pan)
        t_curr += dur_a1 * 0.85
        
        for r_char in ranks_sequence:
            pol = 1 if r_char in ['A', 'B', 'C'] else (-1 if r_char in ['c', 'b', 'a'] else 0)
            f_note = get_band_freq(s_idx, r_char, pol)
            dur_a2 = 0.19 + ((hash(r_char) % 5) - 2) * 0.012
            
            if pol > 0:
                note_sig = synth_violin(f_note, dur_a2, s_idx=s_idx)
                add_note_to_buffer(buffer, note_sig, t_curr, pan)
            elif pol < 0:
                note_sig = synth_trombone(f_note, dur_a2 * 1.25, s_idx=s_idx)
                add_note_to_buffer(buffer, note_sig, t_curr, pan)
            else:
                note_sig = synth_zen_bowl(f_note, dur_a2 * 1.4)
                add_note_to_buffer(buffer, note_sig, t_curr, pan)
                
            t_curr += dur_a2 * 0.80
            
        add_note_to_buffer(buffer, synth_harp(b['fBase'] * 1.25, 0.45), t_curr, pan)
        t_curr += 0.32
        
    print("🕊️ Movimiento 4: Coda y Resonancia Armónica del Octeto N=8 (47s - 56s)...")
    t_coda = 47.0
    for s_idx in range(8):
        b = SUBJECT_BANDS[s_idx]
        note = synth_zen_bowl(b['fBase'], 8.5) * 0.42
        add_note_to_buffer(buffer, note, t_coda + s_idx * 0.22, b['pan'])
        v_pad = synth_violin(b['fBase'], 7.5, s_idx=s_idx, vibrato_depth=1.8) * 0.22
        add_note_to_buffer(buffer, v_pad, t_coda + s_idx * 0.22, b['pan'])
        
    print("🌌 Aplicando reverberación acústica estéreo...")
    stereo_out = apply_reverb_and_pan(buffer)
    
    peak = np.max(np.abs(stereo_out))
    if peak > 0:
        norm_factor = (10 ** (-1.0 / 20.0)) / peak
        stereo_out = stereo_out * norm_factor
        
    int16_out = np.int16(np.clip(stereo_out * 32767.0, -32768, 32767))
    
    wav_path = "05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.wav"
    mp3_path = "05_Web_Promocional/assets/audio/NEXORD_GRABACION_OCTETO_N8_MASTER.mp3"
    
    print(f"💾 Guardando archivo WAV de alta fidelidad: {wav_path}...")
    with wave.open(wav_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(int16_out.tobytes())
        
    print(f"🔄 Convirtiendo a MP3 broadcast mediante ffmpeg: {mp3_path}...")
    try:
        subprocess.run([
            '/usr/local/bin/ffmpeg', '-y', '-i', wav_path,
            '-b:a', '256k', mp3_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ MP3 generado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al convertir a MP3: {e}")
        
    print("🎉 ¡Grabación Maestra del Octeto N=8 generada con total fidelidad acústica!")

if __name__ == "__main__":
    generate_octet_master_recording()
