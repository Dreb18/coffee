import sys, sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()   

    def run(self):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        c1, c2 = 0, 0
        self.tableWidget.setColumnWidth(0, 25)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(4, 480)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 50)
        for i in result:
            for j in i:
                self.tableWidget.setItem(c1, c2, QTableWidgetItem(str(j)))
                c2 += 1
            c1 += 1
            c2 = 0
        con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
