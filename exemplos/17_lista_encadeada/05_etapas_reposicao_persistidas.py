from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_etapa,nome,id_proxima_etapa FROM etapas_reposicao ORDER BY id_etapa")
for etapa in cursor.fetchall(): print(etapa)
cursor.close(); conexao.close()
