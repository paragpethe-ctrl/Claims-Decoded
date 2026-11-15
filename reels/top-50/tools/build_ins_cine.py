import json, re, sys
sys.path.insert(0, '.')
src = open('gen.py').read()
exec(src[src.index("FRAME = ("):src.index("def hook_line")])  # same TITLES, STYLE, CAPTIONS, VOICE, END, question shot
from scripts_ins import T, X
from ins_cine import W, S
AU = {e['ep']: e for e in json.load(open('audit/ins.json'))}
D = '/home/user/Claims-Decoded/reels/insurance-awareness'

def eps(rng):
    out = []
    for i in rng:
        ep = dict(t=T[i], n=[' '.join(p) for p in X[i]], w=W[i], v=S[i])
        au = AU[i + 1]
        out += [f'## {i+1:02d}. {T[i]}', '',
                f'**Hook:** "{" ".join(X[i][0][:2])}" (score {au["hook_score"]}) · /ig-reel beat sheet clean with a loop · /ig-human PASS {au["human"]}  ',
                f'**Timing:** {au["secs"][0]}s + {au["secs"][1]}s + {au["secs"][2]}s spoken, plus a 2s end card', '',
                '**Script**', ''] + [f'{k+1}. ' + ' / '.join(p) for k, p in enumerate(X[i])] + ['']
        for p in range(3):
            out += [f'### Part {p+1}', '', '```', prompt(ep, p), '```', '']
        out += ['---', '']
    return '\n'.join(out)

head = ('Cinematic format, same as the refuge area reel: realistic visuals, narration inside each prompt, red-and-yellow impact '
        'words, title and subtitle. Scripts, facts, sources and captions are unchanged: see the matching pillar file.\n\n'
        'If Gemini refuses a part (most likely in pillar 2, where the narration names court decisions), use the animated, '
        'no-speech prompts for that reel in the pillar file and add the voiceover in your editor.\n\n')
open(f'{D}/pillar-1-cinematic-prompts.md', 'w').write('# Pillar 1: Why buy fire insurance (cinematic prompts)\n\n' + head + eps(range(8)))
open(f'{D}/pillar-2-cinematic-prompts.md', 'w').write('# Pillar 2: Lessons from rejected claims (cinematic prompts)\n\n' + head + eps(range(8, 16)))
print('ok')
