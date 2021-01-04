from PyQt5.QtWidgets import *
from db_islemleri import *
from onem_islemleri_ui import Ui_Form
import sys

class Onemislemleri(QWidget,Ui_Form):
    def __init__(self,k_id):
        super(Onemislemleri,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.onem_adi.clear()
        self.pushButton.clicked.connect(self.fonemekle)
        self.fonemislemleri()

    def fonemislemleri(self):
        self.sozluk = {}
        onemler = onem_listele()
        self.tableWidget.setRowCount(len(onemler))
        k = 0
        for a in onemler:
            self.tableWidget.setItem(k,0,QTableWidgetItem(str(a.onem_adi)))
            
            buton = QPushButton(self)
            buton.setText("Guncelle")
            buton.setObjectName(str(a.onem_id))
            buton.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(k,1,buton)

            buton2 = QPushButton(self)
            buton2.setText("Sil")
            buton2.setObjectName(str(a.onem_id))
            buton2.clicked.connect(self.fsil)
            self.tableWidget.setCellWidget(k,2,buton2)
            self.sozluk[a.onem_id] = k
            k+=1

    def fguncelle(self):
        gelen = self.sender()
        sira = int(self.sozluk[int(gelen.objectName())])
        onem_id = int(gelen.objectName())
        onem_adi = self.tableWidget.item(sira,0).text()
        a = onem_guncelle(onem_id,onem_adi)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
    
    def fsil(self):
        gelen = self.sender()
        onem_id = int(gelen.objectName())
        a = onem_sil(onem_id)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()

    def fonemekle(self):
        onem_adi = self.onem_adi.text()
        a = onem_ekle(onem_adi)
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