from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

id_cliente = 3
cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = %s", (id_cliente,))
print(cursor.fetchone())

cursor.close()
conexao.close()
