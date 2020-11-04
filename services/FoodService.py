from flask import jsonify

from model.BrandFoodModel import BrandFoodModel
from model.FoodModel import FoodModel

import logging

logger = logging.Logger('catch_all')

ALIMENTO_CADASTRADO = "Alimento já cadastrado"


class FoodService:

    @staticmethod
    def get_brands(food_id):
        brands = BrandFoodModel.find_by_food(food_id)
        if len(brands.all()) == 0:
            return {"message": "Não existem marcas para esse alimento"}, 404
        list = [brand.brand() for brand in brands]
        return jsonify(list)

    @staticmethod
    def get_foods():
        foods = FoodModel.find_foods()
        return [food.json() for food in foods]

    @staticmethod
    def create_food(name):
        food = FoodModel(name)
        try:
            if FoodModel.find_by_name(name):
                return {"message": ALIMENTO_CADASTRADO}, 409

            food.save_food()

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar alimento"}, 500
        return food.json(), 201

    @staticmethod
    def update_food(food_id, name):
        food = FoodModel.find_food(food_id)
        if not food:
            return {"message": "Não existe alimento com id {}".format(food_id)}, 404

        try:
            if FoodModel.find_by_name(name):
                return {"message": ALIMENTO_CADASTRADO}, 409

            food.update_food(name)

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar alimento"}, 500
        return food.json(), 200
