from database.config import session

from database.models.MaterialModel import MaterialModel
from database.models.ProductTypeModel import ProductTypeModel
from database.models.PartnerModel import PartnerModel
from database.models.ProductModel import ProductModel
from database.models.OrderModel import OrderModel


# Инициализация материалов
def initialize_materials():
    if not session.query(MaterialModel).first():
        initial_materials = [
            MaterialModel(type="Тип материала 1", percentage_of_defective_material=0.10),
            MaterialModel(type="Тип материала 2", percentage_of_defective_material=0.95),
            MaterialModel(type="Тип материала 3", percentage_of_defective_material=0.28),
            MaterialModel(type="Тип материала 4", percentage_of_defective_material=0.55),
            MaterialModel(type="Тип материала 5", percentage_of_defective_material=0.34),
        ]
        session.add_all(initial_materials)
        session.commit()

# Инициализация заказов
def initialize_orders():
    if not session.query(OrderModel).first():
        initial_orders = [
            OrderModel(
                fk_product_name=1,
                fk_company_name=1,
                quantity_of_products=15500,
                date_of_create="2023-03-23"),
            OrderModel(
                fk_product_name=3,
                fk_company_name=1,
                quantity_of_products=12350,
                date_of_create="2023-12-18"),
            OrderModel(
                fk_product_name=4,
                fk_company_name=1,
                quantity_of_products=37400,
                date_of_create="2024-06-07"),
            OrderModel(
                fk_product_name=2,
                fk_company_name=2,
                quantity_of_products=35000,
                date_of_create="2022-12-02"),
            OrderModel(
                fk_product_name=5,
                fk_company_name=2,
                quantity_of_products=1250,
                date_of_create="2023-05-17"),
            OrderModel(
                fk_product_name=3,
                fk_company_name=2,
                quantity_of_products=1000,
                date_of_create="2024-06-07"),
            OrderModel(
                fk_product_name=1,
                fk_company_name=2,
                quantity_of_products=7550,
                date_of_create="2024-07-01"),
            OrderModel(
                fk_product_name=1,
                fk_company_name=3,
                quantity_of_products=7250,
                date_of_create="2023-01-22"),
            OrderModel(
                fk_product_name=2,
                fk_company_name=3,
                quantity_of_products=2500,
                date_of_create="2024-07-05"),
            OrderModel(
                fk_product_name=4,
                fk_company_name=4,
                quantity_of_products=59050,
                date_of_create="2023-03-20"),
            OrderModel(
                fk_product_name=3,
                fk_company_name=4,
                quantity_of_products=37200,
                date_of_create="2024-03-12"),
            OrderModel(
                fk_product_name=5,
                fk_company_name=4,
                quantity_of_products=4500,
                date_of_create="2024-05-14"),
            OrderModel(
                fk_product_name=3,
                fk_company_name=5,
                quantity_of_products=50000,
                date_of_create="2023-09-19"),
            OrderModel(
                fk_product_name=4,
                fk_company_name=5,
                quantity_of_products=670000,
                date_of_create="2023-11-10"),
            OrderModel(
                fk_product_name=1,
                fk_company_name=5,
                quantity_of_products=350000,
                date_of_create="2024-04-15"),
            OrderModel(
                fk_product_name=2,
                fk_company_name=5,
                quantity_of_products=25000,
                date_of_create="2024-06-12"),

        ]
        session.add_all(initial_orders)
        session.commit()

# Инициализация партнёров
def initialize_partners():
    if not session.query(PartnerModel).first():
        initial_partners = [
            PartnerModel(
                type="ЗАО",
                company_name="База Строитель",
                address="652050, Кемеровская область, город Юрга, ул. Лесная, 15",
                inn="2222455179",
                boss_name="Иванова Александра Ивановна",
                phone_number="493 123 45 67",
                mail="aleksandraivanova@ml.ru",
                rank=7,
            ),
            PartnerModel(
                type="ООО",
                company_name="Паркет 29",
                address="164500, Архангельская область, город Северодвинск, ул. Строителей, 18",
                inn="3333888520",
                boss_name="Петров Василий Петрович",
                phone_number="987 123 56 78",
                mail="vppetrov@vl.ru",
                rank=7,
            ),
            PartnerModel(
                type="ПАО",
                company_name="Стройсервис",
                address="188910, Ленинградская область, город Приморск, ул. Парковая, 21",
                inn="4440391035",
                boss_name="Соловьев Андрей Николаевич",
                phone_number="812 223 32 00",
                mail="ansolovev@st.ru",
                rank=7,
            ),
            PartnerModel(
                type="ОАО",
                company_name="Ремонт и отделка",
                address="143960, Московская область, город Реутов, ул. Свободы, 51",
                inn="1111520857",
                boss_name="Воробьева Екатерина Валерьевна",
                phone_number="444 222 33 11",
                mail="ekaterina.vorobeva@ml.ru",
                rank=5,
            ),
            PartnerModel(
                type="ЗАО",
                company_name="МонтажПро",
                address="309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122",
                inn="5552431140",
                boss_name="Степанов Степан Сергеевич",
                phone_number="912 888 33 33",
                mail="stepanov@stepan.ru",
                rank=10,
            ),
        ]
        session.add_all(initial_partners)
        session.commit()

# Инициализация продуктов
def initialize_products():
    if not session.query(ProductModel).first():
        initial_products = [
            ProductModel(
                article="8758385",
                name="Паркетная доска Ясень темный однополосная 14 мм",
                fk_type=3,
                min_cost=4456.9,
            ),
            ProductModel(
                article="8858958",
                name="Инженерная доска Дуб Французская елка однополосная 12 мм",
                fk_type=3,
                min_cost=7330.99,
            ),
            ProductModel(
                article="7750282",
                name="Ламинат Дуб дымчато-белый 33 класс 12 мм",
                fk_type=1,
                min_cost=1799.33,
            ),
            ProductModel(
                article="7028748",
                name="Ламинат Дуб серый 32 класс 8 мм с фаской",
                fk_type=1,
                min_cost=3890.41,
            ),
            ProductModel(
                article="5012543",
                name="Пробковое напольное клеевое покрытие 32 класс 4 мм",
                fk_type=4,
                min_cost=5450.59,
            ),
        ]
        session.add_all(initial_products)
        session.commit()

# Инициализация типа продуктов
def initialize_product_type():
    if not session.query(ProductTypeModel).first():
        initial_product_type = [
            ProductTypeModel(type="Ламинат", coefficient_of_product_type=2.35),
            ProductTypeModel(type="Массивная доска", coefficient_of_product_type=5.15),
            ProductTypeModel(type="Паркетная доска", coefficient_of_product_type=4.34),
            ProductTypeModel(type="Пробковое покрытие", coefficient_of_product_type=1.5),
        ]
        session.add_all(initial_product_type)
        session.commit()