from sqlalchemy import Column, Integer, String, Float
from database.config import Base, engine

# Модель
class MaterialModel(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    percentage_of_defective_material = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Material(id={self.id}, type='{self.type}', percentage_of_defective_material={self.percentage_of_defective_material})>"


Base.metadata.create_all(engine)