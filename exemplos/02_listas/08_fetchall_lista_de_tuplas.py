from database import criar_conexao

conexao = criar_conexao()
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
