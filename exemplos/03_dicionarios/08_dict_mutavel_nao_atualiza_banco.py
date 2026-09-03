from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

colunas = ("id_cliente", "nome", "cidade")
cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = 1")
cliente = dict(zip(colunas, cursor.fetchone()))
cliente["nome"] = "Nome alterado só no dicionário"
print("Dicionário:", cliente)

cursor.execute("SELECT id_cliente, nome, cidade FROM clientes WHERE id_cliente = 1")
print("Banco:", cursor.fetchone())

cursor.close()
conexao.close()
