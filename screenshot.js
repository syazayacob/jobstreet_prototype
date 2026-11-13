
const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: true
    });

    const page = await browser.newPage({
        viewport: {
            width: 1440,
            height: 900
        }
    });

    await page.goto('https://miniature-space-sniffle-7qpww6p6gpq2wrxp-8501.app.github.dev/');

    // Wait for Streamlit to finish rendering
    await page.waitForTimeout(3000);

    await page.screenshot({
        path: 'application_dashboard.png',
        fullPage: true
    });

    await browser.close();
})();
