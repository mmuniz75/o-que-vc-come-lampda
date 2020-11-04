from sql_alchemy import db, unaccent, lower


class FoodModel(db.Model):

    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @classmethod
    def find_food(cls, food_id):
        return cls.query.filter_by(id=food_id).first()

    @classmethod
    def find_by_name(cls, name):
        return db.session.query(FoodModel).filter(lower(unaccent(FoodModel.name)) == lower(unaccent(name))).first()

    @classmethod
    def find_foods(cls):
        return cls.query.order_by(unaccent(FoodModel.name)).all()

    def save_food(self):
        db.session.add(self)
        db.session.commit()

    def update_food(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def delete_food(self):
        db.session.delete(self)
        db.session.commit()
