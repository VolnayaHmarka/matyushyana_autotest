import pytest
from playwright.sync_api import Page, expect

from configs.settings import TEST_APP_URL

SUCCESS_ALERT_MSG = "You successfully clicked an alert"


@pytest.mark.alerts
class TestAlertsHandling:

    def test_alerts_handling(self, page: Page):
        page.goto(TEST_APP_URL)

        page.get_by_role("link", name="JavaScript Alerts").click()

        # accept alert
  
        # expect that successfulMessage is displayed
