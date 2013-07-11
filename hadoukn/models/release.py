from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from hadoukn.models import Base
from hadoukn.models.behaviors.createable import Createable


class Release(Base, Createable):
    __tablename__ = 'releases'

    # Main Fields
    name = Column(String(10))
    count = Column(Integer)
    description = Column(String(100))
    commit = Column(String(40))
    user_email = Column(String(100))

    # Foreign Keys
    app_id = Column(Integer, ForeignKey('apps.id'))
