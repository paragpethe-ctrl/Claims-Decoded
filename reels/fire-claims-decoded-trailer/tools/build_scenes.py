OUT = __import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'compositions') + '/'

CSS = """    #root { position: absolute; inset: 0; overflow: hidden; }
    .stage { position: absolute; inset: 0; }
    .flash { position: absolute; inset: 0; background: #fff4e2; opacity: 0; }
    .t {
      position: absolute;
      left: 66px;
      font-family: "Oswald", sans-serif;
      font-weight: 700;
      text-transform: uppercase;
      line-height: 0.95;
      color: #fff6ec;
      text-shadow: 0 4px 0 rgba(0, 0, 0, 0.35), 0 10px 44px rgba(0, 0, 0, 0.9), 0 0 18px rgba(0, 0, 0, 0.55);
      white-space: nowrap;
    }
    .hot { color: #ff8a24; }
    .heavy { font-family: "Archivo Black", sans-serif; font-weight: 400; }
    .slab {
      background: #0b0908;
      padding: 12px 26px 18px;
      text-shadow: none;
    }
    .ln { display: block; }
    .ln > span { display: inline-block; }
    svg.draw { position: absolute; overflow: visible; }
    .wire { fill: none; stroke: #ffe6c8; stroke-width: 7; stroke-linecap: round; stroke-linejoin: round; }
    .wire-hot { fill: none; stroke: #ff6a12; stroke-width: 15; stroke-linecap: round; stroke-linejoin: round; opacity: 0.55; }
    .spark { fill: #ffd27a; }"""

JS_HELPERS = """      // seeded PRNG so every shake is the same on every render
      function rng(seed) { return function () { seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
      function shake(sel, t0, amp, dur, seed) {
        const r = rng(seed), n = Math.round(dur * 30);
        for (let i = 0; i < n; i++) {
          const k = Math.pow(1 - i / n, 1.6);
          tl.set(sel, { x: (r() * 2 - 1) * amp * k, y: (r() * 2 - 1) * amp * k, rotation: (r() * 2 - 1) * amp * 0.02 * k }, t0 + i / 30);
        }
        tl.set(sel, { x: 0, y: 0, rotation: 0 }, t0 + dur);
      }
      function flash(sel, t0, a) {
        tl.set(sel, { opacity: a }, t0);
        tl.to(sel, { opacity: 0, duration: 0.2, ease: "power2.out" }, t0 + 0.034);
      }
      function slam(sel, t0, from) {
        tl.fromTo(sel, { opacity: 0, scale: from || 1.7, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.16, ease: "power4.out" }, t0);
      }
      function cut(sel, t0) { tl.set(sel, { opacity: 0 }, t0); }"""

def scene(sid, body, js, extra_css=""):
    return f'''<template>
  <style>
{CSS}
{extra_css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920">
    <div id="{sid}-stage" class="stage">
{body}
    </div>
    <div id="{sid}-flash" class="flash"></div>
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
{JS_HELPERS}
{js}
      window.__timelines["{sid}"] = tl;
    }})();
  </script>
</template>
'''

def t(id_, top, size, lines, cls="", left=None, style=""):
    inner = "".join(f'<span class="ln"><span>{l}</span></span>' for l in lines)
    l = f"left: {left}px; " if left is not None else ""
    return f'      <div id="{id_}" class="t {cls}" style="{l}top: {top}px; font-size: {size}px; {style}">{inner}</div>'

# ---------------- S1 hook 0-3 ----------------
s1 = "\n".join([
    t("s1-stop", 330, 250, ["STOP."], "heavy"),
    t("s1-there", 300, 100, ["THERE ARE"]),
    t("s1-three", 400, 560, ["3"], "heavy hot", style="line-height: 0.82;"),
    t("s1-causes", 880, 160, ["FIRE CAUSES"]),
    t("s1-in", 300, 190, ["IN YOUR", "BUILDING."]),
    t("s1-now", 700, 175, ["RIGHT NOW."], "hot"),
])
s1_js = """      gsap.set(["#s1-there", "#s1-three", "#s1-causes", "#s1-in", "#s1-now"], { opacity: 0 });
      // frame 0 already reads STOP: it lands with a shake, no fade
      tl.fromTo("#s1-stop", { scale: 1.12 }, { scale: 1, duration: 0.2, ease: "power4.out", transformOrigin: "0% 50%" }, 0);
      shake("#s1-stage", 0, 26, 0.4, 11);
      cut("#s1-stop", 0.6);
      slam("#s1-there", 0.6, 1.3);
      slam("#s1-three", 0.75, 2.2);
      flash("#s1-flash", 0.75, 0.55);
      shake("#s1-stage", 0.75, 34, 0.45, 12);
      slam("#s1-causes", 1.0, 1.4);
      cut(["#s1-there", "#s1-three", "#s1-causes"], 2.0);
      slam("#s1-in", 2.0, 1.5);
      shake("#s1-stage", 2.0, 22, 0.3, 13);
      slam("#s1-now", 2.45, 1.6);
      shake("#s1-stage", 2.45, 30, 0.35, 14);
      cut(["#s1-in", "#s1-now"], 2.98);"""
