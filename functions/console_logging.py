from playwright.sync_api import sync_playwright

# Example: Capturing console logs during browser automation

url = 'https://uat-cms.hangseng.com/cms/emkt/pmo/grp01/p61/chi/index.html'  # Changed to Playwright docs which is bot-friendly

console_logs = []

with sync_playwright() as p:
    # Use headless=True. If you face issues, try headless=False
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    # Set up console log capture
    def handle_console_message(msg):
        console_logs.append(f"[{msg.type}] {msg.text}")
        print(f"Console: [{msg.type}] {msg.text}")

    page.on("console", handle_console_message)

    # Navigate to page
    print(f"Navigating to {url}...")
    page.goto(url)
    page.wait_for_load_state('networkidle')

    # Manually trigger a console log to ensure we capture something
    page.evaluate("console.log('Hello from Playwright Automation!');")
    page.evaluate("console.warn('This is a test warning');")

    # Interact with the page
    try:
        # Click the "Get started" button
        page.click('text=Get started') 
    except:
        print("Could not click button, skipping...")
        
    page.wait_for_timeout(1000)

    browser.close()

# Save console logs to file
import os
output_file = 'console.log'
with open(output_file, 'w') as f:
    f.write('\n'.join(console_logs))

print(f"\nCaptured {len(console_logs)} console messages")
print(f"Logs saved to: {os.path.abspath(output_file)}")