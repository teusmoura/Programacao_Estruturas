from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_unidade FROM unidades ORDER BY id_unidade")
ids=[x[0] for x in cursor.fetchall()]; pos={v:i for i,v in enumerate(ids)}
matriz=[[0]*len(ids) for _ in ids]
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
for o,d in cursor.fetchall(): matriz[pos[o]][pos[d]]=1
print("Unidades:",ids)
print("Primeira linha:",matriz[0])
cursor.close(); conexao.close()
