from PySide6.QtWidgets import QWidget

from ui.widgets.PartnerCardWithButton import Ui_PartnerCardWithButton
from ui.widgets.PartnersPage import Ui_PartnersPage

from ui.windows.modal_window.modal_window import ModalWindow

from database.CRUDs.PartnerCRUDs import PartnerCRUD
from database.CRUDs.OrderCRUDs import OrderCRUD

class PartnerPageWidget(QWidget, Ui_PartnersPage):
    def __init__(self):
        super().__init__()
        # Настройка пользовательского интерфейса, созданного в Qt Designer
        self.setupUi(self)

        # Установка заголовка страницы
        self.Title.setText("Партнёры")

        # Заполнение области прокрутки партнёрами
        self.fill_scroll_area()

        # Настройка кнопки для добавления нового партнёра
        self.Button.setText("Добавление нового партнёра")
        self.Button.clicked.connect(lambda: ModalWindow(self, "create/update_partner", "create").exec())

    def update_scroll_area(self):
        # Обновление области прокрутки: удаление старого содержимого и добавление нового
        content_widget = self.scrollArea.widget()
        if content_widget:
            # Удаляем все дочерние элементы виджета
            for child in content_widget.children():
                if isinstance(child, QWidget):
                    child.deleteLater()
            # Обновление лейаута виджета
            content_widget.layout().update()

            # Повторное заполнение области прокрутки
            self.fill_scroll_area()

    def fill_scroll_area(self):
        # Добавление виджетов партнёров в область прокрутки
        for partner_model in PartnerCRUD.read_partners():
            custom_widget = PartnerCardWidget(self, partner_model)  # Создание карточки партнёра
            self.verticalLayout_4.addWidget(custom_widget)  # Добавление карточки в лейаут


class PartnerCardWidget(QWidget, Ui_PartnerCardWithButton):
    def __init__(self, parent, partner_model):
        super().__init__(parent)
        # Настройка пользовательского интерфейса карточки партнёра
        self.setupUi(self)
        # Установка фиксированной высоты карточки
        self.setFixedHeight(180)

        # Установка текстов в соответствующие поля карточки
        self.PartnerTypeAndName.setText(str(partner_model.type) + " | " + str(partner_model.company_name))
        self.BossName.setText(str(partner_model.boss_name))
        self.PhoneNumber.setText(str(partner_model.phone_number))
        self.Rank.setText("Рейтинг " + str(partner_model.rank))

        # Вычисление и отображение процента скидки
        discount_percentage = calculation_of_discount_percentage(partner_model.id)
        self.DiscountPercentage.setText(str(discount_percentage) + "%")

        # Настройка кнопок для просмотра заказов и редактирования партнёра
        self.GetOrdersListButton.setText("Просмотреть заказы \n" + partner_model.company_name)
        self.GetOrdersListButton.clicked.connect(lambda: ModalWindow(parent, "get_orders_list", partner_model=partner_model).exec())

        self.PartnerTypeAndName.clicked.connect(lambda: ModalWindow(parent, "create/update_partner", "update", partner_model).exec())
        self.BossName.clicked.connect(lambda: ModalWindow(parent, "create/update_partner", "update", partner_model).exec())
        self.PhoneNumber.clicked.connect(lambda: ModalWindow(parent, "create/update_partner", "update", partner_model).exec())
        self.Rank.clicked.connect(lambda: ModalWindow(parent, "create/update_partner", "update", partner_model).exec())
        self.DiscountPercentage.clicked.connect(lambda: ModalWindow(parent, "create/update_partner", "update", partner_model).exec())


def calculation_of_discount_percentage(partner_id: int) -> int:
    """
    Функция для вычисления процента скидки на основе общего объёма заказов партнёра.

    :param partner_id: ID партнёра.
    :return Скидка для партнёра.
    """
    discount_percentage = 0
    total_amount_of_order = 0

    # Суммирование количества продуктов во всех заказах партнёра
    for order in OrderCRUD.read_orders_by_company_id(partner_id):
        total_amount_of_order += order.quantity_of_products

    # Условия для вычисления процента скидки
    if 0 < total_amount_of_order < 1000:
        discount_percentage = 0
    elif 10000 < total_amount_of_order < 50000:
        discount_percentage = 5
    elif 50000 < total_amount_of_order < 300000:
        discount_percentage = 10
    elif 300000 < total_amount_of_order:
        discount_percentage = 15

    return discount_percentage