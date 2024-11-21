from config import session
from sqlalchemy.exc import SQLAlchemyError
from database.models.OrderModel import OrderModel

# CRUD операции
class OrderCRUD:
    # @staticmethod
    # def create_order(product_name: str, partner_name: str, quantity_of_products: int, date_of_create=None):
    #     """Создает новый заказ."""
    #     try:
    #         with session.begin():
    #             order = OrderModel(
    #                 product_name=product_name,
    #                 partner_name=partner_name,
    #                 quantity_of_products=quantity_of_products,
    #                 date_of_create=date_of_create,
    #             )
    #             session.add(order)
    #     except SQLAlchemyError as e:
    #         print(f"Ошибка создания заказа: {e}")

    @staticmethod
    def read_orders_by_company_id(company_name):
        """Возвращает список всех заказов конкретного партрнёра."""
        try:
            return session.query(OrderModel).filter(OrderModel.fk_company_name == company_name)
        except SQLAlchemyError as e:
            print(f"Ошибка чтения заказов партнёра {company_name}: {e}")
            return []