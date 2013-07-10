from sqlalchemy import (
    Column,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base


class BaseClass(object):
    id = Column(Integer, primary_key=True)

    @classmethod
    def by_id(cls, db, _id):
        return db.query(cls).filter_by(id=_id).first()


Base = declarative_base(cls=BaseClass)


def initialize_base(engine):
    Base.metadata.bind = engine
