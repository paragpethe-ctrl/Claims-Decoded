import { Composition } from "remotion";
import { Reel, reelSchema } from "./Reel";

// Vertical 9:16 for Instagram Reels / Shorts / TikTok.
export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Reel"
      component={Reel}
      durationInFrames={150}
      fps={30}
      width={1080}
      height={1920}
      schema={reelSchema}
      defaultProps={{
        kicker: "CLAIMS DECODED",
        title: "Why fire claims get rejected",
        subtitle: "And how to make sure yours doesn't",
      }}
    />
  );
};
