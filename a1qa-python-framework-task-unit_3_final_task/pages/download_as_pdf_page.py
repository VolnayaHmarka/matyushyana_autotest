from pathlib import Path

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

class DownloadAsPdfPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Label(page, page.get_by_role('heading', name='Download as PDF'), 'Download as PDF page unique element'), 'Download as PDF Page')
        self.file_name_label = Label(page, page.locator('//div[@class="mw-electronpdfservice-selection-label-desc"]'), 'File name label')
        self.download_button = Button(page, page.locator('//button[@class="oo-ui-inputWidget-input oo-ui-buttonElement-button"]'), 'Download button')

    @step("Get name of the file to download")
    def get_file_name(self) -> str:
        return self.file_name_label.get_text()

    @step("Download PDF file")
    def download_file(self, download_dir: Path) -> Path:
        file_name = self.get_file_name()

        with self.page.expect_download() as download_info:
            self.download_button.click()
        download = download_info.value

        downloaded_file_path = download_dir.joinpath(file_name)
        download.save_as(downloaded_file_path)

        return downloaded_file_path