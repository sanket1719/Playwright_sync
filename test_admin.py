# test_orangehrm.py
import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login_and_search_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    # Login
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()


    # Navigate to Admin
    page.get_by_role("link", name="Admin").click()

    # Perform search
    page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').fill("rms")
    page.get_by_role("button", name="Search").click()

    # Validate search results
    error_message = page.wait_for_selector('//*[@id="oxd-toaster_1"]')
    assert error_message, "Invalid Output"


