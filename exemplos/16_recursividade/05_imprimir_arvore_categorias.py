from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()
cursor.execute("SELECT id_categoria, nome, id_categoria_pai FROM categorias")
registros = cursor.fetchall()
cursor.close(); conexao.close()

filhos = {}
for id_categoria, nome, pai in registros:
    filhos.setdefault(pai, []).append((id_categoria, nome))

def imprimir(pai, nivel=0):
    for id_categoria, nome in filhos.get(pai, []):
        print("  " * nivel + nome)
        imprimir(id_categoria, nivel + 1)

imprimir(None)
