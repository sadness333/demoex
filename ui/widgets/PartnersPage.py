# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnersPage.ui'
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
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PartnersPage(object):
    def setupUi(self, PartnersPage):
        if not PartnersPage.objectName():
            PartnersPage.setObjectName(u"PartnersPage")
        PartnersPage.resize(735, 570)
        PartnersPage.setStyleSheet(u"background-color: #fff")
        self.verticalLayout = QVBoxLayout(PartnersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(PartnersPage)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 70))
        self.label.setPixmap(QPixmap(u"ui/icons/Master_pol.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.Title = QLabel(self.verticalFrame)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(200, 0))
        self.Title.setMaximumSize(QSize(200, 50))
        self.Title.setStyleSheet(u"color: black; font-size: 20px")

        self.horizontalLayout.addWidget(self.Title)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.verticalFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 398))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.Button = QPushButton(self.verticalFrame)
        self.Button.setObjectName(u"Button")
        self.Button.setStyleSheet(u"background-color: #67BA80;  color: bkack; font-size: 15px; border: 0px\n"
"")

        self.verticalLayout_2.addWidget(self.Button)


        self.verticalLayout.addWidget(self.verticalFrame)


        self.retranslateUi(PartnersPage)

        QMetaObject.connectSlotsByName(PartnersPage)
    # setupUi

    def retranslateUi(self, PartnersPage):
        PartnersPage.setWindowTitle(QCoreApplication.translate("PartnersPage", u"Form", None))
        self.label.setText("")
        self.Title.setText(QCoreApplication.translate("PartnersPage", u"<html><head/><body><p>Title</p></body></html>", None))
        self.Button.setText(QCoreApplication.translate("PartnersPage", u"PushButton", None))
    # retranslateUi

