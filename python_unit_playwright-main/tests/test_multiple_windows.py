import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

NEW_WINDOW_TEXT = "New Window"


@pytest.mark.multiple_windows
class TestMultipleWindows:

    def test_new_window_text_is_displayed(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="Multiple Windows").click()

        click_here_link = page.get_by_role("link", name="Click Here")

        # click 'Click Here' link and wait until new window opened
        
        # expect that new window text is displayed
