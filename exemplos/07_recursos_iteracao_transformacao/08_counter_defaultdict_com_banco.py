from collections import Counter, defaultdict
from database import criar_conexao

# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("""SELECT c.nome FROM pedidos p JOIN canais_venda c ON c.id_canal=p.id_canal""")
print("Pedidos por canal:", Counter(linha[0] for linha in cursor.fetchall()))

cursor.execute("SELECT id_fornecedor,nome FROM produtos ORDER BY id_fornecedor,nome")
por_fornecedor=defaultdict(list)
for id_fornecedor,nome in cursor.fetchall():
    por_fornecedor[id_fornecedor].append(nome)
print(dict(por_fornecedor))
cursor.close(); conexao.close()
