IMAGE_NAME="test-image"
CONTAINER_NAME="test-container"
CURRENT_PATH=$(shell pwd)
REPORT_DIRECTORY=reports
REPORT_LOCAL_PATH=${CURRENT_PATH}/${REPORT_DIRECTORY}
REPORT_CONTAINER_PATH=/api-tests-python-pytest/${REPORT_DIRECTORY}

test:
	@docker run --network host --name ${CONTAINER_NAME} ${IMAGE_NAME} /bin/bash -c "pytest -vv --alluredir=./reports/allure_results"

remove:
	@docker rmi -f ${IMAGE_NAME}
	@docker rm ${CONTAINER_NAME}

build: remove
	@docker build -t ${IMAGE_NAME} --build-arg BASE_URL=${BASE_URL} -f Dockerfile .

report.get:
	@docker cp ${CONTAINER_NAME}:/api-tests-python-pytest/reports ./