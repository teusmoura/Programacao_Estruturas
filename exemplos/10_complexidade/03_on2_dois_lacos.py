nomes = ["Ana", "Bruno", "Carla", "Ana"]
pares_iguais = []
for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        if nomes[i] == nomes[j]:
            pares_iguais.append((i, j))
print(pares_iguais)
