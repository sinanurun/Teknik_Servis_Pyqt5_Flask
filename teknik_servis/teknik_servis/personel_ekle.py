from personelekleui import Ui_PersonelEkleme
from PyQt5.QtWidgets import *
from db_islemleri import *
import sys
class PersonelEkleme(QWidget,Ui_PersonelEkleme):
    def __init__(self):
        super(PersonelEkleme,self).__init__()
        self.fbaslat()

    def fbaslat(self):

        self.setupUi(self)
        self.onay.clicked.connect(self.onayla)
        self.ficerik()

    def ficerik(self):
        self.personel_bilgisi = []
        self.p_adi.setText("")
        self.p_eposta.setText("")
        self.p_sifre.setText("")

        self.p_mevki.clear()
        self.mlistesi = mevkilistele()
        for x in self.mlistesi:
            self.p_mevki.addItem(x.mevki_adi)

        self.p_birim.clear()
        self.blistesi = birimistele()
        for x in self.blistesi:
            self.p_birim.addItem(x.birim_adi)



    def onayla(self):

        self.personel_bilgisi = [self.p_adi.text(),
                            self.p_eposta.text(),
                            self.p_sifre.text(),
                            self.p_birim.currentIndex()+1,
                            self.p_mevki.currentIndex()+1]

        # print(self.personel_bilgisi)
        personel_ekle(self.personel_bilgisi)

        dialog = QMessageBox(self)
        islem = QLabel(dialog, text="İşlem Başarılı")
        dialog.show()

        self.ficerik()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = PersonelEkleme()
    pencere.show()
    sys.exit(app.exec_())