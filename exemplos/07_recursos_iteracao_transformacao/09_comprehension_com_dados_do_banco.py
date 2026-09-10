from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
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
