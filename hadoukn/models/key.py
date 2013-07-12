from sqlalchemy import (
    Column,
    Integer,
    String
)

from .meta import Base
from .behaviors.createable import Createable


class Key(Createable, Base):
    __tablename__ = 'keys'

    # Main Fields
    key_type = Column(String(10))
    key_key = Column(String(1000))
    key_comment = Column(String(100))

    # Foreign Keys
    user_id = Column(Integer)
