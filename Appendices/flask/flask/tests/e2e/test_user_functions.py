import re
from playwright.sync_api import Page, expect

def test_add_note(page: Page):
    page.goto("http://localhost:5001/")
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("adam")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("hazel")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Private").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("This is a new note!")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("This is a new note!")).to_be_visible()