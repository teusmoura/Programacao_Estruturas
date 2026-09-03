from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("""
    SELECT s.id_solicitacao,u.nome,p.sku,s.prioridade,s.data_solicitacao
    FROM solicitacoes_reposicao s
    JOIN unidades u ON u.id_unidade=s.id_unidade
    JOIN produtos p ON p.id_produto=s.id_produto
    WHERE s.status='PENDENTE' ORDER BY s.data_solicitacao
""")
fila=deque(cursor.fetchall())
print("Próxima por chegada:",fila[0])
print("Retirada apenas da memória:",fila.popleft())
cursor.close(); conexao.close()
