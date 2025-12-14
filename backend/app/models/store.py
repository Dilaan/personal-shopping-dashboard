from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    website = Column(String, nullable=False)
