from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

from .meta import Base
from .behaviors.createable import Createable


class Release(Createable, Base):
    __tablename__ = 'releases'

    # Main Fields
    tag = Column(String(50))

    # Foreign Keys
    app_id = Column(Integer, ForeignKey('apps.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
