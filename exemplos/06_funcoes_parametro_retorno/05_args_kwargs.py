def totalizar(*valores):
    return sum(valores)

def exibir_campos(**dados):
    for chave, valor in dados.items():
        print(chave, valor)

print(totalizar(39.90, 79.90, 24.90))
exibir_campos(nome="Shampoo Nutritivo 350 ml", sku="CAB-SHA-001", estoque=45)
