from anaekranui import Ui_AnaPencere
from personel_ekle import *
from PyQt5.QtWidgets import *
from db_islemleri import *
from talepekle import *
from kapanantalepler import Kapanantalepler
from personelguncellesil import PersonelGuncelleSil
import time

class Anaekran(QMainWindow,Ui_AnaPencere):
    def __init__(self,personel_id):
        super(Anaekran,self).__init__()
        self.personel_id = personel_id

        self.karsilama()

    def karsilama(self):
        self.setupUi(self)
        # self.setupUi(self)
        #menülerin yönlendirilmesi
        self.actionTalep_A.triggered.connect(self.talep_ekle)
        self.actionPersonel_Ekle.triggered.connect(self.personel_ekle)
        self.actionDevam_Eden_Talepler.triggered.connect(self.karsilama)
        self.actionKapanan_Talepler.triggered.connect(self.fkapanan)
        self.actionPersnel_G_ncelle_Sil.triggered.connect(self.fpersonelgs)
        self.tableWidget.setRowCount(0)
        self.facik_isler()

    def facik_isler(self):
        isler = session.query(Talep).filter(or_(Talep.talep_durumu ==1,Talep.talep_durumu ==2)).all()
        self.tableWidget.setRowCount(len(isler))
        k = 0
        for a in isler:
            if a.talep_durumu==1:
                self.tableWidget.setItem(k, 0, QTableWidgetItem("Açık"))
            else:
                self.tableWidget.setItem(k, 0, QTableWidgetItem("Onayda"))

            # self.tableWidget.setItem(k,0,  QTableWidgetItem(a.talep_durumu))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(a.talep_adi))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(a.talep_acilis))
            self.tableWidget.setItem(k,3,QTableWidgetItem(a.talep_tanimi))
            # if a.talep_durumu==1:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Açık"))
            # else:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Onayda"))



            self.tableWidget.setItem(k, 4, QTableWidgetItem(session.query(Personel).filter(Personel.personel_id==a.talep_giden).value(Personel.personel_adi)))
            if a.talep_onemi == 0:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Önemli"))
            elif a.talep_onemi == 1:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Normal"))
            elif a.talep_onemi == 2:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Önemsiz"))
            buton = QPushButton(self)
            buton.setText("Onayla")
            buton.setObjectName(str(a.talep_id))
            buton.clicked.connect(self.kapat)
            self.tableWidget.setCellWidget(k,6,buton)
            k+=1

    def kapat(self):
        try:
            session.query(Talep).filter(Talep.talep_id==int(self.sender().objectName())).update({Talep.talep_durumu:3,Talep.talep_kapanis:time.asctime(time.localtime(time.time()))}, synchronize_session=False)
            session.commit()
            self.facik_isler()

            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()


        except:

            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Hatalı")
            dialog.show()

        # session.execute(guncel)
        # session.execute(update(Talep).values(Talep.talep_durumu==3).where(Talep.talep_id==int(self.sender().objectName())))


    def personel_ekle(self):
        self.setCentralWidget(PersonelEkleme())

    def talep_ekle(self):
        self.setCentralWidget(TalepEkleme(self.personel_id))

    def fkapanan(self):
        self.setCentralWidget(Kapanantalepler(self.personel_id))

    def fpersonelgs(self):
        self.setCentralWidget(PersonelGuncelleSil(1))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran(1)
    pencere.show()
    sys.exit(app.exec_())