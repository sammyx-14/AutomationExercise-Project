import time

import pytest
from playwright.sync_api import expect

from config import TEST_USER_EMAIL


@pytest.mark.registration
def test_successful_registration(login_page, registration_page):
    unique_email = f"testuser{int(time.time())}@example.com"

    login_page.goto("/login")
    login_page.start_signup("Test User", unique_email)

    registration_page.fill_account_information("Mr.", "Password123", "10", "6", "1997")
    registration_page.fill_address_information(
        "Test", "User", "123 Test Street", "United States", "Ohio", "Columbus", "43004", "1234567890"
    )
    registration_page.create_account()

    expect(registration_page.account_created_locator()).to_be_visible()
    registration_page.continue_after_signup()

    expect(login_page.header.logged_in_as_locator("Test User")).to_be_visible()

    login_page.header.delete_account()
    expect(login_page.header.account_deleted_locator()).to_be_visible()


@pytest.mark.registration
def test_registration_fails_with_existing_email(login_page):
    login_page.goto("/login")
    login_page.start_signup("Existing User", TEST_USER_EMAIL)

    expect(login_page.email_already_exists_locator()).to_be_visible()