open(OUT + "s1.html", "w").write(scene("s1", s1, s1_js))

# ---------------- S2 three causes 3-9 ----------------
socket = '''        <rect class="wire-hot" x="20" y="0" width="420" height="540" rx="22" />
        <rect class="wire" x="20" y="0" width="420" height="540" rx="22" />
        <rect class="wire" x="70" y="50" width="140" height="170" rx="10" />
        <rect class="wire" x="250" y="50" width="140" height="170" rx="10" />
        <rect class="wire" x="105" y="290" width="250" height="200" rx="16" />
        <circle class="wire" cx="230" cy="340" r="20" />
        <circle class="wire" cx="180" cy="430" r="14" />
        <circle class="wire" cx="280" cy="430" r="14" />
        <path class="wire-hot" d="M 280 430 C 330 470, 380 470, 410 500" />
        <path class="wire" d="M 280 430 C 330 470, 380 470, 410 500" />
        <g class="spk"><path class="spark" d="M 410 470 L 420 494 L 446 500 L 420 506 L 410 532 L 400 506 L 374 500 L 400 494 Z" /></g>'''
duct = '''        <path class="wire-hot" d="M 170 0 L 170 260 M 290 0 L 290 260" />
        <path class="wire" d="M 170 -40 L 170 260 M 290 -40 L 290 260" />
        <polygon class="wire-hot" points="120,260 340,260 430,470 30,470" />
        <polygon class="wire" points="120,260 340,260 430,470 30,470" />
        <path class="wire" d="M 50 430 L 410 430" />
        <path class="wire-hot" d="M 186 260 L 186 0 M 274 260 L 274 0" style="stroke: #ff8a24; stroke-width: 9; opacity: 1" />
        <path class="wire" d="M 120 540 Q 230 620 340 540 Z" />
        <g class="spk"><path class="spark" d="M 230 470 C 205 500, 205 525, 230 540 C 255 525, 255 500, 230 470 Z" /></g>'''
pile = '''        <rect class="wire-hot" x="0" y="330" width="210" height="160" />
        <rect class="wire" x="0" y="330" width="210" height="160" />
        <rect class="wire-hot" x="220" y="330" width="210" height="160" />
        <rect class="wire" x="220" y="330" width="210" height="160" />
        <rect class="wire" x="70" y="180" width="230" height="150" />
        <rect class="wire" x="130" y="50" width="150" height="130" />
        <path class="wire" d="M 70 255 L 300 255 M 0 410 L 430 410" style="stroke-width: 4; opacity: 0.6" />
        <g class="spk"><path class="spark" d="M 380 560 L 440 620 M 440 560 L 380 620" style="stroke: #ff8a24; stroke-width: 14; stroke-linecap: round" /></g>'''
causes = [("1", ["LOOSE", "WIRING"], socket), ("2", ["GREASY", "KITCHEN DUCTS"], duct), ("3", ["BLOCKED", "AISLES"], pile)]
parts = []
for i, (num, name, art) in enumerate(causes):
    k = i + 1
    parts.append(f'''      <div id="s2-c{k}" class="cause" style="position: absolute; inset: 0;">
{t(f"s2-n{k}", 270, 330, [num], "heavy hot", style="line-height: 0.8;")}
{t(f"s2-name{k}", 560, 140, name)}
        <svg class="draw" id="s2-art{k}" width="460" height="640" viewBox="0 0 460 640" style="left: 300px; top: 900px;">
{art}
        </svg>
      </div>''')
s2 = "\n".join(parts)
s2_js = """      gsap.set(["#s2-c2", "#s2-c3"], { opacity: 0 });
      gsap.set([".spk"], { opacity: 0 });
      [1, 2, 3].forEach((k, i) => {
        const t0 = i * 2;
        if (i > 0) tl.set("#s2-c" + k, { opacity: 1 }, t0);
        // whip in from the right, matched to the outgoing whip
        tl.fromTo("#s2-c" + k, { x: 900, filter: "blur(16px)" }, { x: 0, filter: "blur(0px)", duration: 0.22, ease: "power3.out" }, t0);
        slam("#s2-n" + k, t0 + 0.05, 2.0);
        shake("#s2-stage", t0 + 0.05, 26, 0.35, 20 + k);
        slam("#s2-name" + k, t0 + 0.3, 1.4);
        tl.fromTo("#s2-art" + k, { scale: 1.25, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: "expo.out" }, t0 + 0.2);
        // the cause ignites
        tl.set("#s2-c" + k + " .spk", { opacity: 1 }, t0 + 1.0);
        tl.fromTo("#s2-c" + k + " .spk", { scale: 0.2, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.25, ease: "back.out(3)" }, t0 + 1.0);
        flash("#s2-flash", t0 + 1.0, 0.35);
        shake("#s2-stage", t0 + 1.0, 14, 0.3, 30 + k);
        // whip out at full speed
        tl.to("#s2-c" + k, { x: -1000, filter: "blur(16px)", duration: 0.18, ease: "power3.in" }, t0 + 1.82);
      });"""
