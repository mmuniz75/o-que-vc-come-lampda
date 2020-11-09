from model.BrandFoodChemicalModel import BrandFoodChemicalModel

from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class BrandFoodChemicalService:

    @staticmethod
    def get_all():
        relations = BrandFoodChemicalModel.find_all()
        return [relation.json() for relation in relations]

    @staticmethod
    def create(brand_id, food_id, chemical_id):
        relation = BrandFoodChemicalModel(brand_id, food_id, chemical_id)
        try:
            relation.save()

        except IntegrityError:
            raise Exception({"statusCode": 409, "message": "Item já cadastrado"})
        except Exception as e:
            logger.error(e, exc_info=True)
            raise Exception({"statusCode": 500, "message": "Error ao salvar relacionamento"})
        return relation.json()

    @staticmethod
    def delete(brand_id, food_id, chemical_id):
        try:
            relation = BrandFoodChemicalModel.find_by_id(brand_id, food_id, chemical_id)
            if not relation:
                raise Exception({"statusCode": 404, "message": "Relacionamento não cadastrado"})

            relation.delete()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise Exception({"statusCode": 500, "message": "Error ao remover relacionamento"})
        return {}
