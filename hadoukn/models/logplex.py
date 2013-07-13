from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

from .meta import Base


class Logplex(Base):
    __tablename__ = 'logplexes'

    # Main Fields
    channel = Column(String(10))  # e.g. app
    source = Column(String(10))  # e.g. web.1

    # Foreign Keys
    app_id = Column(Integer, ForeignKey('apps.id'))

    def __json__(self, request):
        return {
            'id': self.id,
            'channel': self.channel,
            'source': self.source,
            'app_id': self.app_id
        }
