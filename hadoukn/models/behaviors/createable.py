from sqlalchemy import (
    Column,
    DateTime
)


class Createable(object):
    created = Column(DateTime)
