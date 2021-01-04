from orm_db import *
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def kullanici_girisi(eposta,sifre):

    pgirisi = session.query(Personel).filter(Personel.personel_eposta == eposta, Personel.personel_sifre == sifre).first()
    try:
        if (pgirisi.personel_adi) :
            return [True,pgirisi.mevki_id,pgirisi.personel_id]
    except:
        return 0

def mevkilistele():
    return session.query(Mevki).all()

def birimistele():
    return session.query(Birim).all()

def personel_ekle(personel):
    # print(personel)
    bilgi =Personel(personel_adi=personel[0],
                    personel_eposta=personel[1],
                    personel_sifre=personel[2],
                    birim_id=int(personel[3]),
                    mevki_id=int(personel[4]))
    session.add(bilgi)
    session.commit()

def talep_ekle(talep):
    print(talep)
    bilgi =Talep(talep_adi=talep[0],talep_tanimi=talep[1],talep_durumu=talep[2],
                 talep_acan=talep[3],talep_giden=talep[4],talep_onemi=talep[5],talep_notlari=talep[6],
                 talep_acilis=talep[7],talep_birimi=talep[8])
    session.add(bilgi)
    session.commit()





