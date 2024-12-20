# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnersPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLayout, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)

class Ui_PartnersPage(object):
    def setupUi(self, PartnersPage):
        if not PartnersPage.objectName():
            PartnersPage.setObjectName(u"PartnersPage")
        PartnersPage.resize(736, 481)
        PartnersPage.setStyleSheet(u"background-color: #fff")
        self.verticalLayout = QVBoxLayout(PartnersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(PartnersPage)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMouseTracking(False)
        self.verticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.LeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.LeftSpacer)

        self.Icon = QLabel(self.verticalFrame)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setMaximumSize(QSize(50, 50))
        self.Icon.setMouseTracking(False)
        self.Icon.setPixmap(QPixmap(u"../icons/Master_pol.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Icon)

        self.Title = QLabel(self.verticalFrame)
        self.Title.setObjectName(u"Title")
        self.Title.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMinimumSize(QSize(0, 0))
        self.Title.setMaximumSize(QSize(100, 50))
        self.Title.setMouseTracking(False)
        self.Title.setStyleSheet(u"color: black; font-size: 20px")
        self.Title.setMargin(5)

        self.horizontalLayout.addWidget(self.Title)

        self.RightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.RightSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.verticalFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(56, 361))
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 698, 359))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.Button = QPushButton(self.verticalFrame)
        self.Button.setObjectName(u"Button")
        self.Button.setMouseTracking(False)
        self.Button.setStyleSheet(u"background-color: #67BA80;  color: bkack; font-size: 15px; border: 0px\n"
"")

        self.verticalLayout_2.addWidget(self.Button)


        self.verticalLayout.addWidget(self.verticalFrame)


        self.retranslateUi(PartnersPage)

        QMetaObject.connectSlotsByName(PartnersPage)
    # setupUi

    def retranslateUi(self, PartnersPage):
        PartnersPage.setWindowTitle(QCoreApplication.translate("PartnersPage", u"Form", None))
        self.Icon.setText("")
        self.Title.setText(QCoreApplication.translate("PartnersPage", u"<html><head/><body><p>Title</p></body></html>", None))
        self.Button.setText(QCoreApplication.translate("PartnersPage", u"PushButton", None))
    # retranslateUi

