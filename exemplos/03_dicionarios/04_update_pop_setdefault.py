cliente = {"nome": "Bruno Alves", "origem": "LOJA"}
cliente.setdefault("ativo", True)
cliente.update({"cidade": "Sete Lagoas", "uf": "MG"})
origem = cliente.pop("origem")
print("Origem removida:", origem)
print(cliente)
