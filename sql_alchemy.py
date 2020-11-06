from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import ReturnTypeFromArgs
from sqlalchemy import Column, ForeignKey, Integer, String
import os


class unaccent(ReturnTypeFromArgs):
    pass


class lower(ReturnTypeFromArgs):
    pass


db_conn = os.environ.get('DB_CONN')
engine = create_engine(db_conn, echo=True)
Session = sessionmaker(bind=engine)


class db:
    session = Session()
    Model = declarative_base()
    relationship = relationship
    Column = Column
    Integer = Integer
    ForeignKey = ForeignKey
    String = String
