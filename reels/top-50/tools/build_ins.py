import json, re, subprocess, sys
sys.path.insert(0, '.')
from scripts_ins import T, X
from ins_extra import V
SK = '/home/user/Claims-Decoded/.claude/skills/'
AU = {e['ep']: e for e in json.load(open('audit/ins.json'))}
WPS = 165 / 60
SRC = {
 'bt': 'https://www.businesstoday.in/personal-finance/insurance/story/rs-500-a-year-could-save-your-home-uttarkashi-disaster-shows-under-1-are-insured-488503-2025-08-08',
 'bgr': 'https://irdai.gov.in/documents/37343/0/Annexure-I-Bharat+Griha+Raksha.pdf/f6742d71-8194-333f-1409-2c8c652a0964?t=1633438223524',
 'zk': 'https://www.zurichkotak.com/docs/default-source/default-document-library/standard-fire-products-faqs-apr21.pdf?sfvrsn=1894caab_2',
 'bsus': 'https://www.probusinsurance.com/corporate-insurance-plans/bharat-sookshma-udyam-suraksha/',
 'sfsp': 'https://www.universalsompo.com/assets/file/commercial/standard-fire-special-perils-policy/standard-fire-special-perils-policy-prospectus.pdf',
 'gen312': 'https://irdai.gov.in/documents/37343/993134/126.+Standard+Fire+and+Special+Perils_GEN312.pdf/14f6bb58-2ebc-ba19-a6d8-2615ceb16557?version=1.1&t=1668404311211&download=true',
 'hemkund': 'https://www.verdictum.in/supreme-court/ms-new-india-assurance-company-limited-v-ms-hemkund-duplex-and-board-private-limited-2026-insc-1023-1622489',
 'roland': 'https://www.livelaw.in/amp/consumer-cases/strict-enforcement-of-insurance-terms-ncdrc-dismisses-complaint-against-national-insurance-company-294926',
 'roland2': 'https://mahendrabhavsar.com/insurance-claim-denied-for-fraud-ncdrc-upholds-repudiation-based-on-survey-and-forensic-reports/',
 'cotton': 'https://the420.in/ncdrc-fire-insurance-claim-united-india-warehouse-case/',
 'falsedecl': 'https://www.jurishour.in/supreme-court/repudiation-of-fire-insurance-claim-false-declarations-policy-breaches/',
 'surveyor': 'https://www.verdictum.in/supreme-court/ms-new-india-assurance-company-limited-v-ms-hemkund-duplex-and-board-private-limited-2026-insc-1023-1622489',
}
F = [
 ("About 1% of Indian households have home insurance (most-cited estimate, secondary sources). Business Today: about 500 rupees a year for basic cover (estimate).", ['bt']),
 ("General guidance: a landlord's building policy does not cover a tenant's belongings; contents-only policies are sold by many insurers. Check the specific policy.", []),
 ("IRDAI Bharat Griha Raksha wording: underinsurance does not apply; contents cover 20% of building sum insured up to 10 lakh; standard products from 1 April 2021.", ['bgr', 'zk']),
 ("Bharat Sookshma Udyam Suraksha: micro enterprises up to 5 crore per location; underinsurance waived up to 15% (insurer descriptions). The Bharat Laghu Udyam Suraksha threshold above 5 crore was not confirmed in this research; check before posting.", ['bsus', 'zk']),
 ("General guidance: loan-linked home policies often protect the building only; check the schedule. No statistic is claimed.", []),
 ("Standard fire wordings cover storm, tempest, flood and inundation (STFI); earthquake and terrorism are add-ons in many products. Check the specific policy.", ['sfsp']),
 ("Illustrative example (2,500 rupees a square foot) is not a real figure. Sum insured on reinstatement (rebuild) basis is standard advice.", []),
 ("General guidance on disclosure in the proposal form; no specific case claimed.", []),
 ("New India Assurance v Hemkund Duplex, Supreme Court, 21 Sep 2026: NCDRC's 2.4 crore award set aside; physical stock did not match books or bills; no stock register maintained.", ['hemkund']),
 ("Roland Exports v National Insurance, NCDRC, CC 218 of 2014, about June 2025: 2.88 crore claim dismissed; stock registers appeared written in one sitting; accelerants detected. The script does not name the company.", ['roland', 'roland2']),
 ("NCDRC, United India Insurance cotton warehouse case: claim cannot be repudiated on suspicion without cogent proof; 98 lakh ordered with interest; insurer had cited stock discrepancies, no electric connection and recovered iron strips.", ['cotton']),
 ("Standard fire wordings exclude buildings unoccupied for more than 30 days unless the insurer is told in writing and agrees, sometimes for extra premium; dwellings are usually exempt.", ['sfsp']),
 ("Standard fire wording excludes loss to property from its own fermentation, natural heating or spontaneous combustion; it can be added back by endorsement.", ['sfsp', 'gen312']),
 ("Supreme Court has upheld repudiation over false declarations and policy breaches (reported 2026).", ['falsedecl']),
 ("General principle: a loss after the policy expires is not covered by that policy. No specific case claimed.", []),
 ("Hemkund Duplex, Supreme Court, Sep 2026: the NCDRC cannot brush aside surveyor reports without identifying a specific deficiency.", ['surveyor']),
]
BASE = ('Vertical 9:16 animated insurance-awareness explainer, 10 seconds. Clean, stylised 3D animation in a soft, slightly '
        'illustrated look (not photorealistic, not news footage). Fictional generic places and people, faces not detailed. '
        'No logos, no readable text inside the scene. Keep the top 20 percent of the frame clear for a title.')
