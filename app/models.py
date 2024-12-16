from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class PlasticMaterial(Base):
    __tablename__ = "plastic_materials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Назва пластику (тип)
    color = Column(String, index=True)  # Колір
    quantity_kg = Column(Float)  # Кількість у кг
    reorder_threshold = Column(Float)  # Мінімальний залишок перед поповненням

class PrintModel(Base):
    __tablename__ = "print_models"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    plastic_type = Column(String)  # Тип пластику
    plastic_color = Column(String)  # Колір пластику
    plastic_required_kg = Column(Float)  # Необхідний обсяг пластику
