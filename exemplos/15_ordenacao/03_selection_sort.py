valores = [5, 2, 4, 1, 3]
for i in range(len(valores) - 1):
    menor = i
    for j in range(i + 1, len(valores)):
        if valores[j] < valores[menor]:
            menor = j
    valores[i], valores[menor] = valores[menor], valores[i]
print(valores)
