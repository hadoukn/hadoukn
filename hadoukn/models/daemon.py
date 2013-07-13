from sqlalchemy import (
    Column,
    String,
    Integer
)
from .meta import Base
from .behaviors.createable import Createable


class Daemon(Createable, Base):
    __tablename__ = 'daemons'

    host = Column(String(16))
    port = Column(Integer(4))

    def __json__(self, request):
        return {
            'id': self.id,
            'created': self.created,
            'host': self.host,
            'port': self.port
        }
