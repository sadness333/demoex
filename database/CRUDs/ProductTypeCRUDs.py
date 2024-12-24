from database.connection import session

from sqlalchemy.exc import SQLAlchemyError

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