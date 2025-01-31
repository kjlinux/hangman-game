# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_option.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from components.select_option_button import SelectOptionButton
from .select_number import SelectNumber

class SelectOption(object):
    def __init__(self, cube):
        self.cube = cube
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 480)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, 0)
        self.selectLabel = QLabel(self.centralwidget)
        self.selectLabel.setObjectName(u"selectLabel")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(48)
        self.selectLabel.setFont(font)
        self.selectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.selectLabel)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(14)
        font1.setBold(True)
        
        for element in ["Option1", "Option2", "Option3"]:
                elementButton = SelectOptionButton(element)
                elementButton.option_clicked.connect(self.on_option_clicked)
                self.horizontalLayout_3.addWidget(elementButton)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, -1, 300, -1)
        self.nextButton = QPushButton(self.widget_2)
        self.nextButton.setObjectName(u"nextButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        self.nextButton.setFont(font2)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.hide()

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.nextButton.clicked.connect(self.on_next_button_clicked)
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi
    
    def on_option_clicked(self, option):
        if (self.nextButton.isHidden()):
            self.nextButton.show()
            
        if option not in self.cube["options"]:
                self.cube["options"].append(option)
        else:
                self.cube["options"].remove(option)
        
    def on_next_button_clicked(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.select_number = SelectNumber(self.cube)
        self.select_number.setupUi(main_window)

        main_window.resize(current_size)

