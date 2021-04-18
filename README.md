# Testes Automatizados para a api OpenWeather

Neste projeto são feitas automações de testes para a api pública OpenWeather

Você encontra nesse projeto:

- Framworks:
    - Pystest
    - Requests

- Features:
    - Pytest fixtures e parametrize
    - Data drive testes
    - Funções de ajuda
    - teste de contrato com Json Schema
    - Relatório com Allure
    - Lint de código com Pylint
    
## Requesitos
- Python >= 3.6 - [Como instalar o Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [Como instalar o pip](https://pip.pypa.io/en/stable/installing/)
- Docker >= 18.09 - [Como instalar o Docker](https://docs.docker.com/get-docker/)
- Allure Cliente >= 2.0- [Como instalar o cliente allure com npm](https://www.npmjs.com/package/allure-commandline)

## iniciando
Instalar as dependências com o comando:

```bash
$ pip3 install --no-cache-dir -r requirements.txt
```

## Config
Exportar o endereço da api e o appid para variáveis de ambiente:

```bash
$ export BASE_URL=https://api.openweathermap.org/
$ export APPID=<SUA_CHAVE_AQUI>
```

## Para executar os testes:
```bash
$ pytest -vv -p no:cacheprovider --alluredir=./reports/allure_results
```

> No arquivo pytest.ini está configorado para que o pytest considere como um teste qualquer arquivo, classe ou função cujo nome termine com 'test',
>para alterar isto delete o arquivo pystest.ini ou edite o seu conteúdo.
 
## Relatórios
> Você deve ter o allure client e o node instalados.

Executar o comando abaixo para gerar o relatório:

```bash
$ npx allure generate --clean ./reports/allure_results/ -o ./reports/allure-report
```

Para visualizar o relatório no seu navegador:

```bash
$ npx allure open ./reports/allure-report/
```

## Lint do código
Para fazer o lint do código:

```bash
$ pylint *
```