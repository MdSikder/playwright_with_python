# Step 1: Import the synchronous version of Playwright's API.
# This enables blocking (step-by-step) control of browsers.
from playwright.sync_api import sync_playwright

# Step 2: Use a `with` statement to initialize and manage the Playwright instance.
# This ensures proper cleanup of resources after usage.
with sync_playwright() as p:
    # Step 3: Launch a Chromium browser instance in non-headless mode.
    # The `headless=False` argument makes the browser visible.
    browser = p.chromium.launch(headless=False)

    # Step 4: Create a new browser page (tab) instance.
    page = browser.new_page()

    # Step 5: Navigate to the specified URL.
    # Here, we open Google's homepage.
    page.goto("https://www.google.com/")

    # Step 6: Retrieve and print the page's title to verify navigation.
    print(page.title())

    # Step 7: Close the browser to free up resources.
    browser.close()
