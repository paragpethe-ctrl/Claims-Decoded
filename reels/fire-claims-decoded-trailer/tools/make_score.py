"""Trailer score for the Fire Claims Decoded series video, synthesised to the cue sheet.
120 BPM, D minor, 31.5 s. Writes a stereo 48 kHz WAV."""
import sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
import soundfile as sf

SR = 48000
DUR = 31.5
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
BEAT = 0.5

def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)
def tt(d): return np.arange(int(d * SR)) / SR
def add(sig, t0, gain=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N: return
    sig = sig[: N - i]
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    L[i:i + len(sig)] += sig * gain * l * 1.414
    R[i:i + len(sig)] += sig * gain * r * 1.414
def note(n): return 440.0 * 2 ** ((n - 69) / 12)   # MIDI note to Hz
def saw(f, t): return 2 * ((f * t) % 1.0) - 1

# ---------- instruments ----------
def phone(x, drive=4.0, amt=0.6):
    # add upper harmonics of a low sound so small speakers still carry it
    return x + amt * hp(np.tanh(drive * x), 180)

def kick(d=0.45):
    t = tt(d); f = 45 + 95 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return phone(np.sin(ph) * np.exp(-t * 7)) + 0.4 * hp(rng.standard_normal(len(t)), 2000) * np.exp(-t * 300)

def taiko(pitch=78, d=0.6):
    t = tt(d); f = pitch * (1 + 0.5 * np.exp(-t * 30))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6)
    skin = bp(rng.standard_normal(len(t)), 120, 900) * np.exp(-t * 18) * 0.8
    return phone(body, 3.0, 0.5) + skin * 1.3

def snare(d=0.25):
    t = tt(d)
    return bp(rng.standard_normal(len(t)), 900, 7000) * np.exp(-t * 22) + 0.4 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30)

def hat(d=0.06):
    t = tt(d); return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t * 70)

def tick(d=0.03):
    t = tt(d); return np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 220)

def boom(d=3.0):
    t = tt(d); f = 30 + 34 * np.exp(-t * 3)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.4)
    crash = lp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 3.2) * 0.55
    return phone(sub * 0.7, 5.0, 0.5) + crash * 1.4 + np.pad(kick(0.45), (0, len(t) - int(0.45 * SR)))

def braam(root=38, d=2.6, bright=1.0):
    """Low brass-like blast: stacked detuned saws, a bright attack that darkens."""
    t = tt(d); sig = np.zeros(len(t))
    for n, g in ((root, 0.7), (root + 12, 0.9), (root + 19, 0.7), (root + 24, 0.6), (root + 31, 0.35)):
        for det in (-0.12, 0.0, 0.11):
            sig += g * saw(note(n + det), t)
    dark = lp(sig, 700, 4); brightv = lp(sig, 3600 * bright, 4)
    mix = np.exp(-t * 2.2)
    env = np.minimum(t / 0.03, 1) * np.exp(-t * 0.9)
    return (dark * (1 - mix) + brightv * mix) * env * 0.12

def bass(n, d=0.24):
    t = tt(d); f = note(n)
    s = saw(f, t) + 0.5 * saw(f * 1.005, t)
    return lp(s, 520, 4) * np.exp(-t * 10) * np.minimum(t / 0.004, 1) * 0.55

def pluck(n, d=0.16):
    t = tt(d); f = note(n)
    s = saw(f, t) + 0.6 * saw(f * 2.003, t)
    return lp(s, 3200, 2) * np.exp(-t * 18) * np.minimum(t / 0.002, 1) * 0.35

def pad(notes, d, cutoff=900, att=0.6, rel=1.2):
    t = tt(d); s = np.zeros(len(t))
    for n in notes:
        for det in (-0.08, 0.07):
            s += saw(note(n + det), t)
    s = lp(s, cutoff * 2.2, 4)
    env = np.minimum(t / att, 1) * np.minimum((d - t) / rel, 1).clip(0, 1)
    return s * env * 0.05

