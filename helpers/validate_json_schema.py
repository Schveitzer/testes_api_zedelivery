import logging
from jsonschema import validate, exceptions


logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def validate_json(json_data, json_schema):
    try:
        validate(instance=json_data, schema=json_schema)
    except exceptions.ValidationError as err:
        logger.error(err)
        return False

    return True
