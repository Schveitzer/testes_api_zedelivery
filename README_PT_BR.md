# Testes de Api com Python e Pytest

Neste projeto demonstro como automatizar testes para api´s usando a linguagem Python com o Pytest e Requests



Você encontra nesse prjeto:

- Framworks:
    - Pystest
    - Requests

- Features:
    - Testes em api com autenticação via token JWT
    - Pytest fixtures e parametrize
    - Data drive testes
    - Funções de ajuda
    - Cliente http padrão para todos os testes
    - Validação de Json Schema
    - Page Object Pattern
    - Relatório com Allure
    - Lint de código com Pylint
    - Execução simples com docker e makefile
    
## API
Para estes testes eu utilizei uma api local, ela pode ser encontrada aqui: [Simple jwt local api](https://github.com/Schveitzer/simple-api-jwt-server)
    
## Requesitos
- Python >= 3.6 - [Como instalar o Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [Como instalar o pip](https://pip.pypa.io/en/stable/installing/)
- Docker >= 18.09 - [Como instalar o Docker](https://docs.docker.com/get-docker/)
- Allure Cliente >= 2.9 [Como instalar o cliente allure](https://docs.qameta.io/allure/#_commandline)


## iniciando
Instalar as dependências com o comando:

```bash
$ pip install --no-cache-dir -r requirements.txt
```

## Config
Exportar o endereço da api para a variavel de ambiente BASE_URL, no caso deste projeto:

```bash
$ export BASE_URL=http://localhost:3000/
```

## Para executar os testes:
```bash
$ pytest -vv -p no:cacheprovider --alluredir=./reports/allure_results
```

> No arquivo pytest.ini está configorado para que o pytest considere como um teste qualquer arquivo, classe ou função cujo nome temrine com 'test',
>para alterar isto delete o arquivo pystest.ini ou edite o seu conteúdo.
 
## Relatórios
> Você deve ter o allure client instalado.

Execute o comando abaixo para gerar o relatório:

```bash
$ allure generate --clean ./reports/allure_results/ -o ./reports/allure-report
```

Para visualizar o relatório no seu navegador:

```bash
$ allure open ./reports/allure-report/
```

## Lint do código
Para fazer o lint do código:

```bash
$ pylint *
```
## Execução com  Docker

Para executar os testes com docker:

```bash
$ export BASE_URL=http://localhost:3000/
```
build a imagem:
```bash
$ make -i build
```
Execute os testes:
```bash
$ make test
```

Para copiar os arquivos do relatório que foram gerados para a pasta local reports:

```bash
$ make report.get
```
Para gerar o relatório:

> Você deve ter o allure client instalado.

Execute o comando abaixo para gerar o relatório:

```bash
$ allure generate --clean ./reports/allure_results/ -o ./reports/allure-report
```

Para visualizar o relatório no seu navegador:

```bash
$ allure open ./reports/allure-report/
```
