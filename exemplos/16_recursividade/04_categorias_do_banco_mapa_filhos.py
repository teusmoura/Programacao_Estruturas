from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

cursor.execute("SELECT id_categoria, nome, id_categoria_pai FROM categorias")
categorias = cursor.fetchall()
filhos = {}
for id_categoria, nome, pai in categorias:
    filhos.setdefault(pai, []).append((id_categoria, nome))
print(filhos[None])
print(filhos[1])

cursor.close()
conexao.close()
