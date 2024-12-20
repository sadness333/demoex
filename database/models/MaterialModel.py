from sqlalchemy import Column, Integer, String, Float

from database.connection import Base


# Модель для таблицы "Materials".
class MaterialModel(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор материала
    type = Column(String(50), nullable=False)  # Тип материала
    percentage_of_defective_material = Column(Float, nullable=False)  # Процент брака для материала