from PyQt5.QtWidgets import *
from db_islemleri import *
from kapanantaleplerui import Ui_Kapanantalepler
import sys

class Kapanantalepler(QWidget,Ui_Kapanantalepler):
    def __init__(self,k_id):
        super(Kapanantalepler,self).__init__()
        self.setupUi(self)
        self.fkapali_isler()

    def fkapali_isler(self):
        isler = session.query(Talep).filter(Talep.talep_durumu ==3).all()
        self.tableWidget.setRowCount(len(isler))
        k = 0
        for a in isler:
            self.tableWidget.setItem(k,0,  QTableWidgetItem(str(a.talep_id)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(a.talep_adi))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(a.talep_acilis))


            self.tableWidget.setItem(k, 3, QTableWidgetItem("KAPALI"))



            self.tableWidget.setItem(k, 4, QTableWidgetItem(session.query(Personel).filter(Personel.personel_id==a.talep_giden).value(Personel.personel_adi)))
            if a.talep_onemi == 0:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Önemli"))
            elif a.talep_onemi == 1:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Normal"))
            elif a.talep_onemi == 2:
                self.tableWidget.setItem(k, 5, QTableWidgetItem("Önemsiz"))
            buton = QPushButton(self)
            buton.setText("Aç")
            buton.setObjectName(str(a.talep_id))
            buton.clicked.connect(self.fac)
            self.tableWidget.setCellWidget(k,6,buton)
            k+=1

    def fac(self):
        try:
            session.query(Talep).filter(Talep.talep_id==int(self.sender().objectName())).update({Talep.talep_durumu:1}, synchronize_session=False)
            session.commit()
            self.fkapali_isler()

        except:
            print("hata")
        # session.execute(guncel)
        # session.execute(update(Talep).values(Talep.talep_durumu==3).where(Talep.talep_id==int(self.sender().objectName())))

#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     pencere = Kapanantalepler(1)
#     pencere.show()
#     sys.exit(app.exec_())