import pytest
from playwright.sync_api import sync_playwright, Page

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

def test_registration_form(page: Page):
    page.goto("https://demo.automationtesting.in/Register.html")

    enter_Fname = page.locator('//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')
    enter_Fname.fill("Manish")

    enter_Lname = page.locator('//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')
    enter_Lname.fill("Mane")


    assert enter_Fname.input_value() == "Manish", "First name not filled correctly"
    assert enter_Lname.input_value() == "Mane", "Last name not filled correctly"

def test_address(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")

    enter_address = page.locator('//*[@id="basicBootstrapForm"]/div[2]/div/textarea')
    enter_address.fill("Pune,Maharashtra,India")

    assert enter_address.input_value() == "Pune,Maharashtra,India", "Address is not filled"

def test_email(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")

    enter_email = page.locator('//*[@type="email"]')
    enter_email.fill("manish@gmail.com")

    assert enter_email.input_value() == "manish@gmail.com", "Email is not filled"

def test_phone(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")

    enter_phone = page.locator('//*[@type="tel"]')
    enter_phone.fill("4621348526")

    assert enter_phone.input_value() == "4621348526", "Phone is not filled"

def test_skill(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    skill_selector = page.query_selector('//*[@id="Skills"]')
    skill_selector.select_option(value='Python')

    selected_option = skill_selector.input_value()
    assert selected_option == 'Python', f"Expected 'Python', but got {selected_option}"

def test_year(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    year_selector = page.query_selector('//*[@id="yearbox"]')
    year_selector.select_option(value='2002')

    selected_option = year_selector.input_value()
    assert selected_option == '2002', f"Expected '2002', but got {selected_option}"

def test_month(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    month_selector = page.query_selector('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
    month_selector.select_option(value='October')

    selected_option = month_selector.input_value()
    assert selected_option == 'October', f"Expected 'October', but got {selected_option}"

def test_day(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    day_selector = page.query_selector('//*[@id="daybox"]')
    day_selector.select_option(value='17')

    selected_option = day_selector.input_value()
    assert selected_option == '17',f"Expected '17', but got {selected_option}"

def test_language(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    languages = ["English", "Hindi"]
    page.locator('//*[@id="msdd"]').click()

    for language in languages:
        page.locator(f'//li/a[text()="{language}"]').click()

    selected_elements = page.locator('//div[@class="ui-autocomplete-multiselect-item"]')
    selected_texts = selected_elements.all_text_contents()

    assert sorted(selected_texts) == sorted(languages), f"Expected {languages}, but got {selected_texts}"

def test_gender(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")

    male_radio_button = page.locator('input[value="Male"]')
    male_radio_button.click()

    is_checked = page.locator('input[value="Male"]').is_checked()
    assert is_checked, "The 'Male' radio button was not selected."



def test_skill(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    skill_selector = page.query_selector('//*[@id="Skills"]')
    skill_selector.select_option(value='Python')

    selected_skill = skill_selector.input_value()

    assert selected_skill == 'Python', f"Expected {skill_selector}, but got {selected_skill}"

def test_country(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    page.locator("span[role='combobox']").click()
    page.locator("li[role='treeitem']", has_text="India").click()

    selected_country = page.locator("span[role='combobox']").text_content()

    assert selected_country == 'India', f"Expected 'India', but got {selected_country}"

def test_password(page: page):
    page.goto("https://demo.automationtesting.in/Register.html")
    password = page.locator('//*[@id="firstpassword"]')
    password.fill('Asdf@1943')

    entered_password = password.input_value()

    assert entered_password == 'Asdf@1943', f"Expected 'Asdf@1943', but got {entered_password}"


