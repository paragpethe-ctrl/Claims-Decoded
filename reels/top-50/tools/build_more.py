import json, sys
sys.path.insert(0, '.')
src = open('gen.py').read()
exec(src[src.index("FRAME = ("):src.index("def hook_line")])
from more_ins import P1, P2, SRC
AU = {e['id']: e for e in json.load(open('audit/more.json'))}
D = '/home/user/Claims-Decoded/reels/insurance-awareness'

def shots(v):
    setting, fire, obj, fix = v
    return [[f'{setting}, fast push-in', fire, 'the same scene in slow motion, smoke drifting across the frame'],
            [f'{obj}, slow push-in', f'{setting}, quiet the next morning', f'a tight close-up of {obj}'],
            [fix, f'{setting}, safe and orderly in warm light']]

def build(P, tag, start):
    out = []
    for n, e in enumerate(P, 1):
        au = AU[f'{tag}{n:02d}']
        ep = dict(t=e['t'], n=[' '.join(p) for p in e['x']], w=e['w'], v=shots(e['v']))
        num = start + n
        out += [f'## {num:02d}. {e["t"]}', '',
                f'**Hook:** "{" ".join(e["x"][0][:2])}" (score {au["hook"]}) · /ig-reel beat sheet clean with a loop · /ig-human PASS {au["human"]}  ',
                f'**Timing:** {au["secs"][0]}s + {au["secs"][1]}s + {au["secs"][2]}s spoken, plus a 2s end card', '',
                '**Script**', ''] + [f'{k+1}. ' + ' / '.join(p) for k, p in enumerate(e['x'])] + ['',
                f'**Facts to check:** {e["f"]}' + ('  \n**Sources:** ' + ', '.join(f'[{i+1}]({SRC[s]})' for i, s in enumerate(e['s'])) if e['s'] else ''), '']
        for p in range(3):
            out += [f'### Part {p+1}', '', '```', prompt(ep, p), '```', '']
        out += ['---', '']
    return '\n'.join(out)

note = ('Cinematic format (narration, impact text, titles in every prompt), same as the refuge area reel. Every script passed '
        '/ig-reel (hook 94 to 100, beat sheet clean with a loop) and /ig-human (PASS 72 to 81).\n\n'
        'If Gemini refuses a part (likelier where the narration names a court decision), paste that part again without the '
        'NARRATION block and add the voiceover in your editor.\n\n')
open(f'{D}/pillar-1-more-25.md', 'w').write('# Pillar 1: Why buy fire insurance, reels 17 to 41\n\n' + note + build(P1, 'A', 16))
open(f'{D}/pillar-2-more-25.md', 'w').write('# Pillar 2: Lessons from rejected claims, reels 42 to 66\n\n' + note + build(P2, 'B', 41))
print('ok')
