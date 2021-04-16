import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime
)

from pyramid_basemodel import Base


class Capture(Base):
    """Model for captures. Path is path to local file."""
    __tablename__ = 'captures'
    id = Column(Integer, primary_key=True)
    path = Column('path', String)
    created_at = Column('created at', DateTime, default=datetime.datetime.now)
    camera = Column('camera', String)


Index('capture_id', Capture.id, unique=True, mysql_length=255)
