import uuid

import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

random_string = str(uuid.uuid4())


@pytest.mark.dynamic_controls
class TestDynamicControls:

    def test_dynamic_controls(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="Dynamic Controls").click()
        page.get_by_role("button", name="Enable").click()

        input_field = page.locator("#input-example input")

        # expect that input_field is enabled

        # input random_string into input_field

        # expect that random_string is displayed