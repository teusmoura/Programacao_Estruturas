from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
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
