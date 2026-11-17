import { Config } from "@remotion/cli/config";
import fs from "fs";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);

// Use a pre-installed Chromium if one is available (e.g. sandboxed/cloud
// environments that can't download Remotion's headless shell). Override with
// REMOTION_BROWSER_EXECUTABLE; otherwise Remotion downloads its own browser.
const browser =
  process.env.REMOTION_BROWSER_EXECUTABLE ??
  (fs.existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : null);
if (browser) {
  Config.setBrowserExecutable(browser);
}
