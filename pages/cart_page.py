from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # Locators
    CART_INFO_TABLE = (By.ID, "cart_info_table")
    CART_PRODUCTS = (By.XPATH, "//tbody//tr")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[text()='Proceed To Checkout']")
    REGISTER_LOGIN_MODAL = (By.XPATH, "//u[text()='Register / Login']")
    SUBSCRIPTION_HEADING = (By.XPATH, "//div[@class='single-widget']//h2")
    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUCCESS_SUBSCRIBE_MESSAGE = (By.XPATH, "//div[@class='alert-success alert']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_visible(self):
        return self.is_element_visible(self.CART_INFO_TABLE)

    def get_cart_products_count(self):
        try:
            return len(self.find_elements(self.CART_PRODUCTS))
        except:
            return 0

    def get_product_details(self, index=1):
        product_name = (By.XPATH, f"(//tbody//tr)[{index}]//h4/a")
        product_price = (By.XPATH, f"(//tbody//tr)[{index}]//td[@class='cart_price']//p")
        product_quantity = (By.XPATH, f"(//tbody//tr)[{index}]//td[@class='cart_quantity']//button")
        product_total = (By.XPATH, f"(//tbody//tr)[{index}]//td[@class='cart_total']//p")

        return {
            'name': self.get_text(product_name),
            'price': self.get_text(product_price),
            'quantity': self.get_text(product_quantity),
            'total': self.get_text(product_total)
        }

    def remove_product(self, index=1):
        remove_button = (By.XPATH, f"(//tbody//tr)[{index}]//a[@class='cart_quantity_delete']")
        self.click(remove_button)

    def click_proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_register_login_modal(self):
        self.click(self.REGISTER_LOGIN_MODAL)

    def subscribe_email(self, email):
        self.scroll_to_element(self.SUBSCRIPTION_EMAIL)
        self.type(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIPTION_BUTTON)

    def is_subscription_success_visible(self):
        return self.is_element_visible(self.SUCCESS_SUBSCRIBE_MESSAGE)

    def verify_product_in_cart(self, product_name):
        products = self.find_elements((By.XPATH, "//tbody//tr//h4/a"))
        for product in products:
            if product_name.lower() in product.text.lower():
                return True
        return False