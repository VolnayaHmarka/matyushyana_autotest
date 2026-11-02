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
        left_frame = top_frame.frame_locator('frame[name="frame-left"]')

        # expect that left frame text is correct
        expect(left_frame.locator('body')).to_have_text(LEFT_FRAME_TEXT)

        # access the Right nested frame
        right_frame = top_frame.frame_locator('frame[name="frame-right"]')

        # expect that right frame text is correct
        expect(right_frame.locator('body')).to_have_text(RIGHT_FRAME_TEXT)
