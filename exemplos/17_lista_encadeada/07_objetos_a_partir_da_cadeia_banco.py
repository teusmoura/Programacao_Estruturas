class No:
    def __init__(self, id_etapa, nome):
        self.id_etapa = id_etapa
        self.nome = nome
        self.proximo = None

registros = [(1, "Receber"), (2, "Validar"), (3, "Separar")]
nos = [No(id_etapa, nome) for id_etapa, nome in registros]
for i in range(len(nos) - 1):
    nos[i].proximo = nos[i + 1]
print(nos[0].proximo.nome)
