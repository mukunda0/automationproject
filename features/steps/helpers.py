from faker import Faker
import random
import string
import json
import os

fake = Faker()


def generate_random_email():
    """Generate random email"""
    return f"test_{random.randint(1000, 9999)}_{fake.email()}"


def generate_random_string(length=10):
    """Generate random string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_user_data():
    """Generate complete user registration data"""
    return {
        'name': fake.name(),
        'email': generate_random_email(),
        'password': 'Test@123',
        'title': random.choice(['Mr', 'Mrs']),
        'birth_date': str(random.randint(1, 28)),
        'birth_month': random.choice(['January', 'February', 'March', 'April', 'May', 'June',
                                      'July', 'August', 'September', 'October', 'November', 'December']),
        'birth_year': str(random.randint(1970, 2000)),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'company': fake.company(),
        'address': fake.street_address(),
        'address2': fake.secondary_address(),
        'country': 'India',
        'state': fake.state(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'mobile': fake.phone_number()
    }


def load_test_data(filename):
    """Load test data from JSON file"""
    data_path = os.path.join('data', filename)
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            return json.load(f)
    return {}


def save_test_data(filename, data):
    """Save test data to JSON file"""
    data_path = os.path.join('data', filename)
    os.makedirs('data', exist_ok=True)
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2)


def get_product_by_id(product_id):
    """Get product details by ID"""
    products = load_test_data('products.json')
    return products.get(str(product_id), {})


def get_brand_by_id(brand_id):
    """Get brand details by ID"""
    brands = load_test_data('brands.json')
    return brands.get(str(brand_id), {})


def store_user_credentials(context, email, password):
    """Store user credentials in context"""
    if not hasattr(context, 'users'):
        context.users = {}
    context.users[email] = {
        'email': email,
        'password': password
    }


def get_user_credentials(context, email):
    """Get stored user credentials"""
    if hasattr(context, 'users') and email in context.users:
        return context.users[email]
    return None