from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT cpf_cnpj, id_cliente, nome FROM clientes")
por_cpf = {cpf: (id_cliente, nome) for cpf, id_cliente, nome in cursor.fetchall()}
print(por_cpf["333.333.333-03"])

cursor.close()
conexao.close()
