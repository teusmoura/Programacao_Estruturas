cliente = {"id": 1, "nome": "Ana Martins", "cidade": "Sete Lagoas"}
print(cliente.get("cidade"))
print(cliente.get("telefone"))
print(cliente.get("telefone", "não informado"))
