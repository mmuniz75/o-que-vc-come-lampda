from sql_alchemy import db, unaccent, lower


class BrandModel(db.Model):

    __tablename__ = 'brand'

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
    def find_brand(cls, brand_id):
        return cls.query.filter_by(id=brand_id).first()

    @classmethod
    def find_by_name(cls, name):
        return db.session.query(BrandModel).filter(lower(unaccent(BrandModel.name)) == lower(unaccent(name))).first()

    @classmethod
    def find_brands(cls):
        return db.session.query(BrandModel).order_by(unaccent(BrandModel.name)).all()

    def save_brand(self):
        db.session.add(self)
        db.session.commit()

    def update_brand(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def delete_brand(self):
        db.session.delete(self)
        db.session.commit()
