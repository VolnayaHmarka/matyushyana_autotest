import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

LEFT_FRAME_TEXT = "LEFT"
RIGHT_FRAME_TEXT = "RIGHT"


@pytest.mark.nested_frames
class TestNestedFrames:

    def test_check_text_in_frames(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="Frames", exact=True).click()
        page.get_by_role("link", name="Nested Frames").click()

        top_frame = page.frame_locator('frame[name="frame-top"]')

        # access the Left nested frame

        # expect that left frame text is correct

        # access the Right nested frame

        # expect that right frame text is correct
