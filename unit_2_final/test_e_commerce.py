import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SORT_DROPDOWN_VALUE = "price,asc"
CURRENCY_SYMBOL = "$"
SUCCESS_MSG_ADD_TO_CART = "Product added to shopping cart."

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

        #check that prices are sorted from Low to High
        def parse_price(price_in_text):
            return float(price_in_text.replace(CURRENCY_SYMBOL, '').strip())
        
        prices_text = page.locator("#card[data-test='product-price']").all_inner_texts()
        prices = [parse_price(price) for price in prices_text]
        
        assert prices == sorted(prices), f"Expected: prices are sorted form Low to High: {sorted(prices)}, Actual: {prices}"

        #check that the 1st card page opens
        first_card = page.locator(".card").first
        first_card_name = first_card.get_by_role("heading").inner_text()

        first_card.click()

        expect(page.locator("[data-test='product-name']")).to_have_text(first_card_name)

        #add to card
        page.get_by_role("button", name="Add to cart").click()
                
        toast = page.get_by_role("alert")
        expect(toast).to_be_visible()
        expect(toast).to_have_text(SUCCESS_MSG_ADD_TO_CART)
                
        expect(page.get_by_role("link", name="cart")).to_be_visible()