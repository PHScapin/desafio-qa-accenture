from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WindowsPage(BasePage):
    URL = "https://demoqa.com/browser-windows"
    NEW_WINDOW_BTN = (By.ID, "windowButton")
    SAMPLE_TEXT = (By.ID, "sampleHeading")

    def navigate(self):
        self.driver.get(self.URL)
        self._remove_ads()

    def open_new_window(self):
        self.main_window = self.driver.current_window_handle
        self.click(self.NEW_WINDOW_BTN)
        
        self.wait.until(lambda d: len(d.window_handles) > 1)
        
        for handle in self.driver.window_handles:
            if handle != self.main_window:
                self.driver.switch_to.window(handle)
                break

    def get_sample_text(self):
        return self.find_element(self.SAMPLE_TEXT).text

    def close_and_return(self):
        self.driver.close() 
        self.driver.switch_to.window(self.main_window) 