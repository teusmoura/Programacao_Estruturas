precos = [39.90, 79.90, 249.90, 899.90]
com_desconto = [round(preco * 0.9, 2) for preco in precos]
baratos = [preco for preco in precos if preco < 100]
print(com_desconto)
print(baratos)
