from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class WebTablesPage(BasePage):
    URL = "https://demoqa.com/webtables"

    ADD_BTN = (By.ID, "addNewRecordButton")
    SEARCH_BOX = (By.ID, "searchBox")
    MODAL = (By.CLASS_NAME, "modal-content")

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT_BTN = (By.ID, "submit")

    def navigate(self):
        self.driver.get(self.URL)
        self._remove_ads()

    def click_add_record(self):
        self.click(self.ADD_BTN)

    def fill_record_form(self, first, last, email, age, salary, department):
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.EMAIL, email)
        self.type_text(self.AGE, str(age))
        self.type_text(self.SALARY, str(salary))
        self.type_text(self.DEPARTMENT, department)

    def submit_form(self):
        element = self.find_element(self.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].click();", element)

        try:
            self.wait.until(EC.invisibility_of_element_located(self.MODAL))
        except:
            pass

    def search_record(self, text):
        self.type_text(self.SEARCH_BOX, text)

    def _get_row_locator(self, text):
        return (By.XPATH, f"//tr[td[contains(normalize-space(), '{text}')]]")

    def is_record_present(self, text):
        try:
            self.wait.until(EC.presence_of_element_located(self._get_row_locator(text)))
            return True
        except:
            return False

    def is_record_absent(self, text):
        try:
            self.wait.until(EC.invisibility_of_element_located(self._get_row_locator(text)))
            return True
        except:
            return False

    def click_edit_record(self, text):
        locator = (By.XPATH, f"//tr[td[contains(normalize-space(), '{text}')]]//span[contains(@id, 'edit-record')]")
        self.click(locator)

    def click_delete_record(self, text):
        locator = (By.XPATH, f"//tr[td[contains(normalize-space(), '{text}')]]//span[contains(@id, 'delete-record')]")
        self.click(locator)