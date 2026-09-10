from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("""SELECT p.sku,p.nome,p.preco,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE e.id_unidade=1""")
registros=cursor.fetchall()
indice={sku:{"nome":nome,"preco":float(preco),"estoque":qtd} for sku,nome,preco,qtd in registros}
criticos=[(sku,d["nome"],d["estoque"]) for sku,d in indice.items() if d["estoque"]<5]
print(sorted(criticos,key=lambda x:x[2]))
cursor.close(); conexao.close()
