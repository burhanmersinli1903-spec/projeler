# while gorevler: ifadesi liste boşaldığında otomatik durur; pop() ise elemanı hem alır hem siler.

gorevler=["kod", "test", "deploy"]
while gorevler:
    print(gorevler.pop())