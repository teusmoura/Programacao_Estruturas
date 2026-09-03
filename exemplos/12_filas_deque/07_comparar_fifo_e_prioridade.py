from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_solicitacao,prioridade,data_solicitacao,prazo FROM solicitacoes_reposicao WHERE status='PENDENTE'")
registros=cursor.fetchall()
fifo=deque(sorted(registros,key=lambda r:r[2]))
por_prioridade=sorted(registros,key=lambda r:(r[1],r[3],r[2]))
print("FIFO:",fifo[0])
print("Prioridade:",por_prioridade[0])
cursor.close(); conexao.close()
