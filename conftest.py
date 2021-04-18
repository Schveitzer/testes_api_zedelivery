import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def get_base_url():
    base_url = os.getenv("BASE_URL")
    yield base_url

@pytest.fixture(scope="session", autouse=True)
def get_appid():
    appid = os.getenv("APPID")
    yield appid
