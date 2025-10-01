from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators
    DELIVERY_ADDRESS_HEADING = (By.XPATH, "//h3[text()='Your delivery address']")
    BILLING_ADDRESS_HEADING = (By.XPATH, "//h3[text()='Your billing address']")

    DELIVERY_TITLE_NAME = (By.XPATH,
                           "(//ul[@id='address_delivery']//li[@class='address_firstname address_lastname'])[1]")
    DELIVERY_COMPANY = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_address1 address_address2'][1]")
    DELIVERY_ADDRESS1 = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_address1 address_address2'][2]")
    DELIVERY_CITY_STATE_ZIP = (By.XPATH,
                               "//ul[@id='address_delivery']//li[@class='address_city address_state_name address_postcode']")
    DELIVERY_COUNTRY = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_country_name']")
    DELIVERY_PHONE = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_phone']")

    BILLING_TITLE_NAME = (By.XPATH, "(//ul[@id='address_invoice']//li[@class='address_firstname address_lastname'])[1]")
    BILLING_COMPANY = (By.XPATH, "//ul[@id='address_invoice']//li[@class='address_address1 address_address2'][1]")
    BILLING_ADDRESS1 = (By.XPATH, "//ul[@id='address_invoice']//li[@class='address_address1 address_address2'][2]")
    BILLING_CITY_STATE_ZIP = (By.XPATH,
                              "//ul[@id='address_invoice']//li[@class='address_city address_state_name address_postcode']")
    BILLING_COUNTRY = (By.XPATH, "//ul[@id='address_invoice']//li[@class='address_country_name']")
    BILLING_PHONE = (By.XPATH, "//ul[@id='address_invoice']//li[@class='address_phone']")

    ORDER_REVIEW = (By.XPATH, "//h2[text()='Review Your Order']")
    COMMENT_TEXTAREA = (By.NAME, "message")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@href='/payment']")

    PAYMENT_NAME_ON_CARD = (By.NAME, "name_on_card")
    PAYMENT_CARD_NUMBER = (By.NAME, "card_number")
    PAYMENT_CVC = (By.NAME, "cvc")
    PAYMENT_EXPIRY_MONTH = (By.NAME, "expiry_month")
    PAYMENT_EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_AND_CONFIRM_BUTTON = (By.ID, "submit")

    ORDER_PLACED_MESSAGE = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[text()='Download Invoice']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_checkout_page_visible(self):
        return (self.is_element_visible(self.DELIVERY_ADDRESS_HEADING) and
                self.is_element_visible(self.BILLING_ADDRESS_HEADING))

    def get_delivery_address(self):
        return {
            'title_name': self.get_text(self.DELIVERY_TITLE_NAME),
            'company': self.get_text(self.DELIVERY_COMPANY),
            'address1': self.get_text(self.DELIVERY_ADDRESS1),
            'city_state_zip': self.get_text(self.DELIVERY_CITY_STATE_ZIP),
            'country': self.get_text(self.DELIVERY_COUNTRY),
            'phone': self.get_text(self.DELIVERY_PHONE)
        }

    def get_billing_address(self):
        return {
            'title_name': self.get_text(self.BILLING_TITLE_NAME),
            'company': self.get_text(self.BILLING_COMPANY),
            'address1': self.get_text(self.BILLING_ADDRESS1),
            'city_state_zip': self.get_text(self.BILLING_CITY_STATE_ZIP),
            'country': self.get_text(self.BILLING_COUNTRY),
            'phone': self.get_text(self.BILLING_PHONE)
        }

    def verify_address_details(self, expected_details):
        delivery_address = self.get_delivery_address()
        billing_address = self.get_billing_address()
        return delivery_address == billing_address

    def add_order_comment(self, comment):
        self.type(self.COMMENT_TEXTAREA, comment)

    def click_place_order(self):
        self.scroll_to_element(self.PLACE_ORDER_BUTTON)
        self.click(self.PLACE_ORDER_BUTTON)

    def fill_payment_details(self, name, card_number, cvc, expiry_month, expiry_year):
        self.type(self.PAYMENT_NAME_ON_CARD, name)
        self.type(self.PAYMENT_CARD_NUMBER, card_number)
        self.type(self.PAYMENT_CVC, cvc)
        self.type(self.PAYMENT_EXPIRY_MONTH, expiry_month)
        self.type(self.PAYMENT_EXPIRY_YEAR, expiry_year)

    def click_pay_and_confirm(self):
        self.click(self.PAY_AND_CONFIRM_BUTTON)

    def is_order_placed_successfully(self):
        return self.is_element_visible(self.ORDER_PLACED_MESSAGE)

    def download_invoice(self):
        self.click(self.DOWNLOAD_INVOICE_BUTTON)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)