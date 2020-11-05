import logging

from services.FoodService import FoodService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    return FoodService.get_foods()
