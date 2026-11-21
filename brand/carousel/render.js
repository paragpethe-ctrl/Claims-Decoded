// node render.js <html> <outdir> : one 1080x1350 PNG per <section class="slide">
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [html, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(html));
  await page.evaluate(() => document.fonts.ready);
  const slides = await page.$$('section.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(out, String(i + 1).padStart(2, '0') + '.png') });
  }
  await browser.close();
})();
