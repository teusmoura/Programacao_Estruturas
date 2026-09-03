class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor; self.esquerda = esquerda; self.direita = direita

def em_ordem(no):
    if no is None: return
    em_ordem(no.esquerda)
    print(no.valor)
    em_ordem(no.direita)

raiz = No(50, No(30, No(20), No(40)), No(80, No(70), No(90)))
em_ordem(raiz)
