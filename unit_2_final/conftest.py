from enum import Enum

import pytest
from playwright.sync_api import sync_playwright, Browser

DEFAULT_WAITING_TIMEOUT = 30000  # Maximum time in milliseconds
DEFAULT_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}  # Default page width and height in pixels.


class BrowserType(Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


def _get_browser(playwright: sync_playwright, browser_type: BrowserType, headless: bool = False) -> Browser:
    browser_map = {
        BrowserType.FIREFOX: playwright.firefox,
        BrowserType.WEBKIT: playwright.webkit,
        BrowserType.CHROMIUM: playwright.chromium
    }
    browser = browser_map.get(browser_type, playwright.chromium)
    return browser.launch(headless=headless)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default=BrowserType.CHROMIUM.value,
                     help="Choose a browser: chromium, firefox, webkit")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture
def page(request):
    browser_channel = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    with sync_playwright() as playwright:
        browser = _get_browser(playwright, BrowserType(browser_channel), headless)

        context = browser.new_context(viewport=DEFAULT_VIEWPORT_SIZE)
        context.set_default_timeout(DEFAULT_WAITING_TIMEOUT)

        page = context.new_page()
        yield page

        page.close()
        browser.close()
