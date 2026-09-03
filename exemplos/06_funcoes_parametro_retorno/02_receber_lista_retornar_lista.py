def filtrar_precos(precos, limite):
    resultado = []
    for preco in precos:
        if preco <= limite:
            resultado.append(preco)
    return resultado

print(filtrar_precos([39.90, 249.90, 79.90, 899.90], 100))
