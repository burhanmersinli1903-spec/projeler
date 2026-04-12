#alan_adi isimli, değeri bilişim olan bir değişken tanımlayarak içinde kaç adet "i" harfli olduğunu
#bulup ekrana yazma

alan_adi="bilişim"
toplam=0
for aranan in alan_adi:
    if aranan=="i":
        toplam=toplam + 1
print("Bu metinde toplam",toplam,"adet i vardır")