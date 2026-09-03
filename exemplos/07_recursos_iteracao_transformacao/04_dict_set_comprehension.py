produtos = [("CAB-SHA-001", "Shampoo Nutritivo 350 ml"), ("PERF-FEM-001", "Perfume Floral 100 ml")]
por_sku = {sku: nome for sku, nome in produtos}
iniciais = {nome[0] for _, nome in produtos}
print(por_sku)
print(iniciais)
