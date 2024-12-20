# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnerCard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QVBoxLayout)


class Ui_PartnerCard(object):
    def setupUi(self, PartnerCard):
        if not PartnerCard.objectName():
            PartnerCard.setObjectName(u"PartnerCard")
        PartnerCard.resize(900, 180)
        self.PartnerCardVBox = QFrame(PartnerCard)
        self.PartnerCardVBox.setObjectName(u"PartnerCardVBox")
        self.PartnerCardVBox.setGeometry(QRect(0, 0, 900, 180))
        self.PartnerCardVBox.setStyleSheet(u"background: white;  color: black; font-size: 15px; padding: 0px")
        self.horizontalLayout = QHBoxLayout(self.PartnerCardVBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalFrame = QFrame(self.PartnerCardVBox)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"border: 0.5px solid black;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FirstColumn = QFrame(self.horizontalFrame)
        self.FirstColumn.setObjectName(u"FirstColumn")
        self.FirstColumn.setStyleSheet(u"border: none; padding: 0;")
        self.verticalLayout = QVBoxLayout(self.FirstColumn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PartnerTypeAndName = QLabel(self.FirstColumn)
        self.PartnerTypeAndName.setObjectName(u"PartnerTypeAndName")
        self.PartnerTypeAndName.setStyleSheet(u"padding: 0")

        self.verticalLayout.addWidget(self.PartnerTypeAndName)

        self.BossName = QLabel(self.FirstColumn)
        self.BossName.setObjectName(u"BossName")
        self.BossName.setStyleSheet(u"padding: 0")

        self.verticalLayout.addWidget(self.BossName)

        self.PhoneNumber = QLabel(self.FirstColumn)
        self.PhoneNumber.setObjectName(u"PhoneNumber")
        self.PhoneNumber.setStyleSheet(u"padding: 0")

        self.verticalLayout.addWidget(self.PhoneNumber)

        self.Rank = QLabel(self.FirstColumn)
        self.Rank.setObjectName(u"Rank")
        self.Rank.setStyleSheet(u"padding: 0")

        self.verticalLayout.addWidget(self.Rank)

        self.horizontalLayout_2.addWidget(self.FirstColumn)

        self.DiscountPercentage = QLabel(self.horizontalFrame)
        self.DiscountPercentage.setObjectName(u"DiscountPercentage")
        self.DiscountPercentage.setStyleSheet(u"border: none;\n"
                                              "padding: 0")
        self.DiscountPercentage.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.DiscountPercentage)

        self.horizontalLayout.addWidget(self.horizontalFrame)

        self.EditButton = QPushButton(self.PartnerCardVBox)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setMinimumSize(QSize(0, 160))
        self.EditButton.setMaximumSize(QSize(100, 16777215))
        self.EditButton.setStyleSheet(u"background-color: #67BA80;   border-radius: 10px")

        self.horizontalLayout.addWidget(self.EditButton)

        self.GetOrdersListButton = QPushButton(self.PartnerCardVBox)
        self.GetOrdersListButton.setObjectName(u"GetOrdersListButton")
        self.GetOrdersListButton.setMinimumSize(QSize(0, 160))
        self.GetOrdersListButton.setMaximumSize(QSize(180, 16777215))
        self.GetOrdersListButton.setStyleSheet(u"background-color: #67BA80;   border-radius: 10px")

        self.horizontalLayout.addWidget(self.GetOrdersListButton)

        self.retranslateUi(PartnerCard)

        QMetaObject.connectSlotsByName(PartnerCard)

    # setupUi

    def retranslateUi(self, PartnerCard):
        PartnerCard.setWindowTitle(QCoreApplication.translate("PartnerCard", u"Form", None))
        self.PartnerTypeAndName.setText(QCoreApplication.translate("PartnerCard", u"PartnerTypeAndName", None))
        self.BossName.setText(QCoreApplication.translate("PartnerCard", u"BossName", None))
        self.PhoneNumber.setText(QCoreApplication.translate("PartnerCard", u"PhoneNumber", None))
        self.Rank.setText(QCoreApplication.translate("PartnerCard", u"Rank", None))
        self.DiscountPercentage.setText(
            QCoreApplication.translate("PartnerCard", u"<html><head/><body><p>DiscountPercentage</p></body></html>",
                                       None))
        self.EditButton.setText(
            QCoreApplication.translate("PartnerCard", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c\n"
                                                      "\u043f\u0430\u0440\u0442\u043d\u0451\u0440\u0430", None))
        self.GetOrdersListButton.setText(QCoreApplication.translate("PartnerCard", u"PushButton1", None))
    # retranslateUi
