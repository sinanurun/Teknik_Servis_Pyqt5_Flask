# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talepformu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TalepEkleme(object):
    def setupUi(self, TalepEkleme):
        TalepEkleme.setObjectName("TalepEkleme")
        TalepEkleme.resize(607, 364)
        self.formLayoutWidget = QtWidgets.QWidget(TalepEkleme)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 10, 361, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.talepAdiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepAdiLabel.setObjectName("talepAdiLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.talepAdiLabel)
        self.talepadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.talepadi.setObjectName("talepadi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.talepadi)
        self.talepTRLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepTRLabel.setObjectName("talepTRLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.talepTRLabel)
        self.yetkiliPersonelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yetkiliPersonelLabel.setObjectName("yetkiliPersonelLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yetkiliPersonelLabel)
        self.talepNemiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepNemiLabel.setObjectName("talepNemiLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.talepNemiLabel)
        self.talepTanMLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepTanMLabel.setObjectName("talepTanMLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.talepTanMLabel)
        self.taleptanimi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.taleptanimi.setObjectName("taleptanimi")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.taleptanimi)
        self.talepNotuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talepNotuLabel.setObjectName("talepNotuLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.talepNotuLabel)
        self.talenotu = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.talenotu.setObjectName("talenotu")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.talenotu)
        self.taleponemi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.taleponemi.setObjectName("taleponemi")
        self.taleponemi.addItem("")
        self.taleponemi.addItem("")
        self.taleponemi.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taleponemi)
        self.talepbirimi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.talepbirimi.setObjectName("talepbirimi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.talepbirimi)
        self.yetkilipersonel = QtWidgets.QComboBox(self.formLayoutWidget)
        self.yetkilipersonel.setObjectName("yetkilipersonel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yetkilipersonel)
        self.onay = QtWidgets.QPushButton(TalepEkleme)
        self.onay.setGeometry(QtCore.QRect(450, 230, 75, 23))
        self.onay.setObjectName("onay")

        self.retranslateUi(TalepEkleme)
        QtCore.QMetaObject.connectSlotsByName(TalepEkleme)
        TalepEkleme.setTabOrder(self.talepadi, self.talepbirimi)
        TalepEkleme.setTabOrder(self.talepbirimi, self.yetkilipersonel)
        TalepEkleme.setTabOrder(self.yetkilipersonel, self.taleponemi)
        TalepEkleme.setTabOrder(self.taleponemi, self.taleptanimi)
        TalepEkleme.setTabOrder(self.taleptanimi, self.talenotu)
        TalepEkleme.setTabOrder(self.talenotu, self.onay)

    def retranslateUi(self, TalepEkleme):
        _translate = QtCore.QCoreApplication.translate
        TalepEkleme.setWindowTitle(_translate("TalepEkleme", "Talep Formu"))
        self.talepAdiLabel.setText(_translate("TalepEkleme", "Talep Adi"))
        self.talepTRLabel.setText(_translate("TalepEkleme", "Talep Birimi"))
        self.yetkiliPersonelLabel.setText(_translate("TalepEkleme", "Yetkili Personel"))
        self.talepNemiLabel.setText(_translate("TalepEkleme", "Talep Önemi"))
        self.talepTanMLabel.setText(_translate("TalepEkleme", "Talep Tanımı"))
        self.talepNotuLabel.setText(_translate("TalepEkleme", "Talep Notu"))
        self.taleponemi.setItemText(0, _translate("TalepEkleme", "Önemli"))
        self.taleponemi.setItemText(1, _translate("TalepEkleme", "Normal"))
        self.taleponemi.setItemText(2, _translate("TalepEkleme", "Önemsiz"))
        self.onay.setText(_translate("TalepEkleme", "Onayla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TalepEkleme = QtWidgets.QWidget()
    ui = Ui_TalepEkleme()
    ui.setupUi(TalepEkleme)
    TalepEkleme.show()
    sys.exit(app.exec_())

