# backend/create_tables.py
from app.core.database import engine, Base
from app.models import store, product

Base.metadata.create_all(bind=engine)
