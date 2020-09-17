from http import HTTPStatus
import allure
import pytest
from helpers.object_helper import ObjectHelper


@allure.suite('Validations on Comments endpoint')
class CommentsTests:

    # Fixture that configures standard requests using the client() function and baseUrl in the conftest.py
    # file informing a user type, log in and sets the authorization in header,
    # the credentials.json file contains data for the type of user informed.
    @pytest.fixture(autouse=True)
    def setup(self, get_client, get_base_url):
        self.client = get_client(user_type='User 1')
        self.base_url = get_base_url
        self.endpoint = 'comments/'
        self.url = str(self.base_url + self.endpoint)
        self.keys_to_remove = ['id']

    @allure.title('Validates get to comment with id 1')
    @allure.severity(allure.severity_level.NORMAL)
    def get_comment_test(self):
        comment_id = '1'
        response = self.client.get(self.url + comment_id)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body == {
            'articleId': 1,
            'body': 'Brilliant',
            'id': 1,
        }

    @allure.title('Validates registration of a new comment using post')
    @allure.severity(allure.severity_level.NORMAL)
    def post_comment_test(self):
        data = {
            'body': 'Brilliant',
            'articleId': 1,
        }
        response = self.client.post(self.url, data)
        response_body = response.json()

        assert response.status_code == HTTPStatus.CREATED

        # Remove dinamic key id from response for comparation
        response_body = ObjectHelper.remove_keys(response_body, self.keys_to_remove)

        assert response_body == {'body': 'Brilliant', 'articleId': '1'}

    @allure.title('Validates update of a comment using patch')
    @allure.severity(allure.severity_level.NORMAL)
    def patch_comment_test(self):
        comment_id = '10'
        data = {'body': 'Update with PATCH'}
        response = self.client.patch(self.url + comment_id, data)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body == {
            'id': 10,
            'body': 'Update with PATCH',
            'articleId': 1,
        }

    @allure.title('Validates deletion of a comment using delete')
    @allure.severity(allure.severity_level.NORMAL)
    def delete_comment_test(self):
        data = {
            'body': 'Brilliant',
            'articleId': 1,
        }
        response_post = self.client.post(self.url, data)
        response_body = response_post.json()
        assert response_post.status_code == HTTPStatus.CREATED

        comment_id = str(response_body['id'])
        response_delete = self.client.delete(self.url + comment_id)
        assert response_delete.status_code == HTTPStatus.OK
