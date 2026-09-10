from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor = conexao.cursor()

cursor.execute("SELECT sku, id_produto, nome, preco FROM produtos")
por_sku = {sku: (id_produto, nome, preco) for sku, id_produto, nome, preco in cursor.fetchall()}
print(por_sku["PEL-COR-001"])

cursor.close()
conexao.close()
