from http import HTTPStatus
import pytest
import allure
import requests

from helpers.read_data_from_file import read_test_data_from_json
from helpers.validate_json_schema import validate_json


@allure.suite('Validações nos endpoints box da api pública openweathermap ')
class BoxTests:
    # A implementação dos métodos get_base_url, get_appid que são passados como fixtures podem ser vistas no arquivo conftest.py na raiz do projeto.
    @pytest.fixture(autouse=True)
    def setup(self, get_base_url, get_appid):
        self.base_url = get_base_url
        self.appid = '&appid='+get_appid
        self.endpoint = 'data/2.5/box/city'
        self.url = str(self.base_url + self.endpoint)

    @allure.title('GET BOX - Valida se o status code está retornando corretamente quando efetuado um get com dados válidos')
    @allure.severity(allure.severity_level.NORMAL)
    def box_get_pela_cidade_test(self):
        parametros = '?bbox=12,32,15,37,10'+self.appid
        response = requests.get(self.url + parametros)

        assert response.status_code == HTTPStatus.OK

    @allure.title('GET BOX - Valida o contrato da api para um get informando coordenadas corretas')
    @allure.severity(allure.severity_level.NORMAL)
    def box_get_contract_test(self):
        parametros = '?bbox=12,32,15,37,10'+self.appid
        response = requests.get(self.url + parametros)
        base_schema = read_test_data_from_json('schema_box_cordenadas.json')
        response_body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert validate_json(response_body, base_schema)

    @allure.title('GET WEATHER - Valida o código de retorno quando efetuado um get com uma área maior que a permitida')
    @allure.severity(allure.severity_level.NORMAL)
    def box_get_retorno_test(self):
        parametros = '?bbox=12,32,15o,37,10'+self.appid
        response = requests.get(self.url + parametros)
        response_body = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response_body['cod'] == '400'
