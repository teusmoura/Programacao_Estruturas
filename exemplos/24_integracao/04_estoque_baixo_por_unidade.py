from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
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
