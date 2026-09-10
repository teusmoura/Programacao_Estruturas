from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_origem,id_destino,distancia_km FROM rotas WHERE ativa=1")
grafo={}
for origem,destino,distancia in cursor.fetchall(): grafo.setdefault(origem,[]).append((destino,float(distancia)))
print(grafo[20])
cursor.close(); conexao.close()
