try:
    valor = int(input("Digite um inteiro: "))
    print(100 / valor)
except ValueError:
    print("Era esperado um inteiro.")
except ZeroDivisionError:
    print("O inteiro não pode ser zero.")
except Exception as erro:
    print("Erro inesperado:", erro)
