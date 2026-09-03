from database import criar_conexao

conexao = criar_conexao()
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
