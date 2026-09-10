from database import criar_conexao

def listar_produtos():
    # criar_conexao() abre a ligação entre o programa e o banco MySQL.
    conexao=criar_conexao()
    # O cursor envia comandos SQL e recebe os resultados do banco.
    cursor=conexao.cursor()
    cursor.execute("SELECT id_produto, sku, nome, preco FROM produtos ORDER BY id_produto")
    resultado=cursor.fetchall()
    cursor.close(); conexao.close()
    return resultado

print(listar_produtos()[:5])
