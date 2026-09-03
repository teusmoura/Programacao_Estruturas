class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

primeiro = No("Receber pedido")
segundo = No("Validar pagamento")
primeiro.proximo = segundo
print(primeiro.valor)
print(primeiro.proximo.valor)
