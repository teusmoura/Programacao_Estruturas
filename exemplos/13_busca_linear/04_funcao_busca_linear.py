def buscar_por_sku(produtos, sku):
    for produto in produtos:
        if produto[0] == sku:
            return produto
    return None

print(buscar_por_sku([("CAB-SHA-001", "Shampoo"), ("PERF-FEM-001", "Perfume")], "PERF-FEM-001"))
