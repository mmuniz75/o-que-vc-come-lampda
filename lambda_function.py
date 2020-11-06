import logging
import json

from services.FoodService import FoodService
from services.BrandFoodService import BrandFoodService
from services.BrandService import BrandService
from services.ChemicalService import ChemicalService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    route = event['route']
    if route == '/foods':
        name = event['name'] if 'name' in event else None
        return foods(name)
    elif route == '/brands':
        name = event['name'] if 'name' in event else None
        return brands(name)
    elif route == '/chemicals':
        return chemicals()
    elif route == '/foods/<int:food_id>/brands':
        food_id = event['food_id']
        return brands_by_food(food_id)
    elif route == '/brands/<int:brand_id>/foods/<int:food_id>/chemicals':
        food_id = event['food_id']
        brand_id = event['brand_id']
        return chemicals_by_brand_food(brand_id, food_id)
    elif route == '/brands/foods/<string:bar_code>':
        bar_code = event['bar_code']
        return brand_food_bar_code(bar_code)
    elif route == '/brands/<int:brand_id>/foods/<int:food_id>':
        bar_code = event['bar_code']
        food_id = event['food_id']
        brand_id = event['brand_id']
        _chemicals = event['chemicals']
        return brand_food_create(brand_id, food_id, bar_code, _chemicals)


def foods(name):
    if name is None:
        return convert_json(FoodService.get_foods())
    else:
        return FoodService.create_food(name)


def brands_by_food(food_id):
    return convert_json(FoodService.get_brands(food_id))


def chemicals_by_brand_food(brand_id, food_id):
    return convert_json(BrandFoodService.get_chemicals(brand_id, food_id))


def brands(name):
    if name is None:
        return convert_json(BrandService.get_brands())
    else:
        return BrandService.create_brand(name)


def chemicals():
    return convert_json(ChemicalService.get_chemicals())


def brand_food_bar_code(bar_code):
    return BrandFoodService.get_foods_brand_by_barcode(bar_code)


def brand_food_create(brand_id, food_id, bar_code, chemicals):
    return BrandFoodService.create(brand_id, food_id, bar_code, chemicals)


def convert_json(obj):
    return json.dumps(obj, ensure_ascii=False).encode('utf8').decode()
