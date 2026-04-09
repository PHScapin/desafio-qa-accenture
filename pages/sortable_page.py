import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class SortablePage(BasePage):
    URL = "https://demoqa.com/sortable"

    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

    def navigate(self):
        self.driver.get(self.URL)
        self._remove_ads()

    def get_list_items_text(self) -> list:
        """Retorna uma lista com os textos de todos os elementos atuais"""
        elements = self.driver.find_elements(*self.LIST_ITEMS)
        return [el.text for el in elements]

    def sort_in_ascending_order(self):
        """Usa Drag and Drop para ordenar os elementos.
        Se eles já estiverem ordenados, bagunça a lista primeiro para provar que a automação funciona."""
        
        desired_order = ["One", "Two", "Three", "Four", "Five", "Six"]
        actions = ActionChains(self.driver)
        
        items = self.driver.find_elements(*self.LIST_ITEMS)
        if items[0].text == "One":
            actions.click_and_hold(items[5]).move_to_element(items[0]).release().perform()
            time.sleep(1) 

        for index, expected_text in enumerate(desired_order):
            items = self.driver.find_elements(*self.LIST_ITEMS)
            current_text = items[index].text
            
            if current_text != expected_text:
                source_element = next(el for el in items if el.text == expected_text)
                target_element = items[index]
                
                actions.click_and_hold(source_element)\
                       .move_to_element(target_element)\
                       .release()\
                       .perform()
                
                time.sleep(0.5) 

