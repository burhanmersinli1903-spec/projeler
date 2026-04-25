# Bir kişinin askere gitme uygunluğunu denetleyen bir karar mekanizması kuruluyor.

yas=int(input("yaşınızı giriniz:"))
cinsiyet=input("cinsiyetinizi girin:")

if yas>=20 and yas<=40 and cinsiyet=="Erkek" or cinsiyet=="erkek":
    print("askere gidebilir")
elif cinsiyet=="Kız" or cinsiyet=="kız":
    print("hatalı giriş yaptınız")