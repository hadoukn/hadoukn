from sqlalchemy import (
    Column,
    String,
    Integer
)
from .meta import Base
from .behaviors.createable import Createable
from hadoukn.util import print_time


class Daemon(Createable, Base):
    __tablename__ = 'daemons'

    host = Column(String(16))
    port = Column(Integer(4))

    def __json__(self, request):
        return {
            'id': self.id,
            'created': print_time(self.created),
            'host': self.host,
            'port': self.port
        }
