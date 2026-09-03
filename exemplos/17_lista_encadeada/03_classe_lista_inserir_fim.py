class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            return
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

lista = ListaEncadeada()
for valor in ["Receber", "Validar", "Separar"]:
    lista.inserir_fim(valor)
print(lista.inicio.proximo.valor)
