from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""SELECT p.id_produto,p.nome,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE p.id_produto=1 AND e.id_unidade=1""")
registro=cursor.fetchone(); memoria=list(registro)
memoria[2]-=5
cursor.execute("UPDATE estoques SET quantidade=quantidade-5 WHERE id_unidade=1 AND id_produto=1")
conexao.rollback()
print("Objeto em memória:",memoria)
cursor.execute("""SELECT p.id_produto,p.nome,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE p.id_produto=1 AND e.id_unidade=1""")
print("Banco após rollback:",cursor.fetchone())
cursor.close(); conexao.close()
