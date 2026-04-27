fakt=1
sayi=int(input("Faktöriyelini bulmak istediğiniz sayıyı giriniz:"))
for sayi in range(1,sayi+1):
    fakt=fakt*sayi
print("Faktoriyel=",fakt)