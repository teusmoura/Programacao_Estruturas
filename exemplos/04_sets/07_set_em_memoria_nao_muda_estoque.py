from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
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
