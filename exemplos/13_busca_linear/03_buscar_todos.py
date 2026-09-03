produtos = [("Shampoo", 39.90), ("Condicionador", 79.90), ("Creme Dental", 24.90)]
baratos = []
for produto in produtos:
    if produto[1] < 50:
        baratos.append(produto)
print(baratos)
