from sqlalchemy import Column, Integer, String
from database.database import Base

class Usuario(Base):
    __tablename__ = 'Usuarios'

    ID = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String, unique=True, index=True)
    Email = Column(String, unique=True, index=True)
    NomeCompleto = Column(String, index=True)
    Senha = Column(String)
    Ativo = Column(Integer, default=1)  # 1 for active, 0 for inactive
