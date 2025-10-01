from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class SignupPage(BasePage):
    # Locators
    ACCOUNT_INFO_HEADING = (By.XPATH, "//b[text()='Enter Account Information']")
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    ACCOUNT_CREATED_HEADING = (By.XPATH, "//h2[@data-qa='account-created']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    ACCOUNT_DELETED_HEADING = (By.XPATH, "//h2[@data-qa='account-deleted']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_account_info_visible(self):
        return self.is_element_visible(self.ACCOUNT_INFO_HEADING)

    def fill_account_information(self, title, password, day, month, year):
        if title.lower() == "mr":
            self.click(self.TITLE_MR)
        else:
            self.click(self.TITLE_MRS)

        self.type(self.PASSWORD, password)

        Select(self.find_element(self.DAY_DROPDOWN)).select_by_value(day)
        Select(self.find_element(self.MONTH_DROPDOWN)).select_by_value(month)
        Select(self.find_element(self.YEAR_DROPDOWN)).select_by_value(year)

    def select_newsletter(self):
        self.click(self.NEWSLETTER_CHECKBOX)

    def select_special_offers(self):
        self.click(self.SPECIAL_OFFERS_CHECKBOX)

    def fill_address_information(self, first_name, last_name, company, address1, address2,
                                 country, state, city, zipcode, mobile):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.COMPANY, company)
        self.type(self.ADDRESS1, address1)
        self.type(self.ADDRESS2, address2)
        Select(self.find_element(self.COUNTRY_DROPDOWN)).select_by_visible_text(country)
        self.type(self.STATE, state)
        self.type(self.CITY, city)
        self.type(self.ZIPCODE, zipcode)
        self.type(self.MOBILE_NUMBER, mobile)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created_visible(self):
        return self.is_element_visible(self.ACCOUNT_CREATED_HEADING)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_account_deleted_visible(self):
        return self.is_element_visible(self.ACCOUNT_DELETED_HEADING)