import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SORT_DROPDOWN_VALUE = "price,asc"

@pytest.mark.e_commerce
class TestEcommerce:
    def test_e_commerce(self, page: Page):
        page.goto(TEST_APP_URL)

        #choose checkbox 
        checkbox = page.get_by_label("MightyCraft Hardware", exact=True)

        checkbox.check()

        expect(checkbox).to_be_checked()

        #select from Sort dropdown list
        sort_dropdown = page.get_by_role("combobox", name="sort") 
        
        sort_dropdown.select_option(value=SORT_DROPDOWN_VALUE)
        
        expect(sort_dropdown).to_have_value(SORT_DROPDOWN_VALUE)