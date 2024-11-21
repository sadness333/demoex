from sqlalchemy import Column, Integer, String, Float
from config import Base, engine

# Определение модели
class ProductTypeModel(Base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    coefficient_of_product_type = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<ProductType(id={self.id}, type='{self.type}', "
            f"coefficient_of_product_type={self.coefficient_of_product_type})>"
        )