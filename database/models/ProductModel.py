from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.config import Base


# Определение модели
class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    article = Column(String(10), nullable=False)
    name = Column(String(200), nullable=False)
    min_cost = Column(Float, nullable=False)
    fk_type = Column(Integer, ForeignKey('product_type.id'), nullable=False)

    def __repr__(self):
        return (
            f"<Product(id={self.id}, article='{self.article}', name='{self.name}', "
            f"type='{self.type}', min_cost={self.min_cost})>"
        )