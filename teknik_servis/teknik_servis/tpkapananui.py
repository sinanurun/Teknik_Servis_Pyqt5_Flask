# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tpkapanan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Kapanantalepler(object):
    def setupUi(self, Kapanantalepler):
        Kapanantalepler.setObjectName("Kapanantalepler")
        Kapanantalepler.resize(905, 601)
        self.tableWidget = QtWidgets.QTableWidget(Kapanantalepler)
        self.tableWidget.setGeometry(QtCore.QRect(90, 120, 741, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.label = QtWidgets.QLabel(Kapanantalepler)
        self.label.setGeometry(QtCore.QRect(140, 30, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Kapanantalepler)
        QtCore.QMetaObject.connectSlotsByName(Kapanantalepler)

    def retranslateUi(self, Kapanantalepler):
        _translate = QtCore.QCoreApplication.translate
        Kapanantalepler.setWindowTitle(_translate("Kapanantalepler", "Kapanan Talepler"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Kapanantalepler", "Talep Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Kapanantalepler", "Talep Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Kapanantalepler", "Açılış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Kapanantalepler", "Kapanaış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Kapanantalepler", "Talep Önemi"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Kapanantalepler", "Talep Tanımı"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Kapanantalepler", "Talep Notu"))
        self.label.setText(_translate("Kapanantalepler", "Kapanan Talepler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kapanantalepler = QtWidgets.QWidget()
    ui = Ui_Kapanantalepler()
    ui.setupUi(Kapanantalepler)
    Kapanantalepler.show()
    sys.exit(app.exec_())

