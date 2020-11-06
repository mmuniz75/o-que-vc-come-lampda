from sqlalchemy import text

from sql_alchemy import db, unaccent


class BrandFoodModel(db.Model):

    __tablename__ = 'brand_food'

    id_brand = db.Column(db.Integer, db.ForeignKey('brand.id'), primary_key=True)
    id_food = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)

    bar_code = db.Column(db.String(13), nullable=False, unique=True, index=True)

    brands = db.relationship('BrandModel', lazy='joined')
    foods = db.relationship('FoodModel', lazy='joined')

    def __init__(self, id_brand, id_food, bar_code):
        self.id_brand = id_brand
        self.id_food = id_food
        self.bar_code = bar_code

    def json(self):
        return {
            'brandId': self.id_brand,
            'foodId': self.id_food,
            'barCode': self.bar_code
        }

    def brand(self):
        brand = self.brands.json()
        return {
            'barCode': self.bar_code,
            'id': brand['id'],
            'name': brand['name']
        }

    def food(self):
        food = self.foods.json()
        return {
            'barCode': self.bar_code,
            'id': food['id'],
            'name': food['name']
        }

    @classmethod
    def find_by_food(cls, food_id):
        return db.session.query(BrandFoodModel).filter_by(id_food=food_id).order_by(unaccent(text("food_1.name")))

    @classmethod
    def find_by_brand(cls, brand_id):
        return db.session.query(BrandFoodModel).filter_by(id_brand=brand_id).order_by(unaccent(text("brand_1.name")))

    @classmethod
    def find_by_id(cls, brand_id, food_id):
        return db.session.query(BrandFoodModel).enable_eagerloads(False).filter_by(id_brand=brand_id, id_food=food_id).first()

    @classmethod
    def find_by_bar_code(cls, bar_code):
        return db.session.query(BrandFoodModel).enable_eagerloads(False).filter_by(bar_code=bar_code).first()

    @classmethod
    def find_all(cls):
        return db.session.query(BrandFoodModel).enable_eagerloads(False).all()

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
