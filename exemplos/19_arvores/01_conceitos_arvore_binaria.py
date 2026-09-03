class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

raiz = No(50, No(30), No(80))
print("Raiz:", raiz.valor)
print("Filho esquerdo:", raiz.esquerda.valor)
print("Filho direito:", raiz.direita.valor)
