from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

id_cliente = 3
cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = %s", (id_cliente,))
print(cursor.fetchone())

cursor.close()
conexao.close()
