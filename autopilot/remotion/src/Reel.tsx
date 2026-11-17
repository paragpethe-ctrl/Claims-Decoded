import React from "react";
import { AbsoluteFill, Series, useCurrentFrame, useVideoConfig, spring, interpolate } from "remotion";

// ---- brand tokens: Fire Claims Decoded engineering blueprint ----
// Same palette as reels/claims-decoded-explainer. Contrast (WCAG):
// INK on BG 6.2:1 · ORANGE on BG 3.15:1 (large/bold text only) · ORANGE on CARD 5.2:1 · INK2 on CARD 6.8:1
const BG = "#1F5F99";      // blueprint blue
const BG_DEEP = "#174D7E"; // vignette edge
const CARD = "#123E66";    // panels
const INK = "#F2F7FC";     // main text and line work
const INK2 = "#B8CDE2";    // secondary text
const ORANGE = "#FF9A3C";  // accent (fire)
const SERIES = "FIRE CLAIMS DECODED";
const HEAD = "Oswald, 'Arial Narrow', sans-serif";
const SANS = "Roboto, Arial, sans-serif";

type Slide = {
  kind: "hook" | "tool" | "cta";
  n?: number; tag?: string; headline?: string; emphasis?: string; body?: string; important?: boolean;
};
export type ReelProps = { slides: Slide[]; handle?: string };

const Word: React.FC<{ delay: number; children: React.ReactNode }> = ({ delay, children }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 13, stiffness: 200, mass: 0.7 } });
  return <span style={{ display: "inline-block", opacity: s, transform: `translateY(${interpolate(s, [0, 1], [26, 0])}px)` }}>{children}</span>;
};

const Chrome: React.FC<{ handle: string; children: React.ReactNode }> = ({ handle, children }) => (
  <AbsoluteFill style={{ background: `radial-gradient(120% 100% at 50% 35%, ${BG} 55%, ${BG_DEEP} 100%)`, fontFamily: SANS, overflow: "hidden" }}>
    {/* blueprint grid: fine 40px lines, heavier every 200px */}
    <AbsoluteFill style={{
      backgroundImage: `linear-gradient(${INK}14 1px, transparent 1px), linear-gradient(90deg, ${INK}14 1px, transparent 1px),
        linear-gradient(${INK}2e 2px, transparent 2px), linear-gradient(90deg, ${INK}2e 2px, transparent 2px)`,
      backgroundSize: "40px 40px, 40px 40px, 200px 200px, 200px 200px",
    }} />
    {/* drawing border */}
    <div style={{ position: "absolute", inset: 40, border: `2px dashed ${INK}66` }} />
    <div style={{ position: "absolute", top: 120, left: 0, right: 0, textAlign: "center", color: INK, fontFamily: HEAD, fontWeight: 700, fontSize: 40, letterSpacing: 6 }}>{SERIES}</div>
    {children}
    <div style={{ position: "absolute", bottom: 90, left: 96, color: INK2, fontFamily: HEAD, fontWeight: 500, fontSize: 32, letterSpacing: 3, textTransform: "uppercase" }}>{handle}</div>
  </AbsoluteFill>
);

const HookScene: React.FC<{ s: Slide; handle: string }> = ({ s, handle }) => {
  const words = (s.headline || s.emphasis || "Your hook here").split(" ");
  return (<Chrome handle={handle}>
    {s.tag ? <div style={{ position: "absolute", top: 300, left: 0, right: 0, textAlign: "center", color: ORANGE, fontFamily: HEAD, fontWeight: 700, letterSpacing: 4, fontSize: 40 }}>{s.tag}</div> : null}
    <div style={{ position: "absolute", top: 700, left: 60, right: 60, textAlign: "center", display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "0 18px", fontFamily: HEAD, fontWeight: 700, fontSize: 104, color: INK, letterSpacing: 0, lineHeight: 1.1, textTransform: "uppercase" }}>
      {words.map((w, i) => <Word key={i} delay={4 + i * 3}>{w}</Word>)}
    </div>
  </Chrome>);
};

const ToolScene: React.FC<{ s: Slide; handle: string }> = ({ s, handle }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const A = ORANGE;
  const pop = spring({ frame: frame - 4, fps, config: { damping: 12, stiffness: 180, mass: 0.8 } });
  return (<Chrome handle={handle}>
    <div style={{ position: "absolute", top: 620, left: 110, right: 110, transform: `translateY(${interpolate(pop, [0, 1], [24, 0])}px) scale(${interpolate(pop, [0, 1], [0.9, 1])})` }}>
      {s.important ? <div style={{ textAlign: "center", marginBottom: 24 }}><span style={{ background: ORANGE, color: CARD, fontFamily: HEAD, fontWeight: 700, fontSize: 32, letterSpacing: 2, padding: "10px 26px", borderRadius: 6 }}>⚠ MOST IMPORTANT</span></div> : null}
      <div style={{ background: CARD, border: s.important ? `3px solid ${A}` : `2px dashed ${INK}99`, borderRadius: 8, padding: "40px 44px" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
          <div style={{ width: 84, height: 84, borderRadius: 6, background: "transparent", border: `3px solid ${A}`, color: A, fontFamily: HEAD, fontWeight: 700, fontSize: 50, display: "flex", alignItems: "center", justifyContent: "center", flex: "0 0 auto" }}>{s.n ?? 1}</div>
          <div style={{ color: INK, fontFamily: HEAD, fontWeight: 600, fontSize: 52, lineHeight: 1.15 }}>{s.headline}{s.emphasis ? <span style={{ color: A }}> {s.emphasis}</span> : null}</div>
        </div>
        {s.body ? <div style={{ color: INK2, fontSize: 32, marginTop: 24, lineHeight: 1.3 }}>{s.body}</div> : null}
      </div>
    </div>
  </Chrome>);
};

const CtaScene: React.FC<{ s: Slide; handle: string }> = ({ s, handle }) => {
  const kw = (s.emphasis || "FOLLOW").toUpperCase();
  return (<Chrome handle={handle}>
    <div style={{ position: "absolute", top: 760, left: 60, right: 60, textAlign: "center" }}>
      <div style={{ fontFamily: HEAD, fontWeight: 700, fontSize: 84, color: INK, textTransform: "uppercase" }}>Comment <span style={{ color: ORANGE }}>"{kw}"</span></div>
      <div style={{ color: INK, fontSize: 38, marginTop: 16 }}>{s.body || "and I'll DM you the setup"}</div>
      <div style={{ marginTop: 50, display: "inline-flex", alignItems: "center", gap: 16, background: CARD, border: `3px solid ${ORANGE}`, borderRadius: 8, padding: "20px 30px" }}>
        <span style={{ color: INK, fontWeight: 700, fontSize: 38 }}>{kw}</span>
        <span style={{ background: ORANGE, color: CARD, fontFamily: HEAD, fontWeight: 700, fontSize: 32, padding: "12px 28px", borderRadius: 6 }}>Post</span>
      </div>
    </div>
  </Chrome>);
};

export const Reel: React.FC<ReelProps> = ({ slides = [], handle = "@parag_pethe1" }) => {
  const { fps } = useVideoConfig();
  const per = Math.round(3.4 * fps);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Series>
        {slides.map((s, i) => (
          <Series.Sequence key={i} durationInFrames={per}>
            {s.kind === "hook" ? <HookScene s={s} handle={handle} />
              : s.kind === "cta" ? <CtaScene s={s} handle={handle} />
                : <ToolScene s={s} handle={handle} />}
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};
