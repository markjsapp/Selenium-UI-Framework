from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_term):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    def get_page_title(self):
        return self.driver.title