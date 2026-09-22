from pages.base_page import BasePage


class CartPage(BasePage):
    """The /view_cart page — cart contents, quantity, removal, and checkout entry point."""

    def __init__(self, page):
        super().__init__(page)

    def _product_row(self, product_name):
        return self.page.locator("tr").filter(has_text=product_name)

    def get_quantity(self, product_name):
        return self._product_row(product_name).locator(".cart_quantity").inner_text()

    def get_total(self, product_name):
        return self._product_row(product_name).locator(".cart_total_price").inner_text()

    def remove_product(self, product_name):
        self._product_row(product_name).locator(
            ".cart_quantity_delete").click()

    def proceed_to_checkout(self):
        self.page.get_by_text("Proceed To Checkout").click()

    def is_cart_empty_message_visible(self):
        return self.page.locator("#empty_cart").is_visible()
