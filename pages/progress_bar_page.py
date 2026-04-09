from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class ProgressBarPage(BasePage):
    URL = "https://demoqa.com/progress-bar"

    START_STOP_BTN = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.XPATH, "//div[@role='progressbar']")
    RESET_BTN = (By.ID, "resetButton")

    def navigate(self):
        self.driver.get(self.URL)
        self._remove_ads()

    def get_progress_value(self) -> int:
        element = self.find_element(self.PROGRESS_BAR)
        return int(element.get_attribute("aria-valuenow"))

    def stop_at_target(self, target_value=22):
        self.click(self.START_STOP_BTN)
        
        while True:
            current_value = self.get_progress_value()
            if current_value >= target_value:
                self.click(self.START_STOP_BTN)
                break

    def wait_until_100_percent(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: int(d.find_element(*self.PROGRESS_BAR).get_attribute("aria-valuenow")) == 100
        )

    def resume_and_reset(self):
        self.click(self.START_STOP_BTN)
        self.wait_until_100_percent()
        self.click(self.RESET_BTN)