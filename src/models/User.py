from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):
    __tablename__ = 'Usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    password = Column(String)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
