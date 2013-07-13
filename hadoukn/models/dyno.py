from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from .meta import Base
from .behaviors.createable import Createable


class Dyno(Createable, Base):
    __tablename__ = 'dynos'

    # Main Fields
    container_hash = Column(String(100))

    # Foreign Keys
    release_id = Column(Integer, ForeignKey('releases.id'))
    daemon_id = Column(Integer, ForeignKey('daemons.id'))

    def __json__(self, request):
        return {
            'id': self.id,
            'created': self.created,
            'container_hash': self.container_hash,
            'release_id': self.release_id,
            'daemon_id': self.daemon_id
        }
