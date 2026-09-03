import heapq
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT prioridade,prazo,id_solicitacao FROM solicitacoes_reposicao WHERE status='PENDENTE'")
heap=cursor.fetchall(); heapq.heapify(heap); proxima=heapq.heappop(heap)
print("Retirada do heap em memória:",proxima)
cursor.execute("SELECT status FROM solicitacoes_reposicao WHERE id_solicitacao=%s",(proxima[2],))
print("Status no banco:",cursor.fetchone()[0])
cursor.close(); conexao.close()
