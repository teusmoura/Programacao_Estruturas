from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cpf_teste = "900.000.000-01"
cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf_teste,))
conexao.commit()

cursor.execute("""
    INSERT INTO clientes (nome, cpf_cnpj, email, origem, cidade, uf)
    VALUES (%s, %s, %s, %s, %s, %s)
""", ("Cliente Teste", cpf_teste, "teste@email.com", "AULA", "Sete Lagoas", "MG"))
conexao.commit()
print("ID gerado:", cursor.lastrowid)

cursor.execute("SELECT id_cliente, nome FROM clientes WHERE cpf_cnpj = %s", (cpf_teste,))
print(cursor.fetchone())

cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf_teste,))
conexao.commit()
cursor.close()
conexao.close()
