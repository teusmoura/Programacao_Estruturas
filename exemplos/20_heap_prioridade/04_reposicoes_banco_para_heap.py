import heapq
from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT prioridade,prazo,id_solicitacao,id_unidade,id_produto FROM solicitacoes_reposicao WHERE status='PENDENTE'")
heap=cursor.fetchall(); heapq.heapify(heap)
for _ in range(min(3,len(heap))): print(heapq.heappop(heap))
cursor.close(); conexao.close()
