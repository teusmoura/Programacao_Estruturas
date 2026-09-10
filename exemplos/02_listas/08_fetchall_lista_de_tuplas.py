from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("""
    SELECT id_produto, sku, nome, preco
    FROM produtos
    ORDER BY id_produto
    LIMIT 5
""")
produtos = cursor.fetchall()
print(type(produtos))
print(type(produtos[0]))
for produto in produtos:
    print(produto)

cursor.close()
conexao.close()
