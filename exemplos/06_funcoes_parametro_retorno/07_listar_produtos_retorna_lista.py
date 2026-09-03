from database import criar_conexao

def listar_produtos():
    conexao=criar_conexao(); cursor=conexao.cursor()
    cursor.execute("SELECT id_produto, sku, nome, preco FROM produtos ORDER BY id_produto")
    resultado=cursor.fetchall()
    cursor.close(); conexao.close()
    return resultado

print(listar_produtos()[:5])
