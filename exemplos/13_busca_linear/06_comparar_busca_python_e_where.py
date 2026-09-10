from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome FROM produtos")
produtos = cursor.fetchall()
resultado_python = next((p for p in produtos if p[0] == "PEL-FAC-001"), None)
cursor.execute("SELECT sku, nome FROM produtos WHERE sku=%s", ("PEL-FAC-001",))
resultado_sql = cursor.fetchone()
print("Python:", resultado_python)
print("SQL:", resultado_sql)

cursor.close()
conexao.close()
