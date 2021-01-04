from PyQt5.QtWidgets import *
from db_islemleri import *
from tpkapananui import Ui_Kapanantalepler
import sys

class Kapanantalepler(QWidget,Ui_Kapanantalepler):
    def __init__(self,k_id):
        super(Kapanantalepler,self).__init__()
        self.personel_id = k_id
        self.fkarsilama()




    def fkarsilama(self):
        self.setupUi(self)
        self.tableWidget.setRowCount(0)
        self.facik_isler()

    def facik_isler(self):
        isler = session.query(Talep).filter(Talep.talep_durumu ==3).filter(Talep.talep_giden==self.personel_id).all()
        self.talepler = {}
        self.tableWidget.setRowCount(len(isler))
        k = 0
        for a in isler:
            self.tableWidget.setItem(k,0,  QTableWidgetItem(str(a.talep_id)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(a.talep_adi))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(a.talep_acilis))
            self.tableWidget.setItem(k, 3, QTableWidgetItem(a.talep_kapanis))

            # if a.talep_durumu==1:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Açık"))
            # else:
            #     self.tableWidget.setItem(k, 3, QTableWidgetItem("Onayda"))



            # self.tableWidget.setItem(k, 4, QTableWidgetItem(session.query(Personel).filter(Personel.personel_id==a.talep_giden).value(Personel.personel_adi)))
            if a.talep_onemi == 0:
                self.tableWidget.setItem(k, 4, QTableWidgetItem("Önemli"))
            elif a.talep_onemi == 1:
                self.tableWidget.setItem(k, 4, QTableWidgetItem("Normal"))
            elif a.talep_onemi == 2:
                self.tableWidget.setItem(k, 4, QTableWidgetItem("Önemsiz"))

            self.tableWidget.setItem(k, 5, QTableWidgetItem(a.talep_tanimi))
            self.tableWidget.setItem(k, 6, QTableWidgetItem(a.talep_notlari))
            k+=1





if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Kapanantalepler(4)
    pencere.show()
    sys.exit(app.exec_())