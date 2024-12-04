from PySide6.QtWidgets import QWidget

from ui.widgets.PartnerCard import Ui_PartnerCard
from ui.widgets.PartnersPage import Ui_PartnersPage

from ui.windows.modal_window.modal_window import ModalWindow

from database.CRUDs.PartnerCRUDs import PartnerCRUD
from database.CRUDs.OrderCRUDs import OrderCRUD

class PartnerPageWidget(QWidget, Ui_PartnersPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Title.setText("Партнёры")

        self.fill_scroll_area()

        self.Button.setText("Добавление нового партнёра")
        self.Button.clicked.connect(lambda: ModalWindow(self,"create/update_partner",
                                                        "create").exec())

    def update_scroll_area(self):
        content_widget = self.scrollArea.widget()
        if content_widget:
            # Удаляем все дочерние элементы виджета
            for child in content_widget.children():
                if isinstance(child, QWidget):
                    child.deleteLater()
            # Обновление виджета
            content_widget.layout().update()

            self.fill_scroll_area()

    def fill_scroll_area(self):
        for partner_model in PartnerCRUD.read_partners():
            custom_widget = PartnerCardWidget(self, partner_model)
            self.verticalLayout_4.addWidget(custom_widget)


class PartnerCardWidget(QWidget, Ui_PartnerCard):
    def __init__(self, parent, partner_model):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedHeight(180)

        self.PartnerTypeAndName.setText(str(partner_model.type) + " | " + str(partner_model.company_name))
        self.BossName.setText(str(partner_model.boss_name))
        self.PhoneNumber.setText(str(partner_model.phone_number))
        self.Rank.setText("Рейтинг " + str(partner_model.rank))
        discount_percentage = calculation_of_discount_percentage(partner_model.id)
        self.DiscountPercentage.setText(str(discount_percentage) + "%")

        self.GetOrdersListButton.setText("Просмотреть заказы \n" + partner_model.company_name)
        self.EditButton.clicked.connect(lambda: ModalWindow(parent, "create/update_partner",
                                                            "update", partner_model).exec())
        self.GetOrdersListButton.clicked.connect(lambda: ModalWindow(parent, "get_orders_list", partner_model=partner_model).exec())

def calculation_of_discount_percentage(partner_id):
    discount_percentage = 0
    total_amount_of_order = 0

    for order in OrderCRUD.read_orders_by_company_id(partner_id):
        total_amount_of_order += order.quantity_of_products

    if 0 < total_amount_of_order < 1000:
        discount_percentage = 0
    elif 10000 < total_amount_of_order < 50000:
        discount_percentage = 5
    elif 50000 < total_amount_of_order < 300000:
        discount_percentage = 10
    elif 300000 < total_amount_of_order:
        discount_percentage = 15

    return discount_percentage