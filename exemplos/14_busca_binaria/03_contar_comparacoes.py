def busca_binaria(valores, alvo):
    inicio, fim = 0, len(valores) - 1
    comparacoes = 0
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if valores[meio] == alvo:
            return meio, comparacoes
        if valores[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None, comparacoes

print(busca_binaria(list(range(1, 101)), 97))
