from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
cursor.execute("SELECT nome FROM clientes WHERE id_cliente = 1")
nome_original = cursor.fetchone()[0]

cursor.execute("UPDATE clientes SET nome = %s WHERE id_cliente = %s", ("Ana Teste", 1))
print("Linhas afetadas:", cursor.rowcount)
conexao.commit()

cursor.execute("SELECT nome FROM clientes WHERE id_cliente = 1")
print("Persistido:", cursor.fetchone()[0])

cursor.execute("UPDATE clientes SET nome = %s WHERE id_cliente = %s", (nome_original, 1))
conexao.commit()
cursor.close()
conexao.close()
