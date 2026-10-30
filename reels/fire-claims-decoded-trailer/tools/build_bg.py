"""Builds compositions/bg.html: one vivid background world per beat of the trailer, under the fire."""
import math, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'compositions', 'bg.html')

def f(x): return f"{x:.1f}".rstrip('0').rstrip('.')

# ---------- 2. market street: skyline, poles, tangled wires, gas cylinders, hot spots ----------
street = []
bx = -40
heights = [430, 560, 380, 620, 470, 540, 400, 590, 450]
widths = [190, 160, 210, 150, 180, 170, 200, 160, 190]
for i, (w, h) in enumerate(zip(widths, heights)):
    top = 1500 - h
    street.append(f'<rect x="{bx}" y="{top}" width="{w}" height="{h + 40}" fill="#2b0b2e" />')
    # lit windows
    for r in range(2, h // 90):
        for c in range(w // 60):
            if (i * 7 + r * 3 + c * 5) % 4 != 0:
                street.append(f'<rect x="{bx + 18 + c * 58}" y="{top + r * 80 - 120}" width="26" height="34" fill="#ffb347" opacity="{0.55 + ((i + r + c) % 3) * 0.15:.2f}" />')
    # shop shutter at street level
    street.append(f'<rect x="{bx + 16}" y="1380" width="{w - 32}" height="120" fill="{["#16a5a5", "#ffcf3f", "#ff4fa3"][i % 3]}" opacity="0.85" />')
    for k in range(5):
        street.append(f'<line x1="{bx + 16}" x2="{bx + w - 16}" y1="{1392 + k * 22}" y2="{1392 + k * 22}" stroke="#2b0b2e" stroke-width="3" opacity="0.5" />')
    bx += w + 6
street.append('<rect x="-60" y="1500" width="1460" height="460" fill="#1d0720" />')
poles = [140, 640, 1150]
for x in poles:
    street.append(f'<rect x="{x - 9}" y="820" width="18" height="700" fill="#14051a" />')
    street.append(f'<rect x="{x - 70}" y="850" width="140" height="12" fill="#14051a" />')
# the tangle: many sagging wires between poles, more around the middle pole
wires = []
for a, b in ((poles[0], poles[1]), (poles[1], poles[2])):
    for k in range(9):
        y0 = 856 + k * 9 + (k % 3) * 6
        y1 = 860 + ((k * 5) % 9) * 10
        sag = 90 + (k * 37) % 120
        wires.append(f'<path d="M {a} {y0} Q {(a + b) / 2 + ((k % 4) - 1.5) * 30} {max(y0, y1) + sag} {b} {y1}" fill="none" stroke="#14051a" stroke-width="{4 + k % 3}" />')
for k in range(7):   # drops from the pole into the shops
    wires.append(f'<path d="M {poles[1]} {870 + k * 12} Q {poles[1] + (k - 3) * 60} {1100 + k * 20} {poles[1] + (k - 3) * 110} {1385}" fill="none" stroke="#14051a" stroke-width="4" />')
street += wires
street.append(f'<rect x="{poles[1] + 14}" y="1060" width="70" height="96" rx="6" fill="#14051a" />')
# LPG cylinders and piled cartons on the footpath
for k in range(5):
    x = 760 + k * 64
    street.append(f'<rect x="{x}" y="1418" width="54" height="104" rx="22" fill="#e0213f" />')
    street.append(f'<rect x="{x + 17}" y="1402" width="20" height="20" rx="4" fill="#8a0f24" />')
    street.append(f'<rect x="{x + 4}" y="1450" width="46" height="8" fill="#ff8aa0" opacity="0.6" />')
for (x, y, w, h) in ((60, 1430, 120, 90), (80, 1350, 100, 80), (190, 1450, 110, 70), (95, 1280, 80, 70)):
    street.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#c77d3a" stroke="#6a3b12" stroke-width="4" />')
street_svg = "\n            ".join(street)
hot = [(poles[1], 905), (390, 990), (poles[1] + 49, 1108), (905, 960)]
hot_html = "\n".join(f'          <div class="hotspot" style="left: {x - 60}px; top: {y - 60}px;"></div>' for x, y in hot)

# ---------- 4. thermal view of an electrical panel ----------
th = ['<rect x="200" y="1300" width="680" height="640" rx="10" fill="rgba(70,10,110,0.55)" stroke="#ff4fa3" stroke-width="6" />']
for r in range(3):
    for c in range(6):
        x = 240 + c * 102; y = 1380 + r * 170
        hotb = (r, c) == (1, 3)
        th.append(f'<rect x="{x}" y="{y}" width="80" height="130" rx="6" fill="{"#fff3b0" if hotb else "rgba(160,30,140,0.55)"}" stroke="{"#ffe14d" if hotb else "#d1458f"}" stroke-width="4" {"id=\"th-hot\"" if hotb else ""}/>')
        th.append(f'<path d="M {x + 40} {y} C {x + 40} {y - 50}, {x + 20 + c * 4} {1320}, {x + 40} 1300" fill="none" stroke="{"#ffd23f" if hotb else "#ff7a3d"}" stroke-width="{7 if hotb else 4}" />')
thermal_svg = "\n            ".join(th)
hx, hy = 240 + 3 * 102 + 40, 1380 + 170 + 65   # hot breaker centre

# ---------- 5. occupancy silhouettes ----------
occ = {
 "home": ("linear-gradient(180deg, #004d52 0%, #00918c 50%, #19d3c5 100%)", '''<polygon points="180,1180 540,880 900,1180" fill="#9ff7ec" opacity="0.35" />
            <rect x="250" y="1180" width="580" height="520" fill="#9ff7ec" opacity="0.3" />
            <rect x="320" y="1280" width="160" height="150" fill="#004d52" opacity="0.5" />
            <rect x="600" y="1420" width="140" height="280" fill="#004d52" opacity="0.5" />'''),
 "shop": ("linear-gradient(180deg, #6e0036 0%, #c4005c 50%, #ff4fa3 100%)", '''<rect x="140" y="1000" width="800" height="90" fill="#ffd1e6" opacity="0.4" />
            ''' + "".join(f'<path d="M {140 + k * 100} 1090 q 50 70 100 0" fill="{["#ffd1e6", "#ff9cc9"][k % 2]}" opacity="0.45" />' for k in range(8)) + '''
            <rect x="180" y="1170" width="720" height="530" fill="#ffd1e6" opacity="0.25" />
            ''' + "".join(f'<line x1="200" x2="880" y1="{1200 + k * 40}" y2="{1200 + k * 40}" stroke="#6e0036" stroke-width="6" opacity="0.35" />' for k in range(12))),
 "rest": ("linear-gradient(180deg, #8f2a00 0%, #d35400 50%, #ffb100 100%)", '''<polygon points="300,980 780,980 900,1200 180,1200" fill="#ffe0a3" opacity="0.32" />
            <rect x="490" y="760" width="100" height="220" fill="#ffe0a3" opacity="0.32" />
            <path d="M 300 1520 Q 540 1700 780 1520 Z" fill="#ffe0a3" opacity="0.4" />
            <path d="M 540 1300 C 470 1380, 470 1460, 540 1510 C 610 1460, 610 1380, 540 1300 Z" fill="#fff4d6" opacity="0.55" />
            <rect x="380" y="1640" width="320" height="40" fill="#ffe0a3" opacity="0.32" />'''),
 "ind": ("linear-gradient(180deg, #06205f 0%, #1546c4 50%, #4f8fff 100%)", '''<polygon points="120,1300 300,1180 300,1300 480,1180 480,1300 660,1180 660,1300 840,1180 840,1300 960,1300 960,1720 120,1720" fill="#bcd6ff" opacity="0.3" />
            <rect x="700" y="880" width="70" height="300" fill="#bcd6ff" opacity="0.3" />
            <rect x="820" y="940" width="60" height="240" fill="#bcd6ff" opacity="0.3" />
            <circle cx="735" cy="830" r="50" fill="#bcd6ff" opacity="0.18" />
            <circle cx="780" cy="760" r="70" fill="#bcd6ff" opacity="0.14" />
            ''' + "".join(f'<rect x="{170 + k * 150}" y="1440" width="90" height="120" fill="#06205f" opacity="0.35" />' for k in range(5))),
}
occ_html = "\n".join(f'''      <div id="bg-occ-{k}" class="layer" style="background: {g};">
        <svg class="art" id="occ-art-{k}" width="1080" height="1920" viewBox="0 0 1080 1920">
            {art}
        </svg>
      </div>''' for k, (g, art) in occ.items())

# ---------- 7. water spray from an extinguisher / sprinkler ----------
spray = []
for k in range(34):
    ang = math.radians(112 + k * 1.6 + (k % 3) * 0.7)
    L = 1500 + (k * 97) % 600
    x2 = 980 + math.cos(ang) * L; y2 = 140 + math.sin(ang) * L
    spray.append(f'<line class="drop" x1="980" y1="140" x2="{f(x2)}" y2="{f(y2)}" stroke="#e8f6ff" stroke-width="{3 + k % 4}" stroke-linecap="round" stroke-dasharray="{40 + k % 5 * 12} {120 + (k * 13) % 90}" opacity="{0.35 + (k % 4) * 0.12:.2f}" />')
spray_svg = "\n            ".join(spray)

html = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; overflow: hidden; background: #1a0004; }}
    .layer {{ position: absolute; inset: 0; opacity: 0; overflow: hidden; }}
    .art {{ position: absolute; left: 0; top: 0; overflow: visible; }}
    #bg-alarm {{ opacity: 1; background: radial-gradient(120% 80% at 50% 82%, #ff3b1f 0%, #c40018 38%, #4a0008 75%, #1a0004 100%); }}
    #alarm-beams {{
      position: absolute; left: -1060px; top: -840px; width: 3200px; height: 3200px;
      background: repeating-conic-gradient(from 0deg, rgba(255, 226, 196, 0.17) 0deg 13deg, rgba(255, 226, 196, 0) 13deg 45deg);
    }}
    .strobe {{ position: absolute; inset: 0; background: #ffe9dc; opacity: 0; }}
    #bg-street {{ background: linear-gradient(180deg, #2a0845 0%, #7b1556 40%, #e0464a 62%, #ff9a3b 82%, #ffd36b 100%); }}
    #street-sun {{ position: absolute; left: 520px; top: 900px; width: 560px; height: 560px; border-radius: 50%; background: radial-gradient(circle, #fff3c4 0%, #ffc85a 35%, rgba(255, 160, 60, 0) 70%); }}
    .hotspot {{ position: absolute; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #fffbe0 0%, #ffd23f 18%, rgba(255, 110, 20, 0.75) 38%, rgba(255, 80, 0, 0) 70%); }}
    #bg-engulf {{ background: radial-gradient(120% 90% at 50% 90%, #8a1500 0%, #3a0700 55%, #120200 100%); }}
    #bg-thermal {{ background: radial-gradient(130% 90% at 50% 75%, #3d0b6b 0%, #1c0638 55%, #0b0218 100%); }}
    .blob {{ position: absolute; border-radius: 50%; mix-blend-mode: screen; }}
    #th-halo {{ position: absolute; left: {hx - 220}px; top: {hy - 220}px; width: 440px; height: 440px; border-radius: 50%; background: radial-gradient(circle, rgba(255, 252, 220, 0.95) 0%, rgba(255, 210, 60, 0.8) 22%, rgba(255, 90, 0, 0.45) 45%, rgba(200, 0, 120, 0) 72%); }}
    #bg-starts {{ background: radial-gradient(120% 80% at 50% 88%, #ff5a00 0%, #b80000 45%, #2a0000 100%); }}
    #bg-prevent {{ background: radial-gradient(130% 90% at 80% 10%, #6fd0ff 0%, #0a6cff 40%, #062a7a 100%); }}
    .mist {{ position: absolute; border-radius: 50%; background: radial-gradient(circle, rgba(235, 248, 255, 0.5) 0%, rgba(235, 248, 255, 0) 70%); }}
    #bg-claim {{ background: linear-gradient(180deg, #02402a 0%, #047a4c 45%, #12d18e 100%); }}
    #claim-rays {{
      position: absolute; left: -1060px; top: -600px; width: 3200px; height: 3200px;
      background: repeating-conic-gradient(from 0deg, rgba(220, 255, 236, 0.09) 0deg 8deg, rgba(220, 255, 236, 0) 8deg 30deg);
    }}
    #bg-end {{ background: radial-gradient(130% 70% at 50% 100%, #ff6a1f 0%, #c21807 35%, #4a0303 70%, #1a0101 100%); }}
  </style>
  <div id="root" data-composition-id="bg" data-width="1080" data-height="1920">
      <!-- 0-3 alarm -->
      <div id="bg-alarm" class="layer">
        <div id="alarm-beams"></div>
        <div id="alarm-strobe" class="strobe"></div>
      </div>
      <!-- 3-5.5 the everyday street -->
      <div id="bg-street" class="layer">
        <div id="street-sun"></div>
        <div id="street-pan" style="position: absolute; left: 0; right: 0; top: 190px; bottom: -190px;">
          <svg class="art" width="1300" height="1920" viewBox="0 0 1300 1920">
            {street_svg}
          </svg>
{hot_html}
        </div>
      </div>
      <!-- 5.5-10 the engulf (the fire covers it) -->
      <div id="bg-engulf" class="layer"></div>
      <!-- 10-16 decoded: the thermal camera sees the invisible -->
      <div id="bg-thermal" class="layer">
        <div class="blob" id="b1" style="left: -200px; top: 200px; width: 900px; height: 900px; background: radial-gradient(circle, rgba(123, 31, 162, 0.85) 0%, rgba(123, 31, 162, 0) 70%);"></div>
        <div class="blob" id="b2" style="left: 420px; top: 520px; width: 800px; height: 800px; background: radial-gradient(circle, rgba(194, 24, 91, 0.75) 0%, rgba(194, 24, 91, 0) 70%);"></div>
        <div class="blob" id="b3" style="left: 80px; top: 1050px; width: 760px; height: 760px; background: radial-gradient(circle, rgba(255, 109, 0, 0.55) 0%, rgba(255, 109, 0, 0) 70%);"></div>
        <div class="blob" id="b4" style="left: 520px; top: 1200px; width: 640px; height: 640px; background: radial-gradient(circle, rgba(255, 171, 0, 0.45) 0%, rgba(255, 171, 0, 0) 70%);"></div>
        <div class="blob" id="b5" style="left: 600px; top: -200px; width: 700px; height: 700px; background: radial-gradient(circle, rgba(90, 20, 180, 0.7) 0%, rgba(90, 20, 180, 0) 70%);"></div>
        <div id="th-panel" style="position: absolute; left: 0; right: 0; top: 90px; bottom: -90px;">
        <svg class="art" width="1080" height="1920" viewBox="0 0 1080 1920">
            {thermal_svg}
        </svg>
        <div id="th-halo"></div>
        <svg class="art" id="th-cross" width="1080" height="1920" viewBox="0 0 1080 1920">
          <path d="M {hx - 110} {hy - 70} v -40 h 40 M {hx + 70} {hy - 110} h 40 v 40 M {hx + 110} {hy + 70} v 40 h -40 M {hx - 70} {hy + 110} h -40 v -40" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="square" />
          <path d="M {hx - 26} {hy} h 52 M {hx} {hy - 26} v 52" stroke="#ffffff" stroke-width="5" />
        </svg>
        </div>
      </div>
      <!-- 16-18 one occupancy at a time -->
{occ_html}
      <!-- 18-19 how it starts -->
      <div id="bg-starts" class="layer"></div>
      <!-- 19-20.6 how to prevent it -->
      <div id="bg-prevent" class="layer">
        <div class="mist" id="m1" style="left: 80px; top: 900px; width: 900px; height: 900px;"></div>
        <div class="mist" id="m2" style="left: -200px; top: 1300px; width: 800px; height: 800px;"></div>
        <svg class="art" width="1080" height="1920" viewBox="0 0 1080 1920">
            {spray_svg}
            <circle cx="980" cy="140" r="34" fill="#e8f6ff" />
            <rect x="950" y="40" width="60" height="80" rx="10" fill="#e8f6ff" />
        </svg>
      </div>
      <!-- 20.6-23.5 so you never have to make the claim -->
      <div id="bg-claim" class="layer">
        <div id="claim-rays"></div>
        <svg class="art" width="1080" height="1920" viewBox="0 0 1080 1920">
          <path d="M 540 1150 L 820 1250 L 800 1520 Q 760 1720 540 1820 Q 320 1720 280 1520 L 260 1250 Z" fill="#7dffc6" opacity="0.28" />
          <path id="claim-check" d="M 420 1490 L 510 1580 L 680 1390" fill="none" stroke="#ffffff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" pathLength="100" style="stroke-dasharray: 100 120; stroke-dashoffset: 110;" />
        </svg>
      </div>
      <!-- 23.5-27.5 end card -->
      <div id="bg-end" class="layer"></div>
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      // one world per beat, hard cuts on the beat
      const worlds = [["#bg-alarm", 0], ["#bg-street", 3], ["#bg-engulf", 5.5], ["#bg-thermal", 10], ["#bg-occ-home", 16], ["#bg-occ-shop", 16.4], ["#bg-occ-rest", 16.8], ["#bg-occ-ind", 17.2], ["#bg-starts", 18], ["#bg-prevent", 19], ["#bg-claim", 20.6], ["#bg-end", 23.5]];
      worlds.forEach(([sel, t0], i) => {{
        if (i > 0) tl.set(sel, {{ opacity: 1 }}, t0);
        if (i < worlds.length - 1) tl.set(sel, {{ opacity: 0 }}, worlds[i + 1][1]);
      }});
      // alarm: siren beams sweep, a strobe on every slam
      tl.fromTo("#alarm-beams", {{ rotation: 0 }}, {{ rotation: 240, duration: 3, ease: "none" }}, 0);
      [0, 0.75, 1.2, 2.0].forEach((t0) => {{
        tl.set("#alarm-strobe", {{ opacity: 0.38 }}, t0);
        tl.to("#alarm-strobe", {{ opacity: 0, duration: 0.25, ease: "power2.out" }}, t0 + 0.034);
      }});
      // street: we walk past; the hidden hot spots pulse
      tl.fromTo("#street-pan", {{ x: 0 }}, {{ x: -150, duration: 2.5, ease: "none" }}, 3);
      tl.fromTo("#street-sun", {{ y: 0 }}, {{ y: 30, duration: 2.5, ease: "none" }}, 3);
      gsap.utils.toArray(".hotspot").forEach((el, i) => {{
        tl.fromTo(el, {{ opacity: 0.25, scale: 0.7 }}, {{ opacity: 1, scale: 1.15, duration: 0.42, ease: "sine.inOut", repeat: 5, yoyo: true }}, 3 + i * 0.13);
      }});
      // thermal: heat drifts, the camera locks on to the hot breaker
      [["#b1", 80, -60], ["#b2", -90, 70], ["#b3", 60, -40], ["#b4", -50, -60], ["#b5", -70, 50]].forEach(([s, dx, dy]) => {{
        tl.fromTo(s, {{ x: 0, y: 0 }}, {{ x: dx, y: dy, duration: 6, ease: "sine.inOut" }}, 10);
      }});
      tl.fromTo("#th-halo", {{ scale: 0.85, opacity: 0.7 }}, {{ scale: 1.1, opacity: 1, duration: 0.5, ease: "sine.inOut", repeat: 11, yoyo: true }}, 10);
      tl.fromTo("#th-cross", {{ scale: 1.8, opacity: 0, transformOrigin: "{hx}px {hy}px" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "power4.out" }}, 10.6);
      // occupancies: each world lands slightly large and settles
      ["home", "shop", "rest", "ind"].forEach((k, i) => {{
        tl.fromTo("#occ-art-" + k, {{ scale: 1.08, transformOrigin: "50% 70%" }}, {{ scale: 1, duration: i < 3 ? 0.4 : 0.8, ease: "power3.out" }}, 16 + i * 0.4);
      }});
      // prevent: the spray flows and the mist rolls
      tl.fromTo(".drop", {{ strokeDashoffset: 0 }}, {{ strokeDashoffset: -900, duration: 1.6, ease: "none" }}, 19);
      tl.fromTo("#m1", {{ x: 0, y: 0, scale: 0.9 }}, {{ x: -120, y: 80, scale: 1.15, duration: 1.6, ease: "none" }}, 19);
      tl.fromTo("#m2", {{ x: 0, y: 0 }}, {{ x: 100, y: -60, duration: 1.6, ease: "none" }}, 19);
      // claim: light turns slowly, the check is drawn
      tl.fromTo("#claim-rays", {{ rotation: 0 }}, {{ rotation: 18, duration: 2.9, ease: "none" }}, 20.6);
      tl.fromTo("#claim-check", {{ strokeDashoffset: 110 }}, {{ strokeDashoffset: 0, duration: 0.5, ease: "power3.out" }}, 21.0);
      window.__timelines["bg"] = tl;
    }})();
  </script>
</template>
'''
open(OUT, 'w').write(html)
print('ok')
