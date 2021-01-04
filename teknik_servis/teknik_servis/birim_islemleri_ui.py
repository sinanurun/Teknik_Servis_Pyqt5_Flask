# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'birim_islemleri_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(766, 550)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 190, 671, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 50, 261, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.birimAdNGirinizLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.birimAdNGirinizLabel.setObjectName("birimAdNGirinizLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birimAdNGirinizLabel)
        self.birim_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.birim_adi.setObjectName("birim_adi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birim_adi)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Birim Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sil"))
        self.birimAdNGirinizLabel.setText(_translate("Form", "Birim Adını Giriniz"))
        self.pushButton.setText(_translate("Form", "Yeni Birim Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
