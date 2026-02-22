from playwright.sync_api import sync_playwright
import os

# Example: Automating interaction with static HTML files using file:// URLs

html_file_path = os.path.abspath('test_form.html')
file_url = f'file://{html_file_path}'

with sync_playwright() as p:
    # Use headless=False to visualize the automation
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    # Navigate to local HTML file
    print(f"Opening local file: {file_url}")
    page.goto(file_url)

    # Take screenshot
    output_before = 'static_page_before.png'
    page.screenshot(path=output_before, full_page=True)
    print(f"Screenshot saved to {os.path.abspath(output_before)}")

    # Interact with elements
    print("Filling form...")
    page.fill('#name', 'Trae Assistant')
    page.fill('#email', 'trae@example.com')
    
    # Click "Click Me" button
    print("Clicking 'Click Me'...")
    page.click('#click-me-btn')
    page.wait_for_timeout(1000) # Wait for animation/js

    # Submit form (Click Submit button)
    print("Clicking 'Submit Form'...")
    page.click('#submit-btn')
    page.wait_for_timeout(1000)

    # Take final screenshot
    output_after = 'static_page_after.png'
    page.screenshot(path=output_after, full_page=True)
    print(f"Final screenshot saved to {os.path.abspath(output_after)}")

    browser.close()

print("Static HTML automation completed!")