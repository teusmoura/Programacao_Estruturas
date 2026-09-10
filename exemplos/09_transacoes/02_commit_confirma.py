from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cursor.execute("SELECT ativo FROM clientes WHERE id_cliente = 10")
original = cursor.fetchone()[0]

cursor.execute("UPDATE clientes SET ativo = %s WHERE id_cliente = 10", (not bool(original),))
conexao.commit()
cursor.execute("SELECT ativo FROM clientes WHERE id_cliente = 10")
print("Após commit:", cursor.fetchone()[0])

cursor.execute("UPDATE clientes SET ativo = %s WHERE id_cliente = 10", (original,))
conexao.commit()
cursor.close()
conexao.close()
