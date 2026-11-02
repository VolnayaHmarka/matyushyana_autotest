from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

TEST_FILE = "test_file.txt"
TEST_FILE_PATH = Path(__file__).parent / "resources" / TEST_FILE


@pytest.mark.file_upload
class TestFileUpload:

    def test_file_upload(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="File Upload").click()

        # upload file with TEST_FILE_PATH path

        # expect that TEST_FILE on Upload page is correct