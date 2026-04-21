# Hem iki listeyi eşleştirir(zip) hem de her eşleşmeye bir indeks numarası (enumerate) atar.

for i, (a, b) in enumerate(zip(["x"])):
    print(i, a, b)