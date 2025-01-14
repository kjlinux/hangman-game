from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Widget Example")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create two example widgets
        self.page1 = QWidget()
        self.page2 = QWidget()

        # Set up page 1
        layout1 = QVBoxLayout()
        label1 = QLabel("This is page 1")
        button1 = QPushButton("Go to page 2")
        button1.clicked.connect(self.show_page2)
        layout1.addWidget(label1)
        layout1.addWidget(button1)
        self.page1.setLayout(layout1)

        # Set up page 2
        layout2 = QVBoxLayout()
        label2 = QLabel("This is page 2")
        button2 = QPushButton("Go to page 1")
        button2.clicked.connect(self.show_page1)
        layout2.addWidget(label2)
        layout2.addWidget(button2)
        self.page2.setLayout(layout2)

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Show the first page
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())