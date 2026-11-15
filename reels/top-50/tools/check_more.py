import json, subprocess, sys, re
sys.path.insert(0, '.')
from more_ins import P1, P2
SK = '/home/user/Claims-Decoded/.claude/skills/'
LIM = [9.6, 9.6, 7.8]
def run(tool, args, text):
    return json.loads(subprocess.run([sys.executable, '-I', SK + tool, *args], input=text, capture_output=True, text=True).stdout)
def wc(s): return len(re.findall(r"[A-Za-z0-9$%'’-]+", s.replace(',', '')))
out, clean = [], 0
for tag, P in (('A', P1), ('B', P2)):
    for i, e in enumerate(P, 1):
        lines = [s for p in e['x'] for s in p]
        b = run('ig-reel/beats.py', ['-', '--json'], '\n'.join(lines))
        iss = [n.split('.')[0] for n in b['notes'] if not n.startswith('Loops:') and 'target' not in n]
        if not any(n.startswith('Loops:') for n in b['notes']): iss.append('NO LOOP')
        h = run('ig-reel/hookscore.py', ['--json', '--hook', ' '.join(lines[:2])], '')
        d = run('ig-human/detect.py', ['-', '--json'], ' '.join(lines))
        secs = [sum(wc(s) for s in p) * 60 / 165 for p in e['x']]
        iss += [f'P{k+1} {t:.1f}s' for k, (t, l) in enumerate(zip(secs, LIM)) if t > l]
        if h['score'] < 88: iss.append(f'hook {h["score"]:.0f}')
        if d['verdict'] != 'PASS':
            wk = sorted(d['checks'].items(), key=lambda kv: kv[1]['score'])[:2]
            iss.append(f'human {d["human_score"]:.0f} ' + ', '.join(f'{k[:5]} {v["score"]:.0f}' for k, v in wk))
        out.append(dict(id=f'{tag}{i:02d}', hook=round(h['score']), human=round(d['human_score']), secs=[round(s, 1) for s in secs], issues=iss))
        if iss: print(f'{tag}{i:02d}', e['t'][:28], '|', ' || '.join(iss))
        else: clean += 1
json.dump(out, open('audit/more.json', 'w'), indent=1)
print(clean, 'of', len(out), 'clean')
