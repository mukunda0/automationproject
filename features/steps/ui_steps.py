from behave import given, when, then
from features.steps.helpers import (
    generate_random_email,
    generate_user_data,
    store_user_credentials,
    get_user_credentials
)
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.brand_page import BrandPage
from pages.category_page import CategoryPage
import time


# Common steps
@given('I am on the homepage')
def step_navigate_to_homepage(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.open()
    time.sleep(1)


@given('I navigate to login page')
def step_navigate_to_login_page(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.open()
    context.home_page.click_login_link()
    context.login_page = LoginPage(context.driver)


@then('I should see the homepage')
def step_verify_homepage(context):
    context.home_page = HomePage(context.driver, context.base_url)
    assert context.home_page.is_homepage_visible(), "Homepage is not visible"


@then('I should be on the homepage')
def step_verify_on_homepage(context):
    current_url = context.driver.current_url
    assert context.base_url in current_url, f"Not on homepage. Current URL: {current_url}"


# TC01: Register User
@when('I click on Signup / Login button')
def step_click_signup_login(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_login_link()
    context.login_page = LoginPage(context.driver)


@then('I should see "New User Signup!" text')
def step_verify_signup_text(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.is_signup_form_visible(), "Signup form is not visible"


@when('I enter name "{name}" and email address')
def step_enter_signup_details(context, name):
    context.test_name = name
    context.test_email = generate_random_email()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_signup_name(context.test_name)
    context.login_page.enter_signup_email(context.test_email)


@when('I click Signup button')
def step_click_signup_button(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_signup_button()
    context.signup_page = SignupPage(context.driver)


@then('I should see "ENTER ACCOUNT INFORMATION" text')
def step_verify_account_info_text(context):
    context.signup_page = SignupPage(context.driver)
    assert context.signup_page.is_account_info_visible(), "Account information page not visible"


@when('I fill in account details')
def step_fill_account_details(context):
    context.user_data = generate_user_data()
    context.user_data['email'] = context.test_email
    context.user_data['name'] = context.test_name
    context.test_password = context.user_data['password']

    context.signup_page = SignupPage(context.driver)
    context.signup_page.select_title(context.user_data['title'])
    context.signup_page.enter_password(context.user_data['password'])
    context.signup_page.select_date_of_birth(
        context.user_data['birth_date'],
        context.user_data['birth_month'],
        context.user_data['birth_year']
    )


@when('I select checkbox "Sign up for our newsletter!"')
def step_select_newsletter(context):
    context.signup_page = SignupPage(context.driver)
    context.signup_page.select_newsletter()


@when('I select checkbox "Receive special offers from our partners!"')
def step_select_special_offers(context):
    context.signup_page = SignupPage(context.driver)
    context.signup_page.select_special_offers()


@when('I fill in address details')
def step_fill_address_details(context):
    context.signup_page = SignupPage(context.driver)
    context.signup_page.enter_first_name(context.user_data['first_name'])
    context.signup_page.enter_last_name(context.user_data['last_name'])
    context.signup_page.enter_company(context.user_data['company'])
    context.signup_page.enter_address1(context.user_data['address'])
    context.signup_page.enter_address2(context.user_data['address2'])
    context.signup_page.select_country(context.user_data['country'])
    context.signup_page.enter_state(context.user_data['state'])
    context.signup_page.enter_city(context.user_data['city'])
    context.signup_page.enter_zipcode(context.user_data['zipcode'])
    context.signup_page.enter_mobile_number(context.user_data['mobile'])


@when('I click "Create Account" button')
def step_click_create_account(context):
    context.signup_page = SignupPage(context.driver)
    context.signup_page.click_create_account()
    store_user_credentials(context, context.test_email, context.test_password)


@then('I should see "ACCOUNT CREATED!" message')
def step_verify_account_created(context):
    context.signup_page = SignupPage(context.driver)
    assert context.signup_page.is_account_created_visible(), "Account created message not visible"


@when('I click "Continue" button')
def step_click_continue(context):
    context.signup_page = SignupPage(context.driver)
    context.signup_page.click_continue_button()


@then('I should see "Logged in as {username}" text')
def step_verify_logged_in_as(context, username):
    context.home_page = HomePage(context.driver, context.base_url)
    logged_in_text = context.home_page.get_logged_in_username()
    assert username in logged_in_text or context.test_name in logged_in_text, \
        f"Expected to see '{username}' but got '{logged_in_text}'"


@when('I click "Delete Account" button')
def step_click_delete_account(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_delete_account()


@then('I should see "ACCOUNT DELETED!" message')
def step_verify_account_deleted(context):
    time.sleep(1)
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'ACCOUNT DELETED' in page_text, "Account deleted message not visible"


# TC02: Login with valid credentials
@then('I should see "Login to your account" text')
def step_verify_login_text(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.is_login_form_visible(), "Login form is not visible"


@when('I enter valid email "{email}" and password "{password}"')
def step_enter_valid_credentials(context, email, password):
    context.test_email = email
    context.test_password = password
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_login_email(email)
    context.login_page.enter_login_password(password)
    store_user_credentials(context, email, password)


@when('I click login button')
def step_click_login_button(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_login_button()


# TC03: Login with invalid credentials
@when('I enter invalid email "{email}" and password "{password}"')
def step_enter_invalid_credentials(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_login_email(email)
    context.login_page.enter_login_password(password)


@then('I should see error message "{error_message}"')
def step_verify_error_message(context, error_message):
    context.login_page = LoginPage(context.driver)
    actual_error = context.login_page.get_error_message()
    assert error_message.lower() in actual_error.lower(), \
        f"Expected error '{error_message}' but got '{actual_error}'"


# TC04: Logout User
@given('I am logged in with valid credentials')
def step_login_with_valid_credentials(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.open()
    context.home_page.click_login_link()

    context.login_page = LoginPage(context.driver)
    # Use existing credentials or create new user
    if not hasattr(context, 'test_email'):
        context.test_email = "test@example.com"
        context.test_password = "Test@123"

    context.login_page.enter_login_email(context.test_email)
    context.login_page.enter_login_password(context.test_password)
    context.login_page.click_login_button()
    time.sleep(1)


@when('I click Logout button')
def step_click_logout(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_logout()


@then('I should be navigated to login page')
def step_verify_on_login_page(context):
    current_url = context.driver.current_url
    assert '/login' in current_url, f"Not on login page. Current URL: {current_url}"


# TC05: Register with existing email
@when('I enter name "{name}" and existing email')
def step_enter_existing_email(context, name):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_signup_name(name)
    # Use previously created email
    if hasattr(context, 'test_email'):
        context.login_page.enter_signup_email(context.test_email)
    else:
        context.login_page.enter_signup_email("existing@email.com")


@then('I should see error "Email Address already exist!"')
def step_verify_email_exists_error(context):
    time.sleep(1)
    context.login_page = LoginPage(context.driver)
    error = context.login_page.get_error_message()
    assert 'already exist' in error.lower(), f"Expected email exists error but got: {error}"


# TC06: Contact Us Form
@when('I click on Contact Us button')
def step_click_contact_us(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_contact_us()


@then('I should see "GET IN TOUCH" text')
def step_verify_get_in_touch(context):
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'GET IN TOUCH' in page_text, "GET IN TOUCH text not found"


@when('I enter name "{name}", email "{email}", subject "{subject}" and message "{message}"')
def step_enter_contact_form(context, name, email, subject, message):
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.NAME, 'name').send_keys(name)
    context.driver.find_element(By.NAME, 'email').send_keys(email)
    context.driver.find_element(By.NAME, 'subject').send_keys(subject)
    context.driver.find_element(By.NAME, 'message').send_keys(message)


@when('I upload file')
def step_upload_file(context):
    # Create a dummy file if needed
    import os
    file_path = os.path.join(os.getcwd(), 'test_file.txt')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('Test file content')

    from selenium.webdriver.common.by import By
    context.driver.find_element(By.NAME, 'upload_file').send_keys(file_path)


@when('I click Submit button')
def step_click_submit(context):
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.NAME, 'submit').click()


@when('I click OK button on alert')
def step_accept_alert(context):
    time.sleep(1)
    alert = context.driver.switch_to.alert
    alert.accept()


@then('I should see success message "{message}"')
def step_verify_success_message(context, message):
    time.sleep(1)
    page_text = context.driver.find_element_by_tag_name('body').text
    assert message.lower() in page_text.lower(), f"Expected '{message}' not found"


@when('I click Home button')
def step_click_home(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_home()


# TC07: Verify Test Cases Page
@when('I click on Test Cases button')
def step_click_test_cases(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_test_cases()


@then('I should be navigated to test cases page')
def step_verify_test_cases_page(context):
    current_url = context.driver.current_url
    assert 'test_cases' in current_url, f"Not on test cases page. Current URL: {current_url}"


# TC08: Verify All Products
@when('I click on Products button')
def step_click_products(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_products()
    context.product_page = ProductPage(context.driver)


@then('I should be navigated to ALL PRODUCTS page')
def step_verify_all_products_page(context):
    context.product_page = ProductPage(context.driver)
    assert context.product_page.is_products_page_visible(), "Products page not visible"


@then('I should see the products list')
def step_verify_products_list(context):
    context.product_page = ProductPage(context.driver)
    assert context.product_page.get_products_count() > 0, "No products found"


@when('I click on View Product of first product')
def step_click_first_product(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.click_first_product()


@then('I should be navigated to product detail page')
def step_verify_product_detail_page(context):
    current_url = context.driver.current_url
    assert 'product_details' in current_url, f"Not on product detail page. Current URL: {current_url}"


@then('I should see product details including name, category, price, availability, condition, brand')
def step_verify_product_details(context):
    context.product_page = ProductPage(context.driver)
    assert context.product_page.is_product_name_visible(), "Product name not visible"
    assert context.product_page.is_product_category_visible(), "Product category not visible"
    assert context.product_page.is_product_price_visible(), "Product price not visible"
    assert context.product_page.is_product_availability_visible(), "Product availability not visible"


# TC09: Search Product
@when('I enter product name "{product_name}" in search input')
def step_enter_search_product(context, product_name):
    context.product_page = ProductPage(context.driver)
    context.product_page.enter_search_query(product_name)
    context.search_term = product_name


@when('I click search button')
def step_click_search_button(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.click_search_button()


@then('I should see "SEARCHED PRODUCTS" text')
def step_verify_searched_products_text(context):
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'SEARCHED PRODUCTS' in page_text, "SEARCHED PRODUCTS text not found"


@then('I should see all products related to search')
def step_verify_search_results(context):
    context.product_page = ProductPage(context.driver)
    products_count = context.product_page.get_products_count()
    assert products_count > 0, "No search results found"


# TC10: Verify Subscription in home page
@when('I scroll down to footer')
def step_scroll_to_footer(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.scroll_to_footer()


@then('I should see "SUBSCRIPTION" text')
def step_verify_subscription_text(context):
    context.home_page = HomePage(context.driver, context.base_url)
    assert context.home_page.is_subscription_visible(), "Subscription section not visible"


@when('I enter email "{email}" in subscription input')
def step_enter_subscription_email(context, email):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.enter_subscription_email(email)


@when('I click arrow button')
def step_click_subscription_arrow(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_subscription_button()


@then('I should see success message "You have been successfully subscribed!"')
def step_verify_subscription_success(context):
    time.sleep(1)
    context.home_page = HomePage(context.driver, context.base_url)
    assert context.home_page.is_subscription_success_visible(), "Subscription success not visible"


# TC11: Verify Subscription in Cart page
@when('I click Cart button')
def step_click_cart(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_cart()
    context.cart_page = CartPage(context.driver)


# TC12: Add Products in Cart
@when('I hover over first product and click Add to cart')
def step_add_first_product_to_cart(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.hover_and_add_first_product()


@when('I click Continue Shopping button')
def step_click_continue_shopping(context):
    time.sleep(1)
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Continue Shopping')]").click()


@when('I hover over second product and click Add to cart')
def step_add_second_product_to_cart(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.hover_and_add_second_product()


@when('I click View Cart button')
def step_click_view_cart(context):
    time.sleep(1)
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    context.cart_page = CartPage(context.driver)


@then('I should see both products in cart')
def step_verify_both_products_in_cart(context):
    context.cart_page = CartPage(context.driver)
    cart_items = context.cart_page.get_cart_items_count()
    assert cart_items >= 2, f"Expected at least 2 products but found {cart_items}"


@then('I should see product prices, quantities and total price')
def step_verify_cart_details(context):
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.are_prices_visible(), "Product prices not visible"
    assert context.cart_page.are_quantities_visible(), "Product quantities not visible"
    assert context.cart_page.is_total_visible(), "Total price not visible"


# TC13: Verify Product quantity in Cart
@when('I click View Product for any product on home page')
def step_click_view_any_product(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_first_product_view()


@when('I increase quantity to {quantity:d}')
def step_increase_quantity(context, quantity):
    context.product_page = ProductPage(context.driver)
    context.product_page.set_quantity(quantity)
    context.expected_quantity = quantity


@when('I click Add to cart button')
def step_click_add_to_cart(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.click_add_to_cart()


@then('I should see product with quantity {quantity:d}')
def step_verify_product_quantity(context, quantity):
    context.cart_page = CartPage(context.driver)
    actual_quantity = context.cart_page.get_first_product_quantity()
    assert int(actual_quantity) == quantity, \
        f"Expected quantity {quantity} but got {actual_quantity}"


# TC14: Place Order - Register while Checkout
@when('I add products to cart')
def step_add_products_to_cart(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.hover_and_add_first_product()
    time.sleep(1)
    context.home_page.click_continue_shopping_modal()
    time.sleep(1)


@when('I click Proceed To Checkout button')
def step_click_proceed_to_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_proceed_to_checkout()


@when('I click Register / Login button in modal')
def step_click_register_login_modal(context):
    time.sleep(1)
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.XPATH, "//u[text()='Register / Login']").click()


@when('I fill all details in Signup and create account')
def step_create_account_full(context):
    # Signup
    context.test_name = "Test User"
    context.test_email = generate_random_email()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_signup_name(context.test_name)
    context.login_page.enter_signup_email(context.test_email)
    context.login_page.click_signup_button()

    # Fill account details
    context.user_data = generate_user_data()
    context.user_data['email'] = context.test_email
    context.test_password = context.user_data['password']

    context.signup_page = SignupPage(context.driver)
    context.signup_page.select_title(context.user_data['title'])
    context.signup_page.enter_password(context.user_data['password'])
    context.signup_page.select_date_of_birth(
        context.user_data['birth_date'],
        context.user_data['birth_month'],
        context.user_data['birth_year']
    )
    context.signup_page.enter_first_name(context.user_data['first_name'])
    context.signup_page.enter_last_name(context.user_data['last_name'])
    context.signup_page.enter_company(context.user_data['company'])
    context.signup_page.enter_address1(context.user_data['address'])
    context.signup_page.enter_address2(context.user_data['address2'])
    context.signup_page.select_country(context.user_data['country'])
    context.signup_page.enter_state(context.user_data['state'])
    context.signup_page.enter_city(context.user_data['city'])
    context.signup_page.enter_zipcode(context.user_data['zipcode'])
    context.signup_page.enter_mobile_number(context.user_data['mobile'])
    context.signup_page.click_create_account()

    # Click Continue
    time.sleep(2)
    context.signup_page.click_continue_button()


@then('I should see address details and review order')
def step_verify_address_and_review(context):
    context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_address_visible(), "Address not visible"
    assert context.checkout_page.is_review_visible(), "Review section not visible"


@when('I enter description "{description}" in comment area')
def step_enter_comment(context, description):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.enter_comment(description)


@when('I click Place Order button')
def step_click_place_order(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.click_place_order()


@when('I enter payment details: name "{name}", card "{card}", cvc "{cvc}", expiry "{expiry}"')
def step_enter_payment_details(context, name, card, cvc, expiry):
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.NAME, 'name_on_card').send_keys(name)
    context.driver.find_element(By.NAME, 'card_number').send_keys(card)
    context.driver.find_element(By.NAME, 'cvc').send_keys(cvc)
    context.driver.find_element(By.NAME, 'expiry_month').send_keys(expiry.split('/')[0])
    context.driver.find_element(By.NAME, 'expiry_year').send_keys(expiry.split('/')[1])


@when('I click Pay and Confirm Order button')
def step_click_pay_confirm(context):
    from selenium.webdriver.common.by import By
    context.driver.find_element(By.ID, 'submit').click()


@then('I should see success message "Your order has been placed successfully!"')
def step_verify_order_success(context):
    time.sleep(2)
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'order has been placed' in page_text.lower() or 'congratulations' in page_text.lower(), \
        "Order success message not found"


# TC15-16: Checkout with different scenarios covered above

# TC17: Remove Product from Cart
@when('I click X button corresponding to a product')
def step_remove_product_from_cart(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.remove_first_product()


@then('product should be removed from cart')
def step_verify_product_removed(context):
    time.sleep(1)
    context.cart_page = CartPage(context.driver)
    # Cart should be empty or have fewer items
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'empty' in page_text.lower() or context.cart_page.get_cart_items_count() == 0


# TC18: View Category Products
@then('I should see category list on left sidebar')
def step_verify_category_sidebar(context):
    context.home_page = HomePage(context.driver, context.base_url)
    assert context.home_page.is_category_sidebar_visible(), "Category sidebar not visible"


@when('I click on {category} category')
def step_click_category(context, category):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_category(category)


@when('I click on any sub-category link under {category}')
def step_click_subcategory(context, category):
    time.sleep(1)
    context.category_page = CategoryPage(context.driver)
    context.category_page.click_first_subcategory()


@then('I should see category page and products')
def step_verify_category_page(context):
    context.category_page = CategoryPage(context.driver)
    assert context.category_page.are_products_visible(), "Category products not visible"


# TC19: View Brand Products
@then('I should see brands list on left sidebar')
def step_verify_brands_sidebar(context):
    context.home_page = HomePage(context.driver, context.base_url)
    assert context.home_page.is_brands_sidebar_visible(), "Brands sidebar not visible"


@when('I click on any brand name')
def step_click_brand(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.click_first_brand()
    context.brand_page = BrandPage(context.driver)


@then('I should be navigated to brand page')
def step_verify_brand_page(context):
    context.brand_page = BrandPage(context.driver)
    assert context.brand_page.are_products_visible(), "Brand products not visible"


@when('I click on another brand')
def step_click_another_brand(context):
    context.brand_page = BrandPage(context.driver)
    context.brand_page.click_another_brand()


# TC20: Search Products and Verify Cart After Login
@when('I add those products to cart')
def step_add_searched_products(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_first_product_to_cart()
    time.sleep(1)


@then('I should see those products in cart after login')
def step_verify_products_after_login(context):
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.get_cart_items_count() > 0, "Cart is empty after login"


# TC21: Add review on product
@when('I write review with name "{name}", email "{email}" and review "{review}"')
def step_write_review(context, name, email, review):
    context.product_page = ProductPage(context.driver)
    context.product_page.enter_review_name(name)
    context.product_page.enter_review_email(email)
    context.product_page.enter_review_text(review)


@when('I click Submit review button')
def step_submit_review(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.click_submit_review()


@then('I should see success message "Thank you for your review."')
def step_verify_review_success(context):
    time.sleep(1)
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'thank you for your review' in page_text.lower(), "Review success message not found"


# TC22: Add to cart from Recommended items
@when('I scroll to bottom of page')
def step_scroll_to_bottom(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.scroll_to_bottom()


@then('I should see "RECOMMENDED ITEMS" text')
def step_verify_recommended_items(context):
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'RECOMMENDED ITEMS' in page_text, "RECOMMENDED ITEMS text not found"


@when('I click Add To Cart on recommended product')
def step_add_recommended_product(context):
    time.sleep(1)
    from selenium.webdriver.common.by import By
    recommended_section = context.driver.find_element(By.CLASS_NAME, 'recommended_items')
    add_button = recommended_section.find_element(By.XPATH, ".//a[contains(@class,'add-to-cart')]")
    context.driver.execute_script("arguments[0].click();", add_button)


@then('product should be displayed in cart')
def step_verify_recommended_in_cart(context):
    time.sleep(1)
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.get_cart_items_count() > 0, "No products in cart"


# TC23: Verify address details in checkout page
@then('I should see delivery address matches registration details')
def step_verify_delivery_address(context):
    context.checkout_page = CheckoutPage(context.driver)
    delivery_address = context.checkout_page.get_delivery_address()
    assert context.user_data['first_name'] in delivery_address or \
           context.user_data['address'] in delivery_address, \
        "Delivery address doesn't match registration details"


@then('I should see billing address matches registration details')
def step_verify_billing_address(context):
    context.checkout_page = CheckoutPage(context.driver)
    billing_address = context.checkout_page.get_billing_address()
    assert context.user_data['first_name'] in billing_address or \
           context.user_data['address'] in billing_address, \
        "Billing address doesn't match registration details"


# TC24: Download Invoice after purchase order
@when('I click Download Invoice button')
def step_download_invoice(context):
    from selenium.webdriver.common.by import By
    time.sleep(1)
    context.driver.find_element(By.LINK_TEXT, 'Download Invoice').click()


@then('invoice should be downloaded successfully')
def step_verify_invoice_downloaded(context):
    time.sleep(2)
    import os
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    files = os.listdir(downloads_path)
    invoice_files = [f for f in files if 'invoice' in f.lower()]
    assert len(invoice_files) > 0, "Invoice file not found in downloads"


# TC25-26: Scroll and arrow button
@then('page should be scrolled up')
def step_verify_scrolled_up(context):
    scroll_position = context.driver.execute_script("return window.pageYOffset;")
    assert scroll_position < 100, f"Page not scrolled to top. Position: {scroll_position}"


@then('I should see "Full-Fledged practice website" text')
def step_verify_full_fledged_text(context):
    page_text = context.driver.find_element_by_tag_name('body').text
    assert 'Full-Fledged practice website' in page_text or 'automation' in page_text.lower(), \
        "Expected text not found at top"


@when('I scroll up page to top')
def step_scroll_up_manually(context):
    context.home_page = HomePage(context.driver, context.base_url)
    context.home_page.scroll_to_top()


@when('I click on arrow at bottom right to move upward')
def step_click_scroll_arrow(context):
    from selenium.webdriver.common.by import By
    time.sleep(1)
    arrow = context.driver.find_element(By.ID, 'scrollUp')
    context.driver.execute_script("arguments[0].click();", arrow)