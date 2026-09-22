import pytest
from config import TEST_USER_EMAIL, TEST_USER_PASSWORD, TEST_USER_NAME
from pages import login_page
from playwright.sync_api import expect


@pytest.mark.login
def test_successful_login(login_page):
    login_page.goto("/login")
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    expect(login_page.header.logged_in_as_locator(TEST_USER_NAME)).to_be_visible()


@pytest.mark.login
def test_login_fails_with_incorrect_password(login_page):
    login_page.goto("/login")
    login_page.login(TEST_USER_EMAIL, "WrongPassword123")

    assert login_page.is_incorrect_login_credentials_error_visible()


@pytest.mark.login
def test_login_fails_with_unregistered_email(login_page):
    login_page.goto("/login")
    login_page.login("unregistered@example.com", TEST_USER_PASSWORD)

    assert login_page.is_incorrect_login_credentials_error_visible()


@pytest.mark.logout
def test_successful_logout(login_page):
    login_page.goto("/login")
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    assert login_page.header.is_logged_in_as(TEST_USER_NAME)

    login_page.header.logout()
    expect(login_page.header.signup_login_locator()).to_be_visible()