from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):
    # Locators
    CATEGORY_HEADING = (By.XPATH, "//h2[@class='title text-center']")
    PRODUCTS_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='product-image-wrapper']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_category_page_visible(self, category_name):
        heading_text = self.get_text(self.CATEGORY_HEADING)
        return category_name.upper() in heading_text.upper()

    def get_products_count(self):
        return len(self.find_elements(self.PRODUCTS_LIST))