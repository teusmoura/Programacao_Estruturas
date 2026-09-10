from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
colunas = ("id_produto", "sku", "nome", "preco", "estoque_sete_lagoas")
cursor.execute("""
    SELECT p.id_produto, p.sku, p.nome, p.preco, e.quantidade
    FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto
    WHERE p.id_produto=%s AND e.id_unidade=1
""", (4,))
registro = cursor.fetchone()
produto = dict(zip(colunas, registro))
print(produto)
cursor.close(); conexao.close()
