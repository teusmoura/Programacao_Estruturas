from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""
 SELECT u.nome,p.sku,p.nome,e.quantidade,e.estoque_minimo
 FROM estoques e JOIN unidades u ON u.id_unidade=e.id_unidade JOIN produtos p ON p.id_produto=e.id_produto
 WHERE u.tipo='LOJA'
""")
por_unidade={}
for unidade,sku,nome,qtd,minimo in cursor.fetchall():
    if qtd<minimo: por_unidade.setdefault(unidade,[]).append((sku,nome,qtd,minimo))
for unidade,itens in por_unidade.items(): print(unidade,itens)
cursor.close(); conexao.close()
