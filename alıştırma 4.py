sayi=(input("sayıyı girin:"))
sonuc=1
for sayilar in sayi:
    if int(sayilar)!=0:
        sonuc=sonuc*int(sayilar)
print(sonuc)