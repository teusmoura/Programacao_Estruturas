from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
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
