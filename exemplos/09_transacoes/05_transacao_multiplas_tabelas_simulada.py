from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
try:
    cursor.execute("SELECT quantidade FROM estoques WHERE id_unidade=1 AND id_produto=1 FOR UPDATE")
    estoque=cursor.fetchone()[0]
    if estoque < 1: raise ValueError("Estoque insuficiente")
    cursor.execute("INSERT INTO pedidos (id_cliente,id_unidade,id_canal,status) VALUES (1,1,1,'PENDENTE')")
    id_pedido=cursor.lastrowid
    cursor.execute("INSERT INTO itens_pedido (id_pedido,id_produto,quantidade,preco_unitario) VALUES (%s,1,1,24.90)",(id_pedido,))
    cursor.execute("UPDATE estoques SET quantidade=quantidade-1 WHERE id_unidade=1 AND id_produto=1")
    print("Pedido, item e estoque alterados dentro da mesma transação; exemplo fará rollback.")
    conexao.rollback()
except Exception:
    conexao.rollback(); raise
finally:
    cursor.close(); conexao.close()
