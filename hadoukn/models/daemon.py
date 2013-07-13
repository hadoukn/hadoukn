from sqlalchemy import (
    Column,
    String,
    Integer
)
from .meta import Base
from .behaviors.createable import Createable


class Daemon(Base, Createable):
    __tablename__ = 'daemons'

    host = Column(String(16))
    port = Column(Integer(4))

    def __json__(self, request):
        return {
            'host': self.host,
            'port': self.port
        }
