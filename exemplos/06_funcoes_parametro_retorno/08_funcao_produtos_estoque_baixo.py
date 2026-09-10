from database import criar_conexao

def produtos_estoque_baixo(id_unidade):
    # criar_conexao() abre a ligação entre o programa e o banco MySQL.
    conexao=criar_conexao()
    # O cursor envia comandos SQL e recebe os resultados do banco.
    cursor=conexao.cursor()
    cursor.execute("""
        SELECT p.sku,p.nome,e.quantidade,e.estoque_minimo
        FROM estoques e JOIN produtos p ON p.id_produto=e.id_produto
        WHERE e.id_unidade=%s AND e.quantidade < e.estoque_minimo
        ORDER BY e.quantidade
    """,(id_unidade,))
    r=cursor.fetchall(); cursor.close(); conexao.close(); return r

print(produtos_estoque_baixo(1))
