from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT sku, id_produto, nome, preco FROM produtos")
por_sku = {sku: (id_produto, nome, preco) for sku, id_produto, nome, preco in cursor.fetchall()}
print(por_sku["PEL-COR-001"])

cursor.close()
conexao.close()
