from database import criar_conexao

conexao = criar_conexao()
cursor = conexao.cursor()

from bisect import bisect_left

cursor.execute("SELECT sku, nome FROM produtos ORDER BY sku")
produtos = cursor.fetchall()
skus = [p[0] for p in produtos]
alvo = "PEL-FAC-001"
pos = bisect_left(skus, alvo)
if pos < len(skus) and skus[pos] == alvo:
    print(produtos[pos])
else:
    print("Não encontrado")

cursor.close()
conexao.close()
