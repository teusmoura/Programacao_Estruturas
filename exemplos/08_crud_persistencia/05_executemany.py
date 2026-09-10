from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()
cpfs = ["900.000.000-03", "900.000.000-04", "900.000.000-05"]
for cpf in cpfs:
    cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf,))
conexao.commit()

dados = [
    ("Teste A", cpfs[0]),
    ("Teste B", cpfs[1]),
    ("Teste C", cpfs[2]),
]
cursor.executemany("INSERT INTO clientes (nome, cpf_cnpj) VALUES (%s, %s)", dados)
conexao.commit()
print("Inseridos:", cursor.rowcount)

for cpf in cpfs:
    cursor.execute("DELETE FROM clientes WHERE cpf_cnpj = %s", (cpf,))
conexao.commit()
cursor.close()
conexao.close()
