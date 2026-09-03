produto = {"nome": "Perfume Floral 100 ml", "preco": 249.90}
try:
    print(produto["estoque"])
except KeyError:
    print("Chave estoque ausente.")
print("Com get:", produto.get("estoque", 0))
