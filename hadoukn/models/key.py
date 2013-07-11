from sqlalchemy import (
    Column,
    Integer,
    String
)
from hadoukn.models import Base
from hadoukn.models.behaviors import Createable


class Key(Base, Createable):
    __tablename__ = 'keys'

    # Main Fields
    key_type = Column(String(10))
    key_key = Column(String(1000))
    key_comment = Column(String(100))

    # Foreign Keys
    user_id = Column(Integer)
