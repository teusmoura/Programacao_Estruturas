from collections import deque
from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
grafo={}
for o,d in cursor.fetchall(): grafo.setdefault(o,[]).append(d)
cursor.close(); conexao.close()
fila=deque([1]); visitados={1}; ordem=[]
while fila:
    atual=fila.popleft(); ordem.append(atual)
    for v in grafo.get(atual,[]):
        if v not in visitados: visitados.add(v); fila.append(v)
print(ordem)
