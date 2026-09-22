from pages.base_page import BasePage


class ProductPage(BasePage):
    """The /products page — search, listing, and add-to-cart from the listing."""

    def __init__(self, page):
        super().__init__(page)

    def search_product(self, product_name):
        self.page.get_by_role("textbox", name="Search Product").fill(product_name)
        self.page.locator("#submit_search").click()

    def _product_card(self, product_name):
        return self.page.locator("div.product-image-wrapper").filter(has_text=product_name)

    def add_to_cart(self, product_name):
        card = self._product_card(product_name)
        card.hover()
        card.locator("div.product-overlay a.add-to-cart").click()


    def view_product(self, product_name):
        self._product_card(product_name).get_by_text("View Product").click()


    def added_to_cart_confirmation_locator(self):
        return self.page.get_by_role("heading", name="Added!")

    def view_cart_from_modal(self):
        self.page.get_by_role("link", name="View Cart").click()
        self.page.wait_for_load_state("networkidle")