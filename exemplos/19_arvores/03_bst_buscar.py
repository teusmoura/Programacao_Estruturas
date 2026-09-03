def buscar(no, alvo):
    if no is None or no.valor == alvo:
        return no
    if alvo < no.valor:
        return buscar(no.esquerda, alvo)
    return buscar(no.direita, alvo)
