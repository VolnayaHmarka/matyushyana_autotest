from pathlib import Path
import pytest
from configs.settings import WIKIPEDIA_URL
from framework.ui.browser.browser import Browser
from framework.utils import file_utils
from pages.wikipedia_main_page import WikipediaMainPage
from pages.article_page import ArticlePage
from pages.download_as_pdf_page import DownloadAsPdfPage

SEARCH_REQUEST_TEXT = 'Albert Einstein'

class TestDownloadPdf:

    @pytest.mark.download_pdf
    @pytest.mark.usefixtures("cleanup_download_dir")
    def test_download_pdf(self, browser: Browser, download_dir: Path):
        browser.page.goto(WIKIPEDIA_URL)

        main_page = WikipediaMainPage(browser.page)
        main_page.wait_for_page_to_load()
        main_page.select_english_language()
        main_page.type_search_request(SEARCH_REQUEST_TEXT)
        main_page.search_click()

        article_page = ArticlePage(browser.page)
        article_page.wait_for_page_to_load()
        article_page.click_tools_menu_button()
        article_page.click_download_as_pdf_button()

        download_as_pdf_page = DownloadAsPdfPage(browser.page)
        download_as_pdf_page.wait_for_page_to_load()
        download_file_path = download_as_pdf_page.download_file(download_dir)
        
        assert file_utils.is_file_exist(download_file_path) is True
