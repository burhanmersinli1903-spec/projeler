# Dış döndü satırları, iç döngü ise o satıra kaç tane ve hangi sayıların yazılacağını kontrol eder.

kat_sayisi = 5
for i in range(1, kat_sayisi + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()