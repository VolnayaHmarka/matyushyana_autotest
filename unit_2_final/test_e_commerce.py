import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SORT_DROPDOWN_VALUE = "price,asc"
CURRENCY_SYMBOL = "$"
SUCCESS_MSG_ADD_TO_CART = "Product added to shopping cart."
QTY_UPD_MESSAGE = "Product quantity updated."

@pytest.mark.e_commerce
class TestEcommerce:
    def test_e_commerce(self, page: Page):
        page.goto(TEST_APP_URL)

        #1 choose checkbox 
        checkbox = page.get_by_label("MightyCraft Hardware", exact=True)

        checkbox.check()

        expect(checkbox).to_be_checked()

        expect(page.locator("[data-test='filter_completed']")).to_be_visible()

        #2 select from Sort dropdown list
        sort_dropdown = page.locator("[data-test='sort']")
        
        sort_dropdown.select_option(value=SORT_DROPDOWN_VALUE)

        expect(page.locator("[data-test='sorting_completed']")).to_be_visible()
        expect(sort_dropdown).to_have_value(SORT_DROPDOWN_VALUE)

        #3 check that prices are sorted from Low to High
        parse_price = lambda price_in_text: float(price_in_text.replace(CURRENCY_SYMBOL, '').strip())

        prices_locator = page.locator(".card [data-test='product-price']")
        expect(prices_locator.first).to_be_visible()
        prices_text = prices_locator.all_inner_texts()
        prices = [parse_price(price) for price in prices_text]
        
        assert prices, "No prices found"
        assert prices == sorted(prices), f"Expected: prices are sorted form Low to High: {sorted(prices)}, Actual: {prices}"

        #4 check that the 1st card page opens
        first_card = page.locator(".card").first
        first_card_name = first_card.get_by_role("heading").inner_text()
        first_card_price = prices[0]

        first_card.click()

        expect(page.locator("[data-test='product-name']")).to_have_text(first_card_name)

        #5 add to card
        page.get_by_role("button", name="Add to cart").click()
                
        toast = page.get_by_label(SUCCESS_MSG_ADD_TO_CART)
        expect(toast).to_be_visible()
                
        expect(page.get_by_role("link", name="cart")).to_be_visible()

        #6 check that item is present in the cart
        page.get_by_role("link", name="cart").click()

        table = page.get_by_role("table")
        expect(table).to_be_visible()
        
        items = page.locator("[data-test='product-title']")

        expect(items.filter(has_text=first_card_name)).to_be_visible()

        #7 increase the qty to 3 and check the total price
        total_price = first_card_price * 3

        qty_field = page.get_by_role("spinbutton")
        qty_field.clear()
        qty_field.fill('3')

        page.keyboard.press("Enter")

        toast_qty_upd = page.get_by_label(QTY_UPD_MESSAGE, exact=True)
        expect(toast_qty_upd).to_be_visible()

        expect(qty_field).to_have_value('3')

        total_item_text = page.locator("[data-test='line-price']").inner_text()
        total_item = parse_price(total_item_text)

        assert total_item == total_price, f"Expected: total price: {total_price}, Actual: {total_item}"

                            


    




