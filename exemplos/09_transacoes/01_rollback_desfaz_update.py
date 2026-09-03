from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=1 AND id_produto=1")
antes=cursor.fetchone()[0]
cursor.execute("UPDATE estoques SET quantidade=quantidade-1 WHERE id_unidade=1 AND id_produto=1")
cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=1 AND id_produto=1")
print("Durante a transação:", cursor.fetchone()[0])
conexao.rollback()
cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=1 AND id_produto=1")
print("Depois do rollback:", cursor.fetchone()[0], "(antes:", antes, ")")
cursor.close(); conexao.close()
