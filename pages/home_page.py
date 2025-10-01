from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout']")
    DELETE_ACCOUNT_LINK = (By.XPATH, "//a[@href='/delete_account']")
    LOGGED_IN_USER = (By.XPATH, "//li//a[contains(text(), 'Logged in as')]//b")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    CONTACT_US_LINK = (By.XPATH, "//a[@href='/contact_us']")
    TEST_CASES_LINK = (By.XPATH, "//a[@href='/test_cases']")
    SUBSCRIPTION_HEADING = (By.XPATH, "//div[@class='single-widget']//h2")
    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUCCESS_SUBSCRIBE_MESSAGE = (By.XPATH, "//div[@class='alert-success alert']")
    CATEGORY_SECTION = (By.XPATH, "//div[@class='left-sidebar']//h2[text()='Category']")
    WOMEN_CATEGORY = (By.XPATH, "//a[@href='#Women']")
    MEN_CATEGORY = (By.XPATH, "//a[@href='#Men']")
    KIDS_CATEGORY = (By.XPATH, "//a[@href='#Kids']")
    BRANDS_SECTION = (By.XPATH, "//div[@class='brands-name']")
    RECOMMENDED_ITEMS = (By.XPATH, "//div[@class='recommended_items']//h2")
    SCROLL_UP_BUTTON = (By.ID, "scrollUp")
    FULL_FLEDGED_TEXT = (By.XPATH, "//div[@class='item active']//h2")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_home(self):
        self.navigate_to("/")

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def get_logged_in_username(self):
        return self.get_text(self.LOGGED_IN_USER)

    def is_logged_in(self, username):
        return username in self.get_logged_in_username()

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        self.click(self.CART_LINK)

    def click_contact_us(self):
        self.click(self.CONTACT_US_LINK)

    def click_test_cases(self):
        self.click(self.TEST_CASES_LINK)

    def is_home_page_visible(self):
        return self.is_element_visible(self.LOGO)

    def subscribe_email(self, email):
        self.scroll_to_element(self.SUBSCRIPTION_EMAIL)
        self.type(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIPTION_BUTTON)

    def is_subscription_success_visible(self):
        return self.is_element_visible(self.SUCCESS_SUBSCRIBE_MESSAGE)

    def is_category_visible(self):
        return self.is_element_visible(self.CATEGORY_SECTION)

    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)

    def click_category_item(self, category, subcategory):
        category_locator = (By.XPATH, f"//a[@href='#{category}']")
        self.click(category_locator)
        subcategory_locator = (By.XPATH, f"//a[contains(@href, '/category_products/') and contains(text(), '{subcategory}')]")
        self.click(subcategory_locator)

    def is_brands_visible(self):
        return self.is_element_visible(self.BRANDS_SECTION)

    def click_brand(self, brand_name):
        brand_locator = (By.XPATH, f"//a[contains(@href, '/brand_products/') and contains(text(), '{brand_name}')]")
        self.scroll_to_element(brand_locator)
        self.click(brand_locator)

    def is_recommended_items_visible(self):
        return self.is_element_visible(self.RECOMMENDED_ITEMS)

    def add_recommended_product_to_cart(self, index=1):
        add_to_cart = (By.XPATH, f"(//div[@class='recommended_items']//a[@class='btn btn-success add-to-cart'])[{index}]")
        self.scroll_to_element(add_to_cart)
        self.click(add_to_cart)

    def scroll_to_bottom_page(self):
        self.scroll_to_bottom()

    def scroll_to_top_page(self):
        self.scroll_to_top()

    def click_scroll_up_button(self):
        self.click(self.SCROLL_UP_BUTTON)

    def is_scroll_up_button_visible(self):
        return self.is_element_visible(self.SCROLL_UP_BUTTON)

    def is_full_fledged_text_visible(self):
        return self.is_element_visible(self.FULL_FLEDGED_TEXT)