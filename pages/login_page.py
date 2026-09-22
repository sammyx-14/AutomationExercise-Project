from pages.base_page import BasePage
from pages.header_component import HeaderComponent


class LoginPage(BasePage):
    """The /login page — login form and the initial signup fields on the same page."""

    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    def login(self, email, password):
        self.page.locator("form").filter(
            has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def is_incorrect_login_credentials_error_visible(self):
        return self.page.get_by_text("Your email or password is incorrect!").is_visible()

    def start_signup(self, name, email):
        self.page.get_by_role("textbox", name="Name").fill(name)
        self.page.locator("form").filter(
            has_text="Signup").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("button", name="Signup").click()

    def email_already_exists_locator(self):
        return self.page.get_by_text("Email Address already exist!")
