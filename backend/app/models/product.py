from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    product_url = Column(String)

    store_id = Column(Integer, ForeignKey("stores.id"))
