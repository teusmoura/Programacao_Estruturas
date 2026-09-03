produtos = ["Shampoo", "Condicionador"]
try:
    print(produtos[5])
except IndexError:
    print("A posição solicitada não existe.")
