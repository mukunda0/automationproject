from behave import given, when, then
from api.client import APIClient
from api.endpoints import fileEndpoints
from features.steps.helpers import generate_random_email, generate_user_data
import json


@given('I have API client initialized')
def step_init_api_client(context):
    context.api_client = APIClient(context.api_base_url)
    context.test_data = {}


@when('I send GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    context.response = context.api_client.get(endpoint)


@when('I send POST request to "{endpoint}"')
def step_send_post_request(context, endpoint):
    context.response = context.api_client.post(endpoint)


@when('I send PUT request to "{endpoint}"')
def step_send_put_request(context, endpoint):
    context.response = context.api_client.put(endpoint)


@when('I send DELETE request to "{endpoint}"')
def step_send_delete_request(context, endpoint):
    context.response = context.api_client.delete(endpoint)


@when('I send POST request to "{endpoint}" with search parameter "{search_term}"')
def step_post_search_product(context, endpoint, search_term):
    data = {'search_product': search_term}
    context.response = context.api_client.post(endpoint, data=data)


@when('I send POST request to "{endpoint}" without search parameter')
def step_post_without_search_param(context, endpoint):
    context.response = context.api_client.post(endpoint, data={})


@when('I send POST request to "{endpoint}" with valid credentials')
def step_post_valid_login(context, endpoint):
    # Use previously created user or create new one
    if not hasattr(context, 'test_user_email'):
        context.test_user_email = generate_random_email()
        context.test_user_password = "Test@123"

    data = {
        'email': context.test_user_email,
        'password': context.test_user_password
    }
    context.response = context.api_client.post(endpoint, data=data)


@when('I send POST request to "{endpoint}" with invalid credentials')
def step_post_invalid_login(context, endpoint):
    data = {
        'email': 'invalid@email.com',
        'password': 'WrongPassword123'
    }
    context.response = context.api_client.post(endpoint, data=data)


@when('I send POST request to "{endpoint}" without email parameter')
def step_post_without_email(context, endpoint):
    data = {'password': 'Test@123'}
    context.response = context.api_client.post(endpoint, data=data)


@when('I send POST request to "{endpoint}" with user registration data')
def step_post_register_user(context, endpoint):
    user_data = generate_user_data()
    context.test_user_email = user_data['email']
    context.test_user_password = user_data['password']

    data = {
        'name': user_data['name'],
        'email': user_data['email'],
        'password': user_data['password'],
        'title': user_data['title'],
        'birth_date': user_data['birth_date'],
        'birth_month': user_data['birth_month'],
        'birth_year': user_data['birth_year'],
        'firstname': user_data['first_name'],
        'lastname': user_data['last_name'],
        'company': user_data['company'],
        'address1': user_data['address'],
        'address2': user_data['address2'],
        'country': user_data['country'],
        'zipcode': user_data['zipcode'],
        'state': user_data['state'],
        'city': user_data['city'],
        'mobile_number': user_data['mobile']
    }
    context.response = context.api_client.post(endpoint, data=data)


@when('I send DELETE request to "{endpoint}" with user credentials')
def step_delete_user_account(context, endpoint):
    data = {
        'email': context.test_user_email,
        'password': context.test_user_password
    }
    context.response = context.api_client.delete(endpoint, data=data)


@when('I send PUT request to "{endpoint}" with updated user data')
def step_put_update_user(context, endpoint):
    updated_data = {
        'name': 'Updated Name',
        'email': context.test_user_email,
        'password': context.test_user_password,
        'title': 'Mr',
        'birth_date': '15',
        'birth_month': 'May',
        'birth_year': '1990',
        'firstname': 'Updated',
        'lastname': 'User',
        'company': 'Updated Company',
        'address1': 'Updated Address 1',
        'address2': 'Updated Address 2',
        'country': 'India',
        'zipcode': '123456',
        'state': 'Updated State',
        'city': 'Updated City',
        'mobile_number': '9999999999'
    }
    context.response = context.api_client.put(endpoint, data=updated_data)


@when('I send POST request to "{endpoint}" with email parameter')
def step_get_user_by_email(context, endpoint):
    data = {'email': context.test_user_email}
    context.response = context.api_client.post(endpoint, data=data)


@then('the response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    actual_status = context.api_client.get_status_code()
    assert actual_status == status_code, \
        f"Expected status code {status_code}, but got {actual_status}"


@then('the response should contain "{key}" with value "{value}"')
def step_verify_response_contains_key_value(context, key, value):
    response_json = context.api_client.get_response_json()
    assert key in response_json, f"Response does not contain key: {key}"

    actual_value = str(response_json[key])
    assert actual_value == value, \
        f"Expected {key}={value}, but got {key}={actual_value}"


@then('the response should contain "{key}"')
def step_verify_response_contains_key(context, key):
    response_json = context.api_client.get_response_json()
    assert key in response_json, f"Response does not contain key: {key}"


@then('the response should contain products list')
def step_verify_products_list(context):
    response_json = context.api_client.get_response_json()
    assert 'products' in response_json, "Response does not contain products"
    assert len(response_json['products']) > 0, "Products list is empty"


@then('the response should contain brands list')
def step_verify_brands_list(context):
    response_json = context.api_client.get_response_json()
    assert 'brands' in response_json, "Response does not contain brands"
    assert len(response_json['brands']) > 0, "Brands list is empty"


@then('the response should contain searched products')
def step_verify_searched_products(context):
    response_json = context.api_client.get_response_json()
    assert 'products' in response_json, "Response does not contain products"


@then('the response message should be "{expected_message}"')
def step_verify_response_message(context, expected_message):
    response_json = context.api_client.get_response_json()

    if 'message' in response_json:
        actual_message = response_json['message']
        assert expected_message.lower() in actual_message.lower(), \
            f"Expected message '{expected_message}', but got '{actual_message}'"
    elif 'responseCode' in response_json and response_json['responseCode'] == 405:
        assert expected_message.lower() in "method not supported", \
            f"Expected message '{expected_message}' for 405 response"


@then('the response should indicate method not allowed')
def step_verify_method_not_allowed(context):
    response_json = context.api_client.get_response_json()
    response_code = response_json.get('responseCode', 0)
    assert response_code == 405, f"Expected responseCode 405, but got {response_code}"


@then('the response should indicate user created')
def step_verify_user_created(context):
    response_json = context.api_client.get_response_json()
    response_code = response_json.get('responseCode', 0)
    assert response_code in [200, 201], \
        f"Expected responseCode 200 or 201, but got {response_code}"


@then('the response should indicate account deleted')
def step_verify_account_deleted(context):
    response_json = context.api_client.get_response_json()
    response_code = response_json.get('responseCode', 0)
    assert response_code == 200, f"Expected responseCode 200, but got {response_code}"


@then('the response should contain user details')
def step_verify_user_details(context):
    response_json = context.api_client.get_response_json()
    assert 'user' in response_json, "Response does not contain user details"