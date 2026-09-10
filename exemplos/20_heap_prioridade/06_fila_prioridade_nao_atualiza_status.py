import heapq
from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT prioridade,prazo,id_solicitacao FROM solicitacoes_reposicao WHERE status='PENDENTE'")
heap=cursor.fetchall(); heapq.heapify(heap); proxima=heapq.heappop(heap)
print("Retirada do heap em memória:",proxima)
cursor.execute("SELECT status FROM solicitacoes_reposicao WHERE id_solicitacao=%s",(proxima[2],))
print("Status no banco:",cursor.fetchone()[0])
cursor.close(); conexao.close()
