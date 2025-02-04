# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)
from .loading import Loading

class SelectNumber(object):
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectLabel = QLabel(self.widget)
        self.selectLabel.setObjectName(u"selectLabel")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(48)
        
        self.cube["rounds"] = 5
        
        self.selectLabel.setFont(font)
        self.selectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.selectLabel)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.horizontalSlider = QSlider(self.widget_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self.update)

        self.verticalLayout_3.addWidget(self.horizontalSlider)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setText("5")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, -1, 300, -1)
        self.startButton = QPushButton(self.widget_2)
        self.startButton.setObjectName(u"startButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        self.startButton.setFont(font2)
        self.startButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.startButton)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.startButton.clicked.connect(self.start)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectLabel.setText(QCoreApplication.translate("MainWindow", u"ROUNDS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi
    
    def update(self, value):
        self.label.setText(str(value))
        self.cube["rounds"] = value
        print(self.cube)
        
    def start(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.loading = Loading()
        self.loading.setupUi(main_window)

        main_window.resize(current_size)

