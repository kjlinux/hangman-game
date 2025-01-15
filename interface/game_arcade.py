from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QStackedWidget)
from components.chronometer import Chronometer
from components.step import Step
from components.luck import Luck
import source_rc

class GameArcade(object):
    last_game_box_filled = Signal()
    def setupUi(self, MainWindow, game_boxes):
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

        self.chronometer = Chronometer(self.widget)
        self.chronometer.setObjectName(u"chronometer")
        self.horizontalLayout.addWidget(self.chronometer)

        self.step = Step(self.widget)
        self.step.setObjectName(u"step")
        self.horizontalLayout.addWidget(self.step)

        self.luck = Luck(self.widget)
        self.luck.setObjectName(u"luck")
        self.horizontalLayout.addWidget(self.luck)

        self.verticalLayout_2.addWidget(self.widget)
        
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        for game_box in game_boxes:
            self.stackedWidget.addWidget(game_box)
            game_box.all_letters_filled.connect(self.print_coucou)
        
        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def get_luck(self):
        return self.luck
    
    def get_step(self):
        return self.step
    
    def next_game_box(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)
        
    def get_current_game_box(self):
        current_game_box = self.stackedWidget.currentWidget()
        return current_game_box
        
    def check_last_game_box_filled(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index == self.stackedWidget.count() - 1:
            current_game_box = self.get_current_game_box()
            if all(line_edit.text().isalpha() for line_edit in current_game_box.line_edits):
                self.last_game_box_filled.emit()
