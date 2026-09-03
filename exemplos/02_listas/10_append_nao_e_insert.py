from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT id_cliente, nome FROM clientes ORDER BY id_cliente")
clientes = cursor.fetchall()
clientes.append((999, "Cliente apenas na memória"))
print("Último item da lista:", clientes[-1])

cursor.execute("SELECT id_cliente, nome FROM clientes WHERE id_cliente = 999")
print("No banco:", cursor.fetchone())

cursor.close()
conexao.close()
