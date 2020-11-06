import logging
import json

from services.FoodService import FoodService
from services.BrandFoodService import BrandFoodService
from services.BrandService import BrandService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    route = event['route']
    if route == '/foods':
        return foods()
    elif route == '/brands':
        return brands()
    elif route == '/foods/<int:food_id>/brands':
        food_id = event['food_id']
        return brands_by_food(food_id)
    elif route == '/brands/<int:brand_id>/foods/<int:food_id>/chemicals':
        food_id = event['food_id']
        brand_id = event['brand_id']
        return chemicals_by_brand_food(brand_id, food_id)


def foods():
    return convert_json(FoodService.get_foods())


def brands_by_food(food_id):
    return convert_json(FoodService.get_brands(food_id))


def chemicals_by_brand_food(brand_id, food_id):
    return convert_json(BrandFoodService.get_chemicals(brand_id, food_id))


def brands():
    return convert_json(BrandService.get_brands())


def convert_json(obj):
    return json.dumps(obj, ensure_ascii=False).encode('utf8').decode()
