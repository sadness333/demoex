from database.connection import session

from sqlalchemy.exc import SQLAlchemyError

from database.models.MaterialModel import MaterialModel

# Операции для работы с материалами
class MaterialCRUD:
    @staticmethod
    def get_percentage_of_defective_material_by_id(material_id: int) -> float:
        """
        Возвращает процент брака материала по его ID.

        :param material_id: Идентификатор материала.
        :return: Процент брака или 0.0, если не найдено.
        """
        try:
            # Получаем процент брака материала
            material = session.query(MaterialModel.percentage_of_defective_material) \
                .filter(MaterialModel.id == material_id).scalar()
            return material if material is not None else 0.0
        except SQLAlchemyError as e:
            # Откатываем транзакцию и возвращаем 0.0
            session.rollback()
            print(f"Ошибка чтения процента брака материала: {e}")
            return 0.0