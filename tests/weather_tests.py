from http import HTTPStatus
import pytest
import allure
import requests

from helpers.read_data_from_file import read_test_data_from_json
from helpers.validate_json_schema import validate_json


@allure.suite('Validações nos endpoints weather da api pública openweathermap ')
class WeatherTests:

    # A implementação dos métodos get_base_url, get_appid que são passados como fixtures podem ser vistas no arquivo conftest.py na raiz do projeto.
    @pytest.fixture(autouse=True)
    def setup(self, get_base_url, get_appid):
        self.base_url = get_base_url
        self.appid = get_appid
        self.endpoint = 'data/2.5/weather'
        self.url = str(self.base_url + self.endpoint)

    @allure.title('GET WEATHER - Valida se o status code está retornando corretamente quando efetuado um get pelo nome da cidade')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_pela_cidade_test(self):
        parametros = {'q': 'London,uk', 'appid': self.appid}
        response = requests.get(self.url, parametros)

        assert response.status_code == HTTPStatus.OK

    @allure.title('GET WEATHER - Valida se o status code está retornando corretamente quando efetuado um get pelo ID da cidade')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_pelo_id_test(self):
        parametros = {'id': '2172797', 'appid': self.appid}
        response = requests.get(self.url, parametros)

        assert response.status_code == HTTPStatus.OK

    @allure.title('GET WEATHER - Valida se o status code está retornando corretamente quando efetuado um get pelas coordenadas da cidade')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_pelas_coordenadas_test(self):
        parametros = {'lat': '51.5085', 'lon': '0.1257', 'appid': self.appid}
        response = requests.get(self.url, parametros)

        assert response.status_code == HTTPStatus.OK

    @allure.title('GET WEATHER - Valida se o status code está retornando corretamente quando efetuado um get pelo código postal da cidade')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_pelo_cod_postal_test(self):
        parametros = {'zip': '94040', 'appid': self.appid}
        response = requests.get(self.url, parametros)

        assert response.status_code == HTTPStatus.OK

    @allure.title('GET WEATHER - Valida se as cordenadas tazidas no retorno estão corretas')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_coord_test(self):
        parametros = {'q': 'London,uk', 'appid': self.appid}
        response = requests.get(self.url, parametros)
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_body["coord"]["lon"] == -0.1257
        assert response_body["coord"]["lat"] == 51.5085

    @allure.title('GET WEATHER - Valida o contrato da api para um get informando uma cidade')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_contract_test(self):
        parametros = {'q': 'London,uk', 'appid': self.appid}
        response = requests.get(self.url, parametros)
        base_schema = read_test_data_from_json('schema_weather_cidade.json')
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert validate_json(response_body, base_schema)

    @allure.title('GET WEATHER - Valida o código e o retorno quando efetuado um get sem informar nenhum parâmetro')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_retorno_mensagem_test(self):
        parametros = {'?': '', 'appid': self.appid}
        response = requests.get(self.url, parametros)
        response_body = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response_body['cod'] == '400'
        assert response_body['message'] == 'Nothing to geocode'

    @allure.title('GET WEATHER - Valida o código e o retorno quando efetuado um get informando um appid inválido')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_appid_invalido_test(self):
        parametros = {'q': 'London,uk&', 'appid': '45345345345345'}
        response = requests.get(self.url, parametros)
        response_body = response.json()

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response_body['cod'] == 401
        assert response_body['message'] == 'Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.'

    @allure.title('GET WEATHER - Valida o código e o retorno quando efetuado um get informando uma cidade que não existe')
    @allure.severity(allure.severity_level.NORMAL)
    def weather_get_cidade_inexistente_test(self):
        parametros = {'q': 'Londo,uk', 'appid': self.appid}
        response = requests.get(self.url, parametros)
        response_body = response.json()

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response_body['cod'] == '404'
        assert response_body['message'] == 'city not found'
