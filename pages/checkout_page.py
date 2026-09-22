from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """The checkout flow — guest-blocking prompt and the address review step."""

    def __init__(self, page):
        super().__init__(page)

    def is_register_login_prompt_visible(self):
        return self.page.get_by_text("Register / Login account to proceed on checkout.").is_visible()

    def is_address_details_visible(self):
        return self.page.get_by_role("heading", name="Address Details").is_visible()

    def place_order(self):
        self.page.get_by_role("link", name="Place Order").click()