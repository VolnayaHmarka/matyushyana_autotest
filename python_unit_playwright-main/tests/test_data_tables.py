import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

EXPECTED_DUE_VALUE = 251.00
CURRENCY_SYMBOL = "$"


@pytest.mark.data_tables
class TestDataTables:

    def test_data_table(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="Sortable Data Tables").click()

        # get Due column elements

        total_sum = 0.0

        # Get rows count in table.
        # Loop through all rows, extracting values and removing currency symbols

        assert total_sum == EXPECTED_DUE_VALUE, f"Expected Due amount: {EXPECTED_DUE_VALUE}, Actual: {total_sum}"
