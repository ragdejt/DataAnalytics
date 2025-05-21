from sqlalchemy import Column, String, Integer, Boolean
from sql.database.database import Base
from datetime import datetime

class Product(Base):
    __tablename__= "Produtos"

    id = Column(
        Integer,
        name="Identificador",
        primary_key=True,
        autoincrement=True,
        doc="Identificador único do produto",
        comment="Identificador único do produto"
    )
    name = Column(
        String,
        name="Nome",
        unique=True,
        doc="Nome do produto",
        comment="Nome do produto"
    )
    description = Column(
        String,
        name="Descrição",
        nullable=True,
        doc="Descrição do produto",
        comment="Descrição do produto"
    )
    price = Column(
        Integer,
        name="Preço",
        doc="Preço do produto",
        comment="Preço do produto"
    )
    quantity = Column(
        Integer,
        name="Quantidade",
        doc="Quantidade do produto",
        comment="Quantidade do produto"
    )
    category = Column(
        String,
        name="Categoria",
        doc="Categoria do produto",
        comment="Categoria do produto"
    )
    height = Column(
        Integer,
        name="Altura",
        doc="Altura do produto",
        comment="Altura do produto"
    )
    width = Column(
        Integer,
        name="Largura",
        doc="Largura do produto",
        comment="Largura do produto"
    )
    length = Column(
        Integer,
        name="Comprimento",
        doc="Comprimento do produto",
        comment="Comprimento do produto"
    )
    weight = Column(
        Integer,
        name="Peso",
        doc="Peso do produto",
        comment="Peso do produto"
    )
    created = Column(
        String,
        name="Criado Em",
        doc="Data de criação do produto",
        comment="Data de criação do produto"
    )
    updated = Column(
        String,
        name="Atualizado Em",
        doc="Data de atualização do produto",
        comment="Data de atualização do produto",
        onupdate=datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    )
    active = Column(
        Boolean,
        name="Ativo",
        default=False,
        doc="Produto ativo",
        comment="Produto ativo"
    )