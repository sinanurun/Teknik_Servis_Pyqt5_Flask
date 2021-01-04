# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personelguncellesil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PersonelGuncelleSil(object):
    def setupUi(self, PersonelGuncelleSil):
        PersonelGuncelleSil.setObjectName("PersonelGuncelleSil")
        PersonelGuncelleSil.resize(792, 364)
        self.tableWidget = QtWidgets.QTableWidget(PersonelGuncelleSil)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 751, 341))
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

        self.retranslateUi(PersonelGuncelleSil)
        QtCore.QMetaObject.connectSlotsByName(PersonelGuncelleSil)

    def retranslateUi(self, PersonelGuncelleSil):
        _translate = QtCore.QCoreApplication.translate
        PersonelGuncelleSil.setWindowTitle(_translate("PersonelGuncelleSil", "Personel Güncelleme Silme Ekranı"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PersonelGuncelleSil", "Personel Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PersonelGuncelleSil", "Personel E Posta"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PersonelGuncelleSil", "Personel Şifre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PersonelGuncelleSil", "Personel Birim"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PersonelGuncelleSil", "Personel Mevki"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PersonelGuncelleSil", "Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("PersonelGuncelleSil", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonelGuncelleSil = QtWidgets.QWidget()
    ui = Ui_PersonelGuncelleSil()
    ui.setupUi(PersonelGuncelleSil)
    PersonelGuncelleSil.show()
    sys.exit(app.exec_())

