from PyQt5.QtWidgets import *
from db_islemleri import *
from birim_islemleri_ui import Ui_Form
import sys

class Birimislemleri(QWidget,Ui_Form):
    def __init__(self,k_id):
        super(Birimislemleri,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.birim_adi.clear()
        self.pushButton.clicked.connect(self.fbirimekle)
        self.fbirimislemleri()

    def fbirimislemleri(self):
        self.sozluk = {}
        birimler = birimistele()
        self.tableWidget.setRowCount(len(birimler))
        k = 0
        for a in birimler:
            self.tableWidget.setItem(k,0,QTableWidgetItem(str(a.birim_adi)))
            
            buton = QPushButton(self)
            buton.setText("Guncelle")
            buton.setObjectName(str(a.birim_id))
            buton.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(k,1,buton)

            buton2 = QPushButton(self)
            buton2.setText("Sil")
            buton2.setObjectName(str(a.birim_id))
            buton2.clicked.connect(self.fsil)
            self.tableWidget.setCellWidget(k,2,buton2)
            self.sozluk[a.birim_id] = k
            k+=1

    def fguncelle(self):
        gelen = self.sender()
        sira = int(self.sozluk[int(gelen.objectName())])
        birim_id = int(gelen.objectName())
        birim_adi = self.tableWidget.item(sira,0).text()
        a = birim_guncelle(birim_id,birim_adi)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
    
    def fsil(self):
        gelen = self.sender()
        birim_id = int(gelen.objectName())
        a = birim_sil(birim_id)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()

    def fbirimekle(self):
        birim_adi = self.birim_adi.text()
        a = birimekle(birim_adi)
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