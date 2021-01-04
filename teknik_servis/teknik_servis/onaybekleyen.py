from PyQt5.QtWidgets import *
from db_islemleri import *
from tponaybekleyenui import Ui_Onaybekleyen
import sys

class OnayBekleyen(QWidget,Ui_Onaybekleyen):
    def __init__(self,k_id):
        super(OnayBekleyen,self).__init__()
        self.personel_id = k_id
        self.fkarsilama()




    def fkarsilama(self):
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.facik_isler()

    def facik_isler(self):
        isler = session.query(Talep).filter(Talep.talep_durumu ==2).filter(Talep.talep_giden==self.personel_id).all()
        self.talepler = {}
        self.tableWidget.setRowCount(len(isler))
        k = 0
        for a in isler:
            self.tableWidget.setItem(k,0,  QTableWidgetItem(str(a.talep_id)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(a.talep_adi))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(a.talep_acilis))

            # if a.talep_durumu==1:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Açık"))
            # else:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Onayda"))



            # self.tableWidget.setItem(k, 4, QTableWidgetItem(session.query(Personel).filter(Personel.personel_id==a.talep_giden).value(Personel.personel_adi)))
            if a.talep_onemi == 0:
                self.tableWidget.setItem(k, 3, QTableWidgetItem("Önemli"))
            elif a.talep_onemi == 1:
                self.tableWidget.setItem(k, 3, QTableWidgetItem("Normal"))
            elif a.talep_onemi == 2:
                self.tableWidget.setItem(k, 3, QTableWidgetItem("Önemsiz"))

            self.tableWidget.setItem(k, 4, QTableWidgetItem(a.talep_tanimi))
            self.tableWidget.setItem(k, 5, QTableWidgetItem(a.talep_notlari))

            gbuton = QPushButton(self)
            gbuton.setText("Güncelle")
            gbuton.setObjectName(str(a.talep_id))
            gbuton.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(k,6,gbuton)

            obuton = QPushButton(self)
            obuton.setText("Açığa Al")
            obuton.setObjectName(str(a.talep_id))
            obuton.clicked.connect(self.fkapat)
            self.tableWidget.setCellWidget(k,7,obuton)
            self.talepler[a.talep_id]=k
            k+=1


    def fkapat(self):

        try:

            session.query(Talep).filter(Talep.talep_id==int(self.sender().objectName())).update({Talep.talep_durumu:1}, synchronize_session=False)
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


    def fguncelle(self):



        try:
            gelen = int(self.sender().objectName())

            sira = self.talepler[gelen]
            session.query(Talep).filter(Talep.talep_id==gelen).update({Talep.talep_notlari:self.tableWidget.item(sira,5).text()
                                                                                                 }, synchronize_session=False)
            session.commit()
            self.facik_isler()

            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()


        except :

            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Hatalı")
            dialog.show()

        # session.execute(guncel)
        # session.execute(update(Talep).values(Talep.talep_durumu==3).where(Talep.talep_id==int(self.sender().objectName())))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = OnayBekleyen(4)
    pencere.show()
    sys.exit(app.exec_())