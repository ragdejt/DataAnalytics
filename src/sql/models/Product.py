from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP
from sql.database.database import Base
from datetime import datetime

class Product(Base):
    __tablename__= "Produtos"

    id = Column(
        Integer,        primary_key=True,
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
    created = Column(
        TIMESTAMP,
        default=datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
    )
    updated = Column(
        TIMESTAMP,
        default=datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
        onupdate=datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
    )
    active = Column(
        Boolean,
        default=False,
    )