from PyQt5.QtWidgets import *
from db_islemleri import *
from mevki_islemleri_ui import Ui_Form
import sys

class Mevkiislemleri(QWidget,Ui_Form):
    def __init__(self,k_id):
        super(Mevkiislemleri,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.mevki_adi.clear()
        self.pushButton.clicked.connect(self.fmevkiekle)
        self.fmevkiislemleri()

    def fmevkiislemleri(self):
        self.sozluk = {}
        mevkiler = mevkilistele()
        self.tableWidget.setRowCount(len(mevkiler))
        k = 0
        for a in mevkiler:
            self.tableWidget.setItem(k,0,QTableWidgetItem(str(a.mevki_adi)))
            
            buton = QPushButton(self)
            buton.setText("Guncelle")
            buton.setObjectName(str(a.mevki_id))
            buton.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(k,1,buton)

            buton2 = QPushButton(self)
            buton2.setText("Sil")
            buton2.setObjectName(str(a.mevki_id))
            buton2.clicked.connect(self.fsil)
            self.tableWidget.setCellWidget(k,2,buton2)
            self.sozluk[a.mevki_id] = k
            k+=1

    def fguncelle(self):
        gelen = self.sender()
        sira = int(self.sozluk[int(gelen.objectName())])
        mevki_id = int(gelen.objectName())
        mevki_adi = self.tableWidget.item(sira,0).text()
        a = mevki_guncelle(mevki_id,mevki_adi)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
    
    def fsil(self):
        gelen = self.sender()
        mevki_id = int(gelen.objectName())
        a = mevki_sil(mevki_id)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()

    def fmevkiekle(self):
        mevki_adi = self.mevki_adi.text()
        a = mevkiekle(mevki_adi)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()   


#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     pencere = Kapanantalepler(1)
#     pencere.show()
#     sys.exit(app.exec_())