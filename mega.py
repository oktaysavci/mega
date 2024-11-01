from mega import Mega


email = input("Lütfen MEGA e-posta adresinizi girin: ")
password = input("Lütfen MEGA şifrenizi girin: ")


mega = Mega()
m = mega.login(email, password)


dosya_yolu = input("Lütfen yüklemek istediğiniz dosyanın yolunu girin: ")

dosya = m.upload(dosya_yolu)

baglanti = m.get_upload_link(dosya)
print(f"Dosya başarıyla yüklendi. Erişim bağlantısı: {baglanti}")
