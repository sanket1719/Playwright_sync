# test_login.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for non-UI testing
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login_with_valid_credentials(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter Username
    page.locator('//input[@name="username"]').fill("Admin")

    # Enter Password
    page.locator('//input[@type="password"]').fill("admin123")

    # Click Login Button
    page.locator('//button[@type="submit"]').click()

    # Wait for the dashboard to load
    page.wait_for_timeout(3000)  

    # Verify successful login
    page_title = page.title()
    assert "OrangeHRM" in page_title, f"Expected 'OrangeHRM' in title, but got '{page_title}'"

def test_login_with_invalid_username(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter Invalid Username
    page.locator('//input[@name="username"]').fill("InvalidUser")

    # Enter Valid Password
    page.locator('//input[@type="password"]').fill("admin123")

    # Click Login Button
    page.locator('//button[@type="submit"]').click()

    # Wait for the error message to appear
    page.wait_for_timeout(3000)  

    # Verify error message
    error_message = page.locator('text=Invalid credentials').text_content()
    assert error_message == "Invalid credentials", "Error message not displayed correctly."

def test_login_with_invalid_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter Valid Username
    page.locator('//input[@name="username"]').fill("Admin")

    # Enter Invalid Password
    page.locator('//input[@type="password"]').fill("InvalidPassword")

    # Click Login Button
    page.locator('//button[@type="submit"]').click()

    # Wait for the error message to appear
    page.wait_for_timeout(3000) 

    # Verify error message
    error_message = page.locator('text=Invalid credentials').text_content()
    assert error_message == "Invalid credentials", "Error message not displayed correctly."

def test_login_with_empty_fields(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Leave fields empty
    page.locator('//input[@name="username"]').fill("")
    page.locator('//input[@type="password"]').fill("")

    # Click Login Button
    page.locator('//button[@type="submit"]').click()

    # Wait for the error message to appear
    error_message_locator = page.locator('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span')
    page.wait_for_timeout(3000)

    # Verify error message
    error_message = error_message_locator.text_content()
    assert error_message == "Required", "Error message not displayed correctly for empty fields."

def test_login_with_different_roles(page):
    users = [
        {"username": "Admin", "password": "admin123"},
        # Add more user roles if applicable
    ]

    for user in users:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Enter Username and Password
        page.locator('//input[@name="username"]').fill(user["username"])
        page.locator('//input[@type="password"]').fill(user["password"])

        # Click Login Button
        page.locator('//button[@type="submit"]').click()

        # Wait for the page to load
        page.wait_for_timeout(3000) 

        # Verify successful login
        page_title = page.title()
        assert "OrangeHRM" in page_title, f"Expected 'OrangeHRM' in title for user {user['username']}, but got '{page_title}'"

        # Optionally add more checks based on user role
        # e.g., verify specific elements or sections visible to each role

        # Log out if necessary and prepare for the next user
        page.locator('text=Logout').click()