open(OUT + "s2.html", "w").write(scene("s2", s2, s2_js))

# ---------------- S3 turn 9-13 (local 0-4) ----------------
s3 = "\n".join([
    t("s3-walk", 330, 200, ["YOU WALK", "PAST THEM"]),
    t("s3-every", 740, 175, ["EVERY DAY."], "hot"),
    t("s3-until", 330, 150, ["UNTIL ONE", "STARTS A FIRE."], "slab"),
    '''      <div id="s3-stamp" class="t heavy" style="left: 120px; top: 860px; font-size: 118px; color: #ff3b2f; border: 12px solid #ff3b2f; padding: 18px 34px 22px; background: rgba(11, 9, 8, 0.9); text-shadow: none; transform: rotate(-9deg);"><span class="ln"><span>FIRE CLAIM</span></span></div>''',
])
s3_js = """      gsap.set(["#s3-every", "#s3-until", "#s3-stamp"], { opacity: 0 });
      gsap.set("#s3-walk .ln", { opacity: 0 });
      tl.fromTo("#s3-walk .ln", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.25, ease: "power4.out" }, 0.0);
      slam("#s3-every", 0.6, 1.3);
      tl.to(["#s3-walk", "#s3-every"], { opacity: 0, filter: "blur(10px)", duration: 0.15, ease: "power2.in" }, 1.85);
      // the fire takes the frame
      flash("#s3-flash", 2.0, 0.9);
      slam("#s3-until", 2.02, 1.5);
      shake("#s3-stage", 2.0, 44, 0.6, 40);
      // the claim gets stamped
      tl.fromTo("#s3-stamp", { opacity: 0, scale: 2.4, rotation: -4 }, { opacity: 1, scale: 1, rotation: -9, duration: 0.12, ease: "power4.in" }, 2.9);
      shake("#s3-stage", 3.02, 36, 0.4, 41);
      flash("#s3-flash", 3.02, 0.4);"""
open(OUT + "s3.html", "w").write(scene("s3", s3, s3_js))

# ---------------- S4 reveal 13-19 (local 0-6) ----------------
title_a = "".join(f'<span class="ch">{c if c != " " else "&nbsp;"}</span>' for c in "FIRE CLAIMS")
title_b = "".join(f'<span class="ch">{c}</span>' for c in "DECODED")
s4 = f'''      <div id="s4-title" class="t" style="top: 420px;">
        <span class="ln" style="font-size: 172px;">{title_a}</span>
        <span class="ln hot" style="font-size: 240px; line-height: 0.9;">{title_b}</span>
        <span id="s4-rule" class="ln" style="width: 520px; height: 12px; background: #ff8a24; margin-top: 20px; box-shadow: none;"></span>
      </div>
{t("s4-eng", 980, 96, ["I'M AN ENGINEER IN", "PROPERTY INSURANCE."])}
{t("s4-show", 980, 96, ["I SHOW YOU HOW", "FIRES <span class='hot'>REALLY</span> START."])}'''
s4_css = "    .ch { display: inline-block; }"
s4_js = """      gsap.set(["#s4-eng", "#s4-show"], { opacity: 0 });
      gsap.set("#s4-title .ch", { opacity: 0 });
      flash("#s4-flash", 0, 0.95);
      tl.fromTo("#s4-title .ch", { opacity: 0, scale: 2.6, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.14, stagger: 0.035, ease: "power4.out" }, 0.02);
      tl.fromTo("#s4-rule", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 0.4, ease: "expo.out" }, 0.55);
      shake("#s4-stage", 0.02, 40, 0.7, 50);
      // the name moves up and the promise lands under it
      tl.to("#s4-title", { y: -150, scale: 0.78, transformOrigin: "0% 0%", duration: 0.35, ease: "power3.inOut" }, 1.75);
      slam("#s4-eng", 2.0, 1.4);
      shake("#s4-stage", 2.0, 18, 0.3, 51);
      cut("#s4-eng", 4.0);
      slam("#s4-show", 4.0, 1.4);
      shake("#s4-stage", 4.0, 18, 0.3, 52);
      tl.to(["#s4-title", "#s4-show"], { opacity: 0, filter: "blur(10px)", duration: 0.14, ease: "power2.in" }, 5.86);"""
