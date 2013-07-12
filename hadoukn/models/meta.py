from sqlalchemy import (
    Column,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr


class BaseClass(object):
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)

    @classmethod
    def by_id(cls, db, _id):
        return db.query(cls).filter_by(id=_id).first()


Base = declarative_base(cls=BaseClass)
