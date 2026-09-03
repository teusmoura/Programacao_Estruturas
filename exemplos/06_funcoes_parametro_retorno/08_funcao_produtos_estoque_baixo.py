from database import criar_conexao

def produtos_estoque_baixo(id_unidade):
    conexao=criar_conexao(); cursor=conexao.cursor()
    cursor.execute("""
        SELECT p.sku,p.nome,e.quantidade,e.estoque_minimo
        FROM estoques e JOIN produtos p ON p.id_produto=e.id_produto
        WHERE e.id_unidade=%s AND e.quantidade < e.estoque_minimo
        ORDER BY e.quantidade
    """,(id_unidade,))
    r=cursor.fetchall(); cursor.close(); conexao.close(); return r

print(produtos_estoque_baixo(1))
