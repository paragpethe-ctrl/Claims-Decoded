# Claims Decoded — Remotion

Remotion video pipeline for Claims Decoded reels (1080×1920, 30 fps).

## Commands

```bash
npm install
npm run dev     # Remotion Studio (live preview)
npm run build   # render the `Reel` composition to out/reel.mp4
npm run still   # render a single frame to out/reel.png
npm run lint    # type-check
```

Override props at render time:

```bash
npx remotion render Reel out/custom.mp4 --props='{"kicker":"CLAIMS DECODED","title":"Your title","subtitle":"Your subtitle"}'
```

## Structure

- `src/index.ts` — registers the root
- `src/Root.tsx` — composition definitions (id, size, fps, duration, default props)
- `src/Reel.tsx` — starter title-card reel with a zod props schema
- `remotion.config.ts` — render config; uses `/opt/pw-browsers/chromium` or
  `$REMOTION_BROWSER_EXECUTABLE` if present, otherwise Remotion downloads its own browser
