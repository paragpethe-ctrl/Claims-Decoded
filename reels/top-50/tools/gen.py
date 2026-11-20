import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from episodes import E, S
from scripts_v2 import X
AUDIT = {e['ep']: e for e in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audit', 'v2.json')))}
for i, (ep, parts) in enumerate(zip(E, X), 1):
    ep['n'] = [' '.join(p) for p in parts]
    ep['h'] = ' '.join(parts[0][:2])
    ep['beats'] = parts

OUT = sys.argv[1]
HOOKSCORE = sys.argv[2]
WPM = 165

FRAME = ('TITLES (on screen for the full clip, no border or frame around the video): the footage fills the whole 9:16 '
         'screen. Near the top, below the top 12 percent of the frame so the Instagram interface never covers it: the title '
         '"FIRE CLAIMS DECODED" in bold, condensed sans-serif capitals, warm amber-gold (#FFB300) with a soft dark drop shadow. '
         'Directly below it, the subtitle "{topic}" in clean white (#FFFFFF) sentence case, on a slim semi-transparent black '
         'strip (60 percent opacity), with a thin red-orange (#FF4D00) accent line under the strip. Both stay perfectly still '
         'and identical for the whole clip. Spell all text exactly as written.')

STYLE = 'VISUAL STYLE: polished 2D animated explainer with thick clean outlines, cel shading, rich saturated colour, bold flat infographic overlays and expressive faces. Warm daylight at first, turning to a dark orange-lit night in the hazard demonstration. The expert is lip-synced, speaks to the viewer, and points at things in the scene. A cut or camera move every 2 to 3 seconds; no static shots.'

CAPTIONS = ('CAPTIONS: burned-in captions of the narration, synchronised word by word, bold white sans-serif with the '
            'word being spoken highlighted in yellow, in the lower middle of the screen, above the bottom 25 percent where the Instagram caption sits.')

VOICE = 'NARRATION (spoken by THE EXPERT, lip-synced whenever he is on screen, speaking to the viewer; a confident, energetic male voice with a clear Indian English accent). The narration starts on the very first frame with no silence or lead-in, and runs to the end of the clip. Exact words:'

END = ('END CARD (last 2 seconds, from 8 to 10 seconds): the footage cuts to black. Centred, appearing '
       'one line at a time: "FIRE CLAIMS DECODED" in gold, "@fireclaimsdecoded" in white, a bold red "FOLLOW" button, and '
       '"1 FIRE CAUSE EVERY REEL" in yellow. A final deep bass hit. Hold.')

QUESTION_SHOT = ('a single small flame flickering in total darkness, slow push-in, embers drifting upward, '
                 'while the narrator asks the closing question')


def secs(text):
    return len(text.split()) * 60 / WPM


def impact(words, times):
    parts = [f'"{w}" at {t}' for w, t in zip(words, times)]
    return ('IMPACT TEXT: bold red-and-yellow impact typography, centred on screen, punching in with a whoosh: '
            + ', then '.join(parts) + '. Each word holds for about 2 seconds. Spell it exactly as written.')


def prompt(ep, part):
    topic = ep['t']
    narr = ep['n'][part]
    shots = ep['v'][part]
    head = (f'Create a polished 2D animated explainer vertical video clip, part {part + 1} of 3 of an Instagram Reel. '
            f'9:16, 1080 x 1920, 10 seconds.')
    lines = [head, '', FRAME.format(topic=topic), '', STYLE,
             'RECURRING CHARACTER (keep identical in every clip):\nTHE EXPERT (the creator himself): use the attached reference photo as the identity reference. Indian man in his 40s, warm light-brown skin, thick black hair swept back and to the side, broad friendly smile, CLEAN-SHAVEN (no beard, no moustache, no stubble; never add facial hair). Rendered in the illustrated style but clearly recognisable as the man in the photo, with the same face shape, hairline and smile. Wears a white hard hat and a maroon safety jacket with a small shield badge over his own white vertical-striped mandarin-collar shirt (collar visible), a brown leather wristwatch and a thin gold bracelet on the left wrist; slim clipboard. Face and outfit identical in every shot and in every clip.\nIn this clip THE EXPERT appears in at least one shot, standing in the scene, speaking to the viewer and pointing at what the narration describes; in the other shots his lip-synced voice continues over the scene.']
    if part < 2:
        lines += ['', f'Shot 1 (0 to 3 seconds): {shots[0]}.',
                  f'Shot 2 (3 to 6 seconds): {shots[1]}.',
                  f'Shot 3 (6 to 10 seconds): {shots[2]}.']
        times = ['0 seconds', '5 seconds']
    else:
        lines += ['', f'Shot 1 (0 to 2 seconds): {shots[0]}.',
                  f'Shot 2 (2 to 4 seconds): {shots[1]}.',
                  f'Shot 3 (4 to 8 seconds): {QUESTION_SHOT}.',
                  '', END]
        times = ['0 seconds', '2 seconds']
    lines += ['', impact(ep['w'][part], times), '', CAPTIONS, '', f'{VOICE}\n"{narr}"', '']
    if part == 0:
        lines.append('AUDIO: fire ambience; a deep cinematic bass hit on the very first word; a whoosh on every cut.')
    elif part == 1:
        lines.append('AUDIO: fire ambience and a low rising drone; a whoosh on every cut; a bass hit on the last line.')
    else:
        lines.append('AUDIO: fire ambience fading under the question; a whoosh on every cut; a deep bass hit on the end card.')
    return '\n'.join(lines)


def hook_line(ep):
    return ep['h']


hooks = [hook_line(ep) for ep in E]
res = subprocess.run([sys.executable, '-I', HOOKSCORE, '--json', '-'], input='\n'.join(hooks),
                     capture_output=True, text=True)
scores = json.loads(res.stdout)
if isinstance(scores, dict):
    scores = [scores]
score_by_hook = {s['hook']: s for s in scores}

os.makedirs(OUT, exist_ok=True)
index_rows, problems = [], []
for start in range(0, len(E), 10):
    chunk = E[start:start + 10]
    fname = f'episodes-{start + 1:02d}-{start + len(chunk):02d}.md'
    out = [f'# Fire Claims Decoded: episodes {start + 1} to {start + len(chunk)}', '']
    for i, ep in enumerate(chunk, start + 1):
        t = [secs(n) for n in ep['n']]
        limits = [9.6, 9.6, 7.8]
        for k in range(3):
            if t[k] > limits[k]:
                problems.append(f'EP{i:02d} part {k + 1}: {t[k]:.1f}s > {limits[k]}s')
        sc = score_by_hook[hooks[i - 1]]
        out += [f'## {i:02d}. {ep["t"]}', '',
                f'**Hook:** "{hooks[i - 1]}" (hook score {sc["score"]:.0f} {sc["verdict"]})  ',
                f'**Spoken length:** {t[0]:.1f}s + {t[1]:.1f}s + {t[2]:.1f}s = {sum(t):.1f}s, plus a 2s end card  ',
                f'**Instagram skill checks:** hook {AUDIT[i]["hook_score"]} (/ig-reel hookscore), beat sheet clean with a loop (/ig-reel beats), humanizer PASS {AUDIT[i]["human"]} (/ig-human)', '',
                '**Full script**', '',
                *[f'{k + 1}. ' + ' / '.join(p) for k, p in enumerate(ep['beats'])], '',
                f'**Facts to check before posting:** {ep["f"]}', '',
                '**Sources:** ' + ', '.join(f'[{j + 1}]({S[k]})' for j, k in enumerate(ep['s'])), '']
        for p in range(3):
            label = ['hook and events', 'why it happens', 'fix, question and end card'][p]
            out += [f'### Part {p + 1}: {label}', '', '```', prompt(ep, p), '```', '']
        out += ['---', '']
        index_rows.append(f'| {i:02d} | [{ep["t"]}]({fname}#{i:02d}-'
                          + re.sub(r'[^a-z0-9 -]', '', ep['t'].lower()).replace(' ', '-')
                          + f') | {hooks[i - 1]} | {sc["score"]:.0f} |')
    with open(os.path.join(OUT, fname), 'w') as fh:
        fh.write('\n'.join(out))

with open(os.path.join(OUT, 'index-rows.md'), 'w') as fh:
    fh.write('\n'.join(index_rows))
print('\n'.join(problems) if problems else 'all parts within time')
print('hook scores:', sorted(round(s['score']) for s in scores))
