from PyQt5.QtWidgets import *
from ui_giris import Ui_giris_ekrani
import sys
from db_islemleri import *
from anakeran import Anaekran
from tpanaekran import TpAnaekran
class GirisPenceresi(QMainWindow,Ui_giris_ekrani):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.g_butonu.clicked.connect(self.kontrol)
    def kontrol(self):
        kkodu = self.k_adi.text()
        ksifre = self.sifre.text()
        onay = kullanici_girisi(kkodu, ksifre)
        if onay == 0:
            self.hatali_giris.setVisible(1)
        elif onay[0] == True and (onay[1]==1 or onay[1]==2):
            self.hide()
            self.ype = Anaekran(onay[2])
            self.ype.show()
            # return print("giriş yapıldı")
        elif onay[0] == True and onay[1]==3:
            self.hide()
            self.ype = TpAnaekran(onay[2])
            self.ype.show()
            # return print("giriş yapıldı")


            # giriş penceresi kapatılıyor
        # ana ekran penceresine yöneldirme yapılıyor


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())