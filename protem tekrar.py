yas=int(input("Yaşınızı girin:"))
cinsiyet=input("cinsiyetinizi girin:")

if yas>=20 and yas<=40 and cinsiyet =="Erkek" or cinsiyet =="erkek":
    print("askere gidebilir")
elif cinsiyet =="Kız" or cinsiyet =="kız":
    print("askere gidemez")
else:
    print("hatalı giriş yaptınız")