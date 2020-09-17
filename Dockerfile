FROM python:3.6-slim
COPY . /api-tests-python-pytest
WORKDIR /api-tests-python-pytest

ARG BASE_URL
ENV BASE_URL=${BASE_URL}

RUN pip install --no-cache-dir -r requirements.txt