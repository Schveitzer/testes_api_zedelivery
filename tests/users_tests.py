from http import HTTPStatus
import pytest
import allure
from helpers.read_data_from_file import read_test_data_from_json, read_test_data_from_json_tuple
from helpers.object_helper import ObjectHelper
from helpers.validate_json_schema import validate_json


@allure.suite('Validações no endpoint de Usuários')
class UsersTests:

    TEST_DATA_IDS_NAMES = read_test_data_from_json_tuple('users_ids_names_gender.json')

    # Setup use the client() function and baseUrl located in the conftest.py file
    # informing a user type, log in and sets the authorization in header, the credentials.json file contains
    # data for the type of user informed.
    @pytest.fixture(autouse=True)
    def setup(self, get_client, get_base_url):
        self.client = get_client(user_type='User 1')
        self.base_url = get_base_url
        self.endpoint = 'users/'
        self.url = str(self.base_url + self.endpoint)
        self.keys_to_remove = ['id']

    @allure.title('Valida get para o usuário com id 1')
    @allure.severity(allure.severity_level.NORMAL)
    def get_user_test(self):
        user_id = '1'
        file_to_compare = read_test_data_from_json('user_1.json')
        response = self.client.get(self.url + user_id)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body == file_to_compare

    # Parameterized test that validates the name, age and gender for ids contained in the
    # users_ids_names_gender.json
    @pytest.mark.parametrize("user_id, expected_name, expected_gender", TEST_DATA_IDS_NAMES)
    @allure.title('Valida informações do get no endpoint users com os dados:')
    @allure.severity(allure.severity_level.CRITICAL)
    def get_users_test(self, user_id, expected_name, expected_gender):
        response = self.client.get(self.url + user_id)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body["name"] == expected_name
        assert response_body["gender"] == expected_gender

    @allure.title('Valida o schema do json para get no endpoint users')
    @allure.severity(allure.severity_level.NORMAL)
    def get_user_schema_validation_test(self):
        user_id = '1'
        schema = read_test_data_from_json('schema_user_1.json')
        response = self.client.get(self.url + user_id)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert validate_json(response_body, schema)

    @allure.title('Valida informações do get no edpoint users com o filtro: page=1 limit=2')
    @allure.severity(allure.severity_level.NORMAL)
    def get_user_with_filter_test(self):
        filter_data = '?_page=1&_limit=2'
        file_to_compare = read_test_data_from_json('user_2.json')
        response = self.client.get(self.url + filter_data)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body == file_to_compare

    @allure.title('Valida cadastro de um usuário com post no edpoint')
    @allure.severity(allure.severity_level.NORMAL)
    def post_new_user(self):
        file_to_post = read_test_data_from_json('user_3.json')
        response = self.client.post(self.url, file_to_post)
        response_body = response.json()

        # Remove dinamic keys from response for comparation
        response = ObjectHelper.remove_keys(response_body, self.keys_to_remove)

        assert response.status_code == HTTPStatus.CREATED
        assert response_body == file_to_post
