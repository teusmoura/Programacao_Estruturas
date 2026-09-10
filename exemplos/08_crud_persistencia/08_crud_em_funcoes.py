from database import criar_conexao

def buscar_produto(sku):
    # criar_conexao() abre a ligação entre o programa e o banco MySQL.
    conexao=criar_conexao()
    # O cursor envia comandos SQL e recebe os resultados do banco.
    cursor=conexao.cursor()
    cursor.execute("SELECT id_produto,sku,nome,preco FROM produtos WHERE sku=%s",(sku,))
    r=cursor.fetchone(); cursor.close(); conexao.close(); return r

print(buscar_produto("PERF-FEM-001"))
