from database.database import Base
from sqlalchemy import Column, Integer, String

class Estoque(Base):
    """``Tabela de estoques``"""

    __tablename__ = 'Estoques'

    Estoque = Column(
        Integer,
        nullable=False
    )
    Rua = Column(
        Integer,
        nullable=False
    )
    Predio = Column(
        Integer,
        nullable=False
    )
    Andar = Column(
        Integer,
        nullable=False
    )
    Lado = Column(
        String,
        nullable=False
    )
    Produto = Column(
        Integer,
        nullable=False
    )
    Quantidade = Column(
        Integer,
        nullable=False
    )