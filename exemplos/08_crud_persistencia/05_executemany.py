from database import criar_conexao

conexao = criar_conexao()
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
