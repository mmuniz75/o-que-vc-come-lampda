import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    return {"status": 200}