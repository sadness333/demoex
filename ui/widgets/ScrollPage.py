# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScrollPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ScrollPage(object):
    def setupUi(self, ScrollPage):
        if not ScrollPage.objectName():
            ScrollPage.setObjectName(u"ScrollPage")
        ScrollPage.resize(619, 447)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScrollPage.sizePolicy().hasHeightForWidth())
        ScrollPage.setSizePolicy(sizePolicy)
        ScrollPage.setStyleSheet(u"background-color: #fff;")
        self.verticalLayout = QVBoxLayout(ScrollPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(ScrollPage)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(self.verticalFrame)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"color: black; font-size: 20px")

        self.verticalLayout_2.addWidget(self.Title)

        self.scrollArea = QScrollArea(self.verticalFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 581, 350))
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


        self.retranslateUi(ScrollPage)

        QMetaObject.connectSlotsByName(ScrollPage)
    # setupUi

    def retranslateUi(self, ScrollPage):
        ScrollPage.setWindowTitle(QCoreApplication.translate("ScrollPage", u"Form", None))
        self.Title.setText(QCoreApplication.translate("ScrollPage", u"<html><head/><body><p align=\"center\">Title</p></body></html>", None))
        self.Button.setText(QCoreApplication.translate("ScrollPage", u"PushButton", None))
    # retranslateUi

