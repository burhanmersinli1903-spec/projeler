# Liste taranırken karşılaşılan  ilk tek sayı(7) ekrana yazdırılır ve işlem biter.

sayilar = [2, 4, 6, 7, 8, 10]
for s in sayilar:
    if s % 2 != 0:
        print("İlk tek sayı:", s)
        break
