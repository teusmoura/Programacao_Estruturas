class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(no, valor):
    if no is None:
        return No(valor)
    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = inserir(no.direita, valor)
    return no

raiz = None
for valor in [50, 30, 80, 20, 40, 70, 90]:
    raiz = inserir(raiz, valor)
print(raiz.esquerda.direita.valor)
