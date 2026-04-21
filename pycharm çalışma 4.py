# Eğer döngü break ile kesilmeden sonuna kadar çalışırsa else bloğu tetiklenir.

for i in range(2,10):
    if 10 % i == 0:
        break
else:
    print("Döngü hiç break görmedi")

