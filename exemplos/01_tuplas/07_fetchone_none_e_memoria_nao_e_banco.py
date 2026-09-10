from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT id_cliente, nome FROM clientes WHERE id_cliente = %s", (999,))
print("Cliente 999:", cursor.fetchone())

cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = %s", (1,))
original = cursor.fetchone()
alterada = (original[0], "Nome somente na memória", original[2])
print("Tupla original:", original)
print("Nova tupla em memória:", alterada)

cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = %s", (1,))
print("Banco consultado novamente:", cursor.fetchone())

cursor.close()
conexao.close()
