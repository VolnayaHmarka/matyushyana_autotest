from playwright.sync_api import Page
from framework.ui.decorators.decorators import step
from framework.ui.constants.elements import WikipediaCommonLocators
from framework.ui.elements.label import Label
from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

class ArticlePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Label(page, page.locator('//h1'), 'Article page unique element'), 'Article Page')
        self.page = page
        self.download_as_pdf_button = page.locator('a[title="Download this page as a PDF file"]')
        self.tools_menu = Button(page, WikipediaCommonLocators.TOOLS_MENU, 'Tools menu')

    @step("Click Tools menu button")
    def click_tools_menu_button(self):
        self.tools_menu.click()

    @step("Click 'Download as PDF'")
    def click_download_as_pdf_button(self):
        self.download_as_pdf_button.click()
