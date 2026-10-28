const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, 'html');
const pdfDir = path.join(__dirname, 'pdf');
const pngDir = path.join(__dirname, 'png');
fs.mkdirSync(pdfDir, { recursive: true });
fs.mkdirSync(pngDir, { recursive: true });

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  for (const f of fs.readdirSync(dir).filter(n => n.endsWith('.html'))) {
    await page.goto('file://' + path.join(dir, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const report = await page.evaluate(() => {
      const fontsOk = document.fonts.check('16px "Cormorant Garamond"') && document.fonts.check('16px Jost');
      const over = [...document.querySelectorAll('.page')].map((p, i) => {
        const foot = p.querySelector('.foot').getBoundingClientRect();
        const pr = p.getBoundingClientRect();
        return { page: i + 1, spare: Math.round(pr.bottom - foot.bottom) };
      });
      return { fontsOk, over };
    });
    console.log(f, JSON.stringify(report));
    const base = f.replace('.html', '');
    await page.pdf({ path: path.join(pdfDir, base + '.pdf'), format: 'Letter', printBackground: true, preferCSSPageSize: true });
    const pages = await page.$$('.page');
    for (let i = 0; i < pages.length; i++) {
      await pages[i].screenshot({ path: path.join(pngDir, `${base}-${i + 1}.png`) });
    }
  }
  await browser.close();
})();
