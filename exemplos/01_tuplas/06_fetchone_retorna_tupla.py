from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("""
    SELECT id_cliente, nome, email, cidade, uf
    FROM clientes
    WHERE id_cliente = %s
""", (1,))
cliente = cursor.fetchone()
print(cliente)
print(type(cliente))

cursor.close()
conexao.close()
