# for sayıyı her bir sayıyı sırayla sayi değişkenine atar. Biz de her adımda bu sayıyı
#toplam değişkenine ekleriz.

sayilar =[10, 20, 30 , 40, 50]
toplam =0

for sayi in sayilar:
    toplam=toplam + sayi

print("Listenin toplamı:", toplam)