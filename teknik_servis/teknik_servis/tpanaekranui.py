# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tpanaekran.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tpanaekran(object):
    def setupUi(self, Tpanaekran):
        Tpanaekran.setObjectName("Tpanaekran")
        Tpanaekran.resize(902, 600)
        self.centralwidget = QtWidgets.QWidget(Tpanaekran)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 821, 261))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Tpanaekran.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tpanaekran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 21))
        self.menubar.setObjectName("menubar")
        self.menuTalep_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuTalep_i_lemleri.setObjectName("menuTalep_i_lemleri")
        Tpanaekran.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tpanaekran)
        self.statusbar.setObjectName("statusbar")
        Tpanaekran.setStatusBar(self.statusbar)
        self.actionPersonel_Ekle = QtWidgets.QAction(Tpanaekran)
        self.actionPersonel_Ekle.setObjectName("actionPersonel_Ekle")
        self.actionPersnel_G_ncelle_Sil = QtWidgets.QAction(Tpanaekran)
        self.actionPersnel_G_ncelle_Sil.setObjectName("actionPersnel_G_ncelle_Sil")
        self.aciktalepler = QtWidgets.QAction(Tpanaekran)
        self.aciktalepler.setObjectName("aciktalepler")
        self.onaybekleyentalepler = QtWidgets.QAction(Tpanaekran)
        self.onaybekleyentalepler.setObjectName("onaybekleyentalepler")
        self.kapanantalepler = QtWidgets.QAction(Tpanaekran)
        self.kapanantalepler.setObjectName("kapanantalepler")
        self.menuTalep_i_lemleri.addAction(self.aciktalepler)
        self.menuTalep_i_lemleri.addAction(self.onaybekleyentalepler)
        self.menuTalep_i_lemleri.addAction(self.kapanantalepler)
        self.menubar.addAction(self.menuTalep_i_lemleri.menuAction())

        self.retranslateUi(Tpanaekran)
        QtCore.QMetaObject.connectSlotsByName(Tpanaekran)

    def retranslateUi(self, Tpanaekran):
        _translate = QtCore.QCoreApplication.translate
        Tpanaekran.setWindowTitle(_translate("Tpanaekran", "Ana Pencere"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Tpanaekran", "Talep Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Tpanaekran", "Talep Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Tpanaekran", "Açılış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Tpanaekran", "Talep Önemi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Tpanaekran", "Talep Tanımı"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Tpanaekran", "Talep Notu"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Tpanaekran", "Talep Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Tpanaekran", "Onaya Gönder"))
        self.label.setText(_translate("Tpanaekran", "Talep İşlemi Seçiniz"))
        self.menuTalep_i_lemleri.setTitle(_translate("Tpanaekran", "Talep işlemleri"))
        self.actionPersonel_Ekle.setText(_translate("Tpanaekran", "Personel Ekle"))
        self.actionPersnel_G_ncelle_Sil.setText(_translate("Tpanaekran", "Persnel Güncelle - Sil"))
        self.aciktalepler.setText(_translate("Tpanaekran", "Açık Talepler"))
        self.onaybekleyentalepler.setText(_translate("Tpanaekran", "Onay Bekleyen Talepler"))
        self.kapanantalepler.setText(_translate("Tpanaekran", "Kapanan Talepler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tpanaekran = QtWidgets.QMainWindow()
    ui = Ui_Tpanaekran()
    ui.setupUi(Tpanaekran)
    Tpanaekran.show()
    sys.exit(app.exec_())

