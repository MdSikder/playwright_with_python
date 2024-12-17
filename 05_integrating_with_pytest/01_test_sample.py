from playwright.sync_api import sync_playwright

def test_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/locatorspractice/")

        assert page.title() == "Rahul Shetty Academy - Login page", "Title does not match!"

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/locatorspractice/")
        page.fill("//input[@id='inputUsername']", "admin")
        page.fill("//input[@placeholder='Password']", "rahulshettyacademy")
        page.click("//button[normalize-space()='Sign In']")
        assert page.title() == "Rahul Shetty Academy - Login page", "Title does not match!"