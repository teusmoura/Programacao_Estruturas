from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor(); cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
grafo={}
for o,d in cursor.fetchall(): grafo.setdefault(o,[]).append(d)
cursor.close(); conexao.close()
visitados=set(); pilha=[1]; ordem=[]
while pilha:
    atual=pilha.pop()
    if atual in visitados: continue
    visitados.add(atual); ordem.append(atual)
    pilha.extend(reversed(grafo.get(atual,[])))
print(ordem)
