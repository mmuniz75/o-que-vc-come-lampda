from sqlalchemy import text
from sql_alchemy import db, unaccent


class BrandFoodChemicalModel(db.Model):

    __tablename__ = 'brand_food_chemical'

    id_brand = db.Column(db.Integer, db.ForeignKey('brand.id'), primary_key=True)
    id_food = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)
    id_chemical = db.Column(db.Integer, db.ForeignKey('chemical.id'), primary_key=True)

    chemicals = db.relationship('ChemicalModel', lazy='joined')

    def __init__(self, id_brand, id_food, id_chemical):
        self.id_brand = id_brand
        self.id_food = id_food
        self.id_chemical = id_chemical

    def json(self):
        return {
            'brandId': self.id_brand,
            'foodId': self.id_food,
            'chemicalId': self.id_chemical
        }

    def chemical_name(self):
        return self.chemicals.json()['name']

    @classmethod
    def find_by_brand_food(cls, brand_id, food_id):
        return db.session.query(BrandFoodChemicalModel).filter_by(id_brand=brand_id, id_food=food_id).order_by(unaccent(text("name")))

    @classmethod
    def find_by_id(cls, brand_id, food_id, chemical_id):
        return cls.query.enable_eagerloads(False).filter_by(id_brand=brand_id, id_food=food_id, id_chemical=chemical_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.enable_eagerloads(False).all()

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
