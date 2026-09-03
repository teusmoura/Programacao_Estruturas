from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""SELECT p.sku,p.nome,p.preco,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE e.id_unidade=1""")
produtos=cursor.fetchall(); por_sku={p[0]:p for p in produtos}
print("Busca média O(1) por chave:",por_sku["PEL-COR-001"])
print("Menores estoques:",sorted(produtos,key=lambda p:p[3])[:3])
cursor.close(); conexao.close()
