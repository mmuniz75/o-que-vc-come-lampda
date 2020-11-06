from model.BrandFoodModel import BrandFoodModel
from model.BrandFoodChemicalModel import BrandFoodChemicalModel
from sqlalchemy.exc import IntegrityError
from sql_alchemy import db

import logging
import barcodenumber

from services.BrandFoodChemicalService import BrandFoodChemicalService

logger = logging.Logger('catch_all')


class BrandFoodService:

    @staticmethod
    def get_foods_brand_by_barcode(bar_code):
        if not barcodenumber.check_code_ean13(bar_code):
            return {"message": "Codigo de barras invalido"}, 412

        relation = BrandFoodModel.find_by_bar_code(bar_code)
        if not relation:
            return {"message": "Codigo de barra não encontrado"}, 404

        return relation.json();

    @staticmethod
    def get_chemicals_by_barcode(bar_code):
        if not barcodenumber.check_code_ean13(bar_code):
            return {"message": "Codigo de barras invalido"}, 412

        relation = BrandFoodModel.find_by_bar_code(bar_code)
        if not relation:
            return {"message": "Codigo de barra não encontrado"}, 404

        return BrandFoodService.get_chemicals(relation.id_brand, relation.id_food)


    @staticmethod
    def get_chemicals(brand_id, food_id):

        relation = BrandFoodModel.find_by_id(brand_id, food_id)
        if not relation:
            return {"message": "Marca e produto não cadastrado"}, 404

        chemicals = BrandFoodChemicalModel.find_by_brand_food(brand_id, food_id)
        if len(chemicals.all()) == 0:
            return {"message": "Não existe quimicos para alimento {} da marca {}".format(brand_id, food_id)}, 404

        chemical_list = [chemical.chemical_name() for chemical in chemicals]

        chemicals = {"bar_code": relation.bar_code, "chemicals": chemical_list}
        return chemicals

    @staticmethod
    def get_all():
        relations = BrandFoodModel.find_all()
        return [relation.json() for relation in relations]

    @staticmethod
    def create(brand_id, food_id, bar_code, chemicals):

        if not chemicals or len(chemicals) == 0:
            return {"message": "Quimicos não informados"}, 400

        if not barcodenumber.check_code_ean13(bar_code):
            return {"message": "Codigo de barras invalido"}, 412

        relation = BrandFoodModel.find_by_bar_code(bar_code)
        if relation:
            return {"message": "Codigo de barras já cadastrado"}, 409

        relation = BrandFoodModel(brand_id, food_id, bar_code)
        try:
            relation.save()

            for chemical in chemicals:
                BrandFoodChemicalService.create(brand_id, food_id, chemical)

            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            return {"message": "Item já cadastrado"}, 409
        except Exception as e:
            db.session.rollback()
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar relacionamento"}, 500
        return relation.json(), 201

    @staticmethod
    def delete(brand_id, food_id):
        try:
            relation = BrandFoodModel.find_by_id(brand_id, food_id)
            if not relation:
                return {"message": "Relacionamento não cadastrado"}, 404

            relation.delete()
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao remover relacionamento"}, 500
        return {}, 204
