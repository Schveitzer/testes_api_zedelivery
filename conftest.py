import os
from http import HTTPStatus
import requests
import pytest
from helpers.read_data_from_file import read_test_data_from_json


@pytest.fixture(scope="session", autouse=True)
def get_base_url():
    base_url = os.getenv("BASE_URL")
    yield base_url


@pytest.fixture(scope="session", autouse=True)
def get_client():
    def _client(user_type):
        token = get_token(user_type)
        client = requests.Session()
        client.headers.update({'Authorization': token})
        return client

    return _client


def get_token(user_type):
    user = read_test_data_from_json('config/credentials.json')
    response = requests.post(os.getenv("BASE_URL") + 'auth/login', data={
        "email": user[user_type]['email'],
        "password": user[user_type]['password']
    })

    # Checks if the login was successful, if not the tests are aborted
    if response.status_code != HTTPStatus.OK:
        pytest.exit("Aborted tests, unable to log in with get_token() function."
                    " Verify that the credential information in the credentials file is correct,"
                    " or if the login endpoint is working")

    response = response.json()
    return str("Bearer " + response["access_token"])