def riser(d=2.0):
    t = tt(d); k = t / d
    noise = rng.standard_normal(len(t)); out = np.zeros(len(t)); step = int(0.05 * SR)
    for i in range(0, len(t), step):
        f0 = 300 + 6000 * k[i] ** 2
        seg = bp(noise[max(0, i - 2048):i + step], f0, min(f0 * 1.8, 20000))[-(min(step, len(t) - i)):]
        out[i:i + len(seg)] = seg
    tone = np.sin(2 * np.pi * np.cumsum(90 + 600 * k ** 2) / SR)
    return (out * 0.8 + 0.25 * tone) * k ** 2

def whoosh(d=0.4):
    t = tt(d); k = t / d; out = np.zeros(len(t)); noise = rng.standard_normal(len(t) + 4096); step = int(0.02 * SR)
    for i in range(0, len(t), step):
        f0 = 400 + 3500 * np.sin(np.pi * k[i])
        seg = bp(noise[i:i + step + 4096], f0, f0 * 2.2)[-step:]
        out[i:i + len(seg)] = seg[: len(out) - i]
    return out * np.sin(np.pi * k) ** 2

def crack(d=0.3):
    t = tt(d)
    return hp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 40) + 0.5 * np.sin(2 * np.pi * (1800 - 1500 * t) * t) * np.exp(-t * 25)

def stamp(d=0.5):
    return np.pad(snare(0.25), (0, int(0.25 * SR))) * 1.3 + taiko(60, 0.5) * 0.9

# ---------- the score ----------
D2, A1, Bb1, F2, C2 = 38, 33, 34, 41, 36

# HOOK 0-3: boom on STOP, ticking clock, hits on 3 and on BUILDING / RIGHT NOW
add(boom(3.0), 0.0, 0.9); add(braam(D2, 2.4), 0.0, 1.0)
for i in range(12): add(tick(), i * 0.25, 0.25, 0.3 if i % 2 else -0.3)
add(taiko(70), 0.75, 1.0); add(boom(1.5), 0.75, 0.55)
add(taiko(80), 2.0, 0.9); add(taiko(66), 2.45, 1.0)
for i, tr in enumerate(np.arange(2.5, 3.0, 0.0625)): add(snare(0.12), tr, 0.18 + 0.06 * i)

# CAUSES 3-9: driving taiko groove and bass ostinato; impact on each cause, crack on each ignition, whoosh on each whip
def groove(t0, bars, roots, hats=True, intensity=1.0):
    for b in range(bars):
        tb = t0 + b * 2.0; root = roots[b % len(roots)]
        for k in range(4):
            add(kick(), tb + k * BEAT, 0.8 * intensity)
        add(taiko(72), tb + 1 * BEAT + 0.25, 0.55 * intensity, -0.4)
        add(taiko(60), tb + 3 * BEAT + 0.25, 0.55 * intensity, 0.4)
        add(snare(), tb + 1 * BEAT, 0.8 * intensity); add(snare(), tb + 3 * BEAT, 0.8 * intensity)
        if hats:
            for k in range(8): add(hat(), tb + k * BEAT / 2, 0.4 * intensity, 0.5 if k % 2 else -0.5)
        for k in range(8):
            add(bass(root + (12 if k in (3, 7) else 0)), tb + k * BEAT / 2, 0.9 * intensity)
        # sixteenth-note arpeggio an octave and a half above: the energy a phone speaker plays
        arp = [root + 24, root + 27, root + 31, root + 36]
        for k in range(16):
            add(pluck(arp[k % 4] + (12 if k % 8 == 7 else 0)), tb + k * BEAT / 4, 0.32 * intensity, 0.35 if k % 2 else -0.35)
groove(3.0, 3, [D2, D2, D2])
add(pad([50, 53, 57], 6.0, 700), 3.0, 1.0)
for i, tc in enumerate((3.0, 5.0, 7.0)):
    add(boom(1.6), tc, 0.6); add(braam(D2 + (0, 3, 5)[i], 1.4), tc, 0.6)
    add(crack(), tc + 1.0, 0.6, 0.3)
    add(whoosh(0.4), tc + 1.66, 0.7, -0.2 if i % 2 else 0.2)

