from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # Timeout: Customize navigation timeout (default is 30 seconds).
    page.goto("https://rahulshettyacademy.com/locatorspractice/", timeout=60000)

    # Wait Until: Wait for events like load, domcontentloaded, or networkidle.
    page.goto("https://rahulshettyacademy.com/locatorspractice/", wait_until="networkidle")  #Opens the website and waits for network activity to finish.

