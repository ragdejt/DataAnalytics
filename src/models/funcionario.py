from sqlalchemy import Column, Integer, String
from database.database import Base


class Funcionario(Base):
    __tablename__ = 'Funcionarios'

    ID = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    Nome = Column(
        String,
        nullable=False
    )
    Email = Column(
        String,
        unique=True,
        nullable=False
    )
    Estado_Civil = Column(
        String,
        nullable=False
    )
    CPF = Column(
        String,
        unique=True,
        nullable=False
    )
    RG = Column(
        String,
        unique=True,
        nullable=False
    )
    Data_Nascimento = Column(
        String,
        nullable=False
    )
    Data_Admissao = Column(
        String,
        nullable=False
    )
    Data_Demissao = Column(
        String,
        nullable=True
    )
    Endereco = Column(
        String,
        nullable=False
    )
    Cargo = Column(
        String,
        nullable=False
    )
    Salario = Column(
        Integer,
        nullable=False
    )
    Telefone = Column(
        String,
        nullable=True
    )
    Celular = Column(
        String,
        nullable=True
    )
    Ativo = Column(
        Integer,
        default=1
    )
