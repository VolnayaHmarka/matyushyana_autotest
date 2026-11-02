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
        page.locator("#table1").wait_for()

        # get Due column elements
        due_column = page.locator('#table1 td:nth-child(4)')
        total_sum = 0.0
        
        # Get rows count in table.
        count = due_column.count()

        # Loop through all rows, extracting values and removing currency symbols
        for i in range(count):
            text = due_column.all_inner_texts()
            total_sum += float(text.replace(CURRENCY_SYMBOL, '').strip())

        assert total_sum == EXPECTED_DUE_VALUE, f"Expected Due amount: {EXPECTED_DUE_VALUE}, Actual: {total_sum}"
