# Sölüktekiher bir "anahtar" ile "değerin" yerini tek satırda takas eder.

eski={"a": 1, "b": 2}
yeni={v: k for k, v in eski.items()}
print(yeni)


