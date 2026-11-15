import json, subprocess, sys
sys.path.insert(0, '.')
from scripts_v2 import X
from captions_data import C
from episodes import E
SK = '/home/user/Claims-Decoded/.claude/skills/'
topics = [e['t'] for e in E] + ['The Refuge Area That Became a Store Room']

def build(i):
    ask, kws, kwline, tags = C[i]
    p1, p2, p3 = X[i]
    import re
    key = lambda t: set(re.findall(r"\d+(?:[.,]\d+)*|[A-Z][a-z]{2,}", t))
    k1 = key(p1[1])
    lead = p1[2:] if k1 and k1 <= key(ask) else p1[1:]
    paras = [ask, ' '.join(lead), ' '.join(p2), kwline, '⚠️ Here\'s what works. ' + ' '.join(p3[:-1]),
             'Fire Claims Decoded. 1 fire cause, every reel.', ' '.join(tags)]
    return '\n\n'.join(paras), kws

out, results = [], []
for i in range(51):
    cap, kws = build(i)
    lint = json.loads(subprocess.run([sys.executable, '-I', SK + 'ig-caption/caption.py', '-', '--json', '--keywords', ','.join(kws)],
                                     input=cap, capture_output=True, text=True).stdout)
    body = cap.rsplit('\n\n', 1)[0]
    det = json.loads(subprocess.run([sys.executable, '-I', SK + 'ig-human/detect.py', '-', '--json'],
                                    input=body, capture_output=True, text=True).stdout)
    bad = [c for c in lint['checks'] if c['status'] != 'PASS']
    results.append((i + 1, topics[i], cap, kws, lint, det, bad))
    if bad or det['verdict'] != 'PASS':
        print(f'EP{i+1:02d}', [f"{c['check']}: {c['detail'][:70]}" for c in bad], det['verdict'], round(det['human_score']),
              sorted(((k, round(v['score'])) for k, v in det['checks'].items()), key=lambda kv: kv[1])[:2])
json.dump([dict(ep=r[0], topic=r[1], caption=r[2], keywords=r[3], lint=r[4]['checks'], human=r[5]['human_score'], verdict=r[5]['verdict']) for r in results],
          open('audit/captions.json', 'w'), indent=1, ensure_ascii=False)
print(sum(1 for r in results if not r[6] and r[5]['verdict'] == 'PASS'), 'of 51 clean')
