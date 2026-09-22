import pytest
from playwright.sync_api import expect

@pytest.mark.product
def test_search_for_product_by_valid_name(product_page):
    product_page.goto("/products")
    product_page.search_product("Blue Top")

    expect(product_page.page.get_by_text("Blue Top").first).to_be_visible()


@pytest.mark.product
def test_view_full_product_detail_page(product_page, product_detail_page):
    product_page.goto("/products")
    product_page.view_product("Blue Top")

    assert product_detail_page.get_name() == "Blue Top"
    assert product_detail_page.get_price() == "Rs. 500"
    assert "Women" in product_detail_page.get_category()
    assert "In Stock" in product_detail_page.get_availability()
    assert "Polo" in product_detail_page.get_brand()  