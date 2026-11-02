import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SUCCESS_AUTH_MSG = "Congratulations! You must have the proper credentials."


@pytest.mark.basic_auth
class TestBasicAuth:

    def test_basic_auth(self, page: Page):
        # set httpCredentials on a new context 

        auth_page.goto(TEST_APP_URL)
        auth_page.get_by_role("link", name="Basic Auth").click()

        # verify that SUCCESS_AUTH_MSG is displayed
