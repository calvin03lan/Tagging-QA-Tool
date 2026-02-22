import os
from playwright.sync_api import sync_playwright

# Example: Discovering buttons and other elements on a page

with sync_playwright() as p:
    # Use headless=False to see the browser action
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to page and wait for it to fully load
    url = 'https://uat-cms.hangseng.com/cms/emkt/pmo/grp01/p61/chi/index.html'
    print(f"Navigating to {url}...")
    page.goto(url)
    page.wait_for_load_state('networkidle')

    # Prepare output content
    output_content = [f"# Page Element Discovery Report\n\nTarget URL: {url}\n"]

    # Discover all buttons on the page
    buttons = page.locator('button').all()
    print(f"Found {len(buttons)} buttons:")
    output_content.append(f"## Buttons ({len(buttons)})\n")
    for i, button in enumerate(buttons):
        text = button.inner_text().strip() if button.is_visible() else "[hidden]"
        print(f"  [{i}] {text}")
        output_content.append(f"- **Button {i}**: {text}")
    
    # Also look for elements that look like buttons (e.g. div/span with role=button or specific classes if needed)
    # For now, let's stick to <button> tag as requested, but often links act as buttons.

    # Discover links
    links = page.locator('a[href]').all()
    print(f"\nFound {len(links)} links:")
    output_content.append(f"\n## Links ({len(links)})\n")
    for i, link in enumerate(links):
        text = link.inner_text().strip()
        href = link.get_attribute('href')
        # Print to console (limit first 5 to avoid spam, but file gets all)
        if i < 5:
            print(f"  - {text} -> {href}")
        output_content.append(f"- [{text}]({href})")

    # Discover input fields
    inputs = page.locator('input, textarea, select').all()
    print(f"\nFound {len(inputs)} input fields:")
    output_content.append(f"\n## Input Fields ({len(inputs)})\n")
    for input_elem in inputs:
        name = input_elem.get_attribute('name') or input_elem.get_attribute('id') or "[unnamed]"
        input_type = input_elem.get_attribute('type') or 'text'
        print(f"  - {name} ({input_type})")
        output_content.append(f"- Type: `{input_type}`, Name/ID: `{name}`")

    # Save to MD file
    output_md_file = 'element_report.md'
    with open(output_md_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_content))
    print(f"\nReport saved to {os.path.abspath(output_md_file)}")

    # Take screenshot for visual reference
    output_image = 'page_discovery.png'
    page.screenshot(path=output_image, full_page=True)
    print(f"Screenshot saved to {os.path.abspath(output_image)}")

    browser.close()