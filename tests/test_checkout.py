import pytest
from playwright.sync_api import expect
from config import TEST_USER_EMAIL, TEST_USER_PASSWORD, TEST_USER_NAME


@pytest.mark.checkout
def test_guest_cannot_complete_checkout(product_page, cart_page, checkout_page):
    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()
    product_page.view_cart_from_modal()

    cart_page.proceed_to_checkout()

    assert checkout_page.is_register_login_prompt_visible()


@pytest.mark.checkout
def test_place_order_login_before_checkout(login_page, product_page, cart_page, checkout_page, payment_page):
    login_page.goto("/login")
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect(login_page.header.logged_in_as_locator(
        TEST_USER_NAME)).to_be_visible()

    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()
    product_page.view_cart_from_modal()

    cart_page.proceed_to_checkout()
    expect(checkout_page.page.get_by_role(
        "heading", name="Address Details")).to_be_visible()

    checkout_page.place_order()

    payment_page.fill_card_details(
        "Test User", "4111111111111111", "123", "12", "2027")
    payment_page.pay_and_confirm_order()

    expect(payment_page.order_confirmed_locator()).to_be_visible()


@pytest.mark.payment
def test_order_blocked_with_empty_cvc(login_page, product_page, cart_page, checkout_page, payment_page):
    login_page.goto("/login")
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    expect(login_page.header.logged_in_as_locator(
        TEST_USER_NAME)).to_be_visible()

    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()
    product_page.view_cart_from_modal()

    cart_page.proceed_to_checkout()
    expect(checkout_page.page.get_by_role(
        "heading", name="Address Details")).to_be_visible()

    checkout_page.place_order()

    payment_page.fill_card_details(
        "Test User", "4111111111111111", "", "12", "2027")
    payment_page.pay_and_confirm_order()

    assert payment_page.get_field_validation_message("cvc") != ""
