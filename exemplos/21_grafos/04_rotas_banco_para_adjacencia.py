from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_origem,id_destino,distancia_km FROM rotas WHERE ativa=1")
grafo={}
for origem,destino,distancia in cursor.fetchall(): grafo.setdefault(origem,[]).append((destino,float(distancia)))
print(grafo[20])
cursor.close(); conexao.close()
