from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""SELECT p.sku,p.nome,p.preco,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE e.id_unidade=1""")
produtos=cursor.fetchall()
print(sorted(produtos,key=lambda p:(p[3],float(p[2])))[:5])
cursor.close(); conexao.close()
