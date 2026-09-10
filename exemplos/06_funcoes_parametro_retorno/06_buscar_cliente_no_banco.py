from database import criar_conexao


def buscar_cliente(id_cliente):
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
    conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
    cursor = conexao.cursor()
    cursor.execute("SELECT id_cliente, nome, cidade, uf FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conexao.close()
    return cliente

print(buscar_cliente(3))
print(buscar_cliente(999))
