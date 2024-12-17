import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/locatorspractice/", wait_until="networkidle")
    print("page title:",page.title())
    page.fill("//input[@id='inputUsername']", "") # Clearing Input Fields
    page.fill("//input[@id='inputUsername']", "user") # Enters the new value
    page.fill("//input[@placeholder='Password']", "") # Clearing Input Fields
    page.fill("//input[@placeholder='Password']", "admin") # Enters the new value
    page.click("//button[normalize-space()='Sign In']")
    browser.close()
