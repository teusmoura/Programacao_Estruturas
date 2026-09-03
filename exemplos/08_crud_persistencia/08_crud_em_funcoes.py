from database import criar_conexao

def buscar_produto(sku):
    conexao=criar_conexao(); cursor=conexao.cursor()
    cursor.execute("SELECT id_produto,sku,nome,preco FROM produtos WHERE sku=%s",(sku,))
    r=cursor.fetchone(); cursor.close(); conexao.close(); return r

print(buscar_produto("PERF-FEM-001"))
