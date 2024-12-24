from database.connection import session

from sqlalchemy.exc import SQLAlchemyError

from database.models.ProductModel import ProductModel

# Операции для работы с продуктами
class ProductCRUD:
    @staticmethod
    def get_product_min_cost(product_id: int) -> float:
        """
        Возвращает минимальную цену указанного продукта.

        :param product_id: Идентификатор продукта.
        :return: Минимальная цена продукта или 0.0, если не найдено.
        """
        try:
            # Получаем минимальную цену продукта
            cost = session.query(ProductModel.min_cost).filter(ProductModel.id == product_id).scalar()
            return cost if cost is not None else 0.0
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем 0.0
            session.rollback()
            print(f"Ошибка получения минимальной стоимости продукта: {e}")
            return 0.0

    @staticmethod
    def get_product_name(product_id: int) -> str:
        """
        Возвращает название указанного продукта.

        :param product_id: Идентификатор продукта.
        :return: Название продукта или сообщение об ошибке.
        """
        try:
            # Получаем название продукта
            name = session.query(ProductModel.name).filter(ProductModel.id == product_id).scalar()
            return name if name else "Продукт не найден"
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем сообщение об ошибке
            session.rollback()
            print(f"Ошибка получения названия продукта: {e}")
            return "Ошибка"