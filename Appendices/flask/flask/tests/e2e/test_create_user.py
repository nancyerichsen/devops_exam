import re
from playwright.sync_api import Page, expect

def test_create_user(page: Page):
    page.goto("http://localhost:5001/")
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Admin Dashboard").click()
    page.locator("input[name=\"id\"]").click()
    page.locator("input[name=\"id\"]").fill("vio")
    page.locator("input[name=\"pw\"]").click()
    page.locator("input[name=\"pw\"]").fill("vio")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Logout").click()
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("vio")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("vio")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Private").click()
    expect(page.get_by_text("Private Page")).to_be_visible()

