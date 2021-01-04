# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tponaybekleyen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Onaybekleyen(object):
    def setupUi(self, Onaybekleyen):
        Onaybekleyen.setObjectName("Onaybekleyen")
        Onaybekleyen.resize(905, 601)
        self.tableWidget = QtWidgets.QTableWidget(Onaybekleyen)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 821, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(Onaybekleyen)
        self.label.setGeometry(QtCore.QRect(130, 70, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Onaybekleyen)
        QtCore.QMetaObject.connectSlotsByName(Onaybekleyen)

    def retranslateUi(self, Onaybekleyen):
        _translate = QtCore.QCoreApplication.translate
        Onaybekleyen.setWindowTitle(_translate("Onaybekleyen", "Onay Bekleyen Talepler"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Onaybekleyen", "Talep Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Onaybekleyen", "Talep Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Onaybekleyen", "Açılış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Onaybekleyen", "Talep Önemi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Onaybekleyen", "Talep Tanımı"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Onaybekleyen", "Talep Notu"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Onaybekleyen", "Talep Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Onaybekleyen", "Açığa Al"))
        self.label.setText(_translate("Onaybekleyen", "Onay Bekleyen Talepler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Onaybekleyen = QtWidgets.QWidget()
    ui = Ui_Onaybekleyen()
    ui.setupUi(Onaybekleyen)
    Onaybekleyen.show()
    sys.exit(app.exec_())

