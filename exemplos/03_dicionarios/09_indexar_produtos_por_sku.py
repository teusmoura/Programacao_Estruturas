from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT sku, nome, preco FROM produtos")
registros = cursor.fetchall()
por_sku = {}
for sku, nome, preco in registros:
    por_sku[sku] = {"nome": nome, "preco": preco}
print(por_sku["PERF-FEM-001"])

cursor.close()
conexao.close()
