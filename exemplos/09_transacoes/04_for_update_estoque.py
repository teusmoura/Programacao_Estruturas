from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
try:
    cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=%s AND id_produto=%s FOR UPDATE",(1,4))
    print("Estoque bloqueado para decisão:",cursor.fetchone()[0])
    conexao.rollback()
finally:
    cursor.close(); conexao.close()
