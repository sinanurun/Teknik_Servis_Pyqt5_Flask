from PyQt5.QtWidgets import *
from db_islemleri import *
from personelguncellesilui import Ui_PersonelGuncelleSil
import sys

class PersonelGuncelleSil(QWidget,Ui_PersonelGuncelleSil):
    def __init__(self,k_id):
        super(PersonelGuncelleSil,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)


        self.ftablo()

    def ftablo(self):

        self.sozluk = {}
        self.personeller = session.query(Personel).all()

        for personel,sira in zip(self.personeller,range(len(self.personeller))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira,0,QTableWidgetItem(personel.personel_adi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(personel.personel_eposta))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(personel.personel_sifre))
            mcombo = QComboBox(self)
            self.mlistesi = mevkilistele()
            for x in self.mlistesi:
                mcombo.addItem(x.mevki_adi)
            mcombo.setObjectName("m"+str(personel.personel_id))
            mcombo.setCurrentIndex(personel.mevki_id-1)

            bcombo = QComboBox(self)
            self.blistesi = birimistele()
            for x in self.blistesi:
                bcombo.addItem(x.birim_adi)
            bcombo.setObjectName("b"+str(personel.personel_id))
            bcombo.setCurrentIndex(personel.birim_id-1)
            # self.onay.clicked.connect(self.onayla)

            self.tableWidget.setCellWidget(sira, 3, bcombo)
            self.tableWidget.setCellWidget(sira,4, mcombo)
            # self.tableWidget.setItem(0, 3, QTableWidgetItem(str(personel.birim_id)))
            # self.tableWidget.setItem(0, 4, QTableWidgetItem(str(personel.mevki_id)))

            guncelle = QPushButton(self)
            guncelle.setObjectName("g"+str(personel.personel_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.sozluk[personel.personel_id]=[bcombo,mcombo,sira]
            # self.tableWidget.setCellWidget(0, 5, guncelle)


            sil = QPushButton(self)
            sil.setObjectName("s"+str(personel.personel_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 5, guncelle)
            self.tableWidget.setCellWidget(sira, 6, sil)

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        bcombo = self.sozluk[gelen][0]
        mcombo = self.sozluk[gelen][1]
        sira=  self.sozluk[gelen][2]
        session.query(Personel).filter(Personel.personel_id==gelen).update({Personel.personel_adi:self.tableWidget.item(sira,0).text(),
                                                                            Personel.personel_eposta:self.tableWidget.item(sira,1).text(),
                                                                            Personel.personel_sifre:self.tableWidget.item(sira,2).text(),
                                                                            Personel.birim_id:bcombo.currentIndex()+1,
                                                                            Personel.mevki_id:mcombo.currentIndex()+1,
                                                                           }, synchronize_session=False)
        session.commit()
        self.fbaslangic()
        dialog = QMessageBox(self)
        islem = QLabel(dialog, text="İşlem Başarılı")
        dialog.show()

    def fsil(self):

        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        session.query(Personel).filter(Personel.personel_id==gelen).delete()
        session.commit()
        self.tableWidget.setRowCount(0)
        self.ftablo()
        dialog = QMessageBox(self)
        islem = QLabel(dialog, text="İşlem Başarılı")
        dialog.show()

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     pencere = PersonelGuncelleSil(1)
#     pencere.show()
#     sys.exit(app.exec_())