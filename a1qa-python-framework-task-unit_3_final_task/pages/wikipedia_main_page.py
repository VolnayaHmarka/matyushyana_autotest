from playwright.sync_api import Page
from framework.ui.decorators.decorators import step
from framework.ui.constants.elements import WikipediaCommonLocators
from framework.ui.elements.button import Button
from framework.ui.elements.dropdown import Dropdown
from framework.ui.elements.input import Input
from framework.ui.pages.base_page import BasePage

class WikipediaMainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Input(page, page.locator('input#searchInput'), 'main page unique element'), 'Main Page')
        self.search_language = Dropdown(page, WikipediaCommonLocators.SEARCH_LANGUAGE, 'Search language dropdown')
        self.search_text_box = Input(page, WikipediaCommonLocators.SEARCH_TEXT_BOX, 'Search textbox')
        self.search_button = Button(page, WikipediaCommonLocators.SEARCH_BUTTON, 'Search button')

    @step("Check that the English language is selected for search")
    def select_english_language(self):
        self.search_language.select_option('English')

    @step("Type search request")
    def type_search_request(self, text: str):
        self.search_text_box.type_text(text)

    @step("Click the Search button")
    def search_click(self):
        self.search_button.click()
