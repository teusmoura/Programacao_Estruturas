def busca_binaria(valores, alvo):
    inicio = 0
    fim = len(valores) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valores[meio] == alvo:
            return meio
        if valores[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

print(busca_binaria([10, 20, 30, 40, 50], 40))
