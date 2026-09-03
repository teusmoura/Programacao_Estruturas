class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor; self.esquerda = esquerda; self.direita = direita

def pre(no):
    if no:
        print(no.valor, end=" "); pre(no.esquerda); pre(no.direita)

def pos(no):
    if no:
        pos(no.esquerda); pos(no.direita); print(no.valor, end=" ")

raiz = No(2, No(1), No(3))
pre(raiz); print(); pos(raiz)
