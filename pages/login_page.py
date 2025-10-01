from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    LOGIN_HEADING = (By.XPATH, "//div[@class='login-form']//h2")
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    INVALID_CREDENTIALS_ERROR = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    SIGNUP_HEADING = (By.XPATH, "//div[@class='signup-form']//h2")
    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    EMAIL_EXISTS_ERROR = (By.XPATH, "//p[text()='Email Address already exist!']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_form_visible(self):
        return self.is_element_visible(self.LOGIN_HEADING)

    def is_signup_form_visible(self):
        return self.is_element_visible(self.SIGNUP_HEADING)

    def login(self, email, password):
        self.type(self.LOGIN_EMAIL, email)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def signup(self, name, email):
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def is_invalid_credentials_error_visible(self):
        return self.is_element_visible(self.INVALID_CREDENTIALS_ERROR)

    def is_email_exists_error_visible(self):
        return self.is_element_visible(self.EMAIL_EXISTS_ERROR)