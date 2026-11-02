import os
import shutil

import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

DOWNLOAD_DIR = "./downloads"
TEST_FILE = "test.txt"


@pytest.mark.file_download
class TestFileDownload:

    def test_file_download(self, page: Page):
        # ensure download directory exists
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)

        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="File Download", exact=True).click()
        file_link = page.get_by_role("link", name=TEST_FILE, exact=True)

        downloaded_file_path = os.path.join(DOWNLOAD_DIR, TEST_FILE)

        # wait until the file is fully downloaded along the specific downloaded_file_path
        with page.expect_download() as download_info:
            file_link.click()
        download = download_info.value
        download.save_as(downloaded_file_path)

        # assert that file downloaded
        assert os.path.exists(downloaded_file_path)

        # cleanup: delete the DOWNLOAD_DIR folder along with all its contents
        shutil.rmtree(downloaded_file_path, ignore_errors=True)