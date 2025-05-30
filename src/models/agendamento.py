from sqlalchemy import Column, Integer, String
from database.database import Base

class Agendamento(Base):
    __tablename__ = 'Agendamentos'

    ID = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    Veiculo = Column(
        String
        
    )
    Placa = Column(
        String
    )
    Motorista = Column(
        String
    )
    CPF = Column(
        String
    )
    Entrada = Column(
        String
    )
    Saida = Column(
        String
    )
    Observacao = Column(
        String
    )

