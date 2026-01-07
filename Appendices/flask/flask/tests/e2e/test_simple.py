import re
from playwright.sync_api import Playwright, Page, expect

def test_simple(page: Page):
    page.goto("http://localhost:5001/")
    expect(page).to_have_title(re.compile("Flask Example"))