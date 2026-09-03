from database import criar_conexao

conexao = criar_conexao(); cursor = conexao.cursor()
cursor.execute("""
    SELECT p.sku
    FROM estoques e JOIN produtos p ON p.id_produto=e.id_produto
    WHERE e.id_unidade=%s AND e.quantidade > 0
""", (1,))
skus = {linha[0] for linha in cursor.fetchall()}
print("Produtos disponíveis em Sete Lagoas:", skus)
cursor.close(); conexao.close()
