import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    DOB_INPUT = (By.ID, "dateOfBirthInput")
    UPLOAD_FILE = (By.ID, "uploadPicture")
    SUBMIT_BTN = (By.ID, "submit")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    CLOSE_MODAL_BTN = (By.ID, "closeLargeModal")

    def navigate(self):
        self.driver.get(self.URL)
        self._remove_ads() 

    def fill_basic_info(self, first, last, email, mobile):
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.EMAIL, email)
        self.type_text(self.MOBILE, mobile)

    def select_gender(self, gender):
        locator = (By.XPATH, f"//label[normalize-space()='{gender}']")
        self.click(locator)

    def select_hobbies(self, hobby):
        locator = (By.XPATH, f"//label[normalize-space()='{hobby}']")
        self.click(locator)

    def set_date_of_birth(self, date_str):
        element = self.find_element(self.DOB_INPUT)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date_str)
        element.send_keys(Keys.ENTER)

    def upload_txt_file(self, filename="challenge_file.txt"):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "data", filename)
        self.find_element(self.UPLOAD_FILE).send_keys(file_path)

    def submit_form(self):
        # self.driver.save_screenshot("evidencia_formulario_preenchido.png") Coloquei para fins de validação, mas some com o código
        self.click(self.SUBMIT_BTN)

    def get_success_message(self):
        return self.find_element(self.MODAL_TITLE).text
        
    def close_modal(self):
        self.click(self.CLOSE_MODAL_BTN)