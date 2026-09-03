from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome, preco FROM produtos")
memoria = sorted(cursor.fetchall(), key=lambda p: p[2], reverse=True)
cursor.execute("SELECT sku, nome, preco FROM produtos ORDER BY preco DESC")
banco = cursor.fetchall()
print("Mesmo primeiro item?", memoria[0] == banco[0])
print(memoria[0])

cursor.close()
conexao.close()
