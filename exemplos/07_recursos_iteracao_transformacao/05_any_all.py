estoques = [7, 5, 0, 13]
print("Existe zerado?", any(qtd == 0 for qtd in estoques))
print("Todos positivos?", all(qtd > 0 for qtd in estoques))
