from pages.base_page import BasePage

class GooglePage(BasePage):

    def search(self, search_term):
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys(search_term)
        search_box.submit()

    def get_page_title(self):
        return self.driver.title