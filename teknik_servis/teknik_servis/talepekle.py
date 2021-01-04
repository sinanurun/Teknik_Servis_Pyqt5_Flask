from talepformuui import Ui_TalepEkleme
from PyQt5.QtWidgets import *
from db_islemleri import *
import sys
import time
class TalepEkleme(QWidget,Ui_TalepEkleme):
    def __init__(self,personel_id):
        self.k_id = personel_id
        super(TalepEkleme,self).__init__()
        self.setupUi(self)

        self.blistesi = birimistele()
        self.birim_idleri=[]

        for x in self.blistesi:
            self.talepbirimi.addItem(x.birim_adi,x.birim_id)
            self.birim_idleri.append(x.birim_id)

        self.personellistele()
        self.talepbirimi.currentIndexChanged.connect(self.personellistele)

        self.onay.clicked.connect(self.onayla)

    def personellistele(self):
        self.yetkilipersonel.clear()
        try:
            gelen = self.sender()
            print(gelen.currentData())
            birimid = gelen.currentIndex()+1
        except:
            birimid = 1
        finally:
            personeller = session.query(Personel).filter(Personel.birim_id == birimid).filter(Personel.mevki_id == 3).all()
        self.personelid = []
        for x in personeller:
            self.yetkilipersonel.addItem(x.personel_adi)
            self.personelid.append(x.personel_id)

    def onayla(self):
        try:
            talep_bilgisi = [self.talepadi.text(),
                                self.taleptanimi.text(),
                                1,
                                self.k_id,
                             self.personelid[self.yetkilipersonel.currentIndex()],
                             self.taleponemi.currentIndex(),
                             self.talenotu.text(),
                             time.asctime(time.localtime(time.time())),
                             self.birim_idleri[self.talepbirimi.currentIndex()]]
            talep_ekle(talep_bilgisi)
            # print(talep_bilgisi)
            dialog = QMessageBox(self)
            islem = QLabel(dialog,text="İşlem Başarılı")
            dialog.show()
        except:

            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Hatalı")
            dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = TalepEkleme(1)
    pencere.show()
    sys.exit(app.exec_())