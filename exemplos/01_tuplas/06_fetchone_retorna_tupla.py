
from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("""
    SELECT id_cliente, nome, email, cidade, uf
    FROM clientes
    WHERE id_cliente = %s
""", (1,))
cliente = cursor.fetchone()
print(cliente)
print(type(cliente))

cursor.close()
conexao.close()
