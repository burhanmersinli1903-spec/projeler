maas=float(input("Aylık maaşınızı giriniz(TL):"))
mesai_saati=float(input("Yapılan ek mesai süresini giriniz(Saat):"))

mesai_ucreti=mesai_saati * 200
toplam_maas=maas=maas+mesai_ucreti

print("Toplam alacağınız maaş:", toplam_maas,"TL")