from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

colunas = ("id_cliente", "nome", "cidade")
cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = 2")
cliente = dict(zip(colunas, cursor.fetchone()))
cliente["cidade"] = "Cidade apenas na memória"
print("Dicionário:", cliente)
cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = 2")
print("Banco:", cursor.fetchone())

cursor.close()
conexao.close()
