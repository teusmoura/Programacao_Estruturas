from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cpf = "900.000.000-02"
cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf,))
cursor.execute("INSERT INTO clientes (nome, cpf_cnpj) VALUES (%s, %s)", ("Excluir Teste", cpf))
conexao.commit()

cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf,))
print("Excluídos:", cursor.rowcount)
conexao.commit()
cursor.close()
conexao.close()
