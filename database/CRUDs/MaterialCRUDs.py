from sqlalchemy.exc import SQLAlchemyError
from database.config import session
from database.models.MaterialModel import MaterialModel

# CRUD операции
class MaterialCRUD:
    @staticmethod
    def get_percentage_of_defective_material_by_id(material_id):
        """Возвращает процент брака материала по id"""
        try:
            return session.query(MaterialModel).filter(MaterialModel.percentage_of_defective_material == material_id)
        except SQLAlchemyError as e:
            print(f"Ошибка чтения процента брака материала: {e}")
            return []