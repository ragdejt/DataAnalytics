from sqlalchemy import Column, String, Integer
from database.database import Base

class Ticket(Base):
    __tablename__ = 'Tickets'

    Id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    Usuario = Column(String)
    Prioridade = Column(String)
    Status = Column(String)
    Data = Column(String)
    Motivo = Column(String)
    Observacao = Column(String)

