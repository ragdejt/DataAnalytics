from sqlalchemy import Column, String, Integer, Boolean
from sql.database.database import Base

class Product(Base):
    __tablename__= "Produtos"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(
        String,
        unique=True,
    )
    description = Column(
        String,
        nullable=True,
    )
    category = Column(
        String,
    )
    price = Column(
        Integer,
    )
    quantity = Column(
        Integer,
    )
    height = Column(
        Integer,
    )
    width = Column(
        Integer,
    )
    length = Column(
        Integer,
    )
    weight = Column(
        Integer,
    )
    active = Column(
        Boolean,
        default=False,
    )