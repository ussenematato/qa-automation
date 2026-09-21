import json
from pathlib import Path

from pages.login_page import LoginPage


DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "users.json"


def load_users():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def test_valid_login(browser):
    users = load_users()
    login_page = LoginPage(browser).open()

    login_page.login(users["valid_user"]["username"], users["valid_user"]["password"])

    assert "inventory" in browser.current_url.lower()


def test_invalid_login(browser):
    users = load_users()
    login_page = LoginPage(browser).open()

    login_page.login(users["invalid_user"]["username"], users["invalid_user"]["password"])

    assert "Epic sadface" in login_page.error_message()
