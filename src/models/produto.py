from sqlalchemy import Column, String, Integer, Boolean, Numeric
from database.database import Base

class Produto(Base):
    """``Tabela de Produtos``"""

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
        Numeric,
        nullable=False,
    )
    Altura = Column(
        Numeric,
        nullable=True,
        default='Altura Indefinida',
    )
    Largura = Column(
        Numeric,
        nullable=True,
        default='Largura Indefinida',
    )
    Comprimento = Column(
        Numeric,
        nullable=True,
        default='Comprimento Indefinido',
    )
    Peso = Column(
        Numeric,
        nullable=False,
    )
    Ativo = Column(
        Boolean,
        nullable=False,
        default=False,
    )