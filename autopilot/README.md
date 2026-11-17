# Instagram autopilot (switched off)

From [Ootto-AI/claude-instagram-autopilot](https://github.com/Ootto-AI/claude-instagram-autopilot) (MIT, see `LICENSE`), set up for Fire Claims Decoded.

| Part | Where | Status |
|---|---|---|
| Brand settings | `autopilot/config.yml` | Filled in. CTA keyword and deliverable still to set. |
| Reel renderer (Remotion, 9:16) | `autopilot/remotion/` | Ready to use by hand. |
| Daily draft job | `.github/workflows/autopilot.yml` | **Off.** No schedule; manual start only; never posts. |

## Render a reel by hand (free)
```bash
cd autopilot/remotion
npm install
npm run studio     # preview in the browser
npm run render     # -> out/reel.mp4 from sample-carousel.json
```
Colours are the tokens at the top of `remotion/src/Reel.tsx`.

## Switch the job on later
1. Add repo Secrets: `ANTHROPIC_API_KEY` (paid per use), `COMPOSIO_API_KEY`, `IG_BUSINESS_ACCOUNT_ID`.
2. Set `cta.keyword` and `cta.deliverable` in `config.yml`.
3. Run it once by hand from the Actions tab and review the draft in `autopilot/drafts/`.
4. Uncomment the `schedule:` lines in the workflow.
