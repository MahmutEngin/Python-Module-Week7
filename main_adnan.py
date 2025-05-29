import sys
from PyQt6 import QtWidgets, QtCore

from test_adnan import Ui_MainWindow 

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.button_carpi.clicked.connect(self.close)

        self.old_pos = None

    def mousePressEvent(self, event):
        
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint() # PyQt6'da globalPos yerine globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos # PyQt6'da globalPos yerine globalPosition().toPoint()
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint() # Güncel konumu tekrar kaydet

    def mouseReleaseEvent(self, event):
        
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())