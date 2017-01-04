from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    username = Column(Text, primary_key=True)
    password = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    food = Column(Text)
    email = Column(Text)


Index('my_index', MyModel.username, unique=True, mysql_length=255)
