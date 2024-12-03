from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget

from ui.widgets.OrderCard import Ui_OrderCard
from ui.widgets.OrdersPage import Ui_OrdersPage

from database.CRUDs.OrderCRUDs import OrderCRUD
from database.CRUDs.ProductCRUDs import ProductCRUD


class OrderCardWidget(QWidget, Ui_OrderCard):
    def __init__(self, product_name, quantity_of_products, date_of_create):
        super().__init__()
        self.setupUi(self)
        self.setFixedHeight(130)

        self.product_name.setText(product_name)
        self.quantity_of_products.setText("Количество заказанной продукции: " + quantity_of_products + " шт")
        self.date_of_create.setText("Дата создания заказа: " + date_of_create)


class OrderPageWidget(QWidget, Ui_OrdersPage):
    def __init__(self, partner_id):
        super().__init__()
        self.setupUi(self)

        self.Title.setText(QCoreApplication.translate("OrderPage", u"<html><head/><body><p align=\"center\">Заказы</p></body></html>", None))

        for order in OrderCRUD.read_orders_by_company_id(partner_id):
            custom_widget = OrderCardWidget(
                str(ProductCRUD.get_product_name(order.fk_product_name)),
                str(order.quantity_of_products),
                str(order.date_of_create)
            )
            self.verticalLayout_4.addWidget(custom_widget)