const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'content-strategy.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: path.join(__dirname, 'Feminine_Gut_Content_Strategy.pdf'), format: 'Letter', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:7px;letter-spacing:2px;color:#7A6D5B;font-family:Arial;padding:0 0.65in;display:flex;justify-content:space-between"><span>THE FEMININE GUT · CONTENT STRATEGY</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  });
  await b.close();
})();
