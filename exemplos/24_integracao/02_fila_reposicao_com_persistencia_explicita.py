from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_solicitacao,id_unidade,id_produto FROM solicitacoes_reposicao WHERE status='PENDENTE' ORDER BY data_solicitacao")
fila=deque(cursor.fetchall()); proxima=fila.popleft()
print("Selecionada em memória:",proxima)
print("Persistir exigiria: UPDATE solicitacoes_reposicao SET status='EM_SEPARACAO' WHERE id_solicitacao =",proxima[0])
cursor.close(); conexao.close()
