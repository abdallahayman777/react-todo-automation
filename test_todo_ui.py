import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_login_valid(page):
    page.goto("http://localhost:3000")
    # This app doesn't have login by default. Simulate if needed:
    assert "Todo List" in page.title()


def test_create_new_todo(page):
    page.goto("http://localhost:3000")
    page.fill('input[name="text"]', "Test Todo Item")
    page.click('button[type="submit"]')
    assert page.is_visible("text=Test Todo Item")


def test_edit_todo(page):
    page.goto("http://localhost:3000")
    page.fill('input[name="text"]', "Editable Todo")
    page.click('button[type="submit"]')
    page.click("text=Editable Todo")
    page.fill('input[name="text"]', "Edited Todo")
    page.click('button[type="submit"]')
    assert page.is_visible("text=Edited Todo")


def test_delete_todo(page):
    page.goto("http://localhost:3000")
    page.fill('input[name="text"]', "Delete Me")
    page.click('button[type="submit"]')

    # Click the X/delete button — depends on how the app renders it
    # Adjust selector if necessary:
    page.click("button:has-text('X')")  # Update this if not correct

    assert not page.is_visible("text=Delete Me")
