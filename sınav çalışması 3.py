# İlk döngü sözlük yapısını doldurur, ikinci döngü ise verileri belirli bir kritere göre filtreler.

metin="elma armut elma çilek elma armut"
kelimeler=metin.split()
sayac={}

for kelime in kelimeler:
    if kelime in sayac:
        sayac[kelime] += 1
    else:
        sayac[kelime] = 1

for kelime, adet in sayac.items():
    if adet >= 2:
        print(f"Sık kıullanılan: {kelime}")
