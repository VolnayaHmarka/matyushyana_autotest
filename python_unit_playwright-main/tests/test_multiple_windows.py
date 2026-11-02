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
        with page.context.expect_page() as new_page_info:
            click_here_link.click()
        new_page = new_page_info.value
        
        # expect that new window text is displayed
        expect(new_page.locator(".example")).to_have_text(NEW_WINDOW_TEXT)
