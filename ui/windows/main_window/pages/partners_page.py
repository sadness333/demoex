from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget

from ui.widgets.PartnerCard import Ui_PartnerCard
from ui.widgets.ScrollPage import Ui_ScrollPage

from ui.windows.modal_window.modal_window import ModalWindow

from database.CRUDs.PartnerCRUDs import PartnerCRUD

class PartnerCardWidget(QWidget, Ui_PartnerCard):
    def __init__(self, partner_model):
        super().__init__()
        self.setupUi(self)
        self.setFixedHeight(180)

        self.PartnerTypeAndName.setText(str(partner_model.type) + " | " + str(partner_model.company_name))
        self.BossName.setText(str(partner_model.boss_name))
        self.PhoneNumber.setText(str(partner_model.phone_number))
        self.Rank.setText("Рейтинг " + str(partner_model.rank))
        discount_percentage = "10"
        self.DiscountPercentage.setText(discount_percentage + "%")

        self.GetOrdersListButton.setText("Просмотреть заказы \n" + partner_model.company_name)
        self.EditButton.clicked.connect(lambda: ModalWindow("create/update_partner",
                                                            partner_model, "update").exec_())
        self.GetOrdersListButton.clicked.connect(lambda: ModalWindow("get_orders_list", partner_model).exec_())


class PartnerPageWidget(QWidget, Ui_ScrollPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Title.setText(QCoreApplication.translate(
            "test",
            u"<html><head/><body><p align=\"center\">Партнёры</p></body></html>",
            None
        ))

        for partner_model in PartnerCRUD.read_partners():
            custom_widget = PartnerCardWidget(partner_model)
            self.verticalLayout_4.addWidget(custom_widget)

        self.Button.setText("Добавление нового партнёра")
        self.Button.clicked.connect(lambda: ModalWindow("create/update_partner",
                                                          partner_model, "create").exec_())