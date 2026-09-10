from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
try:
    cursor.execute("UPDATE estoques SET quantidade=quantidade-1 WHERE id_unidade=1 AND id_produto=4")
    # FK inválida força falha para demonstrar rollback.
    cursor.execute("INSERT INTO itens_pedido (id_pedido,id_produto,quantidade,preco_unitario) VALUES (%s,%s,%s,%s)",(99999,4,1,129.90))
    conexao.commit()
except Exception as erro:
    conexao.rollback()
    print(type(erro).__name__, "-> rollback executado")
finally:
    cursor.close(); conexao.close()
