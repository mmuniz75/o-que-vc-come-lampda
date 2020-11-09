import json

from model.BrandModel import BrandModel
from model.BrandFoodModel import BrandFoodModel

import logging

logger = logging.Logger('catch_all')

MARCA_CADASTRADA = "Marca já cadastrada"


class BrandService:

    @staticmethod
    def get_foods(brand_id):
        foods = BrandFoodModel.find_by_brand(brand_id)
        if len(foods.all()) == 0:
            raise Exception({"statusCode": 404, "message": "Não existe alimentos para marca {}".format(brand_id)})

        list = [food.food() for food in foods]
        return json.dumps(list)

    @staticmethod
    def get_brands():
        brands = BrandModel.find_brands()
        return [brand.json() for brand in brands]

    @staticmethod
    def create_brand(name):
        brand = BrandModel(name)

        if BrandModel.find_by_name(name):
           raise Exception({"statusCode": 409, "message": MARCA_CADASTRADA})
        try:
            brand.save_brand()

        except Exception as e:
            logger.error(e, exc_info=True)
            raise Exception({"statusCode": 500, "message": "Error ao salvar marca"})
        return brand.json()

    @staticmethod
    def update_brand(brand_id, name):
        brand = BrandModel.find_brand(brand_id)
        if not brand:
            raise Exception({"statusCode": 404, "message": "Não existe marca com id {}".format(brand_id)})

        try:
            if BrandModel.find_by_name(name):
                return {"statusCode": 409, "message": MARCA_CADASTRADA}

            brand.update_brand(name)

        except Exception as e:
            logger.error(e, exc_info=True)
            raise Exception({"statusCode": 500, "message": "Error ao alterar marca"})
        return brand.json(), 200


    def check_brand(name):
        if BrandModel.find_by_name(name):
            raise Exception({"statusCode": 409, "message": "Marca já cadastrada"})
