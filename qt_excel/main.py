import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow_UI import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
import os
# import qdarkstyle
from qt_material import apply_stylesheet
import pandas as pd


class My_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(My_MainWindow, self).__init__()
        self.setupUi(self)

        self.table1 = self.tableWidget
        self.table2 = self.tableWidget_2

        self.pushButton_mainfile.clicked.connect(self.get_mainfile)
        self.pushButton_targetfile.clicked.connect(self.get_targetfile)
        self.pushButton.clicked.connect(self.main)
        self.pushButton_remove1.clicked.connect(self.update1)
        # self.pushButton_remove2.clicked.connect(self.update2)

    def get_mainfile(self):
        """
        pushbutton to load main excel file
        :return:
        """
        file = QFileDialog.getOpenFileName(self, "打开文件", "", "Excel File (*.xlsx)")[0]
        self.lineEdit_mainfile.setText(os.path.basename(file))
        df = pd.read_excel(file)
        self.loadExcelData(df,self.table1)

    def get_targetfile(self):
        """
        :return:
        """
        file = QFileDialog.getOpenFileName(self, "打开文件", "", "Excel File (*.xlsx)")[0]
        self.lineEdit_targetfile.setText(os.path.basename(file))
        self.lineEdit_targetfile.setText(os.path.basename(file))
        df = pd.read_excel(file)
        self.loadExcelData(df,self.table2)


    def loadExcelData(self, data,table):
        table.setRowCount(data.shape[0])
        table.setColumnCount(data.shape[1])
        table.setHorizontalHeaderLabels(data.columns)

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(data.iloc[i, j]))
                table.setItem(i, j, item)
        # table.cellClicked.connect(self.onCellClicked)

    # def onCellClicked(self, row, column):
    #     cell_value = self.table.item(row, column).text()
    #     print(f"Selected cell value: {cell_value}")

    def update1(self):
        self.lineEdit_mainfile.setText("")
        self.table1.clear()

    def update2(self):
        self.lineEdit_targetfile.setText("")
        self.table1.clear()

    def main(self):
        # df = pd.read_excel(r'F:\pycharm_project\Appdev\dem01.xlsx')  # 替换为你的 Excel 文件路径
        # self.loadExcelData(df)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = My_MainWindow()

    # setup stylesheet
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    apply_stylesheet(app, theme='light_lightgreen_500.xml')

    window.show()
    app.exec_()
