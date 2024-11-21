from config import session
from sqlalchemy.exc import SQLAlchemyError
from database.models.ProductModel import ProductModel

# CRUD операции
class ProductCRUD:
    @staticmethod
    def get_product_min_cost(product_id: int):
        """Получает минимальную цену продукта"""
        try:
            return session.query(ProductModel.min_cost).filter(ProductModel.id == product_id).scalar()
        except SQLAlchemyError as e:
            print(f"Ошибка получения минимальной стоимости продукта: {e}")
            return []

    @staticmethod
    def get_product_name(product_id: int):
        """Получает имя продукта"""
        try:
            return session.query(ProductModel.name).filter(ProductModel.id == product_id).scalar()
        except SQLAlchemyError as e:
            print(f"Ошибка получения названия продукта: {e}")
            return None