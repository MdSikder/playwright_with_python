import time # import time: This is a built-in Python module that allows you to introduce pauses using time.sleep() (useful for demonstration purposes).

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/locatorspractice/")
    time.sleep(1)
    page.reload()
    time.sleep(1)
    page.go_back()
    time.sleep(1)
    page.go_forward()
    time.sleep(1)

