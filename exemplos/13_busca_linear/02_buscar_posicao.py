nomes = ["Shampoo", "Condicionador", "Perfume", "Protetor Solar"]
procurado = "Perfume"
posicao = None
for i, nome in enumerate(nomes):
    if nome == procurado:
        posicao = i
        break
print(posicao)
