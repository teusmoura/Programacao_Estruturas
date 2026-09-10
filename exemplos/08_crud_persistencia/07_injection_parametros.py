# Compare: parâmetros mantêm dado e comando separados.
from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
nome = "Ana Martins"
cursor.execute("SELECT id_cliente, nome FROM clientes WHERE nome = %s", (nome,))
print(cursor.fetchone())
cursor.close()
conexao.close()
