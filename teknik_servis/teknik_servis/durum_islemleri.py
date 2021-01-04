from PyQt5.QtWidgets import *
from db_islemleri import *
from durum_islemleri_ui import Ui_Form
import sys

class Durumislemleri(QWidget,Ui_Form):
    def __init__(self,k_id):
        super(Durumislemleri,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.durum_adi.clear()
        self.pushButton.clicked.connect(self.fisdurumuekle)
        self.fisdurumuslemleri()

    def fisdurumuslemleri(self):
        self.sozluk = {}
        isdurumlari = isdurumu_listele()
        self.tableWidget.setRowCount(len(isdurumlari))
        k = 0
        for a in isdurumlari:
            self.tableWidget.setItem(k,0,QTableWidgetItem(str(a.isdurumu_tanimi_adi)))
            
            buton = QPushButton(self)
            buton.setText("Guncelle")
            buton.setObjectName(str(a.isdurumu_id))
            buton.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(k,1,buton)

            buton2 = QPushButton(self)
            buton2.setText("Sil")
            buton2.setObjectName(str(a.isdurumu_id))
            buton2.clicked.connect(self.fsil)
            self.tableWidget.setCellWidget(k,2,buton2)
            self.sozluk[a.isdurumu_id] = k
            k+=1

    def fguncelle(self):
        gelen = self.sender()
        sira = int(self.sozluk[int(gelen.objectName())])
        isdurumu_id = int(gelen.objectName())
        isdurumu_tanimi_adi = self.tableWidget.item(sira,0).text()
        a = isdurumu_guncelle(isdurumu_id,isdurumu_tanimi_adi)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
    
    def fsil(self):
        gelen = self.sender()
        isdurum_id = int(gelen.objectName())
        a = isdurumu_sil(isdurum_id)
        if a == 1:
            self.fbaslangic()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()

    def fisdurumuekle(self):
        isdurumu_tanimi_adi = self.durum_adi.text()
        a = isdurumu_ekle(isdurumu_tanimi_adi)
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