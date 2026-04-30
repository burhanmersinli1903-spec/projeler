umin=int(input("Başlangıcı yazınız."))
umax=int(input("Sonunu yazınız."))
count=int(input("Artma veya azalma miktarını yazınız."))
for i in range(umin, umax+1, count):
    print(i)