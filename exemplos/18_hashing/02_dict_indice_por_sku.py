produtos = [("CAB-SHA-001", "Shampoo Nutritivo 350 ml"), ("PERF-FEM-001", "Perfume Floral 100 ml")]
indice = {sku: nome for sku, nome in produtos}
print(indice["PERF-FEM-001"])
