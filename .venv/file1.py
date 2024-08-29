from playwright.sync_api import sync_playwright

    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://192.168.1.21/")
    page.screenshot(path="screen2.png")
    browser.close()