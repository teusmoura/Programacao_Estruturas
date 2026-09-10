from collections import deque
from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_solicitacao,id_unidade,id_produto FROM solicitacoes_reposicao WHERE status='PENDENTE' ORDER BY data_solicitacao")
fila=deque(cursor.fetchall()); proxima=fila.popleft()
print("Selecionada em memória:",proxima)
print("Persistir exigiria: UPDATE solicitacoes_reposicao SET status='EM_SEPARACAO' WHERE id_solicitacao =",proxima[0])
cursor.close(); conexao.close()
