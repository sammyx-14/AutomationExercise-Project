import pytest
from playwright.sync_api import expect


@pytest.mark.cart
def test_add_product_to_cart_from_listing(product_page, cart_page):
    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")

    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()
    product_page.view_cart_from_modal()

    expect(cart_page.page.locator("tr").filter(
        has_text="Blue Top")).to_be_visible()
    assert cart_page.get_quantity("Blue Top") == "1"
    assert cart_page.get_total("Blue Top") == "Rs. 500"


@pytest.mark.cart
def test_remove_product_from_cart(product_page, cart_page):
    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()
    product_page.view_cart_from_modal()

    expect(cart_page.page.locator("tr").filter(
        has_text="Blue Top")).to_be_visible()

    cart_page.remove_product("Blue Top")

    expect(cart_page.page.locator("tr").filter(
        has_text="Blue Top")).not_to_be_visible(timeout=10000)


@pytest.mark.cart
def test_cart_quantity_reflects_repeated_add(product_page, cart_page):
    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()

    product_page.goto("/products")
    product_page.add_to_cart("Blue Top")
    expect(product_page.added_to_cart_confirmation_locator()).to_be_visible()

    product_page.view_cart_from_modal()

    assert cart_page.get_quantity("Blue Top") == "2"
    assert cart_page.get_total("Blue Top") == "Rs. 1000"

@pytest.mark.checkout
def test_checkout_blocked_with_empty_cart(cart_page):
    cart_page.goto("/view_cart")

    assert cart_page.is_cart_empty_message_visible()