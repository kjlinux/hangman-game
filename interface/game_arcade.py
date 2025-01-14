from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.backButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.backButton)

        self.pseudoTimer = QLabel(self.widget)
        self.pseudoTimer.setObjectName(u"pseudoTimer")
        self.pseudoTimer.setFont(font)
        self.pseudoTimer.setFrameShape(QFrame.Shape.NoFrame)
        self.pseudoTimer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.pseudoTimer)

        self.level = QLabel(self.widget)
        self.level.setObjectName(u"level")
        self.level.setFont(font)
        self.level.setFrameShape(QFrame.Shape.NoFrame)
        self.level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.level)

        self.luck = QLabel(self.widget)
        self.luck.setObjectName(u"luck")
        self.luck.setFont(font)
        self.luck.setFrameShape(QFrame.Shape.NoFrame)
        self.luck.setFrameShadow(QFrame.Shadow.Sunken)
        self.luck.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.luck)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.addWidget()

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

