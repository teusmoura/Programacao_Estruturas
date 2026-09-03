from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
try:
    cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=%s AND id_produto=%s FOR UPDATE",(1,4))
    print("Estoque bloqueado para decisão:",cursor.fetchone()[0])
    conexao.rollback()
finally:
    cursor.close(); conexao.close()
