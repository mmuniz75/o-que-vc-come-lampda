from flask import jsonify

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
            return {"message": "Não existe alimentos para marca {}".format(brand_id)}, 404
        list = [food.food() for food in foods]
        return jsonify(list)

    @staticmethod
    def get_brands():
        brands = BrandModel.find_brands()
        return [brand.json() for brand in brands]

    @staticmethod
    def create_brand(name):
        brand = BrandModel(name)
        try:

            if BrandModel.find_by_name(name):
                return {"message": MARCA_CADASTRADA}, 409

            brand.save_brand()

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar marca"}, 500
        return brand.json(), 201

    @staticmethod
    def update_brand(brand_id, name):
        brand = BrandModel.find_brand(brand_id)
        if not brand:
            return {"message": "Não existe marca com id {}".format(brand_id)}, 404

        try:
            if BrandModel.find_by_name(name):
                return {"message": MARCA_CADASTRADA}, 409

            brand.update_brand(name)

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar marca"}, 500
        return brand.json(), 200

    def check_brand(name):
        if BrandModel.find_by_name(name):
            return {"message": "Marca já cadastrada"}, 409
