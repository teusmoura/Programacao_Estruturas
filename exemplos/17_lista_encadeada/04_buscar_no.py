class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

inicio = No("Receber", No("Validar", No("Separar")))
procurado = "Separar"
atual = inicio
while atual is not None and atual.valor != procurado:
    atual = atual.proximo
print(None if atual is None else atual.valor)
