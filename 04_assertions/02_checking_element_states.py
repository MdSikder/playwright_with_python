from urllib.response import addbase

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/locatorspractice/", wait_until="networkidle")

    # Check if an element is visible
    assert page.is_visible("//h1[normalize-space()='Sign in']"), "Sign In not Visible"

    # Check if an element contains specific text
    assert page.text_content("//h1[normalize-space()='Sign in']") == "Sign in", "Sign In text was not found"

    # Check if an element is enabled
    assert page.is_disabled("//button[normalize-space()='Sign In']"), "Submit button is not disabled"




