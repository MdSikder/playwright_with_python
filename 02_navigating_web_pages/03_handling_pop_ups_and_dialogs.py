# Handling Pop-Ups and Dialogs
# Alerts, Confirms, and Prompts
# Playwright provides methods to handle dialogs like alerts and confirms.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")  # Replace with a suitable test page

    # Handle dialog events
    page.on("dialog", lambda dialog: print(f"Dialog Message: {dialog.message}"))

    # Accepting an alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.evaluate("alert('This is an alert!')")

    # Dismissing a confirm
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.evaluate("confirm('Do you want to proceed?')")

    # Accepting a prompt and providing input
    page.on("dialog", lambda dialog: dialog.accept("Hello Playwright!"))
    page.evaluate("prompt('Enter your name:', 'Default Value')")

    browser.close()


