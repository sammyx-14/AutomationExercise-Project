from pages.base_page import BasePage


class PaymentPage(BasePage):
    """The /payment page — card details and order confirmation."""

    def __init__(self, page):
        super().__init__(page)

    def fill_card_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self.page.locator("input[name='name_on_card']").fill(name_on_card)
        self.page.locator("input[name='card_number']").fill(card_number)
        self.page.locator("input[name='cvc']").fill(cvc)
        self.page.locator("input[name='expiry_month']").fill(expiry_month)
        self.page.locator("input[name='expiry_year']").fill(expiry_year)

    def pay_and_confirm_order(self):
        self.page.get_by_role("button", name="Pay and Confirm Order").click()

    def order_confirmed_locator(self):
        return self.page.get_by_text("Order Placed!")

    def get_field_validation_message(self, field_name):
        return self.page.locator(f"input[name='{field_name}']").evaluate("el => el.validationMessage")