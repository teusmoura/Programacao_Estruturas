texto = "25"
try:
    numero = int(texto)
except ValueError:
    print("Conversão falhou.")
else:
    print("Conversão concluída:", numero)
finally:
    print("Este bloco sempre é executado.")
