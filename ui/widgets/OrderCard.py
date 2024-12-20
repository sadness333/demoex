# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderCard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QFrame, QLabel, QVBoxLayout)

class Ui_OrderCard(object):
    def setupUi(self, OrderCard):
        if not OrderCard.objectName():
            OrderCard.setObjectName(u"OrderCard")
        OrderCard.resize(800, 130)
        OrderCard.setStyleSheet(u"background-color: #fff; color: #000; font-size: 18px; border: 2px solid black")
        self.VLayout = QFrame(OrderCard)
        self.VLayout.setObjectName(u"VLayout")
        self.VLayout.setGeometry(QRect(0, 0, 800, 130))
        self.verticalLayout_2 = QVBoxLayout(self.VLayout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.product_name = QLabel(self.VLayout)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.product_name)

        self.quantity_of_products = QLabel(self.VLayout)
        self.quantity_of_products.setObjectName(u"quantity_of_products")
        self.quantity_of_products.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.quantity_of_products)

        self.date_of_create = QLabel(self.VLayout)
        self.date_of_create.setObjectName(u"date_of_create")
        self.date_of_create.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.date_of_create)


        self.retranslateUi(OrderCard)

        QMetaObject.connectSlotsByName(OrderCard)
    # setupUi

    def retranslateUi(self, OrderCard):
        OrderCard.setWindowTitle(QCoreApplication.translate("OrderCard", u"Form", None))
        self.product_name.setText(QCoreApplication.translate("OrderCard", u"product_name", None))
        self.quantity_of_products.setText(QCoreApplication.translate("OrderCard", u"quantity_of_products", None))
        self.date_of_create.setText(QCoreApplication.translate("OrderCard", u"date_of_create", None))
    # retranslateUi

