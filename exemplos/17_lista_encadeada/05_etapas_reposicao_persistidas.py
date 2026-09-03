from database import criar_conexao
conexao=criar_conexao(); cursor=conexao.cursor()
cursor.execute("SELECT id_etapa,nome,id_proxima_etapa FROM etapas_reposicao ORDER BY id_etapa")
for etapa in cursor.fetchall(): print(etapa)
cursor.close(); conexao.close()
