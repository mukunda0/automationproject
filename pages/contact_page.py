from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactPage(BasePage):
    # Locators
    GET_IN_TOUCH_HEADING = (By.XPATH, "//h2[text()='Get In Touch']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_TEXTAREA = (By.ID, "message")
    UPLOAD_FILE_INPUT = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")
    HOME_BUTTON = (By.XPATH, "//a[@class='btn btn-success']//span")

    def __init__(self, driver):
        super().__init__(driver)

    def is_get_in_touch_visible(self):
        return self.is_element_visible(self.GET_IN_TOUCH_HEADING)

    def fill_contact_form(self, name, email, subject, message):
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.SUBJECT_INPUT, subject)
        self.type(self.MESSAGE_TEXTAREA, message)

    def upload_file(self, file_path):
        self.find_element(self.UPLOAD_FILE_INPUT).send_keys(file_path)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    def is_success_message_visible(self):
        return self.is_element_visible(self.SUCCESS_MESSAGE)

    def click_home_button(self):
        self.click(self.HOME_BUTTON)