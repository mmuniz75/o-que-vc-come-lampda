from model.ChemicalModel import ChemicalModel
from sql_alchemy import db
from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class ChemicalService:

    @staticmethod
    def get_chemicals():
        chemicals = ChemicalModel.find_chemicals()
        return [chemical.json() for chemical in chemicals]

    @staticmethod
    def create_chemical(chemicals):

        try:
            for chemical in chemicals:
                chemicalModel = ChemicalModel(chemical['name'], chemical['url'])
                chemicalModel.save_chemical()

            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()
            return {"message": "Quimico {} já cadastrado".format(ChemicalService.get_field_name(err.orig.args[0]))}, 409
        except Exception as e:
            db.session.rollback()
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar quimico"}, 500
        return {"message": "Quimicos adicionados"}, 201

    @staticmethod
    def get_field_name(erro):
        start = erro.index("(name)=(") + 8
        return erro[start:erro.index(")", start)]

    @staticmethod
    def update_chemical(chemical_id, name):
        chemical = ChemicalModel.find_chemical(chemical_id)
        if not chemical:
            return {"message": "Não existe quimico com id {}".format(chemical_id)}, 404

        try:
            chemical.update_chemical(name)
        except IntegrityError:
            return {"message": "Quimico já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar quimico"}, 500
        return chemical.json(), 200
