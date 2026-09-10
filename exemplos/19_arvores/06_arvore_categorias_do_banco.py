from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao = criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
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
