valores = [5, 2, 4, 1, 3]
for i in range(1, len(valores)):
    atual = valores[i]
    j = i - 1
    while j >= 0 and valores[j] > atual:
        valores[j + 1] = valores[j]
        j -= 1
    valores[j + 1] = atual
print(valores)
