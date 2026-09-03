produtos = [("CAB-SHA-001", "Shampoo Nutritivo 350 ml"), ("PERF-FEM-001", "Perfume Floral 100 ml")]
procurado = "PERF-FEM-001"
encontrado = None
for produto in produtos:
    if produto[0] == procurado:
        encontrado = produto
        break
print(encontrado)
