from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
cursor.execute("SELECT COUNT(*) FROM produtos")
produtos = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM unidades")
unidades = cursor.fetchone()[0]
print(f"Conexão OK. Produtos: {produtos}. Unidades (lojas/CDs): {unidades}.")
cursor.close()
conexao.close()
