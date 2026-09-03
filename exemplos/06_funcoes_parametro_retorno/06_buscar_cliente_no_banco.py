from database import criar_conexao


def buscar_cliente(id_cliente):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_cliente, nome, cidade, uf FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conexao.close()
    return cliente

print(buscar_cliente(3))
print(buscar_cliente(999))
