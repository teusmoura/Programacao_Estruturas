from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT id_categoria, nome, id_categoria_pai FROM categorias")
registros = cursor.fetchall()
filhos = {}
for id_categoria, nome, pai in registros:
    filhos.setdefault(pai, []).append((id_categoria, nome))
for raiz in filhos.get(None, []):
    print("Raiz:", raiz)

cursor.close()
conexao.close()
