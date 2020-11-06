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
            return {"statusCode": 404, "message": "Não existem marcas para esse alimento"}
        list = [brand.brand() for brand in brands]
        return list

    @staticmethod
    def get_foods():
        foods = FoodModel.find_foods()
        return [food.json() for food in foods]

    @staticmethod
    def create_food(name):
        food = FoodModel(name)
        try:
            if FoodModel.find_by_name(name):
                return {"statusCode": 409, "message": ALIMENTO_CADASTRADO}

            food.save_food()

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"statusCode": 500, "message": "Error ao salvar alimento"}
        return food.json()

    @staticmethod
    def update_food(food_id, name):
        food = FoodModel.find_food(food_id)
        if not food:
            return {"statusCode": 404, "message": "Não existe alimento com id {}".format(food_id)}

        try:
            if FoodModel.find_by_name(name):
                return {"statusCode": 404, "message": ALIMENTO_CADASTRADO}

            food.update_food(name)

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"statusCode": 500, "message": "Error ao alterar alimento"}
        return food.json()
