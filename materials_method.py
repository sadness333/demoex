from database.CRUDs.ProductTypeCRUDs import ProductTypeCRUD
from database.CRUDs.MaterialCRUDs import MaterialCRUD


def calculate_material_amount(product_type_id: int, material_type_id: int, product_quantity: int,
                              param1: float, param2: float) -> int:

    try:
        # Проверка корректности входных данных
        if not (isinstance(product_type_id, int) and isinstance(material_type_id, int) and product_type_id > 0 and material_type_id > 0):
            return -1
        if not (isinstance(product_quantity, int) and product_quantity > 0):
            return -1
        if not (isinstance(param1, (float, int)) and isinstance(param2, (float, int)) and param1 > 0 and param2 > 0):
            return -1


        product_coefficient = ProductTypeCRUD.get_coefficient(product_type_id)
        defect_rate = MaterialCRUD.get_percentage_of_defective_material_by_id(material_type_id)  # Вещественное число в процентах (например, 5.0 для 5%)

        if product_coefficient is None or defect_rate is None:
            return -1
        # Расчёт количества материала на одну единицу продукции
        material_per_unit = param1 * param2 * product_coefficient

        # Увеличение на процент брака
        total_material = material_per_unit * product_quantity
        total_material_with_defect = total_material * (1 + defect_rate / 100)

        # Округление до целого числа
        return int(total_material_with_defect)

    except Exception as e:
        print(f"Ошибка в методе calculate_material_amount: {e}")
        return -1

print(calculate_material_amount(1,1,25000, 1.5, 2.5))