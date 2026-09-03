# Compare: parâmetros mantêm dado e comando separados.
from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
nome = "Ana Martins"
cursor.execute("SELECT id_cliente, nome FROM clientes WHERE nome = %s", (nome,))
print(cursor.fetchone())
cursor.close()
conexao.close()
