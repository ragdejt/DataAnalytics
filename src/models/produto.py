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
        default="Sem Descricao",
    )
    Marca = Column(
        String,
        nullable=True,
        default="Sem Marca",
    )
    Modelo = Column(
        String,
        nullable=True,
        default="Sem Modelo",
    )
    Categoria = Column(
        String,
    )
    Preco = Column(
        Integer,
        nullable=False
    )
    Quantidade = Column(
        Integer,
        default=0,
    )
    Altura = Column(
        Integer,
        nullable=True,
        default=0,
    )
    Largura = Column(
        Integer,
        nullable=True,
        default=0,
    )
    Comprimento = Column(
        Integer,
        nullable=True,
        default=0,
    )
    Peso = Column(
        Integer,
        nullable=False,
    )
    Ativo = Column(
        Boolean,
        nullable=False,
        default=False,
    )