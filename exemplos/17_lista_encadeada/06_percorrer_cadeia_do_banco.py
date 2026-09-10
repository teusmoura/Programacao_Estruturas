from database import criar_conexao
# criar_conexao() abre a ligação entre o programa e o banco MySQL.
conexao=criar_conexao()
# O cursor envia comandos SQL e recebe os resultados do banco.
cursor=conexao.cursor()
cursor.execute("SELECT id_etapa,nome,id_proxima_etapa FROM etapas_reposicao")
etapas={id_etapa:(nome,prox) for id_etapa,nome,prox in cursor.fetchall()}
atual=1
while atual is not None:
    nome,atual=etapas[atual]
    print(nome)
cursor.close(); conexao.close()
