from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """The /signup page — Account Information and Address Information form."""

    def __init__(self, page):
        super().__init__(page)

    def fill_account_information(self, title, password, day, month, year):
        self.page.get_by_role("radio", name=title).check()
        self.page.get_by_role("textbox", name="Password *").fill(password)
        self.page.locator("#days").select_option(day)
        self.page.locator("#months").select_option(month)
        self.page.locator("#years").select_option(year)

    def fill_address_information(self, first_name, last_name, address, country, state, city, zipcode, mobile):
        self.page.get_by_role("textbox", name="First name *").fill(first_name)
        self.page.get_by_role("textbox", name="Last name *").fill(last_name)
        self.page.get_by_role("textbox", name="Address * (Street address, P.").fill(address)
        self.page.get_by_label("Country *").select_option(country)
        self.page.get_by_role("textbox", name="State *").fill(state)
        self.page.locator("#city").fill(city)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.get_by_role("textbox", name="Mobile Number *").fill(mobile)


    def create_account(self):
        self.page.get_by_role("button", name="Create Account").click()

    def account_created_locator(self):
        return self.page.get_by_text("Account Created!")

    def continue_after_signup(self):
        self.page.get_by_role("link", name="Continue").click()  