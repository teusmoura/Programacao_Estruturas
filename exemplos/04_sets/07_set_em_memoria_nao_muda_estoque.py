from database import criar_conexao

conexao = criar_conexao(); cursor = conexao.cursor()
cursor.execute("""
    SELECT p.sku FROM estoques e JOIN produtos p ON p.id_produto=e.id_produto
    WHERE e.id_unidade=1 AND e.quantidade > 0
""")
skus = {linha[0] for linha in cursor.fetchall()}
skus.add("SKU-TEMPORARIO")
print("Set em memória:", "SKU-TEMPORARIO" in skus)
cursor.execute("SELECT COUNT(*) FROM produtos WHERE sku='SKU-TEMPORARIO'")
print("Existe no banco:", cursor.fetchone()[0] > 0)
cursor.close(); conexao.close()
