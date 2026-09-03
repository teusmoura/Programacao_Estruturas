class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

inicio = No("A", No("B", No("C")))
atual = inicio
while atual is not None:
    print(atual.valor)
    atual = atual.proximo
