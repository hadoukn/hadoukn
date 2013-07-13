from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from .meta import Base
from .behaviors.createable import Createable


class Dyno(Base, Createable):
    __tablename__ = 'dynos'

    # Main Fields
    container_hash = Column(String(100))

    # Foreign Keys
    release_id = Column(Integer, ForeignKey('releases.id'))
    daemon_id = Column(Integer, ForeignKey('daemons.id'))
