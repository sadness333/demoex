from database.config import session
from sqlalchemy.exc import SQLAlchemyError
from database.models.OrderModel import OrderModel

# CRUD операции
class OrderCRUD:
    @staticmethod
    def read_orders_by_company_id(company_name):
        """Возвращает список всех заказов конкретного партрнёра."""
        try:
            return session.query(OrderModel).filter(OrderModel.fk_company_name == company_name)
        except SQLAlchemyError as e:
            print(f"Ошибка чтения заказов партнёра {company_name}: {e}")
            return []