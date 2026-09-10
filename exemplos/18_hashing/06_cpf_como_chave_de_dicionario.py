from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT cpf_cnpj, id_cliente, nome FROM clientes")
por_cpf = {cpf: (id_cliente, nome) for cpf, id_cliente, nome in cursor.fetchall()}
print(por_cpf["333.333.333-03"])

cursor.close()
conexao.close()
