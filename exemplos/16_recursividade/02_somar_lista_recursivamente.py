def somar(valores):
    if not valores:
        return 0
    return valores[0] + somar(valores[1:])

print(somar([10, 20, 30]))
