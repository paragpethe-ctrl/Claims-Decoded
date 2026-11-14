import json, subprocess, sys
sys.path.insert(0, '.')
from scripts_v2 import X

SK = '/home/user/Claims-Decoded/.claude/skills/'
WPM = 165
LIMITS = [9.6, 9.6, 7.8]


def run(tool, args, text):
    r = subprocess.run([sys.executable, '-I', SK + tool, *args], input=text, capture_output=True, text=True)
    return json.loads(r.stdout)


def wc(s):
    import re
    return len(re.findall(r"[A-Za-z0-9$%'’-]+", s.replace(',', '')))


report, bad = [], 0
for i, parts in enumerate(X, 1):
    lines = [s for p in parts for s in p]
    b = run('ig-reel/beats.py', ['-', '--json'], '\n'.join(lines))
    issues = [n for n in b['notes'] if not n.startswith('Loops:') and 'target' not in n]
    loop = any(n.startswith('Loops:') for n in b['notes'])
    if not loop:
        issues.append('NO LOOP')
    hook = ' '.join(lines[:2])
    h = run('ig-reel/hookscore.py', ['--json', '--hook', hook], '')
    d = run('ig-human/detect.py', ['-', '--json'], ' '.join(lines))
    secs = [sum(wc(s) for s in p) * 60 / WPM for p in parts]
    for k, (t, lim) in enumerate(zip(secs, LIMITS)):
        if t > lim:
            issues.append(f'part {k+1} {t:.1f}s')
    if h['score'] < 88:
        issues.append(f'hook {h["score"]:.0f}')
    if d['verdict'] != 'PASS':
        weak = sorted(d['checks'].items(), key=lambda kv: kv[1]['score'])[:2]
        issues.append(f'human {d["verdict"]} {d["human_score"]:.0f}: ' + ', '.join(f'{k} {v["score"]:.0f} ({v["detail"]})' for k, v in weak))
    report.append(dict(ep=i, hook=hook, hook_score=round(h['score']), human=round(d['human_score']), verdict=d['verdict'], secs=[round(s, 1) for s in secs], issues=issues))
    if issues:
        bad += 1
        print(f'EP{i:02d} hook {h["score"]:.0f} | ' + ' || '.join(issues))
print(f'\n{51 - bad} of 51 clean')
json.dump(report, open('audit/v2.json', 'w'), indent=1)
