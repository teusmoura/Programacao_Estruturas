from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome FROM produtos")
produtos = cursor.fetchall()
procurado = "PERF-INF-001"
for posicao, produto in enumerate(produtos, start=1):
    if produto[0] == procurado:
        print("Encontrado após", posicao, "comparações:", produto)
        break

cursor.close()
conexao.close()
