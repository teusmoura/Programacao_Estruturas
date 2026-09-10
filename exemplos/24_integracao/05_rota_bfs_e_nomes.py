from collections import deque
from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
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
