from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_unidade FROM unidades ORDER BY id_unidade")
ids=[x[0] for x in cursor.fetchall()]; pos={v:i for i,v in enumerate(ids)}
matriz=[[0]*len(ids) for _ in ids]
cursor.execute("SELECT id_origem,id_destino FROM rotas WHERE ativa=1")
for o,d in cursor.fetchall(): matriz[pos[o]][pos[d]]=1
print("Unidades:",ids)
print("Primeira linha:",matriz[0])
cursor.close(); conexao.close()
