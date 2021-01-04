# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arama_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(766, 550)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 50, 261, 88))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.birimAdNGirinizLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.birimAdNGirinizLabel.setObjectName("birimAdNGirinizLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birimAdNGirinizLabel)
        self.talep_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.talep_id.setObjectName("talep_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.talep_id)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.talepBirimiLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepBirimiLabel_2.setObjectName("talepBirimiLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.talepBirimiLabel_2)
        self.talepBirimi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.talepBirimi.setObjectName("talepBirimi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.talepBirimi)
        self.raporlama = QtWidgets.QPushButton(self.formLayoutWidget)
        self.raporlama.setObjectName("raporlama")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.raporlama)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 751, 381))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.birimAdNGirinizLabel.setText(_translate("Form", "Talep İd Giriniz"))
        self.pushButton.setText(_translate("Form", "Talep Ara"))
        self.talepBirimiLabel_2.setText(_translate("Form", "Talep Birimi"))
        self.raporlama.setText(_translate("Form", "Raporla"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Talep Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Talep Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Açılış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Talep Durumu"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Yetkili Personel"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Talep Önemi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Kapanış Tarihi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
