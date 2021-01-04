# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personelekle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PersonelEkleme(object):
    def setupUi(self, PersonelEkleme):
        PersonelEkleme.setObjectName("PersonelEkleme")
        PersonelEkleme.resize(607, 364)
        self.formLayoutWidget = QtWidgets.QWidget(PersonelEkleme)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 10, 361, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.talepAdiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepAdiLabel.setObjectName("talepAdiLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.talepAdiLabel)
        self.p_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_adi.setObjectName("p_adi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.p_adi)
        self.talepTanMLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepTanMLabel.setObjectName("talepTanMLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.talepTanMLabel)
        self.p_birim = QtWidgets.QComboBox(self.formLayoutWidget)
        self.p_birim.setObjectName("p_birim")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p_birim)
        self.talepNemiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepNemiLabel.setObjectName("talepNemiLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.talepNemiLabel)
        self.p_eposta = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_eposta.setObjectName("p_eposta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p_eposta)
        self.yetkiliPersonelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yetkiliPersonelLabel.setObjectName("yetkiliPersonelLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yetkiliPersonelLabel)
        self.p_sifre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_sifre.setObjectName("p_sifre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p_sifre)
        self.talepTRLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepTRLabel.setObjectName("talepTRLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.talepTRLabel)
        self.p_mevki = QtWidgets.QComboBox(self.formLayoutWidget)
        self.p_mevki.setObjectName("p_mevki")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.p_mevki)
        self.onay = QtWidgets.QPushButton(PersonelEkleme)
        self.onay.setGeometry(QtCore.QRect(450, 230, 75, 23))
        self.onay.setObjectName("onay")

        self.retranslateUi(PersonelEkleme)
        QtCore.QMetaObject.connectSlotsByName(PersonelEkleme)
        PersonelEkleme.setTabOrder(self.p_adi, self.p_eposta)
        PersonelEkleme.setTabOrder(self.p_eposta, self.p_sifre)
        PersonelEkleme.setTabOrder(self.p_sifre, self.p_birim)
        PersonelEkleme.setTabOrder(self.p_birim, self.p_mevki)
        PersonelEkleme.setTabOrder(self.p_mevki, self.onay)

    def retranslateUi(self, PersonelEkleme):
        _translate = QtCore.QCoreApplication.translate
        PersonelEkleme.setWindowTitle(_translate("PersonelEkleme", "Personel Ekleme Formu"))
        self.talepAdiLabel.setText(_translate("PersonelEkleme", "Personel Adi"))
        self.talepTanMLabel.setText(_translate("PersonelEkleme", "Personel Birim"))
        self.talepNemiLabel.setText(_translate("PersonelEkleme", "Personel E-Posta"))
        self.yetkiliPersonelLabel.setText(_translate("PersonelEkleme", "Personel Şifre"))
        self.talepTRLabel.setText(_translate("PersonelEkleme", "Personel Mevki"))
        self.onay.setText(_translate("PersonelEkleme", "Onayla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonelEkleme = QtWidgets.QWidget()
    ui = Ui_PersonelEkleme()
    ui.setupUi(PersonelEkleme)
    PersonelEkleme.show()
    sys.exit(app.exec_())

