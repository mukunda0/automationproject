from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    ALL_PRODUCTS_HEADING = (By.XPATH, "//h2[@class='title text-center']")
    PRODUCTS_LIST = (By.XPATH, "//div[@class='features_items']//div[@class='product-image-wrapper']")
    SEARCH_PRODUCT_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADING = (By.XPATH, "//h2[@class='title text-center' and text()='Searched Products']")

    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']//p[contains(text(), 'Category:')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span//span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p//b[text()='Availability:']/..")
    PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']//p//b[text()='Condition:']/..")
    PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']//p//b[text()='Brand:']/..")

    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn btn-default cart']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART_MODAL_BUTTON = (By.XPATH, "//u[text()='View Cart']")

    WRITE_REVIEW_HEADING = (By.XPATH, "//a[@href='#reviews']")
    REVIEW_NAME = (By.ID, "name")
    REVIEW_EMAIL = (By.ID, "email")
    REVIEW_TEXT = (By.ID, "review")
    REVIEW_SUBMIT_BUTTON = (By.ID, "button-review")
    REVIEW_SUCCESS_MESSAGE = (By.XPATH, "//span[text()='Thank you for your review.']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_all_products_page_visible(self):
        return self.is_element_visible(self.ALL_PRODUCTS_HEADING)

    def get_products_count(self):
        return len(self.find_elements(self.PRODUCTS_LIST))

    def view_product_details(self, index=1):
        view_product = (By.XPATH, f"(//a[contains(@href, '/product_details/')])[{index}]")
        self.click(view_product)

    def search_product(self, product_name):
        self.type(self.SEARCH_PRODUCT_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_searched_products_visible(self):
        return self.is_element_visible(self.SEARCHED_PRODUCTS_HEADING)

    def get_all_product_names(self):
        products = self.find_elements((By.XPATH, "//div[@class='productinfo text-center']//p"))
        return [product.text for product in products]

    def is_product_information_visible(self):
        return (self.is_element_visible(self.PRODUCT_NAME) and
                self.is_element_visible(self.PRODUCT_CATEGORY) and
                self.is_element_visible(self.PRODUCT_PRICE))

    def set_quantity(self, quantity):
        element = self.find_element(self.QUANTITY_INPUT)
        element.clear()
        element.send_keys(str(quantity))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_view_cart(self):
        self.click(self.VIEW_CART_MODAL_BUTTON)

    def hover_and_add_product_to_cart(self, index=1):
        product = (By.XPATH, f"(//div[@class='product-image-wrapper'])[{index}]")
        add_to_cart = (By.XPATH,
                       f"(//div[@class='product-image-wrapper'])[{index}]//a[@class='btn btn-default add-to-cart']")
        self.hover_over_element(product)
        self.click(add_to_cart)

    def write_review(self, name, email, review_text):
        self.scroll_to_element(self.WRITE_REVIEW_HEADING)
        self.type(self.REVIEW_NAME, name)
        self.type(self.REVIEW_EMAIL, email)
        self.type(self.REVIEW_TEXT, review_text)
        self.click(self.REVIEW_SUBMIT_BUTTON)

    def is_review_success_visible(self):
        return self.is_element_visible(self.REVIEW_SUCCESS_MESSAGE)