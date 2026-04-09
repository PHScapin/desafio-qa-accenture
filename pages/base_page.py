from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import JavascriptException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).scroll_to_element(element).perform()
        element.click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(element).perform()
        element.clear()
        element.send_keys(text)

    def _remove_ads(self):
        """Método centralizado para limpar o layout do DemoQA"""
        try:
            self.driver.execute_script("""
                var ban = document.getElementById('fixedban');
                if (ban) { ban.style.display = 'none'; }
                
                var foot = document.querySelector('footer');
                if (foot) { foot.style.display = 'none'; }
            """)
        except JavascriptException:
            pass 