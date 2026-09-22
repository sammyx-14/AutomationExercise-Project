from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    """The /product_details/... page — reached via 'View Product', its own URL and page load."""

    def __init__(self, page):
        super().__init__(page)

    def _details(self):
        return self.page.locator("div.product-information")

    def get_name(self):
        return self._details().get_by_role("heading").inner_text()

    def get_price(self):
        return self._details().get_by_text("Rs.").first.inner_text()

    def get_category(self):
        return self._details().get_by_text("Category:").inner_text()

    def get_availability(self):
        return self._details().locator("p", has_text="Availability:").inner_text()

    def get_brand(self):
        return self._details().locator("p", has_text="Brand:").inner_text()