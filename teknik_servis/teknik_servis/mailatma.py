import smtplib                           #smtplib modulunu projemize ekledik
# Hesap bilgilerimiz
kullanıcı="sinanurun24@gmail.com"
kullanıcı_sifresi = '24Birgul24'
alıcı = '1sinanurun1@mail.com'            # alıcının mail adresi
konu = 'Selam'
msj = 'Naber!'
# bilgileri bir metinde derledik
email_text = """
From: {}
To: {}
Subject: {}
{}
""" .format(kullanıcı,alıcı, konu, msj)
try:
    server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
    server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
    server.login(kullanıcı, kullanıcı_sifresi)   # Gmail SMTP server'ına giriş yaptık
    server.sendmail(kullanıcı, alıcı, email_text) # Mail'imizi gönderdik
    server.close()     # SMTP serverimizi kapattık
    print ('email gönderildi')
except:
    print("bir hata oluştu")