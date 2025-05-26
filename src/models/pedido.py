from sqlalchemy import Column, Integer, String
from database.database import Base
from datetime import date
class Pedido(Base):
    __tablename__ = 'Pedidos'
    ID = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    ID_Usuario = Column(
        Integer,
        nullable=False
    )
    ID_Produto = Column(
        Integer,
        nullable=False
    )
    Quantidade = Column(
        Integer,
        nullable=False
    )
    Data = Column(
        String,
        nullable=False,
        default=date.ctime()
    )
    Data_Entrega = Column(
        String,
        nullable=True,
        default="Não informada"
    )
    Status = Column(
        String,
        nullable=False,
    )
    Valor_Total = Column(
        Integer,
        nullable=False
    )
    Observacao = Column(
        String,
        nullable=True,
        default="Sem Observação"
    )
