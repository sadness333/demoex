from database.connection import session

from sqlalchemy.exc import SQLAlchemyError

from database.models.PartnerModel import PartnerModel

# Операции для работы с партнёрами
class PartnerCRUD:
    @staticmethod
    def create_partner(**optional_fields) -> None:
        """
        Создает нового партнера в базе данных.

        :param optional_fields: Ключевые аргументы, соответствующие полям модели PartnerModel.
        """
        try:
            # Создаем объект партнера с переданными полями
            partner = PartnerModel(**optional_fields)
            # Добавляем объект в сессию
            session.add(partner)
            # Фиксируем изменения в базе данных
            session.commit()
            print(f"Партнер {partner.company_name} успешно создан.")
        except SQLAlchemyError as e:
            # В случае ошибки откатываем транзакцию
            session.rollback()
            print(f"Ошибка создания партнера: {e}")

    @staticmethod
    def read_partners() -> list[PartnerModel]:
        """
        Возвращает список всех партнеров из базы данных.

        :return: Список объектов PartnerModel.
        """
        try:
            # Получаем список партнеров, упорядоченных по их ID
            return session.query(PartnerModel).order_by(PartnerModel.id).all()
        except SQLAlchemyError as e:
            # В случае ошибки откатываем транзакцию и возвращаем пустой список
            session.rollback()
            print(f"Ошибка чтения партнеров: {e}")
            return []

    @staticmethod
    def update_partner(partner_id: int, **new_data) -> None:
        """
        Обновляет данные партнера по его ID.

        :param partner_id: Идентификатор партнера.
        :param new_data: Словарь с новыми значениями для обновления.
        """
        try:
            # Находим партнера по ID
            partner = session.query(PartnerModel).filter(PartnerModel.id == partner_id).first()
            if partner:
                # Обновляем поля партнера на основе переданных данных
                for field, value in new_data.items():
                    if hasattr(partner, field) and value is not None:
                        setattr(partner, field, value)
                # Фиксируем изменения
                session.commit()
                print(f"Партнер с ID {partner_id} успешно обновлен.")
            else:
                print(f"Партнер с ID {partner_id} не найден.")
        except SQLAlchemyError as e:
            # Откатываем транзакцию в случае ошибки
            session.rollback()
            print(f"Ошибка обновления партнера: {e}")