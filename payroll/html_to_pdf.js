// Convert every .html file in a folder to a Letter-size PDF next to it.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = process.argv[2];
  const b = await chromium.launch(); const pg = await b.newPage();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    await pg.goto('file://' + path.resolve(dir, f));
    await pg.pdf({ path: path.join(dir, f.replace(/\.html$/, '.pdf')), format: 'Letter', printBackground: true });
  }
  await b.close();
})();
