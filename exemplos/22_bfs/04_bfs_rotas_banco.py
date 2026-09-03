from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
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
