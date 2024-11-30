from sqlalchemy import desc

from config import session
from sqlalchemy.exc import SQLAlchemyError
from database.models.PartnerModel import PartnerModel

# CRUD операции над партнёрами
class PartnerCRUD:
    @staticmethod
    def create_partner(**optional_fields):
        """Создает нового партнера."""
        try:
            partner = PartnerModel(**optional_fields)
            session.add(partner)
            session.commit()
        except SQLAlchemyError as e:
            print(f"Ошибка создания партнера: {e}")

    @staticmethod
    def read_partners():
        """Возвращает список всех партнеров."""
        try:
            return session.query(PartnerModel).order_by(PartnerModel.id).all()
        except SQLAlchemyError as e:
            print(f"Ошибка чтения партнеров: {e}")
            return []

    @staticmethod
    def update_partner(partner_id: int, **new_data):
        """Обновляет данные партнера по его ID."""
        try:
            partner = session.query(PartnerModel).filter(PartnerModel.id == partner_id).first()
            if partner:
                for field, value in new_data.items():
                    if hasattr(partner, field) and value is not None:
                        setattr(partner, field, value)
                session.commit()
            else:
                print(f"Партнер с ID {partner_id} не найден.")
        except SQLAlchemyError as e:
            print(f"Ошибка обновления партнера: {e}")