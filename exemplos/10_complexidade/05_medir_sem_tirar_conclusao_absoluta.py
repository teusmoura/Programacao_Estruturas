from timeit import timeit

lista = list(range(10_000))
conjunto = set(lista)
print("in em lista:", timeit(lambda: 9999 in lista, number=1000))
print("in em set:", timeit(lambda: 9999 in conjunto, number=1000))
