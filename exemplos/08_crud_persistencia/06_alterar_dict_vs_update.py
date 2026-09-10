from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
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
