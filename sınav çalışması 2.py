# İç içe iki döngü kullanır; ilki sayıları gezer, ikincisi o sayının bölenlerini bulup toplar.

limit=500
for sayi in range(2, limit):
    toplam=0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i

    if toplam == sayi:
        print(f"Mükemmel sayı bulundu")