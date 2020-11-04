from sql_alchemy import db, unaccent


class ChemicalModel(db.Model):

    __tablename__ = 'chemical'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    url = db.Column(db.String)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }

    @classmethod
    def find_chemical(cls, chemical_id):
        return cls.query.filter_by(id=chemical_id).first()

    @classmethod
    def find_chemicals(cls):
        return cls.query.filter(ChemicalModel.name != 'Nenhum').order_by(unaccent(ChemicalModel.name)).all()

    def save_chemical(self):
        db.session.add(self)


    def update_chemical(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def delete_chemical(self):
        db.session.delete(self)
        db.session.commit()
