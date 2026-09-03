valores = [1, 2, 3, 5, 4]
for fim in range(len(valores) - 1, 0, -1):
    trocou = False
    for i in range(fim):
        if valores[i] > valores[i + 1]:
            valores[i], valores[i + 1] = valores[i + 1], valores[i]
            trocou = True
    if not trocou:
        break
print(valores)
