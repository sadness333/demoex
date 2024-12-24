from database.connection import session

from sqlalchemy.exc import SQLAlchemyError

from database.models.OrderModel import OrderModel

# Операции для работы с заказами
class OrderCRUD:
    @staticmethod
    def read_orders_by_company_id(company_id: int) -> list[OrderModel]:
        """
        Возвращает список всех заказов для указанной компании.

        :param company_id: Идентификатор компании.
        :return: Список объектов OrderModel.
        """
        try:
            # Получаем заказы, связанные с указанной компанией
            return session.query(OrderModel).filter(OrderModel.fk_company_id == company_id).all()
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем пустой список
            session.rollback()
            print(f"Ошибка чтения заказов партнёра {company_id}: {e}")
            return []