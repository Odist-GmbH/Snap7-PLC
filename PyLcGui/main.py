import sys
from PyLcSnap7 import S7Conn
from qdarkstyle import load_stylesheet_pyqt5
from PyLcGui.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        self.plc = obj()
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handle_btn_connect)


    def handle_btn_connect(self):
        ip = self.lineEdit.text()
        self.plc.ip = ip
        self.plc.connect()



def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet_pyqt5())
    gui = MainWindow(obj=S7Conn)
    gui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
