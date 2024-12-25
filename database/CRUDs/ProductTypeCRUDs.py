from sqlalchemy.exc import SQLAlchemyError

from database.connection import session
from database.models.ProductTypeModel import ProductTypeModel


# Операции для работы с типами продуктов
class ProductTypeCRUD:
    @staticmethod
    def read_all_product_types() -> list[ProductTypeModel]:
        """
        Возвращает список всех типов продуктов.

        :return: Список объектов ProductTypeModel.
        """
        try:
            # Получаем список всех типов продуктов, упорядоченных по их ID
            return session.query(ProductTypeModel).order_by(ProductTypeModel.id).all()
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем пустой список
            session.rollback()
            print(f"Ошибка чтения типов продуктов: {e}")
            return []

    @staticmethod
    def get_coefficient(product_type_id: int):
        try:
            # Получаем процент брака материала
            material = session.query(ProductTypeModel.coefficient_of_product_type).filter(
                ProductTypeModel.id == product_type_id).scalar()
            return material if material is not None else 0.0
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем 0.0
            session.rollback()
            print(f"Ошибка чтения процента брака материала: {e}")
            return 0.0
