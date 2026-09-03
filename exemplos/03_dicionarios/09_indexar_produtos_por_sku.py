from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome, preco FROM produtos")
registros = cursor.fetchall()
por_sku = {}
for sku, nome, preco in registros:
    por_sku[sku] = {"nome": nome, "preco": preco}
print(por_sku["PERF-FEM-001"])

cursor.close()
conexao.close()