# TURN 9-13: drums drop out, heartbeat and ticks; riser into the engulf at 11; stamp at 12
for i in range(8): add(tick(), 9.0 + i * 0.25, 0.3)
for hb in (9.0, 9.35, 10.0, 10.35): add(kick(0.4), hb, 0.7)
add(pad([38, 50, 53], 2.2, 400, 0.3, 0.6), 9.0, 1.2)
add(riser(1.6), 9.4, 0.45)
for i, tr in enumerate(np.arange(10.5, 11.0, 0.0625)): add(snare(0.12), tr, 0.2 + 0.07 * i)
add(boom(3.0), 11.0, 1.0); add(braam(D2, 2.2, 1.2), 11.0, 1.2)
add(stamp(), 12.0, 1.0); add(boom(1.0), 12.0, 0.4)
add(riser(0.9), 12.1, 0.35)

# REVEAL 13-19: the biggest hit, then the full groove over Dm Bb F C
add(boom(3.0), 13.0, 1.0); add(braam(D2, 2.6, 1.3), 13.0, 1.3)
groove(13.0, 3, [D2, Bb1 + 12, F2], intensity=1.05)
for i, (tc, ch) in enumerate(((13.0, [50, 53, 57]), (15.0, [46, 50, 53]), (17.0, [45, 48, 53]))):
    add(pad(ch, 2.1, 1100), tc, 1.1)
    if i: add(braam(ch[0] - 12, 1.2), tc, 0.55); add(taiko(64), tc, 0.8)

# PROMISE 19-24.5: lighter groove with a tick on each occupancy word; hit on HOW IT STARTS; everything cuts on HOW TO STOP IT
groove(19.0, 1, [C2 + 12], hats=True, intensity=0.8)
for i in range(5): add(tick(), 19.0 + i * 0.4, 0.45, 0.4 if i % 2 else -0.4)
add(pad([48, 52, 55], 2.0, 900), 19.0, 1.0)
add(boom(1.0), 21.0, 0.8); add(braam(D2, 1.0), 21.0, 0.9)
for k in range(2): add(kick(), 21.0 + k * BEAT, 0.8); add(bass(D2), 21.0 + k * BEAT, 0.9)
add(snare(), 21.5, 0.5)
add(boom(4.0), 22.0, 0.75)                      # the last breath of the fire, then quiet
add(pad([50, 54, 57, 62], 5.4, 1400, 1.4, 1.6), 22.6, 1.4)   # D major: relief
for k in range(10): add(tick(), 22.6 + k * 0.5, 0.12)

# CLAIM 24.5-27.5: soft pulse under the line, a riser into the end card
for k in range(6): add(kick(0.35), 24.5 + k * BEAT, 0.35)
add(riser(1.4), 26.1, 0.4)

# END 27.5-31.5: the mark lands; chord rings out
add(boom(4.0), 27.5, 1.0); add(braam(D2, 3.4, 1.1), 27.5, 1.1)
add(taiko(70), 27.5, 1.0); add(taiko(60), 28.0, 0.7); add(taiko(55), 28.5, 0.6)
add(pad([50, 53, 57, 62], 4.0, 1200, 0.05, 2.2), 27.5, 1.6)

# ---------- mix ----------
def reverb(x, secs=2.2, wet=0.18, seed=1):
    r = np.random.default_rng(seed); n = int(secs * SR)
    ir = r.standard_normal(n) * np.exp(-np.arange(n) / SR * 6.9 / secs)
    ir = lp(ir, 6000) / np.sqrt(np.sum(ir ** 2))
    return x + wet * fftconvolve(x, ir)[: len(x)]
L = reverb(L, seed=1); R = reverb(R, seed=2)
mix = np.stack([L, R], 1)
mix = hp(mix.T, 35).T                            # nothing under 35 Hz
mix = mix - 0.45 * lp(mix.T, 110).T                # pull the sub back so the mids carry the track
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(mix * 1.6) / np.tanh(1.6)          # glue and soft-limit
fade = np.ones(N); fl = int(1.2 * SR); fade[-fl:] = np.linspace(1, 0, fl) ** 2
mix *= fade[:, None] * 0.8
# loudness for social: push +4.5 dB into a soft ceiling at -1.6 dBFS
ceil = 10 ** (-3.0 / 20)
mix = ceil * np.tanh(mix * 10 ** (4.2 / 20) / ceil)
sf.write(sys.argv[1], mix.astype(np.float32), SR, subtype='PCM_24')
print("wrote", sys.argv[1])
