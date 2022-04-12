import string
import secrets


def get_token():

    #alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(string.digits) for i in range(6))
    return password
