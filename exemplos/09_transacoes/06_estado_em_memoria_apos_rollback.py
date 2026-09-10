from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("""SELECT p.id_produto,p.nome,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE p.id_produto=1 AND e.id_unidade=1""")
registro=cursor.fetchone(); memoria=list(registro)
memoria[2]-=5
cursor.execute("UPDATE estoques SET quantidade=quantidade-5 WHERE id_unidade=1 AND id_produto=1")
conexao.rollback()
print("Objeto em memória:",memoria)
cursor.execute("""SELECT p.id_produto,p.nome,e.quantidade FROM produtos p JOIN estoques e ON e.id_produto=p.id_produto WHERE p.id_produto=1 AND e.id_unidade=1""")
print("Banco após rollback:",cursor.fetchone())
cursor.close(); conexao.close()
