from sqlalchemy import Column, String, Integer, Boolean, Float
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
        nullable=False
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
        nullable=False
    )
    Preco = Column(
        Float,
        nullable=False,
    )
    Quantidade = Column(
        Integer,
        nullable=False,
    )
    Altura = Column(
        Float,
        nullable=True,
        default='Altura Indefinida',
    )
    Largura = Column(
        Float,
        nullable=True,
        default='Largura Indefinida',
    )
    Comprimento = Column(
        Float,
        nullable=True,
        default='Comprimento Indefinido',
    )
    Peso = Column(
        Float,
        nullable=False,
    )
    Ativo = Column(
        Boolean,
        nullable=False,
        default=False,
    )