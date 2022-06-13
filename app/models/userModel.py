from sqlalchemy import Column, Integer, String
from app.connections.conecctionMysql import base

class User(base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, index=True)
    user_nickname = Column(String(50))
    user_firts_name = Column(String(50))
    user_other_name = Column(String(50))
    user_firts_lastname = Column(String(50))
    user_other_lastname = Column(String(50))
    user_rol = Column(String(50))
    state = Column(Integer)

