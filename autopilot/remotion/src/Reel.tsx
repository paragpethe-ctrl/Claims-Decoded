import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { z } from "zod";

export const reelSchema = z.object({
  kicker: z.string(),
  title: z.string(),
  subtitle: z.string(),
});

export const Reel: React.FC<z.infer<typeof reelSchema>> = ({
  kicker,
  title,
  subtitle,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleIn = spring({ frame, fps, config: { damping: 200 } });
  const subIn = spring({ frame: frame - 15, fps, config: { damping: 200 } });
  const barWidth = interpolate(frame, [0, 30], [0, 240], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, #120a05 0%, #2b0f04 60%, #5a1a06 100%)",
        justifyContent: "center",
        padding: 90,
        fontFamily: "Inter, Helvetica, Arial, sans-serif",
        color: "white",
      }}
    >
      <div
        style={{
          fontSize: 40,
          letterSpacing: 8,
          fontWeight: 700,
          color: "#ff7a1a",
          opacity: titleIn,
        }}
      >
        {kicker}
      </div>
      <div
        style={{
          height: 10,
          width: barWidth,
          background: "#ff7a1a",
          margin: "28px 0 40px",
          borderRadius: 5,
        }}
      />
      <div
        style={{
          fontSize: 110,
          fontWeight: 800,
          lineHeight: 1.05,
          opacity: titleIn,
          transform: `translateY(${(1 - titleIn) * 60}px)`,
        }}
      >
        {title}
      </div>
      <div
        style={{
          fontSize: 52,
          marginTop: 40,
          color: "#ffd9bf",
          opacity: subIn,
          transform: `translateY(${(1 - subIn) * 40}px)`,
        }}
      >
        {subtitle}
      </div>
    </AbsoluteFill>
  );
};
