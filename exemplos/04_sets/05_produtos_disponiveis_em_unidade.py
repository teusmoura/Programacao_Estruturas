from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cursor.execute("""
    SELECT p.sku
    FROM estoques e JOIN produtos p ON p.id_produto=e.id_produto
    WHERE e.id_unidade=%s AND e.quantidade > 0
""", (1,))
skus = {linha[0] for linha in cursor.fetchall()}
print("Produtos disponíveis em Sete Lagoas:", skus)
cursor.close(); conexao.close()
