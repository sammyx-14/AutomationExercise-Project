from config import BASE_URL


class BasePage:
    """Parent class for all page objects — shared setup and helpers."""

    def __init__(self, page):
        self.page = page

    def goto(self, path=""):
        self.page.goto(f"{BASE_URL}{path}")
        self._dismiss_consent_banner()

    def _dismiss_consent_banner(self):
        consent_button = self.page.get_by_role("button", name="Consent")
        if consent_button.is_visible():
            consent_button.click()
