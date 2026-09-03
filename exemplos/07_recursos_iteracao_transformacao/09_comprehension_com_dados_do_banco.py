from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""
    SELECT p.sku,p.nome,p.preco,e.quantidade
    FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto
    WHERE e.id_unidade=1
""")
produtos=cursor.fetchall()
estoques={sku:qtd for sku,_,_,qtd in produtos}
caros=[(sku,nome,preco) for sku,nome,preco,_ in produtos if float(preco)>=50]
print(estoques["PERF-FEM-001"])
print(caros)
cursor.close(); conexao.close()
