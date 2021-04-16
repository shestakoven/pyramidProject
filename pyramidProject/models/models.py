from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)

from pyramid_basemodel import Base


class Capture(Base):
    """Model for captures. Path is path to local file."""
    __tablename__ = 'captures'
    id = Column(Integer, primary_key=True)
    path = Column('path', String)
    created_at = Column('created at', String)
    camera = Column('camera', String)


Index('capture_id', Capture.id, unique=True, mysql_length=255)
