import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SUCCESS_AUTH_MSG = "Congratulations! You must have the proper credentials."


@pytest.mark.basic_auth
class TestBasicAuth:

    def test_basic_auth(self, page: Page):  
        # set httpCredentials on a new context
        context = page.context.browser.new_context(
        http_credentials={"username": "admin", "password": "admin"}
        )
        auth_page = context.new_page()

        auth_page.goto(TEST_APP_URL)
        auth_page.get_by_role("link", name="Basic Auth").click()

        # verify that SUCCESS_AUTH_MSG is displayed
        expect(auth_page.get_by_text(SUCCESS_AUTH_MSG, exact=True)).to_be_visible()
