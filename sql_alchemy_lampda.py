from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import ReturnTypeFromArgs
from sqlalchemy import Column, ForeignKey, Integer, String


class unaccent(ReturnTypeFromArgs):
    pass

class lower(ReturnTypeFromArgs):
    pass

engine = create_engine("postgres://qeansobj:y8X8aX5qUuKbFXH6TdILEBa8VgZnDMvY@tuffi.db.elephantsql.com:5432/qeansobj", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

db = {
        "session": Session(),
        "Model": Base,
        "relationship":  relationship,
        "Column": Column,
        "Integer": Integer,
        "ForeignKey": ForeignKey,
        "String": String
      }
