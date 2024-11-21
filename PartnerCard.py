# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnerCard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(658, 182)
        self.PartnerCard = QFrame(Form)
        self.PartnerCard.setObjectName(u"PartnerCard")
        self.PartnerCard.setGeometry(QRect(0, 0, 581, 131))
        self.PartnerCard.setStyleSheet(u"background: white; border: 2px solid black; color: black; font-size: 15px; padding: 0px")
        self.horizontalLayout = QHBoxLayout(self.PartnerCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FirstColumn = QFrame(self.PartnerCard)
        self.FirstColumn.setObjectName(u"FirstColumn")
        self.FirstColumn.setStyleSheet(u"border: none; padding: 0;")
        self.verticalLayout = QVBoxLayout(self.FirstColumn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PartnerType = QLabel(self.FirstColumn)
        self.PartnerType.setObjectName(u"PartnerType")
        self.PartnerType.setStyleSheet(u"padding: 0")

        self.verticalLayout.addWidget(self.PartnerType)

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


        self.horizontalLayout.addWidget(self.FirstColumn)

        self.DiscountPercentage = QLabel(self.PartnerCard)
        self.DiscountPercentage.setObjectName(u"DiscountPercentage")
        self.DiscountPercentage.setStyleSheet(u"border: none;\n"
"padding: 0")
        self.DiscountPercentage.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.DiscountPercentage)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PartnerType.setText(QCoreApplication.translate("Form", u"PartnerTypeAndName", None))
        self.BossName.setText(QCoreApplication.translate("Form", u"BossName", None))
        self.PhoneNumber.setText(QCoreApplication.translate("Form", u"PhoneNumber", None))
        self.Rank.setText(QCoreApplication.translate("Form", u"Rank", None))
        self.DiscountPercentage.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>DiscountPercentage</p></body></html>", None))
    # retranslateUi

