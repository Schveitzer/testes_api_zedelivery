# Api tests Python Pytest
#### [Para ver o projeto em português clique aqui](https://github.com/Schveitzer/api-tests-python-pytest/blob/master/README_PT_BR.md)

In this project I demonstrate how to use Python with Pytest and Requests for automation api tests.

This project includes:

- Framworks:
    - Pystest
    - Requests

- Features:
    - Tests with JWT Api Authentication
    - Pytest fixtures and parametrize
    - Data drive tests
    - Help functions
    - Dafault http client for all tests
    - Json Schema validation
    - Page Object Pattern
    - Report with Allure
    - Code lint with Pylint
    - Simple docker commands with Make
    
## API
For this tests i use a local api which can be found here: [Simple jwt local api](https://github.com/Schveitzer/simple-api-jwt-server)

## Requirements
- Python >= 3.6 - [How install Pytohn](https://www.python.org/downloads/)
- Pip >= 20.0.x - [How install pip](https://pip.pypa.io/en/stable/installing/)
- Docker >= 18.09 - [How install Docker](https://docs.docker.com/get-docker/)
- Allure Cliente >= 2.9 [How install allure client](https://docs.qameta.io/allure/#_commandline)

## Getting Started
Install dependencies:

```bash
$ pip install --no-cache-dir -r requirements.txt
```

## Config
Export your api adress to BASE_URL variable, for this project:

```bash
$ export BASE_URL=http://localhost:3000/
```

## To run tests:
```bash
$ pytest -vv -p no:cacheprovider --alluredir=./reports/allure_results
```

> Pytest.ini is configured so that pytest executes any file, class or function that contains the text test as a sulfix,
> to change this, delete or edit the content of pytest.ini
 

## Reports
> You must have the allure client installed

Run the command below to generate the test report:

```bash
$ allure generate --clean ./reports/allure_results/ -o ./reports/allure-report
```

To view the report in the browser:

```bash
$ allure open ./reports/allure-report/
```

## Lint Code
To lint the code:

```bash
$ pylint *
```
## Docker execution
To start the tests with docker:

```bash
$ export BASE_URL=http://localhost:3000/
```
build imagem:
```bash
$ make -i build
```
Run the tests:
```bash
$ make test
```

To copy the report files to local reports folder:

```bash
$ make report.get
```
To generate reports:
> You must have the allure client installed

Run the command below to generate the test report:

```bash
$ allure generate --clean ./reports/allure_results/ -o ./reports/allure-report
```

To view the report in the browser, run the command:

```bash
$ allure open ./reports/allure-report/
```
