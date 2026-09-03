produtos = ["Shampoo", "Condicionador", "Perfume", "Protetor Solar", "Base Liquida"]
procurado = "Base Liquida"
comparacoes = 0
for produto in produtos:
    comparacoes += 1
    if produto == procurado:
        break
print("Comparações:", comparacoes)
