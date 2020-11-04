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
            return {"message": "Item já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar relacionamento"}, 500
        return relation.json(), 201

    @staticmethod
    def delete(brand_id, food_id, chemical_id):
        try:
            relation = BrandFoodChemicalModel.find_by_id(brand_id, food_id, chemical_id)
            if not relation:
                return {"message": "Relacionamento não cadastrado"}, 404

            relation.delete()
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao remover relacionamento"}, 500
        return {}, 204
