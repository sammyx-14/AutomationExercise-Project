
class HeaderComponent:
    """Reusable header — login state, logout, nav. Composed into other page objects, not used standalone."""

    def __init__(self, page):
        self.page = page

    def is_logged_in_as(self, name):
        return self.page.get_by_text(f"Logged in as {name}").is_visible()


    def signup_login_locator(self):
        return self.page.get_by_role("link", name=" Signup / Login")


    def logged_in_as_locator(self, name):
        return self.page.get_by_text(f"Logged in as {name}")

    def logout(self):
        self.page.get_by_role("link", name=" Logout").click()


    def delete_account(self):
        self.page.get_by_role("link", name=" Delete Account").click()

    def account_deleted_locator(self):
        return self.page.get_by_text("Account Deleted!")

    def continue_after_delete(self):
        self.page.get_by_role("link", name="Continue").click()        