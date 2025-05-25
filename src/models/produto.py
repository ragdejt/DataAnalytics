from sqlalchemy import Column, String, Integer, Boolean
from database.database import Base

class Produto(Base):
    __tablename__= "Produtos"

    ID = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    Nome = Column(
        String,
        unique=True,
    )
    Descricao = Column(
        String,
        nullable=True,
    )
    Categoria = Column(
        String,
    )
    Preco = Column(
        Integer,
    )
    Quantidade = Column(
        Integer,
    )
    Altura = Column(
        Integer,
    )
    Largura = Column(
        Integer,
    )
    Comprimento = Column(
        Integer,
    )
    Peso = Column(
        Integer,
    )
    Ativo = Column(
        Boolean,
        default=False,
    )