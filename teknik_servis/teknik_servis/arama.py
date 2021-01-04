from PyQt5.QtWidgets import *
from db_islemleri import *
from arama_ui import Ui_Form
import sys
import pdfkit
import os
from reportlab.pdfgen import canvas

class Arama(QWidget,Ui_Form):
    def __init__(self,k_id):
        super(Arama,self).__init__()
        self.setupUi(self)
        self.farama_isler(False)
        self.blistesi = birimistele()
        for x in self.blistesi:
            self.talepBirimi.addItem(x.birim_adi,x.birim_id)


        self.pushButton.clicked.connect(self.faramasorgusu)
        self.raporlama.clicked.connect(self.faramasorgusurapor)

    def farama_isler(self, isler):
        print(isler)
        if isler == False:
            isler = session.query(Talep).all()
        self.tableWidget.setRowCount(len(isler))
        k = 0
        for a in isler:
            self.tableWidget.setItem(k,0,  QTableWidgetItem(str(a.talep_id)))
            self.tableWidget.setItem(k, 1, QTableWidgetItem(a.talep_adi))
            self.tableWidget.setItem(k, 2, QTableWidgetItem(a.talep_acilis))


            self.tableWidget.setItem(k, 3, QTableWidgetItem(a.talepdurumu.isdurumu_tanimi_adi))



            self.tableWidget.setItem(k, 4, QTableWidgetItem(session.query(Personel).filter(Personel.personel_id==a.talep_giden).value(Personel.personel_adi)))
            self.tableWidget.setItem(k, 5, QTableWidgetItem(a.taleponem.onem_adi))
            
            self.tableWidget.setItem(k,6,QTableWidgetItem(a.talep_kapanis))
            k+=1


    def faramasorgusu(self):
        self.tableWidget.setRowCount(0)
        birim_id = self.talepBirimi.currentData()

        try:
            if self.talep_id.text()!="":
                id = int(self.talep_id.text())
                isler = session.query(Talep).filter(Talep.talep_id == id, Talep.talep_birimi == birim_id).all()
                self.farama_isler(isler)
                return 0
            else:
                isler = session.query(Talep).filter(Talep.talep_birimi == birim_id).all()
                self.farama_isler(isler)
                return 0
        except:
            self.farama_isler(False)    

    def faramasorgusurapor(self):
        self.tableWidget.setRowCount(0)
        birim_id = self.talepBirimi.currentData()
        options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

        try:
            if self.talep_id.text()!="":
                id = int(self.talep_id.text())
                isler = session.query(Talep).filter(Talep.talep_id == id, Talep.talep_birimi == birim_id).all()
            else:
                isler = session.query(Talep).filter(Talep.talep_birimi == birim_id).all()
            
            res = ""
            for talep in isler:
                res += "{:3}, {:20}, {:30}, {:20}, {:20}, {:20}, {:30} <br>".format(talep.talep_id,
                                        talep.talep_adi,
                                        talep.talep_acilis,
                                        talep.talepdurumu.isdurumu_tanimi_adi,
                                        talep.talepgiden.personel_adi,
                                        talep.taleponem.onem_adi,
                                        talep.talep_kapanis)
            pdfkit.from_string(res, "rapor.pdf", options=options)
            self.farama_isler(isler)
            return 0
        except:
            self.farama_isler(False)         

        # session.execute(guncel)
        # session.execute(update(Talep).values(Talep.talep_durumu==3).where(Talep.talep_id==int(self.sender().objectName())))

#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     pencere = Kapanantalepler(1)
#     pencere.show()
#     sys.exit(app.exec_())