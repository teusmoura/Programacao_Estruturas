valores = [5, 2, 4, 1, 3]
for fim in range(len(valores) - 1, 0, -1):
    for i in range(fim):
        if valores[i] > valores[i + 1]:
            valores[i], valores[i + 1] = valores[i + 1], valores[i]
print(valores)
