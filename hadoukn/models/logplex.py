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
