from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer)