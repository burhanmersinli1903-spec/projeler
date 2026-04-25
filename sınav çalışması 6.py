# Bir öğrencinin sınav sonuçlarına göre başarı durumunu (geçti/kaldı) hesaplayan basit bir python
# programı yapılıyor.

dmiktar=int(input("Doğru sayısı"))
ymiktar=int(input("Yanlış sayısı"))
if dmiktar>=ymiktar:
    print("Dersten geçti")
else:
    print("Dersten kaldı")