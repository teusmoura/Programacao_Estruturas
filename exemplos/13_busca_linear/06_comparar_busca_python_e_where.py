from database import criar_conexao

conexao = criar_conexao()
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
