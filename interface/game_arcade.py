from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QStackedWidget, QDialog)
from components.chronometer import Chronometer
from components.step import Step
from components.luck import Luck
from interface.dialog_lose import DialogLose
from interface.dialog_win import DialogWin
from interface.dialog_back import DialogBack
import source_rc

class GameArcade(object):
    last_game_box_full = Signal()
    
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
        
        self.game_boxes = game_boxes
        
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.backButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.clicked.connect(self.on_back_button_clicked)

        self.horizontalLayout.addWidget(self.backButton)

        self.chronometer = Chronometer(self.widget)
        self.chronometer.start()
        self.chronometer.setObjectName(u"chronometer")
        self.horizontalLayout.addWidget(self.chronometer)

        self.step = Step(self.widget)
        self.step.setObjectName(u"step")
        self.horizontalLayout.addWidget(self.step)

        self.luck = Luck(self.widget)
        self.luck.life_lost.connect(self.game_lose)
        self.luck.setObjectName(u"luck")
        self.horizontalLayout.addWidget(self.luck)

        self.verticalLayout_2.addWidget(self.widget)
        
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        for game_box in self.game_boxes:
            game_box.all_letters_filled.connect(self.next_game_box)
            self.stackedWidget.addWidget(game_box)
        
        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.last_game_box_full.connect(self.game_win)
    # setupUi
    def get_luck(self):
        return self.luck
    
    def get_step(self):
        return self.step
    
    def next_game_box(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)
        luck = self.get_luck()
        luck.reset()
        step = self.get_step()
        step.next()
        self.check_last_game_box_filled()
        
    def check_last_game_box_filled(self):
        last_game_box = self.stackedWidget.widget(self.stackedWidget.count() - 1)
        all_filled = all(line_edit.text() for line_edit in last_game_box.findChildren(QLineEdit))
        if all_filled:
            self.last_game_box_full.emit()

    def game_lose(self):
        dialog = QDialog()
        ui = DialogLose()
        ui.setupUi(dialog)
        dialog.exec()
        
    def game_win(self):
        dialog = QDialog()
        ui = DialogWin()
        ui.setupUi(dialog)
        dialog.exec()
        
    def on_back_button_clicked(self):
        dialog = QDialog()
        ui = DialogBack()
        ui.setupUi(dialog)
        dialog.exec()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pseudoTimer.setText(QCoreApplication.translate("MainWindow", u"15:10", None))
        self.level.setText(QCoreApplication.translate("MainWindow", u"\u00e9tape 9", None))
        self.luck.setText(QCoreApplication.translate("MainWindow", u"8 chances", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"Index: animal aquatique", None))
        self.errorStateImage.setText("")
        self.A_1.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.A_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.A_3.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.A_4.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.A_5.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.A_6.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.A_7.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.A_8.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.A_9.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.A_10.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.A_11.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.A_12.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.A_13.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.A_18.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.A_14.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.A_15.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.A_16.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.A_17.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.A_20.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.A_21.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.A_22.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.A_23.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.A_24.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.A_25.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.A_26.setText(QCoreApplication.translate("MainWindow", u"Z", None))
    # retranslateUi