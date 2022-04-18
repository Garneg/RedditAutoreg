import random
import string


def generate_name() -> str:
    name_length = random.randint(10, 20)
    generated_name = str().join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=name_length))
    return generated_name


def generate_password() -> str:
    password_length = random.randint(8, 18)
    generated_password = str().join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=password_length))
    return generated_password


def generate_email() -> str:
    generated_email = str().join(random.choices(string.ascii_lowercase, k=10)) + '@gmail.com'
    return generated_email
