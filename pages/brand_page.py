from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BrandPage(BasePage):
    # Locators
    BRAND_PRODUCTS_HEADING = (By.XPATH, "//h2[@class='title text-center']")
    PRODUCTS_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='product-image-wrapper']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_brand_products_page_visible(self, brand_name):
        heading_text = self.get_text(self.BRAND_PRODUCTS_HEADING)
        return brand_name.upper() in heading_text.upper()

    def get_products_count(self):
        return len(self.find_elements(self.PRODUCTS_LIST))

    def click_brand_from_sidebar(self, brand_name):
        brand_locator = (By.XPATH, f"//a[contains(@href, '/brand_products/') and contains(text(), '{brand_name}')]")
        self.scroll_to_element(brand_locator)
        self.click(brand_locator)