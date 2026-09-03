from collections import deque
from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_unidade,nome FROM unidades"); nomes=dict(cursor.fetchall())
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1"); grafo={}
for o,d in cursor.fetchall(): grafo.setdefault(o,[]).append(d)
cursor.close(); conexao.close()
origem,destino=1,9
fila=deque([origem]); anterior={origem:None}
while fila:
    atual=fila.popleft()
    if atual==destino: break
    for v in grafo.get(atual,[]):
        if v not in anterior: anterior[v]=atual; fila.append(v)
if destino in anterior:
    caminho=[]; atual=destino
    while atual is not None: caminho.append(nomes[atual]); atual=anterior[atual]
    print(" -> ".join(reversed(caminho)))
else: print("Sem caminho")
