"""Fire Claims Decoded carousel builder.

Usage: python3 build.py decks/<deck>.json  ->  out/<deck>/01.png ... (1080x1350)
Slide types: cover, stat, point, split, myth, recap, cta.
Wrap a word in [brackets] to colour it gold.
"""
import json, re, sys, html, pathlib
HERE = pathlib.Path(__file__).resolve().parent
CAT = {"safety": ("Fire safety", "#FFB300"), "trigger": ("Claim trigger", "#FF8A00"),
       "rejection": ("Claim rejection", "#FF4D00"), "insurance": ("Insurance fact", "#FFFFFF")}
FLAME = ('<svg viewBox="0 0 24 32" class="flame"><path d="M12 1c1 6 9 9 9 18a9 9 0 0 1-18 0c0-5 3-7 4-11 1 3 2 4 4 4-1-4 0-8 1-11z" fill="#FF4D00"/>'
         '<path d="M12 14c1 3 5 5 5 9a5 5 0 0 1-10 0c0-3 2-4 2-6 1 1 2 2 3 2 0-2-1-3 0-5z" fill="#FFB300"/></svg>')

def t(s):
    s = html.escape(s)
    return re.sub(r"\[(.+?)\]", r'<span class="gold">\1</span>', s)

def chrome(i, n, accent, body, last=False):
    swipe = "" if last else '<span class="swipe">Swipe &rarr;</span>'
    return f'''<section class="slide" style="--accent:{accent}">
  <div class="glow"></div>
  <header><div class="mark">{FLAME}<span>FIRE CLAIMS DECODED</span></div><div class="count">{i}/{n}</div></header>
  <main>{body}</main>
  <footer><span class="handle">@fireclaimsdecoded</span>{swipe}</footer>
</section>'''

def slide(s, i, n, deck, accent):
    k = s["type"]
    if k == "cover":
        b = f'''<div class="chip">{t(s.get("chip", CAT[deck["category"]][0]))} &middot; File #{deck["file_no"]}</div>
<h1 class="cover-h">{t(s["title"])}</h1><div class="bar"></div><p class="promise">{t(s["promise"])}</p>
<div class="stamp">DECODED</div>'''
    elif k == "stat":
        b = f'<div class="big">{t(s["big"])}</div><h2 class="label">{t(s["label"])}</h2><p class="body">{t(s["body"])}</p>'
    elif k == "point":
        b = f'<div class="num">{s["n"]}</div><h2>{t(s["title"])}</h2><p class="body">{t(s["body"])}</p>'
    elif k == "split":
        b = f'''<div class="num sm">{s["n"]}</div><h2>{t(s["title"])}</h2>
<div class="panel yes"><div class="ptag">&#10003; Covered</div><p>{t(s["yes"])}</p></div>
<div class="panel no"><div class="ptag">&#10007; Not covered</div><p>{t(s["no"])}</p></div>'''
    elif k == "myth":
        b = f'''<div class="num sm">{s["n"]}</div><h2>{t(s["title"])}</h2>
<div class="panel myth"><div class="ptag">&#10007; Myth</div><p><s>{t(s["myth"])}</s></p></div>
<div class="panel yes"><div class="ptag">&#10003; Fact</div><p>{t(s["fact"])}</p></div>'''
    elif k == "recap":
        items = "".join(f'<li><span class="box">&#10003;</span>{t(x)}</li>' for x in s["items"])
        b = f'<h2 class="recap-h">{t(s["title"])}</h2><ul class="check">{items}</ul><p class="disc">General information, not financial or legal advice. Check your own policy.</p>'
    elif k == "cta":
        b = f'''<h2 class="cta-h">{t(s["title"])}</h2>
<div class="acts"><div><b>SAVE</b><span>for your next renewal</span></div><div><b>SHARE</b><span>with someone who owns a shop or factory</span></div><div><b>FOLLOW</b><span>@fireclaimsdecoded</span></div></div>
<div class="lockup">{FLAME}<div><div class="lw">FIRE CLAIMS DECODED</div><div class="tag">{t(s["sub"])}</div></div></div>
<p class="disc">General information, not financial or legal advice. Check your own policy.</p>'''
    return chrome(i, n, accent, f'<div class="t-{k}">{b}</div>', last=(i == n))

def build(path):
    deck = json.loads(pathlib.Path(path).read_text())
    accent = CAT[deck["category"]][1]
    n = len(deck["slides"])
    body = "\n".join(slide(s, i + 1, n, deck, accent) for i, s in enumerate(deck["slides"]))
    doc = f'<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="brand.css"></head><body>{body}</body></html>'
    out = HERE / "out" / pathlib.Path(path).stem
    out.mkdir(parents=True, exist_ok=True)
    (HERE / f"_{pathlib.Path(path).stem}.html").write_text(doc)
    import subprocess
    subprocess.run(["node", str(HERE / "render.js"), str(HERE / f"_{pathlib.Path(path).stem}.html"), str(out)], check=True)
    print(out)

if __name__ == "__main__":
    build(sys.argv[1])
