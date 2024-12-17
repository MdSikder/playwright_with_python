import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("url, expected_title", [
    ("https://rahulshettyacademy.com/locatorspractice/", "Rahul Shetty Academy - Login page"),
    ("https://playwright.dev", "Playwright")
])
def test_multiple_pages(url, expected_title):
    with sync_playwright() as p:  # Start Playwright context
        browser = p.chromium.launch(headless=False)  # Launch browser
        page = browser.new_page()  # Open a new page
        page.goto(url)  # Navigate to the given URL
        assert page.title() == expected_title, f"Title mismatch for URL: {url}"
        browser.close()  # Close browser after test
