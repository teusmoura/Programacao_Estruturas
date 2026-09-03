from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_solicitacao,status FROM solicitacoes_reposicao WHERE status='PENDENTE' ORDER BY data_solicitacao")
fila=deque(cursor.fetchall()); proximo=fila.popleft()
print("Retirado da fila em memória:",proximo)
cursor.execute("SELECT status FROM solicitacoes_reposicao WHERE id_solicitacao=%s",(proximo[0],))
print("Status persistido:",cursor.fetchone()[0])
cursor.close(); conexao.close()
