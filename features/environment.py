from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.brand_page import BrandPage
from pages.category_page import CategoryPage
from pages.contact_page import ContactPage
from api.client import APIClient
import json
import os


def before_all(context):
    """Runs once before all tests"""
    context.test_data = load_test_data()
    context.api_client = APIClient()


def before_scenario(context, scenario):
    """Runs before each scenario"""
    if 'api' not in scenario.tags:
        # Initialize WebDriver for UI tests
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        context.driver.implicitly_wait(10)

        # Initialize Page Objects
        context.home_page = HomePage(context.driver)
        context.login_page = LoginPage(context.driver)
        context.signup_page = SignupPage(context.driver)
        context.product_page = ProductPage(context.driver)
        context.cart_page = CartPage(context.driver)
        context.checkout_page = CheckoutPage(context.driver)
        context.brand_page = BrandPage(context.driver)
        context.category_page = CategoryPage(context.driver)
        context.contact_page = ContactPage(context.driver)


def after_scenario(context, scenario):
    """Runs after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context):
    """Runs once after all tests"""
    pass


def load_test_data():
    """Load test data from JSON files"""
    data = {}
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

    data_files = ['users.json', 'products.json', 'brands.json',
                  'categories.json', 'testdata.json']

    for file_name in data_files:
        file_path = os.path.join(data_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                key = file_name.replace('.json', '')
                data[key] = json.load(f)

    return data