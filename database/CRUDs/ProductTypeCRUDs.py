from config import session
from sqlalchemy.exc import SQLAlchemyError

from database.models.ProductTypeModel import ProductTypeModel

# CRUD операции
class ProductTypeCRUD:
    @staticmethod
    def read_all_product_types(product_type_id):
        """Получение коэффициента типа продукта"""
        try:
            return session.query(ProductTypeModel).filter(ProductTypeModel.coefficient_of_product_type == product_type_id)
        except SQLAlchemyError as e:
            print(f"Ошибка чтения типов продуктов: {e}")
            return []