open(OUT + "s4.html", "w").write(scene("s4", s4, s4_js, s4_css))

# ---------------- S5 promise 19-24.5 (local 0-5.5) ----------------
words = ["HOMES.", "SHOPS.", "RESTAURANTS.", "WAREHOUSES.", "FACTORIES."]
slot = "".join(f'<span class="slotw" style="position: absolute; left: 0; top: 0;">{w}</span>' for w in words)
s5 = f'''      <div id="s5-slot" class="t hot" style="top: 330px; font-size: 128px; height: 130px; width: 960px;">{slot}</div>
{t("s5-one", 500, 112, ["ONE OCCUPANCY", "AT A TIME."])}
{t("s5-starts", 330, 190, ["HOW IT", "STARTS."], "hot")}
{t("s5-stop", 760, 190, ["HOW TO", "STOP IT."])}'''
s5_js = """      gsap.set(["#s5-one", "#s5-starts", "#s5-stop"], { opacity: 0 });
      gsap.set(".slotw", { opacity: 0 });
      // occupancy names roll like a slot machine, a hard cut each 0.4 s
      document.querySelectorAll(".slotw").forEach((el, i) => {
        const t0 = 0.0 + i * 0.4;
        tl.set(el, { opacity: 1 }, t0);
        tl.fromTo(el, { y: 60 }, { y: 0, duration: 0.12, ease: "power4.out" }, t0);
        if (i < 4) tl.set(el, { opacity: 0 }, t0 + 0.4);
      });
      shake("#s5-stage", 0.0, 16, 0.25, 60);
      slam("#s5-one", 0.5, 1.3);
      cut(["#s5-slot", "#s5-one"], 1.98);
      slam("#s5-starts", 2.0, 1.6);
      shake("#s5-stage", 2.0, 30, 0.45, 61);
      slam("#s5-stop", 3.0, 1.4);
      // as the fire dies, STARTS cools to grey and STOP IT holds
      tl.to("#s5-starts", { color: "#8a7f78", duration: 0.6, ease: "power2.out" }, 3.2);
      tl.to(["#s5-starts", "#s5-stop"], { opacity: 0, filter: "blur(10px)", duration: 0.2, ease: "power2.in" }, 5.25);"""
open(OUT + "s5.html", "w").write(scene("s5", s5, s5_js))

# ---------------- S6 claim 24.5-27.5 (local 0-3) ----------------
claim_words = [("SO YOU NEVER", ""), ("HAVE TO MAKE", ""), ("THE CLAIM.", "hot")]
lines = "".join(f'<span class="ln {c}">' + " ".join(f'<span class="w">{w}</span>' for w in l.split()) + '</span>' for l, c in claim_words)
s6 = f'''      <div id="s6-claim" class="t" style="top: 520px; font-size: 168px; line-height: 1.02;">{lines}</div>'''
s6_css = "    .w { display: inline-block; }"
s6_js = """      gsap.set("#s6-claim .w", { opacity: 0 });
      tl.fromTo("#s6-claim .w", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.16, stagger: 0.12, ease: "power3.out" }, 0.15);
      tl.to("#s6-claim", { opacity: 0, filter: "blur(10px)", duration: 0.18, ease: "power2.in" }, 2.8);"""
open(OUT + "s6.html", "w").write(scene("s6", s6, s6_js, s6_css))

# ---------------- S7 end card 27.5-31.5 (local 0-4) ----------------
s7 = f'''      <div id="s7-mark" class="t" style="top: 420px;">
        <span class="ln" style="font-size: 172px;">FIRE CLAIMS</span>
        <span class="ln hot" style="font-size: 240px; line-height: 0.9;">DECODED</span>
        <span id="s7-rule" class="ln" style="width: 520px; height: 12px; background: #ff8a24; margin-top: 20px;"></span>
      </div>
{t("s7-handle", 960, 96, ["@parag_pethe1"], style="text-transform: none;")}
{t("s7-cta", 1090, 64, ["FOLLOW &middot; 1 FIRE CAUSE EVERY REEL"])}'''
s7_js = """      gsap.set(["#s7-handle", "#s7-cta"], { opacity: 0 });
      flash("#s7-flash", 0, 0.85);
      tl.fromTo("#s7-mark", { scale: 1.35, opacity: 0, filter: "blur(12px)" }, { scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.2, ease: "power4.out", transformOrigin: "0% 50%" }, 0.0);
      tl.fromTo("#s7-rule", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 0.45, ease: "expo.out" }, 0.3);
      shake("#s7-stage", 0.0, 34, 0.5, 70);
      slam("#s7-handle", 0.8, 1.3);
      tl.fromTo("#s7-cta", { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "power2.out" }, 1.15);"""
open(OUT + "s7.html", "w").write(scene("s7", s7, s7_js))
print("ok")