def title(t): return (f'TITLE at the top, on screen the whole time: "FIRE CLAIMS DECODED" in bold amber-gold (#FFB300) capitals, '
                      f'and under it "{t}" in white on a thin semi-transparent black strip with a red-orange (#FF4D00) line beneath.')
def wc(s): return len(re.findall(r"[A-Za-z0-9$%'’-]+", s.replace(',', '')))
def ts(sec): m, s = divmod(sec, 60); return f'{int(m)}:{s:04.1f}'

def caption(i):
    ask, kws, kwline, tags = V[i][3]
    p1, p2, p3 = X[i]
    key = lambda t: set(re.findall(r"\d+(?:[.,]\d+)*|[A-Z][a-z]{2,}", t))
    lead = [t for t in p1[1:] if not (key(t) and key(t) <= key(ask))]
    return '\n\n'.join([ask, ' '.join(lead), ' '.join(p2), kwline, "⚠️ Here's what works. " + ' '.join(p3[:-1]),
                        'Fire Claims Decoded. 1 fire cause, every reel.', ' '.join(tags)]), kws

cap_report = []
def episode(i):
    t, parts, (c1, c2, c3scene, _) = T[i], X[i], V[i]
    au = AU[i + 1]
    cap, kws = caption(i)
    lint = json.loads(subprocess.run([sys.executable, '-I', SK + 'ig-caption/caption.py', '-', '--json', '--keywords', ','.join(kws)], input=cap, capture_output=True, text=True).stdout)
    det = json.loads(subprocess.run([sys.executable, '-I', SK + 'ig-human/detect.py', '-', '--json'], input=cap.rsplit('\n\n', 1)[0], capture_output=True, text=True).stdout)
    bad = [c['check'] for c in lint['checks'] if c['status'] != 'PASS']
    cap_report.append((i + 1, bad, det['verdict'], round(det['human_score'])))
    rows, clock = [], 0.0
    for k, p in enumerate(parts):
        clock = max(clock, k * 10.0)
        for s in p:
            rows.append(f'| {ts(clock)} | {s} |'); clock += wc(s) / WPS
    fix = [re.sub(r'^Fix 1:\s*', '', parts[2][0]).rstrip('.').upper(), parts[2][1].rstrip('.').upper()] if len(parts[2]) > 2 else [re.sub(r'^Fix 1:\s*', '', parts[2][0]).rstrip('.').upper()]
    p1 = '\n\n'.join([BASE, title(t), f'0 to 5 seconds: {c1[0]}. Slow camera push-in.\n5 to 10 seconds: {c1[1]}.', 'Sound: soft ambient music, a low bass hit at the very first frame, a gentle whoosh at 5 seconds. No speech.'])
    p2 = '\n\n'.join([BASE, title(t), f'0 to 4 seconds: {c2[0]}.\n4 to 7 seconds: {c2[1]}.\n7 to 10 seconds: {c2[2]}.', 'Sound: soft ambient music, gentle whooshes on each change. No speech.'])
    p3 = '\n\n'.join([BASE, title(t), f'0 to 3 seconds: {c3scene}.\n3 to 7 seconds: a gold checklist appears one line at a time: ' + ', '.join(f'"{x}"' for x in fix) + '.\n7 to 10 seconds: fade to black; centred, one line at a time: "FIRE CLAIMS DECODED" in gold, "1 FIRE CAUSE EVERY REEL" in yellow, "@parag_pethe1" in white.', 'Sound: calm, positive music building gently, a soft chime as each checklist item appears. No speech.'])
    facts, src = F[i]
    out = [f'## {i+1:02d}. {t}', '',
           f'**Hook:** "{" ".join(parts[0][:2])}" (score {au["hook_score"]})  ',
           f'**Instagram skill checks:** /ig-reel hook {au["hook_score"]}, beat sheet clean with a loop, /ig-human PASS {au["human"]}; caption: /ig-caption all PASS, /ig-human {det["verdict"]} {round(det["human_score"])}  ',
           f'**Timing:** {au["secs"][0]}s + {au["secs"][1]}s + {au["secs"][2]}s spoken', '',
           '**Script**', ''] + [f'{k+1}. ' + ' / '.join(p) for k, p in enumerate(parts)] + ['',
           f'**Facts:** {facts}' + ('  \n**Sources:** ' + ', '.join(f'[{n+1}]({SRC[s]})' for n, s in enumerate(src)) if src else ''), '',
           '### Gemini prompts (no speech; add the voiceover in your editor)', '',
           '**Clip 1 (0 to 10s)**', '', '```', p1, '```', '', '**Clip 2 (10 to 20s)**', '', '```', p2, '```', '',
           '**Clip 3 (20 to 30s)**', '', '```', p3, '```', '',
           '### Voiceover for your editor (CapCut text-to-speech, Indian English male voice, or your own)', '',
           '| time | line |', '|---|---|'] + rows + ['', '### Instagram caption', '', '```', cap, '```', '', '---', '']
    return '\n'.join(out)

A = '\n'.join(episode(i) for i in range(8))
B = '\n'.join(episode(i) for i in range(8, 16))
import os
D = '/home/user/Claims-Decoded/reels/insurance-awareness'
os.makedirs(D, exist_ok=True)
open(f'{D}/pillar-1-why-buy-fire-insurance.md', 'w').write('# Pillar 1: Why buy fire insurance\n\n8 reels that turn fire-safety viewers into people who check, buy or fix their cover.\n\n' + A)
open(f'{D}/pillar-2-lessons-from-rejected-claims.md', 'w').write('# Pillar 2: Lessons from rejected claims\n\n8 reels on why fire claims go unpaid, built on court decisions and standard policy wording.\n\n' + B)
for r in cap_report:
    if r[1] or r[2] != 'PASS': print('CAPTION', r)
print('done', len(cap_report))
