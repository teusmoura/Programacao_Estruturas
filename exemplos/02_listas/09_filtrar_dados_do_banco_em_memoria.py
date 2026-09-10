from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cursor.execute("""
    SELECT p.id_produto, p.nome, p.preco, e.quantidade
    FROM produtos p
    JOIN estoques e ON e.id_produto = p.id_produto
    WHERE e.id_unidade = 1
    ORDER BY p.id_produto
""")
produtos = cursor.fetchall()
baixo_estoque = [p for p in produtos if p[3] < 5]
print(baixo_estoque)
cursor.close(); conexao.close()
