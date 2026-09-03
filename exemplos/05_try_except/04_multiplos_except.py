valor = "10"
divisor = 0
try:
    numero = int(valor)
    print(numero / divisor)
except ValueError:
    print("Valor inválido.")
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
