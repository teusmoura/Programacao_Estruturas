produto = {"sku": "PEL-COR-001", "nome": "Hidratante Corporal 400 ml", "preco": 189.90}
print(list(produto.keys()))
print(list(produto.values()))
for chave, valor in produto.items():
    print(chave, "->", valor)
