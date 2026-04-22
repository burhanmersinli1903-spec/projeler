#   Dıştaki döngü her değiştiğnde içteki döngü baştan sona çalışır. End="\t" komutu, sonuçların yan yana
# düzenli durmasını sağlar.

for i in range(1,6):
    for j in range(1,6):
        print(f"{i} * {j} = {i * j}")
    print()