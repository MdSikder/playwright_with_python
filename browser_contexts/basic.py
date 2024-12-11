from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launch the Chromium browser
    browser = p.chromium.launch(headless=False)

    # Create two different browser contexts (for two different users)
    context_user1 = browser.new_context()
    context_user2 = browser.new_context()


    # Create two pages for the two users
    page_user1 = context_user1.new_page()
    page_user2 = context_user2.new_page()


    # User 1 logs in
    page_user1.goto("https://rahulshettyacademy.com/locatorspractice/")
    page_user1.fill("//input[@id='inputUsername']", "user1")
    page_user1.fill("//input[@placeholder='Password']", "admin")
    page_user1.click("//button[normalize-space()='Sign In']")
    time.sleep(2)


    # User 2 logs in
    page_user2.goto("https://rahulshettyacademy.com/locatorspractice/")
    page_user2.fill("//input[@id='inputUsername']", "user2")
    page_user2.fill("//input[@placeholder='Password']", "admin")
    page_user2.click("//button[normalize-space()='Sign In']")
    time.sleep(2)

    # Print the titles of the two pages to confirm
    # Print the titles of the two pages to confirm
    print("User 1's Page Title: ", page_user1.title())
    print("User 2's Page Title: ", page_user2.title())

    browser.close()